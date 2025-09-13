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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6df7cc77-b164-3dcc-9ffc-b96dfce406c9 | -20.29054 | -46.59345 | 2025-09-13 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b0c99500-2db8-39ca-b12f-2f3baea21575 | -14.19409 | -46.25853 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 351297f6-cd10-3a38-ac01-4289154f1582 | -17.40703 | -48.22019 | 2025-09-13 03:47:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98b4578d-2e50-3be8-89a7-9c2704b66552 | -12.8483 | -47.95077 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8a0c69c9-19f1-3760-9df5-0454ac6d8454 | -12.937 | -47.97755 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8e0bbe1-4c4f-3346-8439-7389c185768f | -11.83124 | -50.57954 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12d0b414-0982-3df4-a031-0dc26e0cb4cb | -13.08718 | -48.26358 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 65234493-492d-32d9-8d89-6f374e4b2da8 | -17.5467 | -44.54873 | 2025-09-13 03:47:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79fb0002-1cf6-3953-8f48-cfc9e757347f | -17.28429 | -46.11502 | 2025-09-13 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 5ef3e88f-505c-3218-a5a9-49ae8a51f3bd | -14.1921 | -46.2686 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 02cd7724-094d-35e3-bf12-5cd75cda1193 | -10.76728 | -50.52475 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4bec79d1-7849-3d7a-b929-296a69e68d83 | -9.05756 | -47.03519 | 2025-09-13 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ea153f7-f889-3735-b4cf-bd1716980372 | -19.25744 | -51.43188 | 2025-09-13 03:47:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74b1f9b1-0b94-312f-aa62-46d20de78eb5 | -11.73807 | -44.20962 | 2025-09-13 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87437e3b-0419-31e8-a3de-56dda63eb0e4 | -11.71589 | -46.56382 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c07961c-c61f-3017-8b89-032af2873863 | -14.21873 | -46.27319 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d11c53c1-ca4e-3d35-af88-2e4c90e1ad8f | -17.28833 | -47.24525 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e134c5a-3b0b-31a4-80fe-4d0fa20303f4 | -11.83835 | -50.58114 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 843acf56-d819-3599-b807-709db66899a7 | -11.41953 | -50.75427 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5822163-2f7e-35da-99c9-0a3dbbcecaf4 | -20.09013 | -46.91116 | 2025-09-13 03:47:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41e5c0d8-1ac1-3d84-9656-2bba115a37f3 | -11.81302 | -50.56055 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9c808557-94a8-37ed-956e-288cbad0f1cf | -17.41061 | -48.22273 | 2025-09-13 03:47:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff2defda-f87e-3071-909f-02ca303fb4f7 | -14.21941 | -46.2979 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 03730467-a5ab-3f87-b48d-5a135d0a6e5c | -16.64418 | -49.757 | 2025-09-13 03:47:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b70f62c9-3925-3eb6-988a-99d4a63f99cb | -17.2864 | -46.10192 | 2025-09-13 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 1a7b786d-fe9b-3338-a612-862da19ddfe1 | -11.93311 | -44.29486 | 2025-09-13 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a01815d6-b9e6-3a1b-98dc-5a8d97a9af21 | -11.84767 | -50.59483 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2a9ac40a-3e05-32a8-a967-ad0d5500c97b | -12.12809 | -44.84298 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 19ab9c75-99ed-3084-88f4-a1d2bb69370e | -10.78701 | -50.54437 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 31a38557-bb82-3db9-931f-2e21f6fe6313 | -17.55026 | -44.55425 | 2025-09-13 03:47:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77761066-1841-3845-b570-50c2223e2134 | -10.7083 | -48.61221 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ed61827-38a5-3a95-9903-a6e79a4880cd | -17.41155 | -49.24543 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0101e7d6-f299-3910-ad4a-d37fb0f2dee7 | -17.29271 | -47.23662 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d614f6f-3e01-3c39-8e39-ab35e40a3411 | -11.33434 | -50.79784 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f965a600-b5f6-3141-b05f-802a0ebf3b6d | -8.08144 | -42.55841 | 2025-09-13 03:47:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a57cd589-c6ed-3dbd-8225-74df29f010a6 | -11.82225 | -50.57404 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4241afaf-4916-34dd-9f73-077d9cdd3501 | -13.29154 | -43.77953 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46cc905a-e8fd-3b6f-b09b-695a522aa583 | -17.8313 | -50.41281 | 2025-09-13 03:47:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f888488e-d9d2-3d95-8246-de79d07591de | -13.4804 | -48.44914 | 2025-09-13 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1405e87-d5e6-3c23-8061-cebce441e5e1 | -18.15443 | -49.18787 | 2025-09-13 03:47:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 5b28a6ac-7cff-3683-8d71-ec0cd61cbbe3 | -11.45675 | -43.58076 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac91a2a2-ef5d-3b7e-ba8c-8344e194ab6e | -18.45073 | -47.19733 | 2025-09-13 03:47:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7fdee6d-77d1-3009-927e-0444cf96a96a | -13.26765 | -43.75515 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a360a8a4-e009-39f7-b08e-abcd290bb081 | -11.82012 | -50.56214 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f723b6ce-9c58-3e8a-9a17-4fbb2a0e6cb6 | -12.12205 | -44.84333 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1190ff59-6085-3c3c-9fc4-7efef450cf9e | -14.21985 | -43.51039 | 2025-09-13 03:47:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcc8ce41-a875-3ddb-b559-52ba4f48cca4 | -14.22334 | -46.30605 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 171af20a-5a21-3db3-995f-652d144d55e5 | -20.60164 | -44.91064 | 2025-09-13 03:47:00 | NPP-375D | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3b69b1f3-692b-3977-9942-0c4be99d84f0 | -14.17806 | -46.25615 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62899faf-1bb9-3534-93a7-21a067d22947 | -17.28903 | -47.25411 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b88b30f-fc84-3644-a381-219e95732375 | -14.18213 | -46.23558 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 70057bce-52ed-3c3d-ab60-e0050a7834da | -17.27941 | -46.11363 | 2025-09-13 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7ce072b5-417f-3a7e-8ec8-d19f5607af22 | -10.77731 | -44.77979 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbe1567f-caa2-3ace-803a-62b25619b120 | -17.12215 | -48.48591 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a695fc3e-c928-3d64-b5e8-203a8723a187 | -8.09599 | -44.51522 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27d3fd4e-39a3-3e4e-83a2-8d84b023cc44 | -17.23639 | -50.236 | 2025-09-13 03:47:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5d1dab9-32cf-37db-be77-bce82688442e | -13.00805 | -44.11978 | 2025-09-13 03:47:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb679e25-5df3-3ac2-a115-8fac9eaeb2b7 | -17.29049 | -47.24717 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 113e423e-9439-3c0f-a24a-0ce3f098cc45 | -8.32766 | -38.0945 | 2025-09-13 03:47:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aac3a157-e314-3c18-bf6a-0f78c0c83ba3 | -17.30096 | -48.73559 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 65a3f017-b1a1-37ea-9346-4f979a07e0f2 | -11.85214 | -50.57343 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8ebdd6d2-70e8-30c8-baf2-8f35721717c8 | -14.22207 | -46.28429 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 3004b18f-10f8-3958-8d56-ca32cbd0c630 | -9.96849 | -50.30758 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ec982ee4-803b-3768-a347-49ed91b76288 | -20.01555 | -47.64683 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26b750df-0bab-3ebd-bf49-43f7f8d7fd50 | -7.77511 | -43.94036 | 2025-09-13 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9bc74cd-b7e3-35c7-9ba8-ff5175feb959 | -17.40619 | -48.22412 | 2025-09-13 03:47:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e678892-28a2-3c57-b0a0-d10d2426fe3d | -13.40456 | -46.80126 | 2025-09-13 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2234db6c-177e-3573-a6b1-6d291f0e6e38 | -14.19604 | -46.27654 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1b962166-9fc4-303f-b1a1-2eceea57734c | -11.73632 | -46.60912 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 280d2bb7-092b-3cb1-bf68-14611d7f0e4a | -10.3686 | -50.50801 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8bdf1ebf-f1a9-3dc3-9bb9-53d8bbe7b6af | -11.13998 | -50.70722 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9f1344d-16a6-3715-862c-9a364be424cd | -10.36021 | -45.3955 | 2025-09-13 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0120a49c-143e-3523-a350-5851a0749921 | -20.09018 | -46.93554 | 2025-09-13 03:47:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4775f9ae-323a-3515-9e86-b204ddb8a86b | -17.43423 | -49.22806 | 2025-09-13 03:47:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae008626-5b4c-342e-93f8-107fde17df90 | -16.65039 | -49.75863 | 2025-09-13 03:47:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 143f02fe-b1f0-3107-988a-b594aa8c223d | -19.63957 | -45.08381 | 2025-09-13 03:47:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 89f1cf6a-f403-3824-b98a-9ee7dd67ec70 | -13.91362 | -48.27777 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| db3d652a-f6c5-3cb4-9ca7-ef90cdd0d3e4 | -14.1288 | -45.37969 | 2025-09-13 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31b4aa8f-5269-3c10-ba78-742425303f5d | -10.7767 | -44.78303 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0018b77-a4a1-3912-b57c-ad430a362d59 | -11.43279 | -45.62444 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e93ded1e-b7f0-31a7-9bcf-e542caf01906 | -20.10501 | -46.91397 | 2025-09-13 03:47:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6e9282cd-ecca-32bc-8c96-e04e606550bc | -18.97333 | -48.60468 | 2025-09-13 03:47:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54c51a97-9fa7-32a9-87be-b60c1f3fd3dd | -18.77772 | -43.80168 | 2025-09-13 03:47:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a152d7b-61de-34e4-97a7-0513dc69be9b | -20.01669 | -47.64394 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4938327b-f8ed-3635-a0ef-2951fb08e1b9 | -17.95118 | -45.26896 | 2025-09-13 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 935bfbf7-49b7-30de-8843-52a78a07242f | -14.18735 | -46.23701 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3bf6b9aa-7b8b-3bec-802e-d2ff2d9200fb | -10.76751 | -41.33464 | 2025-09-13 03:47:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7e2696d2-d530-3dca-9454-d121d9703d0d | -13.13448 | -47.13023 | 2025-09-13 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1947eb3f-d472-3dd6-9a9d-10a40c3f8ff2 | -17.33069 | -46.66445 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2dd8a2e4-1ee3-312d-8d58-a14a75fb05dd | -8.09073 | -44.51424 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8afab8e9-3130-3506-8ee5-4a5e111e52b5 | -16.35355 | -51.54467 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd0bc99f-254e-3329-b88c-9bc30117fb17 | -11.86386 | -46.75521 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| be6afb7d-f9e7-3df6-9c2a-28de00b92c0b | -17.44243 | -49.24787 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5c809c4-f307-3ab2-9712-2cbbf7e1dd29 | -16.41109 | -49.24097 | 2025-09-13 03:47:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 879a846a-f8d0-34af-857f-6de53e925c5c | -17.95057 | -42.52629 | 2025-09-13 03:47:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5cb4a314-7679-36bd-a57b-b4eb70f6b6a2 | -11.85408 | -50.57722 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 09a63ad0-6b72-316f-8994-bdb8dab01932 | -14.2227 | -46.29889 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 56788b3a-2eea-3a9a-93aa-df2bfa027706 | -20.45001 | -46.44188 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1560fbe7-f9c1-329a-b810-5436df6d2a72 | -11.49115 | -43.69295 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45090c02-7903-36b6-b7cb-d5f30a08c76c | -17.23009 | -50.2343 | 2025-09-13 03:47:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
