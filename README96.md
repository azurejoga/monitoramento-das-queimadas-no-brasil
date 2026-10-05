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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82a2d163-b2f0-3edc-a677-3119fc581e9c | -2.81953 | -57.29404 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7b8a1fc1-ed64-352d-8b0a-a569740eca6e | -3.30293 | -53.84502 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85dc417a-3ef7-3bd9-b167-430e944d4668 | -6.33019 | -55.32331 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a6fc9ad5-f3ef-342d-8edb-f376ac93d51a | -3.93666 | -40.72389 | 2026-10-05 16:39:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 15.9 |
| fa5b2142-f323-3fde-bc64-2610d1190bf6 | -3.06443 | -54.16133 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d23ce4f7-8460-3501-8622-5c66d47891a3 | -1.42445 | -47.67778 | 2026-10-05 16:39:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12acffc5-4d6d-3e1e-97c0-970b6c496a1f | -2.96219 | -41.99516 | 2026-10-05 16:39:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c003d7c-afe8-3495-af20-911aec00b22c | -3.92009 | -44.1446 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e5d5041b-dc25-3d09-9923-a59fd604486c | -3.59283 | -54.31505 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6d336e5e-c8ce-3388-b90d-37574d1a78a1 | -4.35448 | -43.82769 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| efd6631c-8819-3da5-8599-a74d5dc800d9 | -1.46923 | -53.61684 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 63428c41-fee1-3ddf-a13e-33e0630ed802 | -6.06003 | -45.13172 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc90b7ef-e45f-36e0-b78f-0c47c92d54be | -3.27078 | -44.66238 | 2026-10-05 16:39:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eac5a490-9c6e-3b00-b9cb-b003fade2a1c | -3.8686 | -55.83302 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 922decf6-7a98-3821-b05a-d936cd88fc89 | -1.07163 | -52.27437 | 2026-10-05 16:39:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| aece9135-f4a0-387d-9bfe-621492fe6901 | -3.72202 | -45.40709 | 2026-10-05 16:39:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 93165d47-7702-334c-a586-712ded961cf1 | -3.52727 | -58.57211 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 421d94fe-6e60-3dc3-9d29-05c5d8211ae1 | -3.16951 | -50.43391 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| e5509724-c717-311f-9d64-55fe8424f889 | -2.60273 | -57.56733 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 23710a16-128d-3db8-b692-66037ce48544 | -3.112 | -40.16247 | 2026-10-05 16:39:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 34ab7c67-4338-3ed8-b3e2-a7608999af78 | -4.36883 | -43.91667 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5498ae5a-67da-327c-b79c-538f503830cc | -4.96302 | -40.56347 | 2026-10-05 16:39:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 40.0 |
| c0fadd78-c8ad-33e6-86e2-a8c4370c0514 | -3.42224 | -60.55026 | 2026-10-05 16:39:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6f0373ef-93bd-322a-9a07-f8d881a385c9 | -2.03909 | -54.3089 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ed10a7bf-5152-34b9-ae97-99ca93004f9e | -4.15176 | -38.48131 | 2026-10-05 16:39:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ad3c85b0-3af0-394b-a353-1b0f68e3a02f | -4.37644 | -43.91549 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c6a2dac-2793-3945-ae22-17ca147f98e6 | -1.12781 | -49.23525 | 2026-10-05 16:39:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 4b0a0963-66d4-3b64-8fe4-5291c56985b1 | -3.77458 | -39.84544 | 2026-10-05 16:39:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| a881c4a9-f1a3-3812-a7d0-fa40f8823321 | -2.95692 | -42.90333 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 2e370065-81f4-3f6b-bbf6-8b12cedd606e | -4.33477 | -43.81924 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 654ea771-a477-3c9c-88fe-45b77d641fb2 | -2.75824 | -57.64861 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 131fd633-8f7f-3c43-903b-2f1d238511c6 | -3.0928 | -43.91838 | 2026-10-05 16:39:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cc8c97fd-d6af-3735-98c9-efcbf73aaf54 | -5.03893 | -44.44592 | 2026-10-05 16:39:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 59e86a98-ffb1-3a7e-b5f7-9f61862a911c | -5.03721 | -43.75067 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a92bbcb1-b379-3118-b532-9c0ca9ebb611 | -3.62448 | -45.33974 | 2026-10-05 16:39:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b337a2fa-f17f-34f8-aa63-77457ddc7ab2 | -6.80955 | -55.29655 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 25e89aa9-7856-36a6-970a-696795456b3f | -5.19817 | -37.36591 | 2026-10-05 16:39:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 609f9149-6ede-3cfb-a479-c8cf552f26bc | -3.17501 | -45.29421 | 2026-10-05 16:39:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| df91e540-b1d4-33e7-8298-32f1fe9b5075 | -3.14323 | -53.72481 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 4f6d63ff-8ca8-3710-8ba8-10b26f473f08 | -0.63959 | -47.34161 | 2026-10-05 16:39:00 | NOAA-21 | SALINÓPOLIS | PARÁ | Brasil | 1506203 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99ac77ae-b44d-3cfe-bef5-0c46818aa3e0 | -3.654 | -59.15975 | 2026-10-05 16:39:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 702bc351-03b6-3c96-8716-27f087074335 | -5.52188 | -41.01675 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 200.8 |
| ca0a633b-4e2d-301d-908e-ca2456b28189 | -4.70125 | -44.20407 | 2026-10-05 16:39:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 74c3c488-9af9-3bf1-bb3e-c7582228485d | -3.16585 | -41.40316 | 2026-10-05 16:39:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 86ebb5d5-72d7-3eef-af92-d89e45370848 | -3.61839 | -45.3242 | 2026-10-05 16:39:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b9ef09e5-2c45-3cd6-a270-f8e58a5d8ccd | -4.36858 | -55.42654 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a7d37b87-3946-3b7f-89a4-cf58450f1bf2 | -3.13332 | -53.7148 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d54c7c19-acf8-3e6a-a81f-11fba60d023d | -5.83438 | -45.00903 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6c521f06-e936-3293-a45c-c1610d597dae | -3.3299 | -59.4796 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| c363b7e6-ed91-3340-bf41-51a52e7ad55e | -3.37355 | -58.19967 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| f0dd793b-7731-3b8b-ab37-2ff0a1967ec7 | -4.11699 | -54.41991 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| cb2035d3-0fe1-3389-a09b-f16b03d1ef7f | -3.62244 | -58.61298 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dc025ee1-a190-3376-aee1-3ac9cae4d920 | -2.95106 | -54.1566 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| acd04455-31ed-357d-9f12-c40fae055371 | -4.13833 | -44.98743 | 2026-10-05 16:39:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 81229bfc-0b6c-3398-8983-2f16690ca53e | -3.05928 | -43.39674 | 2026-10-05 16:39:00 | NOAA-21 | BELÁGUA | MARANHÃO | Brasil | 2101731 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4f1abab2-ee8f-363b-8937-141b489ded44 | -3.99982 | -38.35429 | 2026-10-05 16:39:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| fed08c5a-3bc3-3af6-8cd7-423fd452933c | -5.12542 | -43.99105 | 2026-10-05 16:39:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 81525dbf-b31a-3880-90a2-f6a1c107a4a0 | -4.67116 | -43.57321 | 2026-10-05 16:39:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8ab2af23-2164-3d7a-abcb-2b970307f145 | -3.04038 | -54.26312 | 2026-10-05 16:39:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7c5c5fb9-7377-348c-9205-6fa637606394 | -7.22287 | -55.20014 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6bf0b9c4-0829-3904-bf28-6e40dc5a247e | -2.8562 | -51.30236 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b781d030-6677-30e5-a54b-a4f3faab915a | -3.88005 | -41.02342 | 2026-10-05 16:39:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| a90ac578-c9cf-3aa9-9a33-c173e7e4039a | -4.20804 | -53.46486 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2d18a974-85e4-3b2a-86cb-a67bcc49cf06 | -3.11233 | -44.28728 | 2026-10-05 16:39:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 10ac0ce9-987b-3aab-b144-5f9630020e0b | -1.10519 | -54.15047 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 40947742-417a-3b91-bcfd-c6d0a18e5e36 | -3.05453 | -54.21144 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ba685cb5-61f1-3f92-a74a-8c0a4c804a09 | -3.36141 | -42.61002 | 2026-10-05 16:39:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a9847594-f964-3484-b4f9-9e01ed793500 | -3.24068 | -56.80416 | 2026-10-05 16:39:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 048c09ab-8886-3f47-b72b-25c346217900 | -3.50665 | -54.61631 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 65619ad4-5047-322d-a76e-1fc451966db8 | -5.30561 | -43.21502 | 2026-10-05 16:39:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 15f03728-c74c-38b0-82f9-1f8d6cb2f840 | -2.93198 | -53.94496 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 006316c2-7b8e-320a-950f-ecb0c050dbee | -3.1018 | -53.72007 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ca52a6b6-c684-3cf8-b27c-3ae178f8054c | -3.95245 | -42.97237 | 2026-10-05 16:39:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 73b1ca85-e651-3143-8bd8-bf2a9f40a1ef | -3.10236 | -53.7238 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| a32eddc0-ced9-37d7-9164-1786f80f17ed | -5.83186 | -45.0137 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5c9fd3cd-7e58-31ae-8bbd-9e4808a96414 | -5.21954 | -39.56536 | 2026-10-05 16:39:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 5edc73bf-5ad1-31cc-bccc-da8203834f82 | -4.46173 | -54.96105 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| aac49cf8-1700-3c9d-972a-3db5b521bc1e | -0.83457 | -48.62724 | 2026-10-05 16:39:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dd7029e-b1f9-3690-acb1-3f3fa38a5cda | -2.63757 | -57.72495 | 2026-10-05 16:39:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 788df18b-8112-395f-a0bb-14063b1d9958 | -5.11523 | -36.8328 | 2026-10-05 16:39:00 | NOAA-21 | PORTO DO MANGUE | RIO GRANDE DO NORTE | Brasil | 2410256 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eccbed4b-01bc-398e-8609-cb1dc171c467 | -3.94138 | -40.72304 | 2026-10-05 16:39:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 12c84ffb-16ef-3725-9f8c-2798e6655e0a | -0.38252 | -52.08033 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bd92b95d-b600-3081-a12d-f84e3ab403bb | -2.26808 | -57.09027 | 2026-10-05 16:39:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ba39c79-05b2-3e79-acee-f65bf85beed3 | -5.98694 | -53.63004 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d5e1cff7-0536-395e-b9b9-e181750e8401 | -4.51507 | -42.07107 | 2026-10-05 16:39:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 10511802-ad7d-3a2e-8c6e-7b8ecb377d25 | -7.22162 | -55.20258 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6d80022e-b6e8-33c3-a295-09553e6a767a | -3.58353 | -39.23536 | 2026-10-05 16:39:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 18fe39b4-b174-3ece-bc1d-b95ee02ca613 | -3.11165 | -42.92825 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8843b80c-92db-387f-9d40-9dda81827cd6 | -3.04717 | -57.52022 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 55a9d8f7-40fb-3a99-a465-e37f69fd37c9 | -3.41357 | -42.66001 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 747f0530-62b5-3482-ac11-dcaedf89910c | -5.94606 | -41.3516 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 8dadf370-6cf1-36ce-8538-543872e34a9c | -4.44927 | -54.97211 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 6214c31f-6881-3b89-9557-7f84d5cb3cb8 | -3.67915 | -60.62614 | 2026-10-05 16:39:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| b0d372bc-a2d7-3633-b48e-afdf24c65e60 | -3.28418 | -42.26012 | 2026-10-05 16:39:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 78921694-6586-378b-9059-01bce4375f4c | -2.94621 | -54.15321 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 08100416-1618-3b00-aeee-d2bbeb95c25c | -3.05026 | -54.21205 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5ab978f2-a370-389a-9a6c-5ff4aaad9673 | -2.93358 | -54.12681 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b86be796-9102-3a14-9177-a2f8bd589501 | -3.11307 | -44.2919 | 2026-10-05 16:39:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6d3a6004-d154-368e-83f2-84d7b1bcddaa | -4.37794 | -43.92483 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fb278164-4290-3f01-943b-4c7b5248836e | -5.39779 | -54.45273 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README97.md)
