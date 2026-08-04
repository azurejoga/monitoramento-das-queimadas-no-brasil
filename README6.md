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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 710e3e91-0209-38d3-ae8c-41377cb7f07e | -17.96697 | -47.14464 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e580e31-3793-35bc-bbab-0c489f50bc2b | -17.96014 | -47.14308 | 2026-08-04 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f19d0c0-1c26-3b4e-a99e-3e1be8426117 | -8.3546 | -45.9671 | 2026-08-04 03:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| acb0e196-8dc1-3925-a76e-7d50701127a3 | -8.3544 | -45.9897 | 2026-08-04 03:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 78e219bf-8727-3bf5-981a-6d316e5dd72e | -11.2213 | -54.855 | 2026-08-04 03:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| bae47968-6e29-3bd7-913d-44857fbfdd5e | -8.3546 | -45.9671 | 2026-08-04 03:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| bb114d91-e0f1-33a9-9fc1-d4ef54d6176d | -8.3544 | -45.9897 | 2026-08-04 03:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 54e2bac5-3ee6-3013-8888-f60f2ed0a667 | -11.2213 | -54.855 | 2026-08-04 03:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a9156c72-f565-3f08-9b2a-a69ddbfa6d9f | -11.2213 | -54.855 | 2026-08-04 03:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| fd9c68d4-f154-3f16-985e-5d2e7ff1d270 | -8.3544 | -45.9897 | 2026-08-04 03:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 89af9c3e-b497-3af5-91c8-97c96a8a3f5d | -8.3546 | -45.9671 | 2026-08-04 03:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| ff61676a-5b10-31da-82dd-bbf78c488aac | -8.3546 | -45.9671 | 2026-08-04 04:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| faea4bc0-66bc-356a-a7bd-b5fbd0e918c2 | -11.2213 | -54.855 | 2026-08-04 04:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 13c49c87-ab48-3f30-bf1c-2fed8550179c | -8.3544 | -45.9897 | 2026-08-04 04:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 996991ef-a934-3144-b169-65444c29549f | -8.3546 | -45.9671 | 2026-08-04 04:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| e0920843-39e9-3315-bc70-96f5b592f842 | -8.3544 | -45.9897 | 2026-08-04 04:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 2a7309b1-eafb-3699-9002-4d6f3d5cb87c | -11.2213 | -54.855 | 2026-08-04 04:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d3768690-05bd-3ac3-9111-9238debb5aa4 | -5.54861 | -45.19721 | 2026-08-04 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e20f748f-2512-3613-ac4e-94ab32b1ca99 | -2.96014 | -50.34356 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1c066dc-060f-3e69-adeb-783587377895 | -2.98235 | -47.73622 | 2026-08-04 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db429db9-f09c-3a75-b194-496a5f69dfe9 | -5.34235 | -41.01102 | 2026-08-04 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8db1660c-f749-3dbe-86e7-87500418be0a | -3.66181 | -49.47668 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a815460f-a295-308c-8298-6ff8f1902b40 | -2.96409 | -50.34984 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 561d46c0-c31a-37ac-8218-4b51d1cf2028 | -3.67121 | -49.4812 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a55e955-4bb6-3a22-9a42-23070cc5354a | -5.42279 | -43.43027 | 2026-08-04 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5e65d441-6206-3e88-be5e-78f7d828d2bb | -2.46203 | -54.67873 | 2026-08-04 04:17:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37ad4fcc-5c6b-32f5-b024-518ad540bcef | -1.63901 | -54.46041 | 2026-08-04 04:17:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e9550e1-29df-33be-bf5f-9669ec558734 | -4.89259 | -49.96677 | 2026-08-04 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| febd3c6a-fe81-3b33-8850-757ad28fe1f9 | -1.54821 | -53.69283 | 2026-08-04 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5e2e5da-fa31-3c5c-8e5f-2835be764e6f | -2.54539 | -48.5472 | 2026-08-04 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e8bae32-4b32-3d75-8a3c-0e4ac597d304 | -2.96506 | -50.35977 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 610e60c3-16e7-3623-8922-d40fd79c2fa3 | -3.11148 | -47.91924 | 2026-08-04 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8f49a57-b7e7-35a2-8cd8-459114227e4e | -4.37654 | -43.38457 | 2026-08-04 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8784711-01ca-384e-86ca-76318e482920 | -4.46324 | -47.91657 | 2026-08-04 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 002de35a-d561-3516-b482-222ccfdbbe53 | -2.15974 | -47.88028 | 2026-08-04 04:17:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a577b8f4-bf7f-3593-bd91-8e7996b509b5 | -6.00862 | -47.4059 | 2026-08-04 04:17:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4be6db4-ffda-34c9-a21f-f61aa582c397 | -3.41914 | -43.16518 | 2026-08-04 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 154647ad-24b6-33ed-9521-774a8e42708c | -5.61986 | -47.10513 | 2026-08-04 04:17:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93992b7f-0c72-3bdb-9b30-eb84a9ec6f0b | -2.96226 | -50.36065 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0d6bf95-d0eb-39d6-895f-dcdc3474ae41 | -4.31605 | -38.49116 | 2026-08-04 04:17:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 05c18fcf-cdf6-31ae-b5f5-799bc57dc2d1 | -4.91026 | -43.46949 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7bf3b17-acb4-370f-b561-d96e4b33fb7c | -3.96646 | -48.12411 | 2026-08-04 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b94389a-878c-3268-b0dd-b4eebd5a3798 | -2.73598 | -48.70531 | 2026-08-04 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 590c3011-ee1e-3102-b1b6-d0402b72d34b | -5.34217 | -41.00982 | 2026-08-04 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54a19940-2758-33a1-801d-85d5a846f6f7 | -5.99761 | -45.94988 | 2026-08-04 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75143c10-9997-3cc7-83b7-c27ea0e2da30 | -4.63811 | -43.1284 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e41bd498-b1ee-3dfe-8019-6d3ce2fa7c9c | -6.29505 | -43.82125 | 2026-08-04 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dd061c8-2b2c-3087-9db8-3db62f61ab01 | -3.49426 | -43.31195 | 2026-08-04 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5c622c1d-f440-3d94-ba57-0b48ebea0c44 | -5.54934 | -45.19798 | 2026-08-04 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1e4d7ab-04b0-3c03-bd50-bb8534a1c88a | -4.63866 | -43.12495 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 110cddc0-a5c3-3257-b99b-efa27c989aa7 | -5.3416 | -41.01354 | 2026-08-04 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 31c11c27-b5f9-303a-ad9c-79ce4cb229aa | -6.29781 | -43.82524 | 2026-08-04 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e548652-78ef-3e72-9a50-b68a5ccf3243 | -4.19172 | -44.39067 | 2026-08-04 04:17:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c05453c2-e258-3b03-a72f-da77a79c10e3 | -5.60575 | -41.14083 | 2026-08-04 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d2c79aa6-3d1a-3473-9904-48330de3747d | -2.68837 | -47.36066 | 2026-08-04 04:17:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49ffe40e-5891-3ea0-8088-46d5d604a3df | -4.36543 | -47.77006 | 2026-08-04 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44d2b66d-cb5b-36a5-9a52-14f91d2fb35f | -5.14498 | -46.20579 | 2026-08-04 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 00ff7c98-4fdb-33e0-bda1-3f0190e23033 | -4.63756 | -43.13185 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1ac70b96-0bb7-3192-9761-121bd59fef21 | -2.45894 | -48.15015 | 2026-08-04 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc4b1b7b-7cc9-3fbd-a44d-42965d690e6e | -5.48115 | -45.11753 | 2026-08-04 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a91b78f-dcf9-32e9-96b4-ed587ce09325 | -6.06761 | -44.87613 | 2026-08-04 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 619a42b4-596d-3c7e-9949-68b9c2135910 | -6.49658 | -42.22004 | 2026-08-04 04:17:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9d2d71e-58a5-3dc0-bfff-c661bf2a7a19 | -5.63732 | -45.91611 | 2026-08-04 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1670d645-5f03-3ec9-bb1c-2355b376d212 | -2.73231 | -48.7003 | 2026-08-04 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90e33ab0-ebfe-3990-94df-17ee7d4bc436 | -4.27298 | -48.60962 | 2026-08-04 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94d2f783-27d0-3037-8a92-2d4768065b67 | -2.95829 | -50.35442 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa3cf2d-fc9f-3851-90f7-b1c860b8e3b0 | -3.9706 | -48.12474 | 2026-08-04 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5233e458-babf-38dc-8f22-f14be6f71d3d | -2.96017 | -50.35896 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 699fcd54-a6eb-3b1f-893a-38d948226edd | -5.73562 | -43.27802 | 2026-08-04 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af56cf44-39a2-3044-a22e-c3066fd157af | -6.47823 | -42.22803 | 2026-08-04 04:17:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 13984bed-e50f-3fd3-a583-b44d48553f20 | -1.54277 | -53.69958 | 2026-08-04 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce709c27-b3f7-32f9-8fb4-8c21f9b6d216 | -1.54203 | -53.69154 | 2026-08-04 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28ba7def-f810-3dbf-a038-a78ee82fd3b9 | -2.69182 | -47.36479 | 2026-08-04 04:17:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbedf658-4424-3374-b0e2-0262556d9ada | -4.31449 | -38.4883 | 2026-08-04 04:17:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d6c21e28-cc67-3006-8f96-f07f19776577 | -4.8934 | -49.96202 | 2026-08-04 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0b00da8-0b9c-333a-8a81-2edecbb7f26a | -5.4483 | -38.44833 | 2026-08-04 04:17:00 | NOAA-20 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be2978cd-a00b-3923-a499-118cda3c0dbc | -5.04539 | -43.26011 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1eccd85-8491-357e-b61b-f589c3eccd10 | -5.34137 | -45.35122 | 2026-08-04 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 767b6e76-a4e1-3ed3-ab93-40a688501f6b | -5.75817 | -49.0928 | 2026-08-04 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8531167c-6409-3bd3-ab9a-5ffae83b204a | -3.03069 | -48.41722 | 2026-08-04 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7055328b-e068-3658-b76d-8773061c0093 | -4.64032 | -43.13581 | 2026-08-04 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27c39d90-ddc8-376c-b01c-96e5d8849a66 | -3.49758 | -43.31247 | 2026-08-04 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 92105a92-1390-3400-b0ba-544ffc7499e8 | -5.6388 | -47.10788 | 2026-08-04 04:17:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1456a76-06df-3bce-8541-ee842ef8f6e1 | -3.97683 | -48.43421 | 2026-08-04 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b608678-1fc8-3f6e-8f3a-ce67d3b599f7 | -6.0682 | -44.87252 | 2026-08-04 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ed784e0-a96c-38e2-be86-8e107a39b406 | -3.66291 | -49.47501 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 85db886b-e822-3d21-8ab6-5430669b4411 | -3.57942 | -50.25896 | 2026-08-04 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ca1fe74-90b1-35e5-a61b-50ebf7fdc908 | -3.66667 | -49.48039 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b898d8a9-bd18-3f77-bd04-92bbedbafcaf | -3.67354 | -49.46735 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ba9e03c-9538-37eb-b067-aec7e72ce67d | -3.11208 | -47.91552 | 2026-08-04 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b838518-b46a-3208-8f96-37f55f40e5ec | -5.75759 | -46.37982 | 2026-08-04 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31fbadde-e9ad-399c-aa0f-96f9961996c4 | -2.32716 | -47.20257 | 2026-08-04 04:17:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8361ffa8-6b13-3d66-8243-723abb9b78c0 | -6.54743 | -41.82589 | 2026-08-04 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a63dede1-8a6b-37a2-84dd-dfae55e8c2e6 | -5.48802 | -45.11866 | 2026-08-04 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afd9e24b-1768-3ff5-ab59-bdd6e12aab91 | -3.66822 | -49.47118 | 2026-08-04 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2c0d2595-542e-324a-a112-dfcbbd658944 | -3.97748 | -48.43029 | 2026-08-04 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36d4f64d-632f-3928-80e0-f753952aaa77 | -2.96593 | -50.35434 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2ce75b7-b83d-345c-bfdf-fbc6af39b759 | -2.96105 | -50.35352 | 2026-08-04 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40f3a1d2-3c2e-3554-a6b7-6df1b6560661 | -2.30916 | -48.58525 | 2026-08-04 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b28a86b-052b-3b84-9e1b-c0eeed383858 | -5.5444 | -45.79512 | 2026-08-04 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README7.md)
