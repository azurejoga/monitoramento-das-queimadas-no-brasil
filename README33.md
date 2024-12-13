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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 347bf1a0-c1ee-3676-8618-05849ee5e8ec | -3.19871 | -43.45679 | 2024-12-13 12:42:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a3b31973-e203-3781-98df-a2e6b178cee8 | -3.14177 | -48.59945 | 2024-12-13 12:42:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f1802cc1-3dd8-3894-a0f1-c1ba8a4994a3 | -4.38843 | -43.11316 | 2024-12-13 12:42:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| cab8bc97-8953-36c5-a0eb-5b61c3c8b1a9 | -4.66522 | -42.83928 | 2024-12-13 12:42:00 | TERRA_M-T | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 39.8 |
| d030e3f2-9fe8-37ce-ba98-21c50a820f3a | -7.05412 | -39.70004 | 2024-12-13 12:42:00 | TERRA_M-T | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 0ddbff8f-5e6b-35de-ac63-a8c9d53cd0bb | -4.17251 | -40.42448 | 2024-12-13 12:42:00 | TERRA_M-T | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| e7371087-d56a-396c-9b49-233e48c211e9 | -1.66464 | -45.67207 | 2024-12-13 12:42:00 | TERRA_M-T | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 221070bd-b878-381d-bbef-0f0d561be28f | -1.52725 | -45.40788 | 2024-12-13 12:42:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| a6e97a47-5867-3338-b53f-b70f9f9f1e9a | -2.83388 | -43.86613 | 2024-12-13 12:42:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f16d771b-21a7-373a-ac99-4a5e0fbe6ad0 | -1.38637 | -47.14806 | 2024-12-13 12:42:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 333f160e-7409-3e25-83e5-ebe438e0564a | -5.23702 | -43.1159 | 2024-12-13 12:42:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 47440ea4-409b-3b14-81a4-b73bb71c26c7 | -2.73261 | -45.23528 | 2024-12-13 12:42:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1e0ad15a-44c0-3e54-bf8c-b7e925ee1e23 | -2.34211 | -45.70741 | 2024-12-13 12:42:00 | TERRA_M-T | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e30090de-148a-3075-8e8a-1698320b71e1 | -5.22771 | -43.18456 | 2024-12-13 12:42:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 6caa9669-48db-3eee-8f43-1dd086d5b105 | -1.77467 | -45.29064 | 2024-12-13 12:42:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 84651ff0-7c25-3a73-a00d-be8869b04755 | -1.72486 | -46.53493 | 2024-12-13 12:42:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6fc90021-5024-3759-85ed-bc2c88234028 | -6.13224 | -47.26658 | 2024-12-13 12:42:00 | TERRA_M-T | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a9d7eda7-f09e-3cd5-b14d-3f86fea6963d | -3.45602 | -41.62744 | 2024-12-13 12:42:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 85f28007-e80b-337c-9048-897ae76a1517 | -4.41281 | -44.63981 | 2024-12-13 12:42:00 | TERRA_M-T | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f2ed58ad-b810-3dbf-ab11-b3a7c52d5fe9 | -1.39595 | -45.61581 | 2024-12-13 12:42:00 | TERRA_M-T | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| c4c3e09d-5a6d-33ff-9444-5a344ee0b2f1 | -3.29554 | -43.11902 | 2024-12-13 12:42:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 84cf5104-0acd-32fb-9621-9e6ce6182bb8 | -4.67624 | -42.84085 | 2024-12-13 12:42:00 | TERRA_M-T | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2240806d-b9b6-3e28-87ba-c3d36dea222d | -4.2207 | -44.26851 | 2024-12-13 12:42:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 98b8f176-51a5-3274-a8c5-dc4ca9a3f33b | -5.71232 | -43.67682 | 2024-12-13 12:42:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 05b75cc1-271e-352c-ae0a-b19df15768cd | -3.10556 | -45.27256 | 2024-12-13 12:42:00 | TERRA_M-T | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| bc25cb31-e953-36a8-bc5a-6237007a99be | -6.90654 | -47.53083 | 2024-12-13 12:42:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 454f61b0-5fd1-3d4e-9403-457865fc14f9 | -1.39465 | -45.62486 | 2024-12-13 12:42:00 | TERRA_M-T | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 669b650c-477c-3c41-b3db-4c7d3c53ec1b | -6.92597 | -42.84081 | 2024-12-13 12:42:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 2ab6a280-4ea7-3e8b-a4d8-cd89a0a2efc8 | -2.90423 | -45.19322 | 2024-12-13 12:42:00 | TERRA_M-T | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| f31d1707-582f-3551-a1ca-918060f43007 | -1.71628 | -45.24798 | 2024-12-13 12:42:00 | TERRA_M-T | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1eed447b-fb08-3fb8-815c-17ff4fa50c2a | -2.9963 | -42.36592 | 2024-12-13 12:42:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 34c83b7b-483c-3ff1-b483-1a5f6561e048 | -5.82648 | -40.36554 | 2024-12-13 12:42:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 52.7 |
| ee440494-90c4-3118-aa97-759ac8ac1859 | -3.07229 | -42.55711 | 2024-12-13 12:42:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 616bf424-343d-319d-9a66-6b403d4e6e0a | -4.19832 | -43.62309 | 2024-12-13 12:42:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 93c8d5e3-5d74-3d3e-b1ad-c252b42d2333 | -7.81111 | -38.71207 | 2024-12-13 12:42:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 51.3 |
| 330f9db3-70a1-328c-ab84-dcfd43105ec0 | -2.83229 | -43.87743 | 2024-12-13 12:42:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b3afad4c-2878-3df1-8689-a55f29876234 | -2.34977 | -45.71777 | 2024-12-13 12:42:00 | TERRA_M-T | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| eced40c7-e30b-3ee9-8766-9cd881229b13 | -4.32021 | -42.25479 | 2024-12-13 12:42:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 9383831c-715e-30a8-b899-ceda6ea4c596 | -3.05908 | -41.00312 | 2024-12-13 12:42:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 2baa7f46-1f63-3276-a5b9-f70e29ba89cf | -5.82963 | -40.34185 | 2024-12-13 12:42:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 78f52a5f-856a-3b79-b9c4-2804ecb509c1 | -2.15452 | -46.05234 | 2024-12-13 12:42:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 91a6547f-d2e5-32d6-921f-273aa15f07b2 | -4.21852 | -44.27305 | 2024-12-13 12:42:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ecc12ed6-0635-3cf8-a2c5-3a424d7dcd7c | -1.32762 | -45.32072 | 2024-12-13 12:42:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e4d97921-bb81-3a3a-b8c4-de53e1a1c27a | -6.90781 | -47.52197 | 2024-12-13 12:42:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e0694517-e919-3c63-9e88-3c11cd9790e2 | -2.90558 | -45.1836 | 2024-12-13 12:42:00 | TERRA_M-T | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 097fa49c-7c86-3ce9-a35b-5b970cb2184d | -1.62265 | -46.66615 | 2024-12-13 12:42:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bcfd941e-ed66-315c-94d4-b0de46dccb32 | -1.76394 | -45.43105 | 2024-12-13 12:42:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e77f4e5a-e41d-3645-b793-de285aa79d64 | -3.07429 | -42.54313 | 2024-12-13 12:42:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| ec7d7575-6a9e-3390-ab61-49ff303898bf | -5.83584 | -40.34915 | 2024-12-13 12:42:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 41.4 |
| 70d450dc-d5f4-3a10-ae05-6d5596999a7c | -7.05431 | -39.69323 | 2024-12-13 12:42:00 | TERRA_M-T | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 50.4 |
| 2ac8291f-f667-3b0d-bc17-6ebea6681fbc | -5.21458 | -44.10393 | 2024-12-13 12:42:00 | TERRA_M-T | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d0b2272d-242a-34f2-833c-ccc200cc045e | -2.03491 | -45.59984 | 2024-12-13 12:42:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 48244704-a510-3b94-8d58-39709e1dbbd5 | -3.69713 | -42.04236 | 2024-12-13 12:42:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| b6b7f9b7-1d9b-3b25-99f4-e1415ee8b5ed | -1.776 | -45.28131 | 2024-12-13 12:42:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| ffb4072c-8188-32df-860d-7a4329be47fc | -2.72344 | -45.23399 | 2024-12-13 12:42:00 | TERRA_M-T | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| eb65d5b0-c76f-346e-9bb3-142545a77ea8 | -5.21303 | -43.29263 | 2024-12-13 12:42:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f9476708-45f0-3303-b9b1-5dd7f597ec48 | -6.93742 | -42.84231 | 2024-12-13 12:42:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| f0b3c6c5-ccaa-307f-8efa-4926a791e3bf | -4.03073 | -46.54365 | 2024-12-13 12:42:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 798ac7b7-f174-34c5-9c7b-4da7037d7875 | -4.31813 | -42.27035 | 2024-12-13 12:42:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 671f01d4-7a8c-3262-b7bc-465e3f41fd04 | -3.69399 | -42.04776 | 2024-12-13 12:42:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| a59d6504-707e-39ff-b98a-ed5c88cee360 | -3.94698 | -42.63554 | 2024-12-13 12:42:00 | TERRA_M-T | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 64c9c8b7-6996-3e56-8228-33984573795f | -4.4113 | -44.65043 | 2024-12-13 12:42:00 | TERRA_M-T | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6c4ec151-209b-33c1-a0f5-1d5ff1c803d4 | -4.18801 | -43.6217 | 2024-12-13 12:42:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 1619d33a-8456-37e8-87d3-a985fd3b6f44 | -6.42875 | -39.00609 | 2024-12-13 12:42:00 | TERRA_M-T | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 75ec9ed0-e028-3b14-b9bd-ff1abbd8233b | -3.06331 | -42.54151 | 2024-12-13 12:42:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2b47408e-20e0-3514-8606-8be0dd5bd03c | -2.914 | -48.00933 | 2024-12-13 12:42:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1e470a80-9eb6-3a4e-812b-99bf858ba6a3 | -1.76262 | -45.44027 | 2024-12-13 12:42:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e9a61501-901f-320f-8e7c-928ea1010032 | -1.90969 | -45.57007 | 2024-12-13 12:42:00 | TERRA_M-T | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 252e52d0-99a3-3f96-8e14-78c68461b671 | -4.32077 | -42.26435 | 2024-12-13 12:42:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| bbd024cf-c240-354f-992d-6063d008f790 | -3.04661 | -41.00138 | 2024-12-13 12:42:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 31.8 |
| f711a6a5-cba2-346a-83d6-6427d34c8f31 | -9.14054 | -49.4866 | 2024-12-13 12:44:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6ada2c97-4c47-344e-8ae9-2e723ff3d920 | -12.0544 | -46.89334 | 2024-12-13 12:44:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 375d5e8a-64a5-3c06-85d3-6fd5925673cc | -9.16881 | -49.48137 | 2024-12-13 12:44:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6b9907da-d762-3f05-b103-498508a5281c | -9.64227 | -48.5191 | 2024-12-13 12:44:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e1fea11-70f8-3da9-b276-eb86e5947a3d | -8.66904 | -44.15524 | 2024-12-13 12:44:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 70c8757e-0aea-36ba-84ba-d58bb66cfda2 | -9.21695 | -44.42147 | 2024-12-13 12:44:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 75015d1b-b607-3799-b669-e50e7ee10a91 | -11.58047 | -41.42392 | 2024-12-13 12:44:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 37.0 |
| 334146af-29f0-3bc9-acc6-c7ee943af3f0 | -7.46519 | -47.74619 | 2024-12-13 12:44:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9a9913da-8e6f-3e85-a60f-96e32ea8934a | -9.62079 | -50.34666 | 2024-12-13 12:44:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d6ee416b-fced-3c85-8b9a-15eabbc8fd1a | -14.25928 | -43.25178 | 2024-12-13 12:44:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 465290e2-50d2-39f4-8705-c0853e71feb1 | -12.43162 | -46.64084 | 2024-12-13 12:44:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 73b72c07-7377-3cd4-a198-f5ff173291d3 | -11.20575 | -53.82702 | 2024-12-13 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 030ddfd5-a0e3-3e08-9e28-0ad55397775c | -11.88495 | -48.44351 | 2024-12-13 12:44:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| fa3804db-261a-3347-a703-9b3210f9a0e3 | -14.27177 | -43.25329 | 2024-12-13 12:44:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 72eba0d9-6e41-35d8-903a-2c985d3df6f0 | -12.66333 | -43.82329 | 2024-12-13 12:44:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 82eb82dd-d63e-3a58-a56f-ec09f0f0d226 | -9.81279 | -48.42903 | 2024-12-13 12:44:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ca5be213-e84a-3c3f-bab8-ee93fa38e93b | -10.36114 | -47.68048 | 2024-12-13 12:44:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 738a7725-b9de-3010-86d3-15cae6e0e9cf | -8.26465 | -48.02357 | 2024-12-13 12:44:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3251f6f9-fedf-3b54-8722-566f80e9b18f | -14.26769 | -43.26535 | 2024-12-13 12:44:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 0ea0fc1f-5353-30e7-8ed1-017fe15d504c | -8.57191 | -49.14576 | 2024-12-13 12:44:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1257118b-e877-3caa-b49a-e08c83aff505 | -13.3984 | -51.07497 | 2024-12-13 12:44:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4d0b8c3a-5f6c-3bba-a1d0-631ae4601421 | -12.57584 | -43.79 | 2024-12-13 12:44:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 0173022e-3324-30d4-b3df-38c2844ed43b | -14.27 | -43.24648 | 2024-12-13 12:44:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 33.1 |
| c87bd871-35b3-30a1-8069-b955d9aff848 | -11.87609 | -48.44224 | 2024-12-13 12:44:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c908715c-962f-3f1d-a7f4-0c02766c5fa7 | -12.42214 | -46.6395 | 2024-12-13 12:44:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 07f2be3c-a3be-379d-9aff-ad558d55d2ee | -9.17016 | -49.47216 | 2024-12-13 12:44:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| a0caf835-dc1a-3acf-9732-7e3b572492ab | -9.20361 | -45.35112 | 2024-12-13 12:44:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4f9fbedd-172f-3fa5-ab9f-2ba21b1fedb4 | -12.36942 | -45.66358 | 2024-12-13 12:44:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b2c76fe-64db-3d80-a7f3-706b46d9e068 | -10.46526 | -49.6442 | 2024-12-13 12:44:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4b380fba-7680-34d9-ae05-0518b7370328 | -13.37061 | -43.82727 | 2024-12-13 12:44:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |


[Clique aqui para ver as próximas entradas](README34.md)
