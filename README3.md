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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 866181f6-5860-3e7e-97fa-69d7f4aefab2 | -7.2219 | -43.0682 | 2025-07-02 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| b7b664e4-68ba-3e3a-8eaa-a7c76bfd867f | -10.883 | -56.4567 | 2025-07-02 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| bf66722d-6fe1-39d9-88ca-4793bcd7f23a | -7.2217 | -43.0917 | 2025-07-02 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 247.2 |
| 5f0fc7c9-9952-3c3a-853f-b8e08bf7b874 | -10.8832 | -56.4367 | 2025-07-02 00:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 720b1c6d-65b0-3ee8-ab7b-a08b94752bb8 | -7.7944 | -44.0377 | 2025-07-02 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 8f711388-484d-32aa-86ec-509995a1b2e8 | -7.2217 | -43.0917 | 2025-07-02 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 262.5 |
| 27fb7ad1-4703-3929-be85-de0377347319 | -16.3356 | -49.9289 | 2025-07-02 00:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| d8a01222-98ba-38fe-b75d-044491f2c8a2 | -7.7758 | -44.0164 | 2025-07-02 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cf5763f1-309a-3a3b-9985-66ff402cc093 | -7.2214 | -43.1153 | 2025-07-02 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| d790d4c7-9c94-3640-87bb-918a38586028 | -7.8135 | -44.0126 | 2025-07-02 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 31f11717-06c9-35d5-885f-ef701661d337 | -7.6239 | -45.7447 | 2025-07-02 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 87dccd38-593e-359d-a027-55d47dc86f03 | -7.2031 | -43.0701 | 2025-07-02 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| af0eec77-1a35-3866-8806-43da9ff9fd60 | -16.3552 | -49.9256 | 2025-07-02 00:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 8f9262eb-c06d-3a55-8166-0ededd2974c8 | -7.2028 | -43.0936 | 2025-07-02 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 263.6 |
| 700c3cdf-48b6-39fc-b2cb-ecdc24cbc0f0 | -6.7093 | -51.4165 | 2025-07-02 00:50:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| b653f5d0-f46d-32b9-acde-25e2857b8c14 | -7.7947 | -44.0145 | 2025-07-02 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 242.4 |
| 59a38106-fd06-37c5-aa8f-18a35dcffb98 | -7.2219 | -43.0682 | 2025-07-02 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 3ee1ca0c-54a4-32c6-8fce-8894a18e17d3 | -3.0355 | -49.4476 | 2025-07-02 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2acac6a3-a1ab-373c-9545-f824fad73334 | -7.6048 | -45.7689 | 2025-07-02 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| c567f866-9243-3c61-acbd-19a0f4208437 | -7.6051 | -45.7464 | 2025-07-02 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| f6018803-cc6e-3ebb-9ba2-efcc5f29b87a | -7.8133 | -44.0358 | 2025-07-02 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 145.9 |
| f9427592-9d4c-35fb-b793-6ce18b6ebe16 | -10.883 | -56.4567 | 2025-07-02 00:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 13d41af6-e373-34bb-ba78-99e978d5302d | -7.6051 | -45.7464 | 2025-07-02 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 7a3150c8-7c49-3b99-8459-c54be3572861 | -3.0355 | -49.4476 | 2025-07-02 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a33b5dfa-1d60-3049-a23c-dbc3b7d4fec2 | -7.8133 | -44.0358 | 2025-07-02 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 0ded884d-83cf-3952-814e-12f8f61421a7 | -7.7947 | -44.0145 | 2025-07-02 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 5aafad5a-7f1e-338b-9cc8-e2d04adcc364 | -7.6239 | -45.7447 | 2025-07-02 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 488cc21e-abe5-3f36-a501-75376a270915 | -7.2028 | -43.0936 | 2025-07-02 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 256.3 |
| bd474f92-edb5-3a22-9342-4ad6a0566308 | -6.7093 | -51.4165 | 2025-07-02 01:00:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 63dcdcb5-05b5-3ad4-adb9-b5b2b4bbcbcf | -3.0356 | -49.4264 | 2025-07-02 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| bb33eeab-6da5-3034-8c11-b584ed64ddad | -7.8135 | -44.0126 | 2025-07-02 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 188.8 |
| f70d9ad4-fe70-31e4-b119-8685e933afb4 | -7.2031 | -43.0701 | 2025-07-02 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| e2d6e48e-8c64-3fce-ad65-0d9c9d1f0a27 | -7.7944 | -44.0377 | 2025-07-02 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 5384ce8e-d93d-3c41-ab77-3964088b12b1 | -7.2217 | -43.0917 | 2025-07-02 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 274.8 |
| 2d9dc6b3-78f2-329e-bd20-382b21e0d775 | -7.2219 | -43.0682 | 2025-07-02 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 9075b11c-c15f-36e6-8e06-2e3d4037b48c | -10.883 | -56.4567 | 2025-07-02 01:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d6ad47fa-d244-37b4-b2fe-0dacbcb5ce27 | -10.883 | -56.4567 | 2025-07-02 01:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a3ee2aa1-6d5e-3c9c-bd56-5d31233d4f5b | -7.2031 | -43.0701 | 2025-07-02 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 38143786-90e5-3c10-a26d-acf2f2b4c9f1 | -3.0355 | -49.4476 | 2025-07-02 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5fea5559-8985-3050-b899-01ef2c2db6f2 | -7.7947 | -44.0145 | 2025-07-02 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 8ed5ffb8-81b5-3b22-841f-10b848750a4c | -7.8135 | -44.0126 | 2025-07-02 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 161.2 |
| e436db5d-a012-33e1-9e45-3dd6732da10f | -7.6239 | -45.7447 | 2025-07-02 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| e1b563b4-8a59-3bf5-8340-85f6c8a3acd2 | -7.2217 | -43.0917 | 2025-07-02 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 209.3 |
| 85ca85d6-59f6-3e85-a1fb-b87ce4055c83 | -7.7944 | -44.0377 | 2025-07-02 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| b287ba56-35ae-3859-9e86-679b274497a9 | -7.8133 | -44.0358 | 2025-07-02 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 87a97835-f0ca-3bf5-9916-646135ec828f | -7.2028 | -43.0936 | 2025-07-02 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 209.8 |
| ce24dbdf-89e8-353c-be8f-0f7016de88b8 | -7.2219 | -43.0682 | 2025-07-02 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 255870f7-162f-35db-920d-1c3ecdc4e088 | -6.7093 | -51.4165 | 2025-07-02 01:10:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 4385bd37-2402-3a09-9b54-639f9fa63c98 | -7.6051 | -45.7464 | 2025-07-02 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 62ae0dfd-57de-3ec8-97e3-42946c456c49 | -10.883 | -56.4567 | 2025-07-02 01:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b308c7fa-6007-393f-a2df-e8e355800bd0 | -7.8133 | -44.0358 | 2025-07-02 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 49aff767-250e-34af-a0f8-9f34ac56a4ee | -7.2028 | -43.0936 | 2025-07-02 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 215.5 |
| 98f7ba5f-1c4e-30af-87af-fcc3e8fb4cb7 | -7.7944 | -44.0377 | 2025-07-02 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 2ee0513d-5faf-31c8-860b-be51ca9fd59a | -7.6051 | -45.7464 | 2025-07-02 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| c949d181-019a-33cd-8114-8d242581a3d5 | -7.6239 | -45.7447 | 2025-07-02 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 73411370-6429-388c-8714-4273924fefb1 | -7.8135 | -44.0126 | 2025-07-02 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 4e48d3d7-045d-3345-b5ac-e4737fab50de | -7.2217 | -43.0917 | 2025-07-02 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 181.4 |
| daf3354f-163e-3f08-b6f3-ebb2a999d416 | -7.6053 | -45.7238 | 2025-07-02 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| cb66e0e2-41b3-33f1-8f78-4748a21685f1 | -7.7947 | -44.0145 | 2025-07-02 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 228.0 |
| 1c523eda-ef11-3249-9472-a04559270330 | -6.7093 | -51.4165 | 2025-07-02 01:20:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d8d4a9fb-8549-34f1-b633-1db132cf9751 | -3.0355 | -49.4476 | 2025-07-02 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 49f1fdd6-f049-38f0-9a86-a6ce11453f2c | -7.2219 | -43.0682 | 2025-07-02 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 4dc4d689-301f-3fce-8cd1-ad8920a904b5 | -7.2031 | -43.0701 | 2025-07-02 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| 652d4ed5-40a8-3a44-9561-a6c5c4eaf663 | -7.8135 | -44.0126 | 2025-07-02 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 269.7 |
| 040855ab-c4b3-3e55-9c67-d205e0a5b452 | -7.8133 | -44.0358 | 2025-07-02 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 1dab361b-d4f9-3ec6-a476-de1aad4126e5 | -3.0356 | -49.4264 | 2025-07-02 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a838ff73-e43f-362b-8b18-93a6dc3f68fe | -7.7947 | -44.0145 | 2025-07-02 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 9f88be47-a03b-330c-802b-107762736edc | -7.2028 | -43.0936 | 2025-07-02 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 272.4 |
| 0d889808-6046-3271-a47e-326ba117b88e | -3.0355 | -49.4476 | 2025-07-02 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4daca073-c947-389a-b0c4-b0a438283b0f | -10.883 | -56.4567 | 2025-07-02 01:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 6c4c0c92-3061-31d1-a70b-05c62ac449fa | -7.2031 | -43.0701 | 2025-07-02 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 146.4 |
| aeb89876-58dc-38b0-9430-3e0d93af883c | -7.6239 | -45.7447 | 2025-07-02 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 4b067a7d-cefb-3a17-b287-9d82a05f1172 | -7.6051 | -45.7464 | 2025-07-02 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 06c614c8-b2b4-3e22-a290-d93031b5ed0f | -7.2219 | -43.0682 | 2025-07-02 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.8 |
| a18e961d-85c9-3d72-ad65-65f176185c63 | -7.2217 | -43.0917 | 2025-07-02 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 271.9 |
| 492365d5-225e-3f6f-90c5-e726c326b424 | -7.7944 | -44.0377 | 2025-07-02 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 293ec8cc-9d8f-33b2-845a-53f91a5daca6 | -6.2945 | -43.6659 | 2025-07-02 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| eaa9d35b-0901-36a7-9172-5772b40caf39 | -6.2943 | -43.6891 | 2025-07-02 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 63ce0ed7-40cd-3663-8d6f-394ab61c28d3 | -6.7093 | -51.4165 | 2025-07-02 01:30:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 973294e2-70be-3e09-b7cc-35511e8955a5 | -7.2219 | -43.0682 | 2025-07-02 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 84dfbc5f-cac8-38e8-a01c-140ca267aa5a | -7.7944 | -44.0377 | 2025-07-02 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 48a9b784-6f39-3043-ab5e-4917b6431260 | -15.5327 | -49.9927 | 2025-07-02 01:40:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 106.6 |
| f6ae43c6-d2f3-3f0e-b831-86a4fc3993c6 | -7.8324 | -44.0107 | 2025-07-02 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7d273606-99f1-3d32-91c3-beb619073bda | -10.883 | -56.4567 | 2025-07-02 01:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 930fc428-d503-3e6c-96d8-0f55a39e581b | -3.0355 | -49.4476 | 2025-07-02 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5fdb5664-8b8e-3fd1-9c56-8cbe6af28b7c | -7.7947 | -44.0145 | 2025-07-02 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 223.9 |
| 31f481ec-2958-35b6-8f25-aa775fd0c3b9 | -7.8135 | -44.0126 | 2025-07-02 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 274.7 |
| 422b48ec-11a4-3e7d-8d26-1c214f80e8e4 | -7.6239 | -45.7447 | 2025-07-02 01:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 3d668178-4083-3216-b649-8735762d8b9c | -7.2031 | -43.0701 | 2025-07-02 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 147.6 |
| 0c086a53-7be4-3506-a07b-bca753ca5234 | -7.2028 | -43.0936 | 2025-07-02 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 288.9 |
| 0490fa5b-a4fb-3f72-92e3-a39a6b5efd88 | -7.6051 | -45.7464 | 2025-07-02 01:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 6b24237c-85d7-3062-8448-0ac6abc92c6f | -7.8133 | -44.0358 | 2025-07-02 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 216.0 |
| fca287e8-49ed-31b5-bd31-155ab5774dee | -3.0356 | -49.4264 | 2025-07-02 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f8754772-aef4-3a2f-b32e-5936ae100a73 | -7.2217 | -43.0917 | 2025-07-02 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 246.2 |
| c475d4c7-2a6c-31e6-9e61-d0cfb44dce27 | -7.2217 | -43.0917 | 2025-07-02 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 212.3 |
| a00905ac-ec39-3e8c-a553-e3fdff5f8cc4 | -7.8135 | -44.0126 | 2025-07-02 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 289.9 |
| f1219fe0-7ebb-37f9-972e-7cec2ccd18be | -7.6239 | -45.7447 | 2025-07-02 01:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1da2ff99-c628-3b69-ae27-a71cbbb5fe68 | -7.2028 | -43.0936 | 2025-07-02 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 227.3 |
| f9232ab7-5a7d-3419-a863-0aa2a4931fb3 | -7.8133 | -44.0358 | 2025-07-02 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 253.5 |
| 29008de0-1e7d-3761-9581-e892afbaedca | -7.7944 | -44.0377 | 2025-07-02 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 154.1 |


[Clique aqui para ver as próximas entradas](README4.md)
