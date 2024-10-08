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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd4fe46d-0a9c-3384-ba40-2b740ac95fff | -17.1175 | -57.4449 | 2024-10-08 12:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| c3e60ae1-1f35-39df-8455-ea6ad4c29b53 | -17.1471 | -56.8256 | 2024-10-08 12:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 9c3876cd-2f0f-3ed5-afe6-e27acc0aa602 | -17.1178 | -57.4244 | 2024-10-08 12:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.3 |
| af721822-b6a0-3d79-88ba-5b013bbf2671 | -17.1078 | -56.8304 | 2024-10-08 12:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 8b08c1f4-1506-306a-99ca-9aabd9e0091e | -17.0989 | -57.3857 | 2024-10-08 12:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 4d6a0093-3178-312e-86ef-9980f23fdfbf | -17.1474 | -56.805 | 2024-10-08 12:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 990735dc-6dde-3a88-ac1c-855e8c9adbe1 | -17.6692 | -53.0174 | 2024-10-08 12:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 113.2 |
| c1967107-2a7d-3c4e-b744-1a1c15d629ab | -18.718 | -57.289 | 2024-10-08 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.9 |
| eaf60f6a-ebb6-375f-b2f2-3e53d8285714 | -18.5993 | -57.2629 | 2024-10-08 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 8f71064e-c898-3427-957e-9e0beb32bbb9 | -18.7183 | -57.2682 | 2024-10-08 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 8decada7-e196-30a0-b0eb-914372b292dd | -18.6192 | -57.2603 | 2024-10-08 12:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 0563be1a-4ea0-3090-adbf-75f175e5e415 | -20.3532 | -48.7955 | 2024-10-08 12:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 117.1 |
| d6cdaffc-a068-32b8-9698-51e4a9f79841 | -20.3513 | -48.8648 | 2024-10-08 12:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 8827c9b9-7bb5-3440-ab16-ae4867049296 | -21.9782 | -46.5507 | 2024-10-08 12:27:07 | GOES-16 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 144.8 |
| 4e2a73dc-3c64-3a14-abeb-3fc4d2521ebf | -10.4032 | -49.4318 | 2024-10-08 12:36:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 747eab68-8a21-3ee6-b6ea-0b254cb355dc | -11.2654 | -51.411 | 2024-10-08 12:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 22441762-04d8-3bdf-8f4c-ad1d39983633 | -12.572 | -53.0544 | 2024-10-08 12:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f613f742-e250-3480-bfd5-6656ab742ba7 | -13.2359 | -45.5783 | 2024-10-08 12:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 75b77ba0-ed3f-38b1-8748-666296aace86 | -13.2354 | -45.6014 | 2024-10-08 12:36:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7df91d27-587c-3612-bb7f-1e69134f1518 | -13.8559 | -44.5892 | 2024-10-08 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| c6347196-fbbc-378a-919a-5b8ca9e609a8 | -13.8744 | -44.6329 | 2024-10-08 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 9d32df69-262f-345e-a7b8-f2b9ed982075 | -13.8754 | -44.5858 | 2024-10-08 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 4e439156-1286-3d78-b46f-ce9a3f92479a | -13.8165 | -44.6197 | 2024-10-08 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4b2dee5b-e377-32c2-89ec-70e005781d37 | -13.8364 | -44.5927 | 2024-10-08 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 2eb0b583-9ac5-3dd8-b2b1-f93b39f89572 | -13.817 | -44.5961 | 2024-10-08 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 80ee77b7-fdef-3b9b-ae22-194dcb97e388 | -13.8359 | -44.6162 | 2024-10-08 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 5f32b156-68b5-3d4f-ac61-edd20401e549 | -14.2476 | -51.3291 | 2024-10-08 12:36:27 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ad5ec3b3-e123-3c36-9ca4-5666d6d91dd2 | -14.7186 | -45.1588 | 2024-10-08 12:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 310.3 |
| 97e16e55-a876-3dcd-b7d2-a885772c324f | -15.7068 | -59.4326 | 2024-10-08 12:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| dc38ab5e-c925-30e6-92d5-bd8cf6c596b1 | -16.4729 | -53.9147 | 2024-10-08 12:36:39 | GOES-16 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| c1f2ba01-a7de-3f15-8cde-96d5973ee1a1 | -16.4184 | -55.9455 | 2024-10-08 12:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 214.1 |
| 2a187405-8b08-312a-a34d-2b9fe4cc8647 | -16.5075 | -57.7183 | 2024-10-08 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 82fed6f3-3570-36c9-875e-0f5103279792 | -16.418 | -55.9662 | 2024-10-08 12:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 99.2 |
| 8fc09e0f-69dc-3b84-b626-704c1efaaeb1 | -16.4533 | -53.9174 | 2024-10-08 12:36:39 | GOES-16 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 7501b50c-8fc1-38d2-9eb2-5da0f5b3f599 | -16.5078 | -57.6979 | 2024-10-08 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 62848a5b-6682-34aa-b745-7390f9f590da | -16.5902 | -46.4746 | 2024-10-08 12:36:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 119.7 |
| b9c6c695-162d-3035-829f-33c12ccbf7c5 | -16.5512 | -46.4592 | 2024-10-08 12:36:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4a383412-2051-342c-a4fa-bf002835c6d7 | -16.571 | -46.4553 | 2024-10-08 12:36:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 194.5 |
| 4d316bff-6950-3706-98a8-55b93bda75d5 | -16.3956 | -57.3845 | 2024-10-08 12:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 9d5fb1be-6655-3539-b39e-1eab7be4e4b2 | -16.5752 | -55.9055 | 2024-10-08 12:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 2a4f0b77-389f-3600-a1cf-44fa1bbf487b | -16.5556 | -55.9079 | 2024-10-08 12:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 87298e8c-ae2b-3cad-912f-badc191b0d5d | -16.8706 | -47.134 | 2024-10-08 12:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 610bb85c-3afb-39c7-b42e-776bdf13796b | -16.9741 | -56.6202 | 2024-10-08 12:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 0af27231-efd8-39f4-b5f0-aaa7f329c5a2 | -16.994 | -56.5972 | 2024-10-08 12:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 736b4f94-6f48-3140-bd3b-5949b44d023e | -16.9407 | -57.4859 | 2024-10-08 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 3d982ab5-ec6d-33d7-800b-3de6f6d61073 | -16.9937 | -56.6178 | 2024-10-08 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 135cb728-3eb7-3b03-aad3-0a51eb3286da | -16.941 | -57.4654 | 2024-10-08 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| ed8511aa-36e4-3428-ab47-6f6fdfa94c1b | -17.0123 | -56.6773 | 2024-10-08 12:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| a9c9468a-c552-3416-a710-cf69ec4761b4 | -17.1175 | -57.4449 | 2024-10-08 12:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 6c2fdc8c-71a8-3ea5-bf90-303fbdf6b0a2 | -17.0982 | -57.4267 | 2024-10-08 12:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| f19a8d29-8319-3e72-8f69-99f79d86ffe2 | -17.1584 | -56.1429 | 2024-10-08 12:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 47cf904f-a3b6-340d-a813-c52dc663d19d | -17.0989 | -57.3857 | 2024-10-08 12:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.0 |
| 4505970f-1449-3d0f-88bf-8e50ff675c1c | -17.1375 | -57.4221 | 2024-10-08 12:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 580285ce-4a1a-3cc2-a05a-8f27f05ee897 | -17.1178 | -57.4244 | 2024-10-08 12:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 62c95831-103e-30a1-87a3-3241ff50d343 | -17.0992 | -57.3651 | 2024-10-08 12:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 339.6 |
| 2081d6ab-fe98-3386-aacb-1824b2d88882 | -17.6692 | -53.0174 | 2024-10-08 12:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 119.4 |
| debcd723-eba4-367f-b510-9f5bc480771f | -18.7183 | -57.2682 | 2024-10-08 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.2 |
| 49ef0650-ef26-3088-a7d1-4b5bd69d3fff | -18.6394 | -57.237 | 2024-10-08 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 42028efd-dd91-37f5-bcd2-1443ad124766 | -18.718 | -57.289 | 2024-10-08 12:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| c4a06fd3-ee66-35db-a135-38c9ce7f53a7 | -20.4258 | -47.6453 | 2024-10-08 12:36:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 143.0 |
| bba07565-cc0c-3d31-affe-292a5180014f | -20.3513 | -48.8648 | 2024-10-08 12:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 7acb9175-3678-3cde-a8a2-29c211f745b5 | -21.9782 | -46.5507 | 2024-10-08 12:37:07 | GOES-16 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 144.7 |
| c785eb05-6120-3b23-9459-372f838f87b4 | -10.4032 | -49.4318 | 2024-10-08 12:46:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 932e6ecf-4b2c-34ae-8d08-5b10f5fa4180 | -11.2278 | -51.3938 | 2024-10-08 12:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| cd4f950b-38fe-3f99-8c18-d95e78acd4ff | -12.7065 | -62.9453 | 2024-10-08 12:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| d5698a70-d5c5-3a7e-89ac-0ba71f7fd0af | -12.8242 | -62.4573 | 2024-10-08 12:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8c94013f-712e-3eee-be16-18bcee5e4e89 | -13.8559 | -44.5892 | 2024-10-08 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 628b338b-85e0-3a31-8b84-a380501afa13 | -13.8744 | -44.6329 | 2024-10-08 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 55fa3342-3999-3978-88ee-5f45d054443e | -13.9523 | -44.619 | 2024-10-08 12:46:24 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| acae9ffa-22ad-348b-a744-c4ea71a61dc4 | -13.8359 | -44.6162 | 2024-10-08 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b7fac837-55d5-30bd-894b-4f576cbcbb6d | -13.8754 | -44.5858 | 2024-10-08 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| e92a2f46-fa95-3bd5-a06a-f92728f52590 | -13.9333 | -44.5989 | 2024-10-08 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 01571df4-2864-3321-80a5-24d45e8c9080 | -13.9328 | -44.6225 | 2024-10-08 12:46:24 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 257ee2e5-2657-3e4e-b987-be951c14e14a | -13.9138 | -44.6024 | 2024-10-08 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 71d84446-1796-3995-a0c0-2c53a92a6e3b | -13.8165 | -44.6197 | 2024-10-08 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 5c29227e-9cfe-3b7d-8377-483c69a7ae59 | -13.8364 | -44.5927 | 2024-10-08 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 31dfd4ab-4b12-30e3-80ac-e850c1dc8b1b | -14.7186 | -45.1588 | 2024-10-08 12:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 3528bfe8-1c45-39a3-94a1-0dcbe0dd55d4 | -15.7068 | -59.4326 | 2024-10-08 12:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 94fe702b-3e44-3dcf-8be7-091dfcec3896 | -15.7071 | -59.4126 | 2024-10-08 12:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| bf2e5751-5e5d-3f6f-a7d1-fbcc37e22c53 | -16.5078 | -57.6979 | 2024-10-08 12:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| ce127e36-229e-3994-9aa6-0d2e3fc8c1d7 | -16.4184 | -55.9455 | 2024-10-08 12:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 405.2 |
| 397a6dfb-e521-3a43-a9ee-b0a11d9e87ca | -16.5902 | -46.4746 | 2024-10-08 12:46:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 576b7759-8b61-3d75-b325-c3f64a7f4a65 | -16.5512 | -46.4592 | 2024-10-08 12:46:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 290ae83c-d5eb-36b3-aade-fc2f4cb7a35c | -16.571 | -46.4553 | 2024-10-08 12:46:39 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 7c048eb9-7492-3beb-8c27-a235ad29f969 | -16.5075 | -57.7183 | 2024-10-08 12:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 6196e78d-5b45-3709-b283-6672c3a93eac | -16.488 | -57.7205 | 2024-10-08 12:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 7b4532f7-7bf1-3124-bc2a-6209ccf7c54f | -16.3956 | -57.3845 | 2024-10-08 12:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 585ac1fa-ffed-30af-a730-4120f95119d5 | -16.418 | -55.9662 | 2024-10-08 12:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 159.0 |
| 79822be5-e96a-3be4-bae3-f14150681eaa | -16.4533 | -53.9174 | 2024-10-08 12:46:39 | GOES-16 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ae16a34a-156c-35b8-b78d-6dd61131bd03 | -16.5752 | -55.9055 | 2024-10-08 12:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 2d9db7ad-3c93-3572-be28-5fc81f85205a | -16.8706 | -47.134 | 2024-10-08 12:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 125b20bc-48ca-3ad3-aef1-f3b9114d935c | -16.6143 | -55.9007 | 2024-10-08 12:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 8168778a-39b2-3331-bbad-91116e76c4d2 | -16.8894 | -47.1763 | 2024-10-08 12:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 97c31684-1bca-331c-b388-fc8483fba66c | -16.8899 | -47.1532 | 2024-10-08 12:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1db3d427-ad56-3086-a596-bc7fde598f94 | -16.9741 | -56.6202 | 2024-10-08 12:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| e8716ddd-cbc5-3003-8681-9c9109d947b4 | -16.994 | -56.5972 | 2024-10-08 12:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 246804eb-d7d3-340d-b3ae-255af41d707f | -16.9927 | -56.6797 | 2024-10-08 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 1cd0b9e7-399c-3187-bd77-f524d1fea3f4 | -16.9407 | -57.4859 | 2024-10-08 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 6daa4e89-d1b2-3769-9c5a-5ccb550e1044 | -16.9937 | -56.6178 | 2024-10-08 12:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| a123861a-fc37-3840-bc12-6b70a423c8aa | -16.941 | -57.4654 | 2024-10-08 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.6 |


[Clique aqui para ver as próximas entradas](README138.md)
