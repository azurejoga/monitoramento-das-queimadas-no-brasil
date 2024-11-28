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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bfe4965-d7db-376d-a358-27a4c783a0e0 | -1.66355 | -52.71926 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d08f232a-f3b0-3947-ba27-08d4e63c46f8 | -6.57027 | -46.56202 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de4e4d23-df07-3119-bb0f-3ccdc164ee47 | -2.0996 | -50.34686 | 2024-11-28 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b417fdc-878b-35dc-a9fa-153abcf2c0e4 | -4.09063 | -54.76422 | 2024-11-28 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1946dc8f-2b14-36ae-8889-639795bdb334 | 0.8274 | -50.25845 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8480ce61-90e7-3ac7-8397-df1e3a4a0dbf | -1.2317 | -51.79579 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0a8e189-7a7e-36e7-b913-d76656667275 | -2.06743 | -49.52736 | 2024-11-28 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6eb99e0-fa49-3da6-acce-4ad9dbb1042b | -1.69411 | -52.61967 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d0b8c8d-7f73-3936-8114-26541cc74839 | -1.89185 | -45.46439 | 2024-11-28 04:23:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c04534d-a97b-3f7f-9e9d-8e01d47e3eea | -1.31218 | -51.73705 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d545751-993b-3edb-b517-7f97cd94be19 | -1.63139 | -52.73548 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62e17557-b4f9-3c97-82e2-fbe4c60a349e | -1.32737 | -51.93291 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f73523c8-6ce8-312f-9660-b3efe2a0b145 | -6.58182 | -47.91184 | 2024-11-28 04:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9eb3fa5-3319-3a5f-b147-4ced17d445e6 | -5.92717 | -43.78449 | 2024-11-28 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d950a5fc-af65-3504-b843-be9119487fda | -2.68663 | -46.15562 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d4c395f-8a10-320c-9a15-deb09d0f3a78 | -1.0474 | -51.74208 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 275bcb44-b8a9-337f-a35c-2a2e6df0c572 | 0.94744 | -50.73211 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b208f2d-11c6-3955-94a4-3e9296e8161d | -2.53655 | -47.32795 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aad3bec5-c0a4-3fc7-9ec5-c150c8be1482 | -1.13752 | -48.35719 | 2024-11-28 04:23:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44cbfdb2-9e51-3258-8fb2-b635660d5412 | -2.51151 | -45.19553 | 2024-11-28 04:23:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6eb6bbc1-e527-3c90-ad5a-67c463b3b5cb | -1.29037 | -51.72894 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf1ab74e-51de-3c9f-9012-f8f89335654c | -2.55924 | -46.42575 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8f519b3-7a6e-3883-a417-f4f7954092fb | -1.10094 | -53.39243 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18923889-cbf4-3e25-979d-95e5a3a3a854 | -1.67068 | -52.73656 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 63bc5c53-bf2d-3202-9a96-ddd8fdd09db2 | 1.45416 | -50.66109 | 2024-11-28 04:23:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6aaa3d2-47af-3cf5-b128-7a36badecaf4 | -1.43077 | -52.67172 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d42b8c1c-d557-3fae-8927-6b041592daf5 | -1.08992 | -48.21193 | 2024-11-28 04:23:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4a9f925b-9319-368b-9afb-499f05eda2be | -2.69349 | -46.28535 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a1863f0-6805-31f8-8b20-b4fc65786453 | -2.26632 | -46.36176 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1a804c4-0a64-3c78-9b63-75e15e1b12f2 | -1.98984 | -46.37316 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8022338-aa1d-31b7-a478-0831a5509503 | -2.18971 | -46.63731 | 2024-11-28 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bb1a47b-7a5b-3927-b154-bd76b6f21b6b | -1.67948 | -52.46458 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48b2c640-1733-3e09-b881-50ca658c003d | -2.70943 | -46.2056 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0104506e-2103-3ad5-99bf-1bfc7b21cb33 | -1.08383 | -54.04052 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 476e486a-d911-3e09-a1ae-e94e281f2282 | -1.08913 | -54.04143 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cdf2d33-5ba9-35b1-8d5f-0afdcc78367e | -1.6786 | -52.50057 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9998b3e0-2977-34c5-94f0-02fc2337c75d | -1.56303 | -52.01548 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a902ce9b-8bfe-3f76-8fc3-26e519915dee | -5.97778 | -45.35881 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a815018a-2ea2-3fc3-b9ca-87603a6314a4 | -2.31386 | -48.14854 | 2024-11-28 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3afe7a6b-3a93-33d7-a113-5ac8b800791e | -6.36163 | -47.06441 | 2024-11-28 04:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 161d41f1-6662-340a-8f37-b2c7aa36ea06 | -2.4742 | -47.03934 | 2024-11-28 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c932593d-72e2-3bf7-8b4e-06173597d370 | -1.57725 | -52.01556 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 750ed6f0-47c8-3cc9-a8b4-d1fe3e11c653 | -1.083 | -53.63931 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfc2dea2-5b90-3ab8-81aa-bf4e11c7200a | -6.10251 | -43.96622 | 2024-11-28 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c786573c-d1c0-3b48-9584-7ccacfa8e0bc | -2.44641 | -46.27868 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0540b67-87f2-3a34-9f74-e850d037ad63 | -6.60161 | -39.20087 | 2024-11-28 04:23:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bbccdf3e-5054-34e5-93a4-1058fbf98e0b | -5.97168 | -45.35426 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2be119c8-813c-3180-9e4b-4c94a66dcb7b | -1.10417 | -53.40492 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b77aef36-00c3-34a9-a6d1-3fbcf5efe0be | -0.99374 | -51.72881 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff95248c-6244-3089-b403-c2c86533b29f | -6.48631 | -47.49728 | 2024-11-28 04:23:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6dbf6d3-b0c6-3644-b5d3-0ac5af2bd301 | -1.35956 | -51.96694 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ac921e74-242f-30af-9dc9-ea1314b18101 | -1.62402 | -52.3763 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae7c22f4-afc2-3ebe-8504-d0de4f892333 | -8.54613 | -47.77159 | 2024-11-28 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb516cb9-3ed3-35c7-932d-3a4176f17784 | -1.71969 | -52.49358 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55cd6a17-a88a-3466-ada6-00b3baa49b15 | -2.72012 | -46.24299 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44fbd860-4dae-3672-8304-2ac107a59e72 | -1.12264 | -48.33317 | 2024-11-28 04:23:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21704c2f-e4d9-3990-8c5e-4d19992e0519 | -8.12689 | -47.98711 | 2024-11-28 04:23:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e730179c-6e76-35a8-af13-2dfbc6775556 | -6.08946 | -41.94083 | 2024-11-28 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c7645aee-1cc7-35ae-8549-81ff2c69d6cc | -2.53251 | -47.33118 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01be25b3-c654-3cd7-822d-c0cb2d3155fa | -2.54417 | -46.39095 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35a2fbf8-f71c-3d03-9509-90a9ca92fbeb | -1.66291 | -52.47735 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 80aab66c-7f11-3fa1-a19d-f637147bda17 | -1.58821 | -52.09208 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74dfc1c0-aa6e-31c0-b0ae-5eef7e913402 | -1.81947 | -45.92338 | 2024-11-28 04:23:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 493c62e5-594f-3c73-9733-ab7a7af470e9 | -5.45265 | -48.94559 | 2024-11-28 04:23:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb38cce8-5c50-365c-a704-e358ad0e3e62 | -5.97391 | -45.36177 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fe215ce5-aa4e-36a1-a4e5-a2bd05f65ea0 | -2.70446 | -46.21553 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da978f54-7f9b-366b-9278-4a8554c20b9c | -1.15708 | -53.68275 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0204443-7499-311f-b253-4bdf6d7958a9 | -6.37399 | -45.69153 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 117bc19f-7a30-321f-8977-b34d0a4ec859 | -1.25877 | -51.59673 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48b9420e-29ef-394d-bb62-c0f507b90481 | -0.5884 | -51.70634 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3727a247-a2fa-3e6c-8093-11e7c30b794b | -1.62651 | -52.37426 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57e57736-1bdc-3572-95ff-8d3e78d61d43 | -6.64519 | -46.53837 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26a4c41c-5f13-32ea-92b4-6591a7899c86 | -5.69605 | -43.25654 | 2024-11-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32f9438e-cc83-324d-8f90-120ddb71f6d7 | 0.98538 | -50.13213 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 25ad425d-5877-3bc1-889d-31d41ab4607f | -2.59636 | -46.25219 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dcd698d-c7fe-3673-baa6-4b703bff35ad | -2.54415 | -46.36937 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49bf8837-9145-3973-8e8e-6e29d04b4365 | -1.63622 | -52.46268 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 324d97ea-527c-3698-a90d-568dbb17d535 | -1.74366 | -46.20838 | 2024-11-28 04:23:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93a3846a-8a0b-347e-aa04-96703ef3d2af | -7.82785 | -48.18585 | 2024-11-28 04:23:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52326388-b88b-3650-838c-b1ffceb16e51 | -1.97346 | -48.68209 | 2024-11-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed4362c8-f280-3d42-aec8-df9252a5a2f8 | -1.51978 | -46.1232 | 2024-11-28 04:23:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39642d92-ed72-3efe-8846-c97b9ed4f98c | -1.79226 | -47.26783 | 2024-11-28 04:23:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb224a5c-9ac8-32e1-9a58-c48623831c86 | -2.27639 | -49.14856 | 2024-11-28 04:23:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1eacdb6-4ba7-39d8-8f50-3cebff058844 | -8.85383 | -39.88146 | 2024-11-28 04:23:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc6d1f57-eb8e-33e9-8ce4-ecd1258fad43 | -0.35747 | -49.95528 | 2024-11-28 04:23:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d14e378-6c24-3fa6-8d60-780d69f678be | 0.98698 | -50.25483 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2ed54c6-2b89-37b5-b107-f2fbe34f66bc | 0.69977 | -51.44915 | 2024-11-28 04:23:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9b5333bb-f7e2-3d47-9612-d37fe6e7e02f | -1.6627 | -52.72073 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b58500a1-0846-30b2-b2b9-38d798381571 | 1.79155 | -50.42521 | 2024-11-28 04:23:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 564d447a-d658-33dc-a178-ee761cf0760f | -1.6256 | -52.00617 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc7dcfeb-7f67-3be1-b882-9911dac35fe2 | -2.69016 | -46.28483 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c290819-c84f-3b36-be8f-fb69656d4d5b | -2.53805 | -46.38638 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dd16340-7a1f-355f-827c-ee53f2034aed | -1.40948 | -52.62024 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84d29789-0640-31e7-9526-cc2493899956 | -2.55088 | -46.41359 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a56a202e-531e-3b9c-bbda-751a8859db1d | -6.37014 | -45.69448 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 934bb726-9958-3550-8ee2-e6b94932b583 | -1.70196 | -52.63149 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b623ed52-e362-3e28-8d22-915e1351dec5 | -1.35 | -54.63646 | 2024-11-28 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d87327fd-e199-371b-bd3c-9f0c40b26b2a | -1.67484 | -52.43306 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bf6deb4-f17e-36e0-93e6-61b15c5ba8c4 | -2.15933 | -48.71302 | 2024-11-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17fc46be-65dd-31b9-9177-e484c3bbfac1 | -8.47797 | -47.81171 | 2024-11-28 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README45.md)
