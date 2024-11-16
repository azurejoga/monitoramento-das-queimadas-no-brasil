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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88e917cb-bc90-3c96-9c97-c1baa21a10ec | -2.55702 | -46.89692 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f23d8706-3080-3895-a43e-93580a85d5b1 | -2.79037 | -48.57002 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| e5321249-2c56-34a5-ab0a-2edca0379582 | -1.70704 | -46.16009 | 2024-11-16 04:23:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88c53442-a06c-396f-b494-dfc0631f18f7 | -3.24931 | -47.90554 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac4bd07b-e124-3fda-a6a3-f7292d61cb05 | -3.03237 | -48.09004 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 283e9d27-74ba-3ff9-b0a9-2bfc0de97617 | -3.35449 | -46.64507 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20aeaae0-154d-36e1-9cae-0c5892b50387 | -2.28448 | -48.46672 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac64dd8a-51fc-3b2a-8df4-2b8d4b2b4f56 | -1.99648 | -46.57997 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62007ca7-7d7d-3bed-8b5d-0aca8d2cc3c6 | -2.11361 | -48.20296 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 805f5914-f84e-35c2-938f-00f78eb9a664 | -3.61553 | -44.7922 | 2024-11-16 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ad0e59d-1c30-3d1a-8a3f-dffbcb40dc34 | -2.04654 | -53.9511 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cc6e8f5-7b1b-38da-a974-e6a9569f9703 | -1.69142 | -48.46678 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63d63211-10c0-38ba-863e-eebeb555ca52 | -2.14173 | -48.95605 | 2024-11-16 04:23:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caaf3d5e-a5a0-320d-a7ef-4abbe1237067 | -5.21741 | -43.79007 | 2024-11-16 04:23:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22f3110c-8124-32a2-b03b-df02560d17ed | -2.64014 | -46.1941 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc372de2-2c49-3fb8-8917-ce0a4b9680fb | -3.12833 | -45.88836 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6bd23bf-5ddc-353a-b64f-67aacdece504 | -2.23519 | -46.83587 | 2024-11-16 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf5e2082-a786-346f-995a-18f6aa74c3fc | -3.94894 | -50.20543 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cb94643-0fe5-37e7-ad86-0c58839e215a | -5.66589 | -35.64513 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 45ca8fe2-8208-39b4-82e3-6334ded80d2c | -3.20441 | -45.74844 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b98c0c08-29b2-3db1-8e7c-926935e75f60 | -3.87899 | -44.49191 | 2024-11-16 04:23:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5a2d7a6-52c6-34ba-b070-62256c865ad0 | -3.94898 | -46.71276 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02026803-2592-3e70-8571-dd1dbab18d2b | -1.37737 | -54.1505 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5cec6bb-d37d-348f-b9c3-750ace0d2d0b | -1.89714 | -47.00912 | 2024-11-16 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5c86596-d786-3b3a-b08f-c00c8d3c715c | -1.85829 | -46.2813 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e42cef9a-d3db-3c7f-b837-513ae287d069 | -1.36416 | -47.17278 | 2024-11-16 04:23:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43734d8c-ce32-3e18-bb21-acd5a51fb478 | -2.5576 | -46.89329 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 123aeb0f-632f-3f8e-92a5-c3ce5c548f4d | -2.13256 | -50.81589 | 2024-11-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9188f15c-4bb7-3bf7-99df-6ca59bbcafe8 | -3.92857 | -45.85451 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| acf4534a-4c87-328a-afcb-1bb5cbbe9cb5 | -3.68747 | -50.112 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3c5d195-ca83-30a8-a973-c0aaafb6701c | -2.22503 | -48.37213 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aff3c5fe-1856-375d-837a-151d427a0678 | -3.85152 | -46.64255 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fc0a986-c263-3032-ab23-2f2a7dc13151 | -2.85226 | -46.62519 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0756b83c-cdab-3cfa-b755-5f9956d31e91 | -3.96684 | -49.99539 | 2024-11-16 04:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43f54049-9b53-3d7f-8bbc-adddf3d32bf4 | -3.49556 | -47.20971 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03bcdc00-27a1-3ef0-8c22-e88874edfd14 | -2.71368 | -47.99063 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90f0d3c7-1bed-35d7-9155-4396c9284c75 | -5.24108 | -44.91165 | 2024-11-16 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c7cd7bbf-6f2c-354e-90bd-ef845bf3f6ad | -2.12863 | -48.8913 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b2e7399-bddb-3dba-bc20-1353a9dad20b | -4.10938 | -46.10313 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f6d282f-6353-3f2a-99e8-97c70cb3e7c6 | -3.50276 | -45.44483 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 375ec68d-bdec-310b-9438-a523ef368a5f | -3.04387 | -47.97437 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb7489e1-7366-3ec3-9d2e-1aab6c5ee445 | -2.79864 | -46.64984 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| def73d42-4881-3fef-a576-fe5cfdab82c6 | -3.59765 | -50.35096 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 349fa57a-500f-3a98-8cef-bfea5a8c3103 | -2.13727 | -48.12283 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| caa8a89a-316f-3c4b-9a2a-aa82c382888b | -2.77378 | -48.58033 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 16465969-3e94-3aa1-9b5f-7df9ff5d3267 | -2.65296 | -46.19971 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bdba02d-2c1d-3537-8e3d-34c3aa15980c | -3.73982 | -45.6553 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3bc9e8cc-f40e-322a-96a8-b622e0cbbc5f | -3.65319 | -45.49697 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c8d2319-f5e8-3dc5-b1f3-69aabd564290 | -3.4978 | -47.21756 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eb35943e-1bf7-32b1-a3eb-cf80f6dada70 | -3.41302 | -42.38428 | 2024-11-16 04:23:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| db0dc2d1-2ab6-3856-91d8-ef9ff082f8fd | -4.37185 | -45.62376 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e708bb98-ad32-3664-b067-0d9a03fd470f | -4.11088 | -46.90565 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d5219a7-55cc-3f63-9a54-f8dc958eda21 | -4.2256 | -50.67725 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc37f5c0-d804-3b8b-98c9-b393548bb05b | -5.14093 | -37.69833 | 2024-11-16 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bb1c6355-e6cf-3c37-a3d6-15e2d8c95c8e | -1.46185 | -48.19747 | 2024-11-16 04:23:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83dcf6fc-e1f2-3259-b38e-f41d52ef2add | -2.35486 | -49.11965 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a8cc9dbb-5fa8-38e8-bc78-7c02ad698bc9 | -2.10303 | -46.58943 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79233686-e9eb-395d-aac6-3b29380c00f0 | -2.66409 | -46.19428 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a4763d3-81e8-372f-a353-04d09c936167 | -1.86446 | -54.28078 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b1ad6e8-e828-31cd-b9d3-e8310bf58561 | 2.66127 | -50.89104 | 2024-11-16 04:23:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57299e0f-af4d-3064-925b-d6019495c877 | -2.67133 | -46.19183 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ab19112-5cb5-375b-a660-476ce99a2b81 | -2.19319 | -46.6182 | 2024-11-16 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23dfa525-4db3-3161-b689-35a08f7d5190 | -3.19378 | -46.54016 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e344bf02-3440-3059-8ae3-795fe719ecee | -2.51875 | -46.32238 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30b5ca37-1bc9-3b40-9db1-bc4ddc5d3f57 | -2.6392 | -46.55946 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 784668fa-0365-37a8-a02f-14a8df66b44a | -3.28185 | -46.2442 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7be98635-c032-30cb-b422-45f71baf7748 | -3.12357 | -45.74585 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 918ca231-bec8-3c26-b680-f04a5f923689 | -4.25312 | -45.90241 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d12cfa9-9fc7-3d23-b2f5-56aeb23480eb | -2.89874 | -48.31373 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acffa4de-a620-34bc-be9b-4e3af6e50cbc | -3.73595 | -45.65824 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| a5a5bfdf-c26a-389f-849b-9c3581c2ed4b | -3.76127 | -44.39713 | 2024-11-16 04:23:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0db55dce-3d76-3614-b231-d3f1dfb1ec9f | -3.49839 | -47.2139 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca5b7bb1-7bb3-380c-89e3-c25b8bb0eca6 | -2.74371 | -48.55833 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 953d9eba-33df-345e-a6f8-fa7150fc59a7 | -3.97104 | -45.801 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61ce1a30-70be-3ff7-91cc-2e812f4ebc1b | -4.99893 | -44.31956 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 157e1b61-8ba7-39ab-91b4-00e62fc6be0b | -5.14616 | -37.70427 | 2024-11-16 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3958cb29-819b-395c-a452-803d5e69c91a | -3.15204 | -44.03088 | 2024-11-16 04:23:00 | NPP-375D | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 505ef9b9-5755-33bf-96ae-93f00c601d57 | -3.50122 | -47.21808 | 2024-11-16 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a3d07c3-103a-3813-8f99-cf79ac597f9a | -4.73204 | -43.25309 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 338a5884-d428-3c8c-ba1f-db1c3165fd30 | -4.99215 | -44.31851 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| e693317c-f85f-3e92-9d6c-6a2754a9cb45 | -2.46003 | -46.3675 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 370c1c42-3408-3b9b-a668-fe9938f75bd3 | -2.90299 | -48.3102 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d2d3f6b-fa5a-3f3a-b3c2-deee8058f340 | -1.64376 | -50.44473 | 2024-11-16 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebeddce4-d746-3375-973d-6e947453fa7f | -3.78019 | -50.10888 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 999317a9-761d-3872-9b36-d36c16473a76 | -3.54296 | -51.49168 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e81f241-e1e1-3ed1-b857-9e6f9e3ddc9b | -4.36345 | -45.86637 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30c35fbe-904a-3a35-bb74-f39facb8b8b1 | -2.3579 | -49.12482 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49fab15a-00cf-34aa-afd3-2768c73d4d79 | -3.23265 | -45.39884 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bab7cc35-d694-358b-81a5-86ca3250bc28 | -1.95939 | -46.2171 | 2024-11-16 04:23:00 | NPP-375D | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4670b456-5897-35d8-b3e9-76f26058089b | -2.62404 | -46.82904 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c54cc3-244d-32e7-85a5-7f75b79f247b | -1.12698 | -47.16829 | 2024-11-16 04:23:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 357cfff4-4b56-300a-8446-4cf170452dfe | -1.71039 | -46.16061 | 2024-11-16 04:23:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 712a2469-8d3c-3d20-97de-1976a0695ed9 | -3.2458 | -47.90498 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0f8a66d-bdee-34ba-b1ae-2a1fc3680e21 | -2.58839 | -48.9411 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6dcbe987-ae05-303a-992d-3f205a85fb23 | -4.40294 | -40.69363 | 2024-11-16 04:23:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0f280d84-c6d3-3a62-8ec6-4d02f4568bd2 | -3.27124 | -45.49727 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 117015e1-c4db-3121-93d9-dc122c2c3c36 | -3.69533 | -50.1133 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a4e67099-8227-3d07-99a9-754a94279e2b | -4.36799 | -45.62669 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10c4110c-4604-3670-9bc0-4adb81ed6593 | -3.28403 | -46.20872 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f96e233f-fd57-30c1-aa3b-474ee3acbf0f | -2.35633 | -49.11054 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README31.md)
