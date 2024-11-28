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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1066f969-797a-392d-8bcb-988fbbae55bd | -2.69922 | -51.68462 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec6d2f2f-3274-364f-a0a3-77f3edc67418 | -2.63977 | -51.90255 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f15e7d6b-35d5-3f07-bf22-a9abbf282169 | -3.29511 | -51.15602 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dbbb1fa-b8f6-3ff3-b6cd-cc4652a50a5a | -2.69855 | -51.68914 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5829fe8c-832d-3cdc-9565-b65d6df7300c | -4.17327 | -48.45239 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b76ac0d-bc78-36b2-83a0-b0faf5df64db | -8.56543 | -49.20025 | 2024-11-28 05:18:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6ecf388-48b2-3389-9da2-02a4b5621ac7 | -4.22143 | -50.88668 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98b372a9-a719-30ec-b388-829d6cb63d83 | -3.50446 | -50.49434 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad39d3a1-989f-330a-bf86-5f9eb6d033d3 | -3.24063 | -53.63403 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9b78cc2-0e60-3a5a-a9b2-f4233e19a3f5 | -6.36222 | -47.06134 | 2024-11-28 05:18:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a465883-f8f1-3a6e-98d9-c14baf4d66fc | -3.18028 | -54.32428 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1968d764-758c-3a44-83ed-8b31ff192005 | -5.98647 | -45.36423 | 2024-11-28 05:18:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| dc1d4a58-d0b3-3532-8657-23073b409c55 | -2.96151 | -53.88189 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96ab5cf6-179f-3916-9562-fa06b77c0c92 | -3.08224 | -54.56149 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5a467e3-c756-3a5a-b5a0-aa7fdc8dca8b | -6.08952 | -48.03838 | 2024-11-28 05:18:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60b6cc1c-ce89-3dea-8f15-ef78bc06a239 | -3.08697 | -49.2187 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07239a6c-e89c-3a5e-b5cb-c60be4e53cee | -2.63313 | -51.77357 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fdd5cd5f-7454-376c-b476-0401676a1957 | -2.91115 | -54.18551 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f85179ff-1183-379d-9809-3b20f419b72b | -2.73135 | -54.39848 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f65b743-08ed-3fee-b707-f322f6718261 | -3.10125 | -53.8081 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d7ac13c-9676-3413-8f5a-23ab03637e7a | -3.06219 | -51.29896 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f5e00fd-2e15-34d6-91be-6eb6785982d1 | -3.26107 | -50.43742 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f546820-5e1e-3be8-b4b4-6979c8253ae5 | -3.72381 | -50.18488 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68578b67-9689-3565-8afb-2790fe03e40c | -4.32138 | -49.38955 | 2024-11-28 05:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9e9c77e-d636-39c7-86f3-0be10f00a710 | -3.15376 | -50.58545 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b5da0f6-f039-3b5e-8c96-29c8f84dc8da | -2.80063 | -53.04663 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33affa6f-a596-3eee-8b3b-85e0bb68cd50 | -4.05695 | -48.83558 | 2024-11-28 05:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11a24dc6-29ed-3f05-bdeb-81fbdd482e82 | -3.56994 | -53.02132 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0164b538-4705-338f-a0e7-da63f12e52f4 | -2.72712 | -51.74448 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed02f954-d128-337b-9fdc-d7d082a3b34d | -3.23981 | -51.54983 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f0943e18-4c13-3448-a591-fcbdd4f7ce7b | -3.07546 | -50.98954 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 42238084-6906-32eb-b221-05a59da724c8 | -3.0855 | -54.12905 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66bee359-97d5-352c-a5fb-bec5faec2f09 | -3.75043 | -52.39526 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9f087df-64c4-37d2-8968-b9d654b8c1dd | -3.33126 | -53.72296 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f02e2f57-9fc4-3386-9479-386ba4a91ed1 | -1.99129 | -53.29781 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6414fa0-26e9-3f96-94fd-e6a283bd3b37 | -3.96508 | -48.07908 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1ce6a0ae-0ac9-3b7e-bb9c-b9af27f4f366 | -3.14733 | -51.29293 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd87fc12-a374-3ed3-bb80-c5b7ba53a968 | -3.24914 | -53.63175 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4afafffb-af9c-3e5b-af8f-8c69a3777d1e | -2.59508 | -54.07214 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f25c21ef-2449-3347-a41d-af9b43c3718b | -3.05405 | -52.76056 | 2024-11-28 05:18:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd2af580-37e9-3b51-ba4a-06818a13d05a | -3.27003 | -53.30722 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4236c7a2-1933-3692-898f-9750ec47fc6d | -3.53325 | -50.19374 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1b118b0-4af9-3c95-9593-2a83a474b2a9 | -2.9346 | -54.3345 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d30a60da-09da-3477-88cb-87bf2dc3d0e7 | -3.30325 | -54.1752 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 499a5c87-e558-3245-8b5d-a4dbced2512c | -3.8557 | -50.12528 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe2f86e9-ad33-3ce6-8e3b-ba68c3fc8995 | -3.26886 | -50.61999 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5651ca1-caed-3260-bd3c-695db5e45d4a | -3.96604 | -54.61179 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a71a94b9-0085-3341-bc70-bc4f83392069 | -3.25351 | -48.89045 | 2024-11-28 05:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7389e05a-b752-39aa-b07b-94bcc5327aa5 | -2.23619 | -53.68645 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4128830-3bed-3153-8174-fc0e4016ceaa | -4.22065 | -50.89209 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 293bda9a-6143-3026-9605-50e84da505b7 | -2.82537 | -54.08804 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a2054709-b95a-3a46-83d3-63d900b0415a | -3.27465 | -53.30429 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f86a28c-ef15-3cf5-a938-02ccc347dd78 | -2.42586 | -54.01705 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 67b18802-812d-375b-9c1a-a64ed8b28e5d | -2.82188 | -54.0335 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 964f5d37-c043-3709-9eb3-ed7e34a5a1e1 | -2.3683 | -56.11739 | 2024-11-28 05:18:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8bd77d6-ed76-36fa-9af4-c974c702ff03 | -3.55095 | -51.51086 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 419574fe-8f90-3811-aed0-95e4b3a94b34 | -3.24422 | -50.20478 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7742c2c0-cc76-3dcc-82a4-ea0f297ac0b6 | -2.17615 | -52.13685 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1325790-86db-3623-b212-981e65c14907 | -3.26634 | -45.37524 | 2024-11-28 05:18:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0551e31a-572c-3da0-b45a-e6cc2bd99595 | -3.2741 | -53.30787 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 639586e8-24cc-3c92-9256-2a5a898df944 | -2.79649 | -54.12257 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e05c55c0-d16e-3651-b8b9-b223c1cd0dc3 | -3.2486 | -53.63525 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3ea7138f-f52a-310f-aec7-78ef95e78fcb | -3.32107 | -50.91981 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbd56f5b-b6af-3a23-b152-80d4b375c0a4 | -3.78674 | -51.75437 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d833e7e-dfc1-3085-88b7-b03eb6b2eb96 | -2.80379 | -51.58194 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| df4aa384-4c57-35cf-988b-1e87ff7a2606 | -2.97169 | -53.89368 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b45952e-79c8-370b-afcd-2269e464395e | -2.807 | -51.59177 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d265b440-23f7-3a04-8d14-982ecbf7e3a6 | -4.02177 | -49.54332 | 2024-11-28 05:18:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6c43f99-25d1-3da0-86d6-68fe7c598678 | -3.07856 | -50.96893 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d8c0877f-65f6-35ca-b300-9f75359aae43 | -2.73156 | -54.13684 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49c88e09-4edc-3201-89d8-e6ac39d646de | -2.95836 | -53.87638 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab289ec2-7d85-392b-9481-b81defee02a1 | -3.25138 | -50.61929 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5dbe0005-e1aa-39a8-9762-5cda9a291c8a | -2.74004 | -51.65852 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebc810c5-931d-3131-8fd9-69ebe2f23472 | -3.96798 | -50.18526 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 41e7cbe4-1235-3b04-964b-488a85620dc5 | -2.69523 | -51.98627 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d57f5415-42b6-39d2-985a-69567139a6d4 | -3.45861 | -54.48274 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8562c685-48b6-3374-b1d7-8a4c9043b197 | -3.5117 | -50.50636 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f917fe0-7b03-3b7c-ac67-a244da526b9a | -2.25564 | -53.7465 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6be92fd-b592-3cc3-840b-b0d9baebab76 | -3.43901 | -54.53656 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c47dd599-b3f1-359a-b417-cc51b47bb648 | -3.7496 | -51.77983 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6b2b307-601b-3c5e-b59f-7edf2353fbdf | -3.0416 | -54.04114 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc148070-8a90-3d7e-9a91-548cf919de34 | -3.09368 | -50.35972 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48747904-6ead-31c8-9d07-06a5912fd4f2 | -2.91095 | -51.71278 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0bda2810-d2d4-3afb-bf1a-537d034e1043 | -3.49445 | -53.80896 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cffba28-22b0-39a7-b0b9-019b14d69fe0 | -2.17799 | -52.13518 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7fd8e6a7-6255-33da-809b-6cfa2b8b91ff | -3.59009 | -50.36108 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c11fda87-1935-3a30-805d-f8b425a9103f | -6.37859 | -45.69602 | 2024-11-28 05:18:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bdcb58d5-fbba-3fae-8ff8-fb24ee38c06f | -3.10518 | -53.8087 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c8ff2cf8-7b33-3d03-87b0-4d4996eb9d98 | -2.13548 | -54.84851 | 2024-11-28 05:18:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5735cb9d-7280-3739-b39e-fdb0f11fe2d5 | -4.31489 | -48.08107 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5d86a25-ee3b-3200-844a-6f9d06eb795d | -2.31702 | -51.95634 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| afc37fa4-13a9-37af-a44f-f9a5e0fd3484 | -3.05972 | -53.68274 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 434080f1-97a5-3379-9864-d0c8e9b467e8 | -3.49036 | -50.44599 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03ff9c92-8ab5-3a77-8d93-1e20fd65361a | -3.04293 | -50.97917 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a176309-8fe9-3ffe-b635-1bba26b5fca8 | -3.24848 | -50.62231 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f82f687d-da78-3912-88b9-f2cac0028b0c | -3.4937 | -53.81393 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dda2a823-f57a-38b9-b1d0-64e1eefb1ca3 | -3.31636 | -50.03121 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3a32f78-ddd6-3bca-a439-6cd6010f7c67 | -3.59511 | -50.36174 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e728f1d-44d2-39ff-9c52-2a312ae59795 | -2.96021 | -51.00711 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2dd5707c-332b-3db3-9949-2ceefebac002 | -2.60694 | -54.27303 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README86.md)
