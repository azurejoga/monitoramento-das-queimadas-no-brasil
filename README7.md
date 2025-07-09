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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e3d2114-fa54-3057-8411-3d370313c2cd | -8.5028 | -43.2614 | 2025-07-09 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.8 |
| e9d4c94d-8b45-33b4-838a-2cf2ad7bd03a | -8.5214 | -43.2828 | 2025-07-09 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 191.3 |
| 0de6d8ae-db0a-3c02-84a0-0b5d79689512 | -11.4205 | -45.095 | 2025-07-09 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| ebb83737-033e-3779-ae1c-ee871a4fe596 | -11.4397 | -45.0923 | 2025-07-09 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 748282d0-ea9e-3696-8032-3afb347274b6 | -11.4393 | -45.1154 | 2025-07-09 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 6aa1a359-d441-34cb-9970-dc81cd43b58e | -10.5776 | -49.1316 | 2025-07-09 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 4961ddfd-e90d-371b-862a-112a3ff88cbb | -5.91727 | -37.39485 | 2025-07-09 03:53:00 | NOAA-21 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af53e361-953f-30fb-ae7a-1c7eb3f78412 | -4.6041 | -38.53152 | 2025-07-09 03:53:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1fa4bce0-3bd7-3550-9f5a-3af9e6969f90 | -5.23465 | -45.21559 | 2025-07-09 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d433938-4f9f-3e61-a649-988a9c3ebacc | -5.23083 | -45.21017 | 2025-07-09 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86f5017a-fc3f-394b-a9b3-6391c7d6228b | -4.77977 | -45.34784 | 2025-07-09 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfa9a688-5bcb-38c3-99dd-186136b18b7f | -3.6623 | -41.12936 | 2025-07-09 03:53:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 32596869-88fd-361f-980f-6688ce1a945e | -5.23491 | -45.21347 | 2025-07-09 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0d6987a-e364-354c-8ea4-66467599f6fb | -5.23006 | -45.21483 | 2025-07-09 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ad79e48-e71e-39f0-bedc-04bc351ff269 | -4.78211 | -45.35065 | 2025-07-09 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e13a009a-0f0b-3c16-93a9-eb4b7799bb01 | -5.58128 | -43.58206 | 2025-07-09 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa95a104-e6e0-32df-9d4f-6e805723519b | -4.6816 | -43.25945 | 2025-07-09 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c87b09c-fb2d-37a5-a2d1-90506ed94f1e | -4.97039 | -37.84181 | 2025-07-09 03:53:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ffc10d41-740b-31ae-bf27-4de965bdd8d4 | -4.68276 | -43.25231 | 2025-07-09 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14c6faec-423f-315f-a977-e9f0cc02c401 | -5.0718 | -37.71611 | 2025-07-09 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a81a5220-1e7f-3e97-9f12-1896279aa3e0 | -3.66298 | -41.12519 | 2025-07-09 03:53:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13c12684-a002-371e-8d67-6d837e7fb292 | -9.22737 | -48.59223 | 2025-07-09 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8c2d2c31-3a43-3e50-b774-e1d099c8a30b | -12.982 | -44.86694 | 2025-07-09 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13ff147e-a108-3a80-b9b8-c935cf04843d | -8.395 | -42.93769 | 2025-07-09 03:55:00 | NOAA-21 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 21185d94-4419-3e39-91e7-218e4474a1ee | -11.43678 | -45.10732 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8f2f0cb5-e0f6-3529-a812-88362dc26a46 | -11.47255 | -47.93163 | 2025-07-09 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b597185a-2203-3566-991b-204767462398 | -8.23168 | -46.95369 | 2025-07-09 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9bb78ae8-2d2a-3035-be62-4ed68fc0af91 | -8.51014 | -43.27687 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 06bdf8e1-fb09-34e3-a8fb-fbcb00b62651 | -8.37935 | -43.9473 | 2025-07-09 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39c8d21e-b975-34c3-a29a-02bdff7967cd | -13.31877 | -42.28196 | 2025-07-09 03:55:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7a40442e-3fcf-3fc0-ae7f-5cccd35041b3 | -8.27947 | -42.27647 | 2025-07-09 03:55:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 12be4ba9-3180-337b-a467-23bafeaf0e5d | -6.57169 | -48.24319 | 2025-07-09 03:55:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04aa9fe1-cff3-3683-b1e1-8ab5f6e336a3 | -6.36832 | -43.64836 | 2025-07-09 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cee52ff-db4a-3b6b-a13e-53780a8d97b6 | -8.76293 | -47.67224 | 2025-07-09 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50adef1e-7b73-3e9e-b603-e9ccbd6b37e5 | -6.57085 | -48.24727 | 2025-07-09 03:55:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb1555bb-4dbb-3764-9c86-f85d881e01ff | -7.23778 | -43.07895 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b3897d98-a2a0-3b8c-80d7-b716ea2acad1 | -6.72974 | -44.33155 | 2025-07-09 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96314d84-dff4-369c-9639-d5f2a746ca4c | -11.88931 | -44.93533 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc6c053d-6dab-30d9-887d-dc1b14e6b7ae | -9.29014 | -44.84242 | 2025-07-09 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 12f0efbf-e335-31e8-821f-997597b4a77f | -7.08441 | -44.3154 | 2025-07-09 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fc58230-df02-33ec-987d-c95df120e19f | -5.96017 | -44.18001 | 2025-07-09 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e25530e8-bcfb-33dc-aad2-07d6cf3c7be5 | -10.34689 | -49.91552 | 2025-07-09 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 537a4c7f-4c2d-3ea9-97b8-951d3367626b | -6.54818 | -43.62369 | 2025-07-09 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ac90d51c-237e-3b5c-ae2a-035f8d9fe717 | -6.83827 | -43.35744 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a364c18-aa7d-3850-a786-4759cdc10f1f | -11.47751 | -47.93251 | 2025-07-09 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 600602b4-1cf7-3957-8e88-fe4c9e56f1af | -9.28596 | -44.8417 | 2025-07-09 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b73bb71-14a4-3e60-b66f-a7c1d7cb134c | -7.23085 | -43.07284 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b21e5490-aede-3ab5-9ffd-da6fafc61f7b | -7.66519 | -44.37196 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 823b0bf0-3742-34d8-bcdd-33af12dfe3a6 | -8.23087 | -44.93087 | 2025-07-09 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 460d612e-c9d8-3705-93d4-8a3aba912214 | -8.50475 | -43.28572 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 5333e48d-55cb-3dcb-b793-c4d5adf008d9 | -10.74684 | -40.82681 | 2025-07-09 03:55:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 317e5bbc-88da-39c9-963e-ad926930c523 | -7.03345 | -43.49244 | 2025-07-09 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31424979-e4b9-3fd3-83ef-7b9f4de09038 | -12.9802 | -44.87727 | 2025-07-09 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28645ce1-4c17-3aaa-a107-c4cda7c40b26 | -10.57899 | -49.12809 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| baa95803-99fd-3f26-be9f-b46ff7223451 | -11.4424 | -45.12385 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a174e67b-d8e1-3cfa-b00b-70996319a0b9 | -8.22587 | -44.93422 | 2025-07-09 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b0858c9-187d-3d8c-87be-309143fa2951 | -5.95949 | -44.18398 | 2025-07-09 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa3e5554-80cd-3d7a-83f4-17bfe494b1ef | -11.43202 | -45.11034 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| c9139612-7713-3377-9c2b-8bdbd9378bf8 | -7.23307 | -43.07065 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 802ce61b-968f-332e-8750-e6db4da46077 | -8.51662 | -43.29997 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 048f448a-efea-3ea1-82ad-80b373c28484 | -7.23224 | -43.07551 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d4961475-0ccb-3794-a2ff-0afd9529e453 | -7.23471 | -43.07346 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 61797b46-ab99-350f-a42f-d89b96f777d1 | -7.22699 | -43.07221 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e768ed6b-51dc-3b6c-8750-c4e38950c001 | -7.03242 | -43.32692 | 2025-07-09 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f7adb46a-f943-3846-bc38-e58fb1188a40 | -11.50972 | -48.95323 | 2025-07-09 03:55:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b948b7b-ae5d-3371-8be8-abf30380c39e | -11.50989 | -48.95959 | 2025-07-09 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02b38bdd-bbce-32f2-af2e-0b2944fceb38 | -6.63556 | -43.19415 | 2025-07-09 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 84d87b6f-ebce-3ad7-9cbc-f9aacc6c2917 | -7.2361 | -43.07613 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 954634c1-1561-3d2f-a95c-de1df2443e37 | -7.66226 | -44.36382 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 469dac18-b8b0-387c-bfe3-8202ef586750 | -13.32222 | -42.28255 | 2025-07-09 03:55:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f10a3a6b-d2cf-36e5-a4e8-5f3772d2753f | -5.96439 | -44.18073 | 2025-07-09 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15c02bfb-c9ef-3fe2-b178-9ede8326e59b | -11.42857 | -45.10584 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 75992ca8-0df5-3086-a59d-33f8e22fc74a | -13.75159 | -39.03373 | 2025-07-09 03:55:00 | NOAA-21 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 08d0325f-c11b-355d-b42b-9accbb815490 | -10.57351 | -49.1273 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b1c33860-43d4-30e0-ba19-df69bbbc084e | -11.44304 | -45.12008 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9ed9fe49-fef7-32f0-b448-48932ac3d3f4 | -8.23016 | -44.93493 | 2025-07-09 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ece1320-067b-37c8-908a-98f8cf0930bf | -8.49787 | -43.27966 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c7eaf376-8e90-3e9d-ab4e-55c4821f1474 | -11.42381 | -45.10887 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c8e8c37c-7eff-31a7-85ec-f402632b52af | -6.57148 | -48.24359 | 2025-07-09 03:55:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0664cc4c-727e-3137-a13a-f91260c4d25b | -6.5488 | -43.61998 | 2025-07-09 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7d82313a-ff54-3748-b670-776ab2d82ad8 | -8.54645 | -49.94992 | 2025-07-09 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a091538-321e-30fb-a4a9-9e685fba3673 | -9.28325 | -40.52249 | 2025-07-09 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b464f0f3-e8f5-30a6-b5fd-2afe6e3f2339 | -7.22921 | -43.07003 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0cb3595c-81f8-3a3b-8977-07db171970b4 | -8.50702 | -43.29595 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| e257e4fc-c7a4-3b91-887a-af2514d7f294 | -7.08202 | -43.07592 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e0cd6fb7-8978-309e-9420-f26b3451c0fa | -10.58377 | -49.13268 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10795dcd-1455-3a9c-9662-2c2b8fc9c7bd | -8.51441 | -43.28978 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| d497739e-77bc-3b67-9b03-e6856b2ef412 | -7.24159 | -43.06711 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 0c4c967a-7e8c-31bf-9f6b-99b6b43290e2 | -7.0907 | -43.45868 | 2025-07-09 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 63ebaed3-ec30-3fb7-b1df-14b8a90cd3f1 | -10.18641 | -51.1502 | 2025-07-09 03:55:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89969488-f726-33ae-a182-d65fc7da00be | -12.05849 | -43.51153 | 2025-07-09 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d880f69f-33eb-316d-b3f4-4bb1d222f37f | -7.08587 | -43.46317 | 2025-07-09 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aade0835-925e-3d39-b713-009b977ba0f9 | -9.47824 | -48.67667 | 2025-07-09 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b85fd937-8ab1-3a00-8deb-008289874873 | -8.65165 | -48.49707 | 2025-07-09 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccfead36-e506-3832-9f1f-7e8811f2c0b8 | -7.2355 | -43.06863 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 2e85180c-3008-3b98-aecf-e784464d1e86 | -5.58644 | -52.08392 | 2025-07-09 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66489f8a-41a3-3ef3-a345-f0829a911434 | -6.85947 | -42.79743 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b35fd6b1-c1a3-3e17-a391-af7808366be9 | -11.4532 | -45.11026 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5277a7a1-50c2-3ea2-b36a-c38e362e2c40 | -8.27583 | -42.27589 | 2025-07-09 03:55:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2356423b-6dce-3a53-aa85-b9f2f5053500 | -11.6791 | -43.78064 | 2025-07-09 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README8.md)
