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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab4b35e6-7174-3cdb-bede-52f31ed1e0e9 | -18.19151 | -49.14049 | 2025-06-04 12:27:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 83f60308-7fa4-312b-a3b3-4ea6a1d602c0 | -17.68084 | -46.82681 | 2025-06-04 12:27:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3f111f9d-47bc-3847-8c83-6e9e5ddcb2ad | -11.5428 | -56.4237 | 2025-06-04 12:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b239ad65-43ea-3974-935e-341e792b1dc1 | -11.9155 | -47.4511 | 2025-06-04 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f95dc249-aa77-3311-936e-4a3e2ba4bafc | -7.0169 | -44.5954 | 2025-06-04 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 8d474db9-8b22-3292-b4f7-b87d4f58ea30 | -7.0169 | -44.5954 | 2025-06-04 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 7fc2edb8-ff8f-3f02-9b92-0d95a38e5658 | -6.6373 | -43.1933 | 2025-06-04 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 669ee207-56fa-364d-a2cb-080666d50e1a | -7.0169 | -44.5954 | 2025-06-04 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| eb78cd8f-1bab-3120-9eab-0b3994e7944d | -11.5617 | -56.4221 | 2025-06-04 13:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6938770d-903a-3b6b-a349-9604570d5c23 | -11.5617 | -56.4221 | 2025-06-04 13:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| df18fae7-a150-33af-85af-78b022a1b41e | -7.0169 | -44.5954 | 2025-06-04 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 53c352e9-388a-3fbc-b12c-9cc39946317c | -11.5617 | -56.4221 | 2025-06-04 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 4c8419e4-7a7e-3bb5-baab-26397e29e39d | -6.6371 | -43.2167 | 2025-06-04 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 40130610-afc1-329f-8bf0-4e4d5d694f0b | -14.7202 | -45.0884 | 2025-06-04 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 9b764972-a71a-37f7-bc7d-579b8735a51a | -6.6373 | -43.1933 | 2025-06-04 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 116.9 |
| 71e2b0f2-e389-300f-bcf3-86cdfd1c610d | -7.0169 | -44.5954 | 2025-06-04 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 784d054c-7e2c-3253-8581-807f23c4c370 | -10.5123 | -49.7433 | 2025-06-04 13:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 56c72e9e-67bb-3fb3-90cf-4a54f5d9feda | -11.5428 | -56.4237 | 2025-06-04 13:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f09fe54f-52c4-3e83-ab03-2b9960b7d4d0 | -14.7202 | -45.0884 | 2025-06-04 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| d8be5ed8-876b-3bd2-848c-ee0a3be14d2f | -11.5617 | -56.4221 | 2025-06-04 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| c43a86ad-5a75-3733-aa17-dc16846b7423 | -11.5428 | -56.4237 | 2025-06-04 13:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 4735395d-608b-3c38-b8fb-f746f8bd3db2 | -8.0017 | -50.6975 | 2025-06-04 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a0bef2e7-0270-3d17-8af3-4836fc2d176b | -6.6373 | -43.1933 | 2025-06-04 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 22220e07-a134-3b1e-b158-7ad1b6cbaaf8 | -10.5123 | -49.7433 | 2025-06-04 13:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 1e7dfd91-f6de-329f-945b-9bd18e453d78 | -6.6371 | -43.2167 | 2025-06-04 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 711671f1-1f9b-383b-8a2b-e2eb0d7476f6 | -7.0169 | -44.5954 | 2025-06-04 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 4dcb0464-df26-305c-8ffc-897bca0df23a | -11.5428 | -56.4237 | 2025-06-04 14:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| df9de04a-360b-3367-a231-569467bb1cb1 | -16.4682 | -45.0031 | 2025-06-04 14:00:00 | GOES-19 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 4a264523-f244-3f8f-a6a9-2d6539a30963 | -14.7202 | -45.0884 | 2025-06-04 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 8653a557-83b1-38f1-ba8d-a55b9231a96d | -13.0836 | -52.0304 | 2025-06-04 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| d84d6d47-fbeb-3f5c-89af-1b3fe7738155 | -8.0017 | -50.6975 | 2025-06-04 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 8bfbe49e-500b-35b7-ac37-a32a94bdc636 | -6.6373 | -43.1933 | 2025-06-04 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 7c75eb37-8248-3397-a250-285deb2eea3a | -6.7508 | -44.9155 | 2025-06-04 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 5a3ad023-3122-39c6-b356-186dbbdc0bbf | -11.5617 | -56.4221 | 2025-06-04 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 52901d85-9f43-3386-987f-d9153d8079e4 | -11.5617 | -56.4221 | 2025-06-04 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 8c2a182c-8b53-3d31-b009-0159dccb8804 | -6.6371 | -43.2167 | 2025-06-04 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 9d1c7c52-5922-32b0-ae10-036f680df5cb | -11.5428 | -56.4237 | 2025-06-04 14:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| ae045a6b-040b-35c0-81b9-4aec47f1705e | -6.6373 | -43.1933 | 2025-06-04 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 119.1 |
| d39e38c6-d1aa-3732-8631-f9828dfaaa1b | -14.7202 | -45.0884 | 2025-06-04 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 872ca3c4-a4dd-3c55-bbbf-9b95f4ec1740 | -7.0169 | -44.5954 | 2025-06-04 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 12337375-393f-3dac-b0f2-97798b1ce813 | -8.0017 | -50.6975 | 2025-06-04 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| fda2d351-e08f-37aa-94f5-b1890b0d7e0d | -6.7508 | -44.9155 | 2025-06-04 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 1a5997a0-980c-3a63-b779-f7c94937ffb1 | -13.0836 | -52.0304 | 2025-06-04 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 59fe92fb-c1d0-3043-b7db-f79091b6e4fc | -12.6579 | -58.2079 | 2025-06-04 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| e36ec8e5-6253-37d8-a34a-cefdecc7f343 | -11.5428 | -56.4237 | 2025-06-04 14:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 30118651-0367-3192-ad41-35caf4e124e5 | -13.4823 | -46.7957 | 2025-06-04 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| db8a5100-ded0-3f1e-914f-567ae0842bde | -6.6373 | -43.1933 | 2025-06-04 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 137.6 |
| b7c5bad7-6782-3c68-995e-62fe595d0ff5 | -16.4682 | -45.0031 | 2025-06-04 14:20:00 | GOES-19 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f9ce1a23-eeea-3a41-a038-c422920de0f4 | -6.6371 | -43.2167 | 2025-06-04 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 86.3 |
| f3a7261a-c7d3-3969-a8e5-9061556ee7fd | -14.0328 | -55.13 | 2025-06-04 14:20:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| fcb4e2f6-168e-30fa-ad79-82bc88fb0661 | -8.0017 | -50.6975 | 2025-06-04 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| da347023-a879-3caa-accb-147edc749cfa | -11.5617 | -56.4221 | 2025-06-04 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 8051357d-4830-30ed-ae13-47d263fae158 | -6.7508 | -44.9155 | 2025-06-04 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 787970b3-8f49-3700-9759-b9ccf103a92f | -7.0169 | -44.5954 | 2025-06-04 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 6c2c5d3c-85ca-3ab5-a768-4dbf225fd57f | -6.9981 | -44.5971 | 2025-06-04 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| ddfae1bb-cb26-38bd-af8d-3166a13e4044 | -11.8365 | -51.2854 | 2025-06-04 14:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 2dc1b197-4ce3-3e7c-8d74-f7be5ee079e7 | -14.0328 | -55.13 | 2025-06-04 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a3af57ad-7981-3f03-82ec-e5e26acb5019 | -12.6579 | -58.2079 | 2025-06-04 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| a189c530-db02-3f86-9c6c-d35cf1d37f15 | -11.5428 | -56.4237 | 2025-06-04 14:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 0052341c-91f8-3308-a2bd-a764f4cdcbaa | -6.7508 | -44.9155 | 2025-06-04 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a54bc616-656b-3f6e-be79-438f1e3d3fa6 | -12.6767 | -58.2262 | 2025-06-04 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| f90d3150-229c-35cb-b610-10434b56c6b2 | -11.5617 | -56.4221 | 2025-06-04 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 21e348fa-2247-3bc1-8a15-8fef561e7550 | -12.6577 | -58.2277 | 2025-06-04 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| bdb87215-37f5-312a-ad62-a44b116e2f13 | -14.7202 | -45.0884 | 2025-06-04 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 435a86fa-50c6-3444-b582-2b3159f65075 | -6.6371 | -43.2167 | 2025-06-04 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 120.4 |
| f7eeac23-9be9-3c57-a890-b369214e9bc0 | -6.6373 | -43.1933 | 2025-06-04 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 163.2 |
| b05af6fc-305c-3e66-8eb5-031fdac3b27b | -13.0836 | -52.0304 | 2025-06-04 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 6342bfef-fb96-3962-80f0-cc0d7d47f73e | -7.0169 | -44.5954 | 2025-06-04 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 59ff0e9d-ba62-3896-b270-2f874f30bc0e | -6.7508 | -44.9155 | 2025-06-04 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 38dff628-91dd-3224-b069-76ee71425c7f | -6.6373 | -43.1933 | 2025-06-04 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 164.4 |
| e7d4b548-8469-3758-982e-8f69726ce16a | -11.5617 | -56.4221 | 2025-06-04 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 4c65aa9c-3261-3ee3-9596-536800a3872a | -11.8365 | -51.2854 | 2025-06-04 14:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 4f4636f3-c451-3e31-9dca-f87cf344d7eb | -14.0328 | -55.13 | 2025-06-04 14:40:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d4ebf2bf-39d7-3f3c-a3e6-32a3293963ad | -7.0169 | -44.5954 | 2025-06-04 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 3b9bc097-0de3-3d4e-919a-635ea20d9503 | -6.6371 | -43.2167 | 2025-06-04 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 0d6b3c70-404a-3545-8581-28abcc541512 | -6.9981 | -44.5971 | 2025-06-04 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e690f5b8-1d2f-3c2e-a633-ba9486051a8d | -12.6769 | -58.2063 | 2025-06-04 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 58c3983c-7d27-3b4a-af79-209b81ca21f8 | -12.6767 | -58.2262 | 2025-06-04 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| c9e8fe60-f307-3879-b571-509ec1b3046d | -14.7202 | -45.0884 | 2025-06-04 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 80e50963-9b9c-38b7-abac-9e58a7b3759e | -11.5428 | -56.4237 | 2025-06-04 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 2f7d7013-1201-3f30-947d-fb00439d96d2 | -13.0836 | -52.0304 | 2025-06-04 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| b9a40d13-1cde-3251-942e-5add95975371 | -12.6579 | -58.2079 | 2025-06-04 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |


