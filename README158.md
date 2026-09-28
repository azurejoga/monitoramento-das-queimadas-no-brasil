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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a731ce3-da37-3f11-bc1f-8b8170b2baa7 | -10.51618 | -45.36497 | 2026-09-28 17:09:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 26ab828e-c01f-37e2-a36e-7619f0529ea7 | -11.10302 | -51.17191 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| a4c5c5c9-68df-3d86-a305-78d2d046fbf7 | -9.1441 | -49.97222 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4e2c0529-16dd-3116-8b9b-9739aee2b78d | -10.91087 | -50.6742 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6dd77eba-3ef8-3633-bb9a-b1c36065bc79 | -9.97964 | -45.33832 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab3671e9-6931-30f4-8201-79933398ede1 | -8.09018 | -54.74725 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b21ac07c-206d-3aab-84da-c31da69b52c4 | -13.50865 | -61.14117 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ef19c928-50c3-37d2-92a0-7073eb4bdd48 | -6.16108 | -52.89544 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 12f28eab-ec97-3ea5-8b73-670891c97d75 | -12.07453 | -48.53594 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| db51143e-e0b1-3483-87f5-ac41c744a163 | -6.17277 | -52.83277 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 19bfd289-179a-3daf-a06e-d82d97c34695 | -11.97992 | -57.60122 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 60646cdd-672f-3272-a272-1ae02328fefa | -7.4944 | -44.56192 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e21a0f02-cc13-3d44-abd4-8d0e7f3469d7 | -9.19092 | -45.845 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d1a00ad7-81ac-333f-9008-735d0a629c88 | -9.38979 | -46.38986 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b68f391-eaa2-3fb5-82fe-51e9ef1e799d | -7.27493 | -46.94081 | 2026-09-28 17:09:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6b00606f-72d0-3e2e-93b8-abcbd7ae4fb1 | -10.89958 | -44.65883 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 37493a83-d2e4-3ee3-b673-28bea439b565 | -9.40037 | -46.39361 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4e57ae1f-0021-33e5-ac0e-cbeeb127d2b8 | -10.27225 | -44.62461 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 182.8 |
| b500faa6-ad0b-341e-8392-305c209839c5 | -7.43175 | -55.62602 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 957d7c79-9c02-3242-b14a-68fd4669812a | -11.07752 | -46.07743 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dae6f2e3-51a3-3881-ba1d-f5d6083e0728 | -9.98279 | -45.35516 | 2026-09-28 17:09:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c19c6326-e753-31e9-b98e-e5d41d2830f2 | -10.82507 | -57.22158 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a76b60c1-f66c-37be-997f-749d78b6ecd3 | -11.85877 | -47.10263 | 2026-09-28 17:09:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ae838b97-9e5c-3ccc-96e1-d3603461b124 | -9.02375 | -50.80735 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a00a8c8f-f80b-3d76-8899-44ab19001478 | -10.20552 | -50.01199 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 74998399-f066-3b35-8eb9-d3a77cffebf5 | -8.97538 | -44.14617 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a882198b-7169-3803-a7a3-b8fcfc9b3014 | -11.02446 | -49.70525 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 84851daa-83fe-3910-831f-fe0e97d88925 | -10.21613 | -49.97922 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4c5c712c-4a7d-379e-91ad-311887d7d5ca | -11.12817 | -50.06491 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 103c0cd8-9277-3239-9697-e2fb9449a7a7 | -8.27253 | -54.71879 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7f1415ae-1913-399b-be6d-ae11cc232b69 | -10.70187 | -60.73818 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 875f8eb7-fd67-302b-bcd0-a6f95f79a281 | -11.09149 | -51.1695 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 138c359b-2a07-3883-a74e-1355279094cf | -7.3821 | -44.7691 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7d6392fa-956e-327d-b3ec-8297e6e49f00 | -8.35731 | -45.47203 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b492bec3-2d90-3396-af97-4e49ac8493a0 | -10.51992 | -57.43679 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 5f9da029-7479-3faf-9d9b-b324de83dd84 | -8.67107 | -45.34591 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cc8881c6-09c3-3d9c-9650-fb844f9ed087 | -11.56042 | -47.38653 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a3465323-f21e-3ee2-ad0f-fa483edd0a56 | -9.86671 | -43.62193 | 2026-09-28 17:09:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 52f1cc40-8b72-349a-b5ad-50e9a34d79f7 | -8.189 | -54.79218 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1a94aabb-575b-3278-a5dc-dacd68aee265 | -13.03799 | -56.59652 | 2026-09-28 17:09:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| c441ea71-6c3f-30a0-8b45-f7edd0f7d818 | -10.89321 | -50.69405 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1bdfb60-e5bb-314d-8d00-9691dc1d1e6f | -10.27678 | -49.95536 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8a9ceef9-bd59-30c0-90e4-540fa662d405 | -12.77473 | -52.81448 | 2026-09-28 17:09:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6402fff6-e97b-3fe5-887f-342c28cfae41 | -10.74326 | -48.76598 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| aedaa6ff-eead-3327-925e-6f7852841c62 | -11.54431 | -47.37505 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b1532da3-987a-3df2-915d-4771d7c78197 | -10.88956 | -53.93824 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b75e82d-8a5a-300c-89ef-5a803da377f8 | -10.72526 | -53.99793 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| adabd0d3-4efb-316c-b842-91f2afaa8e18 | -5.25881 | -44.93622 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 73790ae2-3b77-387f-820a-62d4948608bb | -6.34704 | -55.32987 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 0bf70724-71ed-3401-bf93-517e60df687c | -8.85104 | -62.15586 | 2026-09-28 17:09:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2cee737e-6e56-331c-b22b-0d46072640b3 | -9.49463 | -46.60186 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 4102f13c-d6e1-3911-9dbb-6061335340ce | -8.18729 | -54.8031 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f4b4444a-dc38-3e60-b978-b021e3fb4ef2 | -10.08054 | -50.38028 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ff4e362-b574-3c8b-bfcc-d20cb1486de1 | -7.66581 | -45.48033 | 2026-09-28 17:09:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 45c76bbe-430a-3585-af78-b38229df209e | -9.58397 | -47.32417 | 2026-09-28 17:09:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6425b57e-042d-39cf-a7c2-7c80ec193ce1 | -9.78 | -44.82056 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| db5ec8cf-5d98-3ac3-8a06-c89d00165753 | -7.30805 | -43.31496 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4f220ec3-42ed-34d7-8d66-465ac97e0c96 | -8.94661 | -45.90103 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3575541b-7f54-32de-b79b-925657e70be3 | -8.82634 | -46.58683 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7ba3b7b9-343b-3166-811a-05d3e7819c93 | -9.76268 | -44.85001 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0c5e0e6a-3a7a-3262-aea5-283efc771f9e | -10.11888 | -50.19238 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 58917777-3885-3916-a680-b592094258e4 | -9.33344 | -46.5368 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3dc82d97-6874-34dd-ba7c-b417c83a84d7 | -11.17764 | -51.37874 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5c905a68-4fa4-31e2-b6ff-bd9537786d34 | -5.73254 | -43.28394 | 2026-09-28 17:09:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 255a3e45-20d5-387f-9388-5759a3016f85 | -9.80511 | -45.7113 | 2026-09-28 17:09:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 529dc979-4560-383e-bced-cea24d58d638 | -7.3657 | -60.58903 | 2026-09-28 17:09:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 50665d9f-c817-34db-8b1e-66e479a5c520 | -6.03851 | -49.56564 | 2026-09-28 17:09:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9ca4dec9-dcc3-35d3-b062-99721920c8cc | -10.12429 | -45.1453 | 2026-09-28 17:09:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9aacbb92-1fca-3a68-87a8-59625cf47385 | -7.01815 | -45.82703 | 2026-09-28 17:09:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6cef2fa-3108-326a-b6b5-c33a8d1dfe5c | -9.52559 | -46.37238 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9068554b-4d15-3ecf-882c-43afef3c9ff3 | -10.77412 | -48.74464 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 841f1a99-1f85-393e-a39b-b1c6fc68589f | -7.28521 | -44.30779 | 2026-09-28 17:09:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f08ccf87-3bbb-3784-91ef-a3be1c0b19b2 | -8.27838 | -54.71023 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 53c8859a-30b4-3a0d-90d8-98e96f7f8fd4 | -8.62527 | -46.98666 | 2026-09-28 17:09:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 76604a9a-f762-3119-87f9-9420d54f2a5a | -9.76772 | -44.8442 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f88f69dd-55a0-3034-ba67-42927a6bbdfa | -11.0958 | -51.17312 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| c104523c-215f-383c-807f-fac853628e1a | -9.74862 | -48.94987 | 2026-09-28 17:09:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 97ab1f9a-0532-3e23-ad28-373fd4364477 | -12.22341 | -50.43518 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 3d2387f2-5b0f-3d0c-a194-223172aa9d72 | -10.25646 | -44.60226 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a8c2626-1a3a-37be-92ec-3709726a8129 | -7.67798 | -44.88175 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| f82162b9-5dd4-3ec5-aaa3-0c2e236ca98e | -10.12914 | -45.14139 | 2026-09-28 17:09:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5944bf27-ebbb-3907-addc-8093828cb368 | -5.84003 | -53.84422 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9546edab-010e-3228-b002-41601cde6f8d | -7.37551 | -44.76556 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3caddf69-2521-3602-abe7-f39bb1abbe42 | -9.8308 | -44.93983 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 77750c70-0e39-38b3-8a01-b946bbd17b60 | -11.16528 | -50.0606 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a9d8117d-1d69-36e1-94b9-b2b372fbe89d | -9.12069 | -49.90459 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 6f57a378-63db-304c-957e-f266b2da7587 | -9.53701 | -46.89597 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1144cc67-6ab2-380f-9a0a-0db19063bac5 | -11.89931 | -49.98763 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 57a7763f-6d8f-34de-8a82-27734ba0d589 | -12.80033 | -54.00965 | 2026-09-28 17:09:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 28c7b440-c900-38d0-80df-7411c7895023 | -11.57733 | -47.40269 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8340e5b2-7dff-357f-b7d1-67c308d9568d | -9.31829 | -46.56645 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2f160539-e7f8-3162-bfb8-9d979605165a | -8.24251 | -45.40092 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6915a24b-bfc1-3898-b3f6-8d7f1834ee4a | -12.37033 | -50.24074 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e2047a22-fe30-3007-9e36-f0150d319c62 | -9.0737 | -49.8693 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 98d1aa7e-1627-3a2d-aaab-910e53840c0a | -10.73227 | -61.56955 | 2026-09-28 17:09:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 4f989c03-8ff5-3daf-addd-95ec9b445132 | -6.1246 | -56.35062 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| ce216a60-94ab-31f0-bbbf-5aae01aa60ea | -11.16225 | -48.17714 | 2026-09-28 17:09:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1c3aefc6-9981-327e-aeab-e1413842e76a | -9.7759 | -44.8578 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1fd2441c-89b6-3039-8738-16fec07378dd | -6.21426 | -53.47366 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8fe7c84f-b2f3-3e96-89ad-cc3655f48046 | -6.16447 | -52.82601 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README159.md)
