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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8277647d-bf79-3fa3-bbc8-d15a6a11f026 | -17.66353 | -53.10311 | 2024-09-29 01:05:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fe7fedbb-ef34-3d31-8fa6-ba399976442f | -17.62589 | -43.26679 | 2024-09-29 01:05:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ced5a61f-898d-3363-acc6-66df31ff1780 | -17.62345 | -43.25216 | 2024-09-29 01:05:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 096529bd-848e-3146-9e8b-ebbda7b15c98 | -17.50066 | -44.49929 | 2024-09-29 01:05:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 887a5469-f817-395b-baf4-98efce3a3775 | -16.90131 | -45.32014 | 2024-09-29 01:05:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 07735d03-1f30-32a6-964c-c03f2b246678 | -16.89943 | -45.3145 | 2024-09-29 01:05:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a741012d-7e4e-31e7-9452-c0f418aeb486 | -16.88954 | -45.31611 | 2024-09-29 01:05:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9566f7d6-4bb5-358f-8026-ca78137f941c | -15.88372 | -45.04586 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c10734ef-7e8a-3e41-bb2d-c3192ed9dd4d | -15.65293 | -47.22766 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8e771843-037d-34d5-a1c1-ea2f1adc9dd9 | -15.63473 | -47.23048 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c37108c0-9be5-3479-934c-d26dc9263a72 | -15.43642 | -47.44857 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5fd4875e-32f1-380c-bbab-d80a1631e582 | -15.43503 | -47.43896 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a4aea1cc-4532-3917-8205-6366a1a5b87a | -15.38982 | -47.4462 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5e74a3ff-1777-3628-940b-d520d793af10 | -15.38076 | -47.44753 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b90474df-b551-3906-b4ac-4e14c0d46b8a | -15.15812 | -47.37214 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7014a516-5046-3475-9cff-b9f8af918299 | -15.15671 | -47.36246 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 008b750f-fa18-3f16-ae2a-681e72b00d7f | -14.5779 | -45.74404 | 2024-09-29 01:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 63472572-a15e-3b6a-99d0-85bd466fc7ab | -14.57605 | -45.73228 | 2024-09-29 01:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 89aa317b-4532-3192-b1e2-8ac1551877a3 | -14.57422 | -45.7206 | 2024-09-29 01:05:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| db5f15fa-f33e-3a00-bf92-80e3099637b9 | -14.56982 | -45.75753 | 2024-09-29 01:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3a2c90cf-0208-34dd-909a-cdb6ac8d4f00 | -14.56835 | -45.7517 | 2024-09-29 01:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c50ba3ed-8f67-3ab0-861a-0ff33c4464d3 | -14.56798 | -45.74579 | 2024-09-29 01:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 15e28d67-2c3e-3b46-9d51-ddc57857f0ff | -14.56657 | -45.73991 | 2024-09-29 01:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 04c5c464-cab9-37d2-9e12-2725c1c72cde | -14.56612 | -45.73402 | 2024-09-29 01:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 10d8ef87-9537-3670-8425-719873b6bf05 | -14.48059 | -45.24367 | 2024-09-29 01:05:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 5cadb29b-dafd-3fc4-bd5c-f348879042db | -14.47866 | -45.2311 | 2024-09-29 01:05:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e03a97a0-04fa-3f49-a1e5-7290e77f9e12 | -14.47029 | -45.24532 | 2024-09-29 01:05:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 33c872a6-fde7-32af-8a37-ded63c264b66 | -14.39229 | -45.20015 | 2024-09-29 01:05:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2394726a-dcb9-38d2-9673-308da0755ed9 | -14.36769 | -46.04342 | 2024-09-29 01:05:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0786eb87-1f71-3f14-acc7-3fe7f63ca686 | -14.18746 | -44.24745 | 2024-09-29 01:05:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 94babde0-8f1d-39a9-9910-52d6ad35e2fc | -14.17337 | -46.45479 | 2024-09-29 01:05:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f52b4e9c-71a3-39d8-bf61-0b5eacc82d54 | -14.17177 | -46.44421 | 2024-09-29 01:05:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 964c7dd4-821a-35ae-ab50-7f9e084532da | -13.89833 | -41.67333 | 2024-09-29 01:05:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 88c9a6c5-389e-3dba-bb75-0f49a391c29c | -13.78831 | -44.34846 | 2024-09-29 01:05:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 7ee51bee-d5fc-39dd-9760-072f9d7ecef8 | -13.78812 | -44.34283 | 2024-09-29 01:05:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 35c26678-0fcc-3031-8434-19f247549a10 | -13.47275 | -48.59896 | 2024-09-29 01:05:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 36ba54a8-e265-33c4-994f-5b8190d0d01f | -13.43828 | -44.03203 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d83f94bf-78ca-3895-a267-9e8353db162d | -13.3624 | -46.31593 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0d3fbc16-827e-3e79-9396-4daea10c630f | -13.35264 | -46.3175 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5442337b-cdc3-353e-b5ab-d5e66261c700 | -13.35098 | -46.30647 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 378322c9-3836-3dbb-be6e-72330b8cd9e0 | -13.34974 | -42.06552 | 2024-09-29 01:05:00 | TERRA_M-M | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 30.0 |
| 17b4e6b1-91ce-3b4f-b408-d3b043022323 | -13.33812 | -46.35389 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d6f2dded-3559-3c52-8399-77f5449dd09d | -13.25543 | -46.35114 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3c310d20-8dbe-3a01-9573-8ae24bf766cb | -13.24567 | -46.35269 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 6c9e4a3a-1042-366d-818d-fe2386d46696 | -13.24401 | -46.34165 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0c99b14d-91a9-3b34-988e-321accf34a9a | -13.24241 | -46.33108 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ceba3157-9f21-3748-9f69-028fbd30f7d1 | -13.23592 | -46.35429 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ebf4afdd-a215-3b50-8a51-c93c1bfd60ec | -13.23424 | -46.34317 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b69e5fb5-b299-3c61-8855-f046ee0cdc9a | -13.23259 | -46.33226 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1b1c3241-336f-3b10-8d9b-1389e7e5dfa4 | -13.23101 | -46.32183 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 67d1e4b7-6c86-39eb-b058-7396c93f9745 | -13.1647 | -48.50536 | 2024-09-29 01:05:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 24fdb70e-02e2-33d5-945e-f0082022251e | -13.15712 | -48.51602 | 2024-09-29 01:05:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c56bb513-7253-38a2-a313-fbf9bde2ed08 | -13.15579 | -48.50673 | 2024-09-29 01:05:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| ee948a52-df40-3bff-904e-8ce75e9a64f5 | -12.81924 | -44.85 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 010da488-36a8-33b9-9165-0a9fcb5b63cd | -12.81701 | -44.83585 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| a0e8a1e5-2b12-3830-9765-6e1b86ab859b | -12.81478 | -44.82166 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 83032771-51dc-31d0-9021-855b8945291f | -12.80834 | -44.85183 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 77ef08f5-72dc-3e34-9142-101f4c5e9244 | -12.80385 | -44.8235 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 00b4fc9b-fa9a-34f5-9c51-5f6423d55477 | -12.8016 | -44.80928 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ad32d963-1193-37aa-b14c-45401c6c1e4e | -12.59135 | -43.84579 | 2024-09-29 01:05:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 78f39ab4-0ed7-3ef8-8cc1-a157b6395ede | -12.58865 | -43.82887 | 2024-09-29 01:05:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 0532af53-f2a9-34f8-aaf1-eeb1f929bdc9 | -12.57952 | -43.8478 | 2024-09-29 01:05:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a0c0e695-464d-34c2-b908-b0d81a55fb03 | -12.03546 | -45.73891 | 2024-09-29 01:05:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ec4d0a28-b9bf-3f4a-a2ea-1203e75c45cc | -11.91695 | -45.5673 | 2024-09-29 01:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 619d7982-d8f3-31fc-a891-f4d8de745f29 | -11.91494 | -45.5543 | 2024-09-29 01:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 76221397-b6a9-35e5-873e-cd0f10a6c1a9 | -11.89594 | -45.57069 | 2024-09-29 01:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 68e46bf7-fb5e-3bfc-9277-0bf9e54e50cf | -11.88337 | -45.55916 | 2024-09-29 01:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 25a98777-961a-371e-94e5-bd07d8bcbff2 | -11.88022 | -43.81694 | 2024-09-29 01:05:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| f8cb18fa-2618-3f6e-a2c7-e87de58199b8 | -11.87572 | -43.82339 | 2024-09-29 01:05:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| f22a00ae-803d-3c52-a10d-6c4b35dc5db3 | -11.17434 | -45.53348 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8308cfef-b38a-3a16-b2e7-abac3ab41e41 | -11.11886 | -45.63204 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f0f2ac1b-3e0a-31dd-9046-44f497e1c448 | -11.10828 | -45.63385 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 504f0ded-6336-38bf-8dc2-81be5f19be29 | -11.10009 | -45.5803 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 4c3a38d3-205a-3814-beef-5887f37e8af2 | -11.09802 | -45.56676 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 80085a82-3cdc-370f-a0ae-d6e786ab7491 | -11.09769 | -45.63557 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 68e813ad-46b0-3698-ac7f-ec3d1cf4bcf5 | -11.09178 | -45.52605 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3ae5082f-2eb6-398e-a183-862e10027adf | -11.08112 | -45.5279 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 98d16829-0820-3052-8a4b-29446f2dbb8c | -11.08084 | -45.5968 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6b1349b1-be7a-3d48-8663-3e0b946d0f0a | -11.07902 | -45.51429 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5c21500c-48bf-302a-b557-ddd97095fc3f | -10.85901 | -46.02128 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9f1f0897-c50e-3067-8a10-183ea1041fbd | -10.8571 | -46.00887 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| f6d41f17-6cc9-34bd-bc37-8e07a702fb1e | -10.84864 | -46.02276 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c2a6b952-d3dc-3414-9437-cb9da3706e30 | -10.84671 | -46.01033 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b240aec7-e625-37e0-aac9-c1453e6fcd26 | -10.65864 | -44.51414 | 2024-09-29 01:05:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| dbaf855c-9f67-3850-a412-7a7a7a845bee | -10.6561 | -44.49789 | 2024-09-29 01:05:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 4b4b1124-e26f-3cba-b670-9d195305b58e | -10.26083 | -43.5801 | 2024-09-29 01:05:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d0e7b196-9b9e-3984-8203-74778fffb3df | -10.25171 | -43.59531 | 2024-09-29 01:05:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9dcbf040-e6c1-3d6d-a8b7-44618c0c3d26 | -10.24843 | -43.57557 | 2024-09-29 01:05:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 5e185d8c-f6c5-3281-adfb-0e67ad633e6f | -10.2482 | -43.58233 | 2024-09-29 01:05:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| bdf64828-9e20-34bd-a0ce-d5c36470ce04 | -10.15807 | -44.92252 | 2024-09-29 01:05:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 3cc34702-31da-321d-bd9b-1ce598085197 | -10.15565 | -44.907 | 2024-09-29 01:05:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 2e916732-b143-308d-b093-e0f6429273e3 | -10.43748 | -48.19665 | 2024-09-29 01:05:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 069067bb-0625-372b-8020-0de99bb9eea1 | -17.12333 | -56.22351 | 2024-09-29 01:05:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.0 |
| d75af40b-52b5-3a11-aebc-99c31e917ff0 | -17.12078 | -56.19823 | 2024-09-29 01:05:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| e0316202-3590-3820-adb7-03cb10ddc865 | -17.11893 | -56.23071 | 2024-09-29 01:05:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 00a03c18-e676-3297-a8d6-e80431ae103c | -17.11824 | -56.17305 | 2024-09-29 01:05:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.6 |
| 72317423-4469-35b2-b6ff-2a7303a99847 | -17.11622 | -56.20547 | 2024-09-29 01:05:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| fa2bf4f9-0d0a-35cc-b360-d19395d32fea | -17.11351 | -56.18031 | 2024-09-29 01:05:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 252ca427-0fce-31fb-afc1-16f6e45bc269 | -17.10922 | -56.22508 | 2024-09-29 01:05:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 0028d50e-765d-3ecd-9402-d677d26d96e1 | -17.06613 | -56.13503 | 2024-09-29 01:05:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |


[Clique aqui para ver as próximas entradas](README12.md)
