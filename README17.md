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
| bb89720d-e328-3fe5-bc5f-4e83e90aedf9 | -2.84218 | -48.11236 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6302f7a8-fa6a-3045-988b-c4ca8ab4de10 | -1.88856 | -52.07859 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 967014cd-e292-3418-a0e4-a86e34e40c02 | -1.2925 | -53.10432 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32b70dd0-0a2e-36f7-95d8-ce5e6cfbdcab | -1.29657 | -53.13039 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a13ac00-2d11-334c-bcb8-fc021482600b | -3.94929 | -54.63369 | 2024-12-22 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc780336-2791-35d8-9575-6c38f2da9f91 | -4.01271 | -47.0531 | 2024-12-22 05:14:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f981ae39-f7b1-34b5-ae7d-d92ffb27a445 | -1.88833 | -52.07811 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f0842bf-0c8e-3f41-abab-745a6a526ab0 | -1.5755 | -54.04232 | 2024-12-22 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 865c1759-33b1-355b-ac58-df7196f9b6f4 | -1.70534 | -52.41946 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31def9fd-9afe-3d75-b772-9664a792f602 | -2.52051 | -54.23104 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad0f41b5-4ad4-37a0-94ac-6386ad48ee0e | -1.31097 | -53.52403 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41be372a-4b06-3bf6-ad3f-2b29e75c3824 | -2.0443 | -52.10479 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f94cc42a-020b-329e-bda6-04f4b9855606 | -2.63114 | -48.05446 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8492917a-28b2-35dc-bd0f-60f9114aada5 | -2.51678 | -54.23046 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f72085ff-e694-3df6-a752-d8eb56e081cc | -1.89067 | -54.5719 | 2024-12-22 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db1b4712-5eeb-3e08-9056-4a33bcf162f6 | -2.81538 | -48.2547 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 375ec0f6-8e27-3378-a8da-aa7d5b185811 | -2.79884 | -46.7526 | 2024-12-22 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb48311c-cab4-3002-bbd7-dcaf09154637 | -1.28873 | -53.12916 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36fe8bc5-6b50-3cfa-a158-8552fa803f5f | -1.95381 | -53.57248 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 706aa801-57b2-33f0-a74b-657e0acc4865 | -2.44857 | -49.02776 | 2024-12-22 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ec4dd6d-e930-390b-be80-802b4ab70c6e | -1.29302 | -53.12737 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72563861-06de-3a18-9093-c942608d4774 | -3.06464 | -47.77206 | 2024-12-22 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de7178de-79c5-3c2d-ac8e-dc4f499bfba2 | -1.70294 | -52.59041 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 504af7fe-cf50-303c-bab1-fc96766b75f9 | -5.99856 | -45.41092 | 2024-12-22 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5c3fc220-8a97-3bf5-a4a2-eae573133bab | -2.03886 | -52.11197 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eea85fd7-751e-31b4-9aed-1a8d4222ddfc | -1.3749 | -53.70758 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a6c67e1c-f880-3b4c-925e-317712df07bc | -1.29694 | -53.128 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6aab4b65-2d06-3a6d-bc1d-55efd4c948e1 | -3.18134 | -50.39926 | 2024-12-22 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d07f7aa5-74b8-3f8d-90cc-b1223626d018 | -2.50227 | -49.0657 | 2024-12-22 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 927f4149-aa0d-38ed-a1be-fe4e3a090a7a | -1.20925 | -53.92729 | 2024-12-22 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97f5956e-9e76-344d-b9ad-ffd2679d34d0 | -1.72205 | -52.57476 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2e59c268-c783-3e48-92f6-93657c6cb9b7 | -2.63084 | -53.971 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdd8e2a0-e0fc-3f4e-8c57-12c406c4f05c | -2.50566 | -48.06395 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a0cfef3-f93a-35e3-8333-a65c89c922db | -2.56773 | -49.44908 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0186935c-ae20-381b-9d9a-4231e8010b8f | -1.36803 | -53.70185 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6c759069-b2c0-3679-86f1-5381938ca809 | -2.9767 | -48.08361 | 2024-12-22 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07059521-d5c8-3d4d-892b-8f74ebc90b6d | -1.71465 | -52.59591 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2a741105-426a-3539-af5b-45959592dcbc | -2.99056 | -51.44363 | 2024-12-22 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4265e01-7e03-3b45-8ded-a0018358fa7e | 0.64196 | -60.30661 | 2024-12-22 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b62b6419-b5c2-374c-be07-c03adb67a7a6 | -2.50511 | -48.06768 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e8ea552-ed4a-3ec0-a372-aea9a53d8b89 | -1.70703 | -52.59103 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fa23ada-f716-364b-811c-2ca20cd69955 | -2.57288 | -49.44979 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc532188-b321-3355-9bdd-cf6d058b8112 | -3.25683 | -48.89233 | 2024-12-22 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9ab6fc7-5208-322f-8b9f-b9f3e693ba4d | -1.18568 | -52.54629 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 372c4471-ff97-3af6-8e30-b5b3e34e4988 | -2.24884 | -48.31554 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dad5aab-64aa-3897-89d2-86080b11bdae | -2.82252 | -52.86181 | 2024-12-22 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec3b18c4-a6b7-350b-aa5d-dee9fb90e6db | -1.09398 | -53.6722 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0840ce6b-4510-3831-8484-ae20f3b88a9e | -1.30715 | -53.52341 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24a975d4-4639-3bec-bea9-08418025a60e | -1.36942 | -53.69294 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 865de25d-1432-36e0-8e48-1764c6683ec5 | -1.37111 | -53.70699 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 12aa9eaf-646b-3a6c-bbfb-c403be4f66ed | -1.09418 | -53.66995 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cac266e3-7db5-39a7-98d3-9356167685e6 | -2.58264 | -47.54417 | 2024-12-22 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdc9e65e-a9df-3b12-806b-b7edd30d0420 | -2.77322 | -54.35397 | 2024-12-22 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 6b9cd4f7-5c5a-3781-a5fd-86ed63884e0f | -2.67599 | -54.59864 | 2024-12-22 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe157e0a-3a78-301e-9230-19ba3f3f1945 | -2.83147 | -51.78514 | 2024-12-22 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af9eacaa-c0cc-36af-bc53-65ae179e62b6 | -1.14076 | -54.19873 | 2024-12-22 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3352b3cd-9a4b-3984-81a9-b9d00aff169b | -1.53907 | -54.21394 | 2024-12-22 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be6586d5-7e8e-3ce6-8895-a9e4040f513b | -2.74485 | -54.08522 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 195329a8-54a4-36d4-a283-4343768f29d1 | -3.17366 | -53.96489 | 2024-12-22 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b75d0cd-a24e-33cc-9383-8e5377fa5560 | -3.26273 | -48.88974 | 2024-12-22 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b58089f-b592-3207-8c52-d42f42cd09fd | -1.56321 | -55.16294 | 2024-12-22 05:14:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ab23d79-16d0-38cb-be4b-718d70f37474 | -2.52122 | -54.22651 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3129e6e1-f562-31f8-aee8-c10464389146 | -1.36323 | -53.68284 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15302a25-004b-39ed-a6aa-42d3ff977eac | -1.54849 | -54.2448 | 2024-12-22 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 602e45d5-0bbe-3bf6-ba4c-69ecd1ee831a | -2.44392 | -51.78786 | 2024-12-22 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d391a1c-df71-3822-a92e-64346ad40c36 | -3.50387 | -47.19794 | 2024-12-22 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8edcf7b7-3992-394c-a24c-d0cedd87b721 | -1.26044 | -53.52139 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2e29896-c025-39f0-a728-7a6b37c0fafa | -3.58968 | -55.43951 | 2024-12-22 05:14:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be16a50d-307f-37ef-9a06-92e3d9c4bb51 | -3.75488 | -47.19223 | 2024-12-22 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e356e42b-9fed-3d2a-96d1-b0787759b879 | -2.22178 | -53.81305 | 2024-12-22 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ca059e3-c7dd-36ff-b478-a05d101b53a0 | -2.80499 | -46.75356 | 2024-12-22 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4767ed2e-5e69-39e8-9bf2-b8caf1c51a5e | -2.44457 | -51.78366 | 2024-12-22 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a764c15-54ea-304c-a4dc-4855bba2022c | -2.56819 | -49.44604 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 792401bc-f67e-35c2-b517-d8f7551fe94b | -3.94864 | -46.41189 | 2024-12-22 05:14:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3e68392e-bfed-3bc3-9557-d1d997329d5b | -1.69186 | -54.47939 | 2024-12-22 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e341d11-d188-3dd5-915c-8c076b11a50a | -1.71851 | -52.5705 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6746f8f7-fb82-32f5-b71c-8d17a970b068 | -2.57802 | -49.45053 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a6303ac-d409-3b8c-b6b5-85915e223a90 | -2.04249 | -52.11654 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09033b2b-a6f6-3cc7-81cf-3ceceb09c757 | -2.5813 | -49.46347 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92ca685f-72b9-3789-bb13-dba5ced5f7c6 | -2.62831 | -48.03451 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5a2489e-1e04-3e99-85a3-c75e688738b2 | -4.54082 | -45.87934 | 2024-12-22 05:14:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f714a765-b5b4-3421-a8a8-79a4e1e643d7 | -2.93224 | -54.29887 | 2024-12-22 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddecd905-3cd6-30fb-a245-086288e07acf | -2.03946 | -52.10806 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98fd5e3e-fcb1-3e02-b7d2-fd3aba7bea6d | -1.25476 | -53.48183 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff78f2d8-336d-3a88-8d9a-7cd8de798606 | -2.04943 | -45.48528 | 2024-12-22 05:14:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32c3a8db-5e2f-3038-bff8-46d568b03f02 | -2.63339 | -48.03924 | 2024-12-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6c8b2b3-d951-32c0-87f1-74cfb5bcb89c | -2.9716 | -48.07896 | 2024-12-22 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb2718b1-616b-3b09-b15f-82e7470b96ef | -1.5405 | -53.39277 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc67394a-0f69-3ecb-86da-c1c476f1ae65 | -1.28832 | -53.10635 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a59d6072-c42c-3bf8-8f7e-2d7aa6c1bd62 | -2.77694 | -54.35448 | 2024-12-22 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| a064e61e-2e64-36d2-8a80-e47e59fab88c | -2.50179 | -49.06889 | 2024-12-22 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 750f4e6d-009d-33b8-8cb8-7fbfcf3c432f | -2.88286 | -51.80154 | 2024-12-22 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 479c7ccc-8386-3599-becb-c097110a7445 | -2.44829 | -51.7885 | 2024-12-22 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 301161d0-8e2d-33e3-8346-3e582a33a0ab | -2.57895 | -49.44446 | 2024-12-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a19fd8fb-1d96-332e-bd07-285d7b7035ed | -1.26428 | -53.52192 | 2024-12-22 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e68e5b05-eefb-3c5a-a85b-46dfcb01534b | -2.04006 | -52.10414 | 2024-12-22 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb901d81-5d5c-362e-9514-b546c4cd1ce5 | -3.06523 | -47.76797 | 2024-12-22 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b81fb8e-c1af-3f77-aa14-740b35d2afca | -4.2809 | -55.74117 | 2024-12-22 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9fe4f1a-c588-3c2a-b4c0-e782f527b26e | -5.99766 | -45.41762 | 2024-12-22 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b884941-23f9-366c-a565-bff09287df41 | -2.81372 | -54.3871 | 2024-12-22 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README18.md)
