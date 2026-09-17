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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f9da386-bdf9-3301-841f-0eb9e4cdc55c | -7.8033 | -44.8651 | 2026-09-17 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 180.6 |
| f9951aed-bbef-3f63-b93c-dd0e2afa911a | -9.5512 | -45.4296 | 2026-09-17 13:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 3ced9e1f-3a1c-314d-9ad0-d723ee6c0e9e | -10.0422 | -45.5528 | 2026-09-17 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| b5074ac7-7dc9-370b-a9ae-2b877b1c24d2 | -10.4137 | -48.6714 | 2026-09-17 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2a563590-107f-3d39-a501-80e34b618b39 | -11.3463 | -47.2585 | 2026-09-17 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 10b02f70-a2b3-31a6-89ee-a699c08bd2c3 | -8.9293 | -62.4092 | 2026-09-17 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 91761b95-c251-35d2-bdb1-abc63de0e090 | -8.8647 | -45.8693 | 2026-09-17 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 438.3 |
| bb8bc071-b64f-3381-9ee9-dafecb6f88c0 | -12.49 | -50.8901 | 2026-09-17 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9dc45129-d69b-385d-a347-e08f0ad22bb9 | -8.8644 | -45.8919 | 2026-09-17 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 340.0 |
| 80317860-bb9b-3064-b802-4a2bd18ce4cf | -7.1381 | -42.1768 | 2026-09-17 13:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| a3fe7a05-db1d-3f35-a147-41de9d77b9f5 | -14.1742 | -45.1407 | 2026-09-17 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 0d3eb7a9-ee07-34e3-90ad-b9c015cd917e | -10.0418 | -45.5756 | 2026-09-17 13:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 317.7 |
| 7eeb8c15-42a2-3840-a778-38a4a228c5bf | -10.8919 | -54.0062 | 2026-09-17 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| ac8208af-2550-3e72-b4af-69fdb3c5a07d | -10.7927 | -46.1618 | 2026-09-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 1a9fcd7e-dd10-331f-82c5-acea3d0e5dbc | -7.0804 | -47.5031 | 2026-09-17 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 776d0e07-b2d4-3cfb-aadf-f7434a65fbd2 | -9.7497 | -46.1089 | 2026-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 071197d4-5501-3d37-964b-d58f8500f3fb | -9.7687 | -46.1067 | 2026-09-17 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| a50ae476-6e83-3f67-91c8-8b579922cde8 | -8.475 | -46.8943 | 2026-09-17 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 36170bd4-d477-3c6e-9f05-422f29e624e0 | -7.0802 | -47.525 | 2026-09-17 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 9958c7e7-6782-3008-9b78-858a96ee4651 | -7.8221 | -44.8632 | 2026-09-17 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 29095e3a-7db2-35af-95b3-e48b2851934a | -8.4797 | -57.6282 | 2026-09-17 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 1a8facc6-c588-3eed-b67b-1ce09b2d5126 | -10.8118 | -46.1594 | 2026-09-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 221.8 |
| ecc804c1-367c-35e9-8d86-4b4267bb92b5 | -7.0349 | -44.6625 | 2026-09-17 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 145.9 |
| d7c89e90-6c0e-31f8-b7a0-df603a9b395f | -18.8906 | -46.8284 | 2026-09-17 13:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| c434793b-a5d3-3920-aaca-a1ad348e7bfb | -7.0451 | -42.0666 | 2026-09-17 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| d9bb9237-a8ed-38d6-ad68-7415cc92e8c4 | -7.0084 | -43.6497 | 2026-09-17 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 984a39aa-e793-3e0b-b5dd-a3348be85cf9 | -9.8319 | -48.3636 | 2026-09-17 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 162.1 |
| c9aaba66-3beb-351a-b407-6a7e22635ed0 | -8.9107 | -62.41 | 2026-09-17 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 113.0 |
| d0e5689f-b056-36c3-9440-af338b42a928 | -8.8459 | -45.8713 | 2026-09-17 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 0c621084-1560-385b-9814-9ca4e351c383 | -11.8069 | -58.1759 | 2026-09-17 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 7c5266a4-ee59-3523-865c-2f987f933fba | -8.8836 | -45.8672 | 2026-09-17 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| d10c3c93-9dba-380f-8917-da4fb82236bc | -8.4983 | -57.6271 | 2026-09-17 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 87a6de05-d8b0-38bc-a844-cb0679fd51ac | -10.414 | -48.6495 | 2026-09-17 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| a4f9195e-8aba-32eb-85d7-752d1cf67b5e | -14.1547 | -45.1442 | 2026-09-17 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 0e8c1d23-2cbf-37bf-a3a3-308ab30f8361 | -13.3055 | -51.3235 | 2026-09-17 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9a4a378c-7b24-3b9b-ba83-50af00a3d9b6 | -8.1124 | -54.8073 | 2026-09-17 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d15ea07f-e647-3abe-b173-4b34cde135eb | -12.3085 | -47.9539 | 2026-09-17 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| cce0a071-4719-3610-a52b-073a56f57f2b | -8.4797 | -57.6282 | 2026-09-17 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| e1bfd0f5-a37a-39c9-9e11-e965238729ec | -12.7894 | -51.2807 | 2026-09-17 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| d4008fc8-0650-331d-a01b-3c9cf7ca8388 | -11.4861 | -45.7279 | 2026-09-17 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 4f19d892-cb01-31db-a189-72f5c5c65c42 | -10.8118 | -46.1594 | 2026-09-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 8a9897b5-6163-3e73-84ed-8db1768b88ba | -10.8308 | -46.1569 | 2026-09-17 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 1307a698-cd07-3a3d-8cdc-1376e1b2dabd | -11.8069 | -58.1759 | 2026-09-17 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| fc47103b-bbd8-3108-af88-c980b87916bc | -30.6109 | -53.0283 | 2026-09-17 13:50:00 | GOES-19 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 283.7 |
| b6b9e95e-adc6-308f-9be1-b9c74c57dbe9 | -18.8906 | -46.8284 | 2026-09-17 13:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 481daaca-403b-3ab8-bb8a-4c07a4f82382 | -8.8737 | -62.3925 | 2026-09-17 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 242984b2-65d1-3144-a909-b5217269c0e2 | -9.8517 | -46.9269 | 2026-09-17 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| cc770296-a8a1-3e7a-a483-1b2b85a2e447 | -13.6526 | -45.993 | 2026-09-17 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| ecbfd166-1727-3975-8b68-351fe92c1e97 | -9.5512 | -45.4296 | 2026-09-17 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 236.9 |
| e280a73d-34e6-348e-83bd-2d035462b037 | -11.3437 | -44.0141 | 2026-09-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 0b1a59ee-d0b3-3ceb-90f3-523a6c908fb5 | -9.7608 | -60.4561 | 2026-09-17 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6596a546-1389-30a0-8b60-afed389fcaf0 | -10.4137 | -48.6714 | 2026-09-17 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| fa801329-2b6e-310c-9210-7f0ef376f58c | -7.6381 | -46.1478 | 2026-09-17 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 343e89b3-02f6-341b-b18f-cae97504af30 | -7.8033 | -44.8651 | 2026-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 160.6 |
| fc2de68f-bbc2-37d1-a3b3-41585faf550f | -8.1124 | -54.8073 | 2026-09-17 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bfca5bdb-26f2-3f72-ad77-98d1cc9b0d41 | -4.5044 | -54.9845 | 2026-09-17 13:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 15f6857f-5dce-3a9e-8095-e57681961515 | -18.8899 | -46.8519 | 2026-09-17 13:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 83aa28fb-fcae-3222-9e05-8f3e5b6267e9 | -14.8183 | -59.5532 | 2026-09-17 13:50:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| eaddf759-a095-35cf-bdb8-4c6b51bd9adb | -7.3669 | -38.9584 | 2026-09-17 13:50:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 272.4 |
| 53d68833-8c80-3c19-8d80-5ef5bb270620 | -8.9107 | -62.41 | 2026-09-17 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 4b013801-5d99-34c0-b97a-ce74ee30b935 | -9.8505 | -48.3834 | 2026-09-17 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5e216121-97e2-3c1d-bd2e-c9929b716d74 | -9.8319 | -48.3636 | 2026-09-17 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e742f963-8993-3577-826a-a1f3c1177be5 | -7.0617 | -47.5046 | 2026-09-17 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 1d306bba-bb68-3b81-a787-96d84443c038 | -7.6402 | -44.3303 | 2026-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 9915ed83-e182-339a-a3af-47dc37225da2 | -15.5711 | -54.2439 | 2026-09-17 13:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 8bac0efb-ca3e-3871-8d16-b1c441fce3f5 | -11.3442 | -43.9906 | 2026-09-17 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| a3d4bee5-79a8-352b-9cd4-c6d82a9212f7 | -7.0804 | -47.5031 | 2026-09-17 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 49a321d2-cbd2-376b-acad-d068124ab089 | -7.0802 | -47.525 | 2026-09-17 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a924e955-a09c-332d-8e04-ca780e63a72c | -8.8644 | -45.8919 | 2026-09-17 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 1f721a8f-06ec-3fcb-b39a-6e52461f9bcd | -8.8647 | -45.8693 | 2026-09-17 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 154b44c0-34a1-3825-bd1b-f20e0dd60332 | -10.0418 | -45.5756 | 2026-09-17 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 3b5ea450-e934-3759-9e56-eb9149e7a133 | -10.414 | -48.6495 | 2026-09-17 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 3f58eb72-e01e-3b1d-a5b0-1c81ea7be2df | -8.4982 | -57.6468 | 2026-09-17 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 241.8 |
| ab7dad37-b1bd-39e5-b886-743f90c10b4c | -15.5715 | -54.223 | 2026-09-17 13:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| b814476f-c674-3045-95c9-662bf2013f63 | -12.7051 | -48.276 | 2026-09-17 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| fad975e0-0fdd-3754-9ea4-794d51d06592 | -7.0084 | -43.6497 | 2026-09-17 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 833c9d2a-ea26-3262-a746-348b99219d3a | -8.8923 | -62.3917 | 2026-09-17 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 871712f1-9f96-37be-871f-7050a7478108 | -9.8697 | -48.3595 | 2026-09-17 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e2246275-4a86-3bdf-8cab-b1e44656c43f | -10.8919 | -54.0062 | 2026-09-17 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ad7d047d-531a-3c26-bb34-b9353adb4cf2 | -14.5709 | -46.5941 | 2026-09-17 13:50:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 110.3 |
| c76d93e6-6473-3264-b267-f5b9546481a7 | -8.4796 | -57.6478 | 2026-09-17 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 7f78b6f3-4f72-3d6e-ac63-79902c3e8b67 | -8.9108 | -62.391 | 2026-09-17 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 14eb0371-f741-303d-8199-5fcd1158c0d1 | -8.4983 | -57.6271 | 2026-09-17 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| b1ec6b3b-3b00-3fee-be7a-839272791218 | -7.0349 | -44.6625 | 2026-09-17 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 56176289-496c-3284-9783-9af1c5b8ba7f | -14.1742 | -45.1407 | 2026-09-17 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 9f4f21e4-7be6-3cbb-8030-d39e424482f4 | -7.8221 | -44.8632 | 2026-09-17 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 276.4 |
| e6971f76-9bc2-381e-85e4-6647b7cbcdec | -14.1547 | -45.1442 | 2026-09-17 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| a0bd12d7-19a7-375f-b316-744b529b8101 | -13.6531 | -45.97 | 2026-09-17 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 293.5 |
| 74647a03-5bfa-385f-985b-09168bc1cb75 | -4.5229 | -54.9639 | 2026-09-17 13:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c0d8d42b-7d4e-338f-a8e5-27fe2a2a8abb | -9.8884 | -48.3794 | 2026-09-17 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 494dd461-cab2-3a4a-ac9e-c26da945dec7 | -9.8694 | -48.3814 | 2026-09-17 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 98fd49b9-56bd-30ce-97ce-ecc333321f83 | -7.1381 | -42.1768 | 2026-09-17 13:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| efbe8bf1-b6a8-3f78-be68-13b3ea766a6d | -14.1552 | -45.1208 | 2026-09-17 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2a0f53ad-9df9-3741-bb6a-b2c109f5284e | -4.5045 | -54.9646 | 2026-09-17 13:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 5fc34abc-7a0d-3342-93ce-09c7ebbe574a | -3.2212 | -53.9422 | 2026-09-17 13:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 5fffe99b-dd56-3126-acb6-d319e3fae4b2 | -7.4304 | -44.5804 | 2026-09-17 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 81e4e490-f606-319a-85be-65b345011dce | -7.0454 | -42.0427 | 2026-09-17 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 4faa51b9-dfad-3c10-b779-689ff62d0d01 | -8.9107 | -62.41 | 2026-09-17 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 3ee9c849-13f7-3ce6-97c6-7dfc45b1e58f | -12.6816 | -50.8455 | 2026-09-17 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 590893d9-374f-3311-a080-60f1fe2a71b6 | -7.1192 | -42.1786 | 2026-09-17 14:00:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |


[Clique aqui para ver as próximas entradas](README91.md)
