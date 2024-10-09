# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ec1aa22-37c3-36be-ab02-19aeb131ed9c | -4.22243 | -44.26646 | 2024-10-09 05:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0415a41-644a-397d-a284-36aff2c643a2 | -4.2218 | -44.2709 | 2024-10-09 05:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5619b928-b047-3f76-ae85-7a22b68d9841 | -4.2205 | -44.26841 | 2024-10-09 05:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de937d10-fc18-3c2b-b945-dc7d5e9dc5bf | -6.41684 | -44.59801 | 2024-10-09 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cef26403-7eb8-3c63-b6fd-b5f583b29750 | -6.41623 | -44.60263 | 2024-10-09 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cd33711-7c91-389d-bbcc-52479ec38e59 | -6.41562 | -44.5993 | 2024-10-09 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 197656d0-2c8a-31fa-adf5-652762b348cd | -6.41498 | -44.60386 | 2024-10-09 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4798ea0-f573-35a2-ad35-269da74e5fc1 | -6.25061 | -44.81607 | 2024-10-09 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e94a09e-51ca-3f72-b932-d7468106b893 | -6.13309 | -44.70063 | 2024-10-09 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ffcecb7-e5fb-3e2c-869d-4794c2990a9d | -6.01412 | -44.52363 | 2024-10-09 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b51e071-bc45-3a07-a51a-8e8db063f8bc | -6.01353 | -44.52798 | 2024-10-09 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4874ae60-5a30-33c1-a279-d84e9f8fca14 | -6.00589 | -44.62949 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a6a27d8-b45a-3f0e-a05d-0931a8157c9d | -6.00525 | -44.6342 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3df83b11-961f-3f9a-b303-6d9cb60ad2cc | -5.99985 | -44.62867 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49b56dd1-5102-318b-abb0-8870bdf80f51 | -5.99922 | -44.63328 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e72f5cd4-5a95-34e5-aaa9-4a04a930b8b6 | -5.99379 | -44.62794 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fb8638a-98b5-3b96-a1cf-5ef8570d0fc0 | -5.99317 | -44.63248 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de05c05c-509c-3c46-84c0-bea20404463a | -5.99176 | -44.62897 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e89e56dd-41ac-322a-84f3-d18f913d5586 | -5.99111 | -44.63353 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8438dc5-2f9c-31d3-8e93-5f450725f9a1 | -5.9546 | -44.58646 | 2024-10-09 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f9a1520-ecf4-304c-8e03-37f41a2c1bab | -5.8132 | -44.1221 | 2024-10-09 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| da25db90-8de1-335f-9ff1-bd0523e68fd5 | -5.8125 | -44.12711 | 2024-10-09 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c111de0f-3f20-3c90-b7ae-e415a68a702f | -5.81171 | -44.1225 | 2024-10-09 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fd0351fa-c3d3-3aff-8f57-68175ff232a0 | -5.81104 | -44.12751 | 2024-10-09 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f198892c-7e72-3141-918a-607cd8f8c7a2 | -5.58845 | -44.87606 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7ff376cb-2a52-3e48-bb7d-8e71bf9de47c | -5.58785 | -44.8803 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4e17ba84-e28d-374c-a1a0-32bddf9cd7e0 | -5.58312 | -44.8711 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ae182be1-7f2a-3549-b7a6-211150d83465 | -5.58251 | -44.87539 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d5342501-9b5d-344a-b01c-c11b119ea4d1 | -5.58192 | -44.87963 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3d66086f-3261-3cd1-b75f-05ddc6ee5dcd | -5.58133 | -44.8838 | 2024-10-09 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1cda46c5-a268-3a3a-9daf-05a86f020f3f | -6.48368 | -43.88159 | 2024-10-09 05:01:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 380c52ff-8efd-3f22-9d71-ce22a6123467 | -6.47991 | -43.8786 | 2024-10-09 05:01:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d8040e0-cbf7-3e62-8434-5930d0049bbb | -6.47926 | -43.88359 | 2024-10-09 05:01:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 172ba568-92bf-38d9-a8f8-f49de314085c | -6.16994 | -43.7081 | 2024-10-09 05:01:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c22ddc53-8c46-3638-9840-d797049e8292 | -6.16353 | -43.70718 | 2024-10-09 05:01:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b50b946-d1a8-3516-9e2b-6216b7a19b7a | -6.16282 | -43.71238 | 2024-10-09 05:01:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5debc56-49e0-3fdc-bd65-1316fa8158f5 | -5.8454 | -43.75279 | 2024-10-09 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f969d273-5728-312d-a813-a36c80c57a51 | -5.29101 | -43.40592 | 2024-10-09 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1151f954-e772-35e6-a298-7fdd60ee3aaa | -5.23485 | -43.81971 | 2024-10-09 05:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6957cff-ab9e-32d6-96fa-1c9eb00e7b12 | -5.23162 | -43.81635 | 2024-10-09 05:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efe34e73-a0ed-385d-b002-c1c97adeb2df | -5.23092 | -43.82129 | 2024-10-09 05:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b04cc90-25b4-3876-a45e-ae3e4031a8cd | -5.22857 | -43.81876 | 2024-10-09 05:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ae38f01-8e1f-3501-8b84-fb006ca29866 | -5.22464 | -43.8203 | 2024-10-09 05:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 964db9a5-0516-34b2-be53-ce1b4b2559b5 | -5.2223 | -43.81766 | 2024-10-09 05:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9834e42f-5d73-38dc-bd9a-04bba991bfee | -7.63635 | -44.82037 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0372ae9-b172-3fe6-b366-e7fef3dec79c | -7.63115 | -44.81843 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f85e50b-195b-369e-b31f-971e82dc6dfb | -7.63087 | -44.81497 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18177963-6aed-3bd6-b9f2-8de7a3b5cf12 | -7.63054 | -44.82323 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef92e831-3b65-32e8-98d0-e491418f8ab8 | -7.63017 | -44.82015 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 339dfac3-ee1a-3ed4-957b-eed313be1d33 | -7.62956 | -44.82468 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84145d72-b9be-3ae5-92b9-e6509da029f0 | -7.47107 | -43.98431 | 2024-10-09 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e13b0470-dd3e-3033-90f4-215da51e9097 | -7.30999 | -44.98164 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 437a7819-e236-3e7c-a5ac-67a224402f73 | -7.30796 | -44.98151 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 518af758-8b2f-37b8-94c2-5aaa17513bdb | -7.30734 | -44.98602 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b1d280b-3f26-3d19-bc8e-7a4203c901d6 | -7.30395 | -44.981 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 873dae25-896d-320c-8f46-962d89517d41 | -7.30338 | -44.98541 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dc2ee0a-708a-32e3-9eed-eae92d5a6c4f | -7.30134 | -44.98512 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47509f7c-564b-33b9-9db2-6750695ce634 | -7.2974 | -44.98433 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07ff2b9f-9d2b-3a9a-9ac3-8bcb9dec0629 | -7.29536 | -44.98407 | 2024-10-09 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c017170-b808-38bf-85d6-3654c8eb64f8 | -8.33452 | -44.10798 | 2024-10-09 05:01:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f56ff997-15d6-337c-a878-92a73c895dd5 | -8.32812 | -44.10685 | 2024-10-09 05:01:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0992373-42dd-344e-82ce-ad76b749e8e0 | -8.12735 | -44.41892 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 082deebd-f365-341d-8ac3-5d38f1efc118 | -8.12669 | -44.42385 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d3fc8c2-3671-33a5-8ff6-ac2773610e1f | -8.12427 | -44.4214 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c328fe53-e7c6-3319-b6dc-2db896243b09 | -8.12366 | -44.42623 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c796aba2-b0d5-3cfb-86ee-4ab15e18d41d | -8.12041 | -44.42289 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e5a6404-7989-3f46-9724-d8d07d4f2c6f | -8.11978 | -44.42764 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 724d1b63-5122-30be-938c-64a7be34d4eb | -8.00507 | -44.37288 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17711493-cd56-31f6-b4ac-a45bb3669cf5 | -8.00444 | -44.3779 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68c3d08d-a211-3b98-a1ff-b8e017f9e538 | -8.00382 | -44.38292 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f323dda-d268-3bfd-8f0a-0d97da29a316 | -8.00289 | -44.36569 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76a1e3b5-8595-3fb9-867a-73cd5f09f21c | -8.00223 | -44.37071 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35ddac5f-992b-349f-9841-576e001845f3 | -8.00157 | -44.37572 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 494d1ce6-ab70-3e85-8f23-bbb6618832c0 | -8.00091 | -44.38073 | 2024-10-09 05:01:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9bc6636-882a-318c-a559-e0db0289d699 | -4.92904 | -45.67468 | 2024-10-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10764efb-bf3a-32cb-ac4a-f5d38356c719 | -4.7377 | -45.67538 | 2024-10-09 05:01:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb4173a4-d864-345c-b4e0-7bb7ef1ea417 | -4.73212 | -45.67479 | 2024-10-09 05:01:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f9e8df5-204d-37e0-ba62-47b4d41987b3 | -4.7082 | -45.64436 | 2024-10-09 05:01:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3158970a-76c5-3342-a78f-6fecc3bee66d | -4.68657 | -45.87255 | 2024-10-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc15f742-888b-37f7-b556-384ca62a623b | -4.68605 | -45.87616 | 2024-10-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ebac3ac-6b06-3266-80c5-7395e3cf86f1 | -4.68117 | -45.87128 | 2024-10-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbdd978f-8799-3c2c-a645-cb4bc925ca6a | -4.68062 | -45.87513 | 2024-10-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98252c9c-fe39-3e46-89ba-6afcf1d3434a | -4.46208 | -45.9059 | 2024-10-09 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04f1b03b-74f2-3cd5-bfa3-e53a4f00733e | -6.34407 | -46.3322 | 2024-10-09 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 249363df-a9b5-383c-98d4-f6c2764247bd | -5.84642 | -46.23766 | 2024-10-09 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 544d785e-5303-341f-bab1-a84fa0c8629f | -5.84479 | -46.23764 | 2024-10-09 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ff6bfe0-625c-3bda-bb93-ce9e0086d03a | -5.58122 | -46.31395 | 2024-10-09 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 911ae4c6-8e60-3377-a10e-aad099846221 | -5.26156 | -46.14756 | 2024-10-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 290a51b7-2250-36f5-9b0b-3c4a565720e6 | -5.26104 | -46.15124 | 2024-10-09 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d84e9b8-e114-321b-b998-995e3c10d7ae | -5.49978 | -45.37835 | 2024-10-09 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e131a3c2-2869-30dc-a832-a6ec9ce96197 | -5.49922 | -45.38238 | 2024-10-09 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d7df565-1107-305b-8c25-bbf18a32b806 | -5.48051 | -45.51495 | 2024-10-09 05:01:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d73f1ddf-58bb-33e2-a618-57ffa08dadf3 | -5.47997 | -45.51876 | 2024-10-09 05:01:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8c4a612-4d76-3cfe-b16a-341c36558290 | -5.4543 | -45.49575 | 2024-10-09 05:01:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 585dabc1-360f-39e5-891d-770ba96a05b5 | -5.45375 | -45.49971 | 2024-10-09 05:01:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c851b1f5-824e-342b-a2c9-96732457984a | -5.32031 | -45.4829 | 2024-10-09 05:01:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea14d6b8-0180-37c8-bd4c-e5a4aae48134 | -5.31816 | -45.47956 | 2024-10-09 05:01:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3908aa2-ff67-3e9e-b822-cf7c7265bcea | -5.31759 | -45.48349 | 2024-10-09 05:01:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eaed936-40c9-3a25-9cd4-e2987adbb2ac | -5.31463 | -45.48223 | 2024-10-09 05:01:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7e49d73-a8ed-3933-a800-a23bca1031d5 | -6.94723 | -45.2259 | 2024-10-09 05:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README160.md)
