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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0a40176-a38c-3c7b-90aa-93d75ca8037d | -17.08827 | -43.38095 | 2025-10-07 04:38:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77d402b8-45de-35fb-ba8a-b5fd82fec65b | -14.50762 | -46.92031 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 640e443d-24ae-3d93-817c-0429d07490df | -14.90257 | -48.09347 | 2025-10-07 04:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3bccbc4-14b1-3270-be73-55a223dae1c3 | -10.42651 | -50.32658 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5820d31b-5122-3e89-8118-aecb01331646 | -13.22176 | -48.46292 | 2025-10-07 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd620386-f230-30e5-aed2-79152bcb3281 | -9.62223 | -54.31894 | 2025-10-07 04:38:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b112f525-2209-3829-8b9d-306c188a5542 | -14.66831 | -48.39729 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c4a7118-aa01-3c08-8170-77641e0528a6 | -10.88423 | -51.03131 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 083c4f23-0b92-3b0d-ad85-48c83d900287 | -13.63668 | -48.70963 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38a79155-7c77-3fc2-ad2f-7b8f89767f01 | -14.93166 | -51.42886 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f386dcc2-86fb-314f-8646-0609215888c2 | -11.12304 | -47.21141 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87eea20c-295e-3a45-a943-79e88336b627 | -10.45309 | -48.36063 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74cfb5f2-6545-38fb-a75e-c27203bea3a3 | -9.51758 | -54.73408 | 2025-10-07 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad6dbaed-fa0c-39a4-99f2-aecee8d98a04 | -15.99564 | -50.83862 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09f95dc0-6b7d-38f9-9740-b0e48d12a569 | -14.73284 | -46.01716 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2f1d7e70-33f2-3978-9b72-adea65a06e97 | -14.76898 | -46.03191 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a9bccdfa-f2af-3c20-b028-85770cbe1d44 | -9.61869 | -54.31443 | 2025-10-07 04:38:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9038b96d-fd0b-334a-ab24-19c66593036d | -12.98306 | -46.78056 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93c14520-bda3-3f40-9b8f-4dd0241620b4 | -10.5515 | -54.8692 | 2025-10-07 04:38:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4de2779-62fc-37e1-a445-98be3bcb0831 | -14.52486 | -46.92717 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5d851b9-a88b-370b-bc3c-da212a022ddd | -14.91995 | -46.82073 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 400fc466-af3b-39d0-a596-f77c183d8b3a | -16.01935 | -51.04045 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f809c90d-ea3e-3aec-81be-ca8bc3fd4a87 | -9.63431 | -57.02114 | 2025-10-07 04:38:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42a624f7-bed7-3915-b58b-18179269cc0c | -12.89349 | -54.75077 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 65ee789a-4617-35ac-a88a-abea1a5bfdce | -11.79113 | -45.1051 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebb77ca1-9605-3006-8bf0-c34b95f9c5d8 | -13.67593 | -47.95396 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8a90237-d605-34e6-b57f-42d9f803a3c6 | -14.63133 | -52.49734 | 2025-10-07 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e0de2b6-eb6c-3431-bf01-3b45578f631b | -14.94468 | -51.47741 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5daec65-c005-39b7-a1d7-37b8ae9abe4a | -15.27813 | -46.3414 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1934b3ff-88e5-35d5-b7d9-8e85d25542fc | -11.24232 | -47.91197 | 2025-10-07 04:38:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5e0fa11-be37-36e5-93c8-8c82cd08417a | -15.97441 | -50.84246 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ae4bb81-caca-3106-a89d-8d57eeb37406 | -11.03839 | -50.91577 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c445820a-d869-3e73-afb2-825acb276ea9 | -14.72662 | -46.00697 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 61f91514-c5fe-37ba-8224-5a3384992615 | -15.03312 | -56.03347 | 2025-10-07 04:38:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc2e4430-dfb9-3ee9-ab7c-483393de4971 | -14.28838 | -45.84047 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1dfe642-2b1f-303f-896f-5f075b0d8d7b | -10.88769 | -51.0319 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 4efe0876-aa0f-351c-85fa-9977812850cb | -10.30173 | -50.40454 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd978902-9b42-32ae-9c31-21bf1e044898 | -12.45599 | -45.53569 | 2025-10-07 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 105ea7da-4cca-34c3-bf0d-0705aca03320 | -10.15213 | -53.71931 | 2025-10-07 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 454777ed-b887-35aa-b693-154333983f82 | -16.11136 | -48.94291 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37f03c7e-8348-31b4-a309-f23a354296da | -14.71932 | -48.35982 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00ae417c-5d04-31be-8b1f-78188c4b8930 | -14.70294 | -48.37626 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 402c1e29-06ec-397a-a0ff-0854068c22f7 | -10.4473 | -50.34888 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4bb90d18-799c-3063-83f9-cee6a591f423 | -15.21885 | -56.76605 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 183a1847-8adc-386d-a0d6-03ec2cc063bd | -10.8105 | -48.60129 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d942168f-77d1-3cd2-abb0-23e4d553276a | -11.86799 | -44.94017 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1fcb143-7fad-38f0-a4d9-a5205724a51f | -17.95999 | -44.40974 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66afed63-76a8-37d1-8cf7-fa0e2efcd143 | -15.49834 | -46.82653 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9eb479c5-c569-3ce7-bb45-82ff36bbc266 | -15.76406 | -47.77134 | 2025-10-07 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2ba198b-1077-3b37-807a-b70d4df4fc48 | -15.29122 | -46.32923 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8c704c8-1df4-3db4-9285-e4e3e7b9f39b | -15.6239 | -52.54434 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bdd4ed7-ddc2-3ea3-8760-8f19bb6c36d5 | -17.34915 | -46.83614 | 2025-10-07 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 783b7cbd-550b-30d6-b4d7-422d4e4ab020 | -11.95437 | -45.49042 | 2025-10-07 04:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab9125d5-ec45-3c9e-aff6-0a6fdb3c6fee | -10.42591 | -50.33024 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71d42bb7-a2df-3702-9bb0-bf9d5d9c12fd | -12.90369 | -54.74113 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0666841-2ce3-3944-ac5b-c6c37bef02ec | -11.15512 | -47.93172 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8194fb37-a6e4-3903-b418-600040ddd397 | -13.25737 | -46.47119 | 2025-10-07 04:38:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 410d1ff6-d095-3d0e-87fb-15ef7caa6814 | -11.15078 | -54.87624 | 2025-10-07 04:38:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2766329-149d-39b4-bb5f-5df2038ca04b | -10.81003 | -48.82113 | 2025-10-07 04:38:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0f0c2dd-bea5-3b3d-ac75-4af979e1a7bf | -14.7176 | -48.34813 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a2dbdb1-9a54-3086-8183-e29033b99ded | -17.35285 | -46.83666 | 2025-10-07 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 52.3 |
| d4ad0dcd-6186-3fa4-b9f1-63c27e19d73c | -14.92793 | -51.40897 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93c3e2ef-3d26-3e42-bc23-1b7e2f9ba48d | -11.79697 | -45.09159 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1334b92a-75f3-3363-929f-ec427eb65418 | -15.26735 | -48.05372 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea01ad2f-d98e-3d1c-ace8-5411b2cab8d9 | -14.50048 | -46.91922 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40db8dea-9bc0-3f0e-914a-ee6ae67c5d12 | -13.27988 | -48.47586 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e1b5a4f-f36a-39fc-88c7-0bc50347fabf | -17.98081 | -44.99149 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 485fca60-3320-32b3-bfec-b1ecc7d24f69 | -13.37026 | -47.24931 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d0fa686-dc6d-39ff-8cd7-0dfce249dd47 | -13.08743 | -47.86039 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4346b24-b302-3b53-bbf3-6066d30791a1 | -13.34106 | -47.56428 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9d2f1f7-a938-34ad-aa23-53f8fac4c601 | -15.61068 | -52.55852 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b649d3c4-8c8f-3843-8f83-e177a56333c5 | -10.3786 | -50.29979 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 666a4c8e-6632-3efb-9f69-3f19cd2cdd7b | -14.75891 | -46.04906 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4a4fdceb-fe40-3177-b03d-f889dba4bf07 | -11.78401 | -45.12753 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be5351a2-53b7-33f8-80c1-6c1898a3301f | -12.16488 | -51.43794 | 2025-10-07 04:38:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 617b7eb5-4ca7-3ef8-bc99-97abd40c311b | -13.64002 | -48.71019 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc7ec6c2-6761-3f32-8fde-c649518a2b67 | -16.31796 | -47.91312 | 2025-10-07 04:38:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e9c40c4-8e42-324d-8e6b-b7e8c2a920aa | -13.05446 | -47.89418 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 680962a0-b396-38ae-8e57-ba6551fdd746 | -13.26814 | -48.4851 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a55085d4-258c-3086-8e2f-4ed1d67fcc7b | -12.91927 | -54.72496 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75e4dd4c-bc93-3c16-9b93-063ac4d6a5ae | -14.75518 | -46.04845 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62f5d316-2289-3ed3-b34c-221f2b7d6370 | -11.5063 | -54.4538 | 2025-10-07 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9efdc19-cfde-3830-aeff-8abb4f81f0b1 | -14.49988 | -46.92336 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b90f7e5-f8c4-3c17-836b-f6c339dfcce0 | -11.85073 | -45.06257 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d34215e-70ae-3920-83f0-4d259d9b4cca | -13.27418 | -47.57351 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8922ea31-ae02-3819-b917-551e3820fb45 | -12.93904 | -54.73249 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73be8a51-e5ba-3a96-a8b6-7ade02b2b509 | -11.93875 | -46.45096 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54114650-ea5d-3fa8-aaa0-f10fd3dcbbf3 | -14.90758 | -46.84931 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6f82611-7d31-32ba-b22d-0c0d8f36f8c1 | -10.35886 | -57.82712 | 2025-10-07 04:38:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae6f27fb-bb70-3987-a557-a49ed35905c8 | -13.53799 | -42.99474 | 2025-10-07 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 71f61820-1306-3c8a-8eac-7a6fd37aac74 | -14.76946 | -46.05539 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 433e89c6-8eb4-3fcb-89a9-cf6e73c16095 | -10.7883 | -48.59048 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5185afdf-2a3b-3603-978e-77c883217390 | -11.94538 | -46.43105 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b19d68c-98ad-36e9-aa25-40fa5c9115fd | -15.22266 | -49.30767 | 2025-10-07 04:38:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b38de44c-a7bf-3eaf-ba4b-81c372516e1d | -15.5864 | -47.26408 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c1b215f-dbf4-35f8-8f4f-cff0fc8bdf84 | -12.98543 | -46.78443 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e48c41f-d4b0-39fa-9055-561fa829c6c5 | -13.27663 | -48.05989 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b9f734c-965d-3135-b7f2-63449ab0d294 | -17.56249 | -46.07178 | 2025-10-07 04:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c809cf90-25e8-314c-904c-d6c97b5daa4b | -12.18716 | -47.77474 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af44ff2c-b0a6-3393-91da-82d5a41aa064 | -13.24896 | -48.05919 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README65.md)
