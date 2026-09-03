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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d678bef-7065-3584-9d50-584083c9df2d | -8.43486 | -54.68668 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c61ed0cd-bdf0-3fe4-a07a-abee21ecaa2a | -6.69206 | -59.94999 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12143746-5024-37ff-8b92-6355f16b8f90 | -4.14281 | -60.69573 | 2026-09-03 04:57:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af2abf35-b8c2-35d6-83e7-ecbf62ac4651 | -3.19824 | -61.21417 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71fd0eac-567d-3c8d-9eed-d9faf03507b2 | -5.5873 | -60.20353 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed5ce56e-654a-3549-ab8c-1d778457a90b | -6.35149 | -55.86519 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b73693fe-2ba6-3944-8ed0-e632c2eb590a | -6.62047 | -55.2378 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34155271-2732-3378-97e4-8e0c0ae4db5d | -10.99116 | -45.08592 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7ce80fea-4f12-37a4-906a-f3258a235569 | -7.33265 | -55.14564 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f6152c7-c838-3d01-9f99-8b29b5c16e92 | -6.81349 | -58.99859 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a95460a-b0b2-3a1c-b04a-d08d0c2700fb | -10.87407 | -45.32518 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a26a98e9-e235-35c4-bec9-8a574066a961 | -5.94322 | -52.15532 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ab24b1b8-c2ab-3489-9900-d70a65e88f6a | -6.24756 | -55.48394 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15309f21-b059-3dee-a4c6-cba0dd5d1a0f | -10.49188 | -48.64523 | 2026-09-03 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f46118d-8de3-319c-9baa-3c0ad39d73c2 | -11.29389 | -45.14109 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2da16dd6-8e06-3953-b9d6-a66f7ddc0dc1 | -6.31617 | -56.0563 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| adf4b541-20d3-3a77-bd6d-37fc693a21fe | -5.20793 | -60.0374 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d374c21e-f2c3-37e7-b03a-00ec769df4b8 | -9.1021 | -65.50731 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 890b4c1a-33b3-333e-84b8-062a04aacd26 | -6.14864 | -55.66579 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba860479-d33a-3608-8ede-92fda00a8abb | -5.25579 | -60.18972 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1c9280b8-8ffc-37a9-896b-9bee142192a9 | -10.42068 | -57.22964 | 2026-09-03 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adeb0dcb-88d0-3608-b3af-81c11db9c820 | -4.26394 | -55.1594 | 2026-09-03 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 229803a4-fc1c-329e-848b-3f9a3738a8fd | -10.56732 | -47.72942 | 2026-09-03 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecafaaba-9750-394c-9a1b-0379e9ef92e3 | -5.94599 | -52.15932 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0d404af9-6501-31e0-a67c-130701e13227 | -6.84041 | -59.34086 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d3b8f68-37ef-3802-aa3e-cdb555094193 | -11.31877 | -50.53374 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 48e8f349-8aa2-3cd7-be10-1b4433e64d6e | -6.77864 | -56.29664 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 705874df-a80b-327c-95b1-3659b91d7712 | -6.61512 | -55.24882 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 029724f6-aa1c-3eb2-b8eb-f2be640c4232 | -6.42719 | -53.56034 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef065aa2-24b5-3a5d-88fe-42b904f4c47e | -7.24648 | -59.52604 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d5dae2c-90b3-386e-9166-19d49aacb29c | -3.14673 | -60.64557 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f70790d-9a07-3815-ba81-92a43a1ee4a0 | -3.07999 | -61.18019 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 804b4f1b-2418-37fd-b5d2-eb5a406a088e | -9.02035 | -65.72225 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b94f1e17-7a49-349a-b655-a2ac919d95a7 | -10.75761 | -48.97173 | 2026-09-03 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ab6bf19-f44d-3931-bf65-b18aa9325260 | -10.30067 | -49.99097 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25acf21a-d0f1-3639-9c88-5510df8a8523 | -8.43032 | -54.69337 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2bbc9ba-d251-3a65-894c-632931251398 | -8.45681 | -54.67915 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5735fdb4-487d-3883-a767-ef4a08623f86 | -8.07743 | -50.96185 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d59633b-e883-3e62-aaee-e7e7f2d9d47b | -8.45355 | -54.65647 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c02e476c-dd84-358b-b151-5ec392e66909 | -8.4575 | -54.65342 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cb87be1e-e509-3528-aca8-65bed35c7b30 | -8.42974 | -54.69698 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4ded0a5-3d01-3bbb-b51e-50decd60d425 | -7.03807 | -59.215 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae227e00-3202-3cb4-b9cb-e7648aa2aad7 | -6.32356 | -54.75163 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b6de8a4-d351-3f50-af0b-40319e23f590 | -10.35364 | -49.96677 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd38c7a1-6a6e-34c6-ad6b-844c388d9d55 | -8.45239 | -54.66367 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43966b79-0b34-3638-a2f2-88a84dacbc58 | -3.14393 | -60.64518 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd989966-454f-3116-afe6-b81b99ead87c | -7.19422 | -60.66204 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e46dae46-23b0-38f9-bd1b-ce73b75bd436 | -8.42637 | -54.69643 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51d1e416-8f4a-3f83-91db-3243493ca4e5 | -9.88237 | -60.29517 | 2026-09-03 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c54d7f8-cc1d-385c-9337-01f3201446e7 | -3.1416 | -60.64473 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4a13ebe-c80e-3a67-8052-b7f408928ab0 | -8.45739 | -54.67556 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dab352d6-ef0b-3d06-afd2-d7f69de35e50 | -7.34745 | -55.20664 | 2026-09-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5477b418-ea31-32b4-9d63-b39100c31d7d | -8.46817 | -54.65146 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9073dcf9-0160-3338-a876-7c37bfb0d0ef | -10.18333 | -50.2845 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b333664-5145-3a61-b343-7da61affe927 | -8.08378 | -50.96675 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 136cc503-be74-38f1-a704-14029ccc1faa | -8.44018 | -54.7396 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1378a152-b2a3-3a65-b413-e8ffb11fa523 | -6.83634 | -58.96866 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b23db9b-264b-389b-947c-1c62dc4a269e | -5.25664 | -60.18074 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff09aa91-39d4-3085-98de-1055c71b89fc | -5.20527 | -60.05281 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3a8f0a5-2407-38c0-98fc-d1a26569f74d | -6.79906 | -58.97926 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 408ecf93-fff1-3f07-9b96-9e14d0d8332e | -5.20705 | -60.04251 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| beb76dab-d87c-390e-bffe-aa33a63e222a | -6.63847 | -59.43975 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2419c6c2-a16e-39dd-b085-dc9cfd530525 | -6.75064 | -59.44374 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e32100ff-9f2c-37a1-9c12-c0ccfb277868 | -7.61575 | -57.61797 | 2026-09-03 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63c11865-56f0-37fa-be4c-b7fee5990e89 | -10.18286 | -50.26237 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7a2207ab-007c-33d6-8b9a-f7b249b8415a | -5.97091 | -53.58736 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4df27343-4692-338a-bef2-313c2a585da6 | -6.94468 | -45.20466 | 2026-09-03 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06ce1d88-ea2c-35d5-b7c3-3414e30f92b6 | -10.35124 | -49.95722 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27ffa79b-0bb1-3d0d-bd09-826500806e33 | -8.43064 | -54.73431 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11d1e4e0-f623-304f-a9ad-5205034aab23 | -8.43564 | -54.74627 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e67db04c-1e9e-3069-b6cd-8705538a7aaf | -7.08262 | -56.51766 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e93c8088-dc27-3cc9-b866-e98ecddaa1ef | -7.05042 | -59.22163 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd474791-6a9b-3e71-960b-67984f6cc1a5 | -9.06746 | -65.72041 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9c07363-2312-33d3-8c63-0c36b3c8bd42 | -6.24343 | -55.39794 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2017eaea-540d-30b5-8c8b-11edcc445814 | -6.76105 | -59.43641 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 627122ca-c99e-3243-aedb-850950a649ce | -3.12602 | -61.23272 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 267c3159-6b93-35f4-8494-4ddbdedcbd2f | -6.25463 | -55.44024 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c99e204-aaa4-32de-b58f-ecf00c90af1b | -6.78256 | -59.41758 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6538a424-9109-33f6-b72b-f59aee2c5d7a | -11.287 | -54.06152 | 2026-09-03 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4616a49d-29ea-3f56-87b3-f314153033ac | -5.2014 | -60.04686 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d18fad82-da03-3f17-8ca5-ebb4ef40ca89 | -11.30499 | -45.13688 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35c0e6d5-369e-374f-b404-77905e8175ed | -6.87633 | -59.39646 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9997970c-a29d-3705-b5da-92fbd7e86ceb | -7.40723 | -49.74284 | 2026-09-03 04:57:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56f601c0-a62f-3fa9-aef0-ac09f218f511 | -11.31771 | -45.11993 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 98c4965b-3afd-3f29-afd2-ed3eaa872c64 | -8.08032 | -50.96622 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 4aeefc5a-dc91-3ec3-bbcf-4ad73d0e1fcc | -10.99634 | -45.08668 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| edc7bd6a-2c9d-31cc-be63-92e243cbdbfb | -6.30741 | -56.04182 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b14fca59-f052-3f48-b26f-e4116ef4fed8 | -5.85622 | -57.55677 | 2026-09-03 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e902c54-30b2-3ba5-866d-bca773ea6d51 | -5.2476 | -55.89959 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5da964dd-eafc-3b54-b50c-22e38b6a9b75 | -6.41555 | -56.17971 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9b8d371-6136-3845-8fbf-0e96b322fb22 | -10.89097 | -45.31496 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c57e9bb7-1bbb-3c44-b4e5-ceb99f633580 | -5.88709 | -49.88496 | 2026-09-03 04:57:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0806dcba-64ee-3de5-b205-e58c6ec99c10 | -6.32259 | -56.04 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b60896d7-5181-359e-ab8e-ef30577b792b | -6.48955 | -45.92454 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68adfdbc-97bc-3ae0-a05f-6ab9b0734885 | -8.45865 | -54.64623 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e103d0bf-7349-373e-97ef-520d34e2bb47 | -10.87724 | -45.30087 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| eeb3f12b-0e4e-36bb-83ec-80cf6627543a | -6.18656 | -55.27732 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ea8d30a-fdb2-3335-875f-9b8316727773 | -7.08325 | -56.51923 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7572209d-4386-3ef7-8754-1c61ea44de61 | -8.07916 | -50.97388 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a180c53a-ca4d-3831-9b08-a7cbb140bcff | -3.12124 | -61.22843 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README38.md)
