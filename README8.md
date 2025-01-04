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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ed760a6-57dc-3c11-9221-e0398c08ee8a | -10.6071 | -44.34004 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 404bcf98-cf0d-341f-bdc7-6c1c29ef2e37 | -8.5981 | -39.53999 | 2025-01-04 04:31:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9388adb-b080-35b5-bc3a-be677c267ad6 | -8.84042 | -49.90614 | 2025-01-04 04:31:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84217248-65db-3201-bb49-95b4fddfd25d | -12.71568 | -47.6278 | 2025-01-04 04:31:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bd58f37-0412-3aaf-97b2-d2ee6d299456 | -9.84471 | -37.12269 | 2025-01-04 04:31:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3a92a402-1808-3ff8-a485-fa0b8e9360cb | -9.98325 | -36.39238 | 2025-01-04 04:31:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 77e2a524-a81a-3c07-80f1-5b4e11d6ebb3 | -10.60782 | -44.33516 | 2025-01-04 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 193e8c40-b7ee-38f2-91e7-82125f3ddd89 | -12.46656 | -46.93829 | 2025-01-04 04:31:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 96c23dcd-e270-3a49-a5f0-42db83478d85 | -10.54506 | -44.6828 | 2025-01-04 04:31:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8fad9dc0-dfce-3b3b-b2a5-3121dfe23a6e | -12.46714 | -46.9344 | 2025-01-04 04:31:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a70d7fd5-f421-3b51-a47b-351849ce0574 | -12.26898 | -44.98499 | 2025-01-04 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4304b47-de9b-3e02-a0b0-fdd1476f3eef | -22.67508 | -42.85289 | 2025-01-04 04:33:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 34eb9117-4d5f-3d4a-a6f2-daab27b03846 | -22.67476 | -42.85598 | 2025-01-04 04:33:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a8ca39d9-3900-3a36-ba46-6e0d6ecf64af | -22.53934 | -48.81123 | 2025-01-04 04:33:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca98cc28-c404-3abc-bf72-54c1fb38655c | -24.54063 | -51.63628 | 2025-01-04 04:36:00 | NOAA-20 | MANOEL RIBAS | PARANÁ | Brasil | 4114500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d2daa3c3-4f1b-3c79-b48d-d5063c2ffd89 | -27.62625 | -50.20835 | 2025-01-04 04:36:00 | NOAA-20 | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a0a16e2b-1df9-39d8-a678-7a8c1874ddc7 | -27.7823 | -54.34621 | 2025-01-04 04:36:00 | NOAA-20 | TRÊS DE MAIO | RIO GRANDE DO SUL | Brasil | 4321808 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 87c4d52a-b10a-3330-b733-a2f4cebd42c4 | -24.14019 | -52.85884 | 2025-01-04 04:36:00 | NOAA-20 | JANIÓPOLIS | PARANÁ | Brasil | 4112207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5fdba13b-1667-3e90-aaf0-be206847de52 | -24.13957 | -52.86265 | 2025-01-04 04:36:00 | NOAA-20 | JANIÓPOLIS | PARANÁ | Brasil | 4112207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1a4e68e8-e44c-3c00-abe0-169ca0ce342a | -27.62566 | -50.21274 | 2025-01-04 04:36:00 | NOAA-20 | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6d214b0e-854b-38e6-8297-2fb9673675e9 | -28.2276 | -52.36435 | 2025-01-04 04:36:00 | NOAA-20 | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 816eeb30-ff8f-3d10-9658-3c5a518eecae | -24.24217 | -50.74089 | 2025-01-04 04:36:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 39e5d7b4-6912-3ad1-a4aa-7a47aaffc38c | -28.22427 | -52.36371 | 2025-01-04 04:36:00 | NOAA-20 | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bfe7bc1c-d35c-3196-90b5-8662b210cc06 | -23.98323 | -48.91923 | 2025-01-04 04:36:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ad7fe0f-26e4-31d7-81ea-febbc6b67a21 | -25.5674 | -49.36649 | 2025-01-04 04:36:00 | NOAA-20 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9da70ad3-de17-3956-91f7-cc4e0d407e1a | -29.60813 | -51.99356 | 2025-01-04 04:38:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 737f7f96-cf65-3968-a3e0-bec515677ec8 | -30.72922 | -53.33313 | 2025-01-04 04:38:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 04949def-b1e0-3022-b384-bf10a51093b5 | -31.64783 | -52.41019 | 2025-01-04 04:38:00 | NOAA-20 | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 5fa33d47-d044-36af-abcf-e7d33193922d | 1.34 | -60.3122 | 2025-01-04 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 00d646c8-ea97-346d-a876-239da1741cee | -10.6128 | -44.3284 | 2025-01-04 04:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 65f0420d-0397-35f0-894e-67bcf3c58371 | -10.6124 | -44.3517 | 2025-01-04 04:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 63fc89ef-31b1-3736-bc8f-0be29cf9104e | 1.3401 | -60.2932 | 2025-01-04 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9661693f-38cc-341f-a9da-e56f7567a883 | 1.3401 | -60.2932 | 2025-01-04 04:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 629f8eec-c63d-3826-bbfa-fbab43f7e022 | -10.6319 | -44.3257 | 2025-01-04 04:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 4a34b010-80f8-3d40-abb2-7f1242a30905 | -10.6124 | -44.3517 | 2025-01-04 04:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 064cd55c-ead8-3e66-b143-2e4cdb61846a | 1.34 | -60.3122 | 2025-01-04 04:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 65e2572b-cddf-3480-8b78-62da64a891d2 | -10.6128 | -44.3284 | 2025-01-04 04:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| d32ce596-2ed1-36da-8b3d-bbaa4ffaa907 | -9.89635 | -36.26776 | 2025-01-04 04:57:00 | AQUA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 44.4 |
| d139e045-b6f4-3723-9bb8-49130eb01e16 | -9.84825 | -37.12076 | 2025-01-04 04:57:00 | AQUA_M-M | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 36.3 |
| a66d39f6-f80a-38ca-9ea6-1c12bfd0525b | -9.89793 | -36.25652 | 2025-01-04 04:57:00 | AQUA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 35.0 |
| 478bda43-b37a-33fe-82cc-7e5333706eaa | -6.98341 | -40.00097 | 2025-01-04 04:57:00 | AQUA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| aa6bd692-ddea-3cb8-9ed4-b224ad94cce3 | -6.79729 | -35.18297 | 2025-01-04 04:57:00 | AQUA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 032e29be-1e78-3c16-8033-58ff692a2acc | -6.98199 | -40.01014 | 2025-01-04 04:57:00 | AQUA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 5ea9b13c-18ef-3fbc-8be0-2421e3b8fa37 | -10.61752 | -44.33067 | 2025-01-04 04:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e7d03ac9-62b9-3e35-bc4b-965dbadef1e8 | -10.61507 | -44.34572 | 2025-01-04 04:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 58573579-23ee-354d-ad12-de54df74d403 | -10.60633 | -44.32873 | 2025-01-04 04:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| aad5c264-fa8f-3e9b-83fa-f3d6431db7a6 | -10.60386 | -44.34381 | 2025-01-04 04:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 025e752a-c85c-32b2-8505-6e7b0e7860f1 | -10.6124 | -44.3517 | 2025-01-04 05:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a75ecddb-c624-3fd0-9f21-21c1afe5d3d1 | 1.3401 | -60.2932 | 2025-01-04 05:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 64178d35-6e8d-3b64-8290-c5f0a10efe11 | -10.6128 | -44.3284 | 2025-01-04 05:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 71dcfe5f-2abe-341b-ae07-be663862aa79 | 1.34 | -60.3122 | 2025-01-04 05:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 2cbcfe9b-ab92-3d4a-81a7-44fef0b0a8ac | 1.3401 | -60.2932 | 2025-01-04 05:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b9f544ce-9a9a-3d60-9d83-92e39a9924b3 | -10.6128 | -44.3284 | 2025-01-04 05:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| b96ec57d-15d9-3f1c-9fd2-8ecbb44b5b21 | 1.34 | -60.3122 | 2025-01-04 05:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 2a4f2aff-87e3-32e2-bd1b-085d6631cf93 | -10.6124 | -44.3517 | 2025-01-04 05:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1f4e6799-4903-3fe1-b873-bca55eac24bb | -10.6319 | -44.3257 | 2025-01-04 05:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 4a345aca-f688-3521-b656-c073b4bfb240 | 1.3401 | -60.2932 | 2025-01-04 05:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| c93420c2-0fa8-3267-9ca0-2028ad285bfd | -10.6319 | -44.3257 | 2025-01-04 05:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| ba2d1a70-d1bd-3889-ba72-a942defc0dae | 1.34 | -60.3122 | 2025-01-04 05:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 26f9f980-d9b6-3858-bc82-9dbfcde658cc | -10.6128 | -44.3284 | 2025-01-04 05:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 620c544a-5055-3fa6-8ffd-c89b03548c68 | -10.6124 | -44.3517 | 2025-01-04 05:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0bfd0c2b-7dd0-365f-8fbd-8adf6287e1d8 | 3.76771 | -60.30978 | 2025-01-04 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c81541af-f35c-34a4-8308-54608d73d43c | 1.8852 | -60.48237 | 2025-01-04 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92528130-6ced-3b0e-b46e-ec5d6da28b77 | 1.34153 | -60.30795 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| b43887bf-6a44-32b6-9f78-c2c5b816a468 | 3.76089 | -60.31082 | 2025-01-04 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3c124ec-c5cb-3d15-90e5-464d67a0cfd8 | -2.81964 | -54.71678 | 2025-01-04 05:22:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d984e6b-c1b7-3570-975d-e963626cb6fb | 1.32252 | -60.70581 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c17f6579-5dc7-370f-b5ee-535c831b9bec | 3.50677 | -60.36826 | 2025-01-04 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8ce16ec-6920-3902-8da7-4eaa86582486 | -8.83978 | -49.90518 | 2025-01-04 05:22:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e4f28e0-6da2-374e-aa69-1c36865d7ca6 | -8.84038 | -49.90041 | 2025-01-04 05:22:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b158f28b-28e9-3d80-8f39-5c9ae2b6be79 | -1.39115 | -55.20985 | 2025-01-04 05:22:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc5579d3-28c5-3aee-b8d4-68f50b32cb45 | 3.99973 | -60.10524 | 2025-01-04 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8decda55-4bc7-3e72-815e-76250cb1b572 | 3.50385 | -60.64763 | 2025-01-04 05:22:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a7f815f-ce0f-3233-a04e-c6a1e9671a07 | 1.54289 | -60.37985 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa46e7b2-39c7-32bf-8032-923709fb7617 | 1.34825 | -60.30694 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 177578e3-4e50-3556-ad08-6c83f5a8b60c | 3.68725 | -60.0377 | 2025-01-04 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6283c731-28d0-39fc-9707-d078bbcf92f5 | 2.42747 | -60.65144 | 2025-01-04 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d19e55aa-fee1-38d9-b2f0-3281b5cf945d | 1.61939 | -60.32725 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f4687ec-51b9-38f8-81bf-4097f7b2e974 | 1.34098 | -60.3044 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1be31f62-1d9a-3705-b86e-fde91017875a | 1.61658 | -60.33134 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 485fb233-1d89-3b85-8139-b37fbc9881aa | 1.31912 | -60.70633 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4634ff04-84c2-30fe-bbf3-ee12dd07cb3a | 1.33482 | -60.30899 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4a6e2e5b-f071-341f-a942-75b2e6c11e83 | 1.53952 | -60.38036 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94048fe8-98d7-3296-8060-8f776a0db7aa | 1.33817 | -60.30847 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 6dd98b30-173c-3740-a84f-49631cda3b53 | 1.54008 | -60.38395 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71c4003f-b53b-3090-b546-3c1632dd18d5 | 1.33706 | -60.30136 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1fd290bf-356f-3298-bae2-a6abe11260ce | 4.20467 | -60.38844 | 2025-01-04 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c9d9e48-2b04-356b-ab73-15b3edc8134c | 3.79024 | -60.40918 | 2025-01-04 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0eca048-62d3-3dbb-99da-7d39366f2473 | 1.34489 | -60.30744 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 00f74e8b-96a1-356d-962d-241bab80f8ff | 3.99918 | -60.10165 | 2025-01-04 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b28aed94-dc95-3f24-9659-b861ca7560ee | 3.50098 | -60.65193 | 2025-01-04 05:22:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb00dd46-6569-368c-bdbc-7be7d75b1fb2 | 1.34433 | -60.30389 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 39bbece5-8c9c-3544-bf20-391a2f5dd3b9 | -1.90748 | -53.30217 | 2025-01-04 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5754ae19-36f7-3dcf-9d4b-c9cfcf5526bf | 4.20527 | -60.39231 | 2025-01-04 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e121c75f-48f4-342f-b5f0-224ead64f814 | 1.34378 | -60.30033 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 837021c5-2f3e-3fdb-aafd-3304fbdbb575 | 1.61995 | -60.33082 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 447471de-7a9c-38ec-9605-6a80b5ce6cab | 1.34042 | -60.30084 | 2025-01-04 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ba9d3dab-b483-3243-ac32-bd37844c3fa2 | -4.2399 | -53.49177 | 2025-01-04 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53c96337-a362-3e40-91f6-1e2198a3bc8e | -4.23706 | -53.49318 | 2025-01-04 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c149a00-5767-3c6d-80d2-a4ec17ea4de1 | -11.79965 | -49.32635 | 2025-01-04 05:25:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README9.md)
