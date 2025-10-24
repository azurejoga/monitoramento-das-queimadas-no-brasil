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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83d25cac-74c4-306f-9c04-2c5bfa07eca2 | -14.77631 | -44.97582 | 2025-10-24 04:40:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6465b78e-9f8b-3f03-a0cd-694f1a931ae0 | -11.99668 | -45.42548 | 2025-10-24 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1b07515-ed8c-38d7-badd-1dfd8b1cab21 | -12.07304 | -46.41298 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07cec442-86c7-31a4-a0cb-a19d1f9c4cd9 | -12.06966 | -46.43658 | 2025-10-24 04:40:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 917216c9-cd34-394c-ae7c-8100a082b4e4 | -13.88667 | -48.35768 | 2025-10-24 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 079b76ee-80b9-3258-a96b-1ad64e242445 | -12.55558 | -48.55739 | 2025-10-24 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1338c8c8-8963-3e4c-9bc1-a53dbfbab2f1 | -12.82505 | -47.25203 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53f6b062-4f0e-3cc3-a6f9-ef231cb813fe | -12.77636 | -47.38223 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30615fbf-ad27-3c89-877d-d23d3136eda7 | -11.47901 | -54.0107 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a7a736f-a4f1-3ff1-9dd3-fed96a6f76fd | -19.65246 | -53.56123 | 2025-10-24 04:42:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdab247c-edd7-3e01-8141-7755116b5206 | -20.36208 | -45.79832 | 2025-10-24 04:42:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ca6069a-ddee-3049-9651-6760b504780e | -21.29878 | -46.80477 | 2025-10-24 04:42:00 | NOAA-20 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 00f60e95-c052-3fd6-9999-7b3536846c70 | -18.3441 | -51.71386 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce57bda3-9ca2-3762-89b0-1e4ad642bcdc | -18.35791 | -51.71249 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 050eebed-058d-33f3-8281-2d78be912dd2 | -18.91346 | -47.18066 | 2025-10-24 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77a75fdb-8d24-3473-8a44-31cb5f795900 | -22.97555 | -47.39523 | 2025-10-24 04:42:00 | NOAA-20 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 35084ea2-7c04-38a1-ad77-ebc6d7735a6a | -20.20878 | -45.80676 | 2025-10-24 04:42:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b87210c-21e4-39db-b76e-1055fdc55a8b | -22.75556 | -52.19219 | 2025-10-24 04:42:00 | NOAA-20 | INAJÁ | PARANÁ | Brasil | 4110300 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f08afdc1-6237-36c4-ba57-e770b17660e9 | -21.7614 | -52.2663 | 2025-10-24 04:42:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| b06209d5-32dc-3699-a450-1c6b26e2f615 | -20.12994 | -41.79902 | 2025-10-24 04:42:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d6e832bf-21f9-3dfa-acc7-26c3243ecae9 | -19.15506 | -51.86887 | 2025-10-24 04:42:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 539f9aec-f507-3880-9c58-7e7766fd09a3 | -22.97923 | -47.39989 | 2025-10-24 04:42:00 | NOAA-20 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 82831547-e3fe-3c14-9acb-3c57b65fcc4a | -19.3475 | -49.9304 | 2025-10-24 04:42:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5e508bb-5a48-37d3-97cc-f07f8e1a4518 | -18.35081 | -51.69265 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6f0ac9d-4566-3d5f-b4aa-e519a66fc608 | -20.92391 | -55.77892 | 2025-10-24 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27501e1d-00bf-3793-b868-0b9c10fd1c60 | -18.34911 | -51.70354 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34ac2d3e-31a7-3277-aa48-0750b897108a | -21.76082 | -52.27003 | 2025-10-24 04:42:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 5fad20e6-89ff-334b-928c-d4dc05859c1e | -23.34811 | -50.40258 | 2025-10-24 04:42:00 | NOAA-20 | RIBEIRÃO DO PINHAL | PARANÁ | Brasil | 4121901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7b965112-b6e3-353d-a325-9bcc27a092a0 | -19.64556 | -47.8584 | 2025-10-24 04:42:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90a84ac3-1fc1-3354-a59a-d5fa6d4ac4d3 | -20.50107 | -54.60118 | 2025-10-24 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f67148f-edfe-385f-930a-f5a75889b40e | -22.75324 | -52.19315 | 2025-10-24 04:42:00 | NOAA-20 | INAJÁ | PARANÁ | Brasil | 4110300 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6f30967e-a8d4-37b7-b95c-6e987ac868d5 | -18.35848 | -51.70886 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96b2a3e5-fc57-3433-b59d-4753f1f2c856 | -19.88653 | -46.95928 | 2025-10-24 04:42:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67e29e51-cc14-3ae2-bc8f-ccb76e20cb77 | -18.35299 | -51.70048 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 938e6e2c-7321-342a-9031-640425f126e7 | -18.35961 | -51.70161 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efd5c56b-8631-3d00-8a68-a49db9ec6f34 | -20.65348 | -55.08214 | 2025-10-24 04:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec488186-8108-3d58-9862-5d21c1b32233 | -19.15562 | -51.86523 | 2025-10-24 04:42:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0439122a-f58d-3250-900f-8949d4db7cc3 | -24.41878 | -50.76408 | 2025-10-24 04:42:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 02b5ca77-1274-342c-83f4-d793c7e931d1 | -23.89124 | -50.82359 | 2025-10-24 04:42:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bc7c1f73-1463-399d-9b58-1207b1a82a0e | -20.40111 | -44.06293 | 2025-10-24 04:42:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 82510c43-8039-3c3b-904d-3cd64a3fd43c | -21.04406 | -51.3078 | 2025-10-24 04:42:00 | NOAA-20 | MURUTINGA DO SUL | SÃO PAULO | Brasil | 3532108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 91adefd7-8f4a-3643-9cf9-e230ea6f4044 | -22.59519 | -54.99754 | 2025-10-24 04:42:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c01c5c26-7134-30ff-8beb-3f76a06d82d5 | -21.12926 | -45.72871 | 2025-10-24 04:42:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 29707c85-f091-37b8-9b58-19f6124e6f19 | -20.83388 | -45.83987 | 2025-10-24 04:42:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 140ca4f2-97c9-33b4-8992-e7d82d59ad47 | -20.92541 | -55.7704 | 2025-10-24 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06131770-0076-31e4-988a-2ae45752b3cd | -23.54759 | -47.41587 | 2025-10-24 04:42:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36b0bc0d-e5d5-34a4-894d-76f07542f2e2 | -21.0426 | -51.30797 | 2025-10-24 04:42:00 | NOAA-20 | MURUTINGA DO SUL | SÃO PAULO | Brasil | 3532108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c6379ad6-c1e7-3510-b343-cb76d39c5074 | -23.38348 | -51.98848 | 2025-10-24 04:42:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d324e90e-dc3e-3c94-b0a1-1da692d88b86 | -24.12617 | -50.76777 | 2025-10-24 04:42:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 14e424bb-599a-3fb8-8319-862f4ffba1f8 | -22.59252 | -55.01332 | 2025-10-24 04:42:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e822b979-050e-35cb-8b63-3c5a8a3c033f | -17.78298 | -53.31054 | 2025-10-24 04:42:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3308e91d-d7bd-3bca-b213-1dc84e41b446 | -19.49734 | -44.22981 | 2025-10-24 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c04b4b5-6ae2-3664-b060-8c93aaba4cc2 | -22.3915 | -53.52808 | 2025-10-24 04:42:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 24b5d12b-dfb7-340a-98d8-cc75602a6306 | -18.60369 | -51.79096 | 2025-10-24 04:42:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6aded1f1-213f-3e9d-b755-6eda14d116ed | -22.97508 | -47.39931 | 2025-10-24 04:42:00 | NOAA-20 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ddbda172-bca8-3383-a6bb-e87ff6a221b8 | -18.12214 | -54.52197 | 2025-10-24 04:42:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42446ef5-ca4d-326e-b3bb-6053f42f7ece | -19.49546 | -44.22919 | 2025-10-24 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4c77b6b-be1a-37ad-ad9b-e7882edeaa7b | -21.12646 | -45.73095 | 2025-10-24 04:42:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 68b2f8cf-f310-33e9-9264-f46fae6820cf | -19.75526 | -48.27675 | 2025-10-24 04:42:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf7af131-f361-3760-b034-caa91f648028 | -18.91139 | -47.18173 | 2025-10-24 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba27a32f-0dac-3134-9d0f-4899d82caab1 | -19.32763 | -46.49346 | 2025-10-24 04:42:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fe34952-200e-37d1-8006-77321cf651ef | -22.97781 | -47.39684 | 2025-10-24 04:42:00 | NOAA-20 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cbbccbce-b607-3322-b051-0a6c5fa89454 | -22.1396 | -45.64301 | 2025-10-24 04:42:00 | NOAA-20 | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1005ae3c-71a6-3d0d-85e3-378d951ecc2f | -18.35517 | -51.7083 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ca072bd-1c29-3cc9-9c90-caa10e6bad98 | -20.55846 | -54.6564 | 2025-10-24 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 065f1cdf-5df2-38ba-b854-1a0e4f1c587f | -20.56188 | -54.65705 | 2025-10-24 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4449a8f7-caab-3275-b8a7-fd4dce37b12e | -18.34692 | -51.69571 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2d6d143-54eb-3d8f-82e6-5b0341fd766b | -20.49766 | -54.60052 | 2025-10-24 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51adf245-cf80-3386-9eef-1772c7ee31bb | -21.13096 | -45.73158 | 2025-10-24 04:42:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ab0b1f0b-cdbf-35c5-8789-4e25527993c1 | -24.12265 | -50.76717 | 2025-10-24 04:42:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 13626131-a694-3996-8698-154fe5613274 | -19.89062 | -46.95979 | 2025-10-24 04:42:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb9cec00-ffa8-314e-9fea-6b27ba9bbf29 | -17.9339 | -52.69284 | 2025-10-24 04:42:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 569594d3-df50-369c-ae1c-b4234617c818 | -22.28279 | -46.83209 | 2025-10-24 04:42:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a9c55d6d-90df-32fd-8d5e-fa62220e5ae5 | -20.65162 | -55.08334 | 2025-10-24 04:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a2434a2-f1eb-3456-bac6-b665690bb879 | -19.44785 | -49.32859 | 2025-10-24 04:42:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a73cec63-2ddf-3a3d-b3eb-dba1fac90200 | -21.12419 | -45.73289 | 2025-10-24 04:42:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 651aa369-9bb4-3b6d-acd0-37dda89ef548 | -19.41547 | -44.34383 | 2025-10-24 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d336ba4-22be-3c66-8e5d-8f796bc0692a | -23.38684 | -51.98908 | 2025-10-24 04:42:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 58f00a4e-b0b7-39ce-b264-2926676edc06 | -22.89245 | -47.74904 | 2025-10-24 04:42:00 | NOAA-20 | SALTINHO | SÃO PAULO | Brasil | 3545159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0c7ebb11-bdd8-3b33-bd43-7eb1831c79d2 | -21.6165 | -45.41719 | 2025-10-24 04:42:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 38feb423-2cd6-3d21-a35f-0e81f1aed22d | -18.91538 | -47.18221 | 2025-10-24 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58f950e9-19d5-392e-89f7-75314c9483e9 | -22.89293 | -47.74517 | 2025-10-24 04:42:00 | NOAA-20 | SALTINHO | SÃO PAULO | Brasil | 3545159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a776a92f-e5c9-31f4-87e2-7949094b09bf | -22.9773 | -47.40093 | 2025-10-24 04:42:00 | NOAA-20 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4e093e94-ce18-37d9-8632-13faf84c8a05 | -21.20088 | -48.6975 | 2025-10-24 04:42:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9e41dfb2-b6d7-33d9-b1bc-f299f59004bf | -18.36292 | -51.70217 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef82bdcb-9d59-3220-b2bf-5855b7bf13b8 | -20.92466 | -55.77467 | 2025-10-24 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa72bd1f-9723-3ce1-bde6-b10e7592b899 | -20.44043 | -46.59143 | 2025-10-24 04:42:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f09d3026-e49a-3726-b95b-377ad36cf10b | -23.34753 | -50.40685 | 2025-10-24 04:42:00 | NOAA-20 | RIBEIRÃO DO PINHAL | PARANÁ | Brasil | 4121901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b005952d-821b-339e-a8a7-216adfd573eb | -18.91638 | -47.21944 | 2025-10-24 04:42:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94f0dc77-0c81-3478-b91b-a24d5272dc28 | -23.34513 | -47.16722 | 2025-10-24 04:42:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 987a0352-4240-3064-ba6f-1134d837b77d | -24.18654 | -51.68668 | 2025-10-24 04:42:00 | NOAA-20 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a754bf63-e565-3147-9581-5a5913443ec1 | -23.17275 | -46.72493 | 2025-10-24 04:42:00 | NOAA-20 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb4299b3-9ddd-36ff-9e8d-a4c56fa00489 | -18.36066 | -51.71667 | 2025-10-24 04:42:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2295fd28-dd64-3cbe-91d8-e1a86044e7ce | -21.61596 | -45.42212 | 2025-10-24 04:42:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b45fd3e9-73f4-3c6c-9ac5-61ffdc0122b6 | -23.43127 | -53.35829 | 2025-10-24 04:42:00 | NOAA-20 | IVATÉ | PARANÁ | Brasil | 4111555 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| abaf1ded-feb9-3081-b50d-5974ffa5027c | -18.60426 | -51.78733 | 2025-10-24 04:42:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0164fb5a-ab5c-3703-8614-c8b5ec2eff45 | -20.90724 | -49.42568 | 2025-10-24 04:42:00 | NOAA-20 | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 500fa1f6-601f-30c2-9840-ae1ba678904f | -27.15616 | -51.28905 | 2025-10-24 04:44:00 | NOAA-20 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d81812e6-3fe1-3663-a2c8-8455311df4d0 | -28.22503 | -50.36111 | 2025-10-24 04:44:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4d6202a1-514f-366f-ae28-1b56a17870e3 | -24.76881 | -50.96563 | 2025-10-24 04:44:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |


[Clique aqui para ver as próximas entradas](README51.md)
