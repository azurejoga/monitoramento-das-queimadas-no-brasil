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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 735a8c9e-d441-3680-94e1-c8db4baf1699 | -2.64853 | -46.10997 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dcf3191-e3ea-3383-97c6-4d30e9406114 | -4.0473 | -47.02766 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a033a560-fd80-35e9-a6f3-5122446559b8 | -7.54088 | -35.30487 | 2024-12-23 04:31:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 81b057a4-4c51-3e3c-8595-a14f9fbcab9e | -4.07883 | -46.80484 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d23c875-5a90-30c9-9907-49d4966e560c | -4.06243 | -47.08325 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18889418-c58a-38eb-8bb3-50462982549f | -3.64023 | -40.47545 | 2024-12-23 04:31:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| af5569ea-5c3f-313b-8134-3435394a6629 | -11.65116 | -43.87637 | 2024-12-23 04:33:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd341da7-05de-34eb-a0a2-c41a83a1c7b3 | -11.65065 | -43.88006 | 2024-12-23 04:33:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c7ae24b-7a36-3677-a71e-8115090047b3 | -13.50792 | -44.30217 | 2024-12-23 04:33:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58b7ce45-3ad4-3e6a-a7c8-08f3aef9babb | -10.42869 | -44.8857 | 2024-12-23 04:33:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b0c389f-208f-3b7d-a2f4-58fec643b6aa | -8.80093 | -49.79819 | 2024-12-23 04:33:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee4013ce-71f6-39da-aecb-f882d4849971 | -8.80431 | -49.79874 | 2024-12-23 04:33:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 782bacf4-ad25-389f-961d-35110c9ffe6b | -16.85992 | -39.24256 | 2024-12-23 04:36:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b0a773f9-ddcc-3038-8c5b-ad1278d5b062 | -19.33927 | -54.17696 | 2024-12-23 04:36:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34637aea-c710-32ea-bcf8-37cfe9043a55 | -19.06812 | -53.46807 | 2024-12-23 04:36:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f0a1c89-49ce-3f58-8c84-ea9e2faca56e | -16.85093 | -39.23593 | 2024-12-23 04:36:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3e254dbd-d923-3947-82c0-9ebe9aa52705 | -19.8287 | -57.51683 | 2024-12-23 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a7defbf5-0e22-39b4-92e9-1309d6b3ecff | -19.33644 | -54.17189 | 2024-12-23 04:36:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b77506c0-601d-306e-9b69-82ca32b6e3a7 | -18.51509 | -53.40339 | 2024-12-23 04:36:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00de1cd6-e7a6-3bbc-a56b-bce851f6c47a | -19.33567 | -54.17627 | 2024-12-23 04:36:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45a5126c-ee77-3f2c-8fcf-1fd1e94ce086 | -19.02498 | -57.62063 | 2024-12-23 04:36:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a1dd9d77-0fae-33f1-9544-3aa3475e3ecb | -16.84842 | -39.23661 | 2024-12-23 04:36:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 83b35c92-b172-37fc-a447-d06e009d9f9f | -16.85445 | -39.23698 | 2024-12-23 04:36:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 30d9688a-8e9a-36eb-8a2b-89419c37a4a8 | -16.86041 | -39.23802 | 2024-12-23 04:36:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4bf90b42-30b4-33bb-912d-4fc5ab68509c | -16.85647 | -39.24119 | 2024-12-23 04:36:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 306949c2-590e-3d19-9de7-33733a823bda | -18.51579 | -53.39929 | 2024-12-23 04:36:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd181787-6f34-3b09-b3e1-a073e7299c80 | -15.53149 | -50.75002 | 2024-12-23 04:36:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec5e15d8-24ff-36b0-9cd9-0ca2f0c64aa9 | -19.34004 | -54.17258 | 2024-12-23 04:36:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e94377de-9fd0-3cac-95cc-52eea9657a8d | -19.02054 | -57.61991 | 2024-12-23 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4e911fd1-766e-3d9b-99ee-6473effb418f | -27.89621 | -53.29609 | 2024-12-23 04:38:00 | NPP-375D | PALMEIRA DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4313706 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 195967d1-b807-31aa-81e9-85cbed7ab88f | -2.33566 | -54.90024 | 2024-12-23 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9494e797-268f-350b-b94e-3a5e979eeb72 | -3.09395 | -54.60223 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da15c56d-ad3e-3a82-9b3c-10c5285a13cd | -2.12434 | -50.70385 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d329a79-9360-3b0c-a525-16d51a3491cb | -3.75504 | -47.20042 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1799b8bc-be43-31de-9ff9-96b76f038600 | -2.73901 | -46.87143 | 2024-12-23 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d404c6ec-6a1c-36d6-90f3-2ced94d8d899 | -2.80014 | -54.03164 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 292cfc49-6fac-3e1a-9792-d6ff8eadb2cd | -2.49874 | -54.1984 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 872ce477-55f4-355f-bcbd-239959fca68e | -2.53035 | -54.14961 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05f7d6bc-d3f4-32cb-b374-045c6fcdba83 | -2.66753 | -55.2382 | 2024-12-23 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3c1073a-f206-3050-b546-32fa98fbea07 | -1.31752 | -54.08642 | 2024-12-23 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e95c5f8-ea98-3933-8a3b-1826a0d22823 | -1.6334 | -45.84977 | 2024-12-23 04:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed65ebc0-2afa-35c4-b3f0-9cbb0bc5b80b | -3.18336 | -50.56846 | 2024-12-23 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89238ff7-a84c-3eff-b72c-bcb377ee9860 | -2.88598 | -51.80009 | 2024-12-23 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92f06787-c699-305d-92cd-233a22ad9d8a | -0.71455 | -52.84632 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69c9e941-0c64-3774-9cae-89003677e9ec | -2.78985 | -53.23475 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd31883a-9b57-36c0-a5a6-a981f726f16a | -2.4954 | -54.19788 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53d9402b-60b9-36a2-bf2f-5171d0552879 | -2.12696 | -53.47597 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74a240e2-ca94-3468-8c0c-2139c5947933 | -2.08182 | -53.33141 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b178bcb-f115-3ce9-b810-40f9e15dda01 | -3.1903 | -52.89156 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d042940d-0fe5-33c5-92bd-c2cb6aad46fc | -4.04059 | -46.4142 | 2024-12-23 04:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91362abc-4855-3c12-882d-91c3035c12ec | -2.22935 | -53.79639 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb669c22-5568-39dc-9453-942aa992fa4f | -2.66559 | -54.02464 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28441da3-7ab2-31f7-9334-f22dd99b4720 | -3.87265 | -47.2869 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4603765a-bfd2-36c7-b925-b4fd84e51e62 | -1.1399 | -54.19608 | 2024-12-23 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bee1c7de-8e93-3881-ab27-4b4836d9eba2 | -2.78606 | -51.78926 | 2024-12-23 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9d0b24f-71c6-3e7a-84a7-dfeeb58d9fc7 | -2.73456 | -46.87084 | 2024-12-23 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c392706-7267-322f-ad7f-180571f2a465 | -3.99063 | -46.95755 | 2024-12-23 04:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35a2eb02-2c96-3c84-969e-51a404e5f2ed | -3.04405 | -54.67818 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff059b41-7ec3-3b9c-b379-73fabd095878 | -3.31096 | -51.45679 | 2024-12-23 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0c3090a-600a-303a-a7b3-2ffba45d735f | -2.35927 | -53.63967 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbbc816b-8526-3c76-b7f9-aa0b4b04862c | -3.03843 | -52.71215 | 2024-12-23 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a147b25c-8e4f-38b6-bbd4-26e6ae3bc8b5 | -2.37839 | -53.77713 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d01b51d-e08f-3de0-8640-69b15f2f932f | -3.19084 | -52.8881 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e45f7104-ed75-37e0-8859-1c90ae51cc34 | -3.54892 | -51.07857 | 2024-12-23 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9927e8c3-ecad-30e8-8085-bca14f751fd7 | -2.89738 | -54.25414 | 2024-12-23 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 006a5c68-1f76-3471-a7e7-51f0aab7a08c | -1.18734 | -46.6647 | 2024-12-23 04:53:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56a70c00-3fd2-36db-bd1b-60f738351af6 | -2.46258 | -45.81197 | 2024-12-23 04:53:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d00abf23-75b8-3a4d-b3e1-371a834622ac | -2.48482 | -54.17832 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b94eb4a3-c1ef-3305-94a2-8c09b9df87b5 | -3.74689 | -47.19466 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19ebe016-ec57-392c-8a8e-b25ac501cd23 | -2.69119 | -51.91039 | 2024-12-23 04:53:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7d7eb76-a533-3342-abe2-19e35c550705 | -1.62873 | -45.84905 | 2024-12-23 04:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f211e1d-1431-3d4d-a67d-cbafbb06ce2a | -2.79961 | -54.05648 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6e194c4-b9ad-3eeb-b245-97b69aa1fe67 | -2.63779 | -46.97688 | 2024-12-23 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fea9409-fc7c-30a1-a5e7-ad7f48b65f6c | -2.77271 | -53.21448 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c6c19e6-9e73-327e-976a-9b8b6db13a3d | -3.09675 | -54.60631 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13a5a62e-8a42-3c6e-b27f-d2f92934dcc9 | -1.56748 | -54.76731 | 2024-12-23 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ace9ffe-533b-3cc5-a854-d9243b515454 | -3.1477 | -53.1851 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdede7b0-a64c-3fd7-af1e-5335adb1e2a3 | -2.40814 | -53.73961 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea985b3f-af6f-3fd4-bc78-f35f38eb2e0e | -3.90187 | -46.99892 | 2024-12-23 04:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86e6a7a8-a90f-392c-9ccf-af7ca37a3191 | -2.22603 | -53.79588 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9763a740-4f28-3738-aa45-346ce980ac61 | -3.90767 | -46.99069 | 2024-12-23 04:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c09d72a-917d-3f4f-b699-724f6a3373e7 | -2.42544 | -48.59666 | 2024-12-23 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d2fdb8b-76f7-30d0-92f4-219611bb8471 | -1.50459 | -52.63941 | 2024-12-23 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 658acb10-425c-3999-9f9d-7a5c11130c89 | -2.40427 | -53.74255 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c8fab60-d9b0-343e-b5af-c89950900116 | -2.55996 | -53.96136 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cae3baf-0e4f-3e37-852d-9923cb5f399b | 0.15165 | -51.12294 | 2024-12-23 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1796751-44c9-3799-a5eb-bba6d7cdba25 | -3.09731 | -54.60275 | 2024-12-23 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22e9d318-8202-3934-86b1-d59d18916313 | -2.25859 | -53.54625 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a85903a6-0620-3056-9623-26b2416bcfc5 | -3.50851 | -47.19652 | 2024-12-23 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d5a457c-50cd-3673-8f65-01f65080d4bd | -2.40759 | -53.74307 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc71b124-cc20-3597-aa26-03b26ba2b122 | -2.63807 | -45.68825 | 2024-12-23 04:53:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 162af981-d10a-32ac-a174-061b84e86049 | -2.40378 | -54.19871 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3be975dc-31a4-3210-9386-2648cb8145c5 | -2.98269 | -54.12436 | 2024-12-23 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e04060e9-33eb-3f8e-8b4b-43da217110d2 | -3.35038 | -47.11108 | 2024-12-23 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f15ba63-9760-337c-9d6f-6dc1d689b7ed | -3.09421 | -53.2862 | 2024-12-23 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7264c0f5-442e-3aa0-a137-a3c1d91e3796 | -3.02928 | -53.89327 | 2024-12-23 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfe560b9-cc68-3870-b7bd-e06ac1406e1c | -2.67506 | -53.07911 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abf12723-1261-348b-8aa0-f30e098118d9 | -0.20696 | -51.60464 | 2024-12-23 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6781c6b8-4cc4-32d5-b77a-0080c283dd19 | -2.51824 | -54.22649 | 2024-12-23 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d223112c-4bbb-3a2a-953a-605d7c531bbc | -3.17996 | -51.39931 | 2024-12-23 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README16.md)
