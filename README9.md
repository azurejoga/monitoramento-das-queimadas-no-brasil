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
| 204a04c0-d40e-3bd2-a8aa-688df9de5a2e | -8.01146 | -46.89393 | 2025-06-02 12:42:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9f17cb84-86fe-3608-b0e9-4461002b423f | -8.26539 | -49.88483 | 2025-06-02 12:42:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| e92c1f66-20fd-347d-81c5-b4fee51efc59 | -8.01325 | -46.88044 | 2025-06-02 12:42:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| fb563f7f-325f-38f0-9efc-72ce694423e2 | -9.37914 | -48.41751 | 2025-06-02 12:44:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0b9a80b8-8aa6-3c6a-94b8-5c82d5e1d588 | -18.074 | -48.33805 | 2025-06-02 12:44:00 | TERRA_M-T | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 84ad541f-c43e-3834-aef5-502a26d83b56 | -9.34413 | -48.37826 | 2025-06-02 12:44:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c6c99dc7-39f4-31b7-971a-6b8dc3068c03 | -10.24314 | -47.61025 | 2025-06-02 12:44:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 9b9b9faa-8e74-3d79-ad69-3ac833da31d0 | -11.91832 | -54.83071 | 2025-06-02 12:44:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e9131202-fd33-3623-9189-fba8c8d7a80d | -17.66133 | -50.71326 | 2025-06-02 12:44:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72ef5b1f-5b75-3eff-85d9-8ecbaa002f33 | -10.02387 | -46.57943 | 2025-06-02 12:44:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d682e827-1a21-3d14-86b8-ba9421d83fd2 | -10.97566 | -42.18261 | 2025-06-02 12:44:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 4f5824a0-fc9a-3682-998a-f5e6c7813840 | -10.2414 | -47.62334 | 2025-06-02 12:44:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5cc4cfcf-e614-309d-b3db-b305832a1f00 | -11.27022 | -52.46594 | 2025-06-02 12:44:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8d603734-200b-3cb8-8f5d-24d0fafdba90 | -13.89988 | -51.93047 | 2025-06-02 12:44:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cee7a0ba-060d-352c-97a9-fc204aaade0f | -9.26852 | -49.95762 | 2025-06-02 12:44:00 | TERRA_M-T | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d77de9a5-0d21-38e2-a9ab-a8d7c0ac9c42 | -8.60403 | -51.57578 | 2025-06-02 12:44:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 179.4 |
| 88cf4371-f5c1-3208-adc9-8c5714ddbdc2 | -13.3659 | -54.25818 | 2025-06-02 12:44:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2f2a57eb-9e9d-30e4-89e3-3c0abf775323 | -14.65623 | -45.39299 | 2025-06-02 12:44:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| f3f5ab58-9ce5-312d-81e6-384bfe9c998b | -10.24489 | -47.59713 | 2025-06-02 12:44:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a267574d-c2c6-37c1-bec0-f6d3efa6cec2 | -14.64579 | -45.40799 | 2025-06-02 12:44:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 4f48b518-a207-3763-8768-cb55330d8681 | -11.91912 | -54.41929 | 2025-06-02 12:44:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 59045f4c-4fe0-3d00-b0ca-bde24193cb0b | -10.28611 | -46.67681 | 2025-06-02 12:44:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e24dd521-6ad0-32e4-b80a-711237200398 | -13.08792 | -45.25911 | 2025-06-02 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 280.4 |
| 9b333a71-deaf-3d0a-ab22-f5ad0ac69f2b | -17.65654 | -50.71711 | 2025-06-02 12:44:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 55051dbc-95b9-3f13-84f6-3cfb89d5ab63 | -12.63487 | -48.18036 | 2025-06-02 12:44:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 702d7bb3-8afd-33ed-a61c-03a84681bff7 | -13.37516 | -54.25959 | 2025-06-02 12:44:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 0b028b23-ba27-32fc-a90b-8517f7aac1a4 | -10.66991 | -44.38592 | 2025-06-02 12:44:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 57159286-e9c8-3afe-9051-83c603e6bcd6 | -17.91402 | -46.85518 | 2025-06-02 12:44:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 19170f8a-a165-37f1-b6c1-8a071cfb264c | -10.46358 | -47.94361 | 2025-06-02 12:44:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 6c78b12b-a092-3b16-b824-e7773cc40de8 | -10.23486 | -47.16829 | 2025-06-02 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f3bc6cfb-8ed7-308e-84f2-40e6229321d6 | -10.61903 | -48.07643 | 2025-06-02 12:44:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| cfccb88b-8998-3a48-a589-6c341466eef8 | -14.73437 | -45.38412 | 2025-06-02 12:44:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 14bf578c-d9ac-351d-b5cc-4502c70ca4a7 | -12.4737 | -57.1875 | 2025-06-02 12:44:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| e6c08559-b262-37a7-80ad-a3e5dde2df1b | -11.8948 | -47.43454 | 2025-06-02 12:44:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| bdb88be0-b19f-3e74-bc97-08e99f9ce4a9 | -10.28422 | -46.68293 | 2025-06-02 12:44:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 922a2c0f-71d2-3188-9139-7e98f9fa1cf5 | -11.9058 | -47.43599 | 2025-06-02 12:44:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4873f5fe-7ecf-3c6a-b2ac-d5677882874d | -10.47394 | -47.94502 | 2025-06-02 12:44:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| dfcb53d4-7b3d-3193-8350-39e1f72629e8 | -8.60274 | -51.58467 | 2025-06-02 12:44:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 78a57976-133e-3d6b-bbb9-cec5ffa58bbe | -13.09466 | -45.28756 | 2025-06-02 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 9bec80b4-db26-3d54-9c2b-090b4d9518d0 | -14.03462 | -55.13064 | 2025-06-02 12:44:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ae625fde-5835-339c-9ca8-72a0c02e041d | -10.67626 | -44.39221 | 2025-06-02 12:44:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| d4880eeb-bf5f-35e6-ad80-b2642e2acfb5 | -14.72656 | -45.37778 | 2025-06-02 12:44:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| f34dcf01-c48d-3183-b7ea-6735d10aadb9 | -13.09711 | -45.26556 | 2025-06-02 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 8589baa9-ad8f-316a-ac6a-c987fdcc3af3 | -13.10128 | -45.26063 | 2025-06-02 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| b85f43d5-c00e-345a-8fe3-8354824d758d | -13.08533 | -45.28107 | 2025-06-02 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 341.6 |
| 05cb6860-3301-3f09-b0f1-7af07bc8bdc5 | -10.46192 | -47.9561 | 2025-06-02 12:44:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4a735a38-ecde-3624-850c-fc2c9e8256e0 | -10.70462 | -48.81246 | 2025-06-02 12:44:00 | TERRA_M-T | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b6d14856-41ca-3875-b648-af55a1bc23da | -13.09866 | -45.28263 | 2025-06-02 12:44:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 427b7770-4a0e-30fe-9850-0d59d7df241f | -18.07581 | -48.32247 | 2025-06-02 12:44:00 | TERRA_M-T | NOVA AURORA | GOIÁS | Brasil | 5214804 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a17dccdf-34d4-373d-854d-24897d7ad005 | -11.26889 | -52.47501 | 2025-06-02 12:44:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| d1cb0820-ea06-37a9-9838-72e2d0167e5f | -9.17308 | -50.17697 | 2025-06-02 12:44:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| db5b99de-dbd6-3800-a694-34c9c086d294 | -14.65374 | -45.41578 | 2025-06-02 12:44:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| a447cd36-8b5a-3f0c-b4cd-95426d7ded15 | -19.01365 | -53.48056 | 2025-06-02 12:46:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6829ade2-be0c-3911-9c3a-b0d3be5d3a24 | -19.02251 | -53.48193 | 2025-06-02 12:46:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b550d214-b925-3e56-97cd-24080285e581 | -8.6097 | -51.5731 | 2025-06-02 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| fb1e65ad-584d-3bc7-8822-6fbe5a74480e | -8.6097 | -51.5731 | 2025-06-02 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| e254611d-8c74-316b-a202-138e08ec95aa | -8.6097 | -51.5731 | 2025-06-02 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| bae4cf8c-0be1-3289-93e5-8397e8f40d0d | -11.8967 | -47.4313 | 2025-06-02 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9bd82472-3298-30c5-87a2-f1b01e2a1353 | -8.6097 | -51.5731 | 2025-06-02 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| db7d9810-9722-3aac-80e1-ce22c786778f | -8.6097 | -51.5731 | 2025-06-02 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| aea9a5ca-ded2-3c5e-9b16-80f4e2a46738 | -8.6097 | -51.5731 | 2025-06-02 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| d20c5bc8-7a5e-3869-acf1-243da899ed83 | -8.2719 | -49.8916 | 2025-06-02 14:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f9b35fde-c484-3b2d-88cc-1a682d5cae49 | -6.7489 | -45.0977 | 2025-06-02 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1102ce5f-3e7e-3444-a75c-507587912b55 | -10.6689 | -44.3904 | 2025-06-02 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| a5fd46e1-b802-3a96-8091-dfca67a1e64e | -10.2394 | -47.6153 | 2025-06-02 14:20:00 | GOES-19 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| baaa22af-78cc-3627-85cc-b729c88effb8 | -9.3972 | -48.4305 | 2025-06-02 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 47937296-382d-3550-9468-7c4b1704c5eb | -6.7489 | -45.0977 | 2025-06-02 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 26a387dd-a77a-31ea-bf16-e84bfedb803a | -9.3972 | -48.4305 | 2025-06-02 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 771a3601-0082-3878-89ba-60938707fd56 | -10.6689 | -44.3904 | 2025-06-02 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 788aa852-3994-3db8-95f5-01fa1e04fc5b | -6.7489 | -45.0977 | 2025-06-02 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| ba5f7042-d37a-3ecd-ae3e-774d5ebefb8c | -9.3972 | -48.4305 | 2025-06-02 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| d4a4328b-2087-3ec0-a95e-2a02aaf8eb78 | -10.6689 | -44.3904 | 2025-06-02 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |


