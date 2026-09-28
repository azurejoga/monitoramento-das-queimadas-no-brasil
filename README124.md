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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a814b3c-fb83-3eda-b87a-0780af27a8ca | -1.43256 | -48.88681 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ed073c2d-2f31-32fc-859a-efb760ac794b | -1.43866 | -48.90024 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 36687acf-a037-3a50-93c4-0b73f55870ff | 1.88904 | -55.57361 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0504cb69-9dde-3f8b-8384-75f6856ce208 | 2.3775 | -51.00948 | 2026-09-28 16:28:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 389f74ea-b8dc-3335-b0b7-84371169dd00 | -1.44022 | -48.91076 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52053981-51c6-388c-a301-0b8c20944abb | -3.06851 | -44.52172 | 2026-09-28 16:28:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0383aaab-eab8-352e-ba8b-4d12a4f013bf | 0.87706 | -50.78 | 2026-09-28 16:28:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e23c8789-9086-389c-9c77-139dc1c18448 | 1.8838 | -55.56803 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 68b40e0c-7973-3044-8c5b-210ea6f6e3ea | -1.29543 | -49.05683 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35e55eab-8a24-3807-83aa-b6dd539c4d1b | 1.84942 | -55.58997 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f1e393ac-7124-3610-ab7e-d379f4ab3ba4 | 1.84592 | -55.5965 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| cacf5edb-6b9b-3626-b2e1-e7377c89c823 | -2.09339 | -49.55895 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3e8a9322-133b-3fde-a7f2-adbde5ff0d61 | 0.49263 | -50.96805 | 2026-09-28 16:28:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 14f7315e-e4d7-392d-b06f-6566a1a42344 | -1.52722 | -50.22715 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9b29e23-066d-33be-9400-5a7c2cf9dcbb | -3.14712 | -54.08085 | 2026-09-28 16:28:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 9ef7d57d-a3b3-3518-9ab8-8668b7bb087e | -1.30548 | -49.48854 | 2026-09-28 16:28:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa503a45-6d83-3b34-b61e-6b3868d69cda | -2.15004 | -48.87536 | 2026-09-28 16:28:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7291bfd6-607f-3f00-a6e7-540ac1db0ab8 | -1.54833 | -48.20794 | 2026-09-28 16:28:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0ba2cc1-c183-39f3-bdae-3a66df414a84 | -3.20174 | -51.03842 | 2026-09-28 16:28:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 55899720-16de-37a3-b1cb-7371f2ccfe6a | -1.43412 | -48.89735 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3584f307-f20c-3d13-8de0-770369031fc2 | 2.09098 | -55.87965 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 67a79384-3eca-3747-8a27-766ef6d948a3 | 2.0668 | -50.74395 | 2026-09-28 16:28:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 88063be5-51d2-3c39-9850-90f140ecf57a | 2.45003 | -51.00364 | 2026-09-28 16:28:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c5019e85-954a-33a1-9b8f-3d59a1c71812 | -3.15241 | -54.07603 | 2026-09-28 16:28:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| a192df35-4a07-37e4-a8ca-9922c4eb7c3d | 0.63368 | -54.37714 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 458748da-a214-3df1-bba9-7c533061a5f7 | 2.0841 | -55.88334 | 2026-09-28 16:28:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 55c7cf9b-bebc-328d-ab9b-7a85252935e1 | -3.26231 | -44.6326 | 2026-09-28 16:28:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d5efee95-ff1f-36c4-b3fb-8981b81feb3e | -3.00118 | -43.07578 | 2026-09-28 16:28:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 276aeaf5-bc31-383e-9a57-3e21e748e55f | -2.28699 | -48.76014 | 2026-09-28 16:28:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ad13d6cc-ba80-3ac1-bd00-b60a8e28f139 | -0.49512 | -49.12861 | 2026-09-28 16:28:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0e2e9bad-5c78-3213-b255-b1920383fd7d | 0.63309 | -54.38094 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d5ecf93e-e08c-3399-9e33-baeecb1a9d9c | -1.46861 | -48.93531 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c3fafdce-e168-3595-bd47-a93ee0670fde | -3.76426 | -51.83971 | 2026-09-28 16:28:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03bd2c6d-4d38-323a-855c-db3a86a5da1c | -2.06013 | -49.53635 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c7907ca4-9609-3cc8-b91e-26fd956a255c | 1.72404 | -50.97948 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b125db2e-346f-3ab8-ba10-4fe46f786350 | -1.75217 | -46.47201 | 2026-09-28 16:28:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 64d9b04c-0735-375c-800b-07a0d8bd1ccd | -1.22889 | -54.12142 | 2026-09-28 16:28:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 14e143ce-52bd-37d0-b70f-56f197c86225 | -3.10416 | -42.92851 | 2026-09-28 16:28:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 860c2594-5df1-396f-81f9-774495a304ba | -1.4324 | -48.89495 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e6e3af5-873c-37a8-bc44-1ccc9ee33cea | 2.07683 | -50.74903 | 2026-09-28 16:28:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 45a312ff-8000-320b-b837-f6a052e4a9ed | -1.77606 | -53.76395 | 2026-09-28 16:28:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a71472c4-67bf-372a-9c38-f5926e2a45e8 | -2.01489 | -49.87683 | 2026-09-28 16:28:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ab7b3a2a-ca7f-3bde-a653-b562419cd348 | -1.43463 | -48.90085 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6fa84d60-f4f9-3ec0-84fe-19aa35367584 | -2.81585 | -51.34004 | 2026-09-28 16:28:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4fda94ec-4dd8-34a0-976d-5069ee7be084 | -0.50668 | -49.12327 | 2026-09-28 16:28:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c2f72c54-f426-39a3-87d0-dbdaf25ab4ce | -3.21132 | -51.03703 | 2026-09-28 16:28:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a4a879b6-5def-3401-8f31-e13eef5ff839 | 0.63932 | -54.37815 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85d0243e-e34b-3891-a69a-9d4054b14f96 | -1.62732 | -50.1478 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bcd4b6bf-cfc3-3937-b510-ea56d88b464e | 2.07543 | -50.7453 | 2026-09-28 16:28:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a9852e31-f382-3459-894e-460f574674c7 | -1.55088 | -50.42076 | 2026-09-28 16:28:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 2b76da35-b67c-3115-8b04-fc46999d2df9 | -2.65662 | -43.55354 | 2026-09-28 16:28:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69b62d37-9730-38e3-a665-5a4a04058d51 | 1.83918 | -55.60013 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 34448a3f-ed11-3654-91df-3fe7f3b810dd | -1.27752 | -49.37264 | 2026-09-28 16:28:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3194f320-747b-3882-90eb-4429b91491de | -1.61776 | -49.99073 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d79d13fd-6b3d-34d8-8568-d5777e215a7b | 1.72239 | -50.96171 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 42311c3e-5882-3032-b9da-095c501e1afa | -1.03151 | -49.23627 | 2026-09-28 16:28:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6659eca4-369b-35cd-bd88-6c7770232470 | -1.6485 | -50.46082 | 2026-09-28 16:28:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d235e4bb-c4f6-34f9-8336-cc38fc6f59cf | 1.90102 | -55.57559 | 2026-09-28 16:28:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 529e8731-29f7-3a15-ab61-a7733a3b5a48 | 2.37818 | -51.00528 | 2026-09-28 16:28:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c27a9b37-ebef-3df9-9f94-a73ed5941876 | 1.8452 | -55.60102 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c1776b08-9178-3ab9-ac03-26876818ba49 | -3.06904 | -44.52522 | 2026-09-28 16:28:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 744a38be-7458-394f-a96e-018bbe554dc2 | -1.7032 | -49.84024 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5fcb1c37-4029-32b7-9c26-5b5bdd7b025a | -3.60702 | -49.45651 | 2026-09-28 16:28:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 500e9422-4235-3c9f-b07f-a992ec619ef2 | -2.29506 | -48.75892 | 2026-09-28 16:28:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dfa76ca8-58cd-32db-b1d3-5e5760ce7066 | -2.01426 | -49.88403 | 2026-09-28 16:28:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d89ed1db-caf1-3558-9ea1-97f1a8d8fa04 | 1.73355 | -50.97649 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b4cf6211-b1be-371b-9904-d6e40f73dc59 | -3.2784 | -44.49641 | 2026-09-28 16:28:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 44c84704-2488-38d1-a83d-f3759c1bd31f | -1.43186 | -48.89145 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2c31220e-1980-36ba-9ded-9f4902c6055f | -2.92796 | -42.86373 | 2026-09-28 16:28:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 05537680-e2b2-3998-b9d3-f292b6a9cf8f | -0.97409 | -48.11276 | 2026-09-28 16:28:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7f5cb6dc-bc04-3286-9101-377c7c705395 | 2.09023 | -55.88128 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 66f7b96e-74fd-3501-8f11-56c54917542b | -2.05105 | -49.53368 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fc0775bc-4845-3b94-bf2f-e9a244470d52 | 1.48106 | -55.72014 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f5eea763-bd76-3c8e-a1d3-fb9ee7ab9d6d | -2.01732 | -49.87517 | 2026-09-28 16:28:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7b80320b-8b05-3ab5-a51d-dc67fe66c957 | -3.1628 | -43.9351 | 2026-09-28 16:28:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59daede4-870f-3df4-a2a3-a4aee91aed44 | 1.71839 | -50.95839 | 2026-09-28 16:28:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 23b879a7-0262-38a0-ba30-53f9f0f67946 | -0.90076 | -47.52147 | 2026-09-28 16:28:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0705128e-dff3-3fec-a4c7-92799c3953a6 | -1.54909 | -50.22497 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8aaa4377-8aaa-31d3-b989-cb0dfd902893 | -1.98039 | -54.25721 | 2026-09-28 16:28:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 640ed45b-5633-395f-a1aa-a4d3e2c2077b | 1.86293 | -55.58278 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 632f631e-1260-3724-a8e9-bc9fd40bca2c | -3.87063 | -51.79638 | 2026-09-28 16:28:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9addc9ee-4841-3020-8b35-bb3e447b28cb | -1.56463 | -48.26451 | 2026-09-28 16:28:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59a24e08-801d-3dc6-bdb2-e277f3b729a0 | -1.43762 | -48.89322 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 44f6f255-034f-30d8-9d65-dfe673add089 | 2.08488 | -55.87871 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 827442fd-30ce-399e-a695-47dfca7c6e5a | 1.8704 | -55.57474 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 32a65c29-bf26-3357-bb44-0f3ba0811d2e | -1.4336 | -48.89384 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fd64dd05-d35b-3955-8af3-ce207f33f74f | -1.47106 | -48.92414 | 2026-09-28 16:28:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87ad04f3-cab6-300e-b357-3123226d2f7c | -3.75772 | -51.33501 | 2026-09-28 16:28:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f3db34fd-3d8f-3004-89ef-e67d7099e62f | 1.84796 | -55.5988 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e22a592e-34ce-32b8-9fe1-f0d5d0fd674f | -2.08797 | -49.55165 | 2026-09-28 16:28:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f83bfbfb-34fe-3ea8-991c-ef417f3d74c1 | 2.07749 | -50.74496 | 2026-09-28 16:28:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4aa45f8a-d589-3afd-91ea-f52e1f0307e2 | -3.87882 | -51.36113 | 2026-09-28 16:28:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| aede71e3-1ad5-3b59-94a2-9a4fd3d64ba1 | 1.12524 | -50.00945 | 2026-09-28 16:28:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a5fd3d63-ddf6-32e8-b206-ff70d8f053f2 | -1.44498 | -49.58574 | 2026-09-28 16:28:00 | NOAA-20 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 387f8b4e-06f1-3bb5-ab7a-d1ccd1977067 | 1.86147 | -55.59163 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 74ac498d-a63b-3393-8d91-1048b6206893 | 1.95847 | -55.68909 | 2026-09-28 16:28:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 667c6a0c-521c-3d32-8433-0c87e8db1a28 | -2.28646 | -48.75659 | 2026-09-28 16:28:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4958bd9e-cad9-352a-b0e9-117ca0158bbd | -1.69823 | -49.93651 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 00b3f4e0-bd81-3f34-8afe-44d60bad26d0 | -1.60135 | -50.21281 | 2026-09-28 16:28:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 508afc41-e42c-34c8-8734-90d3f7ae0cb0 | -2.21352 | -50.74981 | 2026-09-28 16:28:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README125.md)
