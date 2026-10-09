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

## Dados Diários - Página 221

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0294c65f-135f-33d7-9643-6f3d0c449843 | -6.12909 | -53.50909 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f62d1dc8-542c-3c5b-a262-27bc8550a085 | -6.41165 | -55.19607 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 627a1ed1-bd96-3374-b969-1adf79e61b94 | -5.70112 | -53.48334 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d55ac78a-0d95-35bd-82e6-eacddd99d9e4 | -12.23252 | -57.09724 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| eb4cc422-49bd-352b-b908-3b342c6f9f03 | -13.1512 | -54.35171 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6b74fa5-2a67-3d0d-b755-56cc52852877 | -4.30456 | -60.95035 | 2026-10-09 05:25:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73d88f35-1bf5-3c61-b3fa-11446b374946 | -4.73942 | -55.66732 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 779b4c05-380b-38ab-ba5f-fc819af1bdb8 | -6.07165 | -59.88156 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 654f7344-aebb-39ce-861c-ee12d5ff04f5 | -5.90752 | -53.89186 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26988ed2-0d40-3692-82a5-6a75a5a4b94a | -14.96689 | -47.54895 | 2026-10-09 05:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 065d50a7-214a-3b05-b115-3c700f4ed4c3 | -5.96313 | -55.36716 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 75430c1b-f0d6-3ee3-a9e9-a32c241dc7ee | -5.99218 | -55.36547 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10f99e42-62a5-378b-b3c2-dfaae089d8ee | -12.09698 | -57.15714 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6865aed5-f1a5-3e6b-a2c8-1111ddc43b1f | -12.42626 | -57.22808 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e51fd87-70bd-33d6-8db3-8f89371a90a3 | -4.29232 | -60.96014 | 2026-10-09 05:25:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c698f1d9-68d6-3053-ab5f-8d87c9c240ce | -6.45001 | -55.04408 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5214c7ea-0e85-389b-8b44-5181d1bc7c76 | -4.06037 | -59.84049 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30355a92-7905-368e-929f-267ab3b3b645 | -6.47422 | -55.47029 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 054db959-0331-3f21-aa3d-8d1563255bf0 | -5.26936 | -60.1816 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 681b70d9-5ea7-3784-8d89-89709bb0e69e | -6.50193 | -55.31462 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 784b0d2d-a5b3-3a17-b652-f044369cc43d | -14.96689 | -47.54896 | 2026-10-09 05:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e38c036-8a7b-350f-a0d1-c704b5e93e44 | -6.41929 | -55.20005 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d99c0502-7c45-393d-a81f-710ccbf7df79 | -12.24284 | -57.10314 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c5efc53-8a47-387c-b9b9-cb5c74fe8b79 | -5.98543 | -55.35981 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41f97b46-e5f6-3b05-8603-18ffc8e3e7b8 | -4.91606 | -55.85993 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30b70abb-a4ed-3940-840a-f84a45b7030b | -4.74475 | -55.68063 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1ab00a3f-5024-30b8-9069-813b2d219edf | -7.61202 | -46.53724 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2edb5746-6750-3c83-aecd-3e02fe8dd414 | -6.15466 | -51.70233 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a81429e0-a522-39d2-9a80-73731dec48d1 | -10.68006 | -58.7381 | 2026-10-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d198b91-35f7-3172-80a0-e3a8d043307a | -6.23012 | -60.03663 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06a075c3-5525-3818-97bb-8548f75312a9 | -6.45904 | -55.4951 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3002f946-ddf5-3526-9fbf-019c5b301187 | -5.29423 | -60.09073 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95e29808-e9ef-35c7-8340-e9f6a244a862 | -11.96629 | -57.61127 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd91af5e-509f-3d25-9f75-2b3c23618d79 | -6.32183 | -54.79292 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ef1716f-c5d2-3b7d-b5f2-329484696d53 | -6.22694 | -55.6195 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dadfee83-6c7b-3fd5-9194-f776c6248f9e | -5.93489 | -51.8301 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7348be8-7485-33b2-bb36-da5211196b49 | -6.1295 | -53.06201 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a64cbad-11f6-3be4-8dcf-cc5b811560a5 | -4.73224 | -55.6661 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a36274c4-1b54-3b58-a407-4aac7fbc1e98 | -6.16784 | -52.86046 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 382eface-e83d-371b-965d-21d79d97abb1 | -7.18227 | -52.61561 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca721abb-ec92-310b-86d5-a401d057cd53 | -6.16845 | -52.85628 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3a9fe49-5afc-36a3-bb42-e9d263261604 | -13.21181 | -54.36472 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 819efdfe-97c1-377c-b719-fd7b12352241 | -12.22337 | -57.10908 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7dd4beb0-b132-35fa-a4ed-d162ba5c3396 | -4.05981 | -59.84404 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5b4fe03-3e24-3928-8f12-3632c31f3911 | -12.20446 | -57.1371 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b45d51a-a622-366e-a95f-0301d83d2cbc | -12.21431 | -57.09445 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8c36111e-4e4e-301a-8c83-1a5792ebd2eb | -5.95879 | -55.36034 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 144e1438-ae9a-3083-885f-84b22194bbd2 | -6.14431 | -52.89961 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bb7ae18-e0b3-34f6-bf18-39c20d63b72b | -4.06575 | -59.84114 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f09e87e2-ef77-337d-b692-2245acc80445 | -11.96931 | -57.5909 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5192fb19-3794-3b0a-bd9e-5132c343a88e | -6.40285 | -55.27839 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db7ccbc7-6fdd-3065-ab8f-d50053da9895 | -6.51561 | -55.38355 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f56792f-bc16-39dd-87bc-78cccd58444a | -12.21066 | -57.09388 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| fadbb5a6-4d54-3b42-9f6f-12632cf0d17b | -5.70139 | -53.45211 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92eb7404-928f-3283-bf68-c95d990489fd | -6.44712 | -55.04089 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33d625ed-bae9-3512-aeac-6e3405decfd6 | -5.266 | -60.18106 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86228c74-6163-3916-a2a1-7f32fdb63a35 | -5.25197 | -60.3332 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dea5e647-890c-3940-9b50-2059bcc527f5 | -6.42306 | -55.20061 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7ec96e1-8365-39df-a767-239b27c93121 | -4.73828 | -55.65062 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79913831-df84-357d-b46d-17e4ca36a275 | -5.70224 | -53.47559 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34113100-ec84-3ae2-8278-8b7125a1c7b1 | -3.85999 | -64.9484 | 2026-10-09 05:25:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 090dd6f6-aa02-399d-a79d-c14a23fe41b3 | -6.15315 | -53.31172 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba2e9181-a245-3382-b2e6-39b888b73563 | -11.62866 | -54.5387 | 2026-10-09 05:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3027b702-e1f7-3066-9ab7-51f5e74f28b7 | -6.23785 | -52.84306 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 478f5f24-1a34-3148-a4bf-0a0df684b46f | -14.92344 | -48.12899 | 2026-10-09 05:25:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 304024bf-5e8e-375b-a024-cc65312a4541 | -5.70501 | -53.45653 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27604914-84a7-30c9-9d16-15e9dae4989a | -6.01534 | -53.48153 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d95aedb-d77a-3a67-8654-c90a77197c21 | -6.50315 | -55.31268 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15d303d7-4e3d-37ab-baa8-7c0c76248ae6 | -6.54048 | -56.0417 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47150ac2-78d2-3d12-a9d2-a66a6348bc3d | -5.98914 | -55.36044 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d65671a8-b0b6-3640-bf60-9665ef9b577a | -4.12436 | -59.88326 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdb41421-c657-30d4-8b2b-2c48e38a23dd | -4.121 | -59.88271 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2f6ccd6-dc96-36ae-be58-8e542e738d65 | -6.46274 | -55.49568 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e803894b-16f7-337f-9f5c-a0e0daa7d4a9 | -4.06372 | -59.84102 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1995b38-887f-37b0-98e4-505c90af69bf | -12.23315 | -57.0929 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 44144763-d76c-38ca-853d-b4748dda9582 | -4.75019 | -55.66911 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9287b698-6f01-3572-8b7f-51dc0442fb2b | -5.96556 | -55.36589 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| efbf1a72-dc0b-3025-b15b-3954e29fc948 | -12.21795 | -57.09502 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bfe7ecaa-01fd-3f60-8f66-8d4339d8183d | -6.21837 | -52.88064 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bce4897b-14ec-3907-bed8-d1d804320dda | -12.23201 | -57.075 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8b55b41-426b-3f4b-b72e-c826d419b053 | -5.69219 | -53.47514 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0818063-8b08-3b0a-a79f-7964a437e5d6 | -6.4426 | -55.045 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41f37989-1b05-3ce2-a4cb-04a90544c81b | -15.11469 | -48.52886 | 2026-10-09 05:25:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07dbd1c3-8779-365c-9262-f91688b79154 | -10.38563 | -68.90187 | 2026-10-09 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd03427f-aeb9-397c-9d29-13047c3dcdf9 | -4.74126 | -55.65525 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59ed792b-e994-3a3b-af44-215757d8c945 | -6.44188 | -55.04965 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c9df52b-5fa3-39b2-a5c3-99c3b8a49aca | -6.11377 | -57.85639 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf4d249a-223a-38b5-bfbe-15910eb62812 | -4.06485 | -59.83392 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3378d65a-5e9f-376b-bcfd-a68c15c28d79 | -6.01475 | -53.48543 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cdd84d4-dd7f-32ca-9a4e-8225f2e88ccc | -12.23981 | -57.0983 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3fdb43ab-53d3-3cb5-bd9e-4581156c006a | -5.88909 | -55.52952 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97b24a4c-2977-3be5-9d7c-9e4f89ba76cb | -4.64534 | -59.42905 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aff1b17-cbae-33d7-a849-093aa32f5d5f | -4.1288 | -59.89854 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40669553-0b60-3f6f-9ece-e65a44b52bcb | -8.21661 | -46.43426 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 327c556f-ee4b-3af8-9323-7f7a69378351 | -12.21963 | -57.13493 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20e163c3-ddf6-381c-8d72-ab078e03da4b | -6.49184 | -55.96363 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4d47989-1c3c-3126-b415-8b6f84b57bb2 | -6.87962 | -45.9085 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 74584887-eb5f-32a4-b38d-c20ec8e6cded | -4.80031 | -56.1455 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d648c8ca-a53c-3415-99a5-358e3b6a5b3c | -4.74004 | -55.66327 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2aa13438-96c8-3e00-934d-a4d0b7f409fa | -4.7388 | -55.67139 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README222.md)
