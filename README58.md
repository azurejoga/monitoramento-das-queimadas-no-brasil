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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1e6f93f-e802-3ed4-a034-fc2976f3e9c6 | -18.98179 | -46.93305 | 2025-10-06 04:29:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1268388-4f19-3add-9d3b-c39bedfd6cf2 | -18.0238 | -45.00144 | 2025-10-06 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fbd588f-97e2-3716-b281-311031aac2d7 | -17.85578 | -57.63673 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e9ea7260-f85f-3ddf-9947-39a3fc97bffa | -18.19648 | -53.36867 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8acf74a-9c1a-3899-8bc8-3507b41d6b48 | -20.11791 | -44.4073 | 2025-10-06 04:29:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 89c287b9-430d-3ff5-83b4-e8171773789c | -17.96637 | -57.60364 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fcff6eab-edba-31c5-9ea0-0a1839b5cb31 | -17.97744 | -57.59993 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6c0c2649-8491-3334-9d86-2b166d763039 | -20.217 | -43.64028 | 2025-10-06 04:29:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ba527d0f-f978-3813-8db1-56d800cb9e0a | -17.25227 | -46.91454 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47dd36cd-a080-3971-9d6e-5c4a9711ff98 | -18.00301 | -57.60103 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dd912104-2f0f-3d4c-8a09-7021e2b5589e | -17.99555 | -57.54109 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| f869b55f-dc1f-3551-935b-a606f064b7b5 | -21.70658 | -50.08057 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3a7c5ffb-560d-3258-8ff5-fc70fdaaaa21 | -18.13504 | -53.4091 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e2ad4668-fa17-3603-84b8-c6c0264456a9 | -18.27483 | -45.4282 | 2025-10-06 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07441b84-c6bb-385a-929e-38b73909fdf8 | -18.19272 | -53.36782 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edaa28e1-fedb-3812-9bba-a8926bbc837a | -20.91987 | -45.25099 | 2025-10-06 04:29:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7f293ee4-b01c-3763-89e2-31811a501579 | -15.88025 | -59.37498 | 2025-10-06 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea532e95-98ab-333d-9859-081588e41f1c | -18.11391 | -53.39539 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b5a23a7-a1b6-3802-b336-9bae8eb4fde2 | -18.13197 | -53.38211 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ad011523-7e43-3566-8750-4ac4bea1e620 | -17.96196 | -48.54906 | 2025-10-06 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1787401-32a5-393a-be68-c57101ba9192 | -22.36237 | -44.20933 | 2025-10-06 04:29:00 | NOAA-21 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 6504b6ee-e40a-37e8-8483-e2839418b38a | -22.95671 | -46.12842 | 2025-10-06 04:29:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ac2d37c1-f2fb-3206-9cc3-121fc63e49e0 | -17.97012 | -57.61069 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f52dafeb-6783-33b8-b4d6-e08c45dec4db | -22.57914 | -44.86513 | 2025-10-06 04:29:00 | NOAA-21 | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dba443ff-cbd4-35cc-8999-da206ccf3433 | -20.28413 | -49.19057 | 2025-10-06 04:29:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04f9c7ca-8f86-32b3-9cca-0b65531bd39a | -17.29401 | -49.27451 | 2025-10-06 04:29:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9c01ddb-754c-3cc7-8797-7baf2699e1de | -16.36732 | -51.49403 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bcd829f-361a-35ba-bdfb-c51206b50cac | -18.14159 | -53.39422 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bad20002-45b4-36d6-85b2-f9d1a3a5185e | -21.61082 | -45.29538 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b1f0acd1-0da5-371e-97a8-6c4b46a6de9d | -17.92276 | -57.6148 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0b4af74c-9c45-3cff-a4bd-a51bcd499677 | -22.44763 | -46.86136 | 2025-10-06 04:29:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 841a56dd-e534-3877-8a1e-f7bf25ccf93a | -17.9997 | -57.59564 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0b2110f7-ca49-3d28-8b98-44f4b30597de | -22.36491 | -50.0261 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a0640a32-aed7-3d98-9684-8635b8474e8c | -18.24462 | -53.36212 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5962c4da-e1de-36b5-896d-b811d3be43ea | -18.12254 | -53.39106 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0f172fbf-c3ec-3369-b32a-7bd8b2a4d2a6 | -22.86652 | -48.48671 | 2025-10-06 04:29:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f48e172-642c-3cd0-80e0-49f11136ff46 | -23.3997 | -45.38756 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 005be73b-602f-330a-8f74-59af0a53bc73 | -22.37325 | -50.01615 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 87fac80d-6ca9-3ad7-a3e1-3272f2b27f2d | -19.94448 | -44.64047 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 19c2e491-01c5-3712-bc5a-b750a06d82f7 | -19.48377 | -47.1671 | 2025-10-06 04:29:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15b68163-60f8-3451-a9b3-cc7e234d6be1 | -21.69511 | -50.06712 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7cbcfde1-3df8-332f-a9f4-eff1212763e3 | -19.94171 | -44.63109 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c5c67354-6cdc-3a7a-9a9c-de40ba1e3734 | -22.97464 | -48.34624 | 2025-10-06 04:29:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bcaeff69-98b1-3bd8-993d-a59cad407d27 | -22.15791 | -51.46268 | 2025-10-06 04:29:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0446850f-8937-337b-bfc7-0e1372ab553e | -15.99141 | -59.53549 | 2025-10-06 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 647c4d3f-c079-3ed2-94c1-ec491230e725 | -18.19849 | -53.37925 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9e6f36e-b8aa-3b82-a11d-5bb79ae6bf13 | -17.98731 | -57.60215 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a074172a-57a1-3de1-97c5-30d64f68581f | -18.00913 | -57.59619 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| bc36727a-8b68-39df-923b-423b027c3406 | -23.39192 | -45.38535 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 53ce70cd-b55b-3a11-9885-0730890881a4 | -17.84159 | -57.62998 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7ae910f1-56f6-3074-8a24-b43e43c69423 | -18.17768 | -53.36434 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7042788c-e9ca-3dbb-a3e1-2f329dc62c7c | -18.62294 | -50.67669 | 2025-10-06 04:29:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00a972d8-3304-36ea-a101-aed0ae170502 | -15.9935 | -56.01447 | 2025-10-06 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 482fde05-1378-39a3-b092-6b55146e7d85 | -18.4892 | -43.90987 | 2025-10-06 04:29:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27407b60-cf16-386d-9b9b-69c3bb722073 | -21.39267 | -45.0888 | 2025-10-06 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fcea462e-fd6e-3a64-96f0-e4b0bb8ae393 | -17.88996 | -57.6484 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9f162afa-a20a-3ac7-be3d-1eff54b17f8d | -16.15351 | -57.56698 | 2025-10-06 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| dcdc4fae-f539-39ac-ba5d-73c7f1733d7e | -21.61532 | -45.2909 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0749e235-2db1-3974-81dd-99423cf8e7fe | -17.9614 | -48.55268 | 2025-10-06 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6183a82-92e9-39fc-a897-57924d404bd0 | -23.19574 | -47.24227 | 2025-10-06 04:29:00 | NOAA-21 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6c80ecad-111a-33ec-bfa2-d287e098513c | -19.93586 | -44.64592 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0159cbe6-3e14-3803-a06f-e83bf2acd062 | -17.91809 | -57.61235 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f87a1ee8-6aae-3344-988d-49b488ec949c | -23.17537 | -46.26502 | 2025-10-06 04:29:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c6654374-77f4-3b6c-804b-c5f2eac445dd | -18.24806 | -53.34271 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b92143f9-e89c-3ba5-85ba-fc48fe786da3 | -17.67616 | -52.24291 | 2025-10-06 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 77b0a683-9d39-39db-8196-49251fe1fde3 | -22.5668 | -43.64342 | 2025-10-06 04:29:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dfda0a66-57d4-39c5-8418-a426b9c73634 | -20.00054 | -45.79162 | 2025-10-06 04:29:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ee77087-2c90-3c9f-8cdc-429dc803b898 | -18.27545 | -45.42365 | 2025-10-06 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b43af961-1b30-3944-857c-3acd30af88e8 | -21.39398 | -45.08498 | 2025-10-06 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 69132eb0-c41b-32e5-8093-8581e96af995 | -18.01078 | -57.59193 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 43ef4f8d-01f7-3d73-b844-9d430a65cdd5 | -19.89358 | -44.78551 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 689762f6-9c09-3e77-ab60-44bc4b60f0e5 | -16.36596 | -51.50206 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05f521f4-b2a5-3cdc-ae34-7c7b2bbd0bfa | -19.55072 | -44.10248 | 2025-10-06 04:29:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c08762f3-fdf9-37e5-b8f7-b645ee612cde | -18.13972 | -53.40483 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2e5efdb4-5640-3ad3-8bba-fff602b4fe67 | -17.9897 | -57.53868 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 0f40021e-ec58-33ee-b160-f3b2ab914f43 | -21.69472 | -50.04806 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f51ea0cc-0b6a-316c-ae9d-fa8dba280ec2 | -20.60192 | -51.40624 | 2025-10-06 04:29:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c79b1d87-a180-3e57-8427-35fafa6b7dd8 | -18.10203 | -51.83777 | 2025-10-06 04:29:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 628b154d-50e4-3f3c-a771-12313c329de7 | -17.96953 | -57.61364 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c5e901f1-a507-3466-9099-5fe72f4759de | -20.43021 | -48.85706 | 2025-10-06 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 334e5277-f6d2-3e54-8eaf-b85bc0e0ed02 | -18.0094 | -44.99498 | 2025-10-06 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb0ddcce-e343-3116-9bac-07ba7d6bdd17 | -23.43219 | -45.47999 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 148fdf1d-2503-3d40-adf0-de51467a63ed | -18.50954 | -48.34885 | 2025-10-06 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8e9f5c8-46b4-3c77-84df-d09d31c6241c | -18.59282 | -49.98813 | 2025-10-06 04:29:00 | NOAA-21 | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17d14f0e-1c18-31ba-86b4-303ae03a6159 | -22.70633 | -44.87307 | 2025-10-06 04:29:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5f10efee-ded1-3433-8c42-1ecfc7f1cce1 | -19.07569 | -46.82095 | 2025-10-06 04:29:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16ad9d9c-5edd-3b6c-ac0c-71718a08a918 | -15.316 | -56.92069 | 2025-10-06 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d721aa9e-8a38-35a8-a81d-699663d4cd35 | -18.24423 | -53.34223 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df3fc891-e133-33b6-9153-ee581b64d543 | -18.40854 | -46.76203 | 2025-10-06 04:29:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdfc8ab4-e3f2-3d9b-ac58-9b9ca584e8f6 | -18.54396 | -48.25706 | 2025-10-06 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aaa9eb8a-0016-325e-93ce-69c27849ce3b | -17.26646 | -46.91284 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4814b7b0-20c1-34cb-ab0a-0eb296f42686 | -18.24843 | -53.36264 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2019e04-ec5a-322d-b1eb-91d5599f8af5 | -15.99462 | -55.98339 | 2025-10-06 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7871d2d3-45d6-3eec-a6e9-bac9c5bdb6dd | -16.34468 | -51.45624 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d5f92cf-bb34-33aa-a5d0-de7b86161acf | -16.95107 | -52.67226 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d6c981b-cbec-379e-a8d5-b6f237903f6b | -19.02053 | -45.02554 | 2025-10-06 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 221fafb8-6afb-31d9-b085-89602bb5e3e8 | -17.87112 | -57.58604 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5c319681-201d-3224-be81-712eb584d627 | -17.53618 | -44.32 | 2025-10-06 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b189242-83a2-30d5-89bb-812c9f7f75c8 | -21.13453 | -45.11032 | 2025-10-06 04:29:00 | NOAA-21 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ed0e6e92-c24a-3ae7-8981-16edfb54e02a | -22.00691 | -47.32977 | 2025-10-06 04:29:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README59.md)
