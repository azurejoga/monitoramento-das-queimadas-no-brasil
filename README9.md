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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea38aebc-56b3-34f9-a826-a5ca046c3c4c | -3.1223 | -53.7598 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0138169-43e1-30dc-83c3-3f982beef460 | -11.6987 | -43.512901 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b11f47fd-ed48-3447-ad0f-23b9f072d762 | 1.7983 | -55.590599 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeda0805-b69f-39d1-9c17-74d050229e19 | -2.8842 | -45.4091 | 2026-10-03 00:52:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c84ca2e4-3561-32b1-b50f-f41323435506 | -1.2623 | -54.551399 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31fd3397-a9e0-3c13-b96d-6e874a8ae8eb | -6.0648 | -53.468399 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f7fc258-8f26-33b9-8502-c70b9d40b50e | 0.6254 | -54.413601 | 2026-10-03 00:52:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9814264-56e1-3965-b250-26e23205a6d4 | -11.6442 | -43.5424 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 235005c2-39ba-3e30-a3d1-fe538c2cb768 | -11.4464 | -43.374699 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8fcb02d3-85fe-3802-97d6-9d85afa1d3a3 | -11.7085 | -43.5103 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6ac0eb-7842-364a-897b-536a2f1b3e10 | -3.7181 | -50.6577 | 2026-10-03 00:52:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20b74819-c43b-3d97-a009-3bf2fde33089 | -2.8975 | -45.4217 | 2026-10-03 00:52:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6581c6c-98eb-38a5-a5fe-a9cb9ed77bc5 | -6.7497 | -44.1413 | 2026-10-03 00:52:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05c0f7c7-9048-338d-8ea0-0c02e5e38ff2 | -11.7286 | -43.4272 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21a5bc41-1a3f-3b5f-bf59-52a253f110c2 | -12.9599 | -41.1693 | 2026-10-03 00:52:00 | METOP-C | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9d77e021-c04b-3bce-a6cd-6ec11595f04e | -12.8649 | -44.688499 | 2026-10-03 00:52:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 488c8af8-11cd-32c7-9084-e9db1287a54e | -5.9447 | -43.631901 | 2026-10-03 00:52:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a27fdf9c-aac8-3679-a93b-b08c70e280e3 | -4.4132 | -49.9646 | 2026-10-03 00:52:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d3c2c8a-8aff-32bc-989a-87f52897fbca | -3.6986 | -50.974201 | 2026-10-03 00:52:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11532f57-4040-3a70-bb34-2f4e1683844a | -3.1227 | -48.679901 | 2026-10-03 00:52:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5d59009-ad4d-322b-b0ef-feb3fe8d6514 | -15.3095 | -42.776001 | 2026-10-03 00:52:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8ae3dc45-4b4d-3136-9cf8-e8d5139eebbe | -9.6661 | -40.574299 | 2026-10-03 00:52:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3722d340-8ee9-3669-ad0b-1ee4b2c96be5 | -2.8922 | -54.151199 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14aa84c3-95c3-3eb8-92ae-0431310ed009 | -4.4176 | -55.7463 | 2026-10-03 00:52:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65360596-5a17-33f5-bfb6-4049706d2f1a | -5.6221 | -44.366699 | 2026-10-03 00:52:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3657437a-a792-325c-9c72-161563cebbdc | -4.3558 | -43.809799 | 2026-10-03 00:52:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07bf2181-b3d0-3b47-83aa-c696a02ba2cb | -4.8442 | -43.042 | 2026-10-03 00:52:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b8d42b0-f620-37d4-a6ba-ec6c69b72a02 | -3.4154 | -52.833599 | 2026-10-03 00:52:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59ec5fbd-9382-3d6d-a468-8f66d135f429 | -0.9026 | -47.903198 | 2026-10-03 00:52:00 | METOP-C | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80f3241a-91d0-3c9c-a1d8-4ac687f38bae | -3.9128 | -54.425098 | 2026-10-03 00:52:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fccab1e8-ecfa-3e0b-8b46-33cb2ef28824 | -11.7421 | -43.439301 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02e76b72-be1b-37ef-be82-bcea9ed09337 | -10.9817 | -59.105801 | 2026-10-03 00:52:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e6e104a-0f62-3ef1-a354-d77f22f4ffb8 | -11.803 | -43.516399 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a50841fa-65ac-349f-a9e3-8c8444b4438f | -5.9491 | -43.649502 | 2026-10-03 00:52:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46a4e494-ea29-3b1b-b6f6-7d29a18c1212 | -3.1191 | -53.745899 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c50a0d86-ee83-383a-bccf-c41ce44fa472 | -0.9148 | -47.9118 | 2026-10-03 00:52:00 | METOP-C | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2773b5de-176d-339f-a0bf-386a856907d7 | -2.8889 | -54.137001 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38db27a0-731d-3e29-a224-bbe23a8025f3 | -10.9949 | -59.121201 | 2026-10-03 00:52:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 078a6f2a-3ea3-329b-b240-2b57c2cb7efb | -11.6479 | -43.5569 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2cc03332-d6ac-3f9b-ab5c-52c9c328789e | -4.7915 | -55.7178 | 2026-10-03 00:52:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9d674bd-400b-3ccd-b8b1-4da90a9a8ccf | -4.3603 | -43.8279 | 2026-10-03 00:52:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d417586-da89-372c-9ec7-872e4da6c445 | -3.2441 | -54.519501 | 2026-10-03 00:52:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95141389-7020-3f61-a827-e674a403c4bf | -5.8492 | -53.471298 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68c43468-ab0a-330e-9d3d-fbc6bdc5f0bc | -4.7481 | -43.275799 | 2026-10-03 00:52:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8e4a848-8782-3391-b8cb-c9acdb92f293 | -4.5607 | -46.571301 | 2026-10-03 00:52:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3bcafed5-d25b-3043-8b00-4ec3336693c7 | -2.966 | -53.257301 | 2026-10-03 00:52:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e35e08a1-8b95-33fc-b7f6-33b23837ce10 | -6.019 | -53.5387 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b74af4ba-2023-36c0-9a6e-f0d1f47aad3e | -6.2026 | -53.2584 | 2026-10-03 00:52:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 323d9873-0116-3d55-91a2-6ae7ee2e7d6e | -10.9096 | -43.824699 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4557799c-55aa-33e9-ae98-f9d14abb5803 | -2.4074 | -56.814602 | 2026-10-03 00:52:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57abdbbd-3d46-3184-9d27-f0f49b7620a7 | -6.0632 | -53.4613 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e1d35f7-5394-391f-9c79-5efda1b8dbe3 | 1.7834 | -55.610298 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4853f7b-c6c4-38ff-8fa1-70b293095de2 | -3.1734 | -54.0737 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60efee96-6c16-37c7-80c2-96197d76f99b | -1.0417 | -49.210899 | 2026-10-03 00:52:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6da218cf-debf-30ea-9ac4-da24cea02237 | -1.0874 | -54.103699 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab43a1a3-5605-3c8e-bc39-4bad2fbb12ae | -4.4274 | -55.744202 | 2026-10-03 00:52:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e53006e-a4f7-30fa-af4d-b8ff28c73069 | -5.9534 | -43.667099 | 2026-10-03 00:52:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14bad1d0-5ffd-3e08-b91d-c4ad3548c9be | -4.4508 | -47.928799 | 2026-10-03 00:52:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9c6862c-dbb5-3d92-ac6c-e4132069c137 | -6.7142 | -45.9715 | 2026-10-03 00:52:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07c4d7c5-8830-32d3-81a2-d59afd771856 | -11.8201 | -43.542702 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9123f0c8-b266-3906-84b1-f7a7352cd726 | -5.8508 | -53.478401 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95533961-0d30-30ee-a1af-cac30e74f5d0 | -2.541 | -57.403099 | 2026-10-03 00:52:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2a52f2c-164b-3c41-9f41-f3ae9e4d90a9 | 1.8 | -55.583401 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 930f8fa0-79e8-38be-ac93-cba6c1d12a08 | -5.626 | -44.382599 | 2026-10-03 00:52:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4edc5c15-755f-3319-a996-943c4fc54cc1 | -4.7335 | -43.258598 | 2026-10-03 00:52:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a40f3ec1-4c3d-3902-b3d4-4adad9b6829e | -1.0792 | -54.1129 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e05174f8-267f-36ea-95ca-ba468469ae14 | -4.1185 | -55.013699 | 2026-10-03 00:52:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88b8f112-995a-3819-86c3-862244c71c8e | -11.7971 | -43.533298 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18d251e8-3bd3-37c4-9b94-e74d0852b1d9 | -10.9291 | -43.819698 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c71a265c-bd23-35ff-b28f-b657c7225dc7 | -5.7398 | -45.142601 | 2026-10-03 00:52:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ad9363f-3f3f-34f1-8f15-971203257364 | -4.2634 | -50.7402 | 2026-10-03 00:52:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e80cc1d2-5f71-3976-abba-6e9bfb9717be | -1.1427 | -54.164501 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 031b65e9-984d-3115-b3e7-fd45e9940e0c | -11.4966 | -43.409199 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 124f843d-378d-3a0c-8db6-6d0c7e4a646e | -3.6421 | -55.5009 | 2026-10-03 00:52:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9e21dd-4bdb-308e-bae1-0055fd84174a | 1.7918 | -55.573898 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7868e34b-e3d7-3966-877c-03373129c23d | -10.9852 | -59.1231 | 2026-10-03 00:52:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce5f6f3f-e52b-3fb2-8755-d59f801d4935 | -12.9555 | -41.191799 | 2026-10-03 00:52:00 | METOP-C | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 61857210-e098-31f9-8b75-22e964cdef84 | -11.427 | -43.3797 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0508486-89cc-3623-9201-2025e9a7decb | -11.4696 | -43.384499 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e30b45f-73f6-307f-9aff-3fd536985f96 | -4.8148 | -49.872799 | 2026-10-03 00:52:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93b5857a-0fc2-3774-a915-315273570dc4 | -5.7529 | -45.154202 | 2026-10-03 00:52:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b196cfc8-82b1-3332-9bc3-4751d9dbb100 | -1.2754 | -54.5634 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03ff0f12-935c-3404-ad52-6384ab54e04d | -3.0074 | -53.888302 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbff6d43-5826-3acc-b4d2-76e3adb1dfc8 | -3.2273 | -54.3097 | 2026-10-03 00:52:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96d3a659-4479-3561-a0da-b5e232746b41 | -2.8598 | -49.6287 | 2026-10-03 00:52:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31b284fc-5d8d-3852-8909-19da6ee9076c | -4.1807 | -48.663502 | 2026-10-03 00:52:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb550aa-2e2d-3268-9bfb-715caf504e6c | -6.08 | -53.307999 | 2026-10-03 00:52:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3560117e-70e8-3f7a-9d6f-18dc2656be05 | -11.8521 | -44.734798 | 2026-10-03 00:52:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fb38531-fa2a-3fbd-ba8d-dc01378316fc | -5.7241 | -43.2808 | 2026-10-03 00:52:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce0264c0-3695-36ee-aa06-ee0b3bf839c3 | -6.7439 | -44.1595 | 2026-10-03 00:52:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 914626bd-8393-3c7d-a9fc-8ed68740af59 | -2.7477 | -51.546501 | 2026-10-03 00:52:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2840755-951e-3689-b30d-6571090654e5 | 1.9197 | -55.7794 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09496023-3e0c-3f0e-8527-389371219bf8 | -11.7242 | -43.490799 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| abf3abea-7b9c-3a52-848d-5e89d9776415 | -4.2748 | -50.745201 | 2026-10-03 00:52:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24ddfcd9-3160-33b7-917b-d7ae69357ef8 | -2.9201 | -54.0928 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24fe463e-cd72-35a9-8612-69b4a8a45ccf | -2.8857 | -54.122799 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7aaa862-2299-3e60-9cbf-cb9b9ac77cb7 | -3.0188 | -53.8932 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27044959-80f5-3bf2-9626-bc0dc579a3b1 | -4.4034 | -49.9669 | 2026-10-03 00:52:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69797027-bfc7-3b12-a9c3-865bd09ff4dd | -3.1355 | -53.727501 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b249282c-3861-3573-a037-6be33c13cf83 | -11.7204 | -43.4762 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
