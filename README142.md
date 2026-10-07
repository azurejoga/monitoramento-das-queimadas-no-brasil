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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c89aad0e-d4d7-32ce-b478-e32c2d735d1b | -9.0612 | -65.4729 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 82b4b8c9-76ee-3fd0-85e5-d316c53f9d55 | -2.4989 | -56.1069 | 2026-10-07 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ea5f8a3e-663a-3235-9e97-2658d8f444ca | -6.7066 | -45.5765 | 2026-10-07 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 22dfbb6a-d12d-3bf8-be88-790fba2e55b7 | -12.1742 | -44.7284 | 2026-10-07 15:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 417.8 |
| 53e435fd-a6a4-3fd1-ac22-bc45850585e9 | -3.0734 | -54.147 | 2026-10-07 15:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d9129b79-897a-33bb-86c8-d2a57abe9b25 | -9.1174 | -65.359 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 24e7063f-6867-3835-9be0-eae75e7a01d3 | -1.4301 | -49.0382 | 2026-10-07 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 5dca3cb5-b48a-3834-9502-221b13034870 | -3.5171 | -58.752 | 2026-10-07 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 73bd6073-3018-30d2-931c-7ba61ba3e3ce | -1.5118 | -54.8153 | 2026-10-07 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| e5fb3917-6a77-3eef-8c99-7007c4875aad | -9.3394 | -65.4638 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d255bd37-3cb4-3dcc-8b60-bff82531d05e | -2.8164 | -54.0929 | 2026-10-07 15:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 92f88b77-54ed-32cf-b848-a0fba30a6c50 | 3.5264 | -51.257 | 2026-10-07 15:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 7b22c1c4-0c54-3f4f-98c7-f85ca809239b | -8.1428 | -64.0804 | 2026-10-07 15:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 260a9761-856e-3e74-b2d9-dcade3d055e9 | -3.1117 | -53.7032 | 2026-10-07 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| fb53fffd-736d-3477-9e3a-06766dbd5ffb | -9.0859 | -61.1437 | 2026-10-07 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ebfe86e5-0498-39b3-93a6-49905fe1ee26 | -2.9739 | -56.6278 | 2026-10-07 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 90858be7-906b-3724-aa52-6eb2ea348d60 | -8.7503 | -69.6474 | 2026-10-07 15:40:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4998f184-356f-3fd7-8052-cec831f1a80c | -2.9271 | -53.9295 | 2026-10-07 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 3338ffd4-1012-354e-a7dd-4cde0a8cce3f | -9.1408 | -64.3836 | 2026-10-07 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| cff99271-d98d-37af-9f20-ebd21f912bd5 | -8.8892 | -66.7259 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f280e3cf-e4f4-3d45-8a87-ff9ea0cdcccb | -8.1035 | -70.1349 | 2026-10-07 15:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 03deb62b-7387-309c-8876-c31a8711222a | -8.8891 | -66.7445 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 843d20e0-df25-32ac-aebe-340de55c2aba | -3.4944 | -54.6167 | 2026-10-07 15:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| c8c96a56-11c3-319a-a52c-13d983143900 | -3.0074 | -57.7578 | 2026-10-07 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 8aff8d27-5ddd-3531-a4e3-c2cd1ab9995d | -1.2922 | -54.5585 | 2026-10-07 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 3481ca87-0893-3e72-a157-e2d28a6caec9 | -9.6572 | -65.022 | 2026-10-07 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c55238c1-92ad-38fb-9835-b1f8ce0571ef | -0.3952 | -52.0357 | 2026-10-07 15:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 75.8 |
| cc3423c2-5ed7-3bfd-9049-5ab9f0f1ad7f | -3.0992 | -57.6395 | 2026-10-07 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 0d760231-2e22-39b0-8ca9-fc9ae517859c | 1.9134 | -55.7024 | 2026-10-07 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| b86f6196-3670-3a42-af8a-98181cfe4232 | -3.0074 | -57.7384 | 2026-10-07 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 115.2 |
| a32b3082-d539-332c-b567-4b285a0f4399 | -1.1713 | -49.2544 | 2026-10-07 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 0ab7c8db-3324-3224-a161-7e0bfca45bdb | -2.998 | -54.7492 | 2026-10-07 15:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 7ab1cc0c-fbaf-3869-9f37-529ba5daab1d | -9.0612 | -65.4916 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 133.7 |
| bfb68e21-6a62-3c8e-9581-f8736599be45 | -1.3927 | -49.2727 | 2026-10-07 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 0909640a-7a5c-31c8-bc62-dbd28d3485f8 | -11.0867 | -45.6459 | 2026-10-07 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 7817318f-7d36-3cf7-af8a-69f6e175502f | -2.7613 | -54.0941 | 2026-10-07 15:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 450.7 |
| 439c54f8-4ece-38c2-8614-e1e4ceca9c66 | -9.8619 | -64.9958 | 2026-10-07 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 87c0e09e-68bb-3c03-ad41-0ddfab763c61 | -12.2136 | -44.6758 | 2026-10-07 15:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 3d67fc82-20e4-3a0e-9b85-89a02cb31bfb | -3.0001 | -54.1086 | 2026-10-07 15:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| db7c0660-2042-311f-bd85-391165fe4dbb | -1.1898 | -49.2542 | 2026-10-07 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 03abb7af-1893-3523-92b2-c6ac7cdfcd24 | -11.0863 | -45.6688 | 2026-10-07 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| f545c729-54d7-398b-a0e8-61c9b052172b | -1.4569 | -54.7761 | 2026-10-07 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 250.5 |
| 7d287282-4b2e-3ed9-8718-d31f3b442228 | 3.5263 | -51.2778 | 2026-10-07 15:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 011559d6-15fe-355f-a473-d89f19d41119 | -9.0987 | -65.3783 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3986e60d-560d-3d3e-8df8-fae4dbca8dbf | -2.9979 | -54.7692 | 2026-10-07 15:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| dc7448ad-0a65-340e-9bf3-b60810342694 | -2.8573 | -59.2066 | 2026-10-07 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 36f03e0a-b3f1-3bd7-8375-a9167a242c5e | -9.1363 | -65.2835 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| b7e5b857-d45f-34fd-adf2-3388e845cbe1 | -8.6291 | -67.0482 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a096d0d3-02e8-353c-bc8a-2f35c043d9bc | -2.4988 | -56.1266 | 2026-10-07 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 01d5af76-00c2-3ef7-94c0-d7d6b66763c1 | -3.0932 | -53.7239 | 2026-10-07 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 3b247b08-a7c7-303d-91d2-5629ecc02e78 | -3.0192 | -53.887 | 2026-10-07 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 930b0808-848a-3fa6-aba2-c5c3c288d723 | -9.0232 | -65.6982 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ba9ce2f2-44a1-3caa-ae40-a01c76c53bfa | -0.3952 | -52.0152 | 2026-10-07 15:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 9a6ab8a9-88c6-3634-bbaf-6a4581a9f7ef | -3.8567 | -55.9769 | 2026-10-07 15:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 230.9 |
| 6773178d-4f70-3e74-8ccb-cd2806468213 | -8.1613 | -64.0798 | 2026-10-07 15:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 79401225-b9bf-3421-ba56-4ad2172aff8f | -9.0988 | -65.3596 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 871430d6-aea9-314d-b41e-19b90100f04c | -9.8245 | -65.0348 | 2026-10-07 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| de9e6a8c-e765-32ef-a095-09ea8414b1b0 | 1.8768 | -55.7227 | 2026-10-07 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b4cc2451-664b-39c4-9f38-1e0a3de9ecec | -3.0375 | -53.9066 | 2026-10-07 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 201.7 |
| c94bd940-cd08-32a4-91ad-8dd8e25caf42 | -8.868 | -67.4497 | 2026-10-07 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| fb33c743-8678-3a8d-802e-8cc7ea270bde | -2.9795 | -54.7696 | 2026-10-07 15:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c0bd132b-32ac-313a-a17a-604328009f1f | -8.8519 | -66.8012 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 723a4939-60f0-3bc4-9a13-67856ef2f4df | -2.572 | -56.1646 | 2026-10-07 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 0e1e4f81-b0df-3b93-b033-d3ce4ae251ce | -9.0231 | -65.7169 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e31068d8-b968-3594-9c6f-47306b7fc4c5 | -2.8575 | -59.1107 | 2026-10-07 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 393cfc46-cc8b-3241-89f8-b6ab797fd06c | -2.7513 | -57.6656 | 2026-10-07 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 446bc165-31cb-3c5e-affb-87e44ee24f35 | -2.9327 | -58.3204 | 2026-10-07 15:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 28f366c9-c644-3aef-a6dc-1654a3733f2d | -3.4495 | -56.9498 | 2026-10-07 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 74ce3c9e-e7af-3dae-8dce-f912eb6233b3 | -8.6106 | -67.0486 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 7a3ea7d4-8c07-3986-81c8-f811b1c51929 | -9.5176 | -67.1173 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d3d182ef-b4d1-3860-9b21-75ca34a6ee92 | -9.1356 | -65.4145 | 2026-10-07 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 25840d15-3f6f-3753-817e-a792cc38ffcb | -1.4569 | -54.796 | 2026-10-07 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| efa4e47b-df3a-3ea3-9513-7dbc5328c1c8 | -2.9817 | -54.1091 | 2026-10-07 15:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 34a2f4f3-e987-343e-9032-0cfad86db809 | -3.8383 | -55.9774 | 2026-10-07 15:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 392.5 |
| ad3a3bd1-dc77-3ff9-9851-13733587cac0 | -10.9762 | -45.4094 | 2026-10-07 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| b37fb046-03a6-3b5e-8508-ca4777ec36b0 | -2.9819 | -54.0488 | 2026-10-07 15:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e87eafd3-baac-3584-bfc0-247f0ab17183 | -1.5118 | -54.8352 | 2026-10-07 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 819c580d-10c2-3372-aae5-46bee78f42f1 | -9.9175 | -65.0313 | 2026-10-07 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| b71a1fc4-9732-3c98-a23a-e586d0058aba | -1.1094 | -54.1601 | 2026-10-07 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 527fcc0f-87d5-30a7-b166-8e3d15469264 | -9.1407 | -64.4024 | 2026-10-07 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c5cab940-9b27-33ed-825c-31e26790139b | -9.6419 | -68.6156 | 2026-10-07 15:50:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 80.1 |
| efb61559-855e-3628-93df-5f3d5b66262f | 0.7266 | -51.3749 | 2026-10-07 15:50:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 71.5 |
| c15dc888-545d-321a-9193-2416901f787a | -1.5302 | -54.7952 | 2026-10-07 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b0a82867-3e47-3aa2-957e-9f00ac6f5c62 | -2.8897 | -54.1514 | 2026-10-07 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 301427af-8869-35ca-ab0a-fc410c00ad28 | -9.8245 | -65.0348 | 2026-10-07 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| d2cb3673-da60-3555-a87d-4160884ea181 | -9.5176 | -67.1173 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 012e81f0-86a5-3b88-9742-cb38a86c67ab | -1.2922 | -54.5585 | 2026-10-07 15:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6ef88abb-3836-3c52-95b4-da50c6591085 | -9.9175 | -65.0313 | 2026-10-07 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9070e9c1-cffa-31c8-aa8f-204c8f9ee24b | -12.2132 | -44.6991 | 2026-10-07 15:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 576.4 |
| 415b5c93-fc35-3a28-87a3-4716cef2871e | -8.8519 | -66.8012 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 174ffe6c-a196-3312-8504-309224a0941d | -8.9873 | -65.4379 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4d844a5c-1198-3c2e-8df5-8bf6f98b8149 | 1.7121 | -55.6261 | 2026-10-07 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 87d5080b-1bb0-377a-86d7-ddc8724f4d74 | -3.0265 | -57.466 | 2026-10-07 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2b571530-0ab3-3458-ac4c-fa1223179cc9 | -11.1047 | -45.7119 | 2026-10-07 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| a9a35f29-67f7-3a07-abea-1b7c2fbc6363 | -8.9874 | -65.4192 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6e056394-4e36-3628-a407-d94eccd2a2ae | 1.7121 | -55.6063 | 2026-10-07 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e9aabd08-6b17-33f6-bd7a-e297811827fa | -8.1035 | -70.1349 | 2026-10-07 15:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 117b1949-ed89-3a46-a33d-230d73dbd4dc | -9.0612 | -65.4729 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| dc30fed7-0382-3ed3-a181-2c0ec9ba4135 | -12.1746 | -44.7051 | 2026-10-07 15:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 203.2 |
| bee3e7af-770b-32ce-9222-0c30920483b4 | -2.8714 | -54.1318 | 2026-10-07 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |


[Clique aqui para ver as próximas entradas](README143.md)
