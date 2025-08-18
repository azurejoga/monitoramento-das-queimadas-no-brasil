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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eedcf7cb-db65-382f-8fe7-6b3e4b5dc302 | -13.21379 | -50.75595 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e9aba325-5ae7-3530-b5d8-7d1ec2a0086f | -12.5343 | -48.50136 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b981f75b-18a4-3f60-b496-6cdedac989ff | -17.62746 | -39.92928 | 2025-08-18 03:55:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58a671fb-cbfe-336d-93d8-3df431b2a6a5 | -13.21942 | -50.78781 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b16449f4-100a-3e4a-85d1-ce7b9c23219f | -13.23279 | -50.75134 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbcc176b-8f17-3791-bb98-12226b718f7b | -14.53007 | -39.73466 | 2025-08-18 03:55:00 | NOAA-20 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 53e0ea4c-ce17-3abc-80eb-17dcc0735794 | -11.00265 | -45.65338 | 2025-08-18 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd84460d-04f9-3a95-be59-20ae3eeda0e3 | -13.86346 | -45.54533 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3707ba28-fbed-342d-8bab-92137402a845 | -12.13532 | -47.90382 | 2025-08-18 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60c0cb0c-f8cc-3ea3-9f59-49c0e846886f | -12.54366 | -48.49718 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 027a9860-767e-3f00-8438-287b82846923 | -12.63206 | -46.8907 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fff92cb8-721d-35a5-8df7-1efbde056d03 | -13.21956 | -50.75721 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b8e23131-27e6-3ce2-8150-6f29523a7e0d | -16.73981 | -45.00091 | 2025-08-18 03:55:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea4d24ba-dba4-3f9b-9312-1f4749459c92 | -13.46806 | -47.07035 | 2025-08-18 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a26fd09-b3b1-326b-9b2a-41b50cbe42ad | -12.62034 | -46.90137 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4abc6e6-a52d-3832-a6ec-471d76ea9afd | -13.97844 | -48.10113 | 2025-08-18 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de5e3c79-d285-3326-b02c-b0bff879b15f | -12.72973 | -45.05166 | 2025-08-18 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39160dce-de8d-32b2-ab54-e978e15b1615 | -13.59878 | -46.89296 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be2fd0d6-c64b-3682-b1ef-fc19fabca5c3 | -13.86886 | -45.53881 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 062388ae-fd93-36df-ab58-cf05e0421f0b | -14.17961 | -45.32194 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72bcea0e-afb4-31cb-a2b4-93c98b1604d0 | -13.44475 | -45.88502 | 2025-08-18 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e436918-f367-34ec-a082-f85009c54787 | -12.12542 | -47.90236 | 2025-08-18 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad1ae886-4657-357b-bb2e-c47746ed2737 | -12.3129 | -44.75827 | 2025-08-18 03:55:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7be2c6a-113f-3402-9a6a-7cf053c5c15e | -10.9991 | -45.64841 | 2025-08-18 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5f3dac4-2577-34cb-b67f-75e530c8cf31 | -13.73726 | -42.6832 | 2025-08-18 03:55:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| acfa02fa-aef8-372b-8d62-83bca9815718 | -13.8682 | -45.54247 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ba3d02e-acf0-3cca-b1a3-6576a341ef7c | -12.54308 | -48.50019 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af4fd982-8ff1-3e60-bc1d-61f7849ffd62 | -13.57576 | -47.00103 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7ff959d-4ef9-3d4b-b2a3-89b09c642792 | -13.21872 | -50.76139 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b4ad8fb6-431d-38ee-8bee-d80686b8fbd5 | -10.02742 | -44.31628 | 2025-08-18 03:55:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07294e2a-2921-343e-8d3f-93fd284b95fe | -14.17751 | -45.31042 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed66d1a0-a912-3ff4-8ffb-2ea6c6bf0088 | -11.79998 | -44.94186 | 2025-08-18 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c8819d3-f5d8-33de-9530-8ef372cd897a | -14.17205 | -45.29466 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10291cab-2fae-31f0-b7d8-afb2e0c6a59d | -9.86504 | -44.69706 | 2025-08-18 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3c3e0b9-0ebd-3ea8-b530-dec139f2f3de | -11.91147 | -46.75129 | 2025-08-18 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba221a7a-54d3-368e-a10b-63966ba7d74d | -12.5425 | -48.50322 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1258573-ea03-3785-9ed8-74ccaa94b7ba | -13.60061 | -46.96813 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e37dcf27-0340-3195-b59c-7a8226005ec7 | -16.67791 | -41.36124 | 2025-08-18 03:55:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f6d226a4-5983-3660-b163-6e97494b788e | -13.8804 | -45.54496 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cde8bfd-c6de-377d-af93-2f049f5bf57d | -14.17897 | -45.32555 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09df34b8-9698-32b1-8d94-f2bb5b421432 | -14.62918 | -54.91257 | 2025-08-18 03:55:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 19b56950-3c9d-3477-9ac4-184f0302eb83 | -12.61031 | -46.90479 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 048cebca-b21f-33ac-904f-c7d1b67560c8 | -16.73604 | -45.00016 | 2025-08-18 03:55:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6b6dade-f466-3c72-a983-ac1a5f0c5555 | -13.24749 | -50.79832 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a8041ff-bd51-3e09-9094-aa3fd483186c | -13.87227 | -45.5433 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f6d93ee9-25c6-3a29-bbe4-cd4073b73924 | -9.17453 | -49.66994 | 2025-08-18 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6faebf70-9670-3b6d-b1b7-84e38f3a169b | -13.61105 | -47.77237 | 2025-08-18 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f39a4f8-9e54-3672-ac17-cb469d56eaca | -16.23481 | -45.63663 | 2025-08-18 03:55:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c71aae48-cf80-36e5-bb5d-4f3a6d7e710d | -16.07754 | -43.62574 | 2025-08-18 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a8130b1-87cb-3a08-8951-acb13229aa4a | -15.76559 | -47.79719 | 2025-08-18 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd94d427-d096-3259-84bd-01dc3eb80707 | -13.5903 | -47.75214 | 2025-08-18 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e80e954-1315-3c83-afa5-403edb870c5d | -13.59135 | -47.74659 | 2025-08-18 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7d1a47d-335b-34de-85b5-6cd31ae9585b | -11.75112 | -51.71093 | 2025-08-18 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b397700-39ed-353d-a111-5d590932033f | -12.73104 | -45.04836 | 2025-08-18 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b6f1882-4cc6-33af-9a61-31afd0110cae | -13.62331 | -46.89654 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98254ab3-3093-386c-8e01-8f18e7a26440 | -14.16787 | -41.58524 | 2025-08-18 03:55:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 0b5650c3-ee23-3c73-a349-5f1edd4b468d | -12.61551 | -46.90355 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 175f054b-53c8-3824-903a-050113f53d8a | -13.21857 | -50.79201 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64e0205b-257c-33c1-be0c-61f07911a2d8 | -9.87395 | -44.6948 | 2025-08-18 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aeda0b83-da95-31a7-a2aa-cd2d6446382d | -13.2121 | -50.76432 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 034a3b50-62b0-3503-862c-a3d774f90bb0 | -12.63487 | -46.9009 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09f748b9-7bc3-3f5c-8700-8fb6c442ed77 | -13.22026 | -50.7836 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4adf7d68-dfe3-3ed0-b40c-0f640806c7b1 | -8.78159 | -49.99792 | 2025-08-18 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a929c4f1-6d9a-33bb-b23a-af407f36e472 | -13.46896 | -47.06558 | 2025-08-18 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21ac825f-9fc6-3acd-aa8a-3d6c2b1789bc | -13.575 | -46.99855 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1c82c36-1017-3c44-9e0e-2c8a823a64c3 | -13.97746 | -48.10631 | 2025-08-18 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4975ac90-7336-3053-8666-14f45e366a3a | -9.52297 | -45.18633 | 2025-08-18 03:55:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34046190-fb49-33fc-8f1a-f7eb2b9f33d0 | -15.87066 | -50.20983 | 2025-08-18 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c9fed3ea-1cb8-3070-8bbd-375fcbeb2ce6 | -11.80469 | -44.93895 | 2025-08-18 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 717c4015-e7b0-3f97-b1e2-a39a336c411c | -13.2311 | -50.7597 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fa95c0f-86bb-3bdc-bf65-0ecf3671d21f | -13.86753 | -45.54615 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f78e93a6-5f12-3f1a-b526-477a6a109f45 | -13.60286 | -47.73759 | 2025-08-18 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf6c80b5-a6a2-3a17-91dd-9e59701c04b7 | -10.85797 | -48.46928 | 2025-08-18 03:55:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fed0666-ed6f-3893-a71e-0edcc72c6167 | -13.42126 | -49.1403 | 2025-08-18 03:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25e9e212-dbb7-3748-bb9c-006775712847 | -13.58778 | -46.98682 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b39b2605-3646-3d59-ae1f-ce327262a692 | -11.7501 | -51.716 | 2025-08-18 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b60f2895-d0c3-3237-91ec-a52a25d5286b | -12.53301 | -48.49783 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ba3dafc-424f-3312-9084-ca4b0ace3fff | -10.99785 | -45.64548 | 2025-08-18 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f482f6f1-add8-34c8-a9cd-0cbddcae47cc | -12.5336 | -48.4948 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05819e1a-597a-349a-b7a9-dc7c9bc09a58 | -13.43661 | -45.90445 | 2025-08-18 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7864d7c-3549-3e52-bb2a-3668508d2705 | -10.99835 | -45.65257 | 2025-08-18 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9237cc74-16be-34d5-b5ae-49172a5f1a1d | -12.6267 | -46.91938 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40573dec-354a-3e32-9dc6-8e9a510861fa | -14.1817 | -45.33349 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59c7acca-3dcf-3241-b1e0-1b12252b2c4b | -13.59516 | -46.97234 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1dd01a2-3cea-3de6-acbb-df315f658be5 | -12.6109 | -46.90297 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dafee5e-0bd9-3ebc-b1f7-9ac2091dd104 | -9.87051 | -44.69022 | 2025-08-18 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| debb4c21-f073-30f5-b81c-ef0ace03d2e2 | -16.70899 | -40.45486 | 2025-08-18 03:55:00 | NOAA-20 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3bcb08ee-7e34-3808-aa5e-f2ae80391ef5 | -15.24902 | -49.52675 | 2025-08-18 03:55:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a29bd779-fc57-3abe-a410-34c0af450f9f | -9.26615 | -44.53955 | 2025-08-18 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e28b6f08-8c5f-3b78-83fd-0e57a15b7515 | -14.18214 | -45.30764 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 470b8507-7330-347e-a8a7-c13f5a787136 | -15.96601 | -43.89956 | 2025-08-18 03:55:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f23bf49a-d58f-3f0f-86e4-0c11858389a4 | -12.53545 | -48.49517 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fcd82e3-985b-344f-a00e-8b44c7c0e315 | -14.16727 | -41.58892 | 2025-08-18 03:55:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 55819ee1-b749-3109-b31c-f22c5e89910e | -15.49603 | -48.5284 | 2025-08-18 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a455c6b0-d446-33b1-a444-d87bfa8bab19 | -11.80063 | -44.9382 | 2025-08-18 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7522e2c-5e91-3eec-b570-ddb77f3a7dd3 | -13.22209 | -50.74466 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4f99b765-311b-3b1f-94a3-1cc654eeb1ef | -10.9964 | -45.65382 | 2025-08-18 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ac91e80-39ad-30d2-b1a9-8558aad1cea0 | -12.62098 | -46.89952 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32905771-0f16-349d-8db6-b823159737c0 | -15.64726 | -49.25572 | 2025-08-18 03:55:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99c6bb1f-eb01-3379-b446-0be2b57b30fa | -13.59334 | -46.982 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
