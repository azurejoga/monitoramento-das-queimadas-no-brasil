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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85568855-bb55-38cb-8dbe-50188ea91c6d | -4.4844 | -42.8866 | 2025-09-06 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| a7d2bb3b-4b78-3be9-9235-828945c086d1 | -5.8718 | -51.7145 | 2025-09-06 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 5346fdb4-b41b-3d07-bb03-38a4aec43b51 | -4.5031 | -42.8854 | 2025-09-06 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 321.3 |
| aa359bd0-5dc0-3adb-a2f6-7ebecb60dc18 | -10.6131 | -44.3051 | 2025-09-06 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 689cbb7e-f64e-3a2c-addf-607de8de7ad4 | -9.988 | -60.0184 | 2025-09-06 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| bcec3ee4-bb06-3510-bd03-4e84683f7725 | -15.5747 | -52.9175 | 2025-09-06 00:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 134.8 |
| ced8be4d-3cd3-316c-a26a-4ffdda13232e | -6.5393 | -49.5101 | 2025-09-06 00:50:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 844b1134-4eeb-3605-aa37-018fa8360f77 | -3.2516 | -50.8082 | 2025-09-06 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9a101727-6d34-3459-81d9-572f8cad0542 | -12.5224 | -53.8692 | 2025-09-06 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5881dd14-c1e7-3f40-9320-b5f4cd91f969 | -22.2424 | -48.7513 | 2025-09-06 00:50:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 234.3 |
| 8df52cf6-8100-3ec6-a07e-699b24895228 | -4.4845 | -42.8631 | 2025-09-06 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 083e2e19-e065-3f52-87ad-58547dcb470d | -10.6128 | -44.3284 | 2025-09-06 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 229.7 |
| f7eeed11-8add-3443-a0f6-a4f5ea3e466e | -12.9665 | -54.8116 | 2025-09-06 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 30581b2d-7e63-3a4b-99a8-10589082784a | -22.2431 | -48.7279 | 2025-09-06 00:50:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.4 |
| bf549016-ecbe-3a16-b1eb-d012d6480c0a | -9.7227 | -49.5021 | 2025-09-06 00:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ba307a5a-0ec1-35c4-af06-4a40f42e3c92 | -9.7041 | -49.4825 | 2025-09-06 00:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 8f73fb12-406f-3d37-acc5-5c7ef0d2d380 | -10.6128 | -44.3284 | 2025-09-06 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 04f9add2-035e-3313-80a4-e7f299798554 | -10.594 | -44.3077 | 2025-09-06 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 3ab1fe16-84d1-3871-bb8d-65450769bc99 | -9.7227 | -49.5021 | 2025-09-06 01:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| a01ccfb5-3f65-389b-ba28-d10492364e08 | -15.5743 | -52.9388 | 2025-09-06 01:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 90b9f6ff-a593-3e77-9b11-87a4dfbc3e1b | -15.5747 | -52.9175 | 2025-09-06 01:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 096d9e00-d010-366f-a475-01ccb0bc6696 | -12.4846 | -53.8525 | 2025-09-06 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| eeae5edf-8a59-3f47-bee1-4a3f01b1fd36 | -10.5937 | -44.331 | 2025-09-06 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |
| e669c301-75a4-396a-8325-b3f3505ccbe3 | -15.5751 | -52.8963 | 2025-09-06 01:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e36fc602-4aca-3425-8f13-c0b2ce19902e | -12.5227 | -53.8485 | 2025-09-06 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 929c16da-6704-3021-974f-049fb63e8f06 | -4.5218 | -42.8843 | 2025-09-06 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 396b1efc-3631-3db5-b96c-96cc0d30b6e6 | -22.2417 | -48.7748 | 2025-09-06 01:00:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.0 |
| 2f0fb696-90b5-3aa0-be04-161b6aabf3e0 | -15.5938 | -52.9361 | 2025-09-06 01:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| d7bc207e-de97-318e-99ec-6f46ce7493bc | -4.5031 | -42.8854 | 2025-09-06 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 679.3 |
| 21df3224-2631-37a7-b50d-65a871ec8f80 | -4.5029 | -42.9089 | 2025-09-06 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 216.3 |
| 419e9e9b-309f-3184-8d50-4ee9b8be5b13 | -12.9665 | -54.8116 | 2025-09-06 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 1a16abf3-6704-3567-b14f-03e120174d79 | -3.2516 | -50.8082 | 2025-09-06 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| cafd70dc-4076-31ed-957c-3878775b2e5e | -12.5036 | -53.8505 | 2025-09-06 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 4bfdf58c-dfca-3995-9178-a32f62ab8e7b | -4.5033 | -42.862 | 2025-09-06 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 122ee67b-6034-3435-ae21-5ee3fdfaf00a | -22.2424 | -48.7513 | 2025-09-06 01:00:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 169.7 |
| 1591159a-94a1-3bb7-96b4-575a61ca81fa | -15.7381 | -53.5717 | 2025-09-06 01:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 06f31f83-afe5-3b5c-9e6e-24656b3573c6 | -6.5393 | -49.5101 | 2025-09-06 01:00:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b5460650-9ad0-3b7d-810e-ec0265b87d17 | -15.5942 | -52.9149 | 2025-09-06 01:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 723d6a96-52a8-3a0c-887d-1bc41de35e98 | -9.7038 | -49.504 | 2025-09-06 01:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 01417ef2-db3e-30c3-a7ff-3e2eee4f7c6c | -5.4917 | -60.138 | 2025-09-06 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 134f3a1d-c140-3812-b465-d2da01a74855 | -12.4843 | -53.8732 | 2025-09-06 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4184340e-9c04-3489-a7b6-8049196f053d | -12.5033 | -53.8712 | 2025-09-06 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 7f4d013b-d3ee-30fd-953a-62a620094562 | -15.7186 | -53.5743 | 2025-09-06 01:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 5b87a61d-049c-3578-82b2-93064bb616bf | -9.723 | -49.4806 | 2025-09-06 01:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| eaf5429e-be82-3cd9-ba37-184172895512 | -13.0044 | -54.8282 | 2025-09-06 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 59c8104c-bb89-3ca5-80e1-e3fcab355edd | -10.6131 | -44.3051 | 2025-09-06 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 927ec6c8-ebc6-3b4a-a643-fa00889b3965 | -3.2331 | -50.8087 | 2025-09-06 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| c3c99793-ce43-3d6a-896c-8e59dd052932 | -22.2626 | -48.7697 | 2025-09-06 01:00:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |
| b38f9a37-6c38-3777-a12e-89fc65963fe5 | -9.7041 | -49.4825 | 2025-09-06 01:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 63e5501e-78a4-39b5-bcbc-aeeeb9714889 | -4.4844 | -42.8866 | 2025-09-06 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 9f093b7b-6a0b-3ab7-a564-d92913ebf41e | -3.2516 | -50.7873 | 2025-09-06 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 0c2afe31-3145-3f25-88e2-d0d16fb29102 | -22.2633 | -48.7463 | 2025-09-06 01:00:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 178.7 |
| 1b1f7014-656b-300c-a6df-d8857c2ff089 | -14.9015 | -49.454 | 2025-09-06 01:00:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 496d2043-6ae9-3675-b4db-eb6d6df8f282 | -13.5919 | -43.361801 | 2025-09-06 01:05:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 52955337-f9e6-3b16-84d9-f013c95df155 | -16.7367 | -49.332699 | 2025-09-06 01:05:00 | METOP-C | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 520ef712-d080-37e6-a694-05adb3573315 | -15.5794 | -52.9188 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f4f9a5f-95c2-3899-a921-50015dee6361 | -20.5371 | -46.467201 | 2025-09-06 01:05:00 | METOP-C | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cba4f69c-c3c8-3f12-bbec-92c4fb720d65 | -15.568 | -52.914001 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a2683938-411c-39d7-8c49-728ef8199255 | -6.5375 | -49.521702 | 2025-09-06 01:05:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5bef33a-cd3c-3bf6-91e5-d63815045b66 | -3.9806 | -47.882301 | 2025-09-06 01:05:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93bf083b-a9df-3f56-881f-4ba9e7ca1192 | -6.535 | -49.5112 | 2025-09-06 01:05:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57aea92a-5e5e-36e4-bfb2-be807cde06f0 | -15.5762 | -52.904598 | 2025-09-06 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60c13a9b-b5ab-3298-ae83-13c9f8c9f7de | -6.0065 | -46.702801 | 2025-09-06 01:05:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55e5e83b-709a-3d6d-81d3-ac8043587e0c | -12.5021 | -53.850899 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8dd4a03e-1154-3264-88ff-b67ebb747aa0 | -11.1736 | -55.050098 | 2025-09-06 01:05:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6ce842e-467c-3726-b60c-dbe7352c471f | -4.8584 | -50.8307 | 2025-09-06 01:05:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0faf5d7-76a7-39b5-ad53-626a819c37b5 | -22.241699 | -48.757599 | 2025-09-06 01:05:00 | METOP-C | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae70b797-3687-3279-a385-60f9c1f4201d | -13.9733 | -42.592999 | 2025-09-06 01:05:00 | METOP-C | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cd80b97b-cf9c-3f93-9814-63dbf7a05a5b | -5.9601 | -53.604 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c1638b6-dd66-3a3b-b855-2bd5b5d5a303 | -9.6739 | -51.113899 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 780810c5-f562-3e6a-98ad-eb1636b5d316 | -5.001 | -56.035801 | 2025-09-06 01:05:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aba59a34-58b2-3bb9-8b13-20a085265b99 | -24.152599 | -49.521198 | 2025-09-06 01:05:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 07e6b100-54eb-3386-8b32-f309b6f0c187 | -14.588 | -52.1768 | 2025-09-06 01:05:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be1972cf-4531-35a5-a74f-0b9c925d98c9 | -11.4711 | -55.560001 | 2025-09-06 01:05:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9470b909-f911-365b-afba-3f12c628f00d | -12.4727 | -53.857601 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 546ea35b-1414-3e4b-ae23-ddd8f30438f8 | -12.9552 | -54.828701 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d12fba37-a496-34cb-9a78-0c8e1a98c036 | -9.0512 | -50.448299 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a7df7dd-85b1-31fb-a2bc-d57ffc7cf64b | -11.5891 | -52.194599 | 2025-09-06 01:05:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c87bbe03-e564-3286-8963-7862baa34aa3 | -9.672 | -51.1059 | 2025-09-06 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52c70cb5-09c2-3634-9114-80dab9b67149 | -15.177 | -52.41 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e4aad83-834d-36e9-9c49-3aadf0f79535 | -14.2586 | -52.180099 | 2025-09-06 01:05:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 707f9781-3c69-3d5e-83f1-8124c4e30937 | -18.139999 | -51.787498 | 2025-09-06 01:05:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 855ac4a8-5fe1-324a-9ecd-110c7e993b12 | -9.7051 | -49.5126 | 2025-09-06 01:05:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f771717f-2bf3-36f1-b5a0-39dfe28055a7 | -12.1853 | -53.908199 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b54aa16-0187-3546-b835-daa56cbb5d14 | -12.5068 | -53.872002 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19639323-1aee-3135-9e56-89da944458d9 | -5.0612 | -56.0741 | 2025-09-06 01:05:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af3d4867-6610-334d-b712-75505cbce107 | -4.2612 | -48.194 | 2025-09-06 01:05:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21833fa7-f4ba-3a9d-b2a8-7e1e7093f0b7 | -9.3884 | -54.754501 | 2025-09-06 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d1420b7-81cc-30ed-9c35-1c5e1390339a | -6.5448 | -49.5089 | 2025-09-06 01:05:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a599cb-c3a2-3cc8-995d-556950ca2eef | -15.1918 | -52.384201 | 2025-09-06 01:05:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31739d88-0adb-3759-b3e0-9cc7949bef68 | -13.0107 | -54.8475 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23db15a1-b11c-3bfb-b78e-9c78f1788c40 | -10.6011 | -44.354301 | 2025-09-06 01:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36e3f087-0086-397c-b39c-5612a514df9b | -15.7167 | -53.587799 | 2025-09-06 01:05:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e885dadf-9a6d-31b0-bb9d-42309f6c5a31 | -7.7181 | -50.314999 | 2025-09-06 01:05:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e503b7c-6af5-3d8d-9556-add349169e57 | -12.5103 | -53.841599 | 2025-09-06 01:05:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 861f86e2-9954-30c1-9d24-a43cc1b65e8e | -12.9895 | -54.797798 | 2025-09-06 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 495c033d-287a-3e51-aa6a-de8a202bb1cf | -14.9025 | -49.4515 | 2025-09-06 01:05:00 | METOP-C | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f0130cb0-f9bb-38dd-8f80-a5a7dd3cc117 | -14.8467 | -48.197498 | 2025-09-06 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f4626980-5cb4-37c9-82c7-9b6f63fb2e6e | -9.5567 | -53.587799 | 2025-09-06 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a78a615-f7a6-316b-bcd6-3b5a97d5d602 | -8.9301 | -48.660599 | 2025-09-06 01:05:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
