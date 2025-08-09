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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5aa1f35a-8ae2-32af-b920-64650cfafa4e | -6.8212 | -59.2458 | 2025-08-09 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e23ab036-1e07-3a78-a9f6-0dc27d2252a4 | -5.2073 | -46.0876 | 2025-08-09 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 104.2 |
| bdd40bf1-ea53-381e-a0dc-52577f4fa621 | -13.0386 | -43.8604 | 2025-08-09 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0962a1ca-5b95-337b-92f7-9d479d4ea0bf | -12.0484 | -47.5 | 2025-08-09 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 29b6e08f-c101-32ad-9b76-64cd0708da56 | -13.039 | -43.8367 | 2025-08-09 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b5ad634a-7854-33a7-a567-bae54f15c482 | -8.9399 | -60.7481 | 2025-08-09 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 05b4ceef-fbfb-3603-b0fa-520db140789a | -8.9401 | -60.7288 | 2025-08-09 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e5290625-d3e8-324a-b616-5bbeec039a92 | -13.0773 | -43.8537 | 2025-08-09 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 99168399-709b-3ce1-869d-a6bcbe2bfd0b | -17.5291 | -50.2988 | 2025-08-09 00:00:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 141b82eb-d416-31f7-a182-df4fcc788211 | -19.8124 | -47.0634 | 2025-08-09 00:00:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 1664952e-aa49-32cf-926d-6966e51cc8b3 | -6.5856 | -44.564 | 2025-08-09 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 486657d0-3458-3898-ae94-a5097d449133 | -17.5093 | -50.3023 | 2025-08-09 00:00:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| acef6be3-3eae-3897-a53f-fd9ae2a24cc6 | -11.1077 | -50.4934 | 2025-08-09 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 01c5a65d-64f4-390a-9b62-7a0aa8cf0b0f | -17.5296 | -50.2766 | 2025-08-09 00:00:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 180.3 |
| fb950e76-cd1a-34ba-b17e-0bf7db65fa94 | -5.226 | -46.0865 | 2025-08-09 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 96d2e3cf-badf-3a2a-a371-fb67862383be | -19.813 | -47.0398 | 2025-08-09 00:00:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e57e45c9-edf5-3ead-98fe-3a84e52335a9 | -5.2075 | -46.0653 | 2025-08-09 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 219.2 |
| 44e44e9e-6482-38c1-801d-2b39374bb14b | -17.5098 | -50.2801 | 2025-08-09 00:00:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 700d4b5c-df3c-3375-b18d-f0dc15a54eff | -13.0778 | -43.83 | 2025-08-09 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 3c069c53-878c-3057-b7ec-2e71696da1d2 | -13.0584 | -43.8333 | 2025-08-09 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 263df59c-323f-3ced-83ab-ce2c27edd8a6 | -6.6338 | -47.296 | 2025-08-09 00:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b371a3e0-d8b4-375a-b753-5ba552df4093 | -8.9213 | -60.7489 | 2025-08-09 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 182.3 |
| ac53650e-0368-3957-a0f5-847492773554 | -12.0289 | -47.525 | 2025-08-09 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 7dbdc17d-b52a-380c-b6ab-58046de491e0 | -19.8328 | -47.0586 | 2025-08-09 00:00:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 8e6b3449-0185-3dd1-9c48-9135d213c3fb | -6.8397 | -59.245 | 2025-08-09 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 972de167-c9cb-3b5a-8779-d85adf21d31a | -9.5589 | -62.7238 | 2025-08-09 00:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 567a1af4-f416-34e8-8a22-965b0ff82a9a | -6.8395 | -59.2643 | 2025-08-09 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b17bb313-3a7d-37f7-afbc-6732e967450a | -5.2262 | -46.0642 | 2025-08-09 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 122.2 |
| e7c58580-f0fe-3e27-a8be-eb81f4e8092e | -8.9215 | -60.7297 | 2025-08-09 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| ab1e4514-eba1-3bb9-a418-8d024e620e48 | -13.058 | -43.8571 | 2025-08-09 00:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 1e2fa4f4-9a83-37a3-a951-2adf280570d7 | -12.0481 | -47.5224 | 2025-08-09 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 40117f0e-9332-3fc3-80fc-1e3120ada7ff | -17.5296 | -50.2766 | 2025-08-09 00:10:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 329.3 |
| a2faef14-5187-3fc4-ba89-3a6e1c30cbdc | -18.4539 | -50.6863 | 2025-08-09 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 23657502-e91b-315d-a5f8-04f4b5b935ea | -5.2073 | -46.0876 | 2025-08-09 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 134e5286-2109-37aa-85f8-fd11552ab079 | -13.0386 | -43.8604 | 2025-08-09 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 333752c5-7f66-32a4-baed-dd439ad53145 | -13.0778 | -43.83 | 2025-08-09 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 04b8583f-16aa-32af-8811-3bf51f0360ce | -19.8124 | -47.0634 | 2025-08-09 00:10:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 12977276-5abf-3e8b-a2c3-36c8bd14d891 | -19.813 | -47.0398 | 2025-08-09 00:10:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 44f0c157-664a-3e31-bce5-571eead77275 | -6.6151 | -47.2974 | 2025-08-09 00:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 4751725c-dfdf-3afa-90da-4a314fad5894 | -8.9215 | -60.7297 | 2025-08-09 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 423dfffb-b802-3b16-a290-df1859604af2 | -13.0584 | -43.8333 | 2025-08-09 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 47f98d54-4459-35c3-8307-1bf62d4e67cd | -5.2262 | -46.0642 | 2025-08-09 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 154.6 |
| 8e39ae6a-0a4b-30d0-ba8a-9e35ecab4c5c | -5.226 | -46.0865 | 2025-08-09 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 34f5f762-4710-30bb-b39a-8c50efa61710 | -12.0484 | -47.5 | 2025-08-09 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| bbe28a61-e1fc-3140-9692-c6383c7facab | -17.5301 | -50.2544 | 2025-08-09 00:10:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e1bd95e8-7d4c-36ef-ab75-69e354df9367 | -11.9475 | -44.5306 | 2025-08-09 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 9a99cdfa-206f-30cf-9ce3-2b9662412360 | -17.5103 | -50.2579 | 2025-08-09 00:10:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 4455a087-e067-3667-943c-6a04c034a1f6 | -6.8212 | -59.2458 | 2025-08-09 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| db89b931-8a33-30a7-b93a-9d24983bc2b2 | -6.5856 | -44.564 | 2025-08-09 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0c704b6d-9e22-39d4-90a8-fd4d7fdda208 | -17.5098 | -50.2801 | 2025-08-09 00:10:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 292.8 |
| 217b92af-31f7-37c1-824c-90023ccadeef | -11.9283 | -44.5335 | 2025-08-09 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 0ff08f46-af35-3422-9a05-19fecb15176d | -8.9399 | -60.7481 | 2025-08-09 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 31b228f9-5eaf-3cbc-8e14-5891b6f45f68 | -17.5291 | -50.2988 | 2025-08-09 00:10:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 150.3 |
| dde9289d-5108-3d3d-9f43-308fee21fc6e | -6.8397 | -59.245 | 2025-08-09 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5ec02f95-75cc-364b-b0b1-1d0b177ebf59 | -18.4334 | -50.7122 | 2025-08-09 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 5a391d76-2442-30ce-a9a2-5cb746729c5a | -13.058 | -43.8571 | 2025-08-09 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 90049a1f-b705-3ab3-a14d-97ca7fdd0e15 | -23.6108 | -51.9019 | 2025-08-09 00:10:00 | GOES-19 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| 1f7ea6fa-b6e0-3460-95b3-03b272a78cd5 | -12.0481 | -47.5224 | 2025-08-09 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4add6655-4eef-35ad-a4cc-cd16bd56b5f2 | -18.4534 | -50.7085 | 2025-08-09 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 154.6 |
| a54bbf49-5920-314d-9510-c794c2f3dbe5 | -5.2075 | -46.0653 | 2025-08-09 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 3610309c-962f-387d-9da3-8ff84e3e1d90 | -19.8328 | -47.0586 | 2025-08-09 00:10:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e06814e7-52b0-3c83-8d44-05b42a3cd740 | -8.9213 | -60.7489 | 2025-08-09 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 4d151edd-8863-3c7c-a8f0-92eaba4bb310 | -9.5589 | -62.7238 | 2025-08-09 00:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 93d9edc8-3cdb-3d82-9378-de9ae26cff17 | -11.1077 | -50.4934 | 2025-08-09 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 48ea5615-8821-3543-83a1-9b0aea5908f0 | -17.5093 | -50.3023 | 2025-08-09 00:10:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 81cef994-b3b5-3283-8ae5-030a092c9524 | -8.9401 | -60.7288 | 2025-08-09 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1fd9a324-aa6f-30cd-8f07-01df960a1f12 | -13.039 | -43.8367 | 2025-08-09 00:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 0e16bbdf-fcf7-3961-b58b-6679fddc35d6 | -13.058 | -43.8571 | 2025-08-09 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 220.8 |
| e1372280-ee20-35b4-9210-897ca650b9d9 | -19.813 | -47.0398 | 2025-08-09 00:20:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e42fb14c-eb7e-37d9-9c77-3f749d344ceb | -9.5589 | -62.7238 | 2025-08-09 00:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 76220f6a-7fe1-3c31-9973-ae9d80854e17 | -13.0773 | -43.8537 | 2025-08-09 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 20992894-90c4-38e2-97b5-36def81f0348 | -17.5093 | -50.3023 | 2025-08-09 00:20:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 5ab4d91d-11b7-3b68-8886-8aaaf430a820 | -19.8124 | -47.0634 | 2025-08-09 00:20:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 174.6 |
| c3283ddd-9422-3925-be47-d5086e8bbb49 | -5.2073 | -46.0876 | 2025-08-09 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 7144d494-2266-30a9-a04b-85a9d2e637a5 | -12.0481 | -47.5224 | 2025-08-09 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c9e9c643-2b2f-3adc-bde5-a7125b04fd65 | -8.9401 | -60.7288 | 2025-08-09 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 16a79125-b3e8-3cc3-9449-fe5aeff217e7 | -17.5296 | -50.2766 | 2025-08-09 00:20:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 323.4 |
| 5093059d-d54d-32ac-96be-22f1f60328c0 | -18.4534 | -50.7085 | 2025-08-09 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 14760c56-2211-3125-9212-09c9ae6c5784 | -17.5098 | -50.2801 | 2025-08-09 00:20:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 300.8 |
| 3c823a36-c263-3d18-8840-7105b93e5787 | -6.6338 | -47.296 | 2025-08-09 00:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 93f38b32-e5de-3ccc-b666-72f3babc5bdc | -13.0584 | -43.8333 | 2025-08-09 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 238.7 |
| c95bbebd-963e-3fda-b878-e72c70dae8ab | -6.5856 | -44.564 | 2025-08-09 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 3018a410-14d1-36a5-979d-165dcdf076c1 | -5.226 | -46.0865 | 2025-08-09 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| e6e5220c-d629-3e00-8643-3554b99561fb | -17.5291 | -50.2988 | 2025-08-09 00:20:00 | GOES-19 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 136.0 |
| ebe54889-c654-3fb6-aa63-8a59362003eb | -12.0484 | -47.5 | 2025-08-09 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 619f0939-3f96-3129-8b44-9efc2762f452 | -8.9213 | -60.7489 | 2025-08-09 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 164.5 |
| d62a4bd8-e262-334f-b8df-8fa4ca293615 | -18.4334 | -50.7122 | 2025-08-09 00:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e87f13f4-ee23-3473-9ac4-28e19fa48c60 | -11.9279 | -44.5569 | 2025-08-09 00:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 423018e1-3ba3-3552-8f3f-717ad3103f69 | -13.039 | -43.8367 | 2025-08-09 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c7598e90-7d2a-3643-9943-e46edbb4eb2c | -11.1077 | -50.4934 | 2025-08-09 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| e18fc26f-a975-3a4e-b2a0-3a08be6a3908 | -5.2262 | -46.0642 | 2025-08-09 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 7f036239-5311-3ba1-a039-3cb9903c6cc0 | -13.0778 | -43.83 | 2025-08-09 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 747c7e72-b629-3ce6-b406-d7a645f19545 | -13.0386 | -43.8604 | 2025-08-09 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 0244838d-8a36-3249-af4d-7aaef9128229 | -8.9399 | -60.7481 | 2025-08-09 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 767d63d6-61fc-3537-b51b-ba336115493a | -8.9215 | -60.7297 | 2025-08-09 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 84a20b69-6694-301c-8460-6ac90390622b | -6.8397 | -59.245 | 2025-08-09 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d1e2ca10-7f4e-3c1e-a091-c67e961e2e67 | -19.8328 | -47.0586 | 2025-08-09 00:20:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 74.1 |
| f1f18b8d-5fe6-38a9-93f1-3899fab5f1b1 | -5.2075 | -46.0653 | 2025-08-09 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 194.6 |
| 63dd2ad6-d65a-3442-8f7b-1dbfd4398f66 | -12.0484 | -47.5 | 2025-08-09 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6c791977-50ba-3086-ade9-5e2db1cf2599 | -13.039 | -43.8367 | 2025-08-09 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |


[Clique aqui para ver as próximas entradas](README2.md)
