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

## Dados Diários - Página 206

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dae2881-4643-39c3-b882-65fcc2d4c089 | -20.86437 | -47.03107 | 2024-10-02 12:19:00 | TERRA_M-T | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 98af7c7a-d896-3e8b-9c5c-6ef4545beaa3 | -22.29038 | -48.46095 | 2024-10-02 12:19:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 850e77cf-d346-3925-b406-f817b314f555 | -22.28896 | -48.45013 | 2024-10-02 12:19:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 19.3 |
| de44b6eb-3e0e-36ae-9e52-d9b1cf4bb988 | -22.28588 | -48.46697 | 2024-10-02 12:19:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 51.5 |
| ef1737f8-3dfa-3d54-901d-7d2b78db4086 | -22.27884 | -48.45858 | 2024-10-02 12:19:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 70d492a2-f7de-3a4b-817e-1b298675cc69 | -22.27584 | -48.47564 | 2024-10-02 12:19:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c9d604df-0b49-365e-a944-9c58ea773dc1 | -22.27434 | -48.46456 | 2024-10-02 12:19:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 35dc4b44-c006-36cc-b2f1-5b6659830bb8 | -22.11494 | -48.4549 | 2024-10-02 12:19:00 | TERRA_M-T | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 3b8db6b2-021d-387c-8889-cee0edbf2881 | -21.89334 | -48.47876 | 2024-10-02 12:19:00 | TERRA_M-T | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 81f65ad0-b258-3ea1-aa61-95b7c681bc41 | -21.55224 | -47.78566 | 2024-10-02 12:19:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 88873259-5196-323e-930f-4e701e28823e | -21.29244 | -47.61847 | 2024-10-02 12:19:00 | TERRA_M-T | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a93b07be-5319-328f-9ece-c6c58de31e86 | -22.53569 | -48.1752 | 2024-10-02 12:19:00 | TERRA_M-T | SANTA MARIA DA SERRA | SÃO PAULO | Brasil | 3547007 | 35 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b4fe45c1-c40b-3cbc-bfcb-35d0efa10b56 | -22.53285 | -48.19102 | 2024-10-02 12:19:00 | TERRA_M-T | SANTA MARIA DA SERRA | SÃO PAULO | Brasil | 3547007 | 35 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 222be82f-1219-3613-9ef7-627240d8ccac | -23.81801 | -47.64271 | 2024-10-02 12:19:00 | TERRA_M-T | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| c89f2d95-4de4-3cbb-8550-1b241c07f76f | -23.81376 | -47.63321 | 2024-10-02 12:19:00 | TERRA_M-T | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| 03dc230d-9914-3e05-b499-a1a8888669c0 | -23.81123 | -47.64751 | 2024-10-02 12:19:00 | TERRA_M-T | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.1 |
| e00cdf5b-0f44-3619-b5b1-3ffce84bde24 | -22.77381 | -46.81478 | 2024-10-02 12:19:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 8e77295f-de9d-3d98-bcd5-449368056ed0 | -21.63347 | -50.81454 | 2024-10-02 12:19:00 | TERRA_M-T | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.4 |
| 9c96eeaa-ab07-364e-825c-47bd9d8dacc6 | -21.61957 | -50.81144 | 2024-10-02 12:19:00 | TERRA_M-T | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.0 |
| 705949d8-4f98-3b41-9007-e32c981a1b7d | -22.78183 | -46.82968 | 2024-10-02 12:19:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| ae8c9ab3-75d5-36a7-b2cc-8077bc0c9814 | -23.24552 | -46.64296 | 2024-10-02 12:19:00 | TERRA_M-T | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| edaaf27e-e37a-3cdb-a16f-7d909eab626b | -21.12139 | -45.3126 | 2024-10-02 12:19:00 | TERRA_M-T | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 174b4dc2-5ade-3874-ab6c-91eabb3ace65 | -21.59421 | -46.38148 | 2024-10-02 12:19:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| adbcaa22-2ac6-3a2f-a416-19c044453e19 | -23.09265 | -46.38512 | 2024-10-02 12:19:00 | TERRA_M-T | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 5a1abafd-6b36-3232-a35f-b52d75016643 | -21.12314 | -45.30162 | 2024-10-02 12:19:00 | TERRA_M-T | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 3505b539-bae6-3c06-843b-a2782beee392 | -23.28396 | -46.65677 | 2024-10-02 12:19:00 | TERRA_M-T | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 90226e85-5414-3a9d-8ea4-e5ebaa9fee3f | -21.35748 | -46.62875 | 2024-10-02 12:19:00 | TERRA_M-T | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| a9f01bbd-f9c4-3a0c-b389-fc12de17d049 | -23.35727 | -47.02108 | 2024-10-02 12:19:00 | TERRA_M-T | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 8aa9651a-c37c-3fb5-aeac-676a62e1452c | -21.6258 | -46.43251 | 2024-10-02 12:19:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| ab240d30-132d-3499-99eb-0378fec3506e | -20.21761 | -45.69893 | 2024-10-02 12:19:00 | TERRA_M-T | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d714bb73-36c7-3cbf-97d7-466adbf4a5a6 | -20.21954 | -45.68709 | 2024-10-02 12:19:00 | TERRA_M-T | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3069791b-f687-3d96-be69-a588a578398d | -20.37544 | -46.29547 | 2024-10-02 12:19:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 9392dfc0-10b7-33b5-9dd8-2b8636183136 | -20.37759 | -46.28265 | 2024-10-02 12:19:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 33.3 |
| ecd823cc-2fac-343d-9daf-479d3f144be6 | -20.42371 | -46.06911 | 2024-10-02 12:19:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 17d83c2c-e4a5-3383-aa4f-92944e520bfb | -20.42577 | -46.05667 | 2024-10-02 12:19:00 | TERRA_M-T | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 179.9 |
| dddccd43-9ade-3b6e-b35c-087e9c359027 | -20.51345 | -46.33949 | 2024-10-02 12:19:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2dbe255b-8542-3b91-a618-faae9c5bd555 | -20.51559 | -46.3265 | 2024-10-02 12:19:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 012acbd0-0396-33c5-8cef-8da8b42cab75 | -20.52398 | -46.27539 | 2024-10-02 12:19:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1c615828-52ac-336f-b62e-7520c95dd91c | -23.51319 | -47.23492 | 2024-10-02 12:19:00 | TERRA_M-T | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 7f991dd6-c690-3a1f-a168-9d40d8682dfd | -20.53071 | -46.28268 | 2024-10-02 12:19:00 | TERRA_M-T | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ef2e219b-74cd-3ccf-a384-8988af760beb | -23.03944 | -46.88531 | 2024-10-02 12:19:00 | TERRA_M-T | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| fbc71f8b-4452-379f-9db3-e3b680118679 | -22.78412 | -46.81615 | 2024-10-02 12:19:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| 3702017a-ac72-3de9-b5e1-085251ecc6b0 | -22.76 | -43.78 | 2024-10-02 13:03:14 | MSG-03 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2501563-226b-3a5a-9423-dd5449641204 | -16.61 | -57.24 | 2024-10-02 13:03:51 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aed53c8f-a61d-3b35-b655-4e3c6b305e80 | -16.64 | -57.26 | 2024-10-02 13:03:51 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a5402f7-d604-3cf9-aa1b-e2b8408006b9 | -12.16 | -50.08 | 2024-10-02 13:04:14 | MSG-03 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abf10486-24ef-3f39-8e84-b71cadeb9191 | -10.69 | -46.16 | 2024-10-02 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a76e056-a5b3-351a-b730-3586c47b4a2a | -8.18 | -43.72 | 2024-10-02 13:04:38 | MSG-03 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 48ef4d79-50bd-3e53-b918-5958fcb42726 | -8.17 | -43.67 | 2024-10-02 13:04:38 | MSG-03 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 162f3b12-d71e-3c48-bfd5-759eec24b548 | -12.86 | -62.44 | 2024-10-02 14:04:14 | MSG-03 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f3020a58-c26f-393c-9bba-f908636f3064 | -10.95 | -47.31 | 2024-10-02 14:04:21 | MSG-03 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e711a0a-7081-3430-a7f8-6ef3f18e3628 | -8.99 | -45.25 | 2024-10-02 14:04:35 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b009be1-1a95-321e-a444-8df273a01353 | -3.38 | -54.15 | 2024-10-02 14:05:09 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87987356-9510-3038-840b-702b3179b2c7 | -3.38 | -54.08 | 2024-10-02 14:05:09 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


