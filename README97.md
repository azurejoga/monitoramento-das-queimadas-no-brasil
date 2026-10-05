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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8bb51b8-f380-3003-95d6-c9b09cb6b07b | -3.86147 | -57.15213 | 2026-10-05 16:39:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b09b7379-5415-359b-9d0c-da6e0845dd16 | -1.52474 | -54.82666 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| e7fe9bea-c436-3a5b-94f4-337525a64b37 | -3.43306 | -59.62463 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 2e7bbd97-8748-32cd-ae6c-58cc6455f94d | -3.43154 | -44.44473 | 2026-10-05 16:39:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b205b304-d087-38d9-a0c6-d143fd326ce1 | -5.48193 | -39.56322 | 2026-10-05 16:39:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 36.1 |
| a1510273-0621-39d8-92c8-11020d0578b0 | -4.90812 | -41.74197 | 2026-10-05 16:39:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1d36804e-adb5-3391-9447-6c1bde91c637 | -3.42407 | -44.44587 | 2026-10-05 16:39:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 63dd5960-7ef6-30d6-8f48-0e87a17a73a3 | -3.3756 | -54.10156 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 05cfffe1-9312-3353-bec5-567ee1b27236 | -6.09408 | -47.65291 | 2026-10-05 16:39:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 90ac9dd2-5e0a-3f57-b414-1344cabe3bd5 | -3.98334 | -55.81416 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ae3ddb34-0f4d-301f-90a9-189e397affd6 | -1.62477 | -55.13132 | 2026-10-05 16:39:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7dedc27a-cc3c-3447-921f-ce71954f4659 | -3.3292 | -59.47495 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 88cee4cd-2809-3895-9cb9-ce24e38eff26 | -4.82988 | -43.3828 | 2026-10-05 16:39:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 00328351-83b6-3294-9431-bd06087eac8c | -3.62286 | -58.6144 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 18dbf7fc-5a9b-37dc-afdb-9a4f684f111f | -1.51349 | -54.81113 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f9b0f6d0-66fc-3a1c-9df6-0be0dff01d4a | -2.8389 | -54.07266 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94dcf087-c570-3fd0-8802-cc42b819e74e | -3.3289 | -43.09227 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 87d39f4c-7ff0-3224-9513-333a7c4b6640 | -0.10906 | -49.68763 | 2026-10-05 16:39:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27180fb6-298b-3161-a6f8-6b45b26a2be8 | -1.62987 | -55.13503 | 2026-10-05 16:39:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| bca1dd8b-2c01-30fb-8e83-d3257c94589f | -4.49561 | -39.36475 | 2026-10-05 16:39:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5793a914-52ff-3463-94e7-f2fb7232c3e9 | -5.11375 | -42.63943 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 022611b4-5633-32b4-bfd8-4c44bff106e1 | -5.06201 | -42.89286 | 2026-10-05 16:39:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| be83880e-438d-3234-a3e5-92ec84362384 | -2.87675 | -54.12285 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e429e659-900a-3cfb-84fd-c228ce463dc0 | -3.05086 | -54.21604 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3bd3d3c5-572c-3eea-abb8-44169fd71f87 | -0.63237 | -49.64124 | 2026-10-05 16:39:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b9909a74-cc27-3681-9d14-cd89e40a6198 | -1.5222 | -54.80998 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 4a622134-6acb-3cbe-ad4f-79f35d4ca04e | -5.26988 | -47.90983 | 2026-10-05 16:39:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| affc8328-d23d-3001-8fed-e03ab85d305e | -3.79038 | -42.95086 | 2026-10-05 16:39:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2e098735-eaa6-3577-afca-22c94cea1782 | -2.90858 | -42.34646 | 2026-10-05 16:39:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7b1cb140-f7c2-362e-8e7f-6501524e2d78 | -7.22552 | -55.18384 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 55b4657c-727e-38a9-8602-accd282917e1 | -3.51106 | -59.55935 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| de8f26d7-7f01-383a-a8da-88a4b4caa775 | -7.23187 | -55.19361 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 194105c5-88eb-3e37-aebf-0eeae2b10e96 | -3.79134 | -41.76143 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f8fc40f6-1f1b-39bc-b469-7ef1c7157b09 | -3.34837 | -42.90226 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d20ab954-7663-33a2-8c67-3a0b638dd14d | -2.82 | -57.29726 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 430b7cfb-57b1-318d-ac24-5d25dc871e00 | -1.34164 | -50.47692 | 2026-10-05 16:39:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 760ede88-cb60-37f0-8f80-2b3fcae7a3ce | -3.49781 | -54.61764 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| b9639951-f85d-3b29-a06c-71bd463eba36 | -3.22434 | -53.87119 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d88a363c-d2d1-33e6-b14e-391397b7a1b8 | -1.62921 | -55.1306 | 2026-10-05 16:39:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| bac7d4ce-d6a4-35d9-b5bd-a8885de2a5b5 | -2.80741 | -49.86886 | 2026-10-05 16:39:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86e9f77b-bf97-3fb2-931f-16831240ad2e | -2.94898 | -42.30713 | 2026-10-05 16:39:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 53db12ca-c1fa-3361-ba99-7320552b66dd | -3.86896 | -55.82944 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6def5ed7-906b-3161-bc40-1d49f9e30d6f | -3.63127 | -55.27894 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a0e4cb4f-d583-3a19-81f2-65a47dc91bc1 | -3.23689 | -53.86937 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 932ebfbe-25ab-38d0-bf21-d83869fc10ec | -5.83146 | -45.0135 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 60e3dec2-2d5c-3f01-9681-15b7fcc235c6 | -3.6473 | -58.6193 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0df96c4b-6540-37ab-a841-bad53e6eb941 | -1.61443 | -49.95608 | 2026-10-05 16:39:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a42c2af9-5d14-36e1-9bbc-b8c547ff4bea | -2.47319 | -49.40962 | 2026-10-05 16:39:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4d71791b-c2c8-3a6a-9dc8-94cff76fbd79 | -5.50422 | -42.80466 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 75d6f940-49fb-3d54-8dad-15db0eb7cef5 | -3.57771 | -41.24315 | 2026-10-05 16:39:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| ca132b40-4465-3d98-84f2-3a91d09c7b52 | -4.02285 | -44.82557 | 2026-10-05 16:39:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| bd045db9-9e16-318c-a1a7-53c02472b1b1 | -3.04967 | -54.20807 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 85078b1d-5612-3fb3-b3c1-f45e3039841e | -3.86411 | -55.83006 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 091515e9-8c97-3f11-a659-769bec0b8034 | -0.10574 | -49.68813 | 2026-10-05 16:39:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a7f6d07d-a371-3d6b-8f31-50fb9834beb5 | -3.26736 | -43.07258 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0ccf4096-ff95-322c-ad53-b62cc065e167 | -2.03851 | -54.30498 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b13eb354-8c54-3f03-83db-b0f26b1eff5f | -0.25706 | -48.67198 | 2026-10-05 16:39:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5e34faa8-5f9d-3d15-b74a-f3a2d4835c5b | -4.2492 | -41.7735 | 2026-10-05 16:39:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2edeff95-577d-3f54-82e4-a11ab7500fd1 | -3.31299 | -53.85525 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b4880ce7-69e7-3949-a8c2-e431a4c1750a | -1.18427 | -49.24706 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a089a0f3-a338-3057-9407-2ac4ebc40b25 | -3.11307 | -53.71084 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 213490a0-7bb5-32e9-bef5-efd606d47c95 | -7.22627 | -55.18914 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| ebae88db-d22c-31ae-adfe-eb7608c15525 | -3.68294 | -42.95738 | 2026-10-05 16:39:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 786f8ef7-873d-3706-9168-cb45c49c7773 | -5.13313 | -60.31947 | 2026-10-05 16:39:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| afd85f7a-49f7-3e21-a005-6be930238b5b | -3.07011 | -58.40359 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5c9896d-a3b0-33cf-8190-e0ec86679aa0 | -1.77721 | -53.77612 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3904ab22-76dd-3a0e-8758-aabb8fe15e58 | -3.61873 | -44.42358 | 2026-10-05 16:39:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0ac5f4f5-2c69-33b9-9692-02acb29ad684 | -3.9815 | -42.86814 | 2026-10-05 16:39:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c5f3277e-4ddd-3441-979a-7d85d4184dd4 | -1.9194 | -46.23732 | 2026-10-05 16:39:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7b368abb-e251-39da-a038-d3e7e3b6fa98 | -4.85302 | -40.25626 | 2026-10-05 16:39:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 94ba39be-6e17-3bc9-8f4c-79ca259d646f | -3.64837 | -54.04639 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| d50d221c-b12c-3788-b85b-44f887ce58e7 | -4.467 | -54.96496 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cba543b2-2e89-318a-8a9c-f603e496821c | -1.85227 | -50.62633 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aebb8999-9265-30a4-9f9c-706788a85175 | -4.14048 | -46.8344 | 2026-10-05 16:39:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5b82cf69-5dc5-3048-abf4-1c34845a6941 | -1.64519 | -55.14621 | 2026-10-05 16:39:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef2de7fc-db7b-339a-aeb9-56700280cf47 | -3.10774 | -41.83286 | 2026-10-05 16:39:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 35e2eeab-77bc-3d6b-bed6-378f594204a8 | -2.9498 | -42.91195 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 22628df0-fe74-3d92-96e3-138c1c0f7941 | -3.12865 | -53.71166 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| fc3eb7e1-aea9-3a1e-a9c7-237b6d90abc0 | -3.53969 | -39.88745 | 2026-10-05 16:39:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 63c4f140-973c-3aa3-9fbb-e5f62eb30ae6 | -3.51487 | -54.61078 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e8d6bbaa-c88c-3060-a2cb-d91541ecac4a | -3.69372 | -58.89052 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4b84ea4b-802d-3ef1-b21f-0a9e2f412a88 | -3.21213 | -42.87766 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 3c52704c-bd2e-388f-a9de-9ede5cd4dfaf | -3.0571 | -54.17046 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4086b284-8efa-37ab-a374-86b16a9c96cc | -1.80728 | -45.27732 | 2026-10-05 16:39:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6e487c81-43a1-3d8b-b886-497228d48251 | -7.2199 | -55.17914 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| f5672579-bee9-3291-b1c7-487bbd1159bd | -3.3768 | -54.10957 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c147e3a7-402d-3c0b-b3d0-e491a6ed39db | -2.83162 | -43.69113 | 2026-10-05 16:39:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1f21c782-904d-3434-9431-26ed3e5b59f9 | -3.59026 | -55.29001 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a7799fbd-59f8-3edd-98a3-a29580adcf3e | -4.34502 | -44.37374 | 2026-10-05 16:39:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 46068d6c-2798-3500-b5f7-79a80c6ec22a | -3.61178 | -54.59748 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 5446fb84-6a21-3f03-a72b-a592f75d8802 | -1.47375 | -54.78287 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 255afcd1-3e8a-3f7e-bfbf-5a581a5975ad | -3.16365 | -41.9569 | 2026-10-05 16:39:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e7a4c86-32f2-3215-bc7b-673b010b4464 | -2.80304 | -54.72881 | 2026-10-05 16:39:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 44ba36b5-3f36-36e0-b32a-8e3f696ae034 | -0.37763 | -52.07255 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 93b7bfb2-6c2e-33ec-b754-5a5914b64fbc | -6.18819 | -55.35167 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 3e0fc9e9-917c-3d56-93c1-f68d00c6e434 | -1.00186 | -57.50832 | 2026-10-05 16:39:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c0031c34-a098-3025-bc6b-605e94f2b886 | -1.6946 | -55.02347 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c7bd95f-998d-3a9d-9e7a-94211a23ff87 | -2.92575 | -42.38176 | 2026-10-05 16:39:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2b98965f-2bae-3b98-8daa-a8947c5d418e | -5.18153 | -48.33353 | 2026-10-05 16:39:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a7479d83-c305-35b2-9d41-606f8cfe13d5 | -4.45713 | -54.96167 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |


[Clique aqui para ver as próximas entradas](README98.md)
