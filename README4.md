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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96c141f2-c7d9-3e9d-ae0d-ec4b77daecb5 | -6.18092 | -48.0529 | 2025-07-03 01:05:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 0b55ed84-6ef2-36c3-b286-fa99e6633669 | -6.17997 | -48.06989 | 2025-07-03 01:05:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 46ec67ff-7c2b-36fb-9510-521e7fcfddc3 | -4.53472 | -48.02657 | 2025-07-03 01:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 9432a6f9-aab9-361f-99f3-f50bad37522b | -6.16767 | -48.05533 | 2025-07-03 01:05:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 40a73394-03a6-366e-9654-bf90a7eedfb6 | -6.18418 | -48.07481 | 2025-07-03 01:05:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 69ba943b-ed09-3c44-8e6d-fde6e4978e88 | -14.6287 | -53.9018 | 2025-07-03 01:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 962c28ff-1eb3-3cc9-9723-f419a9be68dd | -9.1668 | -48.7794 | 2025-07-03 01:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c6a0597a-3a3f-344b-b0fc-95e377851256 | -11.6588 | -44.5974 | 2025-07-03 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| fb88e734-8372-3ab6-802e-05442fbca079 | -14.6484 | -53.8785 | 2025-07-03 01:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| fe021097-b074-33dc-aeb9-13432a35a017 | -18.22 | -51.3446 | 2025-07-03 01:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 262.2 |
| 7b156de2-0544-3ac6-8b88-a61b98a6843c | -7.2408 | -43.0664 | 2025-07-03 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| d282ae5f-401d-38a6-aee6-194eff40e42d | -6.9416 | -42.8834 | 2025-07-03 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 194.1 |
| 7879a793-8f2f-340f-8fa0-63a13838282e | -7.2222 | -43.0447 | 2025-07-03 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.8 |
| 209457f9-e91b-3873-9a16-281543bfc5d7 | -14.6481 | -53.8994 | 2025-07-03 01:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 40f95c17-33cd-355e-a417-4ac9a5a77f5a | -7.2219 | -43.0682 | 2025-07-03 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 244.6 |
| 7cf93074-ded0-31b0-9750-ee4de9849a1f | -6.9605 | -42.8816 | 2025-07-03 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 538.0 |
| 221dc99b-b28f-3002-8ced-035e9473311c | -6.9793 | -42.8798 | 2025-07-03 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 5c1a3646-a40d-3dfe-b5bd-10cc4a5ac3cf | -6.1791 | -48.0712 | 2025-07-03 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 7c4cdfd7-fcf9-307d-bb87-bba02ac292f0 | -18.2205 | -51.3226 | 2025-07-03 01:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 46.8 |
| f80ab049-e86b-3d31-8678-4c3d6f475d65 | -6.1792 | -48.0494 | 2025-07-03 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 0d33fd7c-43d0-3ba9-8bfb-e1ac84b2e1c0 | -18.2 | -51.3481 | 2025-07-03 01:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 1a77ab54-2834-32cc-9a4a-33730f04b26d | -9.1857 | -48.7776 | 2025-07-03 01:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 27917122-8eb2-3b65-905c-42a7fe130b49 | -14.6291 | -53.8809 | 2025-07-03 01:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 4f4fa1d8-5244-357b-b825-368d076427ca | -18.2195 | -51.3666 | 2025-07-03 01:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 63183193-6fe7-3828-ad6a-6a40a4bb99ba | -6.9607 | -42.858 | 2025-07-03 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| fb472dab-b5ff-37cf-bb38-84c4d87adcaf | -6.9602 | -42.9052 | 2025-07-03 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 986b0046-05d4-35bb-8def-15e21baa5a78 | -6.9602 | -42.9052 | 2025-07-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 162.5 |
| cd0afafd-ca78-3c05-aa19-7d16caafd2a0 | -6.9607 | -42.858 | 2025-07-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 5c248737-0a41-3354-b294-1ab35a0a2a49 | -18.2399 | -51.3411 | 2025-07-03 01:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 5234223b-a3b0-3f4b-8f19-94825bf64a4f | -6.9605 | -42.8816 | 2025-07-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 451.9 |
| 071b6a6b-e580-3064-bb5e-4f6637491efd | -6.9793 | -42.8798 | 2025-07-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 0f29ab30-a48e-36b8-aed4-336bca59efe7 | -11.6588 | -44.5974 | 2025-07-03 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 29ccd356-ffab-3cdb-9e59-abd2569a29fe | -7.2408 | -43.0664 | 2025-07-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| b516f6bf-ca6d-3832-b5dc-331d05d59523 | -6.9414 | -42.907 | 2025-07-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| f45b3e0d-f0dc-361b-a47f-30d1863e4b1a | -7.2411 | -43.0428 | 2025-07-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 75e004c3-c7ca-32e8-86b3-52edb261a928 | -6.1791 | -48.0712 | 2025-07-03 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| e01110d1-1e72-3ffb-af3c-5291a0b6d772 | -9.1668 | -48.7794 | 2025-07-03 01:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 810e79ba-2cbf-3611-a9f4-a3ce51039332 | -14.6484 | -53.8785 | 2025-07-03 01:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| bfd65b9e-306d-3e58-aa8c-01fe4a68ba70 | -18.2195 | -51.3666 | 2025-07-03 01:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 95e09a33-46d5-3dc5-8112-d8b7e2d4db90 | -7.2222 | -43.0447 | 2025-07-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| ff00951e-40e2-3338-8ab5-8083e31ed73f | -18.2 | -51.3481 | 2025-07-03 01:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| cda9439f-e6fe-31b4-a904-1331cb36220b | -6.1792 | -48.0494 | 2025-07-03 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 0c96c370-a039-3325-890c-d1e45124bd51 | -7.2219 | -43.0682 | 2025-07-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 172.3 |
| f0f7d88a-189e-3691-9200-5b5b1db71ba9 | -6.9416 | -42.8834 | 2025-07-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 175.3 |
| 2eb5d40a-0abb-3c3c-890f-209fb7856223 | -18.22 | -51.3446 | 2025-07-03 01:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 5c948b89-d3bc-34eb-9bb2-13454ce58f45 | -9.1671 | -48.7577 | 2025-07-03 01:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2578687c-f2c3-39d2-8005-84beb5b53458 | -14.6291 | -53.8809 | 2025-07-03 01:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 155.0 |
| fc9354f3-f089-3d89-9f12-821d4ae161ae | -14.6287 | -53.9018 | 2025-07-03 01:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 705a4850-4d62-3d47-973c-a31366e705ab | -6.9607 | -42.858 | 2025-07-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| be55c4cf-aa08-38b1-8327-660094c1d13e | -5.9938 | -43.7366 | 2025-07-03 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 518116d2-bad1-39ed-8870-d27165e667a5 | -7.2222 | -43.0447 | 2025-07-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| ba7a4014-bcbd-3a32-be4b-1ebbce4ece7e | -6.9602 | -42.9052 | 2025-07-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 150.2 |
| 1640e2df-b09c-308b-84b3-bcc9bd8278b0 | -18.2195 | -51.3666 | 2025-07-03 01:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| e12cbdf6-06aa-3537-a548-972a4b63c172 | -6.9605 | -42.8816 | 2025-07-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 454.8 |
| f9478b1d-d56e-33c5-9194-790b40b71617 | -6.9793 | -42.8798 | 2025-07-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 27ab4d39-8cba-303a-a595-10952980f6f3 | -6.9414 | -42.907 | 2025-07-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| c7558cb1-7323-30a5-981d-465b657c4303 | -14.6291 | -53.8809 | 2025-07-03 01:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c58f1ae4-cbea-3c85-98d3-26cd85204df2 | -6.1792 | -48.0494 | 2025-07-03 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| b0528042-7bd0-3a0c-8867-f4db369c8dd7 | -7.2219 | -43.0682 | 2025-07-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 158.0 |
| 9d815bcd-6658-3fdb-8e75-d8931564a6d6 | -6.9416 | -42.8834 | 2025-07-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 198.4 |
| 29b45aab-93b4-3b0d-b561-6385daf00d49 | -9.1668 | -48.7794 | 2025-07-03 01:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e351e7be-d9ab-3155-93b1-25e609c7692a | -14.6484 | -53.8785 | 2025-07-03 01:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a972cd8b-a60d-325e-a2b8-86399047c48f | -7.2408 | -43.0664 | 2025-07-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.7 |
| d2b88144-dff8-33cf-9019-740a65caa47d | -11.6588 | -44.5974 | 2025-07-03 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| aedf3a3e-9314-36df-b84f-f1b00e7f1ae0 | -6.1791 | -48.0712 | 2025-07-03 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9cde80ce-c63f-3020-aea3-1aee69441546 | -18.22 | -51.3446 | 2025-07-03 01:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 00afdf91-4348-37e7-85fa-0cb8075a0fa4 | -18.2399 | -51.3411 | 2025-07-03 01:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| e8941dc9-d9bf-364f-b1ef-0cbc46cd6db5 | -18.2 | -51.3481 | 2025-07-03 01:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 2de2b9f2-f616-3855-90b9-861659cb2cc4 | -11.6592 | -44.5741 | 2025-07-03 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| d01d728c-815b-3a4b-bd7b-06203eb8edcd | -9.1668 | -48.7794 | 2025-07-03 01:40:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 41f78a8d-5778-34b5-843c-6f72023faf98 | -7.2222 | -43.0447 | 2025-07-03 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 1fc28433-39cc-3fc5-82c3-fa6f1b0cb30e | -14.6291 | -53.8809 | 2025-07-03 01:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| b7226c6d-c9bf-3c3e-9abd-ab2ae9770a46 | -7.2408 | -43.0664 | 2025-07-03 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| c3d1f08b-fcce-330b-b8a9-357ee0993f96 | -14.6484 | -53.8785 | 2025-07-03 01:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| caaafbab-fa3e-3312-b12b-832b1108058d | -7.2219 | -43.0682 | 2025-07-03 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 146.9 |
| 5238919c-3424-3854-bb37-a6e78554bdb6 | -18.2 | -51.3481 | 2025-07-03 01:40:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 257c568b-5393-384c-adc9-9756c5e381af | -11.6588 | -44.5974 | 2025-07-03 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e3fb3231-6b71-31d5-a7cc-fa1a5b29f75a | -18.22 | -51.3446 | 2025-07-03 01:40:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 263a6b32-b125-380f-926c-fbda71e95df1 | -6.1792 | -48.0494 | 2025-07-03 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 20a345e1-2465-31a1-a01e-e7e13434e0a6 | -18.2195 | -51.3666 | 2025-07-03 01:40:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 373af5b1-34e3-3a0f-8548-975fb8881ed0 | -11.678 | -44.5945 | 2025-07-03 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 4a2c4fd3-82d0-3f18-9697-097add911103 | -6.9605 | -42.8816 | 2025-07-03 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 499.7 |
| 448bd274-e728-33e4-9f2c-50763805278e | -7.2219 | -43.0682 | 2025-07-03 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 173.3 |
| df8f5941-91bc-3bdc-94c4-6590a50f8805 | -18.22 | -51.3446 | 2025-07-03 01:50:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 219.2 |
| c5ab4378-ad78-3be7-9233-1c2e4143c6c3 | -11.6396 | -44.6003 | 2025-07-03 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| cae3e1d6-37a6-3445-9320-05c31e79021c | -14.6291 | -53.8809 | 2025-07-03 01:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 511c4570-92e5-3455-a624-f234f67be71f | -6.9416 | -42.8834 | 2025-07-03 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 156.6 |
| 86659d29-6329-309f-b73c-93c4e2975bd2 | -11.6588 | -44.5974 | 2025-07-03 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 304.0 |
| 14d0f306-6a97-366e-ab2c-5e281011f1a8 | -18.2 | -51.3481 | 2025-07-03 01:50:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 50.0 |
| a5d73e41-b24c-314f-9571-4efb4ac4a672 | -14.6484 | -53.8785 | 2025-07-03 01:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| b6f0c2e3-44ce-3543-9d4a-06ba3fbdfbae | -6.9602 | -42.9052 | 2025-07-03 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| 3494c384-2198-3ffa-b8b2-dca92fc9d304 | -6.6112 | -43.8941 | 2025-07-03 01:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b0347a19-4434-3ec4-be9e-d4e71e959edd | -11.6592 | -44.5741 | 2025-07-03 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 05a7fca1-bc28-3176-935b-2250663ec74f | -7.2222 | -43.0447 | 2025-07-03 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 3581164a-ef10-323f-b0ca-65ba3ae345ed | -6.9607 | -42.858 | 2025-07-03 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| ec6667b4-06df-36ba-8c47-5716e9518177 | -18.2195 | -51.3666 | 2025-07-03 01:50:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 657916b0-7f06-3881-a4b2-601fc6283b60 | -6.1791 | -48.0712 | 2025-07-03 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a51dd358-4240-35d0-94e1-aa309f7a4f2a | -6.1792 | -48.0494 | 2025-07-03 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 7d0dcf54-8bd2-305b-9ca4-ca0f5f0b02ad | -7.2408 | -43.0664 | 2025-07-03 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 4d1a3854-2808-3db3-bd7c-ab033327a638 | -18.2205 | -51.3226 | 2025-07-03 01:50:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 45.6 |


[Clique aqui para ver as próximas entradas](README5.md)
