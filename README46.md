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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3064fc6-fa57-3c79-80fb-bc4390fe4c13 | -13.08266 | -47.08048 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c20cedd8-c234-30df-94b2-295a29fd75c1 | -15.20279 | -48.16234 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee10db40-9365-3bdf-b418-4515d0b6b2dd | -15.17116 | -43.62596 | 2025-10-02 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 9.9 |
| d5bde365-9c95-3dd2-8c08-482ac12e9c94 | -18.87766 | -48.02489 | 2025-10-02 04:04:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b058f68d-69cd-3ae2-a272-5f2d5bf114e2 | -14.2999 | -45.96131 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8709e4b8-f5d4-3636-8f89-dc82b2354d80 | -13.16002 | -47.82577 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 25c773b4-7620-3703-83e7-df149f481984 | -16.04676 | -50.85785 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc27eb39-4037-332d-9bed-9286089e5047 | -13.30578 | -47.00161 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 821b78d1-be89-369b-9965-780cd4ba1cd3 | -14.18295 | -46.66815 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8918bb83-69b0-3b72-8756-e57c9caec563 | -14.69799 | -49.61979 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03be2e57-fc16-366c-8cde-e99c681cf884 | -14.32622 | -45.96648 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77b935da-b188-3406-b09a-64fb198297ca | -14.04152 | -48.00261 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a8eccb31-c8d0-377d-af53-3690a15d1c95 | -19.98065 | -44.2549 | 2025-10-02 04:04:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a1fd1eff-1a1c-3735-aff2-8636f109d383 | -14.31074 | -45.9883 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b99ee00c-d869-3473-89c9-6f3cf410a351 | -16.04119 | -50.85975 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d3871229-8fd1-368e-a5af-4c29186f4652 | -13.16135 | -47.82893 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5fd27819-190e-3574-b528-7a806a8d0457 | -15.9965 | -50.90112 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 4856fe5d-b497-31bb-a824-e0cea64a4e81 | -14.62087 | -48.30923 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2989051-8ba2-3b45-b062-4e99f6611634 | -13.15739 | -47.84048 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f4da678e-e5cb-338d-8293-1e86275fb78d | -13.74671 | -48.69297 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b36bb0a-1dbd-3ee2-a3da-a1476ce13e3d | -14.42773 | -46.36094 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d54fc07-67e5-3f91-aeb6-74afb119003c | -14.90077 | -48.0976 | 2025-10-02 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6bea1305-0797-3e32-907a-9f05bfb66f54 | -13.95384 | -48.10628 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82045f64-e7b4-3eb3-8983-f439ea3c9250 | -15.32054 | -46.29486 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83a62bde-2044-35b6-93e7-cac1ab1b456d | -14.59778 | -48.33139 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54fc5501-6418-3112-b5c5-0ded06274634 | -13.91126 | -48.06976 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91eb097c-37eb-3dfa-843e-1b2e1a0336d4 | -13.19373 | -47.84696 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa3a4e0b-c3b5-32ea-9cc8-70f72dde5b70 | -19.02225 | -49.74703 | 2025-10-02 04:04:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1b7ff3e2-03b5-372a-936f-ec0fb1f9af33 | -17.09229 | -48.56356 | 2025-10-02 04:04:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f685391d-d3e6-398e-8097-a0a76e7a20ce | -15.99349 | -50.91614 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b787467-4b2a-3f61-b161-3d8e4199cdb9 | -18.19744 | -43.57169 | 2025-10-02 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7cf9bb0-9065-3ed7-8c68-ed14bb1f4531 | -14.96774 | -49.96406 | 2025-10-02 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7092204-9cd4-3f06-9bb9-c8e991a2f09f | -13.77819 | -48.054 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c1492832-1fd1-333f-b28d-568c955fb940 | -15.92653 | -43.33407 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4830aa70-1fdb-3e01-815b-2c7093a2b187 | -17.02119 | -49.15072 | 2025-10-02 04:04:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f0ee782-e294-330e-9969-19149c6f7ecb | -14.61494 | -48.23668 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a418b1b-f04f-3e80-bb2d-6407eec14509 | -17.32289 | -49.38219 | 2025-10-02 04:04:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7756874-1818-3d9d-bf65-95884885bd34 | -15.25872 | -49.32022 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9d0dadbf-6782-3e6f-a885-5b4972120b63 | -13.74973 | -48.00589 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b99e23b7-5566-3eca-ac12-e25aa5b74f91 | -15.21117 | -47.99929 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 50a97cf9-e990-3030-9987-8abe2c1a5a7e | -19.95619 | -43.66599 | 2025-10-02 04:04:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9769d87c-3c65-3b23-aeff-fcae43b3751e | -16.58068 | -45.11838 | 2025-10-02 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 208be1c9-2c2a-327e-a469-556ea9735d48 | -15.93261 | -43.33886 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5513fafb-14a8-3a0f-b98b-6e23bfdbb04b | -16.61083 | -48.98901 | 2025-10-02 04:04:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec0b39cb-be10-31d4-a3e1-3875daaaf762 | -14.33042 | -45.98712 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 806efb98-246c-342e-a4ee-55168a51840c | -14.68505 | -48.10835 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 719ae568-4226-368a-8e9d-e50489afd649 | -13.95084 | -48.09814 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77cda1f4-65cc-3800-8efa-2445f346cc59 | -12.49837 | -50.24101 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d4baaf79-1dbb-3822-b130-c9ca9b9096cd | -14.40246 | -46.08705 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cecd17e1-cfa9-38e9-b9ca-a58c71c25de4 | -14.0302 | -47.99172 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de369ef4-2f9d-38a4-8c8f-b970d796405a | -13.57084 | -47.2792 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a36860dd-35b3-3ef7-8f17-e55b2ce20367 | -13.3146 | -46.9993 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2808a7e4-3fc2-3961-9c83-814db0a88f41 | -13.94716 | -48.09373 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a2ee0f5-5cb6-3995-bbf3-1d79d79ebc9a | -16.82073 | -45.37553 | 2025-10-02 04:04:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed2f3609-4645-3433-88b2-a9cc7cd53f50 | -13.67735 | -48.05136 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 516a21ab-004b-3a96-8d2c-988f6aeb4c77 | -14.68474 | -49.61228 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d13194b0-97a4-3216-b0c6-5c21528acfbc | -13.75321 | -48.70858 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a6ac511-07f0-3ca0-9aab-ee5d97bc3e69 | -13.08129 | -47.08832 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a62708f1-ce1a-3785-b7f9-11fba06c1bbb | -14.6838 | -49.61712 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae890c9b-9ba0-39db-a2d4-2ddeb32306af | -16.77503 | -43.03561 | 2025-10-02 04:04:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55bbabbf-dccb-3564-8198-28f95cb54177 | -20.13565 | -46.34307 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a74c831a-6bf9-3d33-9517-9092f4c1097b | -13.08332 | -47.07665 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23b18c1f-7327-36af-910d-d91b679445cd | -14.86282 | -48.30192 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9fc50ead-9d41-33fc-a2f1-d17152845b2c | -15.15788 | -48.40229 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46fa4859-0a76-3ad1-a345-9b4fde5efc58 | -20.22483 | -43.90202 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 64c45b70-e4d0-3ce0-bbaf-608bdbf9e8c6 | -13.16681 | -47.83764 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| da481565-4801-30de-b262-de275d847b5e | -18.14045 | -42.40287 | 2025-10-02 04:04:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7ab65d8a-433b-399b-a37e-70807dc15534 | -19.0106 | -44.99865 | 2025-10-02 04:04:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 098813bb-07e9-35e6-bbe2-52d1364aa579 | -14.86802 | -48.29803 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fa43b602-2268-33be-86da-0254daac8cf1 | -15.31849 | -46.28445 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7ff1f842-43e7-3a80-8a6b-c567de664f79 | -15.14651 | -48.39128 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c4feeb2-301f-3e9e-83f9-fb6a17fc272b | -14.59337 | -46.72235 | 2025-10-02 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 026d02f9-086e-3013-b057-7edc84d60d68 | -18.49741 | -43.39934 | 2025-10-02 04:04:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f30218c6-127d-3f2e-96df-193ec958f4e1 | -15.50039 | -42.55408 | 2025-10-02 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95ce470b-db01-3f62-83af-f86044342bd1 | -14.57911 | -48.31042 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a29102c7-4f50-3a82-8fd4-046508670cb4 | -14.03293 | -48.00097 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 364abf99-f8f8-3d08-a6b2-17ef91b042c6 | -15.21135 | -48.16373 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| febf6f91-457e-3561-8f7f-865d4d158bcc | -14.55008 | -48.22453 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa0dcb79-f0e6-3310-9c55-cdde5a5cffc1 | -13.56675 | -47.27821 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03b7eb6d-29bd-3552-843c-e794356706f8 | -16.36905 | -41.38445 | 2025-10-02 04:04:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 11266beb-0573-3443-9159-89a8119a7818 | -13.16884 | -47.83674 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c924fc8-731a-3c06-b024-839a96a4e25d | -15.81828 | -41.89494 | 2025-10-02 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2932d705-0413-3590-b00d-27ca4ee2a24a | -13.2133 | -48.50721 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33ea28a6-7850-32a1-aad3-855a009850fe | -15.39184 | -44.96854 | 2025-10-02 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e8446ab-344e-37b7-97c6-d0d222c0e8ae | -15.20694 | -47.99856 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ee1e856e-3173-3a19-8d51-f7cffd29fbef | -18.50621 | -44.04348 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb5af898-e797-33d0-acca-7c67ae587836 | -19.57432 | -42.5846 | 2025-10-02 04:04:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c855db45-43dd-3b96-824c-7e0feda5779e | -13.69047 | -48.64338 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10df0c30-2b74-3bd1-bb0c-d695b9cdcdc1 | -13.52814 | -47.25545 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e86cfdf9-699e-39e7-8354-17b5adbc0b96 | -15.92319 | -43.33351 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4985b12b-0df3-3cbb-aebf-b54bdb78ffc8 | -18.34366 | -44.506 | 2025-10-02 04:04:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3b6359d4-cdff-339c-a102-9f90263cdf7d | -15.82158 | -41.89548 | 2025-10-02 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f395d067-1d4e-3e0b-b91a-1f0c988d11b5 | -13.15921 | -47.80534 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34822422-f66e-3387-93e1-c282c0039c44 | -15.27544 | -46.39925 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c5fb496-8337-3c59-b9cd-118f84c010c1 | -14.47624 | -48.40095 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5ba8bdb9-d413-319a-a69b-3cb8625ab7fe | -16.00212 | -50.89912 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 721e78b7-8686-3825-951b-3988bca99718 | -13.80632 | -47.52556 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9bdde559-1766-39a5-a74b-a18fc6892eb7 | -13.40619 | -47.78048 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b38a255b-282f-3762-bded-a5d5f999d800 | -14.68412 | -49.60942 | 2025-10-02 04:04:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7653e8ae-3ecf-3b39-a250-9bfdb1da82bb | -13.16308 | -47.83357 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README47.md)
