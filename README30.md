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
| dac82ce7-16ef-36b5-b918-72ebad307f2c | -17.83032 | -44.45395 | 2024-09-28 03:30:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ede05b70-5ff9-3c40-8afb-62d2f5e3ea70 | -17.81546 | -44.47082 | 2024-09-28 03:30:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f69d8bfd-4836-3af3-8e01-7a7f41951df0 | -17.80042 | -43.27578 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfdf8167-5ecc-35e9-b02f-834a9520c7f9 | -17.7967 | -43.26828 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| beae775d-fb25-30d1-a3af-497bbee4bae0 | -17.79608 | -43.27135 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 312f1fb2-99c1-3c2c-a183-81bf19c0ae19 | -17.79546 | -43.27443 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74a9c108-912e-3608-8be2-7f2d995a815a | -17.79168 | -43.26723 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d94ce14a-3bd6-3b02-a388-3c945a77297e | -17.79106 | -43.2703 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0565024b-ed41-37e8-a2d5-fcf2747762f2 | -17.79045 | -43.27335 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44f9e084-2d03-3021-a7c9-71fc6f1a667f | -17.78983 | -43.2764 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d10afea8-0d2d-341e-90b7-d7009266f021 | -17.78922 | -43.27945 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 073bcf93-7eba-3de6-a5e5-7f7973aab523 | -17.7886 | -43.28253 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b72d3aa-9259-3c90-97e6-1126d99814a6 | -17.78798 | -43.28563 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28606113-7a18-30b4-b3e7-d187d303d5ec | -17.78665 | -43.26622 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc7d5893-c486-3536-bfff-96b835f14413 | -17.78605 | -43.26921 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26664c66-0689-341c-93b1-7fc371e84a59 | -17.783 | -43.28436 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc0b3f83-4d8b-380c-a42d-dfcea8f34186 | -17.78238 | -43.28743 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d52f4d4d-dde2-33f0-bc1c-8afa531308ec | -17.78226 | -43.26202 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd00b1f3-da6a-3d90-8de9-3e1229b73a70 | -17.78176 | -43.2905 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc052616-092e-363f-96c9-fe735927b47f | -17.78167 | -43.26498 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c4089e5-add3-3933-8301-3a257ead250b | -17.78107 | -43.26792 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6fb5801-47d2-3bf9-9730-77bb7c91109b | -17.77784 | -43.25802 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 91ae1100-2a33-3192-a2a8-745a97489fb1 | -17.77725 | -43.26095 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ad85957a-3ea7-3d27-a7ce-3fa6e136d360 | -17.77665 | -43.26391 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2972b83f-cbc7-384a-9c59-d1f4c39c00bc | -17.77604 | -43.26691 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87334fdf-fb7d-3a9c-824b-ea65f268cfb5 | -17.77343 | -43.25397 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2d886d76-ed93-3e90-871c-486c20289659 | -17.77281 | -43.25702 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2dcfa631-e344-37e2-afbd-d0d278115c53 | -17.77221 | -43.26 | 2024-09-28 03:30:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 470f13da-f544-3ae2-95cb-0d6eb4a2bcaa | -17.37318 | -43.13248 | 2024-09-28 03:30:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7564f47a-4fb0-3ff3-aca7-67ec9fce79fb | -17.37254 | -43.13569 | 2024-09-28 03:30:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d3e7b9b-45ff-3925-88e9-aa0ef3998db1 | -17.04206 | -43.23568 | 2024-09-28 03:30:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e82232e8-29d9-352f-96ef-04ce13db5fba | -17.04147 | -43.23861 | 2024-09-28 03:30:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d294cef5-7c0a-3719-b3d2-d532db2147a5 | -17.03758 | -43.23161 | 2024-09-28 03:30:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97960600-7550-34d8-94da-31cbabfdd2c7 | -17.03699 | -43.23453 | 2024-09-28 03:30:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df195760-1347-359a-ba25-c0461914dcc1 | -18.01695 | -44.32311 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 328f9850-7e73-3947-ac15-3517cf1d284a | -18.01163 | -44.32186 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 764255ea-260d-3eaa-8145-d76d861337c7 | -18.01084 | -44.32567 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fd6f90c-e59c-3277-8ac8-c1585782f246 | -18.00558 | -44.32412 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7671c61-baa0-3202-8f26-8d45dd197a95 | -18.00481 | -44.32784 | 2024-09-28 03:30:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 213f7264-af07-30db-8a6e-0a32cc379e96 | -13.45046 | -44.42738 | 2024-09-28 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3e39e9d-7c14-324a-83e6-f065c75908bd | -13.4493 | -44.42511 | 2024-09-28 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29d76031-e0a9-30ec-9617-7aef812bdadf | -13.44753 | -43.77697 | 2024-09-28 03:30:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1661b60f-184c-317d-9dcc-4b203b6dd8ed | -13.44676 | -43.78087 | 2024-09-28 03:30:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0fb3cbc-e88f-35bb-955f-889d9898df38 | -13.44377 | -44.43041 | 2024-09-28 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce969124-0f34-39ad-8503-5438fc95a590 | -13.44255 | -44.42828 | 2024-09-28 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49e6ddcc-0c7a-3974-ac60-86d0c06e537a | -13.4357 | -44.02318 | 2024-09-28 03:30:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5c334970-aecb-3f9f-955f-c5eb2fdd950f | -13.43431 | -44.02314 | 2024-09-28 03:30:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84a41e4f-4e42-3833-acb7-c921d681425d | -12.99496 | -44.74178 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7eb60edf-2f1c-323b-8b97-6ed7b2f993d1 | -12.99402 | -44.74636 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25a8968f-27df-3e8c-9c4f-f497a1f1920f | -12.73915 | -43.4707 | 2024-09-28 03:30:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68894b77-53b1-3f48-a212-667d3e9ad86f | -12.7384 | -43.47453 | 2024-09-28 03:30:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 766ebe3d-7c42-3d1c-8ab2-a645f4de4846 | -14.45531 | -45.20966 | 2024-09-28 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53150bed-57d4-39ac-8eb9-f9881a0111c6 | -14.44932 | -45.20827 | 2024-09-28 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5b44b0b-83f9-306d-ae84-dd2d47c62e59 | -16.89512 | -45.33404 | 2024-09-28 03:30:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19a8ca1e-129b-3f05-8711-33b5a775d1c7 | -16.8854 | -45.32272 | 2024-09-28 03:30:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0648cf8c-e306-3b0b-99e5-bf6a92ac027e | -16.88449 | -45.327 | 2024-09-28 03:30:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf42591f-2140-363d-ac5b-83dc4b0d18ce | -16.87871 | -45.32563 | 2024-09-28 03:30:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ac83868-fd7c-39bd-9fe7-6afb6b7ef17f | -16.87779 | -45.32993 | 2024-09-28 03:30:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11317d71-dc1e-3765-bd9c-438c06688e22 | -16.87292 | -45.32429 | 2024-09-28 03:30:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 647b3b4a-e397-3829-b887-56b70c6343e0 | -17.77303 | -44.59045 | 2024-09-28 03:30:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 768cb40d-c3d8-318e-b150-edfa0db0191b | -13.33756 | -46.30343 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a0f45fb-f8a4-3823-a3e0-017693b62f2d | -13.33628 | -46.30951 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51195204-630e-331f-82d0-a717b7473f08 | -13.27923 | -46.33007 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 18ee7c99-6608-333d-b7dc-ce8830099fe0 | -13.27776 | -46.32703 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1e3a7a05-5183-3fc4-b490-f295f6e4a2ab | -13.27648 | -46.333 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| bad03c91-a9bd-3fe1-80bd-a2b3b555e05c | -13.274 | -46.32229 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f8d83486-4fa3-3504-b196-d6af2accf5fc | -13.27273 | -46.3284 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 25037536-30b5-3242-a306-000188af9223 | -13.27265 | -46.31889 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 877b4664-b0db-39bf-b81a-e673ae9dce28 | -13.27149 | -46.33435 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6856b5f0-d454-33d5-b2e9-7e7601dffa0e | -13.27127 | -46.32532 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 810a023c-d6cd-39de-90bf-a9b92e03eda5 | -13.2703 | -46.3401 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c28cbe37-ebe5-3f54-8c36-9a3c9c2d07e7 | -13.26999 | -46.33127 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1f364360-3c0b-3a93-bfac-46aacaf5cb53 | -13.26875 | -46.33704 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5b98b437-5b78-32fc-92ae-7b950656a593 | -13.26754 | -46.32039 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d2fb248b-4fb9-34dc-9af7-ebd7b327e98c | -13.26627 | -46.3265 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3ddf5517-11e8-3048-b047-8024cae100e0 | -13.2662 | -46.31699 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1b176723-84df-3ae1-aa78-f3d086e0cfd4 | -13.26507 | -46.33227 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f6d38104-3373-3846-b70c-6e6045615a17 | -13.26481 | -46.32348 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 54fa3d5d-787e-3c0e-aabf-0714731e8c35 | -13.26388 | -46.33796 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3cfd9ee5-dea9-3a36-90df-cb3154f43b8d | -13.26358 | -46.32918 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 217e0c3b-e4ae-34fb-bacb-7ae3a140cc77 | -13.26264 | -46.34392 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| accefe54-7b0a-3a52-a8e2-f469e39ee74d | -13.26238 | -46.33477 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dcf0d8f9-5693-3f20-b460-34a7d1216565 | -13.26147 | -46.34954 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47d4b217-c243-3235-a612-ab60df5c670d | -13.26122 | -46.31783 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cf33e55c-d93c-3051-a66e-151cd2381007 | -13.26115 | -46.34048 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0f6f296-6bfa-38b5-8374-06fd1518f9ab | -13.26031 | -46.35508 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8146803b-571f-3d28-b356-ec2ae2a030be | -13.26007 | -46.32334 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 67616f9b-26a7-3a7f-8b24-460e3cffbfc8 | -13.26002 | -46.31385 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 324e9d32-3ab6-336d-b133-a553a02c84f3 | -13.2598 | -46.34672 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 194b7755-3bd8-359b-9d2f-f52a0abbe8e8 | -13.25901 | -46.32842 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 341.3 |
| 71a8859c-a54d-3116-b842-efeca0e7e05c | -13.25877 | -46.31967 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 5097b3ba-cc27-3177-8ff0-760a18c5ff9b | -13.25863 | -46.35217 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 89312545-4010-3eb2-b501-a1e4ae24b72d | -13.25765 | -46.32483 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 4232c42b-d6e7-3c90-8ceb-1b0754d435f8 | -13.25735 | -46.3581 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53c6ba4a-00c4-3091-a06c-d72881d7e462 | -13.2564 | -46.34092 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 152.6 |
| d1adb42d-a102-3f81-8427-ba66726a5446 | -13.25545 | -46.31264 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7b8a1c6c-776b-3990-aae4-689cf2e24804 | -13.25493 | -46.34799 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 152.6 |
| b15e1e48-9a41-36f9-86c9-d54ea3f97dd0 | -13.2542 | -46.31858 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7e351440-52e8-3f41-8279-fdc3bcfb93a0 | -13.25376 | -46.3536 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4e42e9b-a367-3692-88b4-8a4ef41321a3 | -13.25338 | -46.34465 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |


[Clique aqui para ver as próximas entradas](README31.md)
