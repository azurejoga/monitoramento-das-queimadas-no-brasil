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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 371cf29c-6d79-3a4a-9e48-669a02d9e5cb | -18.08397 | -54.27985 | 2025-07-05 04:21:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce734ba8-d6e7-3df6-a82e-f38beb19d763 | -15.37471 | -44.27824 | 2025-07-05 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c063c350-b048-33d5-b3cf-a3d50a616a7c | -15.07841 | -48.9437 | 2025-07-05 04:21:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 688bd0ea-6379-3cc6-a37e-b27f9e243b6a | -14.67822 | -45.37469 | 2025-07-05 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3376d637-6fae-36d4-b9b5-3f2dc669ddf5 | -18.3319 | -52.04894 | 2025-07-05 04:21:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7ce8580-44c8-3a35-9599-b9c3b0eedc36 | -15.75492 | -43.3773 | 2025-07-05 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15dfb4e7-8195-34db-8dd9-cce699b844e5 | -12.58051 | -56.97274 | 2025-07-05 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b2ac1cd-9582-33a9-90bc-54621c123296 | -18.84856 | -47.48808 | 2025-07-05 04:21:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 150f6cc9-ed8f-3801-9607-803cc736962b | -15.92544 | -43.51891 | 2025-07-05 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bc12c9e-340f-3dc4-a29b-7bc0d7153c7b | -14.74495 | -48.24063 | 2025-07-05 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c9eff45-fb87-3c25-9736-917063427f7b | -18.88263 | -49.01539 | 2025-07-05 04:21:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64f6c498-1902-314d-9e71-3f9444a80307 | -21.19523 | -44.93567 | 2025-07-05 04:21:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f512913-ae14-3557-b9c4-f236ebf1ea6d | -13.2355 | -48.02842 | 2025-07-05 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e5647ef-d50b-35be-a78c-30c4d720ab01 | -19.74975 | -53.99881 | 2025-07-05 04:21:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84602e17-a84e-3ca6-bfda-bcbb09f901b1 | -20.41779 | -43.55145 | 2025-07-05 04:21:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 631b72d4-598b-3bda-ad71-910e9718eca8 | -16.3633 | -46.87864 | 2025-07-05 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8475fd0-2417-33e7-be93-5fa34a603e54 | -14.92229 | -46.90669 | 2025-07-05 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2a05ac3-fb8e-3152-b997-10b87a170723 | -19.45567 | -45.30716 | 2025-07-05 04:21:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e1b8fcd5-08d2-3a87-a4aa-4274a072b3f6 | -16.07434 | -51.5667 | 2025-07-05 04:21:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80541fcc-9fe7-39ed-8d6b-b15ee66ea2cf | -15.75555 | -43.37281 | 2025-07-05 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4629b05-7ff1-3d24-9fcf-1cbd9c0980b5 | -15.92607 | -43.51451 | 2025-07-05 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4b27cea-bb28-3e73-9345-c62f55724378 | -14.60496 | -48.23982 | 2025-07-05 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a1fdc74-8884-303f-a2d7-d939b010151f | -20.28719 | -49.69694 | 2025-07-05 04:21:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72bd41e1-e38e-3d32-b0ae-90bd990a82c6 | -14.47888 | -46.35632 | 2025-07-05 04:21:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31449ff7-735d-3c9a-a24b-505d5ef93d86 | -14.66814 | -45.37308 | 2025-07-05 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bda3d4ea-9133-3f6c-a985-35eb0b5118d9 | -15.60418 | -46.49984 | 2025-07-05 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 689dae70-63e9-32b5-a0d6-b4891b5ba1a3 | -13.7013 | -47.73603 | 2025-07-05 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b41bf442-321a-3cad-b411-a087224feff4 | -14.67094 | -45.37728 | 2025-07-05 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 64438465-74b5-3fde-86e6-7cebe54f25fb | -19.57292 | -54.45504 | 2025-07-05 04:21:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8890f074-1ce4-3350-a1a6-80931903f5e2 | -19.7448 | -54.00191 | 2025-07-05 04:21:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10c577f5-814b-3e34-83f5-e377477d4c3b | -18.65375 | -55.74406 | 2025-07-05 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a6f54699-46d9-3f1d-92ef-7f591c4a2bc7 | -17.91188 | -45.53738 | 2025-07-05 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fd35421-b3f1-301c-af02-51bf11c20ddd | -18.0831 | -54.28429 | 2025-07-05 04:21:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfb7d9fe-de04-3bd5-9d9c-6bbff65ebfde | -18.8513 | -47.49227 | 2025-07-05 04:21:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df208191-2c58-3fd9-a998-81cbb5be17f7 | -14.74434 | -48.24431 | 2025-07-05 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e5d002c-eb78-39db-900a-17b631416162 | -20.08911 | -44.28232 | 2025-07-05 04:21:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 93660438-a824-37a7-bb03-fef2e043e19b | -19.26048 | -44.42879 | 2025-07-05 04:21:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b7d1e5a-4e4f-318d-b2ce-aede7b6ad152 | -18.85187 | -47.48864 | 2025-07-05 04:21:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbf51a22-a908-31c3-9686-0fd8da616610 | -19.25986 | -44.43319 | 2025-07-05 04:21:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f35a370e-23eb-339d-90b1-76ac3f347085 | -18.55959 | -46.49776 | 2025-07-05 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d285f281-df01-3c2e-94ca-243f52ae0ffb | -19.08731 | -56.05265 | 2025-07-05 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 556e3ee3-50a8-3978-b739-f22ba42dc038 | -13.41625 | -47.84205 | 2025-07-05 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78053305-669d-3dae-ae6f-08b493b40850 | -16.67968 | -43.88219 | 2025-07-05 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb1be25-1a0d-32c9-8594-1258c5172b26 | -14.66422 | -45.37621 | 2025-07-05 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afe7dd67-b221-3b16-a4d4-17db55160b79 | -15.75125 | -43.37674 | 2025-07-05 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7079b0e-74bf-33ce-b2df-391be740e97f | -18.45462 | -54.7087 | 2025-07-05 04:21:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0bcf230-7ffe-3411-ab13-4e621a3d3f7f | -18.3328 | -52.04397 | 2025-07-05 04:21:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ca31dab-e4d5-3cc8-ad50-ff65133de4c1 | -20.37688 | -45.60221 | 2025-07-05 04:21:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7c841c3-0759-3d5a-929f-2e3e2dd5ff38 | -18.45553 | -54.70406 | 2025-07-05 04:21:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53fce209-31ec-3a93-8ee7-397b8608ec50 | -17.9113 | -45.54124 | 2025-07-05 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 755628e6-5ec6-37b9-b00f-ae2cecfce9d9 | -18.84913 | -47.48444 | 2025-07-05 04:21:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8861ea1-fe3b-3bc5-b648-74994033d595 | -13.65024 | -46.80844 | 2025-07-05 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd95a9e7-f32d-39de-b315-95af1051b06d | -13.72691 | -49.00193 | 2025-07-05 04:21:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f99b8faf-e514-3ad1-aecd-0477f0fae26e | -17.76389 | -52.44707 | 2025-07-05 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a18a13e-d6ea-3420-9f22-b5a18a70e892 | -19.43716 | -44.33897 | 2025-07-05 04:21:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be219452-65b2-334b-a8ad-918b1ba70248 | -16.29808 | -45.10126 | 2025-07-05 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72e3ee76-c833-3672-b524-e5b65d253cdb | -17.49952 | -44.28137 | 2025-07-05 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88964317-8969-3a2e-9121-b39e2750aaa4 | -19.12761 | -52.68936 | 2025-07-05 04:21:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b9a224ad-65e0-3fd5-9499-e2209b91d30b | -15.70001 | -48.30379 | 2025-07-05 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5bde1c86-62ed-3854-87db-c68838747d14 | -13.69795 | -47.73547 | 2025-07-05 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 182af251-fadf-308c-9431-a3829ece9331 | -19.57378 | -54.45068 | 2025-07-05 04:21:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48fb0763-f333-3ce3-b2a3-5f54fc032ed6 | -18.88202 | -49.01915 | 2025-07-05 04:21:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5ef6a40-b564-3fa5-80b6-7f83d70ca3ba | -15.75187 | -43.37226 | 2025-07-05 04:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96fbc92a-e2a6-35bf-ad8f-4be090fd65b1 | -14.66478 | -45.37254 | 2025-07-05 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bec67d6-13a5-309a-85af-14b7441cff3c | -14.8875 | -48.35955 | 2025-07-05 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 6524f15f-1153-3bdb-b888-e985c1cb680e | -18.66331 | -55.74623 | 2025-07-05 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f089d801-5e0f-3159-b502-b0c58eecf07f | -12.57969 | -56.97685 | 2025-07-05 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d953ff88-cd2b-324a-9ad2-cfee455167e2 | -19.82869 | -42.7013 | 2025-07-05 04:21:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0002b019-d31a-3bb5-8261-96c03166daa0 | -20.7245 | -56.65227 | 2025-07-05 04:23:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 110958a0-02c3-3e73-a86e-e44e7b06d758 | -20.72336 | -56.65783 | 2025-07-05 04:23:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 63b7ed5a-338d-3021-bf43-74c2e2e24a2a | -21.47221 | -44.48578 | 2025-07-05 04:23:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 85b79ff0-9568-329e-82df-6d087f552ba9 | -21.26429 | -46.00861 | 2025-07-05 04:23:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3e22a9ae-495c-3721-be4c-f1df3c277519 | -21.89323 | -56.73502 | 2025-07-05 04:23:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b6e8f1c-0c20-3837-8432-2e340940d505 | -20.44345 | -50.7291 | 2025-07-05 04:23:00 | NOAA-20 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ff2468d3-4633-3453-93cc-151bb05ffa5e | -21.7611 | -48.57655 | 2025-07-05 04:23:00 | NOAA-20 | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a699309-6ab6-309e-b2aa-6f9e38f60b84 | -25.19205 | -49.32805 | 2025-07-05 04:23:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1497ff9e-421f-3afc-92f8-6b3e4bb3847b | -23.6255 | -46.49644 | 2025-07-05 04:23:00 | NOAA-20 | SANTO ANDRÉ | SÃO PAULO | Brasil | 3547809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c37ad5c9-3473-3cf5-9667-60f4621d294d | -21.88693 | -45.5868 | 2025-07-05 04:23:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 743ac494-e7e7-31a8-9ecc-90dcf4c8b826 | -21.89684 | -56.74178 | 2025-07-05 04:23:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78b5eea2-2af2-36b7-a926-cbd9206a54e8 | -23.21201 | -45.8779 | 2025-07-05 04:23:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1dc38375-7928-372a-94bc-28f6b174d249 | -21.60503 | -53.81671 | 2025-07-05 04:23:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 167fb1ab-502e-3ca0-b765-1755e029600b | -21.20835 | -48.63452 | 2025-07-05 04:23:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e367ae7e-b45c-3076-81b2-2d01a7cd4e0d | -20.43996 | -50.72838 | 2025-07-05 04:23:00 | NOAA-20 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d229f82f-9119-36bb-be7b-a07d4572b847 | -23.59235 | -47.439 | 2025-07-05 04:23:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ac848652-f26d-3c10-88dc-1f01b405cc10 | -20.47676 | -53.67573 | 2025-07-05 04:23:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be3866f3-2a97-36f3-8fa7-80d514576ad3 | -20.43718 | -50.72355 | 2025-07-05 04:23:00 | NOAA-20 | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 95ed9956-a0b7-3bf7-b282-fd7749eddc16 | -21.21025 | -48.6653 | 2025-07-05 04:23:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c6d8529c-ddef-3f9b-8152-e82399cb6f5d | -22.67391 | -42.85659 | 2025-07-05 04:23:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 32fa1586-97fd-3bd4-9757-784a2049ccfc | -21.03602 | -47.80876 | 2025-07-05 04:23:00 | NOAA-20 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c21a576a-b57f-3748-8cce-02402151e3d7 | -24.7434 | -53.80596 | 2025-07-05 04:23:00 | NOAA-20 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1d17a354-8660-3124-8838-0e636ed2e6b6 | -22.78408 | -43.75931 | 2025-07-05 04:23:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e30c45f5-5e2d-3c78-b3f4-ebb809832c85 | -21.9531 | -57.58545 | 2025-07-05 04:23:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 015d4c4f-bda1-362f-ac74-b4eb8296c577 | -22.53913 | -48.81091 | 2025-07-05 04:23:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f08ff24f-d87d-3708-b074-7693ea36a0be | -23.61666 | -47.44661 | 2025-07-05 04:23:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 382ce53e-cd48-36a1-8652-c7ca2d421494 | -22.12657 | -42.69939 | 2025-07-05 04:23:00 | NOAA-20 | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 21e4c4d9-b6d6-3442-a502-4e96e4b5f1e0 | -20.46385 | -50.4839 | 2025-07-05 04:23:00 | NOAA-20 | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0c79f18e-b3de-37aa-a1ea-fddc54e1951d | -21.26716 | -46.01323 | 2025-07-05 04:23:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ebef504b-cfde-3154-b47c-cd11d472c631 | -30.14883 | -52.02362 | 2025-07-05 04:25:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| a67c3d7d-53c0-3c60-80c3-763cf2a51c10 | -5.614 | -45.1738 | 2025-07-05 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ef32d67-0da2-3f02-84a3-4552e232a711 | -8.09295 | -45.39747 | 2025-07-05 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README12.md)
