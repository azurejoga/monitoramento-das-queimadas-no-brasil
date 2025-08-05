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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46cf668d-335a-36df-be9b-1e7d5fadf866 | -10.7946 | -47.25817 | 2025-08-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 476becb3-a86c-307e-95e9-ff9182c6cf6f | -7.90391 | -45.53811 | 2025-08-05 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70fa9b4f-23d9-3d8c-b702-c844d9a70cfd | -11.49855 | -44.27131 | 2025-08-05 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d01274c4-fc05-37fa-b6c2-992a3a8ee397 | -8.23564 | -45.05486 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 573f37b8-3dde-32de-a349-cf6c290d74e9 | -11.7587 | -45.01325 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0cd3d96-76d3-3803-ac40-bb0b7c104e9e | -11.76285 | -44.96541 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa497f53-7d89-331a-9152-4265f80bd7eb | -7.21006 | -41.85316 | 2025-08-05 03:49:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 889e55cc-a6bf-3ce4-b556-f050d97733d2 | -7.53425 | -44.86901 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9211b984-d1d3-3fa5-ab2b-cb85c74738c3 | -7.71371 | -43.90727 | 2025-08-05 03:49:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40cf2873-32f5-3c3c-9cf1-e4f1853fa1c1 | -8.84872 | -47.61478 | 2025-08-05 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9ea520d6-3255-3c59-a9bf-f348b89e2edb | -11.74969 | -45.01167 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8cba37c-6320-3904-8f5c-3c009bf479de | -11.27773 | -44.64394 | 2025-08-05 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e23248c6-f61c-310a-960a-709ab8e67aa4 | -7.36295 | -43.71685 | 2025-08-05 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a999b8e3-e7be-39a8-bcd2-cf6c244f0f69 | -7.34456 | -44.68242 | 2025-08-05 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e42d83e5-2d26-3fba-a6d2-f7363159f5fd | -8.25887 | -45.06076 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17dc12f6-88af-3540-acd5-c82a394642a4 | -7.53907 | -44.86971 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95e8e71a-f5da-3429-a849-4c2b54b78eb7 | -7.56739 | -44.90362 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b3cd95b-ee44-3964-97cd-b0f055d3f8ee | -11.75351 | -47.54643 | 2025-08-05 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02c2506d-6f69-3e78-be4b-8e86fa58240c | -8.26834 | -45.06599 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af3eadfa-44a3-36d4-b8d0-5000bacbb18f | -11.78919 | -44.99901 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9a39b99e-1d3a-35ad-a5e9-3685e5c68cb0 | -8.7171 | -46.43614 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a02a39f9-cebe-3d04-b76a-5dfb808649fb | -10.91234 | -48.35875 | 2025-08-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49b7d603-c765-3af7-b79a-86982c100af3 | -10.47436 | -44.37542 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2315487-1596-3b84-a349-0040432dbef3 | -5.98686 | -49.91681 | 2025-08-05 03:49:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1e59e718-252e-31d7-be4b-ddcc0ff8ca4e | -12.52095 | -47.18656 | 2025-08-05 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f25b1a96-a77c-3a43-954a-684ccc6167a5 | -8.87856 | -44.79415 | 2025-08-05 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1584c694-590b-3cee-a2fe-cfef6355efef | -11.77018 | -44.97602 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 944f8f7b-6f29-3a0a-9438-17e8189bedc8 | -8.93707 | -46.73987 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b6f47c39-d50d-3447-9116-af58fc71b665 | -8.22604 | -45.0532 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15e0e59b-dc6f-3c35-9e95-f357b98d2af8 | -7.21755 | -44.47989 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec3e1a7d-d9e3-3443-809a-3ef223e3d057 | -7.99376 | -43.14946 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6e6ca392-ef2e-3ad3-b3ff-b2e13d80fe1b | -9.29623 | -40.2467 | 2025-08-05 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 73bc1d41-f215-3a07-abfe-38f9d57789af | -11.92075 | -44.95008 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a549c661-f96e-3a57-af2b-57eb0c2591eb | -12.72711 | -46.39328 | 2025-08-05 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58d4b76d-47ec-33e4-b1ad-13d5d2a251b8 | -12.68508 | -48.12436 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb7a3ce4-fed6-39c8-9503-f0f5e8d9bd77 | -11.91834 | -44.96343 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 16f44f12-ee49-3449-b907-ede71a252804 | -7.11783 | -47.84212 | 2025-08-05 03:49:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| edde7b2e-c06c-37de-b1b3-0a1d37555b1a | -7.34065 | -44.67666 | 2025-08-05 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf3cbba2-7a81-3076-8660-51d57471d33b | -10.34584 | -44.90593 | 2025-08-05 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a39cb27-9480-3acf-a0e0-e346c77e363e | -6.70363 | -44.09613 | 2025-08-05 03:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae36751a-5080-3bd1-8b6b-a5816ca65b91 | -12.05945 | -40.00933 | 2025-08-05 03:49:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bcda3284-291a-3524-b59d-33d57c70f89c | -10.47956 | -44.37176 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5c6180a-3820-38a1-9bac-1eb819f5de6e | -8.24912 | -45.06273 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c1a94c1-45e1-3964-a95b-23c48fc63bfd | -7.56632 | -44.8816 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9626622f-a6ce-321d-ac98-01a951f829ce | -6.4675 | -43.02715 | 2025-08-05 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62060a46-d8cd-36e9-8a98-da364552df1c | -10.78242 | -45.50682 | 2025-08-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14edb6b8-830c-347e-9ab6-90868730dafc | -7.39048 | -44.64822 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| caa9284e-7e90-3d4a-b189-aa9b237c5e41 | -7.76173 | -45.23083 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9e11a9aa-565a-3ebd-a4c0-fb669cfa7f2f | -8.95359 | -46.73953 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c104c5f1-aa39-3515-ba4f-e662cc7f73d3 | -10.90973 | -48.36301 | 2025-08-05 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eaac0549-1578-3c7b-8b66-2276e55b1aa3 | -10.79989 | -47.25932 | 2025-08-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9a5ea51-41e2-355d-91e7-7f91d0e80a44 | -9.61998 | -48.49215 | 2025-08-05 03:49:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 277968f3-af3c-3486-b9be-0e02b2859f48 | -7.14089 | -44.07793 | 2025-08-05 03:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2b69090-2bf6-3e84-970f-3cf32b0cc2b4 | -8.38902 | -46.54738 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a78b8efa-f75a-35e2-9214-c2e0bfef22f9 | -12.68677 | -48.1214 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34c1b691-fa8c-3fcc-815d-f8f7172dc6ca | -7.90892 | -45.53887 | 2025-08-05 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| daa75ef0-2c17-3412-90f5-ea248c51281a | -10.33263 | -47.82891 | 2025-08-05 03:49:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a3e63489-8039-3f81-9205-43b6ba59151e | -8.95419 | -46.73627 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 56eea11c-ae76-3797-aa81-14c09436bebe | -7.05647 | -47.46217 | 2025-08-05 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ee1dd72-a646-375d-97cd-387a4765daba | -12.70063 | -48.07985 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1199e142-99f0-3791-a2a0-d1cd382a2b00 | -8.22992 | -45.05933 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3d9d3fc-08cd-3475-920c-b4dead6447d5 | -7.85542 | -46.73867 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d11916f-cb16-36ff-a804-b42c6542bad8 | -10.44643 | -44.38182 | 2025-08-05 03:49:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa966e0e-5a03-3b96-97ce-8f74e02a29b0 | -12.95073 | -48.25564 | 2025-08-05 03:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d59e322b-8803-3fe8-8fc1-ef97ddbb6a48 | -9.40177 | -45.50496 | 2025-08-05 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 64192077-c920-35bc-bac5-01d9d6e746aa | -6.93002 | -43.34039 | 2025-08-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a29a9b4-9354-3b92-9261-121cce5b0996 | -12.22522 | -44.19806 | 2025-08-05 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 619d54fa-107c-3a81-a7a9-1899e0f27ac3 | -7.08622 | -44.36219 | 2025-08-05 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b48e65e-bcba-3fe5-ae8d-c5d3d429a263 | -11.75168 | -44.96451 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6289fc7-e264-3ffb-ae7e-18aca209c9fe | -7.39218 | -44.63852 | 2025-08-05 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38733853-ba5e-324d-a068-81b726856eee | -8.26354 | -45.06516 | 2025-08-05 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92eee1ba-91e3-3dd8-9fbb-363a4ee45846 | -11.15388 | -49.70348 | 2025-08-05 03:49:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b497df3a-4332-332d-804f-db753a6e5f2d | -8.84942 | -47.61095 | 2025-08-05 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 56421c84-bf1b-320d-b0b7-0ca7df9b1890 | -8.01935 | -43.17863 | 2025-08-05 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b242aa45-97e6-3cfd-85ba-08a89ca07194 | -11.74691 | -45.00153 | 2025-08-05 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c681dd14-8fc2-34e8-833e-69dca986f252 | -7.60488 | -45.30487 | 2025-08-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8cddfb94-5999-3004-90a1-cdcef14c9a7f | -8.95238 | -46.74607 | 2025-08-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| acad802b-d97f-3193-9799-077f46539430 | -12.68032 | -48.11975 | 2025-08-05 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ba9669f-a233-383e-ad1b-476b52164a91 | -11.9207 | -44.9525 | 2025-08-05 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f968542c-ca5a-3dbc-ac25-d5f35e15f3b3 | -8.9478 | -46.7354 | 2025-08-05 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| a78ee570-1df3-3972-8742-070d85f87b62 | -8.9228 | -60.5376 | 2025-08-05 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 32f14221-b889-363d-b149-24d8c1aef9ca | -7.994 | -43.1534 | 2025-08-05 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| f19d213d-4634-32c8-ab3e-a23c20322f24 | -13.0723 | -56.9131 | 2025-08-05 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 67b01f8a-db09-3a29-aa5d-8aecbd3e897e | -13.0538 | -56.8746 | 2025-08-05 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a3d93f42-b423-3841-af32-b034fdc5c051 | -13.0726 | -56.893 | 2025-08-05 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 9f6d2db5-1b05-354f-9034-a85adf7b3240 | -13.0914 | -56.9114 | 2025-08-05 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7356a243-85d1-308a-b195-076b7c21da96 | -17.2056 | -44.8214 | 2025-08-05 03:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 77f054ce-426a-345e-8c88-d28f899e816b | -8.9227 | -60.5568 | 2025-08-05 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c833dad7-58d8-37d2-bff8-347f5ef168d1 | -17.2256 | -44.817 | 2025-08-05 03:50:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b5e366dd-98b2-3ec7-8aab-104f2a66e94d | -18.85295 | -40.45538 | 2025-08-05 03:51:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4797fc44-9a5a-3f4c-96d4-9429bb5b664b | -14.37705 | -50.3301 | 2025-08-05 03:51:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5e264fc-c4af-3839-92d9-0ef8fa61a09d | -18.85627 | -40.45596 | 2025-08-05 03:51:00 | NOAA-21 | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5b514dc0-9a13-3ab5-bd3a-2724b9d46a3f | -16.08293 | -43.62823 | 2025-08-05 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7525712d-8062-34cb-b245-fafb0b6d772c | -17.22076 | -44.83399 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 50c9cfd1-aacd-3265-b894-99de44291a78 | -17.21866 | -44.82241 | 2025-08-05 03:51:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf57a335-2ae1-390a-936c-707fe458203e | -17.59546 | -43.19783 | 2025-08-05 03:51:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45f75fd9-3847-304d-b8e8-ec7e75ccf4b7 | -17.36287 | -46.0915 | 2025-08-05 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa731a6a-593d-3031-91fe-ef4833b23cde | -15.39084 | -40.84198 | 2025-08-05 03:51:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cb3a047b-18e6-3e81-a89e-b00d4a9854fa | -17.35938 | -46.08604 | 2025-08-05 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06e09bab-0e8e-36c7-82a2-c88f21b29443 | -18.92781 | -42.08746 | 2025-08-05 03:51:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |


[Clique aqui para ver as próximas entradas](README12.md)
