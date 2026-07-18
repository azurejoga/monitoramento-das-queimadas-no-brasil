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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b60f9bf1-5255-3503-8a2b-4cdb357735a5 | -28.75142 | -50.0013 | 2026-07-18 04:44:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1580b10a-4085-3277-93d9-4503d338bbbb | -29.04007 | -50.88107 | 2026-07-18 04:44:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b21885fe-5ee0-3186-8820-db2e40ada522 | -31.12584 | -54.40616 | 2026-07-18 04:44:00 | NOAA-20 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 23a101e4-4330-3b56-b604-547e6231be8a | -32.29921 | -53.36 | 2026-07-18 04:44:00 | NOAA-20 | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| ad7a3c71-fe19-3b47-ba4d-48f953628d43 | -29.07612 | -50.72501 | 2026-07-18 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ace8cb15-24bf-3553-908b-d5771948bd6f | -29.94109 | -51.63999 | 2026-07-18 04:44:00 | NOAA-20 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 53280932-ed73-36e7-985c-be0f879f09ee | -31.55602 | -53.25056 | 2026-07-18 04:44:00 | NOAA-20 | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| fcbb54c8-45e7-31fa-afbd-ea2e67b71ea3 | -29.07662 | -50.72302 | 2026-07-18 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4b59aacf-d09b-33e7-b4ac-3a7aaa738905 | -28.99766 | -50.5881 | 2026-07-18 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3933108e-801a-3f17-959d-08cf70276f37 | -30.69608 | -52.56098 | 2026-07-18 04:44:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| fd6078a0-3c82-31f3-a26e-39fe936bea18 | -29.92609 | -53.90987 | 2026-07-18 04:44:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 28531900-810b-36f3-aec2-5c26f757c5ba | -29.03816 | -50.15897 | 2026-07-18 04:44:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 084604f9-49d0-34e9-bf1b-1cdd6d37d8c9 | -28.7544 | -50.00659 | 2026-07-18 04:44:00 | NOAA-20 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c786ceb3-b9b4-3277-b3f4-78502a5564e2 | -27.54544 | -53.06549 | 2026-07-18 04:44:00 | NOAA-20 | LIBERATO SALZANO | RIO GRANDE DO SUL | Brasil | 4311601 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8578c6a4-263f-3374-8660-29b6d9ed262b | -31.12915 | -54.40688 | 2026-07-18 04:44:00 | NOAA-20 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 77e0afdf-24d3-3e6b-bf41-6d63aae1cbbf | -31.12253 | -54.40544 | 2026-07-18 04:44:00 | NOAA-20 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| d9e2eb14-71dc-3104-8ebc-c1020f558308 | -28.88429 | -50.73338 | 2026-07-18 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d6f1d65c-4198-3c6d-bc5c-b7309cb8dd6d | -28.89009 | -50.48097 | 2026-07-18 04:44:00 | NOAA-20 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| abbec0a0-5b3a-3288-a085-acffb9e9844b | -28.93947 | -50.67101 | 2026-07-18 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e39522b2-2c25-3961-b0a8-5abb3373b69f | -29.07673 | -50.72062 | 2026-07-18 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 27cf5d53-66c2-33b0-96f8-e6598315d789 | -28.8872 | -50.73835 | 2026-07-18 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 44363348-2f1c-3764-b48b-0653f6dcc356 | -13.3217 | -45.1479 | 2026-07-18 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 263.4 |
| 6bc821de-70f0-3d0d-86bf-d1446356feb1 | -20.0252 | -57.9468 | 2026-07-18 04:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 1a6c3005-daef-304b-8727-c5e599a35300 | -13.3023 | -45.1511 | 2026-07-18 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 104260d9-d34f-3c15-ad97-b104332b9ca9 | -18.7364 | -54.1988 | 2026-07-18 04:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c27942a4-f566-392a-8154-49a33bf51445 | -13.3221 | -45.1246 | 2026-07-18 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| bd057549-92ea-30e9-89f9-b1ef1bfa4c2a | -13.3028 | -45.1278 | 2026-07-18 04:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 7d8ec2d4-2c18-35a9-aab7-fa98b851ad4b | -13.3023 | -45.1511 | 2026-07-18 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| f830c872-f6bb-389c-a522-79eee91fcf6b | -13.3028 | -45.1278 | 2026-07-18 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| deb98b5b-7519-3e06-9a3d-d0f6c0de82fa | -13.3217 | -45.1479 | 2026-07-18 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 294.8 |
| 6505d638-3192-36e0-a155-8437b12acb5b | -20.0252 | -57.9468 | 2026-07-18 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 7689f2e3-09d3-3b0c-822e-95bc4587a471 | -18.7364 | -54.1988 | 2026-07-18 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a35bb579-f5df-3184-9a63-0f61fea866e1 | -13.3221 | -45.1246 | 2026-07-18 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 183.2 |
| e7edc363-8d62-3fd6-8cb7-903da6430e59 | -13.3221 | -45.1246 | 2026-07-18 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 2f91366e-ca96-339f-8953-3634b2fb08d7 | -13.3217 | -45.1479 | 2026-07-18 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 374.9 |
| fa4d834a-fbd8-324b-8de3-d2c3113899e4 | -13.3028 | -45.1278 | 2026-07-18 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f38192b8-92d0-334a-a22d-e827f844e18b | -18.7364 | -54.1988 | 2026-07-18 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 3f5c1348-84f5-3c9a-8b60-6b3070bced60 | -13.3023 | -45.1511 | 2026-07-18 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 0dae1331-348d-31d8-b56c-a69103da7a87 | -13.3 | -45.14 | 2026-07-18 05:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4657538-e295-3402-811c-474d68ab3aea | -13.3023 | -45.1511 | 2026-07-18 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 192.7 |
| c38c0e42-cfbe-3e54-8992-b80987a9e26f | -21.2636 | -49.0973 | 2026-07-18 05:20:00 | GOES-19 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.0 |
| c2f007a9-24bc-3348-8fc8-074e2b1432d8 | -18.7364 | -54.1988 | 2026-07-18 05:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e25c15d3-b0d9-3953-97a7-3886fa8df25d | -13.3221 | -45.1246 | 2026-07-18 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| f3aaba06-be59-397a-a225-ee7a204f6cf1 | -13.3217 | -45.1479 | 2026-07-18 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 245.3 |
| cb1760d6-4cf9-308a-b7f9-7ae281a8d8e9 | -13.3028 | -45.1278 | 2026-07-18 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 175a6e8c-6664-347a-a306-18c6d800f39f | -21.263 | -49.1205 | 2026-07-18 05:20:00 | GOES-19 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.8 |
| 6ccabd7d-ab61-3ab1-8a39-799b38086a18 | -9.42115 | -63.19242 | 2026-07-18 05:23:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08e9c0e2-8418-38d0-88e7-dcc2c043bf5d | -9.1665 | -50.88991 | 2026-07-18 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25e27780-a117-3172-9474-14681d4b2dce | -9.30142 | -51.92178 | 2026-07-18 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac371c15-3ade-31a5-8294-a8d4f11d1dde | -10.53012 | -48.15665 | 2026-07-18 05:23:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 612bff94-956f-3db3-a71f-a23064c229d2 | -4.09864 | -49.35796 | 2026-07-18 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26a597da-f513-3676-b5be-cd4f6a70c7bb | -9.09548 | -50.61238 | 2026-07-18 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c30f46ae-aca2-3d9f-ae88-60067f031f8e | -1.81931 | -54.47756 | 2026-07-18 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfb36bdf-4b46-3c6e-a5c9-dc9881dfaec9 | -2.15487 | -53.65146 | 2026-07-18 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4ef2106-c128-354d-bc1d-d727b7874f45 | -2.79067 | -49.52744 | 2026-07-18 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 997f4b3e-8b51-3319-973d-77f2c7697355 | -2.7687 | -49.46607 | 2026-07-18 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8be1fd6-e79a-348c-9068-86b285ae9334 | -9.08911 | -50.61586 | 2026-07-18 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66fa7ce7-6824-33c0-bc9f-c2a3f9f13a35 | -2.77443 | -49.467 | 2026-07-18 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 705429eb-a546-3629-87ef-da7e434efca3 | -4.09759 | -49.35511 | 2026-07-18 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd6c4591-e163-37e1-864b-a2a76c29f593 | -2.76948 | -49.47111 | 2026-07-18 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9ff2f347-6f0d-3585-b0bf-c1b2b949246c | -1.81773 | -54.47787 | 2026-07-18 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b64602f7-6fed-31c6-9e98-ea543086df43 | -7.69155 | -55.36498 | 2026-07-18 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a8930a6-c1dd-3967-a41e-37521b592681 | -9.08013 | -50.59323 | 2026-07-18 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bda7cce-8ebc-3b79-9d03-a1036c3d55ee | -9.89229 | -53.38549 | 2026-07-18 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03023a03-7604-3255-ae36-260a91ff7ade | -9.69959 | -47.70234 | 2026-07-18 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 219f6bd0-c578-3017-b77b-ae43c17c0106 | -4.10347 | -49.35611 | 2026-07-18 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4886ef08-c1c3-3ad2-931a-cc5073d7a0cf | -8.94445 | -47.61719 | 2026-07-18 05:23:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3b83989-eb06-3474-b53c-ba4d3112c3fd | -9.07431 | -50.59237 | 2026-07-18 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cb87cc4-56ae-3a7a-b85d-3b36b9641616 | -9.0971 | -59.40121 | 2026-07-18 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0da43ddb-aecf-349f-bbe1-6441e7b57f20 | -2.79697 | -49.52434 | 2026-07-18 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbb59f4a-a4c7-3971-9c1d-97bc3f6cc339 | -2.7681 | -49.47006 | 2026-07-18 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68e51dae-8590-3a20-b599-9c2ff8a5df41 | -1.81827 | -54.47438 | 2026-07-18 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e473a47c-f970-34a6-be73-0c51b07e6159 | -9.30499 | -51.92112 | 2026-07-18 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c95e0d7-50d2-3665-95ed-d046c8cad84c | -9.90137 | -53.39215 | 2026-07-18 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 728eb75b-8b0a-3257-9fec-13793ddde1c5 | -4.36853 | -55.76967 | 2026-07-18 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51672814-f05e-3dcf-80e2-0a17c0ff92ac | -2.79125 | -49.52348 | 2026-07-18 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c9e3880-9f28-324e-a1be-4fc63d694995 | -9.48236 | -57.3257 | 2026-07-18 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 327f985e-f544-3766-84eb-a9ce6373e872 | -8.71678 | -49.60379 | 2026-07-18 05:23:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92272afd-ea2a-3fe5-a958-6ffa5cd37ede | -9.88345 | -53.33849 | 2026-07-18 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd785233-c55c-3010-84d2-2d6457e00979 | -9.91584 | -53.3201 | 2026-07-18 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 125fef15-bd89-3a2f-8285-f61b4e1061d6 | -11.54988 | -48.25824 | 2026-07-18 05:23:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d1713e0-5a7e-3b89-826e-af94cf61e778 | -9.68653 | -56.10213 | 2026-07-18 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60cabad8-5928-3285-8114-c1a376dda805 | -9.82858 | -57.84919 | 2026-07-18 05:23:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9be0260-7231-37fc-9118-edd353cc0a5c | -7.69103 | -55.36869 | 2026-07-18 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89a8105a-98f9-3bac-a003-5c2b47c58351 | -2.77006 | -49.46711 | 2026-07-18 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cc2107dc-fa89-3414-9609-fc835963b06b | -9.07377 | -50.5966 | 2026-07-18 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b27cfdf-7f2e-3dec-8d1f-f44d3c234f21 | -8.47598 | -50.22536 | 2026-07-18 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21e9bdb8-2895-344e-bc0c-af0541cfab11 | -8.6636 | -66.56581 | 2026-07-18 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be31eaa3-8d07-38f9-8eed-ffcf681ef845 | -9.30188 | -51.91837 | 2026-07-18 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c33eb592-5684-37d8-8e3a-9cdb7558013a | -9.47928 | -57.32058 | 2026-07-18 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 633b9c08-97bc-3fcb-a2cf-c03fba2974df | -9.10129 | -50.61325 | 2026-07-18 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a1f0a2a-2b33-3dfc-98c1-4bc23f8d8877 | -2.77382 | -49.471 | 2026-07-18 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2df833c8-c927-32c2-8ae4-d986d486bdad | -4.09927 | -49.35368 | 2026-07-18 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f523d7d-eb7c-33bc-9bc7-229e202d440f | -11.54912 | -48.26485 | 2026-07-18 05:23:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da00b4ff-bfe2-3b74-9aa9-2645e5927e09 | -8.94525 | -47.61055 | 2026-07-18 05:23:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e95e393-90c1-339f-94f3-f33fe51c43df | -9.16699 | -50.88607 | 2026-07-18 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebd77aa7-5136-3758-a149-4dc18ef4c4f4 | -1.59006 | -50.43867 | 2026-07-18 05:23:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e61df3f9-9d00-3fe8-947d-6e741ba11cc6 | -10.90918 | -56.36674 | 2026-07-18 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c038306-4cd2-3d0a-9822-d5a23baf69f1 | -12.11145 | -63.04299 | 2026-07-18 05:25:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f182c9e9-472d-3fac-95c8-2b2d3afdab1e | -7.91514 | -48.25786 | 2026-07-18 05:25:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README15.md)
