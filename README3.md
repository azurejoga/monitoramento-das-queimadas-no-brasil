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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fd210fc-33da-373d-bba2-40210fa6acdd | -12.35418 | -54.5169 | 2025-05-04 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbba852e-93c0-3a78-a68a-2d1e9d6e5d10 | -11.39526 | -52.94529 | 2025-05-04 04:59:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 677aef3e-0a79-38e6-9cf8-2c90eb6d3774 | -12.53983 | -57.73219 | 2025-05-04 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3ab71cf-94d7-33b9-9a7a-4f1c551d1bf3 | -13.71048 | -45.20808 | 2025-05-04 04:59:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa4e288c-91f5-3dda-80df-aefba8465dfb | -11.39117 | -52.94869 | 2025-05-04 04:59:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b25a81d0-7a4f-3405-a55a-75de475f8565 | -13.05172 | -53.71065 | 2025-05-04 04:59:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63b356a3-090b-3369-9a7a-b3408b1e18c6 | -13.53591 | -52.9647 | 2025-05-04 04:59:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d15deb93-8a8a-3c11-983c-d0aed5594b90 | -11.39235 | -52.94081 | 2025-05-04 04:59:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc4c63e8-ef6f-31a7-8113-dfd9e9cbae2e | -13.70671 | -45.20854 | 2025-05-04 04:59:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c900fa3-70f7-3811-86be-2b7fd2bcda3f | -12.5392 | -57.73601 | 2025-05-04 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44e1aa10-473d-3fc4-a038-bf3d440dfb3a | -13.04827 | -53.71012 | 2025-05-04 04:59:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3449fad6-f361-3725-ba2a-39a2ff5300c1 | -13.53294 | -52.95998 | 2025-05-04 04:59:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfd93353-efc3-3726-9e68-b35850103603 | -13.70776 | -45.19962 | 2025-05-04 04:59:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c70333e3-9b43-3ba0-a89e-5908a2a6e2bb | -11.39467 | -52.94922 | 2025-05-04 04:59:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6082fe2a-bd1e-388e-bd15-6ce05589c533 | -13.53529 | -52.96889 | 2025-05-04 04:59:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56e23e9f-8ac7-37d4-a455-4ac71da031a7 | -13.71313 | -45.20472 | 2025-05-04 04:59:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4be6795-f23c-37a9-9ea2-f71240348502 | -13.54306 | -52.96581 | 2025-05-04 04:59:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18613557-ffb9-313e-b31f-63bebe509ab5 | -8.30883 | -55.1006 | 2025-05-04 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdaa8798-4fd1-32b4-ac8d-083c7359740f | -13.53171 | -52.96835 | 2025-05-04 04:59:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36c4dcd7-f930-362b-b138-b6581d1553d3 | -12.53574 | -57.7354 | 2025-05-04 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a0053dd-0a4c-3582-a37b-af350f5bcd63 | -13.53652 | -52.96053 | 2025-05-04 04:59:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27ffc455-3e64-371d-b27d-ca06ad763e7f | -11.39176 | -52.94475 | 2025-05-04 04:59:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55e08ef5-607e-3bb8-8c7b-ef2fa0477e50 | -18.57795 | -55.53466 | 2025-05-04 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 08df837b-83a2-3cca-8e99-4097d6fb71b9 | -19.04738 | -54.37341 | 2025-05-04 05:01:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f074794-676f-3334-af8c-39d6baf4e5cc | -15.46282 | -42.90446 | 2025-05-04 05:01:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d35c3b1-a718-340b-bfd2-7d5377a6799a | -19.8168 | -54.49716 | 2025-05-04 05:01:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5677ee3-439e-39e4-8b09-786888ff31f3 | -19.57446 | -49.68247 | 2025-05-04 05:01:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 066f91fa-c505-38ce-821a-00217b0da65c | -19.56973 | -49.68184 | 2025-05-04 05:01:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4b675fee-5d6f-34a4-8535-17d9f248ead9 | -19.81465 | -54.49909 | 2025-05-04 05:01:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31fc455b-b266-3d21-8f5b-f2f3c90de7d7 | -19.04677 | -54.37763 | 2025-05-04 05:01:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d9157b5-bee6-3a06-b715-f22000e2fcfc | -17.62099 | -50.91756 | 2025-05-04 05:01:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bd667a5-328c-3643-beaa-9629d66174d4 | -19.04382 | -54.37284 | 2025-05-04 05:01:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75aee44e-7417-3cac-a189-9159ba9b52fb | -15.0783 | -48.94645 | 2025-05-04 05:01:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a1555b2-c2f8-3f92-8882-a0efe98f25fc | -19.81323 | -54.49661 | 2025-05-04 05:01:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4688ff8d-c4d1-3258-8f58-b0737d5b7e57 | -27.76248 | -48.92157 | 2025-05-04 05:04:00 | NPP-375D | ÁGUAS MORNAS | SANTA CATARINA | Brasil | 4200606 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d23c1ea2-35e8-3241-988e-9621fa9132b2 | -27.75704 | -48.92039 | 2025-05-04 05:04:00 | NPP-375D | ÁGUAS MORNAS | SANTA CATARINA | Brasil | 4200606 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ec416dd4-2cb9-39da-87c9-877884415833 | -22.24501 | -52.98049 | 2025-05-04 05:04:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 86ef4da6-8955-3819-b39a-b62fb79b759b | -29.89403 | -52.44198 | 2025-05-04 05:06:00 | NPP-375D | SANTA CRUZ DO SUL | RIO GRANDE DO SUL | Brasil | 4316808 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 92f60a00-cdd1-3299-af7d-6b7d96f20c85 | -2.95311 | -60.01424 | 2025-05-04 05:21:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67117f83-fb76-3f6c-adf5-5ad2ad716fb7 | -5.30194 | -55.9719 | 2025-05-04 05:21:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38c19326-bb34-303e-8288-1d857dc6c26e | -19.04502 | -54.37208 | 2025-05-04 05:23:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87f923fe-b0c1-3165-b272-41fe95a9f21f | -19.04466 | -54.37539 | 2025-05-04 05:23:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4292f80-4d49-3529-af86-ff6c1d1fa59e | -11.38928 | -52.94453 | 2025-05-04 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 121021fb-1ef7-3521-b7ae-2fa7a872daa3 | -19.81295 | -54.49712 | 2025-05-04 05:23:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3dd7ae0a-160e-3c77-84c9-d2b565aaa517 | -13.04859 | -53.71555 | 2025-05-04 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02ee1dab-0941-3943-abeb-85b0032619a8 | -11.39404 | -52.94831 | 2025-05-04 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7383b067-0dc4-3ea0-91fa-23d7b6bc136f | -19.04948 | -54.37935 | 2025-05-04 05:23:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91742752-f5ce-3aba-b06c-9184a3bb607a | -8.30805 | -55.10091 | 2025-05-04 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 164d9747-45ad-3e56-9691-c8c725fa65ad | -11.39443 | -52.94521 | 2025-05-04 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2fe625f-5174-3c82-940d-acffd43ef6c3 | -19.81815 | -54.49762 | 2025-05-04 05:25:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 20654b09-71ec-3c62-a7cd-2a72431c630f | -11.39665 | -52.93628 | 2025-05-04 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 06cb020e-ddb6-3398-a105-8ffa4e513488 | -11.39333 | -52.94314 | 2025-05-04 06:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 6c348aa1-422a-3ab8-9c9c-5c79171b4645 | -6.75398 | -36.69608 | 2025-05-04 11:38:00 | TERRA_M-M | PARELHAS | RIO GRANDE DO NORTE | Brasil | 2408904 | 24 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 3c43e6ef-e949-3246-99f1-884eb49c2c6e | -13.71898 | -45.22049 | 2025-05-04 11:40:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 6d2c2d04-3133-358c-9d42-bccc24dc83b7 | -13.72515 | -45.18651 | 2025-05-04 11:40:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3ebbba9e-7ac1-3c66-8c0c-ab4ee780a55f | -13.71657 | -45.19257 | 2025-05-04 11:40:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 46c45105-0aa6-3c4e-9ea4-0430256fe126 | -13.7075 | -45.1988 | 2025-05-04 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f1b4489f-1136-3e9d-bee3-6b7bc79ac465 | -13.7075 | -45.1988 | 2025-05-04 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 7db2ca16-a435-3391-806e-b0c347e367cd | -13.7075 | -45.1988 | 2025-05-04 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 705c2c2f-e568-3611-9c91-5c7c889d0a3a | -13.7269 | -45.1955 | 2025-05-04 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 3c1d518b-da9b-384a-8182-43afc20c0385 | -13.7269 | -45.1955 | 2025-05-04 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d537dd91-3617-39b5-aa51-97104606245c | -13.7075 | -45.1988 | 2025-05-04 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 4978a2ed-6e41-37da-a7e8-7841ad8148bf | -13.7269 | -45.1955 | 2025-05-04 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 1a2107df-b261-34f0-9652-aad03ae627e5 | -10.4925 | -49.8099 | 2025-05-04 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c167a025-a25d-3f02-bde9-f30980c71aef | -10.4925 | -49.8099 | 2025-05-04 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |


