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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 242396c6-36a5-38a6-b625-9625c0a7e1ef | -14.99267 | -49.96874 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 543c163e-73bf-39c3-9dcf-05f8d37f5b27 | -15.74457 | -46.25596 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 894ec68c-8381-38f6-8e1d-e24ce1a36e7a | -16.03649 | -50.97434 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cfe71011-a923-3cdc-9663-b11d934a6f9a | -11.82033 | -45.1025 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dc523b84-3daa-3ef3-b966-499b68f0f172 | -13.68472 | -47.35661 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 925a5cc7-f58e-3742-9809-09c654603225 | -11.16253 | -47.93039 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43413cd5-2c2e-36fc-b55f-11647bdadd68 | -11.70888 | -47.50591 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 447f2882-1a30-3392-ade6-ffbd18c4913f | -11.02098 | -46.54789 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23a8cc9e-3cb7-30b3-b690-9230bbd7e1cf | -15.59561 | -52.53896 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57ab727b-5eab-3cf7-b988-026b155aa9a9 | -10.39929 | -50.32402 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2cf4006-5d18-36ff-bfa2-34a235d0c568 | -11.06949 | -47.87233 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4ae8ff3-143c-3d95-8fbb-ff351f608c2c | -11.11211 | -47.19167 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 702aa16c-4a4e-3f2f-8f99-5295f0c24630 | -14.35296 | -47.69822 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da08fbbd-eb37-30a3-888d-a313e2b84bd8 | -14.75251 | -48.40967 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77e55751-e9f6-318f-b529-622dcb4a8607 | -12.37771 | -46.50163 | 2025-10-06 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87db03ca-8daa-32e5-b9b8-d21dff044b2d | -12.44414 | -45.57388 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 045049be-2e43-3ac4-aea3-ca7af596636e | -13.23889 | -48.46745 | 2025-10-06 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca7793bc-b81d-3563-b1f0-6336443b17e6 | -13.60149 | -48.69168 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 670c44c7-9e96-33f4-b2a6-13afd3b0f8f7 | -8.61676 | -54.95683 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8353c44f-7f4e-3376-af04-b2203228839b | -9.89738 | -49.95858 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 365f23c1-30dd-30c7-9972-4dfcca15e898 | -13.32616 | -47.1679 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24c0b7e7-465d-3430-9f87-9ecec8c46bed | -14.67499 | -48.33894 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a653b01-002c-3d95-8165-052d9c54c063 | -13.60697 | -48.69992 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f696b63-7247-378a-b90b-9dc591419a63 | -13.36299 | -48.04623 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7108c5e-80f6-3bfa-927c-19b34c6a5bf7 | -12.71785 | -46.87796 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 50eb9b62-88a8-385f-a2c2-54ea16091d4d | -10.67412 | -48.47565 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ab563c7-087c-3e1a-adf8-1eebd2729efb | -13.3129 | -47.56118 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e648020b-6cbc-3dea-b8c1-603cdce5b162 | -10.32604 | -46.95067 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03d8ea71-fc82-3e2c-be71-702bbf9b4e85 | -13.26573 | -46.47312 | 2025-10-06 04:27:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb3fceb7-9bd3-3ca6-bbca-38df3cd5f049 | -13.09803 | -47.93761 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3ce377d-30e1-3aa4-9ed6-d68bac9efefc | -14.36179 | -47.72863 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 131ba682-31df-3b2b-b952-d8d8c98c0355 | -10.61715 | -48.70269 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ec7790a-8d6a-3608-9651-46b70abea2f1 | -11.91088 | -46.22205 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5363e88-bf98-3d49-8fcb-af7594ce5a8d | -15.15827 | -45.75864 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 832c4f5c-26b7-3fdd-a84c-0ed851468eec | -9.32936 | -54.51457 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36b137ab-0fb2-346f-9a1d-6f7c79916cfe | -11.12846 | -47.75613 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f1e3abd-4c45-342b-b273-da419ecb974f | -14.37467 | -52.16702 | 2025-10-06 04:27:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35714a0e-8f74-3bf9-8014-252d031b7a88 | -11.44319 | -43.48645 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 278aa602-0142-386e-93c3-02f48618051f | -11.64078 | -47.74594 | 2025-10-06 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b013c52c-ff9a-3ec9-b752-e768074b2522 | -13.26809 | -48.47595 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b5bf298-f4f9-3698-943d-126cca49e2c3 | -16.00097 | -50.84632 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93a5dd0e-7492-3f37-a9b3-2a30c65dc46c | -10.31507 | -50.26406 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83b184ea-8934-33ca-b074-38bb29ab54d9 | -12.42092 | -51.10476 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41e0c7ce-3e06-3459-a674-814d3dcc4962 | -9.2749 | -51.79928 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8727164c-6228-3b12-8ba2-f5d32ae5b414 | -10.81611 | -48.82097 | 2025-10-06 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15e67b21-a1ee-3507-9b2b-0148b88541bb | -11.5345 | -47.68586 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 298ad96b-471c-3f6a-b099-ddfdf48eadc9 | -10.30723 | -50.267 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b1c9859-8df5-308e-9a50-525df163af0d | -13.72162 | -48.08352 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06787493-2d09-31c0-99cb-1e6cfbec1c57 | -13.12544 | -47.99985 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb9fc02d-9165-3925-853a-4113bdf71cb7 | -9.23075 | -51.82598 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5654ac87-e421-3461-bffa-a6352af941a3 | -14.85897 | -51.49317 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33881288-e9b4-3394-8120-fa79e4da76fa | -13.08485 | -47.93546 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c175dd17-b155-3ff8-8b4a-8e4569c4e093 | -12.41366 | -51.12577 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e23e1b0f-c6b3-32e2-8344-5ecc06a95691 | -14.8561 | -51.48827 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55c07fcf-4e03-3a26-89a3-332c3edd34de | -12.90061 | -54.75687 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7a9972a-3cac-3092-92a5-89f98345e781 | -14.91174 | -46.86376 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c216653e-ac7c-3287-902e-42abebafa1e6 | -13.35049 | -47.1864 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e47d4a5-7767-360d-a843-918ed60bd48f | -14.71619 | -48.35666 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| afa97655-f34f-312c-b12a-6b47cb6ce6b9 | -15.20768 | -56.81443 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4f5daa1-10e6-3817-a372-5d426a05b8a9 | -10.84089 | -47.18357 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39958185-9f40-3902-a21e-96c0ee92753f | -16.28878 | -45.24386 | 2025-10-06 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f992984-d2a3-3437-b2c8-3485c7fa1af6 | -11.48688 | -59.09457 | 2025-10-06 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41743d84-10f7-396c-a30c-987033efb1f1 | -13.25846 | -46.47572 | 2025-10-06 04:27:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 993bef00-dc96-389d-b47c-8719f7aecf92 | -11.84414 | -45.08588 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7ab03eb-1468-3fb3-aba8-97e0d889752c | -14.62359 | -48.12362 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80270c7b-fb06-339d-b8f3-83613c0dd123 | -12.37103 | -46.50059 | 2025-10-06 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52586382-4b99-3df1-9aa2-8a85daa48789 | -9.24354 | -51.82265 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ba0fd1c3-cc05-35b4-839f-4750eae5bd1c | -8.62182 | -54.99427 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95ec48fe-67e2-31c5-bf77-e5145ceb3d50 | -13.63349 | -48.70423 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 283fe4fc-a540-3c6c-9bdf-15fdaee4d02a | -14.34084 | -47.68899 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7bb7f07-25c0-34a5-a4be-c84398f869e2 | -14.91564 | -46.86067 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a15f5bf-fbc8-3c09-a061-a390d2ffa57c | -13.34154 | -48.05357 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffcf9836-30fc-354b-8c9f-2492cc740b17 | -14.3265 | -47.65026 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ac5c583-13be-3549-90af-d99f417cd11c | -13.38166 | -47.55823 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58532cc4-0f2b-337c-b381-08fbf2ebd1c0 | -13.08043 | -47.87713 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2f7c12a2-72cb-3b5f-ac0c-11ce9c489823 | -14.91667 | -46.83098 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bc3c0723-6eae-3a90-9803-3ffa652c8212 | -11.57791 | -46.77369 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68dbce46-c3ee-3172-93c9-0d7338c271ca | -13.26534 | -48.47184 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c47aa49e-3e4b-3fea-8b1f-b1c88eeea5e9 | -12.90451 | -47.30001 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 10194b8d-60a2-338b-a9c1-e8136159594e | -13.07823 | -47.95603 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d09bba10-211f-39ac-be15-1eab4638af55 | -11.03545 | -47.78773 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff5b22ee-b6f1-3355-a4e3-737ddfe77169 | -13.11718 | -48.00934 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d223db64-a0cf-3d70-bdcf-7a11ff184ca5 | -13.0887 | -47.82441 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04a84c2a-c293-3738-8411-e18fa5d1ed71 | -11.86959 | -56.88758 | 2025-10-06 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4e78755-ca05-3f1f-9420-3412690450e7 | -11.9355 | -46.43649 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8bd64d34-975f-329f-b626-8acecfbbba7d | -11.12635 | -47.16533 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56a6a1bd-1f95-32de-ad3d-56eda3e62b6a | -11.68247 | -47.48015 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c3ed25e-2cc9-3390-89f9-b2446bf9f3b8 | -10.61993 | -48.70685 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| def209a1-aa76-3035-8462-4162bd563d6c | -10.96885 | -47.08244 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4f50245-cf2f-32d9-a513-a35b9a9619bd | -10.68421 | -44.14696 | 2025-10-06 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3308af70-331d-3446-8c72-f8150050046d | -12.99071 | -51.04411 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3816fb17-1d7f-3608-95fb-89d32d9a7d19 | -16.0118 | -50.82411 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1d12751-5cf6-3049-8f29-668afe17f7e6 | -13.25654 | -48.46315 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1bd44c1-97b9-371c-ad37-21978f5a2409 | -14.66557 | -48.37735 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdaaa2c5-2919-3536-935c-3679aab09fec | -16.00574 | -50.83906 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5910733b-4b29-38fb-9f93-fe7d13b08044 | -12.91397 | -54.73521 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78290299-e492-396d-993b-1a9d125953f7 | -16.00508 | -50.84297 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33cb0ebb-168a-355f-9042-3c65abaa53d9 | -8.88181 | -50.89386 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b46bd33-2429-3d9c-82d3-d72421efe253 | -13.08925 | -47.82089 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cce3d05-2a4b-3649-b64a-722cf54026b7 | -13.27166 | -47.58705 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README54.md)
