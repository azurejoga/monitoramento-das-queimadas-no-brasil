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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f92fcb88-d047-39db-aa87-0ded47b6207f | -11.68155 | -54.44477 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5319347b-1a12-3d48-9d3b-9f75282f290a | -9.25735 | -46.18922 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ff9315c-00f8-336a-833c-8038a1768be8 | -11.08717 | -48.2965 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e01ea992-90f0-377b-a1dd-e915116ac89d | -11.88943 | -47.65441 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa6e1ef7-9fa5-35ed-a66d-202b35f2a6c8 | -10.45027 | -51.23983 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68d0c232-b1be-3389-9816-6f0697ee23d1 | -5.74191 | -57.57971 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36d67ac2-1cea-3b57-9df6-ab0f5294cc0f | -13.94618 | -47.84386 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c0170b3-feb4-3e71-ba30-d1f0f02d52c6 | -7.41879 | -44.70474 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56190ab4-9f8a-310e-9f93-ff49986c9adb | -10.9239 | -53.97073 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2323c335-6112-33f5-a1dc-7aaea2c918f6 | -11.39093 | -51.38604 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db837c90-1bfe-39b4-86e8-25fe4698cbba | -7.54168 | -48.68593 | 2026-09-20 04:40:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3fe480b-d7fd-3529-b85a-ccd61442bd11 | -9.26159 | -45.94582 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04b155bd-748b-3888-bf97-bb6991185cb1 | -12.53712 | -50.03881 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 72ada563-6f60-316a-abbc-fe1169a37e0a | -9.04504 | -48.71712 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d5d17fc-b99a-3951-95bb-a161072e259b | -9.1765 | -51.51605 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b00873f0-bdaf-3a4a-b0bf-bc0459fc461d | -7.56206 | -45.69032 | 2026-09-20 04:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c81b457-f549-3a32-8616-0534400da80f | -8.6381 | -47.61362 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99c36d1c-f731-3e4a-b447-205b1f61f66d | -7.05386 | -46.22493 | 2026-09-20 04:40:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9704294-e26b-3433-aaaa-3520c48d2619 | -7.55131 | -45.38224 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cbda0497-d6f5-32d5-a383-1c5c8a26c330 | -12.74856 | -46.19921 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02afdb4e-e790-34c1-b9c6-9ef2a029682c | -7.87189 | -44.82375 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb59b18a-1155-3310-8289-c0b7e523e4a5 | -8.42896 | -45.86032 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c404855-aaaf-3b1e-be57-3995ad077d05 | -9.2832 | -48.19802 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c75d8ad9-f920-36cb-bb85-7d6bdc59c911 | -6.77463 | -48.65983 | 2026-09-20 04:40:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4f04ff0-7af0-3940-8b5f-4e00b9429c79 | -11.86996 | -49.00042 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 001ae9dd-6b60-3b43-b0a1-fffbd047a989 | -6.13178 | -59.94922 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6d3bf84b-bb1f-3d2f-9409-be6341f98198 | -5.77554 | -57.58206 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79c9fe07-a16d-3b6c-be5b-1291575e985b | -11.66068 | -43.43392 | 2026-09-20 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7ad1d84-a8af-36a4-9076-9e9d94425a47 | -9.69901 | -48.33937 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9276a699-b3b3-3d33-8649-2b24c9ade6c0 | -8.67011 | -45.32894 | 2026-09-20 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4daf503-39fd-39cb-9f5b-695286464869 | -5.89848 | -52.09259 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c34c863-228d-3204-83d9-6b8a932d8a48 | -7.1554 | -47.47491 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2c1977a-aca3-3e06-92a1-6cc1e9bf21e8 | -12.41818 | -47.47006 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c5ad799-6cad-3216-8619-bd00cde8cdcc | -10.86786 | -57.14332 | 2026-09-20 04:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 253e9eee-ace0-3e1d-9203-bb4508216240 | -10.56447 | -46.55963 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c991e40-658e-3471-b64f-afcf6f092fb2 | -7.58904 | -46.73181 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43aa6e36-7b3a-3b00-b01d-8ee1702ca528 | -10.91201 | -53.96856 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a1b0545-4ea8-3cba-ba65-150332c9eaf6 | -6.65845 | -50.89454 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f624ede-a979-376a-8b52-7a97b41016f8 | -8.43671 | -46.86122 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd02150b-ac2a-306e-bd87-0401a77877aa | -7.55561 | -45.44937 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd44abe0-cf64-361e-85b3-a9f37d4ed3e1 | -11.21993 | -48.38307 | 2026-09-20 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc9b8b3d-95f8-33f7-a7a6-18c3ee71b031 | -11.08976 | -54.03178 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 2a22b49d-0559-3ed0-93d4-dca0ce95a48c | -8.96733 | -44.6658 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1be88e2a-920c-380c-b1be-d54b3a1d8e0b | -6.65964 | -50.93183 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5649299-7791-3481-812b-bb059a59fbfd | -7.15481 | -47.45686 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 686dbdae-b8f1-3cf0-b5f3-944cefea1757 | -14.18386 | -47.8685 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ed3529b-931b-3d4d-88e1-c6dbbe776a76 | -7.97039 | -44.06966 | 2026-09-20 04:40:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 396c095c-fdde-3f36-8fa7-e6ccd1d70583 | -11.83794 | -47.62725 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd6b3802-eebd-3e6e-9b05-0f441401d9d9 | -9.69955 | -48.33591 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61718c1b-367b-3237-b599-f4d8ee81c333 | -11.12225 | -47.72471 | 2026-09-20 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86ad63f7-9017-3689-bab7-2c75c90be732 | -7.75109 | -46.76805 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f0858f0-68da-3cb6-9d82-1e3911fa0471 | -9.915 | -47.71786 | 2026-09-20 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 489a711a-d01c-39c1-b9f5-da9d4fed0e12 | -8.66548 | -45.43572 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c351fcd-b590-3946-8662-ca265db5de58 | -9.5757 | -46.55267 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a7dda0c-d65e-3b00-b260-06315da1f7ef | -9.79235 | -45.06784 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4df7212-839e-311a-acb6-4bdd60de33b1 | -11.32063 | -47.34764 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76c66f58-7b4b-3000-9625-dab0781d2716 | -7.34524 | -44.47299 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e17e494-3582-346c-bf97-bb9c2bf3ad07 | -6.79927 | -47.81846 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ce7bd19-5bae-3fb6-9029-048b37853932 | -7.18152 | -47.89304 | 2026-09-20 04:40:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0feea861-db04-33c2-8dcc-62226fe3e53a | -11.95584 | -50.10315 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2eba7b58-9260-394c-8c91-8e45fba352ea | -10.8779 | -54.09292 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f450ac68-1c8b-340b-b721-65a5d92fd626 | -12.15201 | -47.02949 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 08d86298-e0e7-3287-991d-d3dcf184555a | -8.16856 | -54.77694 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80fef9ec-5b2f-35f0-a55d-a635a1a5c5e9 | -7.768 | -44.05465 | 2026-09-20 04:40:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc1e4cb0-9ef9-3187-b8bc-5982213c76a0 | -10.10307 | -45.65977 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5015bc8a-36ec-3e42-9d47-9064f2e0e6d5 | -7.16037 | -47.46491 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdbcdeac-4308-36ff-87f5-f77c951de812 | -10.06675 | -45.68001 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cadd32c-fe70-3332-9cfb-beb0a3c5acfa | -10.60483 | -46.52871 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2005ca2-528f-364b-b5de-41fe03b7bc82 | -8.4424 | -43.85998 | 2026-09-20 04:40:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 59468b1b-f72d-382d-ad28-acdbe775957a | -12.31223 | -50.73417 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 68f80674-0bb1-3a75-b396-62e239359e8e | -7.35909 | -44.87743 | 2026-09-20 04:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f383d8b-5311-3ab2-9c7b-b09aadf6af65 | -13.02869 | -46.91467 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 931839da-966f-3434-a45d-015d99ddcc0c | -9.705 | -54.82996 | 2026-09-20 04:40:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7a5dd78-07ec-3ab0-abec-0a2cda444b50 | -9.04393 | -48.7669 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14e6cd5f-cf3f-3fd8-9088-1d3921b65c20 | -11.47447 | -47.78603 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfff133a-9b01-30dd-a6bf-56f908ee4650 | -11.03291 | -48.29881 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10ad93d9-40e1-3489-88c8-d283bee9ecfa | -10.31236 | -50.21822 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c98c0280-2cf9-39c9-9be5-c0272823f2cf | -11.08661 | -48.3001 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94c4ca47-120c-36bc-b9dd-10cdb7e7c471 | -10.8757 | -53.98881 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdb68eab-d540-3444-91cf-4203937d89ff | -11.85719 | -47.66062 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0ca72aae-ad36-3e96-ab83-856014e8dbe5 | -7.8627 | -49.61077 | 2026-09-20 04:40:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0deaf93-7601-3a21-b442-37aa011030e6 | -7.57356 | -46.30618 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b92073e-fcc9-33e8-ae63-91fd12e7dae7 | -9.78445 | -48.33505 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1584df19-2c82-3704-849d-7414d05d8046 | -12.16011 | -47.02285 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 663d0fd7-d0d0-30ca-85a2-f70bd8ae6f4f | -7.62311 | -45.45441 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 783b39e0-92ca-3e00-8f53-570988c67f70 | -10.47417 | -51.25873 | 2026-09-20 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16a75d8e-0aab-3846-8939-f81cb8d447a1 | -6.4905 | -58.38058 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26438879-1e1f-3245-b8c4-435d2314b832 | -13.2506 | -51.74569 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3649a55-eab3-3a73-bb05-3565e8fc9dcd | -8.66126 | -45.43936 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6c2973d-7abb-330a-bf27-caff094bf996 | -8.17159 | -54.73369 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3842b9f5-5594-39be-afe8-f0201ef23a6c | -11.79467 | -46.8304 | 2026-09-20 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e311972-94bf-37a5-9f8c-e2edf3fc4b52 | -5.86537 | -51.94246 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b53d908-6898-3cbb-be66-50262e0c54c0 | -10.40485 | -48.36177 | 2026-09-20 04:40:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c510eb11-c540-3896-bea8-93969380ee8b | -10.27836 | -50.26849 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d5300c8-6a05-3e14-99ff-4552a9a13504 | -11.72308 | -54.56512 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1722af54-582a-34d5-8abe-b90d993b9f10 | -11.95308 | -50.09904 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6589f194-cd9e-3a67-bfde-a13205c471a6 | -12.75048 | -52.83877 | 2026-09-20 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0c294f1-aa95-3d76-a5e6-1eca1ec65dcd | -7.16752 | -47.44092 | 2026-09-20 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d7899cf-0338-3bd6-b286-d8386c427936 | -13.30629 | -51.76652 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc5cfa6e-1e7b-3e13-bad4-17eb6af9ca8a | -8.75962 | -48.65383 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README70.md)
