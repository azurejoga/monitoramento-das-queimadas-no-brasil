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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 274ddf22-15bf-3399-b225-4b07660abbe1 | -9.79762 | -60.14348 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fd7720e-6bb9-3219-b34c-841e35e5ed7a | -9.89237 | -65.02007 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b24b9afe-839c-33f6-bc41-59589e08d432 | -8.58711 | -67.14602 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3471c397-2de7-38e4-96cb-b7595ea2afab | -8.89427 | -66.88835 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab30df3b-56a2-36f9-ae93-ceb8f3283171 | -9.71334 | -65.06583 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b971fa42-387c-3d61-87f6-30f0af9fc22e | -8.66828 | -67.11518 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec68eb15-461f-38d6-ba01-4ed8108c2def | -9.82273 | -65.06014 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55911bff-68b1-3262-9e20-b1144a093674 | -8.88796 | -66.89364 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5092e87d-2517-32ed-af94-e1e544405fcf | -9.08023 | -61.15512 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dd946ad-1851-3b0d-a9c4-13bfe97acfec | -10.98862 | -59.14516 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ddbd073-71c7-3900-b523-14b71f2c3e9f | -8.59398 | -66.81388 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aacb4e13-494b-35ca-9156-1bda09600213 | -7.74878 | -49.20663 | 2026-10-04 05:18:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0af87c0b-148f-393a-a9f0-a5965c5f236d | -9.08749 | -63.98044 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c8bcacb-35f6-3539-8b1e-0ecb730fc8aa | -9.88455 | -65.14034 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1bbb1ce1-c069-346d-81e4-1c1fc0b312b8 | -8.55882 | -67.06309 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00fead41-b0bb-340d-9817-d67d47b5879b | -8.88713 | -66.8887 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef91ae0d-ccbd-3c2f-aba7-01a066f55ef5 | -9.91102 | -65.0189 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a6857a7-3949-3dbc-af92-b2ea68e18fce | -10.34564 | -58.49077 | 2026-10-04 05:18:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0654a0c7-5b69-3ff4-8d28-bcb3ef0f3212 | -9.95234 | -59.60661 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26c03ef7-a49c-3f08-af19-13eaf5d0c764 | -9.46778 | -64.33489 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fdf62da-8421-3de5-8a69-8c3dc950c634 | -10.95541 | -60.91145 | 2026-10-04 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4fe6f67-1056-3ce2-9236-b1674e74bcfd | -9.47709 | -64.33237 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5294ad60-0304-33a8-8966-133b1a125a72 | -7.33235 | -55.03217 | 2026-10-04 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36e82992-38b5-317e-967e-4e2797f252fb | -8.73537 | -66.57735 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deda3467-a727-3e72-a64d-ab49baf558b9 | -9.01454 | -65.69879 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8a5a170-1aa2-3e00-b2f0-5e070126dd73 | -8.5774 | -66.81716 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb440d61-4a5e-3928-95a1-9f66ec4c415e | -9.46349 | -64.3341 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 223bd50f-214d-3e6e-a598-e436bd7f43b2 | -11.05451 | -62.57849 | 2026-10-04 05:18:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06d2b7ef-8121-3654-838a-b5f2eef7f327 | -9.48139 | -64.69004 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a472ffdc-edf5-30fb-b9a8-d96f9b5c2d15 | -9.13301 | -65.94476 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e60f8d9e-d835-37c6-9d40-e43176ebac7c | -10.80076 | -57.25266 | 2026-10-04 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3cb810b-2d0b-3388-b5f9-bbee8b88adbb | -9.13128 | -67.92934 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b92e1fc7-6fe5-301c-a659-388cbfdfe812 | -8.56891 | -67.00828 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f38e2c83-3e28-3247-95d6-ab3a86ab3d87 | -9.92279 | -65.03036 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e4e5583-40bd-302c-81e8-2c4f598ab6b9 | -8.59456 | -66.81075 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2cd3978e-9d11-3ac9-848e-828a27289a87 | -8.51208 | -67.11473 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 420570e6-c362-3c65-9203-7579a727e0b5 | -9.89318 | -65.01562 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c5f2439-c11d-3c45-8334-8c721d7e93dd | -6.45459 | -55.00291 | 2026-10-04 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 517348c9-cdf5-3e88-b022-13c21238f96f | -8.55762 | -67.06957 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b16c803b-3a0d-3a04-9d27-0ed5e115a725 | -9.10362 | -49.78167 | 2026-10-04 05:18:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50b82bd5-6276-3e98-a4a7-9c06f57d9ea5 | -9.91752 | -65.03402 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c996b095-e672-3e59-ac16-6d58fe131aab | -9.10882 | -67.7139 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3726b179-305e-35e9-861e-36583336d1ee | -8.88251 | -66.76662 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a24d838-823a-30a0-be65-ca6139454c52 | -8.57436 | -66.82597 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfd1ac01-d791-39f0-ac96-00ada58f0265 | -5.89241 | -57.67353 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc49dd8f-e39f-3427-95ca-46ed838d2f4b | -8.5883 | -67.13944 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f15be2b3-50d2-3dbe-8814-2b9f208949eb | -7.33296 | -55.02816 | 2026-10-04 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb165e01-bed7-35e2-8db3-9d93acbc8737 | -5.89575 | -57.71653 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aed5232-3dda-38f7-8b1a-73d28020d2d7 | -9.61769 | -64.17749 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f66fc486-6158-3196-ab6d-a197212f8c21 | -9.91957 | -65.0484 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3632ea44-3fc5-37e8-a031-880898339d31 | -10.26827 | -63.83377 | 2026-10-04 05:18:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5769289-f560-398b-b820-72e826bfdae3 | -9.12513 | -67.93193 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e81b8236-93e6-3ce7-8859-118d93b026ca | -7.87817 | -61.43615 | 2026-10-04 05:18:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c334b493-9c32-3828-82cc-9c3fdd4f5726 | -10.80524 | -57.24595 | 2026-10-04 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6790827d-db76-339a-b6bb-90d82efa2021 | -9.03422 | -67.47455 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecee02fb-2f72-3c8c-b512-3eb2d77f9b4b | -9.64283 | -64.57082 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aac96b42-1c5b-3700-ae43-1d5f2e1d153a | -7.27678 | -49.25639 | 2026-10-04 05:18:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b457b65d-6d4d-312c-8fa1-ac9f8558cbe8 | -8.04932 | -67.27232 | 2026-10-04 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7009c191-c9f5-3b20-9f45-6a7bda72880f | -9.46423 | -64.32996 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e86ac43-a8d9-3735-9a1c-f022c3889d2b | -9.14933 | -65.39536 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 788f4042-7b5f-39c6-959e-cd67394268cf | -9.21673 | -57.63717 | 2026-10-04 05:18:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f18391a-6190-397e-bb11-bd0633fd1bce | -9.11424 | -67.71494 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3f35596-45c8-36f1-ac3f-14dcb3832c0e | -9.1316 | -67.92795 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2397f99-f281-3af9-80f1-738cab83f5f9 | -5.8963 | -57.71309 | 2026-10-04 05:18:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a92770c-fe29-3df1-b217-f9741a1a96e5 | -9.12818 | -68.2514 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f71e587-4df1-3bfc-b186-9eebe513710a | -9.91672 | -65.03853 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4d2dada-1328-36e9-a27a-992b345311ad | -10.80131 | -57.24904 | 2026-10-04 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 878bec7d-ca8b-37f9-8838-2c05ac01ed92 | -6.50006 | -58.53096 | 2026-10-04 05:18:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 202b8b31-9cf9-3269-89bc-11ce0d589611 | -6.49451 | -58.52282 | 2026-10-04 05:18:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d630bba-6d32-3f17-b2ff-74703a456014 | -9.16299 | -68.26884 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5423699f-e0c6-3596-8262-e1c73c2e803f | -9.1291 | -65.46513 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 035e6c8f-95be-39bf-9998-a916bd568447 | -10.99031 | -59.1346 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f8720af-084b-3b5f-a769-54e59190b231 | -9.9151 | -65.04757 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e89556e-54bd-31dd-8770-3a79ee9bea93 | -11.05826 | -62.57919 | 2026-10-04 05:18:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d25b5ca-0c85-34c9-b4f9-4568d4e8f717 | -9.08601 | -61.16458 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 860be3ba-cda9-3a6f-a4ff-b3a6a5e76772 | -8.66263 | -64.27847 | 2026-10-04 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2eb964a-c771-368c-8b2b-5eed949032f7 | -8.87685 | -66.76872 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f3ab18b-4b0f-3077-82f0-593426e73748 | -9.129 | -65.88399 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66eb6dbb-a6ca-30cb-ba24-c5f2a9fe47f2 | -9.79421 | -60.14292 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5f97b98-7425-32cb-8be9-639b26e41f43 | -8.5889 | -67.13616 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ee1c203-386c-3b2d-93c7-6776dbeff669 | -9.88537 | -65.13578 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ee4f692b-aa4a-336c-abe7-f1a50348dad4 | -9.91144 | -65.04222 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 244c73d0-8c79-3f25-ac67-7363df46c6de | -9.15738 | -68.26779 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03a38bd7-e6d7-39f7-a0a7-de6711802430 | -8.85709 | -66.79029 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 150ba650-e157-3f29-9f8a-8fe6e32e4aaa | -9.37626 | -65.4723 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eeba8e9-21be-30f1-a7ac-b21d3d5c0a79 | -9.79701 | -60.1472 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7450cb55-3500-3c6b-b5ec-f7617c0ba25c | -9.1345 | -68.24863 | 2026-10-04 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9395db7c-5a3b-3ee9-885f-41514f4f6f2f | -9.36328 | -60.31206 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba2b7cd9-3a7e-395c-af12-b88531814292 | -9.08312 | -61.15985 | 2026-10-04 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abe39251-f3b3-3190-884a-616e92d3cd52 | -9.81826 | -65.05929 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c6067de-50bf-3770-9c70-4758124824f4 | -8.89338 | -66.88346 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d80828b-d26c-301c-99da-222bd7fe93d5 | -11.74312 | -58.56633 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ac31b80-bef3-3e53-81a7-cd7c33ef0e89 | -9.92199 | -65.03486 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a3c6f11-7078-3146-a7e0-9ae8227cd5cb | -9.60673 | -64.04137 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cd7e69f-5fbe-38bd-a862-505151c8b07d | -9.47134 | -64.3398 | 2026-10-04 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ff104cb-f57b-3c74-b6ef-5f3b66392d00 | -7.32881 | -55.03162 | 2026-10-04 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1841a5d0-3aae-3291-b63e-bb06759b1125 | -8.88854 | -66.89049 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b110494-1952-36f4-8164-65c774bec382 | -9.94504 | -59.6091 | 2026-10-04 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7453787-4a69-32cd-b56e-980e0f55b53c | -11.73981 | -58.56579 | 2026-10-04 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d2294b3-ddaf-370c-9abe-148c59dc3766 | -8.58769 | -66.81911 | 2026-10-04 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README65.md)
