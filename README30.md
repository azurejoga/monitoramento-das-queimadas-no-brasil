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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36c60fbc-a2b0-3396-aa83-27ee67e93fb2 | -13.35573 | -46.96039 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b359a543-aeed-33f1-834e-7e475b615c0d | -11.56303 | -47.61682 | 2025-08-31 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd919b1c-d664-3dff-a508-c85df6eccf5c | -14.35024 | -51.88983 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7c62f2a-4e5a-3db7-8b94-00a95a096df4 | -11.55868 | -47.61604 | 2025-08-31 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55a4e776-aff5-3fee-a907-a2abcc68acb0 | -14.99276 | -46.70351 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b66d463-188f-3679-a132-fa8190ee89d8 | -13.4864 | -46.8385 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a0e0e7a-7e00-37a8-afcc-3c717422a332 | -18.66582 | -49.09308 | 2025-08-31 04:04:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d87cbec9-c8fe-3b29-a5c5-346e44963402 | -13.35374 | -46.97156 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0c762a3-c4ef-3fe2-8834-a05fff9a930e | -17.14554 | -46.07293 | 2025-08-31 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aa16f41f-c661-36dc-af4f-aa6c753d3ac1 | -11.90014 | -46.42604 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc50bfab-b22c-3926-a9f2-bdbb922137fc | -11.89379 | -46.36902 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9afb0def-01fd-3166-ab5c-2288ddc48dc7 | -16.10534 | -44.55192 | 2025-08-31 04:04:00 | NOAA-21 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef1ad0fd-ad61-32fa-bd27-dbcd392c1a3c | -14.22686 | -48.07033 | 2025-08-31 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c63708cd-c138-31c8-a2ce-a7159a36304f | -11.91594 | -46.40669 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b0203b0-4920-3a52-b747-248c41567ed5 | -18.06569 | -45.94714 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9fbcc34-c88e-3ae8-a7d7-68db668e2c5b | -13.9879 | -44.55133 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 945c9451-ca17-336a-bc0f-ca946e6c7ec4 | -15.67474 | -43.2255 | 2025-08-31 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6893277d-9e20-36fa-aa0b-9a2ef0c12926 | -13.35985 | -46.96072 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee705da8-c5a9-36be-804c-dcff795595dd | -14.53599 | -51.98829 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b25b60f1-cdeb-37ae-bdd7-726eb0e8e88f | -13.37666 | -46.9601 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3694c0c-f42e-3ec4-bfd1-51e5870d0aa4 | -13.31652 | -46.94616 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b6df304-ec1b-320c-beb0-0cf26f0b21bf | -11.87992 | -46.72943 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e065c51e-390e-3847-bc02-d60d56dc841a | -18.06497 | -45.95135 | 2025-08-31 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d33f4432-905b-3c96-b848-28a295f22b22 | -11.92057 | -46.4038 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72ba7094-5b73-337e-9b08-f2824dc331b1 | -11.88813 | -46.49376 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e69f0c7-ae06-3595-a31e-114885016fd4 | -11.8224 | -46.43618 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1278d156-994a-393e-9108-c109e3148fa4 | -13.47621 | -46.94241 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bd7aee1-eb9f-3105-acd6-b4e02fda9e0d | -11.90676 | -46.69627 | 2025-08-31 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf2b5004-8fde-32ee-9e5b-6df7d8bbe26d | -18.79373 | -46.8289 | 2025-08-31 04:04:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14c89829-a916-3f12-a873-2e599481ad41 | -16.21957 | -52.67646 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14d8f31b-cb84-3eca-8bdd-d801cd214336 | -14.8232 | -46.74603 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a5aa3622-7f51-31be-877b-920905e0655d | -14.27708 | -51.88317 | 2025-08-31 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7d09189f-7fdd-38f8-99b8-7e26a69005eb | -13.33091 | -43.19003 | 2025-08-31 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a9e650a7-ff32-395a-accc-38ff78066273 | -15.21381 | -56.062 | 2025-08-31 04:04:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5bb63c9f-49fa-32b4-a6d2-deb51d3ee6c2 | -11.86337 | -46.51066 | 2025-08-31 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54a28903-9855-38ad-9bd1-040bcca51fe6 | -13.99752 | -46.32486 | 2025-08-31 04:04:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4e80e8c-e623-3488-a2c1-a6c7583b391c | -16.2268 | -52.68977 | 2025-08-31 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 863007c6-abf2-3741-8432-7fbeb9951629 | -17.4782 | -46.99794 | 2025-08-31 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f72ebee-7a72-3883-b9ba-44dbc636bb8d | -13.31005 | -46.88478 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b81c6c0-e2d9-34ce-9c0a-0ca4011b589f | -12.45471 | -44.04973 | 2025-08-31 04:04:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d61cf2be-c4a5-3329-bd15-c40cb34dac02 | -13.66946 | -46.87245 | 2025-08-31 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cad0ba6-73a9-3755-8717-45799217e36e | -17.86483 | -44.30913 | 2025-08-31 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a34a7f4-2d08-3197-8794-25d7f907dd6a | -13.50361 | -46.83466 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 851a06a9-b0b8-3a7a-8954-cafa58133c87 | -11.06132 | -52.04223 | 2025-08-31 04:04:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bef5fd29-fc11-30ca-878e-3b26a0530e49 | -13.30724 | -44.27382 | 2025-08-31 04:04:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a21abb06-c3e7-3854-8b3b-a9481feb44aa | -14.99676 | -46.70361 | 2025-08-31 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdc2ba20-d0eb-3561-906a-a67c6132f751 | -14.03925 | -44.56865 | 2025-08-31 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a41c4123-6a5e-329e-9457-b73178be4431 | -11.55979 | -47.61494 | 2025-08-31 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c4fa65e-de26-30b0-a136-9fcef59e6d6b | -12.8487 | -48.08307 | 2025-08-31 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fe25e158-f234-38c0-9a26-0bc77bc6f741 | -13.12167 | -41.05371 | 2025-08-31 04:04:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e86130f3-1b7e-3dbb-a53b-1af52edbd54f | -16.76778 | -50.30503 | 2025-08-31 04:04:00 | NOAA-21 | SÃO JOÃO DA PARAÚNA | GOIÁS | Brasil | 5220058 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b790c03-1991-3e26-868a-84aaf5527fd5 | -11.56415 | -47.61572 | 2025-08-31 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab00507d-341c-34cd-9f18-c1e7a5d1802d | -13.49697 | -46.96627 | 2025-08-31 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc61bd64-1805-35ae-8835-641550545fc0 | -13.34683 | -51.76786 | 2025-08-31 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b825d3c-f550-3803-8aa5-7e8efa32c8a6 | -15.29935 | -49.11659 | 2025-08-31 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3f19acb-ae20-3faf-9917-a788cc8aeab4 | -10.95927 | -50.84874 | 2025-08-31 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c1b0656f-e7a0-3538-a4d7-f1761dcd5181 | -15.49691 | -41.521 | 2025-08-31 04:04:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b5a5cb9b-e677-3bec-8567-be145f7cd584 | -22.25018 | -56.12603 | 2025-08-31 04:06:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4865a3f2-70ef-3f47-b938-6631a79f8eae | -21.43711 | -54.1516 | 2025-08-31 04:06:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d052a0a1-88ff-31f1-b04f-a7b6cc62f25d | -20.55068 | -56.26194 | 2025-08-31 04:06:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7b887bee-b89d-3baa-9a06-0d1de19c6e02 | -22.18052 | -46.63691 | 2025-08-31 04:06:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e9942c7f-3376-3212-978a-0477d4fe7c68 | -23.8403 | -47.79986 | 2025-08-31 04:06:00 | NOAA-21 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7bb6d8c-76bb-3645-ae52-6aa7c89c2bc8 | -20.55319 | -56.26107 | 2025-08-31 04:06:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a9d76453-59a2-3c3f-9729-0df80d7c25c9 | -21.1292 | -47.86056 | 2025-08-31 04:06:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31389866-c19f-38e9-98ec-8f9bfdd63b20 | -23.13494 | -50.45036 | 2025-08-31 04:06:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ebc9628a-7ce7-332c-ab6b-ff8b85049b86 | -22.96509 | -47.21066 | 2025-08-31 04:06:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1f4e4526-777e-352b-a730-7cc19b0d3569 | -22.71236 | -46.82269 | 2025-08-31 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c90d4a0e-2573-3471-aa0d-17c0259fdbca | -21.15771 | -46.17534 | 2025-08-31 04:06:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7447a25-601a-33aa-8414-caa549a29693 | -22.7131 | -46.81844 | 2025-08-31 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 29c0f78d-275e-3a06-8435-f6aa61ad786c | -22.14236 | -46.94101 | 2025-08-31 04:06:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f922c6d0-2e96-321a-a5db-bdb91a118034 | -22.62488 | -47.93973 | 2025-08-31 04:06:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 661fa72a-fffc-38e6-ba23-014fcdb5d4fb | -19.99027 | -46.99719 | 2025-08-31 04:06:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4988d53-fc27-3c2d-b581-e08666d8844b | -22.69316 | -46.8495 | 2025-08-31 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9319b49f-41eb-37a4-99aa-16bde900306e | -22.47656 | -47.44025 | 2025-08-31 04:06:00 | NOAA-21 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5dc7a367-07e5-3f99-9aea-17220f1304f7 | -23.54877 | -47.44983 | 2025-08-31 04:06:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 3b230d63-9abb-3b05-97a6-e42dcbc133ff | -23.54237 | -46.18779 | 2025-08-31 04:06:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 108d4b9f-4dc0-38d5-8c9b-f32145f6b3ba | -23.6334 | -53.38248 | 2025-08-31 04:06:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e2feac1d-6a01-34c7-98a0-dd343e0097eb | -23.13406 | -50.44992 | 2025-08-31 04:06:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4e3bdbd3-d34e-362b-8f57-085019dcbb0e | -20.26233 | -46.01136 | 2025-08-31 04:06:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a0804f3-2c4b-37ca-a092-9eb92df82082 | -22.0167 | -45.12311 | 2025-08-31 04:06:00 | NOAA-21 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e00f5c0-18e5-39d9-a49f-5378b7c21c24 | -22.21268 | -45.87086 | 2025-08-31 04:06:00 | NOAA-21 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59bf5345-cb93-36d1-b008-98714f0ba0d2 | -22.62118 | -47.93892 | 2025-08-31 04:06:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 22.1 |
| f702e5fe-9602-3aac-9043-3558ff2b22f2 | -22.62401 | -47.94455 | 2025-08-31 04:06:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ba938ed-77f5-390b-a9cf-d1afbfd6e613 | -23.18862 | -50.94295 | 2025-08-31 04:06:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 52a4bf6b-c468-34b7-8b41-8515998660c5 | -19.88544 | -44.76322 | 2025-08-31 04:06:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 739d7ebb-f089-39da-af6e-98b3948f449c | -22.04106 | -47.93329 | 2025-08-31 04:06:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63572e1a-81cf-3d0c-bdc0-21ef52a7bba7 | -21.13298 | -47.86128 | 2025-08-31 04:06:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52ac5cea-7dea-3993-bf7f-c3d97aacefea | -22.73875 | -46.12962 | 2025-08-31 04:06:00 | NOAA-21 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 87e85069-fe9e-3fa0-80fd-9d4dc1d2ba14 | -20.74897 | -47.13667 | 2025-08-31 04:06:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37a8ad01-8057-39d0-8fdd-abf3ec364457 | -22.71662 | -46.81912 | 2025-08-31 04:06:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bb0e34c8-e64d-3144-86c6-808cedd8ee1e | -22.40379 | -47.00354 | 2025-08-31 04:06:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9afab20-013d-35fa-8d2b-4ba21bc48eb1 | -21.43625 | -54.15545 | 2025-08-31 04:06:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 3f32576a-d3fc-3d19-963f-ac21f552d93f | -20.26089 | -46.01964 | 2025-08-31 04:06:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 7aca10f2-80a0-3284-bac5-3fe06c9594f4 | -20.26161 | -46.01549 | 2025-08-31 04:06:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4041e5f-da5d-30c0-8414-ba53edd0e17f | -23.0225 | -46.46572 | 2025-08-31 04:06:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 77e1b781-25f0-30a8-bc0d-2999e6abe876 | -22.38432 | -46.96819 | 2025-08-31 04:06:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9bf5c4dc-9d35-3fab-9701-4a50be948c07 | -24.12578 | -46.71044 | 2025-08-31 04:06:00 | NOAA-21 | MONGAGUÁ | SÃO PAULO | Brasil | 3531100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6f9e5995-9c58-338b-9e75-c3ae7e0e145a | -22.62031 | -47.94376 | 2025-08-31 04:06:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7f408e00-2d4c-39a0-adfe-7358f920a98f | -22.80159 | -43.72221 | 2025-08-31 04:06:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0616bbab-ba30-31e1-a738-1010bec7c69d | -29.47377 | -51.33681 | 2025-08-31 04:08:00 | NOAA-21 | FELIZ | RIO GRANDE DO SUL | Brasil | 4308102 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |


[Clique aqui para ver as próximas entradas](README31.md)
