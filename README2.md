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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e679deb-a66c-3841-829e-73fb3874fbe0 | -5.6786 | -43.3659 | 2025-09-10 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| bd0cd18f-5f33-3717-a973-a8cdecbc56ae | -13.1364 | -54.9376 | 2025-09-10 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d1c30695-f361-3142-8856-c7aa8a9ea141 | -15.8873 | -51.8059 | 2025-09-10 00:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 150.3 |
| c6e443fc-d7ec-39af-97e1-2f814f00e76b | -18.1325 | -51.7096 | 2025-09-10 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 3fac1f2c-35e8-336f-99e4-5a11dba0ee92 | -11.3393 | -46.5193 | 2025-09-10 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 461b9fd1-f59e-3ada-9bd9-32541944e372 | -18.1519 | -51.7281 | 2025-09-10 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 570d421d-1abd-3342-ba11-3c46d46ce2aa | -7.7893 | -46.0667 | 2025-09-10 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 0abe44b8-fa0c-38cd-b067-06dfff5d04da | -13.2031 | -45.2834 | 2025-09-10 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 66d6c643-c58d-32d4-9667-cc49e735e2ea | -18.1524 | -51.7062 | 2025-09-10 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 4336bfb7-5f4d-32ea-bc8b-1ef5e9e65cc2 | -23.758 | -51.8917 | 2025-09-10 00:20:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 50.3 |
| 23ab1294-1b3e-3a73-a94f-1dfc74c2b464 | -11.4465 | -43.6224 | 2025-09-10 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 4acfc795-a4de-3f90-940e-b3431cd3071e | -8.0602 | -48.6856 | 2025-09-10 00:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 0bd11eea-c801-3375-a538-dacbedc5dfe2 | -15.8873 | -51.8059 | 2025-09-10 00:20:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| dc2237fe-57d3-31eb-b6a6-509374feb71d | -7.7705 | -46.0684 | 2025-09-10 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 5477a0dd-7609-3abf-be9d-6ca1c3444869 | -9.4388 | -46.7052 | 2025-09-10 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 4372c094-16ad-3204-930d-51f38e00dabe | -8.7564 | -63.4756 | 2025-09-10 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 88c1597d-7edc-324c-850f-5fa641038897 | -21.0371 | -48.41 | 2025-09-10 00:20:00 | GOES-19 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 4f9c36f0-ea00-3857-9170-5e6ff35cfaf9 | -11.3202 | -46.5218 | 2025-09-10 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| afebd345-7045-3112-81bc-4511b870658d | -13.1369 | -54.8966 | 2025-09-10 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 38b3ef64-b99f-365f-9e59-c3b59ac1e1c4 | -13.937 | -48.2522 | 2025-09-10 00:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 7f88cb24-f2c0-3400-9f02-c5894a5d1f45 | -5.6786 | -43.3659 | 2025-09-10 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 555ddd31-b257-3368-ae89-34ac915001ee | -8.0414 | -48.6873 | 2025-09-10 00:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 2b7424c1-73d9-35ed-bd31-baba987bbd06 | -11.4469 | -43.5988 | 2025-09-10 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 198a2c29-1b18-39e6-8bda-b3b044ff2a3b | -12.9286 | -54.7949 | 2025-09-10 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1752fe50-ef6b-30e2-9869-de6e5eb235d3 | -15.8677 | -51.8087 | 2025-09-10 00:20:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| dd359fdb-7da2-3851-90fa-db4e8903ae71 | -18.1325 | -51.7096 | 2025-09-10 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 2037c32c-af0a-35d5-8a93-73717c4c4a8d | -6.871 | -47.8911 | 2025-09-10 00:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ebb11bcc-9b28-3cb3-a815-5ad486930a7a | -13.9564 | -48.2493 | 2025-09-10 00:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 597e5f7f-6aed-3f61-a10c-3ff44283f5a7 | -13.2036 | -45.2601 | 2025-09-10 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| df48fa36-0d92-3ae7-b318-69d94546ed91 | -11.3205 | -46.4992 | 2025-09-10 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| cb78e822-f196-35de-b6a7-cfae3f19ed54 | -13.1178 | -54.8986 | 2025-09-10 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b9b283c1-8484-3de1-9d4d-92980d664998 | -13.1837 | -45.2865 | 2025-09-10 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 1fe1e97c-2b42-3e81-ad58-7bd69f56a54d | -5.589 | -45.0505 | 2025-09-10 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| f8e82d0f-226e-323b-8092-71343cea7196 | -5.6598 | -43.3673 | 2025-09-10 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| b0c8f2a7-b076-3d84-adf0-3723d36fe1fe | -15.8673 | -51.8303 | 2025-09-10 00:20:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a0254a7b-2097-369e-b543-1f11b8518c2c | -13.1364 | -54.9376 | 2025-09-10 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| faf0099c-d73b-3bec-b7aa-faabfafb2228 | -12.9673 | -54.7499 | 2025-09-10 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2420e59d-190c-3722-b06b-8f639dcdeac4 | -11.3393 | -46.5193 | 2025-09-10 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 9695937e-71b7-366f-8073-fb3b8095e1da | -5.5892 | -45.0278 | 2025-09-10 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| c44c5c5b-747b-3fbc-83c9-73f595e94802 | -15.8869 | -51.8274 | 2025-09-10 00:20:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 103.3 |
| e40c3265-2f5d-38d7-acf8-ba856c4ed66b | -13.1367 | -54.9171 | 2025-09-10 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 9a626bad-12c5-39ac-ab8b-a56b16fec95a | -5.6788 | -43.3425 | 2025-09-10 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| d1234cdc-8482-3b81-bcf2-0c456129ad51 | -6.2595 | -43.4129 | 2025-09-10 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 909b5157-77b4-3bff-b73a-054a87554dd4 | -5.66 | -43.344 | 2025-09-10 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| f8f4dc45-a9bf-32cf-8855-23a5a2c5394d | -18.1519 | -51.7281 | 2025-09-10 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| bd10b962-42d1-3794-ab9e-27d9507d4dd0 | -12.9482 | -54.7519 | 2025-09-10 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1acc474b-692b-3fca-b677-b0ded2bbcfab | -13.1176 | -54.9191 | 2025-09-10 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 5c31096f-2e5f-3175-9560-2dd3392fe746 | -13.1173 | -54.9396 | 2025-09-10 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 37f5559c-a7f8-37a1-a971-94269f2b3c1e | -13.1842 | -45.2633 | 2025-09-10 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| aee380de-e614-3026-84d6-b40ad2139980 | -18.132 | -51.7315 | 2025-09-10 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 2cd4c002-4402-3534-964d-8e27b2ef3b86 | -22.15241 | -43.226 | 2025-09-10 00:26:00 | TERRA_M-M | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 107.6 |
| 6dcefe5e-c89e-34bc-92c0-256d0f393d5f | -23.74978 | -51.90463 | 2025-09-10 00:26:00 | TERRA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 35.6 |
| 87a72d04-8c51-3aac-bee1-2a88d2da7539 | -22.02878 | -42.894 | 2025-09-10 00:26:00 | TERRA_M-M | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 5aadd53c-eabf-397e-8f74-914e3d353018 | -22.15394 | -43.23613 | 2025-09-10 00:26:00 | TERRA_M-M | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 8e5adb2b-c6b3-33a4-9633-c3b3db1d974b | -22.40341 | -46.76199 | 2025-09-10 00:26:00 | TERRA_M-M | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| baa66f84-6edf-3983-92f0-fba99e83529b | -23.36527 | -47.18849 | 2025-09-10 00:26:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 57b390e3-01bd-3f2f-b392-af4767e4fe2d | -22.77274 | -46.20919 | 2025-09-10 00:26:00 | TERRA_M-M | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e29a3db5-4355-359a-ab13-1dd68a413214 | -21.57753 | -44.01779 | 2025-09-10 00:26:00 | TERRA_M-M | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 6cd7ec76-b0ca-3252-944a-330568a642df | -23.36662 | -47.19946 | 2025-09-10 00:26:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 7306cab3-9ca5-3d71-a716-4279d98aa7e0 | -23.74628 | -51.89976 | 2025-09-10 00:26:00 | TERRA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 0a17700b-a030-346c-87b3-0ec1463f7754 | -23.75954 | -51.89835 | 2025-09-10 00:26:00 | TERRA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 70226cee-c37c-3bf7-aa8b-613fc1f842c8 | -22.92694 | -45.42731 | 2025-09-10 00:26:00 | TERRA_M-M | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 1a310c3c-aacb-3c6d-85a7-8c6f3c0071b7 | -21.31993 | -43.89408 | 2025-09-10 00:26:00 | TERRA_M-M | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.9 |
| dca330dd-ec85-3f39-8246-4472f440279d | -22.8793 | -51.232 | 2025-09-10 00:26:00 | TERRA_M-M | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 51.1 |
| 4ca953ad-9810-3431-be30-0e3995577ef1 | -22.77857 | -45.35516 | 2025-09-10 00:26:00 | TERRA_M-M | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| cd219805-3256-3fd2-8377-9a1b99c9b516 | -22.33524 | -47.32827 | 2025-09-10 00:26:00 | TERRA_M-M | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.2 |
| 20b4dd51-5bc3-3b89-991f-35197628a283 | -21.57612 | -44.00805 | 2025-09-10 00:26:00 | TERRA_M-M | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 46cc0cfa-1608-3245-bb2e-d752b5361c7e | -21.40005 | -43.87408 | 2025-09-10 00:26:00 | TERRA_M-M | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| ce3ad3da-0841-3b77-b453-eb7287d85135 | -23.35716 | -47.20092 | 2025-09-10 00:26:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.9 |
| d4c3e012-5752-36f8-bd0e-8485cff21df9 | -21.8834 | -48.14268 | 2025-09-10 00:26:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a5fb9da0-e50f-30db-87e1-8cacb04440f3 | -21.31094 | -43.89561 | 2025-09-10 00:26:00 | TERRA_M-M | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 7ba38dac-3c41-37e3-b2dd-57f6b07f5e46 | -23.35851 | -47.21197 | 2025-09-10 00:26:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.2 |
| 5d579ce0-5692-3d0a-85a1-1ad151cef94c | -23.49799 | -47.20797 | 2025-09-10 00:26:00 | TERRA_M-M | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 7a16ada8-4823-3ace-9204-1ef80ae47942 | -22.11304 | -45.13477 | 2025-09-10 00:26:00 | TERRA_M-M | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 568e0e69-7f48-3372-acc6-9c034d500ebd | -22.03029 | -42.90388 | 2025-09-10 00:26:00 | TERRA_M-M | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 91c554bb-3b79-33ae-9e89-8e0952527892 | -23.14799 | -48.25719 | 2025-09-10 00:26:00 | TERRA_M-M | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| e11391a8-185a-3528-83bc-795314a488a3 | -21.31847 | -43.88421 | 2025-09-10 00:26:00 | TERRA_M-M | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |
| 0a370447-11d7-36ee-829c-482dd7589501 | -23.37744 | -47.20896 | 2025-09-10 00:26:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 995d6a45-0168-3ffa-bbef-7081bb346e39 | -21.58507 | -44.00655 | 2025-09-10 00:26:00 | TERRA_M-M | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 7d4ae18a-8f59-3e9f-b747-ff26837ce8ec | -17.58418 | -49.82045 | 2025-09-10 00:28:00 | TERRA_M-M | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f52bde13-e38d-3320-8cdd-444eb029ebe6 | -14.75156 | -45.33904 | 2025-09-10 00:28:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| f31bc9e0-f8d0-38f2-8ac8-c5c5a8b37849 | -19.21084 | -43.05501 | 2025-09-10 00:28:00 | TERRA_M-M | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| e11a50b2-688d-351d-b57a-f1d659af4004 | -15.80671 | -52.25694 | 2025-09-10 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b2bd9279-fd06-351b-9b4a-af65032aca78 | -19.51559 | -45.00417 | 2025-09-10 00:28:00 | TERRA_M-M | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1a8dae5a-b53d-35e2-8fb3-4f2a800c47b7 | -16.89699 | -48.23115 | 2025-09-10 00:28:00 | TERRA_M-M | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| db283025-123e-3de3-9ce2-6c3af4da58a7 | -17.74339 | -44.47614 | 2025-09-10 00:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a0e6d924-40cf-3bb6-9fba-073c902a25ab | -20.94366 | -45.79753 | 2025-09-10 00:28:00 | TERRA_M-M | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d1bbc2fe-2a21-3749-b70d-dbeac45e14a0 | -20.01546 | -47.62712 | 2025-09-10 00:28:00 | TERRA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 109f9bc6-3983-3aaa-87df-27f12d887945 | -17.32974 | -46.70756 | 2025-09-10 00:28:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5fd57eda-3f94-3cf1-b130-4e10709bd57c | -16.70572 | -48.54447 | 2025-09-10 00:28:00 | TERRA_M-M | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e24834b4-918f-3f2e-bd8c-9d908ffd014f | -18.01094 | -47.12056 | 2025-09-10 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 191c71d2-1e74-3c9d-89c7-798b15e4e6de | -16.46834 | -50.67719 | 2025-09-10 00:28:00 | TERRA_M-M | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| aa8963c0-c3d5-327c-a588-fbd4980aa21c | -20.94366 | -46.28178 | 2025-09-10 00:28:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| a90fbe65-e8d5-3cb3-a1d3-8eea698ca3da | -18.14334 | -51.72607 | 2025-09-10 00:28:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 94cea109-7e70-3c02-aa57-0bfbb1fbf711 | -17.56015 | -44.54785 | 2025-09-10 00:28:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c28e6e1b-2f01-3759-8c77-bfacaa98f027 | -15.89162 | -51.81606 | 2025-09-10 00:28:00 | TERRA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 8497ae8b-8bd7-3bd6-a951-f3de39791b75 | -15.22567 | -44.03574 | 2025-09-10 00:28:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 50a7a68d-0f17-3492-8f2f-fad89aff8001 | -20.91912 | -45.89507 | 2025-09-10 00:28:00 | TERRA_M-M | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cc72707f-be69-3ab4-ac39-c0b8f228f3db | -16.29432 | -45.68687 | 2025-09-10 00:28:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e7686076-bd0f-35b6-9ba6-2e59c4422e3c | -15.93576 | -46.35265 | 2025-09-10 00:28:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README3.md)
