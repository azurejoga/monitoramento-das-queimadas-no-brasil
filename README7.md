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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01c935cb-01db-38b6-a8fc-e3783e288557 | -11.43739 | -55.10671 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 92bbdd79-7702-3cdd-9f06-1f2018ce60fa | -13.64979 | -45.5546 | 2026-05-06 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bf7f48f-abeb-39ce-a8f6-b54ff49e4375 | -12.49606 | -58.47048 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 06539ac6-3120-3ff5-8866-e3a0edf4a68c | -11.99562 | -47.77298 | 2026-05-06 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afa98738-a905-310b-9769-c3261ea59d9a | -13.93862 | -47.55127 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 447f22f8-4a7b-3c2b-bc81-4b186776a90a | -12.12287 | -54.66872 | 2026-05-06 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b8e3518-5934-31ac-b162-2b610dadc9e1 | -12.15541 | -57.75487 | 2026-05-06 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f02580d-438e-3072-8f98-aeb9bba6b257 | -11.44076 | -55.10726 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb1572b6-852c-3f97-acee-90e4c36737cd | -11.44134 | -55.10361 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f621d69-4bb5-3d7c-a435-48ba250b9422 | -11.45086 | -55.10891 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e43f883-839a-349a-b07d-5f0f4135ff3b | -9.42076 | -50.69342 | 2026-05-06 04:53:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74845561-5b71-3f5a-99b4-48be6f569cef | -12.46081 | -54.4476 | 2026-05-06 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83d7e081-d0ac-3e39-a0e4-bee2dffd3971 | -12.39403 | -46.3253 | 2026-05-06 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cbef9d1-45fc-360a-b604-4f1f5191ae40 | -11.13815 | -45.14008 | 2026-05-06 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eb42734c-5042-3e5d-ae6d-a5d611ef8fe8 | -12.34478 | -50.02291 | 2026-05-06 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a7dbc24-6b6c-358a-b956-58df6239e4b8 | -11.2919 | -54.02895 | 2026-05-06 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38410f65-413d-32aa-a7fe-2c9b9dcddf2a | -13.1139 | -51.72322 | 2026-05-06 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e779519-df38-3edf-90e6-b4927df22c52 | -11.12576 | -45.11639 | 2026-05-06 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2c85504-81df-3b85-a08d-c48cbe190c8b | -11.99935 | -47.77779 | 2026-05-06 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f713b795-98db-3f0d-946b-7530c0189900 | -13.96556 | -47.54093 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be656cc5-d32c-32a8-91df-3bcd10cc4a5e | -14.07253 | -47.76123 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3aeaddac-1a02-39ad-8b13-b962b3aa0e75 | -14.1347 | -45.35534 | 2026-05-06 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0e173bf-5e68-39ef-86dd-3ec93fe6af03 | -11.80183 | -43.61525 | 2026-05-06 04:53:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b7b56065-8470-364c-a8a8-23e4025f7479 | -13.79878 | -43.34621 | 2026-05-06 04:53:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 18d2ec86-2e6c-3939-a499-b2a8c55fbd3c | -13.70155 | -55.68851 | 2026-05-06 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c78c8bc1-6177-3d51-b8b6-7ee9bc9b7b65 | -13.69818 | -55.68793 | 2026-05-06 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8479ad0-15c6-3640-b2d1-081adceeda57 | -12.50213 | -58.48173 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aafd1c4c-7bad-3706-b8d7-6defaab9f9e2 | -13.46974 | -56.85513 | 2026-05-06 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 384c0a35-81dd-3bb7-94b9-a1d5197bf2b7 | -13.69877 | -55.68424 | 2026-05-06 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 351b1c5a-9c01-3fec-a856-1f17f6c17946 | -12.6043 | -58.66116 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a92980b-1327-3d91-bbf9-1754756c726e | -12.34294 | -50.00869 | 2026-05-06 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a313e6ca-35c3-34f1-a250-20e8f64f92ab | -14.07303 | -47.75736 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 811547c8-baee-347a-a06b-e34bada10313 | -11.46547 | -55.11542 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eaf8ff3-8d9b-3553-a8ba-12c07b110534 | -12.27475 | -43.50875 | 2026-05-06 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dd6cc411-feb5-35a3-9110-66ab16e7cedc | -9.83111 | -56.34751 | 2026-05-06 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f45dbec8-40c7-3bd2-8db1-d74e5559e484 | -11.43797 | -55.10306 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d330a48d-00c5-3243-af11-4fee81782acd | -14.0275 | -47.58947 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5929af2e-c000-3868-9f2d-f3828e59d592 | -11.30243 | -54.02771 | 2026-05-06 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85939591-c3f3-33f3-b2a6-925df98aa098 | -10.58974 | -44.332 | 2026-05-06 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30d8399b-da26-3017-98d7-415bf854ab8a | -13.43627 | -43.84809 | 2026-05-06 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75c0555b-f861-340f-8f42-dea77dab8f01 | -13.99547 | -56.64042 | 2026-05-06 04:53:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ee1ec54-a576-38c3-ae11-126e66ca387f | -13.94352 | -47.54857 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb85da26-ce52-301b-8738-2cd2ebb1017d | -11.85244 | -57.36874 | 2026-05-06 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76d4c77c-7bac-3abf-ae3f-88715d4ee44e | -14.14508 | -45.35681 | 2026-05-06 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8369854-3bec-39ea-af5c-da1718af61ab | -12.5077 | -58.47259 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 90208abc-9b7e-3e0d-b954-cda79425845d | -13.43996 | -43.84373 | 2026-05-06 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4492c51c-8f25-32d0-b0ed-76c2f891a7aa | -11.63796 | -54.16516 | 2026-05-06 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d6c4ca6-72d2-3791-a3e3-cbde020313b4 | -11.80136 | -43.61921 | 2026-05-06 04:53:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ba1dd6c4-7ea0-3641-8701-243f564b6a0f | -12.43841 | -44.6249 | 2026-05-06 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c75a08df-5763-3bec-a6d3-0c1418ee708f | -13.65412 | -45.56142 | 2026-05-06 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e70e7344-880f-3429-9be2-d0ff05c70770 | -13.44237 | -43.84517 | 2026-05-06 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f4421f35-75ed-3868-bed8-6463add390da | -12.49994 | -58.47119 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9b71c6d2-9ceb-347e-8148-d076c72df54d | -13.96296 | -47.53893 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e279201-156f-3a16-a48b-434c109e7ee7 | -12.34649 | -54.76061 | 2026-05-06 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b337834f-0c97-3bee-9d75-a3f949ec8bf7 | -13.99953 | -47.59554 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 956739f6-7f3e-3148-a31c-bc4b97dd11ab | -12.60084 | -58.65837 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c02f1b3-219e-3bf5-a4c6-9641ccaa41c0 | -12.50129 | -58.48668 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 14d2515f-825f-32df-b0b0-89c3347520cf | -11.45596 | -55.11011 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d64c58f5-724b-3b7a-878e-55122e57e144 | -13.6954 | -55.68367 | 2026-05-06 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a813e36f-9820-3052-a7cf-0e0b12f672b8 | -12.39466 | -46.32021 | 2026-05-06 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a516f94d-cd62-3915-b078-970b80164e0e | -10.59016 | -44.32872 | 2026-05-06 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d921f3d-584b-337a-98fe-ce12651c3e38 | -14.02566 | -56.79117 | 2026-05-06 04:53:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c1780bf-222a-3938-ab44-bd5ee2386ac6 | -14.13952 | -45.35927 | 2026-05-06 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 308d12be-dc61-32aa-9a4f-a483447ec602 | -9.25084 | -60.33348 | 2026-05-06 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8f585985-a0d9-333c-942b-fb3721d6d295 | -14.07686 | -47.61967 | 2026-05-06 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f634a13f-c98d-327a-83a0-a454830947b4 | -9.24996 | -60.33829 | 2026-05-06 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 228c87a6-ac9f-3d5c-8d88-17ce88ccbeef | -13.70215 | -55.68481 | 2026-05-06 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c077d5cf-0366-3ad0-8da3-1daee6da84fa | -13.69758 | -55.69163 | 2026-05-06 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c30fc870-56dc-3af8-a7cc-9db441ac265b | -11.38121 | -55.17634 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea239cc7-97a6-3551-923b-6841a727137c | -9.83246 | -56.34876 | 2026-05-06 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9cff854-f833-3f1d-9175-8a8f7cc76025 | -11.63852 | -54.16164 | 2026-05-06 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7c01097-7a1d-36c3-a8ed-1d2a3deba73b | -14.07685 | -47.76263 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1a9797b-b8b1-34db-affa-22ab41c4a76d | -11.29912 | -54.02718 | 2026-05-06 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f407e724-ebb8-3eeb-a80f-3dd0dea6f4d2 | -11.44808 | -55.10471 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 785d6eac-e16e-35fc-9ba9-4a58a37c4421 | -10.09937 | -53.99808 | 2026-05-06 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c830f6d-9359-3014-9ea5-535d4b74720f | -11.4346 | -55.10251 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86654748-a713-3651-b671-e53543f2729d | -14.07319 | -47.79128 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29766a3d-c066-344a-bc6d-edb3c8c4e071 | -11.61675 | -48.05677 | 2026-05-06 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| de037677-fe0b-3f67-8538-a05eff324c23 | -13.43671 | -43.84415 | 2026-05-06 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fa8ea1e-5f45-3117-b606-d3cded753723 | -12.34592 | -54.76418 | 2026-05-06 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a800dbd-abae-3d74-ba7a-04a32fdcdc18 | -12.33537 | -44.59546 | 2026-05-06 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fbe78e7-4cd7-3542-95a7-6634344010eb | -12.34915 | -50.01894 | 2026-05-06 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4adfa2f3-d48d-3b73-a787-dc230a2cb140 | -14.08466 | -47.62965 | 2026-05-06 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1704a964-07fa-3ec5-9301-9d16f6b065f2 | -14.13989 | -45.35609 | 2026-05-06 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c61457f1-2d19-3056-a28f-7e2015164471 | -12.13342 | -54.66678 | 2026-05-06 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 222797fb-857c-31a6-8217-9d83289a9fb7 | -12.35161 | -50.02859 | 2026-05-06 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cb6fd125-d452-3d9b-941b-86957416ca01 | -14.85521 | -48.54235 | 2026-05-06 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7abca40-141c-3bb1-a008-f6570890f121 | -14.08132 | -47.62026 | 2026-05-06 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d55bc3f1-ca0d-335d-aa03-27c482022431 | -12.5099 | -58.48312 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0741e97-943e-39f0-a8f1-e732c6353af3 | -12.50686 | -58.4775 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d9ebdf8e-e07c-307b-9910-906eb7bdc6b7 | -11.80834 | -56.98871 | 2026-05-06 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3f107ce-39ec-3e14-a09e-5d3dd35d01af | -12.50382 | -58.4719 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 60899cc2-3dd0-3b3a-9e56-984d3899d908 | -12.7168 | -54.99797 | 2026-05-06 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c942cc-307e-3977-a4c2-e6bfc6d619fa | -14.07272 | -47.79497 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bf2371c5-f160-367d-b2d5-de7536fd8d7a | -12.26902 | -43.50802 | 2026-05-06 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32330a56-f4ad-316a-8958-83f149194aa5 | -11.55323 | -48.27241 | 2026-05-06 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19c71706-aab1-3a3e-be90-6367d0e32125 | -12.50517 | -58.48737 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 28a2468b-fd8b-35c2-a676-ac637dc324a0 | -10.48556 | -49.36229 | 2026-05-06 04:53:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44b6fb37-270b-3c5c-b433-c19d461d28b5 | -14.08077 | -47.62461 | 2026-05-06 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f034121-0b1e-3edb-aeea-9d4b03f2d942 | -12.1262 | -54.66925 | 2026-05-06 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README8.md)
