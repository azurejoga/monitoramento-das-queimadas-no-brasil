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
| c7d0ffa9-0d71-366b-a442-0c2abd8d0608 | -2.6759 | -57.555 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4a8ae5eb-f700-3f39-bb45-cb4bcfe625a9 | -6.29756 | -59.94981 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 335c58c6-1629-344d-932e-cd273619170a | -6.29515 | -59.9402 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f08c55c-63e3-3e04-9ecf-a23e9c1194b7 | -7.57782 | -57.6944 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f06fa92-9c92-37dd-8330-0ff186aee376 | -2.92977 | -50.40303 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 583b58ee-6390-369b-8ca0-b853daa2baff | -3.136 | -60.62796 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c73a81be-29be-3392-8571-4fb158041415 | -2.90729 | -50.39421 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3fe4bd7b-1887-31da-98b8-6ba64c0e0d59 | -3.41139 | -58.21005 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bd6ac36a-6b90-361b-bddf-97ee6a46ace2 | -6.85901 | -55.56725 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01b214dc-51cd-3ee9-baf9-a085b15a33ad | -6.06909 | -57.86187 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5afb05b5-6d6e-3568-bfd2-74e183256cf8 | -2.62003 | -54.72738 | 2026-09-14 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de50ab8b-1dd3-3787-ac78-55f74eab41f3 | -3.37329 | -61.34283 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e806a7f-a60d-3065-bc99-cae1b323457f | -3.73487 | -61.75101 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e498835c-03ec-3bd0-aa75-833db726649e | -2.92152 | -50.36534 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b02ffb2-2390-35a8-9a61-3081b6b7b02e | -6.79153 | -62.98057 | 2026-09-14 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39f6f4cf-f7cf-3783-b3ec-f8fe93726fe5 | -3.15278 | -60.65841 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf6fc279-7740-3d9f-b862-803e0781855c | -2.70195 | -57.55128 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03285589-86ef-319e-b63d-9d0d0ac8de8b | -6.30736 | -55.27552 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 994c68c1-dff3-302d-b3f4-617f0d37fe7c | -3.60203 | -59.0707 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f79ad8fe-8910-35f2-a5f4-0d4c7fa6e93a | -2.89131 | -50.38477 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8b56f2c-4aed-3755-a59a-77a70b11dc17 | -6.02452 | -59.94067 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b79b66e8-c779-39e3-b74e-e66ff6533fda | -2.91637 | -50.40097 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9f99bc9f-3ce5-3c40-bf68-a4c9e5065268 | -3.37955 | -61.32494 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52b0a6b5-472b-3e4e-acda-897a0d6df459 | -3.35131 | -58.14318 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc5d7a0e-9904-38e5-8e89-d561fb45941a | -6.79829 | -58.78961 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b9a4f98-9cda-3168-adf2-445f320904f8 | -6.58244 | -58.84199 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf1341cd-11fa-3700-bc7c-80df67f3331c | -2.88051 | -50.39006 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33ceedb7-9460-3eaa-9118-0683b641b1df | -2.91539 | -50.45501 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6434b55-7b9c-34bb-bc06-19f6f7753629 | -2.92392 | -50.39613 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2da7e1f1-edc9-32bb-bcc6-7628926cb40b | -3.74219 | -61.74844 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cee535b-cd56-335a-a738-4e5649da65e6 | -3.43249 | -61.07398 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d01f831b-e54e-3b75-a923-37b709f17788 | -3.15378 | -60.41761 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff0776b9-104d-3d1e-825e-637d4cc9b4cb | -6.56801 | -58.56917 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c7393aa-a380-34d5-bcfa-6ec4177f3473 | -2.91808 | -50.38915 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 91602874-6656-3521-9c74-5aebf970b090 | -2.99562 | -60.81154 | 2026-09-14 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f42f2c-6ee7-3e5a-be12-722732ecf81d | -3.73825 | -61.75153 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d3805ed-2573-3a78-8c59-aded5523c9ba | -2.91225 | -50.38206 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5aaa359b-0407-3fa7-8a29-975f31a264e8 | -2.83584 | -57.63589 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09130e76-813d-371c-84ec-4d673699c243 | -5.59227 | -60.18671 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5982debe-6486-3a98-b001-3bcb7ba8e77b | -6.58296 | -58.83845 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c0edb92-38ae-39dc-a9db-b185caea5a40 | -5.59162 | -60.19103 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04621254-5218-3d19-932e-930ed5f718eb | -3.34088 | -58.20375 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f6ec9a0-0cd4-34c4-adcf-bea931072c52 | -3.39203 | -59.41187 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 275f5fd2-4a43-3751-9ef1-a7aa0326ee7e | -8.12058 | -54.80459 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e45ccfda-932f-38e2-b1fb-b26a7304abee | -4.0967 | -54.44231 | 2026-09-14 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8eedb41-77ff-321d-af77-d5fb1cc41b98 | -6.2868 | -55.27262 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08a5589e-5c3f-33b1-ac75-4ed6bdce145c | -2.90884 | -50.40578 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fae446ef-ad89-30d1-b245-1ae6b3ba2f20 | -6.34266 | -57.87697 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c9d288c-7053-35ed-b046-ecf90283a4e8 | -2.90969 | -50.39985 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a5f66c4a-523e-31d3-b016-f7d195082654 | -6.65244 | -59.96117 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b156048-8dd0-34bd-9147-60b1d62eeec4 | -5.07363 | -56.25386 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd42bc83-5674-3ce4-a679-5c3d3bbf8300 | -3.55829 | -59.04959 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33641905-0788-348e-8056-ed77c3eb78a0 | -2.89175 | -50.45198 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac788e4a-d735-39a9-84f3-db7b276c5acd | -3.16748 | -58.65057 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 54d61929-26c1-366f-8dc7-c293110aeafa | -2.92564 | -50.38425 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 96ed6a15-808e-3ec8-8fd5-41caebc00682 | -8.11921 | -54.80251 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f794b5c7-0903-30cb-bfbe-b53d2afbde44 | -3.73432 | -61.75462 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aca8374b-db0a-38f9-8fd7-dc0c4a4cda4a | -4.3938 | -55.20519 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c8955de-1c65-3d59-a520-4d0a87235ea0 | -3.17614 | -61.18841 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1d925dd-2950-37f6-87b7-126124c9b987 | -6.82739 | -58.64813 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c29a8b4-c910-3cd6-a4bd-7ae744818646 | -3.1718 | -58.65304 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b50388f3-2914-3e58-be4a-7507d5e57661 | -2.90461 | -50.43512 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 07e63a94-8e83-318a-8fe8-e2ce59c7e365 | -4.11967 | -60.68611 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f76807aa-2b55-3af7-9df4-d40cde2ec0e5 | -3.18021 | -61.11668 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2749260b-37af-3fd8-bc13-eea7a3eb7527 | -6.84507 | -55.5666 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e14ab2a-7233-380c-ae49-495789b11a22 | -2.89479 | -50.38619 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93125348-4555-3fde-9f1d-8595a48e2792 | -6.64795 | -59.96303 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17d2420f-6dc4-31c1-9fca-8b3cafcb8b8e | -3.55265 | -58.68162 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 187f0bea-99ca-35f1-b4d4-3f533b84b949 | -5.12721 | -55.94779 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| af47c5e3-fc94-3abc-9763-e57391382e44 | -6.7907 | -58.78471 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cb3024c-535e-34f8-a9f1-102c87a83b2f | -6.34209 | -57.88095 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a38e5f5-30f6-3fcb-892e-f2120f9ded9a | -2.91712 | -50.44307 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 08d04102-2aed-3570-9178-2c69b635f24a | -3.40791 | -58.20591 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c90bd3cf-83a1-3a72-8390-954f36c5bcc9 | -6.37528 | -55.25757 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14e58493-3b10-3f9a-b132-0652a8974f97 | -3.40737 | -58.20941 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db0e2bd9-a6d3-3aad-93e2-5e8c667fe08c | -3.18249 | -61.12468 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ef16c9f-6e7e-3736-99d5-09d2c0da3937 | -6.15553 | -59.94399 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fad95513-49d8-3b1c-b1a8-f56e6a26b636 | -4.09718 | -54.43908 | 2026-09-14 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d4c22a8-c846-38ae-8b13-9abd9c451650 | -7.07422 | -63.06407 | 2026-09-14 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 013defe2-6c14-3a04-89fe-d70c4aa06fe1 | -2.69532 | -57.53865 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83e6d8c8-65b6-320f-bde8-0bc645b70bab | -2.92822 | -50.36644 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55e56f04-032d-3821-84b6-b9540ec8e0c0 | -3.41595 | -58.20714 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 773de123-4dc0-3be7-a023-cc5b1056ef35 | -6.6394 | -58.82433 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83868026-b98a-35ab-a240-ceccf5ac8703 | -3.16545 | -58.64206 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c1e402df-8f4e-3262-919c-61fe4a83d72e | -5.72921 | -60.22306 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5ebb209-18a4-367a-adff-72786885a9e0 | -3.35664 | -59.62316 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 02a81484-7676-37d7-8e1d-42f78bc83bed | -7.10166 | -55.62714 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34132db0-dc71-33c4-83e7-bc8e8ec0caf7 | -3.73376 | -61.75822 | 2026-09-14 05:36:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e825edc-914b-3e65-bfd3-d60b5613fd83 | -5.13047 | -55.95936 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b25f2a5-3b11-30ee-92cb-0f12ba9b4dc7 | -6.32655 | -60.02098 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5b8790d-d52e-3513-979b-5f5c48cff729 | -3.64135 | -58.62547 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9204ac55-1ad1-3aba-be12-40b9174eb41a | -6.32636 | -55.17716 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2967c32-7840-3b9d-a4b4-369c04530db3 | -3.87745 | -58.9038 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00836df9-8c21-3645-85a6-4db9d4634399 | -6.7937 | -58.7926 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4173c38d-a585-395e-a715-155e7d8349b1 | -2.611 | -54.7534 | 2026-09-14 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0f483ec5-e625-3d63-8f4b-c9304d25affb | -6.75026 | -58.68934 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27f2d07f-7f8a-3fc6-99e0-3b5241fa8574 | -2.67577 | -57.57135 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ad05971-b723-3924-ae29-c2f15f8008e4 | -6.302 | -59.94582 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 081706a4-d825-3d43-bb51-27e7c9932cd2 | -2.88897 | -50.37932 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e53f631-a89f-3cdf-92bf-00c94417416e | -2.89631 | -50.39768 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README56.md)
