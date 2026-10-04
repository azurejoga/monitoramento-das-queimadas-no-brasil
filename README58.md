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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aaa9aa4-4c0a-3dfd-8e2a-8a11429c2edb | -2.89247 | -56.94325 | 2026-10-04 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2cf6af8-a42d-347d-8429-d97703107fe1 | -2.76733 | -57.00456 | 2026-10-04 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d81861ea-0bdf-3047-accf-2496fbe6ccce | -5.7401 | -45.14933 | 2026-10-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 20209a4e-b4b6-382f-b62f-f7d051f0a5f8 | -5.37533 | -56.04331 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a81ffa3-2639-3bf8-aaba-891c67d37cb6 | -0.49378 | -49.10968 | 2026-10-04 05:16:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 373d602e-2e1b-3c48-8f5c-c9d4e39e1e0b | -3.05345 | -54.16431 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 483917e4-d225-38e2-8228-aab8ffb634ea | -2.9462 | -54.13219 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3032ae49-bfe9-35ad-97e7-0c2a6abb880d | -2.91238 | -54.09476 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d1daa3d-66ca-3f6f-acd7-c3096b76f608 | -4.2107 | -53.46548 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1813a360-2790-3e45-a244-af086badda7b | -3.37109 | -58.18633 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b72f2ed3-c663-33f2-a060-047541608d18 | -2.82471 | -54.12311 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70da7af6-f646-36d8-91b6-5463088dee3f | -3.13426 | -53.74515 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dc253d0-77f2-3eb3-877e-c01e0b2114d0 | -3.85096 | -55.97409 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8df3ad7-b4b0-3de2-8797-a52a231add63 | -2.85121 | -51.28773 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2847dec4-4c20-361c-9f48-a63da56d6e27 | -2.81203 | -54.08898 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ff55bed-691e-3130-8272-4b546f4aaa56 | -2.90915 | -54.13859 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd2dd43d-6ac4-3f23-a27b-2db79b72d0c0 | -3.28348 | -53.84984 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89817eaf-138b-30e3-a7b7-9d96a7f61adb | -2.92261 | -54.14468 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0ea0f8f-373f-36f4-8ce6-d99b6bb7de70 | -3.29613 | -53.83929 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b473b16f-28d2-3930-a3d3-f6b14d796681 | -2.25519 | -51.88548 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 46f29273-5a01-34e8-8be7-9b1c2728e4d4 | -2.89691 | -54.12466 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d6f7f4a-b775-3c2c-9512-d797f6ca0f70 | -1.12014 | -54.15028 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ec6268ca-508b-301d-886f-f355b3eac30c | -3.11435 | -53.75472 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 58d802bb-61e7-3022-a590-f7ec065c238d | -2.95469 | -54.10128 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15b75400-0cfb-3d1a-adb1-ef68153e7c37 | -1.08227 | -54.1064 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c61f95fb-b599-38ec-b02e-156f5e6f7254 | -3.81152 | -50.85592 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24693f33-12e7-325f-a64d-314eafc193ba | -3.64573 | -55.50331 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2132cdb-94e6-3faf-80aa-7dea4c9b048b | -1.9107 | -47.01793 | 2026-10-04 05:16:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 998c4182-84c8-3974-865e-a14293348d3d | -2.75761 | -58.0941 | 2026-10-04 05:16:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccc3b2e6-d405-327b-a350-5c8b121e9760 | -2.90212 | -54.13751 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 28487051-1b60-3d07-a7e9-dc19bb5f66a6 | -3.04023 | -54.20243 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68cafa58-8679-32d8-99c1-b4fab309b084 | -6.06233 | -53.478 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02563746-2541-38b2-8ca2-394b8b38035f | -4.32002 | -55.62481 | 2026-10-04 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4462622f-ae1b-3ae3-8fb6-f2ad2b8cba0f | -3.13326 | -53.72815 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 54ad5f8a-99d3-3122-aca6-e13dcc231e12 | -3.18282 | -54.07791 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d820fde1-9ace-342f-8921-24e6a549221f | -2.58568 | -51.87352 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e836eb2-921b-3fe5-8dc0-6bc0492f6490 | -3.81213 | -50.85181 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a187510b-8ac0-3fb1-a17e-3a715e0f25ca | -3.28538 | -53.83762 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7d65957-354b-3205-8644-92fed6d8cf61 | -3.11626 | -50.2819 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e9717a3-4628-37a0-a591-0ec5eb94d49d | -6.19633 | -52.8004 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edbeb178-01f1-3f82-8e14-9f2798c156f2 | -4.51819 | -54.89278 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf0cf4e8-27be-3f56-8d96-cd913ad9c469 | -3.12377 | -53.71828 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 7129ccdf-8f1b-35bf-b50f-661317e3f030 | -3.13066 | -53.7446 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69f2978d-1e32-33aa-8fd4-3a05c7c1874e | -4.71279 | -56.14726 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6a09694-9c37-368c-ab1a-110b0e5062be | -3.07826 | -51.27436 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0d4755a-60f0-3ed6-a665-6d32aa9d2338 | 2.01128 | -61.09217 | 2026-10-04 05:16:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0ba920f-06d1-3836-9e24-6ee3109abac3 | -1.2626 | -54.561 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1cf1d22-0ad3-358a-8ced-9927288866e2 | -2.75102 | -51.55445 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56c7affd-cd43-3ba3-8e83-e503cd764906 | -2.97342 | -53.2708 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c03c5679-cc11-3963-8c6d-95bd6abf79a2 | -3.02709 | -51.27425 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1336ef30-8550-3135-9e64-b6c039065d5a | -2.83164 | -54.21601 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6b7b502-d982-30ea-89fd-412f6167dd42 | -2.89803 | -56.67297 | 2026-10-04 05:16:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 766dc9ac-2be0-38a7-ae49-f9988636e0be | -2.43938 | -49.02578 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c51b5d18-375d-3a8b-a8d5-7d570889154d | -1.67922 | -55.65697 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a672375-0dbd-3880-8d04-7745db647d04 | -5.84164 | -53.81894 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32ff7301-71df-3900-b0b0-0ea6ef980b47 | -3.13736 | -53.73591 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c0b09f2-5b75-35ce-986a-3128d74b360a | -3.18501 | -50.53503 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1790013f-9b1d-3489-a9e3-2ee867abfacb | -2.98872 | -51.04427 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 19be423c-4c27-3719-bc83-3b9f2d232c4e | -1.10513 | -54.14096 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9c2c6fb-cd59-32f9-885d-ab4ada79396c | -3.01407 | -50.47534 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7442a670-25ec-37f5-ae17-2d1aa110143d | -2.81767 | -54.12203 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ecf63df-f50b-3ee7-bd6f-69c54ad323cb | -3.47302 | -50.1058 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9ceb505a-1405-3580-a555-e7405dcf524d | -3.7058 | -50.66094 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a2c1015-edfe-3f05-a078-c7fafc614aef | -3.94035 | -56.05255 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04363dd2-48d1-3648-ad6e-2d894a4a5f83 | -3.07276 | -49.5276 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6eb205d-948c-390b-9bcc-7b7a498280f2 | -3.67495 | -55.5151 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a632eb91-714f-3a88-9219-426f2efded69 | 1.76014 | -55.63953 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91acb17b-0612-333c-aad2-ee77e7afc8ce | -3.16095 | -54.07874 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23bd61d5-bd89-33ad-a1ad-022fc5acae23 | -3.4509 | -59.63728 | 2026-10-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83698e6d-c8ad-33eb-92c3-56c38b6f2d1f | -3.13611 | -53.74415 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0efb2736-6d57-3191-a1bd-6f33df9c78a5 | -6.03046 | -53.88585 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbfe9143-0a30-3bc1-a943-6b8ac44525b7 | -3.29826 | -50.3241 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a07bec0-a97c-3333-87e3-f411d8c07099 | -2.97041 | -53.266 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 902ea89e-c0e5-323c-8ffd-a3557f8ad9da | -3.06581 | -49.54176 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ce6e01e8-50aa-339f-926c-095f1b61df2b | -3.93737 | -55.85399 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a74a3aa-97c9-3f8a-9ad2-31c0b298bf15 | -4.12162 | -54.01895 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55acb687-df21-391d-bc17-68b60eba6497 | -2.56139 | -54.72642 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 95febaf2-4278-3f9e-8fa3-dbc4b7059d66 | -3.86706 | -55.8069 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f0053c0-a5cd-3949-8938-975fcd5791b8 | -3.95908 | -55.78122 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4801f57-af55-3a38-9dcd-2730f5f0cca4 | -3.49056 | -58.60409 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 84f62fb3-2178-31b2-a4e6-0c661b89db1c | -3.47699 | -50.10522 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c54add84-5154-3c60-b7b6-fca096c5c403 | -2.79779 | -54.11093 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93a440c4-07e4-3776-b29f-99fc737ce6d5 | -5.96015 | -55.35041 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32963065-1d8d-3b63-b3c3-1f155cbea918 | -1.09491 | -54.11609 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 07645902-1862-3919-ab9e-deeeb35eb7ae | -3.00967 | -50.47467 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 72311ad4-ca5b-3922-bfec-9f9479610a62 | -3.12412 | -53.73939 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a116494c-dbfc-3e2b-a354-e5b958b0d5ff | -4.25764 | -50.78774 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce27c199-60e2-300e-8635-b82717446af8 | -2.80528 | -54.13216 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b51d3583-62a3-3fa9-b17e-b013e3f2da3d | -2.80482 | -54.11202 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ea4fe87-a9f1-3f8e-936c-7caf83bea155 | -1.48351 | -49.43703 | 2026-10-04 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c91ff0c1-171b-37d8-96dc-4b90556c7dea | -1.75683 | -55.55459 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99943373-7641-3db7-9a78-fccce6ec8578 | -3.89511 | -49.69309 | 2026-10-04 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a737725-0be2-3a45-b32b-c2086ce736c1 | -2.94458 | -54.18811 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a551fdcb-241c-3822-bb48-022713cb802e | -2.8036 | -54.11987 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 534ed96e-221d-38ac-9941-b22c44391d12 | -3.88906 | -49.70142 | 2026-10-04 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0ff399d9-1dfa-3973-9bd8-7ec91394b992 | -3.0419 | -54.21471 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 045e6f86-f465-36b7-b947-720261e28eaa | -3.64236 | -55.50278 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b48f1f5e-10f2-305e-8abd-a0adb0d5caad | -4.20768 | -53.46057 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc0e80c1-3562-3370-88ec-b9e095a659f0 | -3.1887 | -54.08634 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 701c3f0e-e6db-3ace-a92f-8a2db655b27f | -2.82409 | -54.12703 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README59.md)
