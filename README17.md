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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba2ebb9f-d8ff-38e8-a519-142d408d5899 | -14.8153 | -47.9343 | 2025-08-24 01:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| baa29f21-b561-3851-b5b3-826c73cc208b | -16.7965 | -51.3637 | 2025-08-24 01:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7ad4bc0c-c752-3002-a262-e3d14084af8b | -10.6128 | -44.3284 | 2025-08-24 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 08aa59bd-f6d7-3609-b74b-d0838b6275f4 | -11.5245 | -51.8685 | 2025-08-24 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 5953c650-1fa8-3842-b52e-6c9dbff861ec | -3.5994 | -47.5359 | 2025-08-24 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8d91952a-f359-38f1-b0e8-fd4c08af2077 | -5.4182 | -60.1593 | 2025-08-24 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 2d5fb02f-d3ea-330f-8c9c-1f9d4d1060a6 | -9.0232 | -65.6982 | 2025-08-24 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 39d91926-f71a-3237-b6bc-d42085515c89 | -9.1722 | -59.4629 | 2025-08-24 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 6b55fd36-1c7d-3c45-b0fb-295f3d21c661 | -20.3594 | -51.7023 | 2025-08-24 01:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 6fcb0f12-ed23-3dd3-9d89-b668315932af | -9.1535 | -59.4834 | 2025-08-24 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 149.6 |
| a8eb3058-4d1e-3ec6-a807-a8b7f036a94e | -4.9605 | -55.8226 | 2025-08-24 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 177bcb2b-2e76-3df7-91c2-bf3292fa4fbd | -9.0046 | -65.6988 | 2025-08-24 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 3738cc95-c390-3739-9b4a-32035bd78507 | -5.4364 | -60.1779 | 2025-08-24 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 7fb08d7a-0afb-3b16-aadf-b81d79bc4a60 | -9.0231 | -65.7169 | 2025-08-24 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| ea68c5e8-8c56-3132-a9ac-b97793ba51c6 | -10.6131 | -44.3051 | 2025-08-24 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c3d9aa87-cb7a-37e4-bc87-27593cbb9d3f | -20.3396 | -51.6839 | 2025-08-24 01:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 43bd4024-f392-3625-bebd-c7c6be2add45 | -17.6176 | -44.298 | 2025-08-24 02:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 01c278fa-11b0-382e-a099-e264d69f5eef | -9.1535 | -59.4834 | 2025-08-24 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 4a444dce-d8fb-30f8-b81d-765f8420ddab | -9.1998 | -60.793 | 2025-08-24 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| ea99fcbe-a594-3790-9857-556fb01c48d7 | -20.3396 | -51.6839 | 2025-08-24 02:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 89de5c88-690d-3544-bbc1-00b537f6b842 | -5.8507 | -52.0878 | 2025-08-24 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 93383356-5e9d-347a-8e12-8745b4533bd8 | -9.0246 | -65.3807 | 2025-08-24 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e95707c3-e08b-3dee-9492-f1e54e95d0cc | -20.3594 | -51.7023 | 2025-08-24 02:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 105.0 |
| cdec5054-bdee-3fde-ba16-1d216ce60370 | -16.797 | -51.3419 | 2025-08-24 02:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 8015dc2f-bbbf-3467-b7b2-df695c0d48d1 | -17.4045 | -42.6186 | 2025-08-24 02:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 55.0 |
| c3301cf2-49d4-3fd7-9bae-38e9caa30de5 | -9.0046 | -65.6988 | 2025-08-24 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| e175f1a8-ea96-3713-bb10-4b7764e15303 | -10.416 | -47.1955 | 2025-08-24 02:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 18d12794-b8aa-3601-882a-3ff8a2f3a56a | -20.339 | -51.7062 | 2025-08-24 02:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 81.9 |
| e8515804-5ded-3b7e-ac83-9296acb02f2d | -9.1721 | -59.4823 | 2025-08-24 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| c3beb78e-d7e1-3eaf-8308-957fe3cc457e | -9.1533 | -59.5027 | 2025-08-24 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 469ee065-8e6a-3a9c-9bd1-ffa471b2afb3 | -17.6183 | -44.2738 | 2025-08-24 02:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 83ac41fd-0b9c-36e9-8886-a8997c14a612 | -10.5937 | -44.331 | 2025-08-24 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 14e46de7-f8b0-3a4b-926f-9c111e21231f | -11.5245 | -51.8685 | 2025-08-24 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| da49371d-7a8c-3165-bf23-4f43555208f5 | -9.0232 | -65.6982 | 2025-08-24 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 463688a7-d2d0-34f9-8772-e0a1cb10979a | -9.1536 | -59.464 | 2025-08-24 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 186.1 |
| e8270ba6-eed1-3077-b788-429b6cee061b | -9.0231 | -65.7169 | 2025-08-24 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 3bebaff8-41a0-38f3-a553-f270b4713c3f | -10.8078 | -46.4083 | 2025-08-24 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 82f4f368-817e-3fd9-bf92-53bb8e06d15b | -17.5975 | -44.3027 | 2025-08-24 02:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 6bd7adbd-bff3-3ebc-ba96-f29023fe4094 | -9.1722 | -59.4629 | 2025-08-24 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| f5c9ced4-878e-319a-8561-4b3064c09d3f | -17.5982 | -44.2784 | 2025-08-24 02:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 32ec73c6-0acf-375a-afcc-252ba6e98cd7 | -5.8692 | -52.0868 | 2025-08-24 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 25fa9d35-7215-34ab-9b40-931d3cd24b06 | -4.9605 | -55.8226 | 2025-08-24 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 18ff5d92-2c80-3881-b465-3e6aa1d3ca6b | -9.1538 | -59.4446 | 2025-08-24 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 3ca06d25-8503-39e4-8e20-d15675609dec | -9.1441 | -60.7765 | 2025-08-24 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 366fdded-8af6-365b-ade5-85726c773cd4 | -5.4364 | -60.1779 | 2025-08-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 73a8016f-3fc1-39b6-bbb5-ffa21f5c4391 | -9.0416 | -65.7163 | 2025-08-24 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2efaac4e-6ae2-3a9d-bb42-f2c15995edeb | -20.3701 | -46.7433 | 2025-08-24 02:00:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 0bbda8c9-9b43-3546-b4d5-1ba8ae1e19f6 | -20.3599 | -51.68 | 2025-08-24 02:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 170.5 |
| d950b411-07d3-32eb-9255-2c10a9aa6d9f | -5.4181 | -60.1784 | 2025-08-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a2ddc27b-7c46-3877-99ab-8fc3fd37ed81 | -14.8153 | -47.9343 | 2025-08-24 02:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 55a69c6d-a787-3036-82f6-e48e1c4c46f8 | -5.4365 | -60.1588 | 2025-08-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1212cc58-307e-3b00-998a-2a9127591673 | -10.6128 | -44.3284 | 2025-08-24 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4fd9c4ea-84a4-38f7-ba5f-dfbcf873812c | -16.7965 | -51.3637 | 2025-08-24 02:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 415d3165-c0b9-39bc-8eda-8d25d3b23002 | -3.5994 | -47.5359 | 2025-08-24 02:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 51af4f71-b261-3625-8cc1-b7c7d9bb2a78 | -20.339 | -51.7062 | 2025-08-24 02:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 78.7 |
| fe230950-14dd-3fef-9c87-4cf51040c2a0 | -10.6128 | -44.3284 | 2025-08-24 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| f659c763-5128-3e50-8f3e-1fba0a691da4 | -17.4045 | -42.6186 | 2025-08-24 02:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| d8d34315-6bda-3bfe-82a8-ae81cc207a1b | -8.9104 | -62.4669 | 2025-08-24 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8308f86e-9b11-3e75-be49-bbeec0ae3bb1 | -16.7965 | -51.3637 | 2025-08-24 02:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 30f1b1b1-ceaf-3767-b27b-ae3324800eb6 | -17.6183 | -44.2738 | 2025-08-24 02:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 49.6 |
| ffe573fe-cb59-3577-ad2a-649999c7f07e | -8.6131 | -62.5929 | 2025-08-24 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| df2221a9-da51-3ff2-9544-7213ce9798d8 | -10.5937 | -44.331 | 2025-08-24 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| fd910d38-a114-3173-9ed6-e33d059dad58 | -9.1998 | -60.793 | 2025-08-24 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| d37c76b0-af8e-355b-a43f-262979ddf204 | -9.1721 | -59.4823 | 2025-08-24 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| b493f2fb-fdab-3b54-a676-16776dcf15fb | -9.1538 | -59.4446 | 2025-08-24 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| bf79edf5-8b46-36b2-b883-ffd981303f53 | -11.5245 | -51.8685 | 2025-08-24 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 452e80e0-358c-3039-a651-fd737a00e152 | -17.5975 | -44.3027 | 2025-08-24 02:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9faedec1-018a-3f76-b837-a09069147eca | -9.0246 | -65.3807 | 2025-08-24 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 0c8c4e08-2444-32a3-85a6-22f89b7fe627 | -9.1722 | -59.4629 | 2025-08-24 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| e2220f5e-e9ee-3a0d-be67-2e20f122a6a1 | -9.0232 | -65.6982 | 2025-08-24 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 124.9 |
| c8812dd8-9705-3174-bdd2-8642b64234ab | -20.3599 | -51.68 | 2025-08-24 02:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 146.6 |
| f54db4c2-82b2-3e04-a97e-fc8573cb5e39 | -5.4364 | -60.1779 | 2025-08-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 4f8f48b5-368b-3dd2-877f-8bce31495c63 | -6.893 | -45.6737 | 2025-08-24 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 28f1dd19-9ed7-3a8f-ad8f-f3c3eacab208 | -10.8078 | -46.4083 | 2025-08-24 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| e0f4f37a-cc1f-3e38-af66-c35cd7fdf1f7 | -9.1535 | -59.4834 | 2025-08-24 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 4fc3995d-754c-384d-822d-376d7df535a8 | -5.4365 | -60.1588 | 2025-08-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| a108f92c-928d-3a6d-b0a1-35dc3f04335e | -8.9106 | -62.4289 | 2025-08-24 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a7d783b8-c000-3d44-80aa-86609b7344eb | -9.0046 | -65.6988 | 2025-08-24 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 90d1e3a6-6a41-3e0d-801f-a38561f068fe | -16.797 | -51.3419 | 2025-08-24 02:10:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 69f2a51c-c641-385c-8c53-09d42aa720a9 | -9.1536 | -59.464 | 2025-08-24 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 917b40eb-1748-3fbd-9089-5faa1c79f680 | -9.1441 | -60.7765 | 2025-08-24 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 257b88d6-cf72-349c-94d7-867555fb7527 | -20.3594 | -51.7023 | 2025-08-24 02:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b34ed597-891e-3c20-a58c-5185599d5989 | -4.9605 | -55.8226 | 2025-08-24 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| aab69d34-979f-36ed-b547-b44b42ff7636 | -9.0231 | -65.7169 | 2025-08-24 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| f2b503e3-4424-3893-9a5e-4c13afe4c18b | -14.8153 | -47.9343 | 2025-08-24 02:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 83f05a2a-387d-32ec-a323-0c5deb76b426 | -20.3396 | -51.6839 | 2025-08-24 02:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a7d61b62-8b7c-3522-9478-34e2d912acd3 | -9.1533 | -59.5027 | 2025-08-24 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0ce593b6-1bce-3ca3-a3f8-8d9030431766 | -23.8479 | -47.5793 | 2025-08-24 02:10:00 | GOES-19 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| e3e2cf63-fd8b-3642-a3ac-02ce425a46aa | -8.8919 | -62.4487 | 2025-08-24 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 7f654745-b9d4-3135-82f6-000903189d70 | -5.4181 | -60.1784 | 2025-08-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5caf483d-6654-3d2d-8789-0e0896cbf01c | -17.6176 | -44.298 | 2025-08-24 02:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 96.7 |
| c795f889-9411-3b3a-ae5f-411b6feef762 | -8.9105 | -62.4479 | 2025-08-24 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 140.0 |
| e3cec39e-7b35-34a9-b65b-5f2afdc0f5fa | -11.9796 | -61.030201 | 2025-08-24 02:14:00 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d504876c-2f1c-3f10-897a-3ae490352d7d | -8.9942 | -65.388 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a278571-8533-3e7b-bc1e-0278215ae365 | -9.004 | -65.385597 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87273f2b-4b96-3b8f-8001-4f1633861cbe | -8.8839 | -62.443901 | 2025-08-24 02:14:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63b70296-d95c-3f6e-84f2-83f673668757 | -9.0375 | -65.731796 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d56a7f6-0cf7-3130-b31f-299bcef2eff6 | -8.9871 | -65.694702 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9491510f-87f3-33cd-b8fd-6cab28110096 | -8.9928 | -65.718102 | 2025-08-24 02:14:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4548832-fb66-3cd9-91fe-9e9c654cb09d | -9.1538 | -59.5075 | 2025-08-24 02:14:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
