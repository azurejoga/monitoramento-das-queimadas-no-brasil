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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 090aaf0e-f137-302b-b219-8b0ac55c4557 | -14.14139 | -51.12903 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6969c5ee-b888-31bc-94ba-d9d9862603e4 | -18.8962 | -43.81048 | 2026-10-01 04:36:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2b29b1f-ba73-3824-8e05-fe721c885ace | -18.27751 | -42.18383 | 2026-10-01 04:36:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7a0c5e11-2a25-3f1c-ad2a-d3d545cbf03d | -14.87292 | -51.85273 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ea91141-1249-30c0-a831-66aa2cdb20cf | -15.77657 | -46.03239 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 26a6617b-ce98-314d-9b3a-60a2519283f0 | -14.48968 | -48.30888 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76ba456d-eff1-3af8-b5ea-ae9791455d5e | -20.38371 | -47.18337 | 2026-10-01 04:36:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81f7e9d7-359e-3ced-8ce8-7ec282225509 | -14.40283 | -51.25261 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5ba15f61-9da2-3500-b8ed-8dedc95d15ac | -16.28702 | -48.01793 | 2026-10-01 04:36:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92c41a87-b568-38b7-9f5b-f42365eaa1a2 | -14.48362 | -48.30423 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1994c633-1bdf-3a2d-8357-ed37e4ebd5d8 | -16.02714 | -45.13027 | 2026-10-01 04:36:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e08cdc8-d631-3a07-8e78-c5f12c5821b2 | -14.4028 | -51.27398 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35b557bc-e145-3576-80a6-2cefffcc1e16 | -13.6586 | -53.93726 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3b4afb7f-6305-3b50-b099-33b2dbfcad0d | -15.49896 | -46.12449 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| add5da3e-750f-3cf6-8c30-0f9c1ddf29d8 | -15.64878 | -44.71597 | 2026-10-01 04:36:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b87b65b-0fe3-37b7-a045-5b246e446ce2 | -15.44416 | -45.68631 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddb1dd22-ed13-34c3-a354-328e6a5990eb | -17.30908 | -41.83828 | 2026-10-01 04:36:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6d065130-da38-3f9b-be2a-36c79471d48c | -15.63914 | -40.99255 | 2026-10-01 04:36:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b84d1cb0-468b-3e37-a636-74234a850401 | -17.24785 | -43.88291 | 2026-10-01 04:36:00 | NOAA-20 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9230ac16-8970-3161-ab1d-581d961d70fa | -17.00093 | -45.46874 | 2026-10-01 04:36:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 196dcfc4-7ca3-30e2-8908-f2273840cf0c | -14.3928 | -51.28931 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a95dad1-cab9-3788-b18b-e5591c7eccdf | -14.39878 | -51.26189 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 29f6fbcd-4c55-3a4c-945a-17322fa19c5a | -15.95818 | -45.97228 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 262cb809-8b10-3525-9164-e14ab0eea5c7 | -16.65179 | -51.70885 | 2026-10-01 04:36:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09599830-4130-34e6-85a2-40f340549d2b | -18.16498 | -46.85665 | 2026-10-01 04:36:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97535980-759e-3e98-9509-e4d26614f505 | -16.67432 | -41.84949 | 2026-10-01 04:36:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 74d7169f-9e4d-3a84-ae19-c4825ed4de2e | -15.45022 | -42.10083 | 2026-10-01 04:36:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9f400120-e588-3eee-ab57-6d96f090510f | -13.66552 | -53.94692 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c47ad12f-a88b-367b-bf46-cead976855c2 | -15.30808 | -42.77777 | 2026-10-01 04:36:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 05963b33-7025-3d5b-9b0b-1185be16be40 | -15.64131 | -44.71484 | 2026-10-01 04:36:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 871dcc08-1c71-3a92-9d24-3482cf477bd1 | -15.30853 | -42.77443 | 2026-10-01 04:36:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf8f8068-6efd-36b0-9c6f-458167d7e6ad | -13.66897 | -53.95178 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8344992b-4797-3e83-b747-ffddad47c744 | -14.40567 | -51.25739 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d95b634-cdb5-387f-851d-ce41a89d3602 | -16.42419 | -47.18816 | 2026-10-01 04:36:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3e52ea14-bb2a-337f-ae84-e6421bc46297 | -14.42843 | -51.25295 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a606e20-5219-32af-92f4-b414f0d705e4 | -13.65093 | -53.93183 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 43942192-8111-3a97-b540-dc9478d8f5a9 | -13.66479 | -53.95095 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcc185bc-a2f0-34cf-b0e8-d1c7fc267154 | -14.14992 | -51.14331 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c136be1-862d-3f9c-b8dc-2b164f0c9878 | -14.48306 | -48.30778 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76322623-cf73-3e81-b5f9-cb2f03375edc | -17.88018 | -44.30875 | 2026-10-01 04:36:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c100306-1b88-3d7f-8067-68d586232fe4 | -14.14353 | -51.13791 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| acc0cb46-784b-3b66-9b2c-27d953a2f6b1 | -19.33983 | -41.45587 | 2026-10-01 04:36:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 089a8d58-62f5-3826-ad92-271ae39a069e | -14.42055 | -51.3201 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 275dfe93-67b3-3d63-a862-efabc7972b41 | -20.18889 | -50.89896 | 2026-10-01 04:36:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 12ad2aeb-f312-3832-87a7-45c0956875cc | -14.89444 | -52.89514 | 2026-10-01 04:36:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e076ff7-aca8-3919-9597-d356c27a4d1e | -14.3964 | -51.26855 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 055be219-a8a2-3a0c-b9dd-9e270beb9cc1 | -18.51206 | -45.14304 | 2026-10-01 04:36:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f800955-36b0-3cfb-9e81-8a10176992d0 | -14.38924 | -51.28867 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ad29730-38b4-3def-b7e2-e5e699e4980a | -14.88655 | -51.88232 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4b66e90e-b8b8-3ae8-9cf0-9b04fc085b0e | -16.52178 | -46.86417 | 2026-10-01 04:36:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86928dd7-048b-3f95-b6e5-1d622427b6e1 | -15.16001 | -46.12315 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6c90c33c-df41-3ff0-a06a-d6506e730caa | -15.63992 | -44.71705 | 2026-10-01 04:36:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66adee7c-f682-3854-92e7-49fa0eb0cbdd | -16.01918 | -45.13363 | 2026-10-01 04:36:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7aac1bc2-e875-3410-abbd-e915ab7f2b1e | -15.16348 | -46.1237 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fa66359-fae2-3b26-9579-cf2d67013a67 | -17.30878 | -41.83904 | 2026-10-01 04:36:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 29c4565b-2867-3e93-a7e6-9f3b8c49c0d2 | -14.39429 | -51.25961 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| de83ea91-8881-3398-a803-8495bb2fdbfe | -14.86641 | -51.84701 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75071bb0-06b3-323b-aa80-7e2d8de78306 | -20.18548 | -47.40332 | 2026-10-01 04:36:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b26ca6b2-1ad7-3d8f-9034-a098a2ecccd8 | -13.65369 | -53.94044 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 06a26fc0-8ea5-39a8-9bb4-e381553908fc | -15.49547 | -46.12402 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1499f356-1df5-357a-9e52-7f0539efba5f | -14.49355 | -48.30588 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20b23c8f-6579-3d5c-aba2-7873a15af91e | -16.22334 | -43.6202 | 2026-10-01 04:36:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83a2a883-2e28-3cf7-8caa-2e9fd674b8a0 | -13.64601 | -53.93502 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ad704bba-9cc4-3c8d-a167-dd2d7305cfee | -15.50594 | -46.1496 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbcb95aa-2944-381c-80e2-34087ce39897 | -15.23584 | -46.1501 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc280c4b-7a6a-3bef-8c11-4c1e8b89c3dd | -15.23641 | -46.14626 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0bca50e-1b3a-38db-9810-7668d3673513 | -16.52577 | -46.86087 | 2026-10-01 04:36:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50a6f6a0-1c60-34fe-952b-003465f5e219 | -14.4014 | -51.26089 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d45ffce-5471-307b-bb93-45f80abf7f5b | -15.77715 | -46.02835 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4382dd4-9d6a-3788-85c1-e63e84f3d293 | -14.88215 | -51.88604 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b3c7ab15-8e89-3122-907f-a1e5beb34047 | -14.15347 | -51.14395 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 53f56c53-c94a-399a-9ff0-e7b17fbaff4b | -13.64037 | -53.94219 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4aa3c72-bf6b-3e60-87bf-f9a9463589a4 | -16.13259 | -43.73976 | 2026-10-01 04:36:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7447c79-19b6-3841-a8c6-039ef9c665a1 | -15.30428 | -42.77429 | 2026-10-01 04:36:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8260922b-d046-3612-b873-50e8d752b6b4 | -14.86201 | -51.8507 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f23d8cbf-4069-3c3c-96ba-dfed4ee6185b | -14.15767 | -51.11924 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1192248-310c-3849-84dc-b2210fa61269 | -13.65931 | -53.93335 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4bc9f3d0-2e4d-38b9-ac51-a0e85a3b9c1c | -15.50537 | -46.15348 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5110f16b-7498-3c93-8ff0-5696c816a1d6 | -14.40995 | -51.25389 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c7d32e8-2031-3284-954d-d41ca67e9263 | -17.21712 | -46.84291 | 2026-10-01 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f23476e-2ee5-369d-bef7-e68ce5b08fbd | -14.39784 | -51.26025 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| fb3df18a-ac79-33b9-8b9a-2a0c66d656c8 | -14.86852 | -51.85643 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a6579bb2-e33b-3ebb-8353-c3245a6cbe10 | -15.2098 | -46.14685 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e85a124-199b-3c42-bed2-f807dcfbb31e | -14.15702 | -51.14458 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7e7a36d5-9fd8-3962-90ae-2b33b95de76c | -14.15058 | -51.11797 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc830296-acfb-36ea-b7cd-a57c93979dd7 | -15.44771 | -45.68688 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cfdfab8-919c-3b39-a22a-f2028c4d06d0 | -19.83798 | -45.01605 | 2026-10-01 04:36:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e872f3f7-1229-3c63-bad3-54d79f08ce1c | -20.18893 | -47.40392 | 2026-10-01 04:36:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8109b194-ca5a-36f8-bf74-98e7f55f0898 | -14.39285 | -51.26791 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 47d95b0b-d1ec-3ffc-bf02-6ae27f5b3003 | -14.39924 | -51.27334 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1a63250-1c73-32f8-8d40-23dabc53b4ac | -14.41848 | -51.24689 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a00c954d-dc6e-36e4-b2ac-2962ac436e2f | -18.06784 | -44.5192 | 2026-10-01 04:36:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d3032ccc-6613-3be6-bd04-2c157f545e77 | -14.43838 | -51.25902 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2cddf50f-2d6c-37e9-b357-9247d4fab163 | -14.89019 | -51.883 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c3e84f2a-be88-37e0-981b-a7bb6a282661 | -18.06647 | -44.52948 | 2026-10-01 04:36:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 73dc1544-31d5-3e20-86d0-9893c0571990 | -18.48747 | -45.12498 | 2026-10-01 04:36:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38e30aa2-3dd5-3e15-bca6-76ad2195a20f | -14.39996 | -51.26919 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 045d47d9-8bda-37f1-b96e-e43f568a166b | -20.18491 | -47.40722 | 2026-10-01 04:36:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b6e90212-bc74-3124-8d58-addf4f3bff91 | -14.15063 | -51.13919 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1b1ae5de-f376-3e07-af8d-1feed7715dc9 | -13.65022 | -53.93573 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README68.md)
