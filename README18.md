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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86a7c811-f464-30af-ac8f-a9ee8b1805fd | -18.2731 | -56.642 | 2024-10-18 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 20701b20-8539-3ded-a394-421d0b1c4232 | -18.2735 | -56.6211 | 2024-10-18 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.9 |
| c4835b30-9a09-31a0-9b81-ae3a03c7a3f3 | -19.61769 | -57.01302 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| e42a89a3-3147-3fd8-8a6b-fa8c5ad76289 | -19.61296 | -57.12477 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.3 |
| cc377bfa-35dc-3354-9c38-57d676a6f32f | -19.61091 | -56.97892 | 2024-10-18 02:17:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 0e4461a5-85e6-3fa2-9e74-685823723f7c | -19.60916 | -57.02 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 184.2 |
| e5476c12-e480-3970-8f45-0993c10d5219 | -19.60872 | -57.05048 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 409.8 |
| ca93a6d7-a814-3a3f-abba-cd2f622b31b7 | -19.60648 | -57.12114 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.8 |
| f2d4e3dc-8f1f-3c61-8d45-d638b8412e4b | -19.60259 | -56.98584 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 0eb3e4ee-6ea8-3165-90fd-e4c8882f8555 | -19.60196 | -57.01662 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2843.0 |
| 552c0843-ee32-354e-bc08-f5dbda628a73 | -19.59999 | -57.05755 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 294.4 |
| b570c9fc-8340-3e13-b588-7f7cda567cf7 | -19.59978 | -57.0877 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.2 |
| a118b3e3-e1ba-3d1c-95fb-d5275cb4fbac | -19.59515 | -56.98251 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 414.8 |
| 24d068f7-21bd-3ed2-8ca5-ecbd40c2ba64 | -19.59344 | -57.02364 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4713.0 |
| 03fcad83-449b-37ed-844c-835f23dcc0c5 | -19.59303 | -57.05405 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 295.7 |
| 33da385e-cc0b-3d7e-bef7-5805c8feb364 | -19.58683 | -56.98948 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 921.3 |
| 07bf9ace-db8b-3705-b8a1-5787f0598594 | -19.58623 | -57.0202 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2260.9 |
| 14490637-6638-37e2-87ac-c4fc9e6e0692 | -19.57938 | -56.98611 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.5 |
| aa2e879f-16de-3ac1-a8ae-d9af51219175 | -19.57772 | -57.02726 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.2 |
| 708282c3-deff-30c4-be96-25555698092c | -18.66467 | -57.32872 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.0 |
| d09e1059-7ca2-3cd8-9f0f-47dba8861320 | -18.65588 | -57.33743 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.7 |
| cb1384aa-212f-31d7-af24-eeafb94fe7b0 | -18.26351 | -56.6113 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 5dd82df2-6e21-3376-925f-04e6e57ec1fc | -18.25455 | -56.6535 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 209.1 |
| 5079a566-bd0e-3c09-8c39-d49eea21e5f9 | -18.25025 | -56.65952 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.1 |
| 88a55dca-f0d3-38dd-a794-a74bf40bd594 | -18.24689 | -56.61507 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 185.8 |
| c663c909-d887-3f98-acd6-78a17cb22dc2 | -18.24283 | -56.62102 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 174.4 |
| 24f4109b-65e7-36ac-90cf-3e7cc5f0de8f | -18.07479 | -57.361 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.9 |
| 7bcb9b9e-146f-3a57-82f6-625b467d4dd4 | -18.06681 | -57.35589 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.1 |
| 25a94065-0553-3f75-8dc7-a61c10f14943 | -18.007 | -57.26771 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| a3a35cae-57f7-3feb-83f9-c7ba5ba136b1 | -18.00015 | -57.23267 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.7 |
| 2712211b-06e2-30d6-9783-86430d7fc4eb | -17.99955 | -57.27443 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 173.7 |
| 3f769f5f-4d52-37b4-8d6c-50146d53ab1d | -17.99785 | -57.30603 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.3 |
| 089c16c9-365d-3890-8bf7-e6d6123ef131 | -17.99102 | -57.27124 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 306.0 |
| 7d13f72b-0142-3b10-804b-a5e75bd9710e | -17.98357 | -57.27797 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 344.3 |
| 0ce20f7a-f6b7-3e4b-b17a-47d329f194e9 | -17.9769 | -57.24286 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 196083a8-e62a-3238-a0f4-a35839e40f4d | -17.95906 | -57.27826 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.5 |
| 030e41b8-72bc-3732-96a7-fad40df81ec4 | -17.9521 | -57.24326 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.8 |
| b5246282-bda7-3caa-83d7-61e24c2af8ef | -17.92252 | -57.44226 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.0 |
| d7d24396-590a-3bc9-9216-47edfaac63bf | -17.8899 | -57.2254 | 2024-10-18 02:17:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 6c435939-d95e-3b90-8af5-46f86665c546 | -17.23597 | -57.30588 | 2024-10-18 02:17:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 7d490903-b826-3328-a164-06548591f528 | -17.22595 | -57.3028 | 2024-10-18 02:17:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 03176a64-57ad-31c5-90bc-34459aacad16 | -17.21978 | -57.30942 | 2024-10-18 02:17:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 2b83a633-a387-3de6-9d5a-35cc02236e67 | -17.01742 | -57.4764 | 2024-10-18 02:17:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.3 |
| cad6309a-c5dc-3e45-8c7c-b393288dd967 | -17.01048 | -57.48493 | 2024-10-18 02:17:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| d4d6a6a4-758f-3c61-9ded-0fdcdb4778da | -21.9662 | -49.7186 | 2024-10-18 02:17:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.3 |
| af6652b9-09ff-367f-94b7-577948470110 | -9.95731 | -68.91348 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a10a9bf5-b774-3759-96c4-be4c410c6596 | -9.8843 | -66.79096 | 2024-10-18 02:19:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 28.0 |
| f64dcc7d-ade1-344d-9a9f-51dbf9b33f0d | -9.87874 | -66.79816 | 2024-10-18 02:19:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5debfcb0-b8a1-3d8a-8e3e-1733da0b79e5 | -9.8773 | -66.78816 | 2024-10-18 02:19:00 | TERRA_M-M | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cadcdcc5-5b81-3df0-bb34-a0e4b576e600 | -9.70974 | -68.39696 | 2024-10-18 02:19:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f4e7378-ff5e-3ce1-9814-65553c5ab4e8 | -9.67679 | -68.54797 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c403f37c-2a03-3467-8ed0-083e4a38167d | -9.67195 | -68.59096 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 406b1831-cb36-3139-b9d6-378dcd6effa2 | -9.66695 | -68.55521 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d03133ae-2d0f-300d-879a-ea894e46e123 | -9.65656 | -68.73886 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 89e17a39-e469-3431-a6f3-78de223b876c | -9.65585 | -69.05708 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 503df344-8a77-355d-a6e1-a8cf6848ae71 | -9.65461 | -69.04817 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a5818070-13e2-3c1a-80ca-4a36eb9dcb1a | -9.65309 | -68.52074 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e0a065d0-2382-319a-b553-c0506f2689e6 | -9.64149 | -68.69557 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b2377fcd-7e00-3410-9a69-49169aa5b3c3 | -9.64024 | -68.68665 | 2024-10-18 02:19:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f383e521-ea54-3c38-b8b5-66f300fee9fa | -9.57538 | -66.17867 | 2024-10-18 02:19:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 9a8065a6-cd17-323e-894e-5225dc731c39 | -9.56571 | -66.18015 | 2024-10-18 02:19:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.7 |
| bbc7b1d0-27e9-3b60-837f-b4d61bd9113a | -9.56413 | -66.16939 | 2024-10-18 02:19:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| af527c30-fbbf-35c1-bc18-a3e27a36e034 | -9.53431 | -68.71754 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b1e25a82-1b04-37ee-bfb7-7f34b830a824 | -9.52288 | -68.76468 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 422b1d09-bbce-3123-8b2d-b8b954ebfe90 | -9.51664 | -68.72012 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 69b556c1-adcd-35f9-ab58-f0db1ed292f8 | -9.50168 | -68.48533 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 168cf096-2dd5-3a6c-82f7-6c6b7fe2a234 | -9.47296 | -67.06585 | 2024-10-18 02:19:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 941fcf52-d9f9-350a-8a8f-3b1274861279 | -9.47171 | -68.47727 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33d47c14-8632-325c-81c2-b39b151ea7c0 | -9.47153 | -67.05607 | 2024-10-18 02:19:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79a2ecf4-31b7-332b-b0a7-5ee5ebe317c2 | -9.45381 | -64.5746 | 2024-10-18 02:19:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3b709788-2785-354a-8de5-d64b1ae3e346 | -9.4502 | -67.15469 | 2024-10-18 02:19:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a08182d-fab3-38c2-b5c0-369804bb206e | -9.4493 | -64.56705 | 2024-10-18 02:19:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d8266803-82af-32e9-a1ab-89a6b6354058 | -9.44881 | -67.145 | 2024-10-18 02:19:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 42167d07-9e66-3e46-b224-38decb100f9e | -9.41679 | -64.57223 | 2024-10-18 02:19:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 75eebc76-05f3-38dc-8dd1-bb05f9bece60 | -9.40205 | -68.23969 | 2024-10-18 02:19:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e6a3fc0-2686-3632-b097-10679758c205 | -9.3965 | -68.98588 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a4f7713-f960-3554-84de-c7e27c790644 | -9.39448 | -68.31444 | 2024-10-18 02:19:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa0be4fe-31d6-3ceb-8edc-dd1b9caea67b | -9.39321 | -68.30543 | 2024-10-18 02:19:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3796211c-97b4-3a14-a942-5744e14aa31f | -9.37673 | -68.31705 | 2024-10-18 02:19:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d3a8f806-ff71-3d42-968a-ee1d4cfb936c | -9.25871 | -68.33749 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b381d71d-d1b3-30d0-a138-45eb8a08bede | -9.16648 | -67.94302 | 2024-10-18 02:19:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aa595ec3-4ea9-3945-86fa-7b4c4430a7e5 | -9.16559 | -67.67852 | 2024-10-18 02:19:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 284c7f8e-a3a3-31bd-9b0e-b0b6a5a624c2 | -9.13994 | -68.80515 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 3fd8c39b-5b96-33b6-8ca3-6c66b1e3a124 | -9.1387 | -68.79624 | 2024-10-18 02:19:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b78e0aa1-68a0-3680-b8b3-e9b69f041637 | -8.97375 | -68.47104 | 2024-10-18 02:19:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 280419d3-2cc4-3d99-93d4-0521fa133f56 | -8.97249 | -68.46207 | 2024-10-18 02:19:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0c6621fe-0f85-3b21-a2f5-a3b22a21981e | -8.84987 | -69.43402 | 2024-10-18 02:19:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 13e665e8-d890-3ebd-a5f5-93d6d5906fa4 | -8.80601 | -67.61642 | 2024-10-18 02:19:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d6012e57-a6e8-3d91-b7bb-216e68e31933 | -8.797 | -67.61398 | 2024-10-18 02:19:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 946b1922-5fbe-383d-9e77-c8764df1bac4 | -8.71711 | -69.5321 | 2024-10-18 02:19:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a9a994e2-1591-3217-97ae-edd1ef302135 | -8.65271 | -69.60178 | 2024-10-18 02:19:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7246a956-9b25-3d32-bb47-7d41f8945b57 | -8.61594 | -69.74113 | 2024-10-18 02:19:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c2a99bbb-4e0d-3367-a21f-2c0cef8df361 | -8.55752 | -69.98497 | 2024-10-18 02:19:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f000525c-d334-30df-a66d-ee7479446a26 | -8.51076 | -70.24872 | 2024-10-18 02:19:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cda3938c-dda0-3efe-90f8-276c24b77e1d | -8.50179 | -70.24998 | 2024-10-18 02:19:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be249896-8a06-3c13-b8df-4dcce29a5f68 | -11.02758 | -68.46534 | 2024-10-18 02:19:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5530e738-b499-34ed-a817-36b496c1a3f4 | -10.90645 | -69.51994 | 2024-10-18 02:19:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| db6e87e2-ce0c-3e26-bb2f-e417ccc5c4c7 | -10.87967 | -69.52375 | 2024-10-18 02:19:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 35d91b80-c96d-306e-8830-1065d88248d6 | -10.8552 | -69.14837 | 2024-10-18 02:19:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8495d12-4625-3a7f-9c76-2a3d05a31a5a | -10.85453 | -69.40656 | 2024-10-18 02:19:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README19.md)
