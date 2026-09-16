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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adae9ece-e3ad-3be5-a10d-8e242450a0fc | -3.08215 | -50.56337 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40b24eae-5905-3dca-8c94-19da08337800 | -4.3784 | -55.03248 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3f98aba-aa66-3355-bcd3-bda2bcefbcb3 | -3.08154 | -50.56746 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb59541d-999e-3e0a-9e3c-63081431686c | -4.51753 | -54.97113 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a3e97a9-a1f9-399e-b0f0-19fdcbbde8aa | -4.08768 | -54.4362 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea9432ee-dea8-32c3-9eb4-6a7edd83ccc3 | -2.90785 | -50.42565 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bc1049b-c0ae-36d8-a350-fd216c8f05d6 | -3.01784 | -51.34035 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0bc4d138-c77d-3fb1-9abe-0143ee8c1293 | -5.64496 | -60.22103 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b7cbfbb-c453-3b8e-900f-cba0de4e2eb1 | -4.08714 | -54.43966 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6524ceb7-88e6-31c4-b2e9-a6d0e335a1c0 | -5.36901 | -50.16279 | 2026-09-16 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23411c04-d1ba-3c24-9873-8bc728e8f59f | -3.17095 | -58.64532 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71fe8fed-27db-3faf-859d-d6858ab9ca26 | -6.13294 | -57.71305 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb5930c3-c061-39d5-a02e-a5fdc63f359f | -3.47377 | -54.68536 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91cacbad-f5bf-311d-b65a-41723c559597 | -3.4771 | -54.68589 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b392f97-900c-3e32-9f15-a6c268baaae3 | -2.97132 | -54.15845 | 2026-09-16 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2098880-abfb-3edf-b793-766daced9195 | -4.18141 | -49.40556 | 2026-09-16 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f49163d8-ea6a-31e2-8eea-78d944d64c8d | -7.33855 | -44.48963 | 2026-09-16 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a030e7bc-6c56-3d7c-acb4-256db888bfc4 | -3.18586 | -61.10923 | 2026-09-16 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 270ecaf2-a77f-357c-a759-4284189ee15c | -7.21474 | -46.12774 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8d697b0-b4fe-3e7a-a404-ae2996aee260 | -3.3281 | -59.44843 | 2026-09-16 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 898d8469-8db1-3f7b-85a6-a88394df75bf | -6.78071 | -47.87654 | 2026-09-16 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60f1c786-5bdd-3cc6-aa95-551d5f5a0768 | -5.45946 | -60.2178 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1584adf-ad84-3e2d-80a8-336ff5a47d3e | -7.08617 | -42.09649 | 2026-09-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 78e27f95-8716-3e9c-b8a7-aae0bc98a6c1 | -6.64753 | -59.96321 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1b90ca5-178d-32a0-bcef-a256809a7c7e | -4.3656 | -47.78469 | 2026-09-16 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3b3908ea-2805-357a-822c-1937aceb5c0d | -6.13777 | -57.68338 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a80e19a-151c-3cb5-962a-663f3b0d630c | -4.29794 | -56.26886 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 223cc699-254a-31e1-92f6-5a55ef7e9843 | -7.08573 | -43.56478 | 2026-09-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ef2c5714-4a1d-3a51-b355-fc521cd0797d | -5.90661 | -52.09956 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1fe9b19e-d10d-3741-9a48-9ab8e93984bd | -9.34134 | -44.3908 | 2026-09-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5a26d5f4-f5d5-3b8a-b371-6de3848c582a | -1.28288 | -55.7186 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf82db76-ab49-3ac7-ae4e-83a0497a8e5f | -3.15738 | -49.41251 | 2026-09-16 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f009cdcd-4e87-37e8-88c9-61f986d33e7a | -2.63348 | -54.18693 | 2026-09-16 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7384cc3b-9b37-3740-bbe4-1083a7d08592 | -7.11236 | -55.12851 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a980bc5-0a9a-3978-9871-efdb063a2377 | -6.79118 | -58.78836 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 310eb83e-7c0e-3998-9269-4b1b6d38d434 | -5.89103 | -52.06237 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df342269-250f-323c-b5ad-0435a45c63e4 | -4.9957 | -55.94506 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9e8a531-480e-3e42-b224-5aed840e0630 | -5.75845 | -57.59179 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65f8061b-6867-345b-9c44-ec984e7737e8 | -4.34595 | -46.61526 | 2026-09-16 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1b0726a0-1a17-37b2-9422-ff227d5ae3ab | -9.54374 | -45.41947 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 665e133a-f3ce-38cd-b125-b8774e4c0634 | -2.90299 | -50.43338 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ad3b3b9-2aff-37ca-9cd3-6470d20d0619 | -5.13928 | -47.60097 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 834e514d-2cc9-375d-b16c-a7f49d3ee101 | -6.36533 | -55.8314 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f48dc4d-80a7-3d43-92e0-ebd88556c5d9 | -7.07905 | -45.24027 | 2026-09-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 347b9272-5e00-3c75-8508-b5df02627a3d | -7.08362 | -43.56336 | 2026-09-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca878ca1-72c2-3e2f-b60e-8f107fa9b41b | -6.75021 | -58.80879 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 262f0f45-6d9c-3df1-b587-643162a7aa7e | -6.71472 | -58.80807 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 91fd1bd2-2c33-3d49-8d45-05de8e3494aa | -5.07775 | -56.24529 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84679173-84ef-32dd-b37f-2e5cc9c20c3e | -2.9212 | -50.4107 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b91d9553-d341-3b72-becb-357c1358045f | -3.45459 | -57.98636 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68532a7a-0980-33f5-99c3-886a862a53b0 | -2.60726 | -47.74968 | 2026-09-16 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b19c5fa-0cc3-3718-b772-35ec0ff16996 | -4.40851 | -55.08041 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 332c07b8-1ca1-3ef0-8062-8767927d3386 | -6.36927 | -54.96412 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 536d58b2-f9de-3149-a2b1-6d4227049dea | -6.81164 | -59.17091 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 172a3699-c704-3d40-8e5d-b3ff9e7b9b56 | -6.62903 | -55.1303 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dabbe9d5-55c6-3001-bf94-b52346f41871 | -7.51374 | -47.56454 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 764c524f-ae90-3464-bfec-87ef08aa2d98 | -5.14316 | -47.59889 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02a4d273-bbff-3c0b-ba09-450c36355a96 | -3.44465 | -50.661 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c4f6a29-d7f9-3638-b7be-17dad6394293 | -4.28654 | -54.77381 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4da395dc-6935-37bb-8320-04ea9c0bf5e5 | -5.09987 | -47.622 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 65fb4078-ffdc-3206-a40b-c1b644ec762a | -3.25793 | -50.02182 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5881f4b3-0db4-32c9-bf29-eecd7bfd9722 | -6.15921 | -55.71443 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 872556e7-50f7-3bf7-b4cf-c49c5144763c | -3.58451 | -58.54678 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b64d6bc0-25b4-3b9f-aa47-25e2eafa65e3 | -6.36872 | -54.96759 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84338c91-8353-3a57-bc26-135413b97149 | -6.34429 | -62.69279 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fbc734cd-7b80-3615-bb6b-5153a01ceb0d | -6.15291 | -52.74094 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47abcf47-3b00-3baa-b707-6f5dca0d8eb4 | -4.36126 | -47.78405 | 2026-09-16 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7050707f-6bf4-3187-ae1a-ff877c00470c | -8.7823 | -45.90281 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85636ac7-e2c8-3cd9-a58a-42e3fec700ad | -4.49164 | -55.49605 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a25fb65f-8ce8-35eb-8fd1-bd6fc7da10dc | -3.84564 | -59.33204 | 2026-09-16 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e3dbd75-a979-32d9-bd6b-731d2ca01c5d | -6.78149 | -48.65635 | 2026-09-16 04:57:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 411edc7a-35a1-3b45-aa41-65e0e2d79e2c | -4.46341 | -55.24909 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54070c48-b189-3479-a0ca-41434e35a9af | -2.9416 | -50.49416 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ce77c554-e0aa-3269-a696-85294cbb5e74 | -4.52809 | -54.96914 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79eed41a-b695-3a91-abb0-f516b8bcbaed | -2.91209 | -50.42205 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33feae63-d926-38f6-9fa0-2b8debb0b39a | -6.31494 | -59.95211 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9656b75-4db7-300f-9b52-8d231c299da0 | -8.3321 | -51.31351 | 2026-09-16 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f644f87-4060-3290-973e-62ccdefe3aac | -5.63337 | -51.67842 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c4628ac-0128-3d44-8050-adbd0bab2014 | -9.10476 | -45.72752 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ab8d893-9580-35bc-8e2b-01254b7935f9 | -2.89515 | -50.43645 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fd66c1e-67c4-32b9-ae5d-323aa5383ee3 | -6.3438 | -62.69571 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c63f66de-770a-32f3-a040-290c27fd669f | -6.31657 | -59.96803 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 93dd1c05-f9a3-3040-a5b0-397f5333cbc6 | -4.43367 | -55.78973 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd01fc54-b175-3876-ba5d-04d36453956c | -5.64067 | -60.22032 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e14ba4cb-e66e-3be9-a673-dbd7f6ac7a60 | -2.911 | -50.40489 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33ff6c38-9001-358d-8732-a12f245b4f67 | -8.57324 | -48.5183 | 2026-09-16 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2cbb4d3-d51f-3cf7-9e32-f74d54b6f7e9 | -4.71684 | -48.31283 | 2026-09-16 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84e6dde0-f6f9-38b8-ae8c-1a8b2865e14d | -8.84875 | -44.89241 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8918e73-0a1e-332e-a3c9-104e109b9f6e | -2.58263 | -55.99258 | 2026-09-16 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14c063f3-1846-3e1d-b5fa-0fcf48bfaf4f | -6.35301 | -55.56195 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 55fa5283-1611-3c7b-8642-9f705b9f0a51 | -3.81821 | -55.5777 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 097a39ce-5f0b-3373-897b-65d6c5ffbc33 | -6.02744 | -52.20578 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23ad676c-e174-363d-88bd-5e7993c63acf | -2.90237 | -50.43752 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec8d0295-e8a9-38d8-8e87-54374ec21d25 | -2.89045 | -50.41872 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4807115a-657c-3a1b-9092-b58fd9dcb97e | -6.32689 | -60.00926 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e85bf57-5e7d-33ba-a437-0907e135af6e | -2.26565 | -57.08937 | 2026-09-16 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b44dce3-e7ca-36a8-91fb-49f1e38b73ae | -6.01995 | -52.16229 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63d890cb-14a0-3b20-a6e0-5191373b95da | -4.49501 | -55.49658 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2c83012-18e6-3735-a553-d4260ca465cd | -3.36998 | -61.33496 | 2026-09-16 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbc423c0-d961-33ca-a551-9e656b2f91f1 | -3.69641 | -58.88282 | 2026-09-16 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
