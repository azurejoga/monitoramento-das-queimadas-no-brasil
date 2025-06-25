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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6373f34-c617-313c-962e-eb5aa0a132c0 | -5.9229 | -43.4778 | 2025-06-25 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cd0e0e60-0f94-3880-8c62-61cd382cc108 | -4.52832 | -48.0094 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10cd9f74-1814-3797-995c-cf3efd470334 | -9.56969 | -49.10921 | 2025-06-25 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8b8f1f66-70aa-3ac7-aeb8-b729a94826cd | -7.43867 | -48.09949 | 2025-06-25 04:57:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 905f4239-7e32-3c60-8b25-f834b227efee | -8.34173 | -48.52525 | 2025-06-25 04:57:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0baaccd-a22d-346f-b125-e6f2dfb49980 | -6.2934 | -44.23517 | 2025-06-25 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4517994a-bd8c-34b2-8e06-8c8a40e948c2 | -9.51061 | -56.10537 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b8679b57-eb93-3807-be2d-d6ff1d0e5f96 | -3.61883 | -47.53151 | 2025-06-25 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dfcb4c96-f000-3716-a39e-0d72007a08b4 | -4.53739 | -48.00696 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3ffafa0d-7eed-3756-9bd1-50d5d108d619 | -8.05855 | -43.10567 | 2025-06-25 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ca97b460-4dc2-39fb-9ced-f144b151571e | -4.54531 | -48.01249 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 32fc086d-f555-3a9c-beab-ce9194f6c8da | -4.52896 | -48.01118 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b41f2d5-b6fd-39e0-bc06-843edd29b4e9 | -9.9205 | -52.43565 | 2025-06-25 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6d57a63-302c-36c2-b8bd-5096f6bf005e | -9.92873 | -52.42873 | 2025-06-25 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc52a432-3974-3338-8abc-df7440f4b5e6 | -9.81554 | -48.38616 | 2025-06-25 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bad95b6-4963-363a-af33-fc489ab7ce93 | -10.45467 | -47.95028 | 2025-06-25 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d37a4877-20d1-3488-92eb-a085233a709e | -4.53804 | -48.00874 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| db416421-eb0d-31dc-a6fa-ba3ede0b931d | -8.53639 | -46.3288 | 2025-06-25 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f53e114-6c2b-339f-b52b-161b8e20d1fb | -9.50175 | -56.09665 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf776934-e0d3-30a3-9201-c4956d0f6c92 | -7.02434 | -44.5718 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11268508-2b71-3c0d-bfa1-2f6d4d6c0c3a | -7.00975 | -44.55295 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 200590b8-72a0-329c-85fe-090593e8f9d8 | -7.88374 | -47.88234 | 2025-06-25 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9598d4ef-7131-36b1-b786-6c5d00831893 | -6.95548 | -42.80187 | 2025-06-25 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e5a0806c-09c2-3180-9857-0a7492b80ac8 | -4.53315 | -48.00615 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 531dc312-186c-303a-aa6d-52ad81bec565 | -9.50866 | -45.44112 | 2025-06-25 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0114b3f6-498d-302e-8a3e-156727ea3a3a | -5.35781 | -45.11861 | 2025-06-25 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbebac8f-a61c-3191-9faf-3ab8a9f958f2 | -2.90864 | -54.48749 | 2025-06-25 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e22fc678-2c88-32ad-8c43-340c5ccf3628 | -10.13783 | -52.13867 | 2025-06-25 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 387ac247-01de-339a-9599-9bec62f5d6a2 | -6.60461 | -44.26003 | 2025-06-25 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5097c33f-282a-3cda-ba22-59c9e27e2206 | -6.18022 | -48.06512 | 2025-06-25 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 32af22be-564e-3e36-9733-08e4e8d47275 | -10.51886 | -47.58212 | 2025-06-25 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 391d488b-18ea-3052-b1db-c2611654b2cf | -7.02039 | -44.55884 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 944f618c-8bcb-3596-89fe-2867985c2e6a | -4.52957 | -48.00714 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdc45e75-54c2-3ba5-a97b-0f4138118547 | -6.95871 | -42.80774 | 2025-06-25 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4ec8f88e-859a-3bd9-87c2-6af8d7e5ee84 | -9.92814 | -52.43272 | 2025-06-25 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d850303-e949-350d-8466-7018eabe79d3 | -3.61757 | -47.53982 | 2025-06-25 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41b6d339-d87f-3fb0-870b-f975f4976262 | -8.98321 | -49.86795 | 2025-06-25 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56e39eb5-55a5-3d80-ae7d-a7223ee2d05b | -7.0148 | -44.55794 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 409a148e-e1b9-30d0-a962-3a6a15e854a9 | -9.92521 | -52.42819 | 2025-06-25 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26d79705-35ae-36b8-9e5c-00108f61c5c7 | -9.56915 | -49.11324 | 2025-06-25 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 444fcc70-19b3-38f5-bef9-6e941be296ab | -9.81491 | -48.39082 | 2025-06-25 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d3282bd3-f780-3082-924a-c2759c942717 | -5.92231 | -43.48203 | 2025-06-25 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 53aa80cb-ef66-35a3-ad2b-4fed0c846f9f | -8.15348 | -46.82244 | 2025-06-25 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1719a2a7-6fa3-3024-9bab-9ac9fcb4288c | -10.51486 | -47.57603 | 2025-06-25 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27953aae-43aa-358e-8ad2-9b034756f61b | -4.53381 | -48.00795 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5935a79e-d71f-3f9d-a835-90826f692db9 | -8.86993 | -47.27603 | 2025-06-25 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4931a6d-6ad8-333d-a154-088bbe6fb4b4 | -7.94616 | -63.00971 | 2025-06-25 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f2a0d8a-3199-3235-aad1-7e7d612491ca | -9.57341 | -49.11388 | 2025-06-25 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 950b569c-b64e-3a81-8fe0-8d942dd14470 | -5.10965 | -43.1476 | 2025-06-25 04:57:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6f9295d-af31-3436-b8ab-4c91684da61e | -8.66878 | -51.46339 | 2025-06-25 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1d5e24d-f0ed-3eb4-9b4f-12eddd902730 | -6.29915 | -44.23537 | 2025-06-25 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6798f827-9218-3eee-91fb-e39ed0a499ec | -9.50727 | -56.10484 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5e8cb36-1b8e-35c8-89d3-59dfb943fe98 | -10.22613 | -50.56585 | 2025-06-25 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1946bfa-3f30-3755-ab72-0c242422bf86 | -8.5313 | -46.32811 | 2025-06-25 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d0b478b-8929-3a67-b0da-b0143824521c | -7.0193 | -44.56688 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 37b4d617-adbd-34a4-bc34-ea13817428c8 | -8.98723 | -49.86854 | 2025-06-25 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50ca16bd-758b-3805-bfab-48fe92f60f61 | -7.00426 | -44.55125 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64a7d3bf-c62c-3a3c-a39a-d3a259d4a118 | -3.72153 | -53.7529 | 2025-06-25 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aff9352a-5268-3f20-86e1-44f7a770cf00 | -11.10926 | -44.52347 | 2025-06-25 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd818172-d73d-3e3b-8bfa-060480cd7c70 | -7.43847 | -45.54077 | 2025-06-25 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cf0a699-4bc6-379e-b5f6-6188ce58affc | -10.51952 | -47.57692 | 2025-06-25 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35f2c80b-3bfd-3e98-88a8-0367716c6dab | -7.71055 | -47.38212 | 2025-06-25 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dfec4bb-d4c0-3a4d-b1d4-6c38e2dd992e | -5.36305 | -45.11958 | 2025-06-25 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5caaf5dd-9330-306c-9429-7300bde7e3a7 | -9.51413 | -45.44199 | 2025-06-25 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c89389db-c345-31b0-8850-6bd75897c24a | -6.29863 | -44.23918 | 2025-06-25 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5ec15613-299e-3b3c-a5fb-4465c7dfebf8 | -9.50899 | -56.09415 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b96bf2d2-7146-3ecc-a00d-2712f78ee5e8 | -9.26503 | -47.64485 | 2025-06-25 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d222107d-eca7-3a99-94c4-0a57ee554509 | -8.47958 | -50.27616 | 2025-06-25 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7feda0a8-716f-3624-8854-62859a32a37c | -7.03053 | -44.56832 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e572a569-94dd-3cd7-84a4-f5a690548ad5 | -4.53319 | -48.01199 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 70f03e43-86ad-3984-b2f5-48c8c7de2497 | -9.50508 | -56.09718 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1cc03b0-79bc-38fe-b39e-4dca54b1fc1d | -9.9211 | -52.43165 | 2025-06-25 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9afbcd5b-959b-375d-84aa-d25750114e3e | -6.96105 | -42.80796 | 2025-06-25 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 25d707f8-8d0e-32ef-a6b0-27bfd588605a | -10.44467 | -47.95375 | 2025-06-25 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 22ac9891-ba10-38ed-8b75-546764eccc9e | -6.34811 | -43.7869 | 2025-06-25 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a46d2ff6-7aec-3882-ba4f-ee9c0ee8beb1 | -6.10012 | -49.61929 | 2025-06-25 04:57:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 998e25ef-22fb-3bd3-ae1f-6e0207f4c151 | -9.57396 | -49.10985 | 2025-06-25 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e7bcadc-616e-3613-b732-27bf61a114cd | -4.53681 | -48.01103 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 84d79ef6-d2eb-3983-a7bc-a49f05ff9aff | -6.92328 | -46.41129 | 2025-06-25 04:57:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b363116-0067-3b3a-917e-e5a4847fbe33 | -9.92402 | -52.43618 | 2025-06-25 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a81f683e-5808-3690-b7f6-8b574f4000ce | -4.53743 | -48.01279 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 68490e05-91a6-3bb9-922b-84b6707ffd53 | -7.02489 | -44.56782 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5291e269-8e7d-3265-b85f-66a14dbe4574 | -8.47887 | -50.28109 | 2025-06-25 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0a40f485-4a6d-338f-91f7-81165fd3d0ba | -4.53797 | -48.00292 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87de49fd-d34d-3fe7-b028-7f4820b6cdb6 | -6.95935 | -42.80268 | 2025-06-25 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e103d9b6-e143-3825-9ec6-2eb6596dd2eb | -9.50451 | -56.10074 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06351729-ac63-3ed4-9cae-c9143a8b23c0 | -8.67178 | -51.46819 | 2025-06-25 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 207d71e1-19f6-3e33-80fe-fc94c516fcd2 | -9.50784 | -56.10128 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6806c20c-dfb8-36ad-b047-78a7bf4fae0d | -10.27936 | -48.20835 | 2025-06-25 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7118363d-f1c0-3c9e-b707-9dcb241edf10 | -7.01532 | -44.55405 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 851f58e9-5289-392c-b575-127f76941d54 | -5.92115 | -43.47609 | 2025-06-25 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf21298a-c61a-3e05-8efb-f4200885098e | -7.43892 | -45.53749 | 2025-06-25 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7dfe563-0943-3a9e-8365-bdb2a9a066b3 | -8.14403 | -50.98826 | 2025-06-25 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 828e1d76-7cdb-34f6-b3fa-bf733a83e8fd | -4.54106 | -48.01178 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b6057d09-829f-3479-aead-6bf40c23bde0 | -10.44533 | -47.94886 | 2025-06-25 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 9ea8c47e-74e6-3fcb-87bc-e592a5914971 | -3.7282 | -53.77501 | 2025-06-25 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b286d39b-0a7f-3151-bf4c-a637689b6e72 | -4.54589 | -48.00845 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d70188f1-6133-354a-8063-ccb6a524be68 | -8.58238 | -51.54597 | 2025-06-25 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ce1cb57-bcf6-36b6-bc9c-7b3fdee2646a | -3.61384 | -47.53511 | 2025-06-25 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e68ef8fb-9a83-3cfb-b117-c01c65405468 | -10.56276 | -46.66964 | 2025-06-25 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README14.md)
