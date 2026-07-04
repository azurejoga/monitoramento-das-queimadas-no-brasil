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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4c78da9-a66e-3d75-8997-5596debe87fc | -5.93735 | -46.35433 | 2026-07-04 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db8debdd-7fcd-32d4-b3bb-2fbcbdff5488 | -10.98397 | -43.70638 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4db5388-d7bd-3677-8c50-e276500ca9cb | -12.76737 | -44.51407 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 333ac839-bba4-3676-95f8-8e0906b478ed | -12.75505 | -44.53447 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1035d40a-63eb-3dc8-9eb6-c2749db49bd1 | -8.95516 | -49.8647 | 2026-07-04 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9948eb5-7cbd-3f75-9a82-5868b6aff980 | -7.23338 | -47.11601 | 2026-07-04 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 49f4397e-c194-301c-a85d-f61a52b584dd | -9.44188 | -40.32523 | 2026-07-04 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 6c1f33ee-dc1d-3461-a71d-91680800909b | -12.35396 | -47.89953 | 2026-07-04 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba9b93ab-b0d9-342c-8356-6dcede749a43 | -11.42816 | -46.58249 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 68a8fb24-ada4-31ed-8c6b-c5d660b7aeb1 | -11.33451 | -46.90603 | 2026-07-04 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a863323-a787-3540-9baa-517dc6008fad | -8.8557 | -62.22414 | 2026-07-04 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f969315c-0105-3fd1-afd9-c13366ebc0b8 | -7.73122 | -44.17341 | 2026-07-04 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8c99b0e-fc5c-3dfd-b949-0cae76ae7e07 | -8.86122 | -62.22161 | 2026-07-04 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eae3b0ca-8dc3-3124-8b7f-e463e12f3b5d | -8.08262 | -47.15944 | 2026-07-04 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fce7bab-5d81-3952-a735-23b6a2b90994 | -12.76257 | -44.5237 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e51b8c22-7a99-3247-8b46-3d964775c3e3 | -12.76047 | -44.54 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 87f91d56-a3db-3b6f-b63d-2838f4e4dfdf | -6.42571 | -43.72264 | 2026-07-04 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5cce3e2f-5e54-3402-b9b7-7588eb610546 | -10.91725 | -43.04521 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd7b15bc-baaf-3232-853c-679faae27be1 | -7.00884 | -42.78256 | 2026-07-04 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b94fd63-37c6-39b6-a4cc-7aa2a330ac5e | -11.424 | -46.58208 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d4d64bc3-0237-31c9-9193-13468f66beaa | -8.45139 | -51.56725 | 2026-07-04 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 076fdedc-9dd6-3c5e-b0bb-da0291ede98f | -12.76944 | -44.5467 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87c78bfc-485d-3cbc-98b3-9500666c1b23 | -10.9277 | -43.05372 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 5bb8a48c-c351-3bd0-81df-aa1521256b0b | -7.73653 | -44.16916 | 2026-07-04 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75b53b6f-3458-3f82-aabb-283b15d81141 | -6.90486 | -43.71754 | 2026-07-04 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a675c0a4-fecf-3761-a1e0-2d0e4b706a36 | -6.61318 | -55.29025 | 2026-07-04 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 064d376a-54de-3d42-a0b4-f54fc78e4357 | -8.08626 | -47.15719 | 2026-07-04 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e25e51d2-83b6-30ee-9d96-cfd0fb759719 | -9.4433 | -40.31626 | 2026-07-04 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| df92debd-1264-34c8-bde4-800e1d090e42 | -10.38992 | -56.76864 | 2026-07-04 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c09e72e-ac7c-3e42-a0e7-3b8ef45f9a8c | -10.91805 | -43.04589 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e16ec7c-f431-3fc6-8426-60b3640a9b61 | -11.425 | -46.57456 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8e15de78-0c2f-327c-810f-1717223e003d | -12.76117 | -44.53454 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3da2aef8-ac64-3353-a7da-22fea29cfa27 | -7.9008 | -48.25471 | 2026-07-04 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9d316f8-24a6-3826-82a1-7f97e589a30d | -11.50717 | -47.41906 | 2026-07-04 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd248f9d-387d-34e0-b552-7898b49ebaf5 | -8.987 | -47.74578 | 2026-07-04 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4bba92d-a446-347a-b204-b671788ee8cc | -7.90499 | -48.25117 | 2026-07-04 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0629182c-45c6-3e5c-a274-9400cdb418d1 | -9.04649 | -47.74311 | 2026-07-04 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37cc98a3-efd9-366a-aafb-8bb1a6862b4a | -9.39767 | -48.77428 | 2026-07-04 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bce4278f-47f1-34d8-9993-6f05efa3f1b7 | -7.80282 | -45.22187 | 2026-07-04 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6d27a27-e44b-3555-8353-b011a080b8dd | -12.75773 | -44.52305 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 53547a95-e6bb-3221-8995-e58e81d03e58 | -6.93379 | -43.71667 | 2026-07-04 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06f1cf49-020f-38a5-8400-f7a5f4a5131c | -10.92327 | -43.04659 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab5f2efb-81c0-3a18-8e01-8b78336dbaaf | -7.23707 | -47.11449 | 2026-07-04 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fd914fb4-6b21-3baf-ab46-53fb861d6714 | -5.473 | -45.42392 | 2026-07-04 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba8d33d1-88b2-34ce-a4fe-adc682cb5318 | -7.01308 | -42.78908 | 2026-07-04 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef01421a-b64e-33d0-a978-6fb9addf03de | -12.76121 | -44.52421 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4b2dd0f6-7e7f-3bb6-bfaa-e3d094cdf078 | -6.90017 | -43.7168 | 2026-07-04 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| acee9fc4-ee56-3dfb-97de-0c2846aa913f | -8.44755 | -51.57019 | 2026-07-04 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 047e7840-bae9-314d-8cdb-5f48161d2b75 | -11.45658 | -46.55917 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5b45e32-7609-32ba-b151-75124d9917fb | -7.01347 | -42.78619 | 2026-07-04 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 27b42f94-9b1a-319a-8b9a-45a61971d044 | -12.74664 | -44.53262 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e40b7797-978e-3754-9deb-4cc7b3bd1ed2 | -5.43339 | -44.65023 | 2026-07-04 04:46:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 199949e9-25ce-3a52-93be-dc26451951aa | -12.76187 | -44.51881 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7850b2ae-dea0-3de6-8d51-220920d4cb4f | -12.75078 | -44.53873 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| dd2397d3-5470-385d-b7a2-36114e2e972f | -10.93894 | -43.04872 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0fa48e1-896f-3172-8fc8-465279004590 | -12.97172 | -42.58575 | 2026-07-04 04:46:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ca5213d-b0fa-387e-81b6-c7b90dab17a2 | -8.08574 | -46.70479 | 2026-07-04 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00153a8f-1aa7-3ab2-9fda-0d6c68546183 | -10.92206 | -43.0491 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d8eccac-f0f3-3f39-9576-3123bb183f9f | -12.75724 | -44.55692 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 61b83f50-07ff-3a70-9d12-7b1c988c4611 | -10.92248 | -43.04589 | 2026-07-04 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbf011bb-a9a8-3eb3-b3c6-4eaa6d6e2a75 | -12.74939 | -44.54957 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| a1c920bd-ad22-3b07-8500-67e82070a208 | -12.51284 | -48.25863 | 2026-07-04 04:46:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae144b85-dde2-3175-b73f-eb908454669c | -6.43103 | -43.71858 | 2026-07-04 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d74881cb-8397-3fa7-b583-9cdc2c596158 | -5.53118 | -45.25761 | 2026-07-04 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 701f28ad-7ab9-3128-a86a-d95705be0b95 | -11.43845 | -46.56854 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 50a11214-a2b9-3fd8-99ef-060dc6aa5a99 | -12.75633 | -44.53392 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 52d84872-2e1c-38dd-aee9-f070ac8554df | -4.87867 | -49.64291 | 2026-07-04 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc9545dd-b49e-3f8f-ac91-89c1022b5084 | -10.90865 | -56.85498 | 2026-07-04 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae1feef3-8c35-358f-8597-da280f1ac7d9 | -5.79392 | -45.06115 | 2026-07-04 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acc5dfd2-21a7-3917-8d6c-4781f4b099a8 | -11.8714 | -45.59731 | 2026-07-04 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c18eb556-a6f0-38eb-8551-fa54119b3363 | -12.75241 | -44.55623 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7e050592-7adc-38ec-b642-ea461f68e24e | -6.66666 | -47.91656 | 2026-07-04 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0807b8e-b781-3254-90e0-744d0c7ec23a | -5.80068 | -43.63892 | 2026-07-04 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2eb01382-4dfd-3167-9b52-926b3b1be6c7 | -5.79603 | -43.6382 | 2026-07-04 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d38d0ba-77b3-3e18-b417-0276ff8274b7 | -10.30111 | -57.13104 | 2026-07-04 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c440ad3-6032-3c23-9767-7fe5e995c4bb | -12.32107 | -46.73798 | 2026-07-04 04:46:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9f59742-1c69-3d8d-af49-d5e5b7ec44de | -12.76881 | -44.51357 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b42a631-1281-3081-aba8-be5a331c404a | -8.44809 | -51.56673 | 2026-07-04 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d513766b-b1cd-3bc9-b640-3c104af913b5 | -10.78611 | -54.10967 | 2026-07-04 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64b4fa31-9c03-3d47-b0fe-f11e9888716c | -12.74804 | -44.52174 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 276e967e-14c8-3449-8ade-573a0cb1b9cc | -7.74119 | -44.16948 | 2026-07-04 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c35b094-9a08-32a7-849d-d36af533f04a | -6.22465 | -55.65872 | 2026-07-04 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 937e3eaf-b2d6-3072-9b4e-f34944370c27 | -12.75923 | -44.54057 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| fa509802-6edd-3628-83ce-b784a635387d | -6.42312 | -43.72089 | 2026-07-04 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a19ec86e-f3c6-31b8-af6a-523476391026 | -6.61433 | -55.29271 | 2026-07-04 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12d6b16e-c998-329a-b249-6e124196b001 | -10.43932 | -47.46766 | 2026-07-04 04:46:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e9a77cd-5276-33f1-a605-11fbd07d039d | -12.52467 | -48.28433 | 2026-07-04 04:46:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34cc9d95-2b87-3317-b750-cfba2b8e9d86 | -7.00499 | -42.77313 | 2026-07-04 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f2a5c33e-49c1-3902-b0e2-cb01eab0b3a6 | -12.76341 | -44.54668 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 89f09c84-6113-3d97-aa57-24d8087372a1 | -10.30235 | -57.12376 | 2026-07-04 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f925fc2-6e92-3d0e-bcb2-80e044a4d59d | -8.03549 | -46.23917 | 2026-07-04 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 465abe1e-7761-35e8-8040-a540ed076669 | -7.51178 | -49.52735 | 2026-07-04 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95e55bfb-a89d-35f0-9fed-00193eea2a00 | -11.49169 | -52.91928 | 2026-07-04 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e763ebcd-dc00-3211-ab25-bda51a2bb2d1 | -12.74889 | -44.5447 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| c7354779-08d2-3b26-89dd-50518c52c5e7 | -12.35956 | -47.42514 | 2026-07-04 04:46:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44844cc7-3f95-38c1-ba34-a6af61a33254 | -5.42126 | -45.29654 | 2026-07-04 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dbe86d14-74d2-3474-95bc-6ec34922fd20 | -12.75571 | -44.52899 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d685a8ad-1093-30c4-a8af-0df475c520c3 | -12.76389 | -44.55155 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| b4f33e31-49af-3ecc-9b58-f612332af8c4 | -11.45757 | -46.55185 | 2026-07-04 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 984112d3-c942-3c19-a7fc-256aa390d588 | -12.75637 | -44.52356 | 2026-07-04 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README14.md)
