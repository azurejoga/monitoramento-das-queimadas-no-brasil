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

## Dados Diários - Página 221

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f48465c5-8678-3279-81b1-8897eb66e3f1 | -3.26927 | -54.03863 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 08497945-b6a8-3806-af8b-8463005d79c2 | -3.01187 | -54.23648 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 93d66372-7320-3bee-ade2-97a0d38d431d | -3.05448 | -54.02889 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a3c655ca-8a2b-332c-bb6d-c41689d123cb | 1.42474 | -55.66053 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ace9960-c608-3837-b660-d122d3aca06d | -1.772 | -55.06694 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57cae283-0039-3d5d-8517-71a9de53ab38 | 3.21838 | -51.31075 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 10b21ad5-605e-3301-8d9c-104b78ab27cf | -3.57707 | -54.65532 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c63f400f-cc17-3b2f-aa14-95dfea917a5b | -2.87566 | -43.71281 | 2026-10-07 16:39:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d7099bdc-b2f3-3df4-8076-28fbf4c1aa03 | -4.15405 | -55.2512 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15bf3d91-7ff2-356c-877a-b3e617fa5ec1 | -3.15364 | -43.92115 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 57fab7ed-8c06-3a9f-b0f0-8788e4fb55e1 | -2.65809 | -54.31358 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b478035d-f6f7-32ff-92d1-efd72bbd0dd2 | -3.10662 | -54.15828 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 72645697-42f3-356b-8462-2cec90a4d23a | -4.14859 | -54.02742 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0b63e120-5424-3a55-961f-e221c5d849d6 | -3.17179 | -50.43688 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8929c817-beb7-3993-b20d-701f459d0076 | -2.58305 | -56.16275 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 091655f4-1af1-3009-a532-f91dd2e14dcf | -1.71828 | -55.44828 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 51ed6b92-b378-3487-9c08-bc9898a30735 | -1.20657 | -49.03328 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 99e08666-d975-3eef-8ef4-fbe8d14f5dcf | -3.18643 | -50.56575 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1a72e6fd-abfb-3766-802f-ab87a061c095 | -3.06524 | -54.25669 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 186988a6-4229-368b-9ef8-aa05a7d46d2c | 1.88704 | -55.71464 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9a3fe302-b268-33f7-b1ea-e1a0a19fa6c3 | -3.23702 | -50.17625 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 6ac5fc1b-b893-397a-a62d-9c60b30d7724 | 1.94995 | -55.12459 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a5b58609-e0c3-3b6d-854b-40b727b4a3af | -4.15836 | -55.15713 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f09bed89-2af6-3f11-92eb-5c7f550d4a5d | -1.63684 | -55.41875 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c3cd94d4-22e1-3268-b6fb-ca4b9b0a2ba8 | -3.19435 | -50.56052 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 2d9765f7-74a0-3691-8b48-17fcfcad7b9e | -2.89273 | -54.1554 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 33ea2a36-1acd-344e-bbc5-cda6886489da | -2.75965 | -54.08694 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ff6887b5-77bc-3335-b23b-0c7033943323 | -3.18721 | -50.54155 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5b4fc314-7e5f-3f5c-98d1-76a4ea88aa52 | -2.99462 | -54.04558 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cea3e8ee-c237-31da-9be6-a06b5b15b5a4 | -1.20156 | -54.20796 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e6ac9f42-35e7-3c30-bde6-8772cbd6798a | -1.99668 | -45.08418 | 2026-10-07 16:39:00 | NPP-375 | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b6d8f14-2ee0-3720-9a10-d243448a1d8b | -3.26255 | -50.40839 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d3b9c9ec-a698-3e08-a81e-1449da476d8d | 1.34177 | -50.83782 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 44707b55-90cc-3cb0-baec-facc6ee4627e | -2.93379 | -54.17049 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 095b0c4e-e44a-374f-9589-f20b0cbd7e37 | -3.02118 | -53.89461 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0846b8cd-298d-319f-86e9-3dbef2a22239 | 1.91795 | -55.70044 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b636c1e7-03a1-31b7-b7f5-467d53b5f2ab | 1.86662 | -55.73441 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97e34ca1-dd1a-3ff8-be12-96cdf7bf663c | -4.14457 | -54.90199 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7b236e07-23df-34e3-8cf9-a836a5d09565 | -3.47111 | -49.93483 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d4b91af5-19de-3350-9f76-57867992ed9f | -1.20661 | -47.78043 | 2026-10-07 16:39:00 | NPP-375 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6eb22a04-109c-3610-9665-614d8da045c8 | -2.79635 | -54.07478 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e1f7cdb0-0ea6-394f-904c-d3d00281d3a0 | -3.57336 | -50.35874 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 73d6928b-ea1c-3b45-ba8b-c12b542cf349 | 1.70669 | -55.61323 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 09168fa2-19bd-36ce-96d1-6d5a3c465c64 | -3.04754 | -53.90622 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| bad7719b-c1f7-3560-b901-c41e80fd1a51 | -2.49481 | -56.1115 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7a8577be-281f-37dd-adcc-e184cfec0d71 | -1.3799 | -52.67287 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c9aabeec-612b-3972-bf2f-6acd8dac57aa | -4.7713 | -55.72419 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ff86e4b0-6338-3023-846c-127a759f9b8d | -2.58101 | -56.14727 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9dc54f98-8cd0-303a-ab47-6a08fe61fea3 | -3.02463 | -54.06202 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| a8a941fe-6624-3db4-99f6-97d8b22a9b83 | -3.27919 | -54.06892 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7a099de0-742c-3d50-9517-dde399b2a6dd | -1.22352 | -49.04114 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 47bb70e3-0b71-31f3-a0a5-0c4be8e90682 | -2.94172 | -54.11323 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 904ad13e-124b-3693-8dae-457fafd43ee2 | -3.00088 | -54.12483 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 377b71ba-728f-343f-8fe9-723b7d79e3e8 | 1.81056 | -55.52921 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| c5951943-7a22-3c9a-af5b-42c0aa30c1a7 | -3.13674 | -54.36245 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 9984cbb5-43fd-36e6-9d83-6379eb5384ad | -2.37267 | -56.13297 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 22ba2280-9219-3307-ae65-b5999232456e | -0.77981 | -49.26629 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 55ab0112-f4b5-3b44-9601-0f160d4194c9 | -3.35716 | -50.46981 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b50ed485-d5a4-31ce-9586-36c428ad6b52 | -3.26715 | -54.25639 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 11e42955-8048-3d59-b0fe-d50f0fb219f9 | -2.79349 | -54.09244 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 212.9 |
| fac8af51-08eb-38b0-b95a-338d661bcb2a | -2.68875 | -49.04119 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 9c399860-d9a6-355b-a581-63407454e32e | 1.35088 | -56.13119 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 53c67211-add2-372c-a33b-360c13a5c94e | -1.21079 | -47.19704 | 2026-10-07 16:39:00 | NPP-375 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fce0ff38-0873-35b6-8403-3c4f3c478c88 | -2.76757 | -54.10325 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 0f53c39b-2d0d-3262-8f6b-ecf63e129dd3 | -3.07675 | -54.25946 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b95c38e9-e508-3ab4-a00f-be5e2ab2352f | -2.77329 | -54.06766 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d0c49826-4130-31fb-a36a-0b4339e4a5b3 | -3.06003 | -54.1433 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a7661eaf-3284-3418-ad80-2548136b591a | -3.27468 | -54.03784 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 43feeda7-6ce7-309a-824f-e80d2b5f1f5b | -2.04556 | -56.19883 | 2026-10-07 16:39:00 | NPP-375 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 42ba028b-9e59-398c-9d35-59374cba56d7 | -3.09272 | -54.29196 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 40f17127-6898-3791-87a3-ba4ee039e872 | -3.1102 | -53.77961 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| dcf92d08-74c3-341a-9015-05b83360822b | -3.17514 | -57.23867 | 2026-10-07 16:39:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0aad5abd-2871-31b4-a3ac-bec92984a31f | 0.30211 | -51.13773 | 2026-10-07 16:39:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7061b2c0-e707-39f2-a8e5-84d955b36594 | -3.72156 | -55.49229 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 01305288-0513-3db1-85ae-f59bae1289ee | -4.60862 | -55.71676 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 14241d84-ec1d-3ab1-bd8b-d609393f5355 | -3.99485 | -56.24899 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a2ef20e2-8a43-3e59-b69e-8abcae2f91d7 | -3.26733 | -54.06345 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7a1a8c96-e941-39a7-97e4-73e16897a5f4 | -2.0 | -45.08368 | 2026-10-07 16:39:00 | NPP-375 | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3977e4a5-af23-3e57-b378-a9a63a5b18c4 | -2.40481 | -51.30361 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fcabe716-c10a-3c84-b2e6-8103ccc41b78 | -3.70205 | -50.66847 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d0ee5e11-80db-3ca4-b9de-b060cd4c8351 | -4.33909 | -56.38845 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 161de9c5-4c95-3825-8fa4-e8974f55f34b | -3.25731 | -44.6831 | 2026-10-07 16:39:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8bf3fb21-4780-36d8-9e49-c73314b1c77f | -1.7564 | -56.19246 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43ba4e60-34fd-3031-977e-aff18d0d0b3c | -3.48209 | -55.43139 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| ec17b9e9-d568-3cf6-bbdd-26e3165e2bf5 | -3.68231 | -55.95192 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e4e8cc0e-0ca5-3667-9ce2-7b3497d02048 | -3.54304 | -50.09248 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8fd2a116-b7f1-3506-9502-62869a69b9be | -3.30412 | -53.86471 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 3a2a2f26-1aaf-320e-aeb2-a756d4ea4ee0 | -3.18218 | -50.56638 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 34fbb1ec-85b0-3519-9caa-663050442b98 | -1.46179 | -54.76862 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 02ba550d-3834-3776-be46-17f59fb3f71f | -3.83601 | -55.97906 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 43175fde-ed2c-3fbc-9052-e7cdaec8d774 | -2.86063 | -41.81033 | 2026-10-07 16:39:00 | NPP-375 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b09b9469-cfe4-3ddb-9a6a-b3070b970938 | -3.73335 | -51.21021 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2f57bbb0-9d88-3186-a48a-1410d945e706 | -2.48503 | -49.40861 | 2026-10-07 16:39:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 69d62c87-0604-3b94-9a25-540af292c192 | -2.64092 | -56.54469 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 82b7322f-7060-3a54-ba23-344bb58cd0b6 | -3.05288 | -53.94272 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3a3fe23e-6df8-3b6f-8324-25024ace5a3c | -3.03247 | -53.91516 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a842f391-a633-3f1b-b1a7-44f446e843cc | -3.0455 | -57.48959 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 6404671b-c0f8-317f-90c5-569db434d618 | -3.27071 | -54.01052 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d745b434-bed2-309e-9d1d-7db5601a6459 | 2.10659 | -50.96589 | 2026-10-07 16:39:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bee8c27d-adad-37e1-9422-f879ad4f20f1 | 3.22186 | -51.3149 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |


[Clique aqui para ver as próximas entradas](README222.md)
