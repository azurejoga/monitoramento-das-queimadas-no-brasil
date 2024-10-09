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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6983e35-9b5e-330b-9663-f17466a1ce30 | -13.8764 | -44.5386 | 2024-10-09 03:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 2e0007d7-cf22-3014-aeea-bb891952c70e | -13.8769 | -44.515 | 2024-10-09 03:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| bbc70705-4a8a-35b2-90a3-8cf62567e16f | -13.8963 | -44.5116 | 2024-10-09 03:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| b0cc00f7-dc37-31f3-84e1-a4eb4b8148f0 | -13.9158 | -44.5081 | 2024-10-09 03:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 9ef0800e-7664-3a76-8cd4-8b0df4f6ac85 | -13.9163 | -44.4845 | 2024-10-09 03:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b34fe6f3-c27d-3bf8-98a4-8cbb10ae0c6e | -14.0975 | -51.0918 | 2024-10-09 03:26:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 22e14d34-2183-3635-a341-c2263abd4f02 | -14.1168 | -51.0892 | 2024-10-09 03:26:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a9dbe178-343f-35af-8c75-6482da834b57 | -15.6791 | -52.5206 | 2024-10-09 03:26:34 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6d09f81b-3a0f-3856-8bf9-118f460d7cbd | -15.6795 | -52.4993 | 2024-10-09 03:26:34 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 30fb3bea-4042-3da6-95d6-6dbbecbe61f2 | -16.4184 | -55.9455 | 2024-10-09 03:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 030eeb32-841a-3667-ab8d-24670c61250b | -16.7846 | -57.4629 | 2024-10-09 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| dba53efb-c79f-3a88-b861-0acfb3712cef | -16.8573 | -57.8218 | 2024-10-09 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| f9989fd3-d7c5-3e73-b87a-4c64a1e23750 | -16.8576 | -57.8014 | 2024-10-09 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 2f43d8ef-519a-3b9f-a350-dc6843028ef8 | -16.8898 | -55.8039 | 2024-10-09 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 145.0 |
| 9a0cebcf-43f5-39c3-b89c-66aa33b52661 | -16.8901 | -55.7831 | 2024-10-09 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 124.0 |
| 818186da-aaa9-3196-813e-e2810d0ef386 | -16.8768 | -57.8196 | 2024-10-09 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 001c5eff-efa1-38b9-bf54-30b147dd8cb5 | -16.8772 | -57.7992 | 2024-10-09 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| ab759c67-b84c-3b09-80f2-8251ac3a1c35 | -16.9091 | -55.8222 | 2024-10-09 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 743fb287-677e-3fd3-b7e2-1c469ffc6836 | -16.9094 | -55.8014 | 2024-10-09 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 294.8 |
| eabfda11-d7b2-39e7-aa53-7bceca23df59 | -16.9098 | -55.7806 | 2024-10-09 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 221.3 |
| f303545f-dfbe-33fb-9174-ef916f61d08b | -16.929 | -55.7989 | 2024-10-09 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| c0aeb565-30da-38e2-af3b-a022fbe9eecb | -17.7526 | -53.7948 | 2024-10-09 03:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 58cba423-8ffa-3a0c-9db4-75ebb341c8d1 | -17.753 | -53.7735 | 2024-10-09 03:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 666c2834-11aa-3a12-abad-5b12c50639cc | -18.1189 | -56.413 | 2024-10-09 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 92b8a8a4-529d-3faa-bd8c-6063332b7055 | -18.1193 | -56.3921 | 2024-10-09 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.5 |
| 4a01eef1-6148-31c4-98ae-cbd54beed7d1 | -18.1196 | -56.3713 | 2024-10-09 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 95fef1fc-0884-33f4-83ed-76e88a9ea8b2 | -18.1391 | -56.3895 | 2024-10-09 03:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| cf8c0049-4ba2-33b4-b037-4758eb833a47 | -18.5993 | -57.2629 | 2024-10-09 03:26:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| e84b3abd-0336-37af-a5b0-401c9f5c38f6 | -18.5996 | -57.2422 | 2024-10-09 03:26:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| ce0d466f-8302-38ea-a629-d48ca993d18b | -18.6597 | -57.2137 | 2024-10-09 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 151efcf2-a52c-3974-acf9-3e1733fbaffa | -20.3346 | -48.7307 | 2024-10-09 03:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 571a1712-62f2-3ffd-b20a-ee9dfc47adf0 | -20.3352 | -48.7076 | 2024-10-09 03:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 193bc5d4-d827-3b4e-8176-e6f2990875ae | -20.3551 | -48.7262 | 2024-10-09 03:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 9653f07e-1013-3faf-8726-95e0749fcb21 | -20.6396 | -45.9158 | 2024-10-09 03:27:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 1188611f-b5e0-364b-9a3c-1a568e2656b9 | -20.812 | -45.6315 | 2024-10-09 03:27:01 | GOES-16 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 6b42352b-8715-3765-8279-31ef856ae364 | -20.8128 | -45.6072 | 2024-10-09 03:27:01 | GOES-16 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c1f383fe-22ae-3e2c-bd30-70126291ba5d | -21.0719 | -47.2094 | 2024-10-09 03:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 5bc538f4-f173-3bef-8064-606c0b9e9e58 | -21.0926 | -47.2043 | 2024-10-09 03:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6c9d76fb-21e0-31fc-8c72-39472d3ac639 | -21.572 | -46.9898 | 2024-10-09 03:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a22a277a-4df9-3903-ae69-17c1efae3504 | -21.5727 | -46.9659 | 2024-10-09 03:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 8278fd8a-7441-3ace-aef7-ca7fd2d4478f | -21.5864 | -47.8827 | 2024-10-09 03:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 5ad30068-8067-3a61-9ea5-6e0f31dc10d7 | -22.1369 | -48.1224 | 2024-10-09 03:27:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 174b49dd-6b2c-3171-90df-43a71d0205fe | -22.1571 | -48.1409 | 2024-10-09 03:27:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 99445981-7167-3ff0-94df-eb95ad54294f | -22.1578 | -48.1172 | 2024-10-09 03:27:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c0ddc767-b299-3870-90cf-64e7de9a1875 | -22.1585 | -48.0936 | 2024-10-09 03:27:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 177.0 |
| f0686ac1-c448-30de-b7be-5f6f5fa833c7 | -22.1592 | -48.0699 | 2024-10-09 03:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 5d7ad0dc-cda1-34a2-8c9d-48ea32c10693 | -22.1794 | -48.0884 | 2024-10-09 03:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 63e7407e-76a5-3c2f-9901-8fc63f8335ab | -22.1801 | -48.0647 | 2024-10-09 03:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f65fa94c-7571-325b-b0c5-405bf6149afd | -22.1981 | -48.1541 | 2024-10-09 03:27:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e03fd48c-3f8d-3ac1-a06b-9c0524f5b7ee | -22.8139 | -54.451 | 2024-10-09 03:27:12 | GOES-16 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 137.2 |
| 8d7f8ccd-33bc-354d-bb6e-bbc00eb012c0 | -22.8348 | -54.4471 | 2024-10-09 03:27:12 | GOES-16 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 134.8 |
| 9f5c2c55-7753-3f86-aa13-83163c43c336 | -22.8353 | -54.425 | 2024-10-09 03:27:12 | GOES-16 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 101.5 |
| 00fa5ed5-41a4-3c2e-ab88-198f9a79a808 | -1.11 | -53.6173 | 2024-10-09 03:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| de03ad08-7f19-32d7-bd52-4ba6bda57846 | -3.9021 | -46.4689 | 2024-10-09 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| db8f3194-b826-3816-b212-08636e37652d | -3.9023 | -46.4467 | 2024-10-09 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 45.6 |
| cc58616f-ee67-34b5-bc7a-b5d8b2204ba3 | -3.9208 | -46.4459 | 2024-10-09 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 443b49d1-31c3-3c9b-86c8-5d4002d4d6c0 | -3.9394 | -46.445 | 2024-10-09 03:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 31c616a2-ea4b-324c-952f-0ccbfbcc1e9b | -5.5905 | -44.8687 | 2024-10-09 03:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 2ce68e0b-be49-39ba-ab6a-d4254def3b0f | -6.7614 | -60.0559 | 2024-10-09 03:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 352c16a5-29c0-3444-94d9-8b1f3bcfc670 | -6.7615 | -60.0367 | 2024-10-09 03:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| ad72640b-9a6c-3916-b46c-dc55d56e3981 | -6.7798 | -60.0552 | 2024-10-09 03:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 3dfa7db7-e25f-3d26-aa9f-1e1c1a52186b | -6.7799 | -60.036 | 2024-10-09 03:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| cc1a0fba-ea0e-304a-a975-fd3dc828569e | -8.4919 | -48.6476 | 2024-10-09 03:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 128eafe0-e674-3a14-8645-ee2e6216bc27 | -10.3655 | -64.8451 | 2024-10-09 03:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 094994b7-902e-3d82-b82e-1e1701c78523 | -10.3656 | -64.8262 | 2024-10-09 03:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 4b01343a-4cd1-3fbb-be84-110a15fe2762 | -10.3894 | -61.2502 | 2024-10-09 03:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| e4b5fac0-bf29-39a2-a888-b0d543c1043b | -10.3842 | -64.8443 | 2024-10-09 03:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 3c8c8cf8-9118-39a2-afba-163daa467178 | -10.3843 | -64.8255 | 2024-10-09 03:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 35.5 |
| a23f771e-1daa-36f7-86f7-4b013062e682 | -10.4287 | -60.9979 | 2024-10-09 03:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 3692dbb7-d898-31ee-a892-cbd9c0e0feaf | -10.6253 | -55.9355 | 2024-10-09 03:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 5e61ec57-9755-3b75-a8e4-d7ae8d888be5 | -10.6256 | -55.9154 | 2024-10-09 03:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 9db41c4a-f3ae-3990-8964-9a35fee6a11a | -10.6258 | -55.8953 | 2024-10-09 03:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1e91356b-cf64-3942-bc53-9910c820d79a | -10.8754 | -63.9169 | 2024-10-09 03:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 1e2fa8b1-2840-35ba-b73c-d57b4fa62985 | -10.8755 | -63.8979 | 2024-10-09 03:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 2bd4bc66-b1ef-3aa9-b2c5-8d878c911ba8 | -11.2582 | -60.4079 | 2024-10-09 03:36:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 32dbd551-7dfd-384d-a14a-91dafe251965 | -11.2583 | -60.3885 | 2024-10-09 03:36:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| c86f1802-9eaa-3e2d-a636-5df305e347c4 | -11.277 | -60.4067 | 2024-10-09 03:36:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 27772ae7-2eae-3218-8eac-90894c017a42 | -11.2771 | -60.3873 | 2024-10-09 03:36:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 37b42e31-a6b0-318e-88b5-51daccda0f1a | -11.5232 | -65.1559 | 2024-10-09 03:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| a89f6f97-7809-3564-8743-5cea40eeee10 | -11.5233 | -65.137 | 2024-10-09 03:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0eec82ec-edd0-3eb7-9b8d-3263d6b6096c | -11.6928 | -65.0353 | 2024-10-09 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 92ebc09c-7061-306f-b80c-5a0ef784276f | -11.693 | -65.0163 | 2024-10-09 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 143.1 |
| bed67b57-8acf-314f-85ff-17088cc50362 | -11.6931 | -64.9974 | 2024-10-09 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 663768c7-19e5-3dbf-9a24-772731376ea9 | -11.7117 | -65.0155 | 2024-10-09 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 159.9 |
| dc38b2b4-477b-3c28-bbdf-1e6f34060fd5 | -11.7119 | -64.9966 | 2024-10-09 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 21512f18-c4fe-3015-beb2-81204a1e423e | -12.878 | -62.8007 | 2024-10-09 03:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 1b987991-40f1-36fe-af64-810309dca13b | -13.2877 | -53.704 | 2024-10-09 03:36:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 8102c987-8923-3e96-839c-4c15d09e487e | -13.3788 | -61.9388 | 2024-10-09 03:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 1f850da0-a618-36dc-a26e-579858120fa3 | -13.379 | -61.9194 | 2024-10-09 03:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 76cf0b27-8868-3148-ba79-b38c5b691bd1 | -13.8369 | -44.5691 | 2024-10-09 03:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5d21a47e-43d9-3865-92cd-912e880a8455 | -13.3978 | -61.9376 | 2024-10-09 03:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 85fe62ed-29e0-3edd-a9c5-06bdc472bcaa | -13.398 | -61.9182 | 2024-10-09 03:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 71622247-1554-3206-8cc7-8d79f00e06cd | -13.417 | -61.9169 | 2024-10-09 03:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 9fa5d853-8867-3caf-957e-a2c0cff6133f | -13.9158 | -44.5081 | 2024-10-09 03:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 00c71c55-da31-3b7d-918d-a951e4a850b7 | -13.9348 | -44.5282 | 2024-10-09 03:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| ed2b69dc-9e66-33f6-bad3-e178a922e182 | -14.0975 | -51.0918 | 2024-10-09 03:36:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 402447d4-dd38-358b-ac00-282b5438b80f | -16.4184 | -55.9455 | 2024-10-09 03:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 4091d986-b4a9-3ecd-be87-5be32405503f | -16.8241 | -57.438 | 2024-10-09 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.3 |
| 5134ab19-0702-30c3-b186-884f528e6e90 | -16.8573 | -57.8218 | 2024-10-09 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| f367b5b6-493f-31c2-84cd-05dd6d108397 | -16.8576 | -57.8014 | 2024-10-09 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |


[Clique aqui para ver as próximas entradas](README67.md)
