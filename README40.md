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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fcffe91-08e5-3a2a-9ab6-18005abb0427 | -13.3832 | -61.951801 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cca2277e-3a8d-390a-b643-bbc7ef6b29ee | -13.3848 | -61.9594 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4840d8da-ac80-3a78-bbe4-ff9338caf51f | -13.3864 | -61.9669 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8d97456e-349d-3898-98b8-736ed1b227bb | -13.3881 | -61.974499 | 2024-10-09 01:26:10 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7101b6ba-9384-37a0-ac40-72ba2ec0dd0d | -11.3838 | -51.0807 | 2024-10-09 01:26:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 26a2ce51-ce71-3340-b01b-2d819a354d28 | -12.9646 | -60.0816 | 2024-10-09 01:26:11 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4385e08d-1f62-3dda-8cb1-aa544f1e912e | -11.5233 | -65.137 | 2024-10-09 01:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 96df795e-a60f-37a9-9259-b00d5ebf71f2 | -11.5726 | -58.9619 | 2024-10-09 01:26:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 6b171409-b112-38fe-8946-d83b10d2e49e | -10.6466 | -50.897598 | 2024-10-09 01:26:12 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66fbba7f-4bb8-34be-be22-3fee282050c6 | -11.6806 | -64.0312 | 2024-10-09 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d11b47d3-8abc-33aa-b0f4-ba074e403785 | -12.2958 | -57.863201 | 2024-10-09 01:26:13 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91fb7543-99ed-3f5e-bbae-3e82e8ea536f | -12.2976 | -57.870998 | 2024-10-09 01:26:13 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32331505-ab5e-37c9-a23b-52168b137af3 | -12.8834 | -60.505001 | 2024-10-09 01:26:13 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65952f06-a9ec-377a-ad01-818d5754e862 | -11.992 | -51.0553 | 2024-10-09 01:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 5bd06c9c-a76a-35a6-92e4-2f6bfc3a3743 | -12.0107 | -51.0744 | 2024-10-09 01:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 5a802c23-43a2-3b63-97a2-2bd2a294fede | -12.011 | -51.0531 | 2024-10-09 01:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.8 |
| c7a8e957-337e-39fa-ab82-e0be1ebdfc2a | -12.6628 | -59.790401 | 2024-10-09 01:26:14 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8cf7a2d6-6ab3-348e-87ca-35acc2e353b5 | -12.6643 | -59.797401 | 2024-10-09 01:26:14 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 997728c7-7435-384c-8abc-e481ad072b0f | -11.12 | -53.990601 | 2024-10-09 01:26:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a34126a3-8d77-3b5d-84ac-ff372c02a2fa | -11.1233 | -54.003799 | 2024-10-09 01:26:17 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 813b9064-715c-3284-a734-e494839fda3c | -12.3626 | -59.281101 | 2024-10-09 01:26:17 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91a76132-e332-3dff-894c-0f02f3a0d098 | -13.0716 | -62.5107 | 2024-10-09 01:26:17 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4360acde-e21c-3b0b-93b9-5db4c542f061 | -12.6676 | -63.0819 | 2024-10-09 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e92dab65-f9b1-3a3e-94ac-db4347c3ea40 | -11.1038 | -54.008701 | 2024-10-09 01:26:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54de31dd-a096-3423-948c-529480bed690 | -11.9626 | -57.5844 | 2024-10-09 01:26:18 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e52fcd13-bfc4-38f8-b6af-30293c2601c7 | -11.9645 | -57.5924 | 2024-10-09 01:26:18 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddfb77d5-6318-33e4-b039-a6f3c60e3e22 | -12.3139 | -59.157299 | 2024-10-09 01:26:18 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74ca9d5b-f3b4-3be0-ad7f-d264988676d0 | -12.3155 | -59.164501 | 2024-10-09 01:26:18 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d7bdc06-cfd0-3a37-be85-3b8d57e34b05 | -12.3172 | -59.1716 | 2024-10-09 01:26:18 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| efb91ba3-8e07-3422-ab02-d07fd89b6184 | -12.3041 | -59.159599 | 2024-10-09 01:26:18 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 666b409f-04fc-36b1-9e31-35c886635f6e | -12.3057 | -59.166801 | 2024-10-09 01:26:18 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ae3c99a9-c8fe-3b76-85e8-9e21d16d7d59 | -12.3074 | -59.173901 | 2024-10-09 01:26:18 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ad1d93e-c8e4-3c03-9762-07da3169852a | -12.2977 | -59.176201 | 2024-10-09 01:26:18 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 867aac99-1fb0-3e9a-97de-287ce0079ded | -12.3074 | -59.219002 | 2024-10-09 01:26:18 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a876349d-d0d5-3c4d-a56e-57af5566cb4e | -12.309 | -59.2262 | 2024-10-09 01:26:18 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3cb7d1a-2417-37bd-9a93-5e1924613e08 | -12.6835 | -60.905102 | 2024-10-09 01:26:18 | METOP-B | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b958ed9e-f940-3da2-aa6e-f18472142bef | -11.1248 | -54.303398 | 2024-10-09 01:26:18 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09840b07-1386-3b9c-b44a-9361a11963fc | -12.7501 | -62.269 | 2024-10-09 01:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 93aa5bf1-b551-3702-8f96-2d359d7797d7 | -12.9864 | -62.447701 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f95dfa31-39e2-35b4-a969-1fa94e9cc093 | -12.9881 | -62.455502 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7c5c251-9c71-3cb8-942a-ff7545c81c37 | -12.975 | -62.442101 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd1c408f-8e39-3057-a417-3918768e72d7 | -12.9766 | -62.449902 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 674b90a9-fddf-31a7-8248-bd5ec1a5ec84 | -12.9783 | -62.4576 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 00b729b2-abd4-3258-a7d2-ac18d12afff1 | -13.0149 | -62.630001 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c4598a6-29e4-38d0-b95a-21491f6f1f5f | -12.9652 | -62.444302 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 017cdc28-41b1-3b1e-827f-2d9bd2896324 | -12.9668 | -62.452099 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 50d975fc-41e9-3e02-8594-7fe2c730ccd3 | -12.9685 | -62.459801 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aada17f4-96f5-3580-85a7-6117ec430d5a | -12.9701 | -62.467602 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e6336523-52bf-3367-a039-8ce718a121aa | -12.9537 | -62.438599 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a433968-479d-3db0-8e01-b00b28596faf | -12.9554 | -62.4464 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4420e565-baaf-3ad3-9a8e-e71412dcbcf1 | -12.9603 | -62.4697 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3df2e288-7d17-327b-aa5e-5224ec6ae542 | -12.962 | -62.477501 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8576d144-01c8-3816-a188-090407b4215e | -12.9439 | -62.4408 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77667c3e-4cda-39e0-ab38-e8d8a410f92c | -12.9456 | -62.448601 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 21033fcd-33a9-3831-add0-2954ac38e86a | -12.9522 | -62.479698 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d52e897-2d91-32f2-99d8-0c060ec4d5fd | -12.9872 | -62.644402 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9bbe7af9-1721-3464-8fbf-965dd8695bb5 | -13.0058 | -62.731602 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 16f28e1a-ed2f-3fca-8d57-26aaaa2241f2 | -12.9325 | -62.4352 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f70d6668-23ce-308b-8717-27b1dc89ef87 | -12.9341 | -62.442902 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 329e5b94-b519-3cdf-b986-beb4ebe6c06d | -12.9358 | -62.450699 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bf021829-0cc6-30fd-b698-cb847a7e6222 | -12.9424 | -62.4818 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce1d1d3-debd-32d0-91a6-8a6aefd18acc | -12.9909 | -62.7099 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93dc0905-9006-3929-b4da-2740e53bc7eb | -12.9943 | -62.7258 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cc5098f6-d4c3-383c-b64d-f504eb88fa1d | -12.996 | -62.7337 | 2024-10-09 01:26:19 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6c20d5cc-9b80-35e3-8535-55e2297f95e9 | -12.8591 | -62.8018 | 2024-10-09 01:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 109.6 |
| be4edf17-022e-3358-ad2a-c4bcec276d9e | -12.8779 | -62.82 | 2024-10-09 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 5bfa2120-48f9-3aaa-9364-6849aef54ff4 | -12.878 | -62.8007 | 2024-10-09 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 226.5 |
| 47e87bfe-c7f2-34a8-b6fe-513b50622a0e | -12.926 | -62.4529 | 2024-10-09 01:26:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ccc69ecf-908c-35c6-b7b9-349bb3c8b968 | -12.9276 | -62.460701 | 2024-10-09 01:26:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ca3f2bb9-636a-33b4-92e1-0d9b9738c75d | -12.9326 | -62.484001 | 2024-10-09 01:26:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d1b02947-fdba-3a00-8114-aa9518b82595 | -12.9343 | -62.491798 | 2024-10-09 01:26:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b8739ffc-3032-3cd1-af53-42f3459df865 | -12.9727 | -62.672401 | 2024-10-09 01:26:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8367b455-40c3-3a0a-a244-84ea8c76b735 | -12.9743 | -62.680302 | 2024-10-09 01:26:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0edbadd1-9faf-3195-9fa2-1bc150fc0129 | -12.5581 | -60.8964 | 2024-10-09 01:26:20 | METOP-B | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 103e3123-a6a5-3bda-b6f8-9c7b825b42b6 | -12.9215 | -62.576302 | 2024-10-09 01:26:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 200b7280-c90d-3086-91d7-07523b309923 | -12.9232 | -62.584202 | 2024-10-09 01:26:20 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dca9ef97-45aa-3c85-85ae-1f5decea65cb | -13.3065 | -53.7227 | 2024-10-09 01:26:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cbe6ef80-3fa2-3140-b405-4a80fd882675 | -12.9172 | -62.701099 | 2024-10-09 01:26:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d11736a4-f105-335d-ae67-bfcf7560813b | -12.9189 | -62.709 | 2024-10-09 01:26:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b0c329ce-35a1-36b9-99cf-9037a673be23 | -12.9206 | -62.716999 | 2024-10-09 01:26:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 57540d4b-ddc5-3fa8-bd62-4b4e104ff067 | -12.9223 | -62.724899 | 2024-10-09 01:26:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| df2cac69-bbeb-3d94-9339-e408f07bb584 | -12.9074 | -62.703201 | 2024-10-09 01:26:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eb3a783c-2b15-3a68-992c-217c1a851ed4 | -12.9091 | -62.711102 | 2024-10-09 01:26:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9ea8201f-e189-3dfa-a18b-4a4d159817f6 | -12.8679 | -62.662201 | 2024-10-09 01:26:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae19400-6def-37c3-ba17-b26a28663c00 | -12.8696 | -62.670101 | 2024-10-09 01:26:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 641bfcc6-4319-3e59-8901-200546091048 | -12.88 | -62.767399 | 2024-10-09 01:26:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 874211fe-c97f-3f54-986f-2a27fe2a31eb | -12.8817 | -62.775398 | 2024-10-09 01:26:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7e73518f-7635-3bd1-ab49-1c625180f770 | -12.8834 | -62.783298 | 2024-10-09 01:26:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf7a2ab-a25b-3832-865e-6ef5114308eb | -12.8851 | -62.791302 | 2024-10-09 01:26:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18167112-dc80-311e-9bc8-21d05ac2778f | -12.7592 | -62.248299 | 2024-10-09 01:26:22 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1058f111-f593-38e3-9ba2-7f7fae78e27d | -12.7608 | -62.255901 | 2024-10-09 01:26:22 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fccc0553-ca89-3d86-9d16-11039800240e | -12.8719 | -62.7775 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c5224cce-e7df-35f0-839e-cd7b18f64527 | -12.8736 | -62.7855 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a94e5e07-ead6-38e0-b2f7-e09622866e16 | -12.8753 | -62.793499 | 2024-10-09 01:26:22 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bd9d87e8-ea86-33aa-a168-2bf984713a90 | -12.877 | -62.801498 | 2024-10-09 01:26:22 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8955caeb-a598-3992-befa-e6f630bab752 | -12.8604 | -62.771702 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ebea6b2-10ff-3fc3-975e-d339f33e71f3 | -12.8621 | -62.779701 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c9b9b7a4-1dc2-38aa-bd43-4a1246548b5d | -12.8638 | -62.787601 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 48ad9ded-5393-3fb8-840f-d8911a2273fc | -12.8655 | -62.795601 | 2024-10-09 01:26:22 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 59ae2891-b959-3137-bb6c-227b0a5286f3 | -12.8523 | -62.781799 | 2024-10-09 01:26:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README41.md)
