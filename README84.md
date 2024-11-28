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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6b6e55f-ac49-3a5e-91af-543721bb295a | -3.17337 | -54.31833 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dab353f-da2d-3aed-a814-0d56dc80af95 | -2.73705 | -54.11065 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42952ade-83df-37c7-a5b2-ed0a4d5b6ac9 | -3.49859 | -50.45887 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8f096637-0378-3d6e-92b3-93b0d362802d | -3.23948 | -53.92981 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 09627d7f-78b1-39ac-a875-b64fbabbf103 | -3.10958 | -53.99423 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 656cbe41-34b2-36a7-8206-54957dc17df0 | -3.30972 | -50.28165 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b34e8b26-993c-3987-89c1-9c0e83904174 | -2.90109 | -54.1743 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50b856c1-40dc-37da-ac6f-129c248c0394 | -3.64781 | -51.39357 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 419de983-f7fb-3e9b-beb2-5e0a64285aa1 | -2.82574 | -54.03409 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba9669cd-48af-3104-a112-4743fe61ebfe | -3.96449 | -48.08325 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 83ebaf2e-9bc3-39d4-9f0a-ba4162fa1cd5 | -3.0953 | -54.03671 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a01bfb91-14bd-32bb-a208-c8048542a00d | -3.99965 | -47.91862 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 769582bd-d81a-300c-9efd-6a8e4d5fb2e9 | -3.71701 | -50.54007 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6eeaff68-975c-354b-8741-6419f915a232 | -3.10777 | -50.36769 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 819616c2-d51f-370b-bea9-d4524c8a6b47 | -3.50348 | -50.49375 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ca6f7060-e65b-3df1-96b7-0f01149e800c | -3.71431 | -51.79794 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7c6d104-14d1-38e4-b06d-400e6be90cbb | -3.34687 | -50.51574 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3893bb0-791e-395d-87eb-4bc583c2918e | -2.23152 | -53.69078 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbdf3485-aed7-3ead-b51f-ab994d9d53f1 | -2.97923 | -54.66054 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a46450c2-8da3-3654-b3bb-10bfc153ba06 | -3.39978 | -54.28047 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d469c28-0eb7-3228-954d-a2bd2e6f1487 | -2.7021 | -52.00055 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 02290d43-f482-3c76-a282-0a9d224455f5 | -3.10516 | -53.26721 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| debfb161-447e-3104-b07c-445d8a233dfe | -2.17679 | -52.13273 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04de4425-3b5f-3fc8-9778-4ffb4234f9e0 | -3.10208 | -50.36633 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a27e29c5-a333-333b-924e-8035b3b0e5d4 | -3.56077 | -51.56742 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33cc5415-b92e-3627-aa06-fc75eafaa0be | -2.7372 | -54.13493 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c3055b4-a7be-3b64-8181-8a1d74ab4345 | -3.29856 | -50.35968 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebdf5659-5ffa-38a2-a590-d8673722e643 | -1.98783 | -53.29373 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae95117b-4f0c-399c-aae1-cac202674125 | -3.25041 | -53.63877 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f4b0367b-5169-3a1b-b316-d131a74d9499 | -3.69148 | -50.22864 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0115f784-88a3-3320-aad9-320e271b9444 | -2.18356 | -52.12754 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afe7b1c2-bb66-30dd-802f-c558291480a8 | -3.17647 | -54.32365 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 659dc544-b607-3617-b590-f98d45929173 | -2.86895 | -54.03583 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d55caebf-e4b5-3f45-ab37-23b84052db00 | -2.52992 | -54.0211 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 553fd215-ed21-39c8-a7b0-a3c9dd53e6f3 | -2.80446 | -54.07013 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 383a66c6-395c-39cd-b5e1-956c21235d7c | -2.64489 | -54.27886 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 837918ab-9bbb-36ad-ae6c-d78c3f5ba243 | -5.76107 | -46.26124 | 2024-11-28 05:18:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a361abc9-f437-388b-ad5b-6d96962fe162 | -2.60263 | -53.9709 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2fd750f-b949-3f55-be71-1443649203a0 | -3.24288 | -53.88034 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e01c2817-10d8-3843-aa35-58c9eb0a92b4 | -3.17628 | -50.28348 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0396d99-9ea3-3568-83f3-c8aa3140501b | -3.85614 | -50.12233 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b5607b8-2d18-3518-b444-3ebce44adacc | -6.11938 | -46.59468 | 2024-11-28 05:18:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b3ee1a2-a7d0-3a38-9af8-602d6f04024c | -3.49188 | -50.08708 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e3a8d0a-ab13-3d7e-9c64-031afb72bab5 | -3.32242 | -53.70119 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 43c4ac66-c367-3fa8-a43e-222406437183 | -6.37948 | -45.68931 | 2024-11-28 05:18:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 570699ba-e009-3afd-9721-fad2cbe1c929 | -3.46026 | -50.84455 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6ec2ce9-cb90-3c26-bd0b-8f2226c8687c | -5.9813 | -45.34854 | 2024-11-28 05:18:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 35757581-d55c-33d5-bef5-6dac9a8aca36 | -3.4624 | -54.48332 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03b9d576-3424-339c-9d97-c199c4899ae0 | -2.65209 | -49.50972 | 2024-11-28 05:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee690626-1100-3546-8962-c12420b93bc7 | -3.44277 | -50.00901 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87694f31-8ce3-37a9-9d78-35430aea894a | -3.24914 | -50.77359 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7bcb616e-8f18-3a38-a10e-b25f4293ec9f | -3.11274 | -53.99969 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62c102e9-c570-3c95-8c7b-caa67de82d93 | -2.53657 | -53.97818 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66156708-39cd-323f-b872-24e182d42248 | -3.34362 | -53.28812 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 481aa7f3-d2b7-37e4-be8d-4cb3e3284ee5 | -4.02708 | -49.54422 | 2024-11-28 05:18:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98509fe3-051a-3b4e-b796-6658a24aa710 | -3.61636 | -51.54187 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d6bf149-fbb8-3031-a46b-199ba148a225 | -2.63761 | -51.77423 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 11a49d26-5504-3c7b-9ef7-84d6e8b588a5 | -3.96628 | -48.07045 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe99db06-ee1c-38fb-bfe9-403aa36e0584 | -2.58135 | -53.66324 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d7e8f47b-2c9d-3a90-bf7f-769b6908df5f | -3.37459 | -50.11797 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5a97f62-4d35-3cfe-a18a-ee080e291716 | -3.33605 | -50.07385 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 691eed13-8ca8-3c2f-b604-6201f98e9469 | -2.74503 | -54.03371 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 770ef6ba-4d1f-375d-b57e-4920849d1281 | -2.94808 | -51.58714 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1a91d101-bd2b-38ba-be26-9534b32c64ce | -3.11283 | -53.75908 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa38814e-fad4-3a68-8c0f-7388ae6aa9fc | -3.57666 | -51.55527 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3c466cf-ce75-368a-8a1b-047c103092df | -3.27095 | -50.62243 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 62e4b24d-c34e-3ff7-81c5-33cfe17a73ff | -2.17738 | -52.13929 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15ca0405-61c5-341d-88f2-803a769b159c | -2.59343 | -53.97937 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 390a41ec-19af-36b4-b192-0441ec594897 | -3.08936 | -54.12959 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0d5443ad-6b84-3856-8e8a-18cd9c1419c7 | -3.54802 | -50.18996 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 547a68f5-bc76-3829-9225-dca8b76a22ba | -2.32078 | -51.9613 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e5b4009-919b-33a8-9b14-7725b107f47f | -2.89437 | -53.95706 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29882cbc-b71d-37ae-89a4-ffd4df876817 | -2.97364 | -51.5721 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 264f77cf-ad66-39ad-ab49-7f5ebdb1e0af | -2.83178 | -54.12312 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bd38f69-0367-3a75-9aa8-72b7a0bf2e3e | -3.62342 | -51.49413 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3675b48e-969e-3efd-8fb3-f51ccf059433 | -3.05258 | -53.67626 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db24fe4d-c6ee-3ae2-84f6-b42336c52cff | -3.61585 | -49.89968 | 2024-11-28 05:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6458aa90-c532-3341-a82b-5a170c2966d6 | -3.38185 | -50.10377 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7b28d42-72a2-3fa7-b298-b51509d9cd16 | -2.9496 | -53.72203 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 051e2200-787e-3ee2-a41b-d5975f2e23b4 | -3.59552 | -50.35899 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 77f3787a-4eb0-35dd-b2bc-ffa9c6efd0cc | -2.09868 | -53.35655 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 856f78cd-ae64-314e-aa95-00221356d190 | -2.20084 | -54.52072 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc21258f-006f-3154-986e-ab601d86a452 | -3.5905 | -50.35825 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46fc5be5-785d-3e2e-a050-d8c544b150b1 | -2.83442 | -51.84119 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 03922625-a8b7-3f0c-8f97-2288195c91f7 | -3.67794 | -53.55622 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff26de1d-21a5-3d4b-b93e-23acfc3f2a19 | -3.4156 | -54.17474 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 811cc411-1997-34a5-8e5b-6ccbf11b4d25 | -3.24991 | -50.76828 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dedc8b2d-2cc2-31fa-8f9b-3cf4b0a02825 | -3.38053 | -50.11282 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e49286bc-509e-347e-bd2b-56022a84712e | -2.58957 | -53.97878 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 71e92849-bd1c-3f18-a92c-6cc8b525f83f | -2.24933 | -53.62726 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3f8ef1ad-0633-353b-8d25-d3cb8ec9c04e | -1.92191 | -54.4387 | 2024-11-28 05:18:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8cad0c7d-95c4-36d8-a186-875a340ddd5f | -3.54428 | -50.18932 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bfb7754-3364-3dd9-b79c-fceba1f54395 | -1.98729 | -53.29719 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa5e5123-b070-3c16-b74c-adceb2d8b75e | -3.38141 | -50.10679 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a702516d-0bb7-3c4d-ae94-e4d6ce726650 | -2.8294 | -54.11302 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8631906-3658-322a-9663-e8bbfb5e4d96 | -1.63022 | -55.71268 | 2024-11-28 05:18:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17d1b0ae-1c00-3f73-a5a6-ed7b867a6f10 | -2.87234 | -53.99846 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfe1e043-b477-3feb-815f-3150a459cc8d | -2.77668 | -52.90642 | 2024-11-28 05:18:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ddc631c-6b3d-3b40-8233-24424545d93b | -3.72116 | -52.014 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e220ef3-d0c5-328a-a766-0c6a38b324ff | -3.03816 | -50.97854 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README85.md)
