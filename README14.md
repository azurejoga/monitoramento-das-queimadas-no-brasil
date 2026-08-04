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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fb82f72-d201-3726-a14c-002c7f534a8d | -11.24004 | -54.85522 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 776de404-5cdb-3187-be74-457f6efac4f3 | -11.19942 | -54.86848 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 019951e4-360c-3bca-a132-3b65e0aa6b80 | -13.43681 | -43.86906 | 2026-08-04 05:06:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 61cc0edc-7559-3935-ad54-5ef33bd7d43d | -10.98718 | -50.93238 | 2026-08-04 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71ec8a16-c2fa-3b7e-a4d6-4bae307d80c1 | -11.20797 | -54.85815 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5de07d02-b294-3df8-bb2c-3d4cdd25d3f9 | -12.55444 | -52.2467 | 2026-08-04 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ab585d9-85c2-367d-9502-7a132bc8f5f1 | -13.43762 | -43.86139 | 2026-08-04 05:06:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8b489620-a923-3d53-b0f0-f4794149d980 | -12.85129 | -52.82649 | 2026-08-04 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d8bb70c-749f-3ca4-a5d3-3a053bb4e90e | -9.61077 | -47.76442 | 2026-08-04 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90600961-c291-3c19-9beb-ffa76673fa48 | -11.24919 | -54.84103 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94dd9290-fa21-327d-877c-57ea982dbce1 | -11.25376 | -54.83395 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df435212-2276-3e34-9e8f-8d6dcf9d6b9f | -11.20461 | -54.88089 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0da1d99a-9660-3890-9596-87bf564056c0 | -11.21484 | -54.85922 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e827b6a-5902-3aea-b0f8-cd05d23fbcc6 | -11.74988 | -50.27716 | 2026-08-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d5e3d77-d909-3f7e-8f68-b8a0608b3fdb | -11.2051 | -54.85381 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb68ae61-efe9-380a-a0ad-44218c63a7f8 | -11.2366 | -54.85471 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 109287e7-e13a-348e-ab8a-e991a9351bc2 | -10.82057 | -65.09517 | 2026-08-04 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 062fb60a-ebd6-333d-abef-737a87b6ab0f | -14.26229 | -45.2603 | 2026-08-04 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 19eb859e-c48c-3f4d-b05f-1e2c252a7d11 | -11.22116 | -54.86406 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3196e067-ab72-3441-87c0-4ebefc51d30e | -11.2035 | -54.88845 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccc097ec-c611-3896-99c1-2f88fea9b0d5 | -11.18968 | -54.86307 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6eafb434-7abd-341e-a5f4-7b17a3ddfa7a | -11.24975 | -54.83724 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66d59728-84bf-30fd-91a6-702919005630 | -11.20735 | -54.83854 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e975521-9aa5-31ae-a38b-238de49db9a1 | -11.21828 | -54.85974 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abbb6947-5aa7-39fc-a922-f07843593edd | -11.22228 | -54.85646 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efe8f60a-f83b-3c0d-ba8a-02792f5d9e94 | -11.2246 | -54.86457 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 45175e36-6e04-37ba-a32c-7fe200d8639d | -12.02692 | -63.08841 | 2026-08-04 05:06:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2a420cc-bfae-3963-a020-4fc53dfd2356 | -11.76221 | -50.28825 | 2026-08-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b3cd2675-a041-3059-b577-192352a5db2b | -8.94949 | -62.05198 | 2026-08-04 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14fbd467-fa9c-349e-8040-3097e06c65e9 | -11.56752 | -50.23767 | 2026-08-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67dbf7a9-a5fe-3d7a-8d47-8c11b5d3c6af | -7.73582 | -55.34365 | 2026-08-04 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76e13a58-d52d-3852-86fe-7d7910b986a9 | -11.20573 | -54.87333 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba2e093e-fad1-3ff2-974f-4be4c275024c | -11.20566 | -54.84999 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8b764c0-7753-3cbb-93b4-9b33379b25cf | -11.21653 | -54.84777 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0255af66-4a09-34a1-9c33-eb87ab00cd35 | -10.55994 | -46.77706 | 2026-08-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfe5b97d-73c7-390a-90d9-2c2990763971 | -11.20791 | -54.83472 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4204a3b8-40c4-3689-a18a-3c7767b0fffa | -11.20517 | -54.87711 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20aec3f8-2801-3329-93f2-67a776450ce3 | -11.12998 | -50.39262 | 2026-08-04 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 713716e6-865b-318e-9fca-c139e413aa80 | -11.22172 | -54.86026 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8eece9ee-db85-3fe0-be43-1233692b6e05 | -11.19599 | -54.86794 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fccdf62b-b0b6-3be6-9d0f-ce4f9c566850 | -11.21428 | -54.86302 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 397f9bcc-63f1-3488-8385-2ecb8cbe64ad | -13.4362 | -43.86631 | 2026-08-04 05:06:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d1b539dc-00e3-30c1-a1a4-68f35dbd1c95 | -10.64095 | -46.76918 | 2026-08-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dbd8a46f-a64a-37cf-b07e-b990099e7898 | -9.93805 | -53.32976 | 2026-08-04 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a772626-c290-3e59-a0b7-ffd0573fd8ec | -9.93503 | -53.32501 | 2026-08-04 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43f9762b-36e0-32f2-ad4d-de0668256c95 | -11.76161 | -50.29284 | 2026-08-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 73bdbe75-1bb2-3e16-9467-7cac2683cc6f | -12.85198 | -52.82154 | 2026-08-04 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 230569e1-d9ae-380e-9ebf-eb778db371bb | -11.21716 | -54.86732 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82ba8bb9-d6d2-3bdf-aa4c-1b3f82b55ecb | -9.25282 | -60.334 | 2026-08-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44412d05-25df-3f05-9b5c-4df53841daaf | -11.20174 | -54.87658 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90c4ada1-ba17-398b-979c-9877481bc396 | -11.21084 | -54.8625 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aec98fdd-ad56-3a0c-ab06-64e9d89fb93d | -11.21141 | -54.85868 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00cadcc7-cfd1-3dcd-8fb5-2021b1f3562e | -11.7583 | -50.28302 | 2026-08-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| da9391ad-c5c6-3e4f-90d2-e69995eb7b09 | -11.21884 | -54.85593 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 591b1c7f-48da-3125-ac03-edca8474a2d4 | -12.85585 | -52.82211 | 2026-08-04 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b17ed62-0252-3815-a00a-1f282527f755 | -11.20118 | -54.88036 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a723e97-17ed-3666-96ce-5c5a50f530a4 | -10.56226 | -46.77539 | 2026-08-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fc4c970-cc24-39d0-9a79-dce117378db4 | -8.94882 | -62.05583 | 2026-08-04 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 388f9166-097c-3420-af84-d44081c9242a | -11.21772 | -54.86354 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c816d2e-e3ec-3a09-84eb-87b58d117247 | -11.2023 | -54.8728 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c814b029-80c1-362f-b2bf-9173830ae219 | -7.73528 | -55.34716 | 2026-08-04 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e509b682-bc4b-32cf-b518-8e3c8c84ff69 | -10.58286 | -46.77651 | 2026-08-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e81ab2b8-713e-3668-9de6-747921f01e6e | -13.31746 | -54.3012 | 2026-08-04 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72c04d53-353c-36b3-b9e9-3641472bfe0d | -10.56176 | -46.77932 | 2026-08-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffea93cd-8de8-382a-9703-9bca3f8ebc49 | -7.23388 | -59.45077 | 2026-08-04 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bc456f0-79b2-36d8-ae58-be0196986df3 | -11.21029 | -54.86628 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6175e8ee-d756-3a1c-b52b-4df4ecbeb1e1 | -11.25146 | -54.82579 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f9c7dee-b034-3778-8b2e-4c99b081573e | -11.19998 | -54.86468 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85bff252-8022-37a2-b4ec-df519ba820c6 | -12.45421 | -50.38778 | 2026-08-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc896c5d-7a21-3b07-9138-25dbe7b36455 | -12.02621 | -63.09248 | 2026-08-04 05:06:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74a18d7e-08f7-38cf-a2aa-d95410a1245c | -8.83171 | -50.48371 | 2026-08-04 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1771138b-b8c8-3bb2-86e7-3e77bf9f05bf | -11.22516 | -54.86078 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a31a334d-17de-3407-9d27-7c914c8d77af | -7.23683 | -59.45563 | 2026-08-04 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82ba6a18-723c-3ebf-a107-2cc5b8927163 | -11.19655 | -54.86413 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 33f72e4f-d1f8-312f-844f-3354ae59203f | -11.21022 | -54.84289 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40b99882-7e57-3441-a5de-b41cc21ca572 | -11.75439 | -50.27779 | 2026-08-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4c8be7e-eece-3fd9-91a2-79ef35893aff | -11.20966 | -54.8467 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b8841aa-9f78-3f78-ab65-ab9762d50d80 | -10.56603 | -46.77393 | 2026-08-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 967b9811-acd3-316a-8811-333906934f50 | -10.56787 | -46.7762 | 2026-08-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a943625-a308-338d-88b2-86a0611bb33d | -14.26819 | -45.26668 | 2026-08-04 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8644221-b30a-3dd5-bc77-012d9c1d263a | -11.20741 | -54.86196 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d2c8d8b-9f85-33ff-ad8d-bb5e0f9ff72e | -7.23753 | -59.45133 | 2026-08-04 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2ac9abd-e6ce-31f9-a947-b4ecca87dfc2 | -12.55492 | -52.24318 | 2026-08-04 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 251f771f-51b8-3d9b-8c5d-1bbaffa023da | -10.98769 | -50.93452 | 2026-08-04 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4110c768-3733-3c70-8380-7ee5bfbe8ac9 | -11.21372 | -54.86681 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75ecc9f6-6782-3517-8031-8444b936046d | -8.66002 | -54.97054 | 2026-08-04 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1167e92-7443-3fcf-bfae-0b0990de913d | -11.21366 | -54.84343 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 610d978e-7dea-3575-92b7-b5e7f62e159f | -10.64659 | -46.76988 | 2026-08-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9eb15914-3f30-32e1-9485-d80b30a522f0 | -11.20398 | -54.86142 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c757659e-84f6-3d4b-8d76-6031541a5ef9 | -11.20973 | -54.87006 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb7ca3af-4c82-3b41-beaf-3caf00529d6f | -10.80178 | -52.7562 | 2026-08-04 05:06:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec5ec7c3-9bbb-3272-9df8-04dd353df64a | -11.75379 | -50.28238 | 2026-08-04 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cf8f124-570d-3204-90c1-d196120222de | -11.12496 | -50.3964 | 2026-08-04 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 110d99b0-e647-3cf2-9746-a29ed4b6efbd | -11.21253 | -54.85106 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e606277-719b-32db-b1b2-4a16fad4c815 | -11.19024 | -54.85926 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9a0fb624-2392-3037-a099-d84129495ecb | -11.13501 | -50.38882 | 2026-08-04 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11a06249-b167-3026-96cf-40271ab870ff | -11.2091 | -54.85052 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a7492d3-fbd4-3699-9d50-d40c14633b90 | -9.61118 | -47.76125 | 2026-08-04 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a59b2a7-d610-36f3-b0af-46ebc2a8e2d4 | -9.92475 | -53.31913 | 2026-08-04 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2671b6c-cdf2-374d-964a-717ae3a0ff80 | -9.93442 | -53.32923 | 2026-08-04 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README15.md)
