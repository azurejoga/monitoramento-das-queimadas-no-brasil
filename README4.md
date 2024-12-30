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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52bc3494-2020-3b43-b933-6a3ebaa17999 | 3.52451 | -60.4659 | 2024-12-30 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ef6c532-d316-311c-b3fc-8be74e9ac76a | 3.6152 | -60.6251 | 2024-12-30 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00e3613a-4e48-3093-9873-452017c3c03f | -9.13552 | -61.51757 | 2024-12-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 276f714c-e569-3d23-8ea8-8a12df348a3a | -9.92292 | -59.90113 | 2024-12-30 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e77e0609-2d23-35ee-bbc4-073d6770f8f3 | -13.13575 | -58.89072 | 2024-12-30 05:20:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 219b4709-c5a8-3947-b3af-531eb655fa3c | -12.79397 | -61.49833 | 2024-12-30 05:20:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab3ca5e7-0a41-3310-a8a2-8263b9fd8f93 | -12.7934 | -61.5019 | 2024-12-30 05:20:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35fbb0d5-febf-33e8-a665-56775cf0f92f | -15.80244 | -59.06734 | 2024-12-30 05:20:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e3e776e-62e4-33e5-8fb0-21dc02180ee0 | -13.54957 | -60.65582 | 2024-12-30 05:20:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a614300b-26dc-30ea-9c2e-e1347fa6b60f | -16.29403 | -57.69754 | 2024-12-30 05:20:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 604f6a58-3e64-3fa2-9d3d-7a63e8353115 | -12.59069 | -62.00672 | 2024-12-30 05:20:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| feb3ac75-08fb-3f97-8caf-acb9e89cce49 | -12.17323 | -63.83072 | 2024-12-30 05:20:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ca202c5-d1f5-3174-9a2f-cfd6d0124a7a | -12.59405 | -62.00729 | 2024-12-30 05:20:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96650a8e-96ce-301d-a388-a095becb8fe4 | -16.30203 | -57.6942 | 2024-12-30 05:20:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0e21215b-e665-3bba-a7f6-6582be106c65 | -16.29834 | -57.6936 | 2024-12-30 05:20:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1d9d6277-e8c0-3c3a-9ac8-e605d2328261 | -13.54902 | -60.65935 | 2024-12-30 05:20:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d92238d0-8d68-35c4-8bb2-d03c55e3e911 | -15.57697 | -57.56902 | 2024-12-30 05:20:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccb0bd42-4b92-357c-a0fb-5df85f09f5b3 | -15.09626 | -59.62884 | 2024-12-30 05:20:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d87cdec-cffc-3229-bac2-b3098a1d849a | -12.59585 | -62.00718 | 2024-12-30 05:20:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21f8601b-ba73-3a7e-b7c8-9dcad0354a69 | -9.92237 | -59.90461 | 2024-12-30 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 83be8a62-a8d4-3bef-85d7-e1f576f1d5eb | -9.934 | -59.93857 | 2024-12-30 05:20:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34417c7a-944a-3e6b-b5d8-bcbb288d2d18 | -12.17252 | -63.835 | 2024-12-30 05:20:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a8eafbe-8d5e-3eb1-8196-0526d8ac8e8f | -15.77047 | -58.93081 | 2024-12-30 05:20:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5774d141-c489-3ee2-a0fa-7eb6d483c727 | -29.6047 | -51.98926 | 2024-12-30 05:25:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 51358fb6-8272-3b31-ae58-b60ed6303be6 | 3.61095 | -60.62905 | 2024-12-30 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 67dc4a20-a991-3a41-8317-1833ed4fcf3e | 3.61448 | -60.62849 | 2024-12-30 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00094658-c105-385a-b788-59a541b73011 | -12.39411 | -63.68164 | 2024-12-30 05:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b75b376e-e207-3255-a9d7-12c56f132c3d | -9.92502 | -59.90099 | 2024-12-30 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c27253d-d1ab-3e86-80d9-09a61fefaffb | -12.39692 | -63.68298 | 2024-12-30 05:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abc1c03e-a3ac-3b38-b3f4-83f0154faf5f | -12.59677 | -62.00584 | 2024-12-30 05:44:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33998129-4120-35ff-aa59-0a6caab65d59 | -12.3935 | -63.68587 | 2024-12-30 05:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aadb7b67-4592-3a2e-89f3-8d7ded527722 | -9.9206 | -59.90035 | 2024-12-30 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c885dcf4-8942-372b-b865-b3e4857dcfaa | -9.92534 | -59.90318 | 2024-12-30 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0bc4773a-7dce-3d56-8ae8-6b213234bd39 | -12.59278 | -62.0053 | 2024-12-30 05:44:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ff7e42dd-c63b-335b-ad7a-1d45de39dc9f | -9.92092 | -59.90257 | 2024-12-30 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0c5b72b4-f9be-3f15-b0a2-32cf052f0d56 | -9.92444 | -59.90526 | 2024-12-30 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dd31e0fa-3a7c-3ed5-bf2c-8d8329028390 | -12.39268 | -63.68665 | 2024-12-30 05:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb83ad09-1bf5-3276-bfbc-6ca2efed88b5 | -12.39331 | -63.68243 | 2024-12-30 05:44:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d1c5387-47f8-313e-be75-69be7d35f441 | -9.92002 | -59.90465 | 2024-12-30 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bd3db75b-b220-3b44-b162-145073e27b91 | -15.77111 | -58.9266 | 2024-12-30 05:44:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c3996e7-c9d3-3ffa-a2ac-9a4f0014a318 | -12.39103 | -63.68856 | 2024-12-30 06:07:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be483cab-3788-3fce-ab1e-48ecea9bf0f9 | -12.39427 | -63.68966 | 2024-12-30 06:07:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 805fdb20-bc08-3a65-969c-1eeb6de1d739 | -12.39146 | -63.68515 | 2024-12-30 06:07:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c4c5f6e-439b-361e-ab39-abb7066c7031 | -12.39468 | -63.68624 | 2024-12-30 06:07:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b470d40-2edc-3928-a902-764522027b8d | -12.39011 | -63.68391 | 2024-12-30 06:37:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4d0eb58-7114-3bec-8a36-13bdaf06b125 | -1.1659 | -46.69315 | 2024-12-30 12:29:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 73a6eda7-eedd-36a8-a950-68866d0d5dd4 | -1.16025 | -46.69669 | 2024-12-30 12:29:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 89178eb8-e82b-37b7-92cc-77bf87bebd2d | -1.81748 | -45.32914 | 2024-12-30 12:31:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bf6c80dc-73ea-34e2-971f-e59adb65af61 | -2.93468 | -41.21676 | 2024-12-30 12:31:00 | TERRA_M-T | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 21d07a69-8154-3909-afc6-6361970040d5 | -1.81619 | -45.33813 | 2024-12-30 12:31:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| eabd9623-f099-32dc-aa4d-1e81dfb23789 | -8.30198 | -39.45599 | 2024-12-30 12:31:00 | TERRA_M-T | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 246fb5c3-76e5-3bdc-84fc-343403f0f16f | -3.47321 | -43.31947 | 2024-12-30 12:31:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 399993e1-9053-35cc-8f4e-d7eb99595800 | -4.89486 | -40.01567 | 2024-12-30 12:31:00 | TERRA_M-T | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 3b3a69f0-7fde-3c75-8959-e5a915e9e4ba | -6.1172 | -42.37846 | 2024-12-30 12:31:00 | TERRA_M-T | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 1ed26b7b-4042-3ab2-aa0c-3ab51950460f | -2.80524 | -41.77636 | 2024-12-30 12:31:00 | TERRA_M-T | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e550bffe-0a9e-3419-b96e-32b02f78a79c | -3.3115 | -39.76872 | 2024-12-30 12:31:00 | TERRA_M-T | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 5a281f51-bdb8-3772-873b-a70f48cae7e1 | -6.1187 | -42.3674 | 2024-12-30 12:31:00 | TERRA_M-T | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c2847c62-656a-3441-98b4-cbde2502b718 | -9.33275 | -40.78059 | 2024-12-30 12:31:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 78952923-27d3-3c77-85f2-75047cdf7b63 | -2.93301 | -41.22854 | 2024-12-30 12:31:00 | TERRA_M-T | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ba0b45e0-4850-372e-beb4-cc4d7d64468d | -4.55045 | -43.71885 | 2024-12-30 12:31:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 88cdc645-c0e3-38c9-af61-f5bd478285e1 | -7.83631 | -37.60873 | 2024-12-30 12:31:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 1272654b-beda-3786-bd5d-8c2268cae518 | -3.25911 | -43.26802 | 2024-12-30 12:31:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 471b9bb0-f484-3f56-bf27-62f0174a70eb | -6.08561 | -42.6829 | 2024-12-30 12:31:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 34.9 |
| e18be79f-d872-38cb-a3b7-c9ffb46af264 | -4.90488 | -41.09993 | 2024-12-30 12:31:00 | TERRA_M-T | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d0c68cef-3a10-3b44-afa5-d23a3ab70a45 | -3.51065 | -41.99984 | 2024-12-30 12:31:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| eb73f346-899a-3404-beda-4d7d5f683ec4 | -8.16876 | -43.94113 | 2024-12-30 12:31:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 377ed222-4336-3682-90bc-15b55e213cec | -2.81349 | -41.78857 | 2024-12-30 12:31:00 | TERRA_M-T | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 077fe4b0-bc1b-3c60-a7c1-e1185f98d938 | -2.96805 | -41.83832 | 2024-12-30 12:31:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ca79ed81-ff07-3129-a62e-300ed72612ab | -3.4763 | -42.01106 | 2024-12-30 12:31:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7f2820cc-c509-379c-8d59-0227b65fa83c | -4.54915 | -43.72806 | 2024-12-30 12:31:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0b81101a-2b1d-36da-b926-d51db0940216 | -7.60703 | -35.24425 | 2024-12-30 12:31:00 | TERRA_M-T | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 28255423-873f-3cdc-94ce-21e7971b82f2 | -3.27889 | -43.51561 | 2024-12-30 12:31:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 24829d79-6974-3802-83e1-e4940bc8e4ca | -4.90996 | -41.10629 | 2024-12-30 12:31:00 | TERRA_M-T | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 6033a6df-6647-3abc-9b97-037d752be6f1 | -7.81671 | -37.90321 | 2024-12-30 12:31:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 14f739e0-fcc7-3857-add6-008f86afe735 | -2.86998 | -42.31644 | 2024-12-30 12:31:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 21534ad4-9e5b-3080-bebd-1d7bd233ef07 | -3.35369 | -41.50776 | 2024-12-30 12:31:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 99b2cc02-36fe-36b0-acdb-5fc01c40e459 | -2.8507 | -42.03979 | 2024-12-30 12:31:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| c66b7574-f172-3ed7-9cd4-cd79ce772d04 | -6.08707 | -42.67225 | 2024-12-30 12:31:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| dd4b943d-8a32-3848-83c7-245eb697cd5b | -6.5173 | -39.71289 | 2024-12-30 12:31:00 | TERRA_M-T | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 6152574c-6ea4-38b7-935d-2fe19bdf22d1 | -10.12368 | -39.39065 | 2024-12-30 12:31:00 | TERRA_M-T | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 10e87e0e-e8c4-37fe-9bc8-b861689f2c7b | -3.51215 | -41.98901 | 2024-12-30 12:31:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 78df32dd-ea81-3fdc-9b58-5fec4967d193 | -6.09365 | -40.31676 | 2024-12-30 12:31:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 19.7 |
| ff739bc5-d8a1-3108-8d07-aeee49a7462a | -3.40045 | -42.26935 | 2024-12-30 12:31:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0a69ae7d-cf95-3658-ad80-be9fc9552d43 | -8.92394 | -44.33538 | 2024-12-30 12:31:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 01f38e98-2cac-3c9d-af68-a29bddf7ff1a | -4.90826 | -41.1189 | 2024-12-30 12:31:00 | TERRA_M-T | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 28.8 |
| db10a205-4d65-3c91-8ad0-8d15f3d4b4d0 | -9.58485 | -43.33284 | 2024-12-30 12:31:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1c8491aa-b612-3e2b-98a3-29b2593347a1 | -7.86123 | -38.01157 | 2024-12-30 12:31:00 | TERRA_M-T | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 28.5 |
| d261ff65-69fb-3a6c-88af-ee6396110147 | -2.84924 | -42.0503 | 2024-12-30 12:31:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 160bd385-8798-3799-bb53-85d53a923ac2 | -9.58631 | -43.32198 | 2024-12-30 12:31:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 23fc5138-1caf-3ad7-9b4e-4ca79c3c890d | -8.67261 | -44.1558 | 2024-12-30 12:31:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9ff3b57c-4eeb-360e-90b0-07508a0ed1cb | -4.48693 | -40.64671 | 2024-12-30 12:31:00 | TERRA_M-T | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 25.5 |
| f0a3bed3-e393-3e62-872c-fdd0b19136f1 | -10.12631 | -39.36912 | 2024-12-30 12:31:00 | TERRA_M-T | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 30.0 |
| c5de4892-1325-3fee-821e-cd46e0a045f8 | -7.60748 | -35.252 | 2024-12-30 12:31:00 | TERRA_M-T | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 69f33f8c-9cb5-3227-87d5-bec188f34a13 | -2.80373 | -41.78723 | 2024-12-30 12:31:00 | TERRA_M-T | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d2cbf776-1727-3b90-ac12-4ddad2186b14 | -4.58121 | -47.07124 | 2024-12-30 12:31:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8c8cbbfd-46c8-36b4-80f0-08011375d19d | -6.96194 | -43.00303 | 2024-12-30 12:31:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 4ffc7a54-8716-3e6f-8174-741a43080f17 | -3.85952 | -42.73152 | 2024-12-30 12:31:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b7629f8d-9d67-3f9f-a342-d77a8f7a89c5 | -6.97149 | -43.00438 | 2024-12-30 12:31:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 18bbe10a-2834-3450-8c1a-1e5fee3ade2e | -6.80759 | -37.96006 | 2024-12-30 12:31:00 | TERRA_M-T | SÃO DOMINGOS | PARAÍBA | Brasil | 2513968 | 25 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 90a62ed9-969b-308a-894a-9b81ad609ef3 | -13.80962 | -41.56743 | 2024-12-30 12:33:00 | TERRA_M-T | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 27.0 |


[Clique aqui para ver as próximas entradas](README5.md)
