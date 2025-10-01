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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e229012d-912a-3323-95e8-a73b4cb86741 | -15.93119 | -48.13594 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57c90c3b-abc0-3212-a92a-0b674914f3fa | -10.08787 | -50.19866 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| da4ff6d1-ca1f-33ce-b8f7-33812118fcfc | -16.40417 | -47.06249 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e94344c-25f8-3c61-8f71-22d858015d7e | -15.33955 | -46.27363 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e9bc9b45-72d6-34a9-af32-79f1bb626dde | -14.51766 | -48.37455 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a6245d63-ebbf-35b9-8d25-4b889abff151 | -11.39402 | -44.89444 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4716b658-72d7-3079-9f2e-5d85c23d84a4 | -11.45339 | -45.02136 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68c674a2-4f5f-37f5-beb5-eea8d97e5d36 | -13.37401 | -48.15758 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bb2526a-0882-3a14-bf5b-50dd649cfe2b | -9.92715 | -43.69126 | 2025-10-01 04:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2924995-dcfa-32db-a793-0d89c68e289b | -10.66647 | -48.53223 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b8a1f17-187e-3187-b95e-7a34dad7858e | -15.26467 | -49.25955 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa2905b7-0945-3c35-96ed-b9a18e25d7ba | -12.88808 | -45.26876 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24de1711-ca4b-3fdc-9b59-b89ecadb4a21 | -13.03433 | -48.67252 | 2025-10-01 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f464aa0c-2e02-37dc-85a0-7b6cf0c5c969 | -11.47529 | -45.09086 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5f08983-1408-3238-bc2f-85e25d2f1da9 | -14.72898 | -45.21603 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99a12328-33ae-3b72-a2eb-09fc005a5ff2 | -14.70765 | -48.12212 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a674eb60-e77e-345a-a646-fa4996853a4b | -10.03828 | -50.40995 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4d40ac3-d8b8-30b5-a470-f371ed467792 | -12.45111 | -50.20818 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f6e2600-a0de-31a4-948f-c6704478d4d2 | -15.2911 | -48.01636 | 2025-10-01 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc4fa73e-bf61-3d51-9c39-f844651475cd | -14.50603 | -48.4886 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2dea092-0dcc-31ce-85b6-144dbeeab01a | -14.68892 | -48.23024 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 037c626d-03a9-342d-9e5e-abef67df4f46 | -11.06202 | -47.83714 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9843855a-9932-372a-af53-0b179021ebbc | -13.46129 | -44.37646 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 377e9444-1165-3a09-baba-35c22af61b3b | -10.7735 | -45.36926 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6c2631a-ff71-3800-8027-abc3c8e42855 | -12.24594 | -47.79445 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75e0f80a-9a19-390c-8b85-0d8fdf302587 | -11.39416 | -55.086 | 2025-10-01 04:51:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e55f23a-b6a1-37a2-88e1-9297efdce3c4 | -15.17988 | -46.40008 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76af6ce8-0b34-3dac-b294-a65269d24416 | -12.80071 | -46.89689 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7890451e-9549-3139-b845-00be14469c56 | -13.32828 | -47.82222 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6dba1885-c6a4-3bac-bfa2-8e554f2330c9 | -9.41408 | -63.21136 | 2025-10-01 04:51:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 381278b1-ade1-3e22-8818-5ad9c1cdd843 | -12.91843 | -47.1668 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa417ee9-d42e-3bd4-8c09-5b5f14b77048 | -15.31362 | -46.40184 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4eb83836-620b-3eba-8d1b-124d6ee3b5be | -12.46678 | -50.22254 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7da0227-31fe-3950-b1e1-95c550e93f45 | -14.34949 | -45.91904 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cc2fa668-ee91-30f5-a905-edcac3f6ed7f | -13.32906 | -47.33391 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c48bc7b0-d386-3ea9-a002-de1db5e71118 | -11.8278 | -44.95366 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ef6ae00-4c1d-3f1f-9550-a0eb1c05c11a | -11.46702 | -45.00922 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac211409-6d36-3fc2-8f27-10da12c1ed7a | -11.76086 | -46.87541 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7652f34b-b53d-3ca3-abb1-e5ffb81f7f42 | -16.38233 | -47.05956 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60ba368a-f1d3-3ce4-90ba-0cb95385b0c3 | -10.90219 | -46.56603 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 165e5f45-6b5f-34db-9846-537a21879d98 | -14.51196 | -48.47589 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 95612211-c687-3c52-8dd1-38bd7113956f | -15.78026 | -43.68777 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd6f1ee3-7e64-350d-ab9e-fe32bd013a19 | -15.77907 | -43.69842 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e60ad7b-995a-3224-99d0-710ff3ac63d7 | -14.59889 | -48.21926 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d2f2cef3-4191-3e79-a3d9-bf67f360daf8 | -12.85119 | -46.87166 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c8aaf9a-1f65-3640-8b64-e58b86e1afa9 | -15.8181 | -41.89445 | 2025-10-01 04:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26480379-59fc-3cce-87d1-3e56bc80ca0f | -14.72337 | -48.15561 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 594a395c-053a-3b93-bddb-9499e43d83f4 | -11.5109 | -43.53869 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8f79d24-1b7a-3887-bb83-17b8d2819ba2 | -14.50992 | -48.4892 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5a2cdc5-4d31-39d7-b2d6-1b85e237b5b5 | -13.73163 | -48.69014 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4db1b4ac-547d-329b-bb30-31302e0c840b | -11.94297 | -47.08134 | 2025-10-01 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f30803a2-4234-3667-97d9-2aec237655e6 | -12.80135 | -46.89194 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 353fa7e4-f981-3f0f-9d8a-1d5671fcbb8f | -14.21488 | -46.09927 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad8eed60-c24f-3339-9450-cb5fb5a1b125 | -13.31242 | -47.20824 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a623d123-468e-3ec9-87bb-535dd9f22377 | -14.70116 | -48.2587 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a479d46-2b15-3c99-a9ab-1607581b2f80 | -10.6256 | -48.59089 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dce3cc86-af14-3198-a4c3-193811566dcd | -13.13577 | -47.42016 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 805369df-cc2a-34b1-9879-998a5e5e5315 | -14.68685 | -48.24544 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 545262a5-887f-3c02-aa42-b970ea3beb23 | -9.21645 | -50.69108 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff44919a-1d18-398f-ac3c-703e545813f0 | -15.48583 | -45.91516 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e95c334-a2b3-3b16-bbf4-441fd81c6c6c | -11.47397 | -45.10078 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2450148-ccca-3b2a-affd-82587f6f9629 | -14.8967 | -48.13158 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bcf2b10c-fa60-3ce4-96c4-3f3f5a73e69f | -11.63032 | -47.49574 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c19c3970-0ed9-3a58-ae38-d8d17609324d | -13.76524 | -47.97416 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 043ae5a8-a963-33d3-84ee-c3644343991d | -14.09435 | -49.74463 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc4509dd-979e-3f64-b891-ad3a16e1e424 | -14.67875 | -46.95776 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9249b99-dc3c-3918-ab0d-f0bdebee2d4a | -12.82736 | -46.98424 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f806d6b6-a492-3d6a-8247-1801aa40476b | -16.37803 | -47.05844 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fbe25467-538e-39f3-838d-e3ae450398ff | -14.0291 | -53.88306 | 2025-10-01 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e442f684-b3cf-3c08-990a-43480454d544 | -13.3662 | -48.15645 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 445c94e0-2787-3894-a973-c8cb0a1222cb | -13.67009 | -48.06281 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4d78ee2-349b-3b62-b5cd-5a1bce852d67 | -10.47828 | -55.61736 | 2025-10-01 04:51:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4971ff26-0ef1-3753-a4ea-cdc0bd76d827 | -12.85174 | -46.8676 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc125f42-57f9-3c8d-9916-694096cb3706 | -10.73936 | -45.37234 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fea758d1-20e5-340c-97e5-fb305b8de2a0 | -12.16014 | -47.89952 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a7c662f-fdb5-3041-91b9-efe39a35544a | -10.93219 | -46.50636 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5551f5a3-5287-3d13-bfcf-4a0b6a035c7a | -16.40969 | -47.0543 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8dcff15d-001d-3485-8f25-8e342d9b2174 | -11.06011 | -47.82267 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12506544-d72e-3c5b-88d8-dbe84264cecb | -11.16597 | -54.11937 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 958ea9e1-a5fe-323a-899e-41802c6ea356 | -11.80123 | -46.61162 | 2025-10-01 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2cced56-cf60-3a9a-8cce-2cd10709a2c4 | -13.78692 | -51.21782 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94fc5b55-ba50-3607-894a-6435d2a0a27f | -13.31191 | -47.21207 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51c73923-81de-3e1e-aae3-bf86439dbd56 | -12.76965 | -50.55101 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92866cff-5929-33e6-a0cb-9944af26cf52 | -9.42115 | -54.71194 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a272675a-59ae-3795-8648-691ae507248a | -14.91353 | -51.67324 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 59c0bd8f-baf3-30d4-a97d-25017b5915b4 | -13.36997 | -48.15882 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27f111ea-a63d-39eb-9252-477e670af3c0 | -15.25766 | -49.25578 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2691d664-4084-3e66-8e1a-49b70488d3bf | -13.31091 | -47.21956 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51c13921-f648-318a-9646-ce6208c7a470 | -11.83461 | -44.97479 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c562405e-e313-34e3-b404-e1a6ea100516 | -14.98674 | -50.76522 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a5332a2-eb84-38f6-a43e-a9fa4de44c7b | -14.02702 | -46.3206 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a22c4ba8-fed1-3ed2-8657-95c2e73d2712 | -14.7202 | -48.26668 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a629cd33-8f3f-3bf1-ad1d-21d33d9c9835 | -15.00686 | -46.97083 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ffaf346-f72d-3295-9982-03ac1745a3cc | -12.01267 | -46.63343 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b99e81c7-6a82-32ff-92fe-1131073a234f | -9.32809 | -45.69176 | 2025-10-01 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6be290e2-1434-31f9-97ab-92f2dd8f8ecc | -14.19335 | -46.12412 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bdee675a-1eb7-3d97-947c-930e0052b4d4 | -11.83441 | -48.05811 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f002e59b-3ab7-3932-b416-faf404026c6e | -14.43629 | -46.35814 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04c7c95c-36af-3b37-93e0-b30ac3ae1cfb | -15.4403 | -43.64577 | 2025-10-01 04:51:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 099599b7-0cdc-3cfb-94d3-9af6bb01e54f | -14.6983 | -48.13115 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README90.md)
