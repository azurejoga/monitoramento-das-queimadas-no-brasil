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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fae803eb-ab14-36e4-9506-64f4a75d6b85 | -15.30068 | -56.16027 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7558e757-1d49-3d08-9254-60c1531ffd5e | -16.07464 | -47.94157 | 2025-08-24 05:01:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c592c970-0dec-3d02-accc-0c9b7ecd1832 | -9.02111 | -65.69621 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7cd9a5d2-7a1e-38b9-894a-2088195258fe | -23.35952 | -46.92828 | 2025-08-24 05:04:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b6ae6e3d-9e91-35d7-814d-2275bc42d75d | -21.4153 | -47.61026 | 2025-08-24 05:04:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 858a0cf3-566f-3059-8e60-07240880f6fb | -20.94332 | -46.83828 | 2025-08-24 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c04a70e-b8c8-3b23-a009-c190d2716db9 | -23.25584 | -46.63073 | 2025-08-24 05:04:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c81313eb-4c27-34b7-970f-3235f49b6a6f | -22.95357 | -45.12954 | 2025-08-24 05:04:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cafddf0d-5d84-357c-b728-cb32f8ae0b66 | -20.12208 | -45.36661 | 2025-08-24 05:04:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 94123d31-c278-31df-b836-a9dc1bd4a5a5 | -23.6317 | -50.55908 | 2025-08-24 05:04:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 86b77f8d-428d-3b2c-80bf-b32e2770397f | -20.34913 | -51.68514 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c241b56c-e8dc-3593-8a25-2d65dd4aef09 | -21.27123 | -43.75454 | 2025-08-24 05:04:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3fd269d4-67c8-39a3-91c6-a217eb4decfc | -21.31959 | -48.67232 | 2025-08-24 05:04:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d845c72-fb63-3d5c-b292-521b38bc0c13 | -23.28958 | -47.63447 | 2025-08-24 05:04:00 | NPP-375D | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a5537cc0-50dc-3bc3-9bda-8bbe992285cd | -21.27813 | -43.7551 | 2025-08-24 05:04:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a2b7ff19-87e4-3b54-b45e-52771229b951 | -23.25622 | -46.62608 | 2025-08-24 05:04:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cdde28b9-e183-35cb-8174-441b3fb9c2c7 | -22.00546 | -44.99709 | 2025-08-24 05:04:00 | NPP-375D | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f385754d-2bcb-36b6-ad05-d25f3496561e | -20.35645 | -51.69409 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 180028e5-68d1-3e1d-8f37-921c8f0786ce | -22.05067 | -53.8339 | 2025-08-24 05:04:00 | NPP-375D | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 088e132b-bdce-335a-b089-495fcc75695e | -20.59228 | -45.82063 | 2025-08-24 05:04:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14304b89-06d6-3a09-b382-3b668ccb929d | -19.72952 | -47.98336 | 2025-08-24 05:04:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da83070a-5c49-37d1-98a3-0ad87e939b43 | -19.72987 | -47.98002 | 2025-08-24 05:04:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd0c3c96-4b41-3d97-b3ba-dee584f19a88 | -23.36483 | -46.86494 | 2025-08-24 05:04:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4d0bde9e-8a9f-3f41-935c-5d016b1c7e14 | -22.54596 | -43.71473 | 2025-08-24 05:04:00 | NPP-375D | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ac8615d-d3bc-34cb-9840-d476381abbfd | -19.6328 | -43.18758 | 2025-08-24 05:04:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 51864609-0b23-3e57-843f-e5368ae71d81 | -23.84757 | -50.72382 | 2025-08-24 05:04:00 | NPP-375D | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9801c6e7-e182-378b-8e58-846e49b07648 | -22.94656 | -45.13193 | 2025-08-24 05:04:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5d2e3e83-8154-3b70-b69a-44cd8cfd0af1 | -20.36379 | -46.73269 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b6d09ed-7486-3958-8005-a2598eec0801 | -20.3616 | -51.68672 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87ed5a78-f34a-36dc-8b9b-d29b96412fc2 | -23.46874 | -46.81088 | 2025-08-24 05:04:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 576953d5-b14d-318b-bf81-dfe6b7e274f1 | -20.36209 | -51.68278 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82d07fdd-c682-3c52-9cf2-1419d15a0cfc | -25.14953 | -49.53632 | 2025-08-24 05:04:00 | NPP-375D | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5a05a25c-e558-378d-bee3-43e6a5de319f | -22.80425 | -43.6906 | 2025-08-24 05:04:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7144fb7e-2487-30cd-8293-adaf9b089899 | -23.25275 | -46.62739 | 2025-08-24 05:04:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6e81487-5e44-37f4-9f4a-d8cd7e9069ef | -20.3622 | -46.74915 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f600725-e821-3949-9374-09a63f48e571 | -22.61025 | -52.49806 | 2025-08-24 05:04:00 | NPP-375D | EUCLIDES DA CUNHA PAULISTA | SÃO PAULO | Brasil | 3515350 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1088b589-c7eb-3f2b-b492-7a4e71d62c7b | -20.94437 | -46.82772 | 2025-08-24 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a9cf071-fe57-3f2e-9b93-c0b2fa747fee | -19.94409 | -47.48782 | 2025-08-24 05:04:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e322fb9d-b790-3cd7-88cb-06aebe9b48a1 | -20.35802 | -46.73259 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45ddb1e5-b881-3ca0-be56-c64a08372d41 | -21.69797 | -46.90577 | 2025-08-24 05:04:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2f5369ab-888d-3414-bc0e-d10d82cbaa41 | -20.08291 | -46.1167 | 2025-08-24 05:04:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d8ffd4a4-bddb-3384-a573-5dd68f1fcec6 | -23.29259 | -47.63684 | 2025-08-24 05:04:00 | NPP-375D | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a0de14ce-c262-3693-b9d4-6db3a2478de5 | -20.07655 | -46.12066 | 2025-08-24 05:04:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82b48e20-93a8-3745-aaca-f189b86ea910 | -23.47011 | -46.81419 | 2025-08-24 05:04:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9e1aff41-69ad-3ec6-97ad-444accb254c3 | -23.50703 | -47.25599 | 2025-08-24 05:04:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 96d7e553-863f-3513-8b59-437eaaa4b310 | -20.36148 | -46.75649 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fecce5fd-16a0-32e6-bafe-6cfbfff27d9d | -20.36659 | -46.76335 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14d760ea-ee9f-31bb-a1f5-ab3c73dacc52 | -20.93789 | -46.83474 | 2025-08-24 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95a4782e-c6a8-3382-b908-6acb578d1ee6 | -19.93867 | -47.4871 | 2025-08-24 05:04:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fee9ed5-4066-35d0-a3e6-d30b5eaff3a8 | -23.28701 | -47.63607 | 2025-08-24 05:04:00 | NPP-375D | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 523560d8-b2cf-36d9-9621-1cd7cf8c69de | -20.35378 | -51.68172 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7e73fbb7-9011-36b0-af45-bd1b14140583 | -22.72516 | -46.98054 | 2025-08-24 05:04:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3b36007a-d3b2-3a31-843c-980af8758f99 | -20.35694 | -51.69014 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 0fe1b761-a405-3c43-a9da-82cc11c7e56a | -22.903 | -47.72228 | 2025-08-24 05:04:00 | NPP-375D | SALTINHO | SÃO PAULO | Brasil | 3545159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6d7f0cd-8473-3a2a-8c7f-5be23cbae222 | -23.32442 | -47.84288 | 2025-08-24 05:04:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| a2060cbb-ff12-3287-be1f-87f5d12c66ad | -22.1418 | -43.66081 | 2025-08-24 05:04:00 | NPP-375D | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 0c7b10da-dd95-387e-bf34-1c5edefebb14 | -22.05169 | -53.83201 | 2025-08-24 05:04:00 | NPP-375D | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6cb4aa5b-8e5f-374a-874b-98bc62368e85 | -23.32957 | -47.84743 | 2025-08-24 05:04:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| d6873b4b-20f2-3eaf-95c8-f1cac1090503 | -23.37107 | -46.86112 | 2025-08-24 05:04:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 777153ad-f4d5-38c1-9dab-115e8fc1ad36 | -22.84429 | -46.29366 | 2025-08-24 05:04:00 | NPP-375D | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f35afabe-ad82-3b06-b16f-2a1167eba953 | -20.35793 | -51.68225 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c9f76e3d-78f5-3bcb-a27d-fd3e554321b3 | -23.4705 | -46.80986 | 2025-08-24 05:04:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4cb5a61f-2009-3a98-a007-36519346c461 | -22.54636 | -43.70869 | 2025-08-24 05:04:00 | NPP-375D | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 37894e5b-395a-39c0-ac9a-f9f31c09adf1 | -22.22298 | -45.69422 | 2025-08-24 05:04:00 | NPP-375D | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cf0c1769-ccbe-3f5e-afd4-4cbbfcb8f258 | -23.6311 | -50.56441 | 2025-08-24 05:04:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 312222e6-7504-3435-8e0f-e1b232c10cda | -19.69031 | -48.98645 | 2025-08-24 05:04:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d80afb53-5931-3a5b-975f-ed14944bcd6e | -20.08248 | -46.12131 | 2025-08-24 05:04:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0631c7f-0291-374f-9f0d-1841b32290ac | -20.59836 | -45.82116 | 2025-08-24 05:04:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5d2f57ec-498a-3fc8-bfa0-d486e80ff650 | -23.31288 | -45.53227 | 2025-08-24 05:04:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 444d2d1a-aa9c-34ee-8359-ba1aaf1a719e | -23.25871 | -46.62785 | 2025-08-24 05:04:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b174b8a-9a9a-3333-afb2-0484173aefb5 | -20.36918 | -46.7368 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a27a7719-d142-3c7b-afaa-f39671634a35 | -21.27061 | -43.7529 | 2025-08-24 05:04:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| df759042-0767-3a79-b488-0056ec449b40 | -21.27178 | -43.7475 | 2025-08-24 05:04:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b753d221-fed6-30a9-b144-d05db12a38b8 | -22.95318 | -45.13487 | 2025-08-24 05:04:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 171045f6-9368-3d32-9bf0-059a404e8539 | -23.31247 | -45.53743 | 2025-08-24 05:04:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| ba8671fe-7e92-3662-9bd1-4a16aa8616f9 | -20.36877 | -46.741 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4770094-6ade-3fd0-bff3-6b4e4e76517a | -23.13496 | -47.03035 | 2025-08-24 05:04:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 66ff4ce6-af3b-3f06-9a57-f30484a545c0 | -25.14447 | -49.53561 | 2025-08-24 05:04:00 | NPP-375D | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3d68b500-187b-3377-adad-3d177e82e3bf | -20.34715 | -51.70095 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c133f43-8825-33e4-abf3-ebd3461b6776 | -23.32994 | -47.84354 | 2025-08-24 05:04:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 890b12bb-1bdf-37f7-bdf0-d0c9d2dcf8c6 | -23.10652 | -49.97328 | 2025-08-24 05:04:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c51f66ad-64de-3bdd-9abe-a8598735162d | -21.70368 | -46.9069 | 2025-08-24 05:04:00 | NPP-375D | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce58f39d-c550-3c67-ab9a-db514733bf4c | -22.79724 | -43.68995 | 2025-08-24 05:04:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 829d27c5-2386-3cbd-851a-1d921ed743b0 | -20.34448 | -51.68853 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2f11d61b-dc2e-35a3-841c-8d06e3dd7464 | -20.36802 | -46.74871 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be42ef87-86a8-352e-9a6a-1d1b4d26cd4c | -20.37047 | -46.72349 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d675f603-6a87-33ca-a0b1-cc850505d1b3 | -20.36732 | -46.75584 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8435d732-51d9-375e-822b-460cd9a82609 | -20.35725 | -46.74057 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85ea7bce-f2e0-3367-b5b1-c7bfc01cee1e | -20.37004 | -46.72792 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56fd8ae3-5399-33bd-8b31-32bf6bddc69c | -21.72972 | -46.81401 | 2025-08-24 05:04:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3f14ab92-4781-3d78-87e6-5f7138dfffa4 | -23.13519 | -47.03374 | 2025-08-24 05:04:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eb8c2c41-5e15-33c1-bcb3-96fd3d950a79 | -23.50668 | -47.26018 | 2025-08-24 05:04:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 20cfd5fb-0930-385c-8eab-8d628b814780 | -20.343 | -51.70039 | 2025-08-24 05:04:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a8f9f1ff-3d67-3ea1-84c1-c4fb38f8c877 | -22.95266 | -45.13729 | 2025-08-24 05:04:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 209f346d-e909-3aa4-9938-5b08675e6626 | -23.63366 | -50.56031 | 2025-08-24 05:04:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 59244501-8c3e-391b-9936-d97b18764386 | -19.94377 | -47.49091 | 2025-08-24 05:04:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdd55a63-4255-348c-bb5f-e2e0f48a6b5d | -20.37461 | -46.74042 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8a46dbad-fc50-3ef0-9f9b-724ff444a14c | -20.36695 | -46.75962 | 2025-08-24 05:04:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 558c2d20-c403-3a2e-bab5-f5251e3f21fe | -21.27752 | -43.75348 | 2025-08-24 05:04:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0b0c4439-31f1-35c0-ad3b-959d78b4ce9c | -22.21678 | -45.69327 | 2025-08-24 05:04:00 | NPP-375D | SANTA RITA DO SAPUCAÍ | MINAS GERAIS | Brasil | 3159605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README70.md)
