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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38d3f220-c856-3dbc-bdc4-2c543d4e0ef4 | -16.7644 | -57.5061 | 2024-10-05 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 0d0adda1-fb14-364b-a6a3-5e0c38f568b0 | -16.6598 | -55.5219 | 2024-10-05 02:46:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| 4a8a7886-2674-3033-b240-ad6e14dcb502 | -16.6594 | -55.5427 | 2024-10-05 02:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.6 |
| 69c039a0-6939-31fb-81d4-418d62d0fa99 | -16.765 | -57.4652 | 2024-10-05 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| b0163081-dc64-35c1-b873-bb828712bdf6 | -16.7647 | -57.4856 | 2024-10-05 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.5 |
| d917de16-7751-37ac-b0eb-be654a44c746 | -16.6871 | -57.4536 | 2024-10-05 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 44fc204b-56da-32ab-9546-be751cf89316 | -16.7843 | -57.4834 | 2024-10-05 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| cc454165-875c-3b56-8426-ca849725292b | -17.1381 | -57.381 | 2024-10-05 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 882ab67d-7c1d-3182-aeff-be94e5a3cf9a | -17.1378 | -57.4016 | 2024-10-05 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 189.2 |
| 42b590d1-c980-3c30-ab75-a4d072a8d145 | -17.1375 | -57.4221 | 2024-10-05 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.9 |
| 74f7e485-3c1b-3292-9879-eb44c6cf2c8d | -17.1182 | -57.4039 | 2024-10-05 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 139.9 |
| ad70b5ce-97e8-3486-81f0-18e0358e2fd7 | -17.1178 | -57.4244 | 2024-10-05 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.3 |
| 8e20250c-6efb-3a03-a4a4-6fc1b5dc4541 | -17.1085 | -56.7892 | 2024-10-05 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| b8b40421-074e-37e6-ac08-7b8e49eadf86 | -17.0892 | -56.7709 | 2024-10-05 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 01913879-4f61-3c55-9ad4-420d5d4f811c | -17.1574 | -57.3993 | 2024-10-05 02:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 24682de5-07b6-3a45-85d3-d174755d3cc1 | -18.6525 | -43.1453 | 2024-10-05 02:46:49 | GOES-16 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 956c3531-78df-3a71-8ff4-ddf90d686162 | -18.4858 | -52.8442 | 2024-10-05 02:46:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 276.6 |
| 6ab794f2-b843-3460-ba47-f2f2f2452125 | -18.4862 | -52.8226 | 2024-10-05 02:46:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 71cbe941-87a9-30e2-8477-89473a6c3b74 | -18.5053 | -52.8626 | 2024-10-05 02:46:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 88da1abf-bd23-3ef7-905e-1a9beca3ef83 | -18.5058 | -52.841 | 2024-10-05 02:46:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 860.4 |
| 2aba58b8-2e52-39b9-bd14-695264391cb1 | -18.5062 | -52.8193 | 2024-10-05 02:46:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 448.4 |
| ed2ee3a1-50a5-3aac-8594-901e15a037c5 | -18.5257 | -52.8377 | 2024-10-05 02:46:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 21f4e97a-3770-39eb-bc62-56e04af31242 | -18.6582 | -57.2967 | 2024-10-05 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.6 |
| cf4eb274-f63c-3eda-a534-8fbadc265902 | -18.6586 | -57.2759 | 2024-10-05 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| eb30c8ae-f40a-3b77-a934-8b5e93b2ab8d | -18.6782 | -57.2941 | 2024-10-05 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 8c9fcfd8-db29-397b-8ac1-f2bfd1158da6 | -18.6785 | -57.2734 | 2024-10-05 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.5 |
| 19001d1b-54f7-37e7-a00c-1e9804708857 | -18.6981 | -57.2915 | 2024-10-05 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.1 |
| f48ff0b9-a950-30fd-856d-a8d1737480a6 | -2.9014 | -50.7142 | 2024-10-05 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b44ba168-f66d-397c-9ab2-1c554a7dde26 | -3.3083 | -50.4719 | 2024-10-05 02:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 932fef41-2c50-3718-af48-22d1dd9e1881 | -3.3084 | -50.451 | 2024-10-05 02:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 3918a219-3dbb-3618-9ae2-c221ef338436 | -3.618 | -47.5352 | 2024-10-05 02:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| d9c764d1-c6a5-3ea6-a9a3-2aee7117e4c2 | -4.0794 | -47.9502 | 2024-10-05 02:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6520e12e-dc6f-3a8b-aaec-15f934a797f2 | -5.8214 | -44.1426 | 2024-10-05 02:55:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 08baffab-c2a8-3cdd-a926-8937f1e14fa5 | -5.8216 | -44.1196 | 2024-10-05 02:55:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1b4fe426-85fd-3a9e-9e03-063853500304 | -6.9514 | -59.0666 | 2024-10-05 02:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6a2155d0-d693-35d0-ac1b-480287bb626a | -7.5193 | -63.2558 | 2024-10-05 02:55:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d6712e17-2471-3c81-b8d9-b585c03e06b6 | -8.7652 | -44.8335 | 2024-10-05 02:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 40e40398-2c52-37c8-a40f-36f0549830d8 | -8.7655 | -44.8106 | 2024-10-05 02:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 871310c6-d654-32ab-bf33-48add47f0ff4 | -8.7841 | -44.8315 | 2024-10-05 02:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7206b82c-01b8-38e3-b995-b60a332cc593 | -8.7844 | -44.8085 | 2024-10-05 02:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| ec41c689-b457-34a3-a2f0-4dd010c67b33 | -8.7772 | -49.955 | 2024-10-05 02:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e52d9e5f-a472-33fd-b2b5-c1cfb3b95220 | -8.7957 | -49.9747 | 2024-10-05 02:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 532464ae-18b3-3318-8a27-56ba8daeaecf | -8.7959 | -49.9533 | 2024-10-05 02:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f8e1f3c8-aeab-3ec5-bca0-d8f9ddc9ee51 | -8.9853 | -49.8083 | 2024-10-05 02:55:57 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 49dbea7e-ac77-3f97-a878-8e868a20fc03 | -9.4574 | -40.3641 | 2024-10-05 02:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.6 |
| c4de3a87-537d-3099-8971-1bf5a2023f9f | -9.2839 | -65.4283 | 2024-10-05 02:55:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| fc6a5ec4-7835-32e3-933e-548c936206da | -9.284 | -65.4096 | 2024-10-05 02:55:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2042c201-3a35-3621-a61f-e24bcbfcb66a | -5.11731 | -37.57108 | 2024-10-05 02:56:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 17633955-3c82-32ed-b5cf-6c010c75860e | -9.9505 | -44.0908 | 2024-10-05 02:56:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| b832fdf0-6c70-3776-8318-070f54262853 | -11.0966 | -54.2336 | 2024-10-05 02:56:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 80ee489b-b338-3d03-adaf-b1f4581bc5a4 | -11.1155 | -54.2319 | 2024-10-05 02:56:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4970da0c-35b8-3216-86e9-fc14ddf0c628 | -11.6995 | -47.8131 | 2024-10-05 02:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 943c73e7-f9aa-3af5-b6f9-3130fc8d55ba | -11.7187 | -47.8107 | 2024-10-05 02:56:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| a3c7d7ee-27a3-3b9f-b82c-6b94125152b4 | -11.896 | -56.9354 | 2024-10-05 02:56:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ef668cf1-8ed1-34ed-8162-4b6c85aa0e58 | -12.7627 | -50.5567 | 2024-10-05 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 24854438-5d71-3f51-954a-22878547f913 | -12.7815 | -50.5758 | 2024-10-05 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 25d81884-3cae-33e6-b9c7-7e01be9c6674 | -12.7819 | -50.5543 | 2024-10-05 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 545.6 |
| 6e2c475d-b7ff-3af9-b897-1942b30a350b | -12.7822 | -50.5328 | 2024-10-05 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| b648606a-04e3-326f-af1e-8aaf8a85624d | -12.801 | -50.5519 | 2024-10-05 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 34371556-799e-3c9c-a838-e25d7756886c | -12.8202 | -50.5495 | 2024-10-05 02:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 8832e0ed-805e-3ce4-bd6d-3056032c907b | -13.1358 | -51.1527 | 2024-10-05 02:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 005ec6c3-6f24-3e3b-a698-0ee7b4b0fe6f | -13.1362 | -51.1313 | 2024-10-05 02:56:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| a65026cc-64e2-3515-ad6b-8cef1bb0bc5b | -15.5597 | -57.4553 | 2024-10-05 02:56:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4e74def8-07e2-307e-913a-8601e9267822 | -15.5791 | -57.4532 | 2024-10-05 02:56:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 0e24c8fe-3c00-3bf1-bd7e-ab4eb01bc278 | -16.4155 | -57.3619 | 2024-10-05 02:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| c1932d68-7df9-3969-b103-ca60e425632b | -16.6402 | -55.5243 | 2024-10-05 02:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| f8fdbea1-e1ed-337d-ad99-8618f713d7ee | -16.6405 | -55.5035 | 2024-10-05 02:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| d3a19508-db2b-3ed0-9738-f2623b757843 | -16.6594 | -55.5427 | 2024-10-05 02:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 4f268320-4aec-35b3-a5e4-9d59e916ce92 | -16.6598 | -55.5219 | 2024-10-05 02:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 113.8 |
| 39764e31-7e1f-3ca4-8a50-9a0bd33230f6 | -16.6601 | -55.501 | 2024-10-05 02:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| bebbc1b6-9bc7-3604-b62d-6601d186f181 | -16.6871 | -57.4536 | 2024-10-05 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 1ecd3a09-89a2-3954-b0c1-e9eaf44ff94f | -16.7647 | -57.4856 | 2024-10-05 02:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 56bedf1f-4ea1-3c0b-be6b-b45a2af62f4a | -17.0888 | -56.7915 | 2024-10-05 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| a6614e9a-64b5-32af-89f0-fe510b3ca146 | -17.0892 | -56.7709 | 2024-10-05 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| a50a8503-2ac2-3fb1-99cb-ca417a4992a6 | -17.1178 | -57.4244 | 2024-10-05 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 2d5a2f9c-f7a8-3919-8720-0ed4c1729984 | -17.1182 | -57.4039 | 2024-10-05 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.0 |
| cc079cb6-26a7-32cc-aff2-2ecaad40bae1 | -17.1375 | -57.4221 | 2024-10-05 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 142.8 |
| 59f901ce-4057-3100-afbd-d34321bd49f0 | -17.1378 | -57.4016 | 2024-10-05 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 185.9 |
| aef89845-afa1-3282-ba31-8c6d8c9aee8e | -17.1381 | -57.381 | 2024-10-05 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 91ce5a9e-1c98-39fc-bef8-9cd15dcbc86b | -17.1574 | -57.3993 | 2024-10-05 02:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 72a078a4-af33-38fb-b6fc-33482558f992 | -18.4858 | -52.8442 | 2024-10-05 02:56:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 617d62ab-80e7-3b44-be4d-11db06bef1f4 | -18.4862 | -52.8226 | 2024-10-05 02:56:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| e96aa3f4-6ead-3fa3-b04d-9dbb17f57beb | -18.5053 | -52.8626 | 2024-10-05 02:56:49 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 9f583070-f289-320f-8d1e-4a481d44520a | -18.5058 | -52.841 | 2024-10-05 02:56:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 934.0 |
| 1ecf3d43-5aef-3323-aa93-373dd180d4a4 | -18.5062 | -52.8193 | 2024-10-05 02:56:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 368.8 |
| 46bf7f66-f7a4-3fc0-b815-76ac5aabc5a2 | -18.5257 | -52.8377 | 2024-10-05 02:56:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 654c33be-68a5-3992-9fdc-f99ca7fa04ac | -18.6586 | -57.2759 | 2024-10-05 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| aad75042-c329-36a7-ab63-0ecec7ebb719 | -18.6782 | -57.2941 | 2024-10-05 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 999346e9-4954-37b9-8dcc-c8b93f8a6ea5 | -18.6785 | -57.2734 | 2024-10-05 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.6 |
| 9d4359e0-7306-38cd-8d32-a82f97ef50d5 | -18.6981 | -57.2915 | 2024-10-05 02:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 39efebbd-f44a-3714-90cc-c73f509f87ea | -19.0944 | -48.2415 | 2024-10-05 02:56:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c0c2e248-4d2f-35a8-b534-b8f7c55c18d9 | -19.095 | -48.2184 | 2024-10-05 02:56:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5abb0b03-3075-37eb-8939-150b897f998d | -15.26998 | -40.33166 | 2024-10-05 02:58:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3b9ea06c-62fb-3d10-9f47-ce61dc9387a6 | -15.26837 | -40.32587 | 2024-10-05 02:58:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ad2183a3-0644-3f3b-8aa7-a65e1bb154af | -15.26682 | -40.33257 | 2024-10-05 02:58:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2b0a71aa-c589-333d-b55b-78065b479e48 | -17.93253 | -40.54784 | 2024-10-05 03:00:00 | NOAA-20 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 440bc525-8c74-3fca-9a56-a31218712a14 | -17.93171 | -40.54781 | 2024-10-05 03:00:00 | NOAA-20 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 1410020b-7d54-39fb-9b88-c4d103ff2704 | -18.48 | -52.84 | 2024-10-05 03:03:38 | MSG-03 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 61a61630-4579-368c-b534-1f144a47b7ce | -17.03 | -56.71 | 2024-10-05 03:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b4f038fe-be48-3d98-a6d8-b9325ebad637 | -12.62 | -53.12 | 2024-10-05 03:04:13 | MSG-03 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README36.md)
