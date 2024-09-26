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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32933db3-f26e-3b96-8806-9a14a5c634a3 | -10.45836 | -57.65659 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a8ce688-3c9b-3461-86bc-64f73e51e265 | -10.45551 | -57.65205 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 465cdd16-6cc7-37b2-917f-7f1b8acf7afa | -10.45331 | -57.6436 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77ba9c94-e2a5-3b0b-9f61-0c022876726c | -10.45202 | -57.65147 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b96be1e8-b2cc-34de-859d-26bd2edaabd2 | -10.41833 | -57.50884 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03572dfe-d86e-3bda-96fa-7e317a2387fd | -10.4177 | -57.57705 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f0d9859-b71b-341e-8748-cd8a443db649 | -10.37541 | -57.60707 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0781ac0-5f2e-3123-beba-d6a6c2f5fabf | -10.31946 | -58.09827 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b2aa047-dcd8-3749-92c6-7376204a9b0c | -10.29538 | -58.09544 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ce23611-f20f-34a9-969c-f02e03804a58 | -10.14084 | -58.08265 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e61122ee-97ae-3e8c-8d94-4635872aacc4 | -10.45808 | -56.92609 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6628b008-b37c-3d12-90c0-df0e0837416b | -10.45747 | -56.92981 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3d4baddd-f337-3713-9e06-7a7a6a420792 | -10.45467 | -56.92554 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19305fa2-c35b-3e91-a313-4f9cc4e6d604 | -10.45407 | -56.92925 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b753635-8794-3a43-9e03-79886c720a06 | -10.33316 | -57.2851 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b79e88f1-dd4f-3e82-bb11-afeaafebc23c | -10.33254 | -57.28893 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78f0bad7-ccfd-342b-a75e-5d0f846634e1 | -10.33192 | -57.29276 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecdf63d4-0bc7-3f3a-9667-f103d74c42c8 | -10.3313 | -57.29659 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bff4d1cc-ee31-32ea-953c-c7407396f82c | -10.32909 | -57.28833 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c14ddad0-14e1-3ef4-875a-4960be6badac | -10.32785 | -57.29598 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fafd28c-e586-3f17-88c4-7a58a800a6e1 | -10.32723 | -57.2998 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02a6b279-f40e-3d36-b0d0-74bc5dfc9697 | -10.32662 | -57.30359 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 824c92d1-79b0-3807-9fa2-33126e52607c | -10.3238 | -57.29912 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bb8e5d7-b94b-3cca-b0d5-a1cb1ce70781 | -10.32364 | -56.8046 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49fc3e63-cae7-32a9-8eaa-11fd9762151e | -10.32086 | -56.80035 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5e69188-d173-3596-a6e6-c5e59d5137b2 | -10.30653 | -57.25289 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d9f168b-0122-3a75-98c5-ce90df8ac257 | -10.30591 | -57.25668 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a675a59-5bf3-3348-98ec-2859b9cdbf68 | -10.30309 | -57.25233 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e48f7bdb-a168-3e7d-b0f3-eb8c9d11f33c | -10.30247 | -57.25612 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1e3dfa0-c430-3d5d-ad72-413f678df36c | -10.30219 | -57.27954 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4131630-75eb-3157-8400-6d85ae4529ac | -10.30123 | -57.26372 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe4f6a66-e121-3aef-8fd4-d7cfa483a58b | -10.3006 | -57.26753 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8415d0af-6230-38a5-9279-b4c6dba0d054 | -10.29998 | -57.27135 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0ab4a89e-060b-34e7-bdc2-97e4550fc291 | -10.29936 | -57.27517 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 050db572-1508-3eff-83ec-2b6f84caf5dc | -10.29653 | -57.27081 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb646691-4cb0-380c-a637-04225fb166bb | -10.29591 | -57.27463 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c710a76-75c3-38c0-965b-e5586c803d04 | -10.2937 | -57.26645 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf3ffc70-1cfb-3509-a0d7-e60efc2a9098 | -10.29308 | -57.27026 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff00e617-0dab-3956-82bc-541a07c2af7e | -10.29245 | -57.27409 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b732df08-0da4-3a9c-8938-e5ac6d901972 | -10.29088 | -57.26208 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9536a631-8a01-3e8d-902f-4adcb6f90da7 | -10.27463 | -56.84263 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6d6bbf2-b792-3e35-b828-7ab86872392e | -10.27403 | -56.84634 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a664c455-ada1-3ca2-83b0-bcece81f6b1e | -10.27343 | -56.85009 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 972e5f00-d3fd-3eff-8eaf-65f0361fedd2 | -10.27123 | -56.84209 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 835b1f40-ac15-3c4e-9197-813a3466531f | -10.27063 | -56.84579 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7132538-95c7-3c72-9064-8bc5f5260c69 | -10.27003 | -56.84953 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d633567-bd8f-3cb5-b5c0-03543d831798 | -10.34945 | -56.77446 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12047f2c-266f-37f1-977a-bde5ec5f3814 | -10.34606 | -56.77391 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46964f82-ef91-3a35-b45e-005f26494680 | -10.32327 | -56.78561 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 378cde40-02ad-3731-9fe1-74d0d2456be0 | -10.31988 | -56.78505 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01a869c5-8ec4-3a64-a6ed-f738be1ccb9b | -10.31927 | -56.78875 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9230d344-3d27-3284-8502-b508d68f312c | -10.31674 | -56.76173 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f01f0aa5-acf8-3d45-8b84-ea0b963b905e | -10.31614 | -56.7654 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 645d4ef6-5e86-3545-a5e7-9aa395831a38 | -10.31589 | -56.78815 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07ff9049-3bcc-36e3-b19d-a7cdfb481fdb | -10.31554 | -56.76909 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95c1c57c-9589-3f7d-960b-541e08fe1b55 | -10.31528 | -56.79187 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 472f2086-1cba-3f8b-9f81-00a35fea4479 | -10.31493 | -56.77279 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd4f9519-93b2-38a4-bd7f-799eccf39f2d | -10.3125 | -56.78757 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c1a518c-f200-3b44-aae8-d6d194fcf976 | -10.31215 | -56.76855 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1787af54-3e27-33f6-87cc-bc4695ad0d59 | -10.31189 | -56.7913 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c0056e45-1f90-32c8-97da-8455899d8108 | -10.31154 | -56.77224 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de2bb7b4-8670-315d-8636-b9a13d3ecd21 | -10.31093 | -56.77596 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9302d65-884f-3854-903b-94186c8c4f96 | -10.31091 | -56.76873 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44ee07d4-f3f1-3f3f-95c5-5693ffae2e42 | -10.31032 | -56.77243 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d67ce52-7d2a-3d57-b2c0-308891b6ad99 | -10.30972 | -56.77615 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0d32835-8e63-394d-b86a-bdd222f91c09 | -10.30911 | -56.78704 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 847a059f-c85d-3f3d-9570-d7dc902ce16c | -9.56534 | -57.54535 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15359536-6ceb-3001-9327-5a9fb78b9248 | -9.56184 | -57.54473 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 46f33df7-5ee4-3bb4-9e76-fcd023238174 | -9.56117 | -57.54874 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e714c162-3fc5-3d71-a52f-462579fc410a | -9.45127 | -57.21823 | 2024-09-26 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b21c037-b042-3103-af21-f8c65320a56b | -9.42392 | -58.0514 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8f7d757-726f-3185-92c3-979415570380 | -11.35858 | -58.32109 | 2024-09-26 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e5e84a6-1d33-38db-8472-d23c94b35290 | -11.35571 | -58.31631 | 2024-09-26 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e0b3d4e-57bc-3305-aea5-93d70a51e484 | -11.35502 | -58.32048 | 2024-09-26 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e604ab4-cbe1-38a2-8921-ffff43657ad6 | -11.34651 | -58.32758 | 2024-09-26 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14a3f474-1c61-369e-907b-10e76df7e2af | -11.28872 | -57.52016 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 50ad60f1-6044-3a47-8461-82c4ac724cc5 | -10.90727 | -57.42567 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d2b5384-6963-36e3-8b35-aad05d56361a | -10.90601 | -57.4333 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca9f5233-4aa8-3690-9b44-e6242774c3ed | -10.90447 | -57.42115 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d390645-13d4-35d1-8239-833789eabec2 | -10.90384 | -57.42497 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40e154f0-beab-37fa-8a7c-39f0b81212f7 | -10.90103 | -57.42054 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31649b75-5789-3164-ae32-497a5c77cdc7 | -10.9004 | -57.42435 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61d2a3ce-9968-3a8b-b626-b91feeda549d | -10.8982 | -57.41619 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23e2c159-08fd-3bdd-897e-455a3ab533d2 | -10.89758 | -57.41995 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c52857f-e4b8-315c-92df-539a84883668 | -10.89506 | -57.43525 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccb41234-f649-3809-a66b-bf6ecec01690 | -10.89475 | -57.4156 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0792466a-7749-3803-ab34-b5d12284f959 | -10.89413 | -57.41936 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85c0a06d-c079-32c1-9999-c49a256cec9a | -10.89351 | -57.42317 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e62acf24-6da3-3c0e-b841-275aab137d76 | -10.89288 | -57.42699 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 260598d9-8068-3911-9289-d90f86c654af | -10.89188 | -57.45452 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89c52b62-6509-358b-ac65-23a2d1b796d6 | -10.89161 | -57.43466 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cb8be9a-ff22-313e-86b5-d116e1c0f2de | -10.8888 | -57.43023 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d66eaeb-6713-323c-a57e-49ad987feaf9 | -10.88778 | -57.45784 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c12b957-dd33-3047-9ba0-ce693a2e235b | -10.88689 | -57.44177 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 603e4e04-7040-348b-aa47-d926749574df | -10.88497 | -57.45336 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2477d64-50a3-394a-85b6-d2c602260527 | -10.88343 | -57.44122 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eecebf92-95d3-3a55-99f1-1e0d33155677 | -10.8828 | -57.44507 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0efd7c0-d115-36f6-b34f-3453d82a71e6 | -10.88216 | -57.44893 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e1eff53-3a49-3245-82b1-8f1e09082055 | -10.88176 | -57.47276 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4187f29b-c477-3d1a-90d7-88e805be47ed | -10.88152 | -57.45277 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README133.md)
