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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 315a37ca-554f-37ff-a2f2-bbb9d67ceecb | -11.68019 | -43.89749 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fa908b0-426c-3b72-b3ff-14793e74057d | -14.91904 | -46.71558 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f6f0cc5-734d-3405-980c-b1504b4ba92d | -11.34915 | -44.21032 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d669a170-d80d-3847-b780-08a1ce5b59f5 | -13.45971 | -48.1114 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84b9e20b-8e70-3aa8-98e7-6dbbf094b8e7 | -15.53038 | -45.69839 | 2025-10-18 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99c72c8b-8ea8-3dab-96f3-68ae3c9b53e9 | -13.92411 | -45.59644 | 2025-10-18 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aafc104c-6df2-304c-83a2-f9e6ba9ddde0 | -15.74929 | -41.91499 | 2025-10-18 04:32:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b5cc9f9f-c49a-3450-b406-542a1544e5a8 | -14.7419 | -47.42109 | 2025-10-18 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d869839-28c2-36e0-826d-d66a71d77afb | -13.04095 | -46.94847 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0709ae6b-270d-3891-a394-3649c1475780 | -11.45758 | -44.20749 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32ad7763-e32c-32f2-a92e-a5f17e37983f | -13.22593 | -43.97664 | 2025-10-18 04:32:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74157e38-6a83-3221-999c-6ef6884c24f0 | -13.73129 | -48.12008 | 2025-10-18 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a547fa7-f7a2-3036-b842-43fe2a524479 | -16.1301 | -46.87693 | 2025-10-18 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0589ed21-982f-329f-b289-679ded253749 | -13.76921 | -48.24673 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8ca81ade-c18b-3ba4-af78-7fd1a4ab35bb | -15.80034 | -43.57275 | 2025-10-18 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 285bcaca-0a01-3fd1-9e9f-eac9ecfcddf0 | -13.03312 | -46.95462 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15b7ba78-846b-39e3-9b14-0742e41534af | -12.16161 | -45.08939 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1290abd6-ea4d-39b1-88f4-a6852aba1363 | -10.9996 | -47.9011 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b01b7d10-b8f2-3e98-9f47-96d8841eb249 | -18.40012 | -41.82391 | 2025-10-18 04:32:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99563ca7-be93-3a3a-b7f1-af8d3fcb892d | -13.0348 | -46.94382 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bfeb64f-8a02-36ac-926c-c671e26827da | -11.35279 | -47.29785 | 2025-10-18 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 898a3edb-f5e6-3289-875a-8733c24b0c82 | -13.03427 | -49.23359 | 2025-10-18 04:32:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5d2a977-946f-305e-bf85-c77c78bd8bcd | -12.60853 | -52.8213 | 2025-10-18 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6010e26-26b3-3aee-b510-28ffeaad598a | -13.72918 | -48.11998 | 2025-10-18 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f938590-2a8f-3cfd-a1ea-00e7790f50e7 | -19.10705 | -57.55121 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2366b031-f8dc-3ca1-8947-18e1b5586e6d | -19.1022 | -57.55011 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cba975fb-b675-327e-b88e-cf5a5202aacc | -19.21223 | -42.91996 | 2025-10-18 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0ebbb899-407a-3445-b6ea-627743d5577d | -17.02358 | -55.9189 | 2025-10-18 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 560fc5c5-1417-301b-b9de-4e85dee279b8 | -19.11189 | -57.55231 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6dc2b3a0-e421-3a8b-807a-fde744fb4877 | -20.09046 | -43.01266 | 2025-10-18 04:34:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f29e0f5a-b296-3282-a048-4c54d8b7de9b | -19.21201 | -42.92214 | 2025-10-18 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0e16d100-cdae-3d2a-b907-6b31a1840c2d | -18.38064 | -55.43419 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 90b5b516-1804-39c2-ba04-cc3ae50c198d | -19.09735 | -57.54901 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a887de5a-8b14-3e3f-9c2d-7ac714bd4690 | -17.02377 | -55.91746 | 2025-10-18 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a623aa73-5ad6-36e2-820d-a810c24c901e | -17.44159 | -55.02728 | 2025-10-18 04:34:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8e4014e3-b0b2-34e6-91a5-0eda1279ca2b | -17.01922 | -55.9165 | 2025-10-18 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4ad34601-f36e-3282-aaf7-737f586cde8f | -20.26636 | -42.70154 | 2025-10-18 04:34:00 | NPP-375D | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5cd626f4-9003-3b8d-b54b-63b7e8727bdc | -19.10075 | -57.54695 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bb48e0b5-5f51-3a74-8251-7800c26e9204 | -19.48924 | -44.86515 | 2025-10-18 04:34:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 373a8b91-fb05-32ed-a47e-dcb200ed6090 | -18.38271 | -55.47023 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8f48654e-db7a-38fa-9ba4-1137e14e3b6a | -18.38969 | -55.48065 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 402a3af8-2122-3dd5-9c68-f417eda77dee | -19.48796 | -44.8686 | 2025-10-18 04:34:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 24053ad2-80a0-3f02-a521-3772a3f472ec | -20.05285 | -44.75076 | 2025-10-18 04:34:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48d978a1-872f-3673-b290-b81410bd2d12 | -18.37982 | -55.43847 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a36de331-08da-3a77-a466-194856597734 | -19.48858 | -44.87027 | 2025-10-18 04:34:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 582025df-8de7-3ac2-9a92-0e05d229fe06 | -18.3747 | -55.44183 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fce9cdf8-87e4-3c02-ba9c-e246b981ed7b | -19.09963 | -57.55256 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d620cc82-9eb2-3a63-a987-45e96833494a | -17.4408 | -55.03144 | 2025-10-18 04:34:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bd6f6fec-2c4d-3396-ba68-6db635371d45 | -17.34639 | -55.09594 | 2025-10-18 04:34:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3e115ec2-acd5-3163-844a-825a9884b09b | -17.95801 | -57.63238 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9861cd95-73bb-3da7-82c2-c5c43767b450 | -18.38538 | -55.47973 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 0c1cc075-2555-3de9-b8e7-efa5965b9f1a | -18.3862 | -55.47543 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 7b36f50f-9219-36bd-80ea-c3cb72cc57ee | -19.09619 | -57.55462 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7015d628-52c5-31bf-afd7-b9b2ccf139df | -17.02471 | -55.91267 | 2025-10-18 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f1c6020f-b5f6-3403-90e2-30430e36980f | -18.3905 | -55.47635 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c3c89aa3-0adb-3215-8314-f82a572a739e | -19.10588 | -57.55682 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c6959c2c-f1ce-358c-bc08-9b5b0c6d6f36 | -18.37737 | -55.45129 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3218040d-906f-3c41-a738-4fbadace2f53 | -19.21164 | -42.92458 | 2025-10-18 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ea7ae116-afe2-3d85-b516-74e8fe897ee2 | -19.10559 | -57.54806 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7ceb7e93-db02-3182-8a0d-77e794c1535f | -17.0245 | -55.91409 | 2025-10-18 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 565331b4-8bed-3c43-b3cd-891439bf6880 | -18.38189 | -55.47452 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| cc5b182b-7edb-3378-8e47-744f41fb74e0 | -18.379 | -55.44275 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cf119676-cfb8-387c-8628-e1c85e84e729 | -18.37634 | -55.43328 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c6fd6ba9-b87c-3481-8c21-5df477b9c977 | -20.05548 | -44.75244 | 2025-10-18 04:34:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5939d32b-de41-3238-b82e-96e60e9c6126 | -17.01996 | -55.91312 | 2025-10-18 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 403f7abe-2694-3116-bc0c-90643ccd2b9d | -19.10104 | -57.55572 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 65f56d9a-dfa6-3c8f-ba3c-cc590c751c9e | -17.44585 | -55.02816 | 2025-10-18 04:34:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75226910-b03a-36d7-bf12-cc304535d0aa | -18.37552 | -55.43755 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 919fd78e-9af5-32f0-b02f-04bf74cbec74 | -19.1285 | -43.27017 | 2025-10-18 04:34:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 142e77ce-1197-3c70-ab17-14dfb9f04259 | -20.27084 | -42.70224 | 2025-10-18 04:34:00 | NPP-375D | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba644cda-8d95-386f-971a-6b23bd83f837 | -19.10447 | -57.55367 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 042b4daa-24c9-385c-8933-0d7b1fa580f3 | -18.38702 | -55.47115 | 2025-10-18 04:34:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8a51b51f-8adc-39c5-bfec-b0592b10685b | -19.11073 | -57.55794 | 2025-10-18 04:34:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ce3c4bc5-8fd8-3eed-8414-c0903ee828b1 | -10.9755 | -45.4553 | 2025-10-18 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| bd9b9341-9d32-32dd-b6cd-ca3cdd045bdc | -4.4446 | -43.2164 | 2025-10-18 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| d234bca2-766d-3e5e-af29-8e918d8445e5 | -4.4445 | -43.2397 | 2025-10-18 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 53bb5033-433d-3918-b854-5171a512aa1f | 1.7664 | -55.9805 | 2025-10-18 04:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 0f0a84a9-781d-3a62-a628-bf13a8d4275a | -10.9564 | -45.4579 | 2025-10-18 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 4af8a4ca-bfbc-3305-ac00-6c6b183860c2 | -5.0215 | -46.0097 | 2025-10-18 04:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 43c11850-97e8-31b0-9772-7c6a350f190d | -4.4632 | -43.2386 | 2025-10-18 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| e7c58740-1f2e-3d03-80c8-be30ac2c745a | -4.4633 | -43.2152 | 2025-10-18 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 9555b526-e3b7-323d-bdf0-159a9bff4515 | -6.5631 | -51.1126 | 2025-10-18 04:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c9d14bf8-863f-3bc7-864e-cc20a49ec815 | -10.4941 | -43.4315 | 2025-10-18 04:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| d7e53750-92c7-3d0b-b74f-86f541f94c31 | 0.99221 | -51.19316 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 382acb2a-270d-307c-b3ee-6ac878e3edcc | 1.77001 | -55.93176 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 203ba32b-4030-3d88-ae95-f2c2e4867b46 | 1.49968 | -56.04835 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32025122-764d-30de-b7b6-42514d59747e | 1.32062 | -51.25094 | 2025-10-18 04:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a024fcc9-fe2a-39ec-b633-0d1120fb60b6 | 1.77236 | -55.91982 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dc7390c-34d5-398e-b425-d0c36593ca1a | 1.76281 | -55.967 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 810c54a6-6d11-3d81-8471-ac6cd1baccc4 | 0.86118 | -51.37579 | 2025-10-18 04:46:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33c82327-be77-33db-968e-b9a2e3192c7e | -0.75351 | -47.76328 | 2025-10-18 04:46:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0719990-8385-3036-a6d1-c44b72f10951 | 1.76157 | -55.98629 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 423c437c-7757-30a9-8a99-c6c0036bbd68 | 2.0186 | -55.84901 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25b16b8e-d2da-3b1e-921d-509e1a9aecad | 1.87653 | -55.65146 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1dfa247-2ad3-389d-b9c3-ca6ae30e346c | -0.90403 | -47.54554 | 2025-10-18 04:46:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff13677c-cf6f-3b48-b95c-c68a49d96774 | 2.16517 | -50.91764 | 2025-10-18 04:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8c6322a-1f11-33cd-90c1-66c47cab9b4c | 1.82138 | -55.7006 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a373b36-05d3-3df3-b25e-07ec5b74e561 | 1.76943 | -55.92803 | 2025-10-18 04:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4cfc7d5-7a94-3352-bdf8-d60023ecaa74 | 2.01992 | -55.8299 | 2025-10-18 04:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d034d87-2dff-393f-a4de-b518b8976ead | 1.25492 | -53.07506 | 2025-10-18 04:46:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README66.md)
