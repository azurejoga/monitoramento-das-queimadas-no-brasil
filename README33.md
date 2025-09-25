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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efe9d9a1-5ff0-3afc-99e0-a4b4edd5a4fd | -16.58382 | -56.76765 | 2025-09-25 05:04:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d95f7ce8-0c24-3e70-9941-2e97ef63cbb9 | -20.79982 | -56.95726 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b776a11d-f84c-39bc-968e-6868a9511183 | -15.90629 | -59.35011 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0345463e-12df-379e-8c06-814a0c6b14f3 | -15.93605 | -59.35936 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6d84b7d6-d741-363b-8886-e30f7fc379c7 | -20.99221 | -50.47663 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 51aa8591-661f-37ba-88fd-6eb4aeb807d0 | -20.70584 | -57.86259 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c70fda6f-20c7-3adc-addb-111c9bdf56c2 | -15.76513 | -59.47903 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 94662b87-e583-3098-87a1-feb790f3cab2 | -20.08368 | -54.62164 | 2025-09-25 05:04:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c4f613a-c764-34c2-9809-6734cf372d02 | -20.98956 | -50.01301 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| bf51752b-d99d-3b55-9a01-053c10aff3cb | -15.8302 | -59.60019 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74ca9d09-f4f3-3c94-8b91-f71e2a3a0c14 | -20.70096 | -56.74128 | 2025-09-25 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29b056e7-bfd5-35ab-8644-f438da6edf7b | -15.35796 | -59.19407 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1524dc3-edee-370b-931a-3bd2b28703d2 | -20.24294 | -56.05698 | 2025-09-25 05:04:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d1bb643-1dfd-3ad7-82b4-86d45dbd4844 | -15.86989 | -59.34779 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2e33292-e86c-32d8-998b-bd301fbb6169 | -22.36266 | -49.47963 | 2025-09-25 05:04:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 215c4619-432f-3930-b7ef-464c4f29a142 | -17.94124 | -55.86356 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| d1826d75-678a-3f19-b07d-cfc99850cbdf | -15.87418 | -59.34426 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75c168d5-40cf-3b21-985f-027a349a82f9 | -17.939 | -55.85558 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 27c52f86-e706-357e-bb9d-40e80aae1f0b | -15.97346 | -59.50651 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d470ca0-e6be-30e7-8a99-2b74571b49f0 | -15.35724 | -59.17672 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 575c4bfb-75c1-372b-b41c-19ca3bffa3c8 | -20.98693 | -50.4775 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cc04f086-9bcf-3e27-8c52-bbbd9b7d57e2 | -17.22988 | -52.40508 | 2025-09-25 05:04:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac630629-3574-39f2-8b88-9c0c35de53f9 | -15.75721 | -59.48197 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d21c6feb-6ca3-35a1-8c05-90b00a8aab2f | -15.91962 | -59.34801 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c777d081-0890-363f-bd9c-c7f79921a0b4 | -15.3601 | -59.18153 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfd25c1f-4acd-3493-af37-bc381845107e | -20.98879 | -50.46633 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6fd59753-eeb4-38f7-9828-f42d1a3be682 | -20.71976 | -57.86129 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 695cb359-50e1-3aea-ac97-41df88ff78c9 | -18.18616 | -53.33216 | 2025-09-25 05:04:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ad4a4ee5-9719-3cc9-8f4c-b5f21f7c18f8 | -21.83628 | -50.57841 | 2025-09-25 05:04:00 | NPP-375D | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d8707a63-616c-3811-bd30-ec9e8b788671 | -20.9931 | -50.0239 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 980e4cb4-06a5-37dc-943d-02fdb2ba9d58 | -15.88628 | -59.40281 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edfb9fb4-2b41-3c61-916d-e2af73b304ab | -15.76947 | -59.47533 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5de68ec6-de22-39b6-b941-2ac0f09e5c40 | -15.76428 | -59.50575 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 48b10e0c-71ca-3ce8-a562-f85398e0a303 | -15.8549 | -58.13085 | 2025-09-25 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 423c0b5c-89ed-32f6-9866-bf4b6eada9ef | -15.88552 | -59.38561 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c2a06ca-b902-37dc-8049-99e71cf8b1da | -17.93058 | -55.86559 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 53b76fb4-8003-3015-b537-b96b8c0d62e7 | -15.28448 | -59.42757 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e998d60f-89c1-3120-9744-fbaa7ca5861d | -17.93675 | -55.87041 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| fa94088b-8eb3-37c3-9ae7-513be11f20ba | -15.80634 | -59.48046 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4d63bec-b490-3ee4-a512-2cfa387d9d6c | -20.69899 | -57.81945 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bb2e1425-b673-3912-8954-88e4431e0d0a | -22.61224 | -49.02578 | 2025-09-25 05:06:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33bbc6e2-dfff-32bc-93b4-717c43dacffa | -22.35932 | -54.61739 | 2025-09-25 05:06:00 | NPP-375D | FÁTIMA DO SUL | MATO GROSSO DO SUL | Brasil | 5003801 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d4956227-7222-3a4d-8118-7985e7c04e71 | -21.96439 | -56.67607 | 2025-09-25 05:06:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 189689e6-8dd9-394c-9123-d7cc13fc7641 | -22.36351 | -54.64092 | 2025-09-25 05:06:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e45119d9-2e8e-3930-91f0-7537f26f58f6 | -22.36413 | -54.63642 | 2025-09-25 05:06:00 | NPP-375D | FÁTIMA DO SUL | MATO GROSSO DO SUL | Brasil | 5003801 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 32acdfb7-fa9e-33a4-9a95-f95e61b4ac44 | -25.93906 | -52.06004 | 2025-09-25 05:06:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 60094b3c-2820-346c-9680-2b0e9a78623c | -22.70525 | -53.0136 | 2025-09-25 05:06:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dd9f53df-b73d-3ca2-ad19-37691ddf5c04 | -21.8592 | -55.95771 | 2025-09-25 05:06:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 003a71fd-342a-3f12-ae4b-9187182bdda3 | -21.99382 | -56.05484 | 2025-09-25 05:06:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b353c2cf-1635-31bc-badc-4920f67b2559 | -22.61255 | -49.02281 | 2025-09-25 05:06:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11eeaf0b-6ccf-3b74-b055-a111bf2a5d52 | -21.99324 | -56.05884 | 2025-09-25 05:06:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e99aa8a6-38e6-3aa9-8a86-8c73e61f8931 | -26.05886 | -51.76637 | 2025-09-25 05:06:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 565f6124-42e9-38a5-9978-eb3b7e0e68cc | -22.36777 | -54.63699 | 2025-09-25 05:06:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 80d95168-3244-3ba1-b660-f1ef23a62bc7 | -22.38229 | -53.73719 | 2025-09-25 05:06:00 | NPP-375D | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1879aa09-46cb-336f-8c3d-a586e3d299f0 | -26.0614 | -51.76872 | 2025-09-25 05:06:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| caedd8f5-b6cd-3708-a797-5dcc52227b69 | -21.99667 | -56.05941 | 2025-09-25 05:06:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a66f3e96-3554-3c90-8300-2f2f410806ac | -29.75546 | -56.02932 | 2025-09-25 05:08:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| b15079b3-333a-3809-8884-8aca02799188 | 4.41588 | -60.28569 | 2025-09-25 05:21:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ce0ffb-fbb9-3437-831c-6310fbe41642 | -2.1974 | -54.46179 | 2025-09-25 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d676642-49c1-3857-b788-a3a736b1bb52 | -1.82207 | -55.27877 | 2025-09-25 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6752b31-5d54-3782-9ecd-2e9af34b851c | -3.15229 | -49.47659 | 2025-09-25 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4312a309-5f3a-31db-9789-15aa028f44a7 | -2.19685 | -54.46534 | 2025-09-25 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af8af18a-72bf-3798-a206-e421ca969333 | -2.9241 | -48.31396 | 2025-09-25 05:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 8b30e6e2-4d11-369c-9afb-6a50482e05cf | -1.14809 | -54.22111 | 2025-09-25 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9beade49-99be-34ff-857d-991338917ca4 | -2.19225 | -54.46828 | 2025-09-25 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2395128b-a624-3787-9035-cff467a1ab87 | 2.33445 | -60.39931 | 2025-09-25 05:21:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d139fb2f-2364-383a-ba97-71a7e56edd02 | 3.99136 | -59.72179 | 2025-09-25 05:21:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb1f8538-fda4-3b62-81c5-bdeb3b0cb4c5 | -2.1928 | -54.46473 | 2025-09-25 05:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f389503-a4db-31eb-94a5-5e85ae9c1a52 | -1.72744 | -55.74337 | 2025-09-25 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d4a3e0d-9c23-335e-aca3-c2299148d8c4 | -3.39732 | -47.50152 | 2025-09-25 05:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce15a894-cf6e-3698-a32a-3330f3cfd07f | -2.2535 | -47.88561 | 2025-09-25 05:21:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b9b16e9-bddf-3bf6-94f7-ac53a93d29d8 | -2.92553 | -48.30447 | 2025-09-25 05:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 08d0f22c-a850-3508-82e2-f43196064d44 | -3.01483 | -51.35405 | 2025-09-25 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 998514ee-091e-3d64-8540-ff1b5048f7e5 | -3.01436 | -51.35706 | 2025-09-25 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdbb8490-8969-3cb7-88f8-591832f16ffe | 4.63208 | -60.69724 | 2025-09-25 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3875e625-7fec-3a79-96c0-91672d0a9173 | -1.82588 | -55.27938 | 2025-09-25 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 081639a8-c82a-3b11-9310-ed7b54e23fc8 | -1.60806 | -54.31832 | 2025-09-25 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f01ac546-0ddb-32d5-8b48-bca19f4a5cc1 | -2.18471 | -54.46351 | 2025-09-25 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a3aee9b-a45f-3e54-87a7-459321491ef7 | 4.37935 | -60.02908 | 2025-09-25 05:21:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90096de6-77f8-3f05-bdd1-7479dd409eeb | -1.53464 | -51.61826 | 2025-09-25 05:21:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f10f5c55-ce14-39a1-95be-93e0f2e6de9b | -2.24988 | -47.88851 | 2025-09-25 05:21:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 188e46d8-eee2-3cc3-a69b-accb9944f003 | -2.17625 | -56.63679 | 2025-09-25 05:21:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4243ce0b-9370-352e-abef-ab3bf32804f4 | -2.91862 | -48.3083 | 2025-09-25 05:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 647f38f0-7ec3-3fa4-a897-0135f0b9eb80 | -1.08657 | -54.10966 | 2025-09-25 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ee35018-3b9d-3522-80f5-432bae8876be | -1.80079 | -55.59045 | 2025-09-25 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fe6841e-ae5f-3a57-8eba-8ae92bc9d5f6 | 4.41528 | -60.28185 | 2025-09-25 05:21:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94d7d8f6-15df-3d91-b0e5-89389d84a996 | -1.94826 | -52.08512 | 2025-09-25 05:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 790d667b-ef10-3c2f-aad6-4aabe1d2df54 | -2.92008 | -48.29864 | 2025-09-25 05:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e4a8d42-58c5-3110-801b-a8f956a9b891 | 3.98743 | -59.71879 | 2025-09-25 05:21:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08fc2d65-b513-35bb-8a33-cfedae98abd7 | -1.59588 | -55.89472 | 2025-09-25 05:21:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71f5251d-bc80-37f6-bb89-65aad4b722d9 | -2.92482 | -48.30922 | 2025-09-25 05:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c1a8df93-49b2-3650-8597-a5280cac7adb | -2.91791 | -48.31304 | 2025-09-25 05:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0bfeb34c-d015-3502-a952-cf150366581c | -1.6075 | -54.31792 | 2025-09-25 05:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41860d24-b608-31ae-aef9-148b904bc46d | -2.24719 | -47.88473 | 2025-09-25 05:21:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43485ab3-a9bf-3552-8db6-ce0bf3e393fd | -2.91934 | -48.30354 | 2025-09-25 05:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dd4ee202-2517-3a69-af30-e90f8cebadae | -15.87798 | -59.34727 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7948135f-2567-3abe-84a9-5ff36b2d1842 | -4.16768 | -54.63409 | 2025-09-25 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 134d97db-6f06-338e-8566-c99d4a1cb261 | -16.85458 | -50.52046 | 2025-09-25 05:23:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b95a345f-6047-325b-a6cf-1c18ab1ee269 | -16.84972 | -50.51671 | 2025-09-25 05:23:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a877d85d-74ce-3c81-9a21-da8afb79cd21 | -15.35408 | -59.17724 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README34.md)
