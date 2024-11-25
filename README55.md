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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e9f2184-0d1a-3247-8c5c-5faa5c386866 | -1.62206 | -55.17881 | 2024-11-25 05:20:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c88041e-2699-3b9b-884b-15cc1f0794a7 | -3.70617 | -52.42051 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a2c6d762-5971-3471-9231-dd39b172d77e | -2.73388 | -54.13354 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19fd2eed-fd07-30de-8ffa-81567d09dde8 | -3.47753 | -51.99438 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36bc1b26-5fdd-3f70-ae16-9bea1d0a67d6 | -3.5475 | -51.52834 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f668d376-5df9-3117-8ec9-661f60da2dec | -0.94064 | -53.21522 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e8c9cf5-ac69-3fc0-932b-9a3584062374 | -0.92854 | -52.64907 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc48b67b-f093-3466-ac12-45cb580c15c7 | -2.81684 | -54.71418 | 2024-11-25 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af138b83-7d9b-3ce7-a3c9-ce94f7386bd8 | 1.71179 | -55.82368 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cf0872b6-dbd1-36b0-9f68-f6b2645ec92f | -3.65455 | -50.2353 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aef6a647-d11c-3a4f-b7a0-268a6ba450e1 | -1.23919 | -51.74114 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f689f3b8-ebbf-3523-a887-17fdedc3349f | -3.49625 | -50.46208 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ac7b494b-788c-361a-8f78-b2848a9e9284 | -1.72259 | -52.48676 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 202e35dc-7a45-3961-9f9c-61dfdc196b42 | -3.07239 | -50.95357 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be08653b-eaf5-32e8-9574-f667453bf89b | 1.94945 | -60.85543 | 2024-11-25 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e11fd84-5d79-3132-ac63-6e65b526f4cd | -2.36857 | -53.85951 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a31686a8-884f-3233-8285-d64196923cb0 | -2.89686 | -51.57178 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 758a2be5-db9e-318c-acae-3112ac586c79 | -2.97902 | -54.08263 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1eb35670-4b09-3ac7-9b51-c0f0a83beaeb | -0.24454 | -51.61466 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d6f47d8-df03-3561-8de4-997597aed77a | -0.95162 | -51.63926 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e950f99-e068-34b5-8dda-f108de415f66 | -3.49235 | -50.46133 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b91d1c14-b590-3434-b03a-5b4e0be31863 | -2.82434 | -54.10054 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b109e22d-14d9-33a6-b907-8cbfa43c041a | -1.23021 | -51.79821 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 353662bd-1f51-3a2e-bbb7-0a201091f7e8 | -1.4522 | -53.40415 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 639c7864-a649-3a0f-9e90-a4a01763f8a9 | -3.71157 | -51.80449 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfd190dc-0f0c-3aef-8880-cbb39b08b6bb | -3.10455 | -54.98079 | 2024-11-25 05:20:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6618c2ed-289c-3300-9e2f-ba2006438a43 | -2.80249 | -53.0084 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df46c82b-8137-3559-903b-f831d1c5297b | -3.24713 | -54.21981 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ca93f90-1f74-39d0-99e4-30d00a3632a9 | -3.51728 | -53.81456 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c804fe15-1307-3845-9289-5ef11e17f2c7 | -2.82786 | -54.0224 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94355233-ab3f-3f69-9efc-742d291b1c96 | -2.56691 | -54.06197 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8989b7cb-0604-3755-9563-80165ca3bb75 | -2.46219 | -53.69561 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33ac0f41-64cc-3817-8b85-a88841517c1d | -2.83266 | -54.01916 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ddf0d61-cd0a-3450-adfc-06a8f6cf8169 | -2.85885 | -51.2763 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c964a92-7c5b-3fb8-aae5-c33fc96e70d6 | -3.10541 | -53.99001 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 678aafc9-8505-321f-b169-6898bc1a92c4 | -3.50426 | -53.81319 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38ef52aa-6033-3c6a-b2fd-94086951ff82 | -3.25189 | -54.21667 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 669d9da6-4301-3f10-8858-9d8879df6206 | -3.53286 | -54.07894 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42cb46c2-948d-3421-87cb-4a8c274aba15 | -1.04313 | -51.74136 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 78622994-639f-3798-b364-2e1e488b48fa | -0.74043 | -51.95385 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7866cfb6-84a2-38be-85e7-6a093388a111 | -3.25607 | -54.21732 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c54193f-c6fd-3d57-90d0-95f4f8d27b8f | -2.5876 | -54.2313 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 940c5c63-48eb-3f91-9e95-c17870cc412f | -3.80115 | -51.17649 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9230548-59f4-39cd-a660-0ce1bbdb1884 | -2.82726 | -54.02627 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9c3f4e4-2d73-3097-9cab-9daf0189ce64 | -1.61057 | -53.30558 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82912ed9-9adb-3e2a-b73d-64d803e7a085 | -3.94761 | -47.99664 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45edb21d-c974-34be-883e-7dcd8806576a | -3.25175 | -54.2271 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93c48e73-5cde-313b-b91d-733180307a04 | -3.84886 | -52.15495 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a6fc89f-d5a9-3879-bb5e-c3f1c7cea985 | -3.06718 | -50.95272 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee83b4c2-2242-31f6-899b-2295952a63ab | -1.54787 | -52.58385 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f32d385b-550f-37b6-8e28-b0b708a1e05f | -3.81484 | -51.99788 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 526bd1a0-c016-3a19-96af-60a17cd478bc | -3.53218 | -54.49335 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b73b37c-e74b-321d-9b24-29e42cf4021c | -3.42663 | -53.28579 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 972dc1d4-fdff-3eb7-a3f2-ced622e479f2 | -3.46908 | -47.68691 | 2024-11-25 05:20:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d209c5c2-71e7-3466-b354-b7166cb62204 | -3.25997 | -53.70816 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dde76958-9a9b-3381-a24c-5ac85760dc39 | -1.11198 | -53.39372 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c04316d9-8cbe-322c-870a-8acabb227005 | -3.24522 | -54.71721 | 2024-11-25 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb0bcd60-dcd8-3d90-b908-876ba10e44f5 | -2.7973 | -53.01232 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ddf57c7-8645-3837-b20d-93a49bedb28b | -3.25479 | -54.23545 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f50fc545-569e-3135-9534-2d50f82de3b5 | -4.54677 | -48.95456 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49645883-0d10-32b3-9d90-e7883ec094d4 | -2.67779 | -53.05919 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0fab7f6-23a4-3fae-8bdc-a87efc994346 | -0.99846 | -57.5288 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a87f79af-bc64-32da-b729-8ec407447f2b | 1.44556 | -56.01746 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eab2feb6-08ac-33bc-9ebe-b3a2f31f0727 | -4.29075 | -46.90693 | 2024-11-25 05:20:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 176736db-f1ae-3a36-95fc-f6cc764fc475 | -2.80682 | -54.01931 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc6ae6a0-2ef2-3d5c-8ed1-153f1c927604 | -3.31857 | -54.09565 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4209a769-c930-3bd5-bc8b-7ad95971663d | -1.77498 | -52.72971 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2d08d4d-a189-36d4-894a-62c16c9ea0f0 | -3.25372 | -53.27358 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f912d73-4283-32e8-8da4-e054eee9c40d | -4.29759 | -46.90806 | 2024-11-25 05:20:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 86db041e-56ae-38bc-821b-4d27a6c5a156 | -2.89644 | -51.57465 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ea37c77-841f-3c69-83f6-0f6dc90916c3 | -2.33205 | -53.87182 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b958ab2a-bc58-39fe-a955-b8fc339777b4 | -3.25131 | -54.22044 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 131b29db-f8e0-3eb9-b013-7a5ca79367bf | -2.8584 | -51.2793 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0aa46c96-cfc2-3865-a078-cf6e9655ee5c | -2.56748 | -54.05819 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b1ab427-878d-3f69-9580-269901b07a63 | -0.8793 | -51.72404 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9f6a4992-33ee-39fc-b87e-87adf963e3e5 | -1.11688 | -53.39026 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1bd3a80-6d03-3642-b535-e9bc4a3c10f9 | -2.85836 | -53.96609 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0fe5c52-5a52-39cc-865f-ded2abb12f95 | 1.39556 | -55.90724 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abca9748-e9e6-3265-845d-e8e2938f0d2f | -3.5012 | -50.46606 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cc94cc64-770c-3199-9aa3-3fa1b48b60c1 | -2.96962 | -53.86189 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b96380df-0ada-3110-ac63-0dde9fb5e92a | -1.11136 | -53.3978 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e4c4321-a4c9-3527-a4de-2f929b3dd179 | -0.81532 | -51.59993 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18bb95c0-e5d7-35fd-b41f-c8c87e93a8fb | -1.77184 | -52.71991 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7869c2f-2e22-31c0-95ed-cac244bee8ee | -0.3575 | -51.97816 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5c2ed77-8fcc-3417-becf-d2549f691bec | -1.0025 | -57.50327 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc188461-09e1-3038-be6d-57f98fc1af09 | -0.74119 | -51.94892 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32cebaad-7ad7-3d65-8257-63cca8a9c345 | -3.10415 | -53.96958 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e58e8e5-e17e-3716-8c22-dab6d0ba9cf4 | -2.81721 | -54.11895 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f44d0579-a314-382d-a3ba-92f89d42354f | -1.71776 | -52.75988 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a4e4fc5-6f8d-3054-9396-2225439471c9 | -2.17164 | -52.08067 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c443a88-de28-3d5a-b508-9eb8a8e9961f | -4.41294 | -49.70552 | 2024-11-25 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50943145-c548-372f-ae59-a22af2c2fc4e | -3.28632 | -53.85369 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db47495a-ce18-3043-836a-d60a6dba4715 | -2.79578 | -53.00905 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6008e1f-97d2-38b9-ae93-919bc0cd7db4 | -1.92208 | -53.00325 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49619f47-37d6-3ddc-aaf1-4e88c7aedb24 | -2.8796 | -51.58291 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 994df032-b54c-3624-8bf6-60ea78a3e38f | -3.4973 | -50.46548 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 66a6ee8a-dbf8-3ebc-879c-ff13af6d2ad6 | -1.48349 | -52.51712 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb009b4c-cdd0-3600-84aa-050bb548a557 | -2.64705 | -51.77519 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4502e67-9de8-358a-bd86-418ff55dde9b | -3.39807 | -53.80186 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e79003e1-e81d-3f00-9276-23f6e5429089 | -2.82907 | -54.04234 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README56.md)
