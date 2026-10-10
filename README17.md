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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44287681-d386-3318-977b-176e4435b30d | -3.5676 | -54.6946 | 2026-10-10 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ee7b8b76-ae9b-3db3-b659-f16c0ae7c3d5 | -12.3066 | -63.3701 | 2026-10-10 01:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 774d6a52-bb20-3e50-a2f7-5a26eb0a5cf8 | -7.927 | -54.7384 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 69cddf9c-8298-363c-bc24-64a47d8757f1 | -12.3064 | -63.3893 | 2026-10-10 01:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| aa57e2dd-d12a-3ff6-927d-168c4a6ee0d3 | -7.1825 | -52.6283 | 2026-10-10 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f399f989-8fb3-3bf4-8be4-a99cb27483aa | -7.5159 | -45.3251 | 2026-10-10 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| eeeb6b40-d8df-3f3e-88ce-64a5ec75cb37 | -6.478 | -55.0606 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 51afa3c4-a480-3a4d-918c-346d3f5b9a01 | -12.2877 | -63.3711 | 2026-10-10 01:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 1d4e9efd-49d3-3686-865a-50d7f40613c0 | -3.1101 | -54.1661 | 2026-10-10 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 79e7adf8-fbd5-3b92-9f6c-0059c8b1651e | -9.3168 | -47.3629 | 2026-10-10 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b468dcae-fac3-360a-9989-1a93d9d26a8b | -10.6012 | -60.4863 | 2026-10-10 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 2c31ce6c-d439-3c84-bf14-035bfc6ba219 | -7.9084 | -54.7396 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e1acbab0-640b-35e0-88d9-109d9463b428 | -10.6199 | -60.4852 | 2026-10-10 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 0464d56b-306a-3d32-b82f-958b0c771585 | -7.4975 | -55.0055 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| cd0f4989-e424-3b7b-924d-df6bce1178f6 | -7.2187 | -55.0815 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 36947681-56d9-3316-a8be-8a048b8101aa | -5.0876 | -60.2263 | 2026-10-10 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 129fec2d-e0cc-34f4-b463-921a49f8ceba | -3.5307 | -54.7356 | 2026-10-10 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 00e3938e-5af6-3124-8882-18f2b88d65ce | -7.5347 | -45.3233 | 2026-10-10 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 135.3 |
| b3c7a773-47df-32ea-8419-dda85496f556 | -10.8902 | -44.8464 | 2026-10-10 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 277.8 |
| 098a38b9-d7c2-3c48-be65-e8f30d9672cd | -3.5864 | -54.5942 | 2026-10-10 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 468a010c-6ad6-3151-b4e2-bf9f08f685ca | -10.9093 | -44.8438 | 2026-10-10 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 94b63fdf-f7e4-375d-a937-3a491e027c65 | -3.1285 | -54.1657 | 2026-10-10 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ebe9af76-ffac-3506-b4a2-cca804a3578e | -14.4726 | -43.956 | 2026-10-10 01:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 23891ffc-2b57-34e8-98ca-1831f43af91c | -3.2031 | -53.8621 | 2026-10-10 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 6a9b017f-3355-366f-a6c3-7708e7c30674 | -10.6013 | -60.4669 | 2026-10-10 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 7a5cc591-e659-3389-bdea-4b9d5902be00 | -4.4506 | -47.9329 | 2026-10-10 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d02917dd-fa78-3518-bbfc-79ddcd716162 | -5.3598 | -45.6751 | 2026-10-10 01:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cd032350-8aea-31e8-8579-0de8992b9942 | -11.0933 | -44.1209 | 2026-10-10 01:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 9eff3ecf-cb92-30ed-be10-900b0eca4342 | -11.0937 | -44.0975 | 2026-10-10 01:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 785a9f6a-855e-3776-895f-3c1b806f782a | -4.4507 | -47.9112 | 2026-10-10 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b745d51d-a1cf-3d35-a1b2-c4505890465e | -22.0909 | -48.9738 | 2026-10-10 01:20:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 1de334a7-aab5-3f12-a641-a825c8b40afb | -12.2329 | -44.6728 | 2026-10-10 01:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| adcc044a-164a-3f36-b6cf-e7cbba426cbb | -11.0745 | -44.1003 | 2026-10-10 01:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| bfc3affe-e725-3f08-bd30-6e2e59a43085 | -3.2203 | -49.4417 | 2026-10-10 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 64a3eb06-58bc-3a5f-9f7e-35a49c7345cb | -3.839 | -55.7997 | 2026-10-10 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 42c5b1b8-d603-3ead-bb56-e321a7da50e2 | -3.6048 | -54.5936 | 2026-10-10 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e9abad28-5a1d-371e-9cdb-829dfda23fe6 | -7.9086 | -54.7194 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 539971dc-4157-3579-8724-197eeb660052 | -3.8391 | -55.7799 | 2026-10-10 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 54921c7a-653f-3938-8140-1f8dc8f02e51 | -1.2723 | -55.7494 | 2026-10-10 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 34062508-8326-31eb-b132-275de447018f | -7.1997 | -55.1427 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 5a2fc640-c41d-3540-ae24-fb6a0bc5281f | -11.0332 | -45.4246 | 2026-10-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 26ab706c-7250-3c4a-abe2-1bb71877c038 | -10.9097 | -44.8206 | 2026-10-10 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 507.6 |
| cb519151-1c7f-3972-ae96-ccc828ffcb30 | -6.4595 | -55.0615 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 46e384f3-3e27-3afc-b729-c5678b0b5f7c | -9.3165 | -47.3851 | 2026-10-10 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 48702c45-be7c-33af-bf48-53fc0f397e9e | -7.0228 | -47.661 | 2026-10-10 01:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 116d7cb0-4f13-346b-b098-ff69271565c8 | -10.8909 | -44.8001 | 2026-10-10 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 347.3 |
| f3d001a2-9d3f-3dc2-b18e-a89106e62b38 | -3.2571 | -54.1824 | 2026-10-10 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4f8fc6e1-41d3-3ef3-8faa-11ebda931092 | -4.5929 | -55.7366 | 2026-10-10 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 245727c9-639b-361e-adbd-f425fd91fd2e | -4.4025 | -49.7774 | 2026-10-10 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 4e27c9f6-4c1e-3cdd-a344-3621e58cea8d | -13.386 | -43.8945 | 2026-10-10 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 10a473cd-a260-3e25-95f8-9fcf135fadd4 | -7.535 | -45.3006 | 2026-10-10 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 51b06763-7af1-393c-9095-a99b66d6352a | -11.0741 | -44.1237 | 2026-10-10 01:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 817f20c3-6b19-392a-bb74-8887e13a4f5a | -7.1995 | -55.1627 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 1e8e68b0-5be7-3391-aadd-8bf580bd1c02 | -10.8905 | -44.8232 | 2026-10-10 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 976.9 |
| 64d2a5a1-27e8-382a-a458-d115bd946967 | -5.7378 | -45.1307 | 2026-10-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 36caf3e7-6a4b-34a4-9cf4-41489b995ed1 | -17.4575 | -45.075 | 2026-10-10 01:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0932dc1a-d1e9-3887-9e85-baa73161fe19 | -6.4411 | -55.0424 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e4467261-f4b2-3249-9a42-c0c2498907a0 | -7.9272 | -54.7182 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| b1b9925f-ff99-3dda-842e-86fcedfb84bc | -12.2851 | -63.361599 | 2026-10-10 01:26:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65b7e585-0fc3-31e9-b4cc-5ab096471964 | -7.5992 | -63.415401 | 2026-10-10 01:26:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3abad14c-08dc-33b9-95f5-12f9bbb07482 | -8.7009 | -62.378899 | 2026-10-10 01:26:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc567a0b-22c8-3a92-b3d3-f6c9d656dca3 | -10.6034 | -60.470501 | 2026-10-10 01:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d359bf8f-a91d-34ea-ba0d-39a97ac2d92f | -10.5898 | -60.457401 | 2026-10-10 01:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dbea45bf-115b-3b72-ab83-1e19d054b07d | -8.5317 | -66.959999 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07bd7522-9134-3fe9-900d-f7b29b7873f2 | -8.6224 | -66.770302 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87e09ff1-fbc6-3732-98be-0330a28a9dea | -10.5995 | -60.454899 | 2026-10-10 01:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10d77886-b4ab-3741-9611-c3ab98179898 | -5.0774 | -60.213501 | 2026-10-10 01:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00190f36-eccb-32d3-aca7-371f92d35831 | -12.3069 | -63.366299 | 2026-10-10 01:26:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f2b8260f-37b1-33c4-9c46-5fc5c42b8f82 | -5.0629 | -60.1959 | 2026-10-10 01:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35bd1f52-ca56-3437-a885-f1d33a5ee289 | -3.9713 | -59.325401 | 2026-10-10 01:26:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d537f5b-903a-3625-9e13-c624b0f8aa0b | -9.2484 | -62.2966 | 2026-10-10 01:26:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 483ded08-f82f-33f6-99d1-0bea62c7f19a | -9.0837 | -61.036598 | 2026-10-10 01:26:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e987241e-75b9-3239-a32a-ad2e931b4835 | -12.2948 | -63.3592 | 2026-10-10 01:26:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51daa029-e98d-3832-845d-e8b913f82d51 | -5.2322 | -60.1758 | 2026-10-10 01:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6a50f36-b8f1-30e8-a60d-5b89f71a022d | -6.4849 | -62.8503 | 2026-10-10 01:26:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ae39029-aacb-3a4c-a311-9e636fed30bb | -8.5334 | -66.9673 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78660ef2-ac01-3e37-bb7e-612b048d584a | -8.6241 | -66.777603 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d7fdd35a-acad-3b48-959c-298230df8d16 | -8.5188 | -66.9935 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16c07a71-2d2a-363c-9b06-33c0d68df655 | -10.6073 | -60.486099 | 2026-10-10 01:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0fcc62ce-16b9-375e-ad59-862e1e056ee2 | 2.7352 | -60.2616 | 2026-10-10 01:26:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0377f0aa-8e2b-3b65-93f4-9f0b3b7fa8bb | -8.6815 | -62.383701 | 2026-10-10 01:26:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| db0dee76-2188-30f9-a469-91de34ebd36e | -5.0677 | -60.215801 | 2026-10-10 01:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88927e87-83ae-3f2a-908a-1eafe1e10769 | -7.5939 | -63.3932 | 2026-10-10 01:26:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a814f9a-8694-3244-8e5b-a202c38fe647 | -5.087 | -60.211102 | 2026-10-10 01:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0292d15-67b1-3186-9142-9aae9126cb70 | -8.5156 | -67.024696 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09e36360-f6a7-34c2-ad4f-b20566b5d948 | -8.5678 | -66.9823 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df3b8742-aa57-3c60-a5e8-52df56c242a7 | -5.1789 | -60.293598 | 2026-10-10 01:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee854a24-4258-30a6-af22-57eda955b4ed | -12.3046 | -63.356701 | 2026-10-10 01:26:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 39cfcdd3-f1ae-3886-ba8a-1b95cd373ba5 | -9.3678 | -64.648804 | 2026-10-10 01:26:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ce62061a-75e2-343a-8611-64efcc77bb80 | -7.4529 | -63.623699 | 2026-10-10 01:26:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a75a93b-ef4b-3423-8f4b-dee2fff8bfb9 | -12.3023 | -63.347 | 2026-10-10 01:26:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a90f86b2-9ad1-39c9-989e-e81eb09cb1db | -5.0726 | -60.1936 | 2026-10-10 01:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bea42de-5db9-3296-b07b-33e515f6a16d | -7.5966 | -63.404301 | 2026-10-10 01:26:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f4369e5-cc5d-399c-871c-a82395b079e8 | -10.5937 | -60.473 | 2026-10-10 01:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b08784d3-d6b3-3451-b62a-06fd473d58da | -12.2971 | -63.368801 | 2026-10-10 01:26:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 05e0589a-bc7f-3ae0-b202-8b6f2bdf52cb | -8.671 | -67.117699 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bee56cf-2fe6-3c40-8858-bf7fcc9ecf49 | -3.9772 | -59.3493 | 2026-10-10 01:26:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e668e12-c095-33d9-adad-fe6ccc3068e5 | -12.2925 | -63.349499 | 2026-10-10 01:26:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b4fa771-259f-33be-a9b7-2ae559796306 | -8.5171 | -66.986298 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e3bf916-9e45-3856-a2ab-3e5a43c8d46f | -6.4819 | -62.837799 | 2026-10-10 01:26:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
