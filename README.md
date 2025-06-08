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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef0c934a-94d5-380d-a585-da86ee21a396 | -12.3636 | -57.416 | 2025-06-08 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| c0ad1e9b-e79a-3bf6-8349-f4e4b5698cb3 | -12.3638 | -57.396 | 2025-06-08 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| be435ea9-8cc9-358d-9cf1-28bdaee04009 | -11.6316 | -48.4837 | 2025-06-08 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 245299ba-a3a6-342d-b696-05b7daa65aad | -12.3828 | -57.3944 | 2025-06-08 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2d256163-9a1f-3908-b422-eac7a2717815 | -7.7364 | -44.1592 | 2025-06-08 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 495ce0a7-ffde-31ee-98cb-047c3fbf471a | -7.0169 | -44.5954 | 2025-06-08 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| c7e21faa-4a24-366a-a66f-f2ec8c6ffc88 | -7.7361 | -44.1823 | 2025-06-08 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| babe8dd2-9b82-3765-8135-5ffc657ffba7 | -12.3826 | -57.4144 | 2025-06-08 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 7ce89538-4fb7-3afe-a22b-e7578e9382d6 | -7.0169 | -44.5954 | 2025-06-08 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| df46d770-b16b-38e4-81ec-d1b469dfb26e | -12.3638 | -57.396 | 2025-06-08 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3a193a0d-19a7-3502-b216-a52a2ffc9ea7 | -13.4733 | -56.8557 | 2025-06-08 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 860666cd-b485-3608-a671-b28e89360da1 | -12.3636 | -57.416 | 2025-06-08 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d9575e5f-a517-3660-9828-8779258eb29b | -12.3828 | -57.3944 | 2025-06-08 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 7c001331-2f69-3c01-ba36-56d1201fbff2 | -12.3826 | -57.4144 | 2025-06-08 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4af332e4-8a76-35f1-b178-5d71f05fbe3a | -11.1295 | -54.6391 | 2025-06-08 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| c7179b95-c2d9-3bb1-9ef7-b9a4f2e69825 | -12.3636 | -57.416 | 2025-06-08 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c506bcba-b7b4-3d50-835d-e3769059f263 | -7.7361 | -44.1823 | 2025-06-08 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9d27c119-9475-3157-adb6-6d9107c23562 | -11.6316 | -48.4837 | 2025-06-08 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8ac51869-9b6d-3eab-8864-c46cdd85f6ab | -12.3638 | -57.396 | 2025-06-08 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 64986e39-0e7e-3a52-9e44-d813f0278fe4 | -12.3828 | -57.3944 | 2025-06-08 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3e68cd86-d694-3c1e-8634-a641d7125d0d | -7.0169 | -44.5954 | 2025-06-08 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| d5e16dc4-7d2b-3e89-ad92-38909a3d12a1 | -7.7364 | -44.1592 | 2025-06-08 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 7d5b5f4f-353e-3634-b1d3-9b2878478488 | -12.3826 | -57.4144 | 2025-06-08 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 522f7ff4-b713-3a02-bd04-ec9967e090d2 | -7.026 | -44.597401 | 2025-06-08 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a21148d1-609e-3105-90ba-82e5916cf4db | -10.7973 | -43.370098 | 2025-06-08 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 62e1ad18-cb00-38aa-a7dd-c1d592109561 | -7.8722 | -47.899502 | 2025-06-08 00:24:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 390a26e8-87b7-300c-8fd2-f7861a16a7c0 | -6.4976 | -47.494099 | 2025-06-08 00:24:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1652e6b-5902-32fa-b595-d5fead063142 | -11.8051 | -48.0769 | 2025-06-08 00:24:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e2548c0-f592-3510-aab9-7447d431fda3 | -7.7319 | -44.168701 | 2025-06-08 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8cde6493-0e05-37ae-99cf-01baacad49a5 | -7.8624 | -47.901699 | 2025-06-08 00:24:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 872009ff-1813-35ad-adb6-bddc72734a2b | -7.8686 | -47.882801 | 2025-06-08 00:24:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 905c8b39-883c-311b-a5df-b5ead2d9aa51 | -6.2375 | -48.539501 | 2025-06-08 00:24:00 | METOP-C | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b429e85a-bf2a-3a5c-9ad4-9a308727c5be | -5.6383 | -43.723202 | 2025-06-08 00:24:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c25629c-1c59-3aa7-ad54-59094904a702 | -7.0311 | -44.5746 | 2025-06-08 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3deb06f-febb-30cf-a73d-17c771d66734 | -10.7989 | -43.377102 | 2025-06-08 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d535fbac-607e-3ea9-96f1-27c1633cd64b | -8.5182 | -50.019901 | 2025-06-08 00:24:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46c38dd2-a89e-3688-86da-e845f5eb4b1c | -6.883 | -47.240101 | 2025-06-08 00:24:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bcb81ce-809b-380b-99e8-9b227586281b | -6.8732 | -47.242298 | 2025-06-08 00:24:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4fb373c0-1604-33d7-8323-6867515b9827 | -7.7335 | -44.175701 | 2025-06-08 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df469b53-3faa-3ec9-b828-10ac732d5b4c | -5.6399 | -43.730301 | 2025-06-08 00:24:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d245842-217f-33e2-b136-5e1be6d84ec0 | -4.4264 | -47.662701 | 2025-06-08 00:24:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ede6c86-9c10-31d6-88d9-5759f6d66b27 | -9.0729 | -47.150902 | 2025-06-08 00:24:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f38d31a-f773-3564-8ef1-386a6147d906 | -11.6352 | -48.4823 | 2025-06-08 00:24:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d2ea6bd-4c4c-3700-9d84-bc468e19f0f5 | -6.1952 | -43.3223 | 2025-06-08 00:24:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a13dcdb2-449c-3e4e-9a08-9494a81b082c | -5.6464 | -43.713699 | 2025-06-08 00:24:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00e3f8cd-c5cf-3fd2-80e8-a3850a3cfd58 | -12.5431 | -45.411201 | 2025-06-08 00:24:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a9cebaf-fad3-396d-9b6a-ae7eca26b45b | -5.5775 | -45.205299 | 2025-06-08 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af41ae6a-f785-37b2-b796-f25c5b1992ed | -11.1234 | -54.628101 | 2025-06-08 00:24:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f395858-5502-388c-a7e6-c509e237e37e | -8.5304 | -50.029099 | 2025-06-08 00:24:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db3d55ca-e296-3b79-b57a-918daed7a450 | -4.4842 | -43.773701 | 2025-06-08 00:24:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4bbe200-e2c0-385b-b941-94e826efd97d | -11.7973 | -48.0886 | 2025-06-08 00:24:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee986b5e-2332-3f39-80f5-edbae3b6673d | -13.5483 | -44.142799 | 2025-06-08 00:24:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f777b82-4d99-36ec-9c5b-721c9255cd2c | -12.9658 | -46.746899 | 2025-06-08 00:24:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9734e7c-996f-306b-aaa0-bc43e74e69c1 | -6.8813 | -47.232399 | 2025-06-08 00:24:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0e563ce-89ac-3fa7-9376-94f0f9bd1f94 | -9.4083 | -48.452 | 2025-06-08 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36bd1510-649e-33eb-8296-0fe4789bc525 | -12.9774 | -46.753201 | 2025-06-08 00:24:00 | METOP-C | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9cdb8dbb-92ac-3df8-9f85-a691f0c3ed7a | -7.0229 | -44.583698 | 2025-06-08 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b412d27-9aac-337b-b0a9-8d64d4a71cca | -14.8778 | -48.122398 | 2025-06-08 00:24:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4910259d-8e36-326b-a82c-71d9ed07f975 | -7.8704 | -47.891201 | 2025-06-08 00:24:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91ddedc5-b580-303e-b4f2-6050d399aab0 | -9.4063 | -48.442699 | 2025-06-08 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 002be078-e136-3729-8c92-5895fc97b663 | -7.0146 | -44.592701 | 2025-06-08 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23670105-6164-3127-9580-655c078e4f57 | -11.6373 | -48.492298 | 2025-06-08 00:24:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae447d27-3780-3a5b-bad0-d469b428db5c | -6.4959 | -47.486301 | 2025-06-08 00:24:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26bb23ed-b64e-3d52-bb50-55301f4169d8 | -12.9676 | -46.755299 | 2025-06-08 00:24:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7d4089e-9d3c-3322-8dc6-1a5fe7812c6b | -7.0213 | -44.576801 | 2025-06-08 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6107d28a-0628-3c17-9444-dc4b66fe04e0 | -7.0162 | -44.599602 | 2025-06-08 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 457d61c8-4bb5-3cc3-8f46-85d614221802 | -7.7303 | -44.1618 | 2025-06-08 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d756782-a9b8-3f19-889a-7c88da0974c0 | -10.8005 | -43.384102 | 2025-06-08 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 92cf65d0-b451-30dd-8ee9-36e6c3798441 | -7.7417 | -44.1665 | 2025-06-08 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 463fb046-9941-39a3-b898-f7911260cc44 | -5.7801 | -43.622799 | 2025-06-08 00:24:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bb80aaf-de72-389d-af0b-1305a5005ed7 | -7.7367 | -44.189499 | 2025-06-08 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27923930-cdfb-3e5f-b5dd-0d2d8e15688b | -3.7182 | -49.0816 | 2025-06-08 00:24:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b7c231-43ee-3135-a0cb-81f73150bf55 | -6.1969 | -43.329601 | 2025-06-08 00:24:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d47b4368-a0ac-3b61-87a5-96e21edb3cd0 | -11.7953 | -48.078999 | 2025-06-08 00:24:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4cddfa50-39a4-3af6-a3b9-dadcc8f127ae | -3.2543 | -47.534199 | 2025-06-08 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59ebadb8-e847-33f3-8c9c-c86de24ca224 | -6.2084 | -43.334702 | 2025-06-08 00:24:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61bc1439-7b16-3264-aa22-1517bcdb2f5c | -11.7994 | -48.098202 | 2025-06-08 00:24:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f36cb95-4edf-37a7-9dc3-4333cf88afb7 | -7.0178 | -44.606499 | 2025-06-08 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e98b4cbd-037a-332f-96ea-0af67952f285 | -9.0712 | -47.143002 | 2025-06-08 00:24:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9402fa6-b89c-303b-864d-a1f67cb4540c | -9.081 | -47.1408 | 2025-06-08 00:24:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da91bd4d-ceb1-3b28-af6d-58d87f172d7c | -11.8092 | -48.0961 | 2025-06-08 00:24:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35102b12-be81-32bf-a0d9-822edade85de | -6.4501 | -45.7318 | 2025-06-08 00:24:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb1b8f20-0be3-3ba5-83d8-285014a5829b | -5.6366 | -43.716 | 2025-06-08 00:24:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e93857f-0788-30a8-9c44-3183dbf46eed | -6.2067 | -43.3274 | 2025-06-08 00:24:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4459bc7d-80a2-3c00-98f5-4f9828a5dd18 | -7.7351 | -44.182598 | 2025-06-08 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dee17e12-074b-38e3-b09a-8fa54a96119a | -12.5447 | -45.418598 | 2025-06-08 00:24:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d5460fd-cc8a-34bd-a6ef-2074118a7de1 | -3.2559 | -47.5415 | 2025-06-08 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8840b3-ac57-39e3-be85-3867e8332ceb | -11.8071 | -48.086498 | 2025-06-08 00:24:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 516f3aaa-e737-3137-a494-2e8a4e3219db | -7.8606 | -47.893299 | 2025-06-08 00:24:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4f48eb3-fdb8-3645-8ab5-28e448896d14 | -9.4161 | -48.440601 | 2025-06-08 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8271569e-da2d-3d6a-a5f0-f6aad719857a | -4.4859 | -43.780899 | 2025-06-08 00:24:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d25ee515-cd70-3449-8d56-36a84cf928ce | -12.9694 | -46.763802 | 2025-06-08 00:24:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd7f8669-3f5a-3f1f-978d-802674c0b7e0 | -8.5822 | -48.988499 | 2025-06-08 00:24:00 | METOP-C | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8410edcb-9879-3e01-a2bf-f1f41d4b96e2 | -7.7433 | -44.173401 | 2025-06-08 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8e5a0567-4855-3e18-9df3-2d5697d0e310 | -9.4181 | -48.449902 | 2025-06-08 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 224aa9ea-3006-397d-a3ac-fd4a9562978b | -11.1137 | -54.629902 | 2025-06-08 00:24:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d206ab8-f95b-329f-8263-e1f7d13b41ce | -9.4043 | -48.433399 | 2025-06-08 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe0591e-fed0-3559-9282-61a79eaf7fef | -6.205 | -43.320099 | 2025-06-08 00:24:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c3a3bfd-2e92-3425-b851-014cdc60099a | -8.528 | -50.017899 | 2025-06-08 00:24:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f263864f-95e4-3e43-a3eb-68156b170cc5 | -8.598 | -44.167801 | 2025-06-08 00:24:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
