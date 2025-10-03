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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d9a0635-479f-3bfa-b330-253bfeaa140a | -12.7435 | -50.5591 | 2025-10-03 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 3a53db86-5ed1-3fc6-a4e6-a89dc802371b | -13.7666 | -48.0777 | 2025-10-03 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 55ae55b8-2666-3d26-b68e-b2dd817a1e63 | -14.6497 | -44.7499 | 2025-10-03 12:40:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 02b80667-1875-3193-b771-9b3fdcc2707d | -11.8818 | -44.9815 | 2025-10-03 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6bcfa165-5c30-31ba-8046-6f347a62764b | -13.7472 | -48.0806 | 2025-10-03 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 135.3 |
| dbaa9ed6-3032-352a-937c-54fb5b1cf1c9 | -14.0037 | -44.9376 | 2025-10-03 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 214.7 |
| f4c91c52-0052-3c17-a6c1-43b7a18d25d6 | -12.6131 | -46.9725 | 2025-10-03 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 2a42567b-7db2-37b4-bd02-d41e6dd3a9e2 | -11.1271 | -47.8856 | 2025-10-03 12:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 841c6c97-85cb-3ac8-bf37-c0ce35fdb68c | -7.7496 | -46.2496 | 2025-10-03 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c2cd2ed2-1b41-3538-ab71-a373d9c64b2a | -9.8991 | -43.7237 | 2025-10-03 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 74b81205-98e3-3a3d-8ff5-6b02564175fd | -9.3389 | -45.7266 | 2025-10-03 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| e220a32f-e3ea-3e89-8fa7-00ae02446474 | -10.9483 | -51.0634 | 2025-10-03 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 6294ae24-8304-3c3b-99e4-acf7d8e83cb4 | -14.0032 | -44.961 | 2025-10-03 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 9433d402-35dd-3654-b813-1f73ca6bf9ab | -10.955 | -46.7269 | 2025-10-03 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 2f75216c-df5b-375f-85eb-2109d00e49c7 | -13.3422 | -48.0965 | 2025-10-03 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 0266de75-ec2c-3876-bdf9-41a92d401cfb | -9.3386 | -45.7493 | 2025-10-03 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 04d53640-a2ab-3f70-ae64-07216f78489f | -9.3547 | -45.951 | 2025-10-03 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3504cdd4-db20-3ab4-8361-5fd4b2d4efcd | -12.6323 | -46.9697 | 2025-10-03 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d716caef-17c9-3840-a71d-a49410c46086 | -13.7669 | -51.2858 | 2025-10-03 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| fa656ac3-b8b5-336d-95b2-b9abf0343a88 | -17.6338 | -44.4385 | 2025-10-03 12:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 19b2816c-67d9-3424-90d4-4af1d6b0e40f | -10.948 | -51.0846 | 2025-10-03 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b020c2bd-988b-3918-9955-2600ccf585ba | -12.7627 | -50.5567 | 2025-10-03 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 862c4f41-3967-31a5-bd7b-cb5ac932db10 | -9.9182 | -43.7212 | 2025-10-03 12:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 175.7 |
| 9783d211-ce1e-39a1-8ead-e6ca200c42c3 | -13.3414 | -48.1411 | 2025-10-03 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 460def89-e1e3-36ba-8309-2ea14ab8ad4c | -14.2316 | -46.1024 | 2025-10-03 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3656ae07-7c15-38d0-9017-70761a697d8c | -12.5305 | -47.2988 | 2025-10-03 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 77221e93-c557-31e1-b341-29dee0a1f5cb | -17.6338 | -44.4385 | 2025-10-03 12:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f30f118c-b87a-36f1-a4bc-4a2bc81c4cb3 | -10.0278 | -44.0108 | 2025-10-03 12:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| fa38aa99-1dfc-34ae-aa24-76ab5d4b3bd3 | -10.9554 | -46.7044 | 2025-10-03 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| c11ff787-9062-3123-8ee4-715d2eef8198 | -7.7496 | -46.2496 | 2025-10-03 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 52898940-ef7e-326b-8208-00c3030bdd38 | -12.7627 | -50.5567 | 2025-10-03 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| ee88a252-1cc2-3d60-be63-f8f18c398ea0 | -11.9151 | -46.3499 | 2025-10-03 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f41525af-f9d2-30be-8777-e677fe4fdedd | -14.2172 | -44.9463 | 2025-10-03 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| f3995f5f-5e76-3c34-8882-567600a148f7 | -9.9182 | -43.7212 | 2025-10-03 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 205.8 |
| a6d68474-a971-359e-8fcf-3c9734179392 | -12.6131 | -46.9725 | 2025-10-03 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 18448f47-cc15-3b21-8f8c-cef79bef3181 | -8.1888 | -44.1588 | 2025-10-03 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d0e8b6ab-348b-3108-8ae9-23c95e474a13 | -13.9843 | -44.941 | 2025-10-03 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 306.2 |
| 9093bbd9-3491-3607-bd0f-92d63c5a21ed | -13.7472 | -48.0806 | 2025-10-03 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 4b03b7d1-6992-3650-a658-f96e17f9fc6e | -8.5389 | -47.8368 | 2025-10-03 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 8c18f889-afa9-3630-9510-b70c0808af21 | -13.3418 | -48.1188 | 2025-10-03 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 167.9 |
| a0c33498-83da-3687-87ea-6ed09364a1ae | -14.607 | -46.7249 | 2025-10-03 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 8837d580-077a-30f4-9e3b-719f4dca7187 | -13.1156 | -47.8625 | 2025-10-03 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 2a2cc8ff-fde2-3721-9209-b70b3293d456 | -9.062 | -46.6565 | 2025-10-03 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 44006513-4c31-3c7e-8d8e-b64adcd1b939 | -9.8772 | -47.8103 | 2025-10-03 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 84ad9f8a-21fd-3f83-8958-3441cf0d69fb | -8.8343 | -46.7694 | 2025-10-03 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f3dbf4c1-340f-3656-b39c-e9751c2297b4 | -8.8222 | -44.8043 | 2025-10-03 12:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 9da5be27-4481-3e07-a6fd-2b4ce88dad04 | -12.6127 | -46.9951 | 2025-10-03 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 65edea66-ebe1-3059-a0b0-12c410f17559 | -11.1172 | -49.8276 | 2025-10-03 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| db0b311b-92a1-398b-b738-370b04ffcc8b | -11.5462 | -46.6943 | 2025-10-03 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d0df929b-0f9f-32b8-8002-cc1d1b6fad69 | -13.3414 | -48.1411 | 2025-10-03 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 199604cb-762a-3fc7-932c-d173a6aaf3c2 | -14.6497 | -44.7499 | 2025-10-03 12:50:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 59935e80-b4d3-3ffb-b9a5-a224a8163b9d | -13.7858 | -51.3047 | 2025-10-03 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 5bf88a59-ea09-375d-a495-1d2fec5f5ae5 | -14.2367 | -44.9428 | 2025-10-03 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 667d25d1-68ef-357e-8b69-2139b96d41af | -11.8818 | -44.9815 | 2025-10-03 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| fbc6e880-092a-30ca-b278-431f849964c2 | -12.5301 | -47.3213 | 2025-10-03 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ec2a2bb9-7e72-3b7a-a09d-7fe2c6b9f3dd | -7.2913 | -45.2548 | 2025-10-03 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 051d6eca-7a53-31ac-ae1b-c413c16379de | -11.9155 | -46.3272 | 2025-10-03 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 282.5 |
| 6f68314e-3236-3b61-a884-0b341632d077 | -14.8063 | -51.424 | 2025-10-03 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e0cd0c5f-b238-3ce1-a1ea-61642856d4c0 | -17.6331 | -44.4626 | 2025-10-03 12:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 193.3 |
| a8ce29a0-ce7c-35bf-a060-0a3735a7305a | -10.9483 | -51.0634 | 2025-10-03 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 5f47b957-ba99-35fe-a76a-6d80ee139375 | -7.3101 | -45.2531 | 2025-10-03 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| edb2970d-99c3-33be-b7a3-d2e06a690430 | -13.7673 | -51.2643 | 2025-10-03 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 9e799d66-7095-3d48-9b11-b96f53b7bb43 | -9.8769 | -47.8324 | 2025-10-03 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 39a3249f-18af-3159-a832-f04b5995e3ca | -14.0032 | -44.961 | 2025-10-03 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 411.3 |
| 25aec2b6-bd35-34dc-91c5-8cbdad9a624d | -9.9186 | -43.6978 | 2025-10-03 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 1cd211b4-036c-3e7f-bab4-65051b613c5a | -7.2845 | -44.18 | 2025-10-03 12:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 114c5ea4-ef12-3983-8d19-87ed1c0d6291 | -8.5959 | -44.7833 | 2025-10-03 12:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ac653fd1-3f43-3578-96ff-22cefab001ee | -7.2911 | -45.2775 | 2025-10-03 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 250.0 |
| 92de5eec-e1d6-3a99-991a-703966a26d7f | -14.0042 | -44.9142 | 2025-10-03 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 07d9a673-f5c4-3d00-9805-e115bbacee40 | -13.7669 | -51.2858 | 2025-10-03 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 505e3b01-338d-3d93-b709-b2b9051e19f6 | -12.7435 | -50.5591 | 2025-10-03 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f28fa5cc-26dc-353a-9804-075bbf3d3a78 | -13.3422 | -48.0965 | 2025-10-03 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 100.2 |
| b4be73eb-67cb-3bb2-8f50-f3ef1b0b86d5 | -11.1278 | -47.8413 | 2025-10-03 12:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| d5303490-f126-39c7-9ea1-f538d8750f3d | -14.0037 | -44.9376 | 2025-10-03 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 490.9 |
| 66d90314-f896-3b3a-a04c-d88e0fccdbf5 | -8.1699 | -44.1608 | 2025-10-03 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 194.3 |
| d2ebf949-366a-3bdb-8065-c804aa6ea529 | -11.1271 | -47.8856 | 2025-10-03 12:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7aa048f9-7325-3ef6-8fe3-4c8a3a298b19 | -11.1275 | -47.8634 | 2025-10-03 12:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 05ae6aef-dc3b-3e6d-be96-e44a6ebecac0 | -11.9159 | -46.3044 | 2025-10-03 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 2bc29dfe-a15b-3ae2-a418-328f91046fd5 | -10.9939 | -46.677 | 2025-10-03 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 939f68f1-1ded-3365-9320-24274b3af0a1 | -7.7494 | -46.272 | 2025-10-03 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| d2bc18af-a069-3675-ac93-3e9d67b241b8 | -9.8991 | -43.7237 | 2025-10-03 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 0edb669e-37b4-36a2-977a-17a818aa9951 | -7.7682 | -46.2703 | 2025-10-03 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d6ae2b31-98e4-365c-aa4b-2573ded63540 | -14.607 | -46.7249 | 2025-10-03 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 735084df-5a12-366e-b10e-24af26dee854 | -13.9843 | -44.941 | 2025-10-03 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 1fa872d7-223c-3a0c-9f1f-1db8d988fbfa | -16.0583 | -51.0454 | 2025-10-03 13:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 4ca34bdf-fab7-3f3f-b739-84ac91c04e98 | -14.0037 | -44.9376 | 2025-10-03 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 3b6d8b81-1fb4-3b79-a39e-f3cb838ad7a7 | -17.6338 | -44.4385 | 2025-10-03 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 146.1 |
| b2046ec8-587c-324c-8456-3c48b3924209 | -7.7496 | -46.2496 | 2025-10-03 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c0f93396-38d7-3b6b-888d-be61fc66df51 | -9.3357 | -45.9532 | 2025-10-03 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 62e19988-938c-351e-9849-71bb6f23e096 | -9.9959 | -50.2462 | 2025-10-03 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e78a514f-6461-33a7-b4eb-3c5511f9b158 | -8.1917 | -47.0101 | 2025-10-03 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 25c28b8a-6c85-319c-b4ed-3e00cacf7392 | -13.1919 | -47.8959 | 2025-10-03 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| de0e5992-1571-33b6-8cbe-d1cecb3692a5 | -13.1156 | -47.8625 | 2025-10-03 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| c56c3bfa-6ad1-3505-bfa8-b1abd90eb08e | -10.0906 | -50.2154 | 2025-10-03 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| a217eeb4-9a84-3deb-a34a-0ab6308e34bb | -10.1092 | -50.2349 | 2025-10-03 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 65ea81b5-d8ae-3155-9955-0c6192541bc1 | -13.1727 | -47.8987 | 2025-10-03 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 86add347-2431-3381-b657-2aca25226450 | -18.9673 | -48.4968 | 2025-10-03 13:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 8ca04d2b-8696-35e0-aed7-b5a827346cf1 | -10.9363 | -46.7068 | 2025-10-03 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 974d3a9c-64c7-3fb5-b324-9b239325fd4f | -12.7627 | -50.5567 | 2025-10-03 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 3f9a1f5f-066e-3d1b-bf4e-f6575499179c | -8.1728 | -47.0119 | 2025-10-03 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |


[Clique aqui para ver as próximas entradas](README146.md)
