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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54eb259b-c2fa-3a2f-9116-36d67869dfd3 | -6.70097 | -42.13272 | 2025-05-03 03:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0e531cf9-5989-3be1-a297-bf9276c305c8 | -6.69751 | -42.13215 | 2025-05-03 03:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 455fda16-83c7-3e94-a125-ec77f4d8799e | -7.31396 | -37.42466 | 2025-05-03 03:57:00 | NOAA-20 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cadc0183-2c3e-3e89-8fd1-1bf407b77995 | -5.78984 | -43.6149 | 2025-05-03 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8da94c6a-9d11-3e37-9903-4f9c31b46fff | -6.69812 | -42.12835 | 2025-05-03 03:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| 8fdb3bdc-16bd-387f-8fad-410734bae5ea | -6.7053 | -42.1234 | 2025-05-03 04:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 4dc51481-5a56-3fcd-8e06-5725119e070c | -7.68501 | -42.98882 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 54e6e66e-faa8-3582-bc0a-bb20be43c58d | -9.60488 | -37.04173 | 2025-05-03 04:00:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 28a0b16a-1121-3361-a753-2900a24d42a2 | -7.68146 | -42.98824 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 054e81da-5112-3fad-9fe7-c09e5201bc12 | -6.96176 | -42.80316 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 53173c6e-1e54-3b9d-b549-b755c9f26133 | -7.67858 | -42.98361 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 467caa10-ee03-3ed9-8e54-c5a6aa0c88fb | -6.95355 | -42.79059 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de221fc3-4445-3b9c-b84f-a9c5aa878d24 | -9.09168 | -40.47671 | 2025-05-03 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 040011a4-9018-30fd-a89a-4a6b132026a9 | -9.7731 | -37.2206 | 2025-05-03 04:00:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 70488ad0-3633-394b-bd68-036f111ff87d | -6.96795 | -42.78773 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f84a6d8f-d294-3b74-8afb-3a6779fd6b68 | -6.96663 | -42.79572 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6c9e2e4d-c8d8-3d1a-889d-2a0f8160fca5 | -7.68568 | -42.98476 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 0238cda8-2a20-340c-b955-d76a7503e31d | -7.68193 | -42.98909 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 730cdb67-39e9-3e93-be12-6edc6b5d2747 | -6.96308 | -42.79515 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4b27439f-400e-30b5-8ba2-5919a0fe532d | -6.96729 | -42.79173 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c1dea074-75f7-3e79-87cd-7dcba761ba11 | -7.68259 | -42.98502 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| f7fdce0c-db40-3e78-ad68-53ca4caeb207 | -6.95311 | -42.7894 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ec4916fe-0c02-3d57-b1c4-bbfa0c8a180c | -6.95244 | -42.79341 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 299eac6f-422b-307f-979c-d1a740fe486c | -9.77311 | -37.21891 | 2025-05-03 04:00:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a523e650-94dd-3f22-80ee-58a666ce236d | -9.60984 | -37.03347 | 2025-05-03 04:00:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 75e4b9e0-b9fa-3b78-8159-4674fa2f262a | -6.7171 | -47.59479 | 2025-05-03 04:00:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40b9125d-3bfc-3046-924c-bfd61e94b669 | -7.67791 | -42.98766 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 35e65d5c-3a5e-38f2-8c2a-1e7a89b31e19 | -6.95291 | -42.79461 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d98c90e-cebd-3a9d-9610-d05bab8deda3 | -7.67838 | -42.98851 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 2a5ca238-6178-30d2-b4a0-8e068162b68a | -6.95599 | -42.794 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a637610-39c2-3350-9945-3b8ef92f0dd2 | -6.96374 | -42.79116 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d36171ff-bc12-339d-90a8-57b7872e8d1c | -7.67904 | -42.98444 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 248ebc00-9145-3863-8bff-a3135580fb1c | -8.0824 | -43.10978 | 2025-05-03 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d394eea-9b0d-37f8-becf-569458f66a6d | -8.07885 | -43.10916 | 2025-05-03 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 93455414-2e74-3d22-ab11-dd6c5f527710 | -7.67483 | -42.98794 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ac4825ec-3257-3597-b482-a7027ddfd256 | -6.95887 | -42.79859 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c46d4014-dc26-3ea9-8169-5cec3cd082d0 | -6.95821 | -42.8026 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fd08d42a-23e1-3f91-a6cb-8e6ae976021c | -6.95665 | -42.78999 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f345ffdb-7cd6-3df3-8eaf-201148328862 | -7.68213 | -42.98418 | 2025-05-03 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 0ac01d2e-e475-36fd-926c-01d0a436ccbe | -8.42401 | -35.65145 | 2025-05-03 04:00:00 | NOAA-20 | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ac64d2b9-d131-3921-aa4a-fdb7f424de08 | -6.96242 | -42.79915 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 464b8f25-afd4-3fd3-bb43-1aea1940ff40 | -7.18054 | -44.87908 | 2025-05-03 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcfd2199-db23-3436-881b-9e298cf383e1 | -6.49511 | -44.72689 | 2025-05-03 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dc96599-5a4f-391f-91ae-b2a764323bab | -6.95732 | -42.78598 | 2025-05-03 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ac7bb08-754d-3863-9867-9eb276ed9d71 | -10.34083 | -38.483 | 2025-05-03 04:00:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1545eb1-ef1e-3675-9fd9-1adf93b9b706 | -17.86729 | -44.56956 | 2025-05-03 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da7aae0e-e90f-3699-a3ab-34428b546c7f | -16.34867 | -43.69642 | 2025-05-03 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25b32093-c993-3d4c-a783-93de9b4c338f | -19.84843 | -43.84488 | 2025-05-03 04:02:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fe3c6960-8e81-35c8-b284-f09e2f2814ae | -19.65175 | -44.90297 | 2025-05-03 04:02:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 332070dd-9580-33ff-ae3e-173366a25c16 | -20.32141 | -40.36326 | 2025-05-03 04:02:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 277fcce6-cf7b-3998-96b7-9db24e195d7c | -11.39353 | -52.94947 | 2025-05-03 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63f60816-7f78-362d-8aea-c61add7f42ae | -17.86386 | -44.56894 | 2025-05-03 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f25bf26c-2ec3-33e5-82d3-c4ef6b920d02 | -17.6218 | -50.91716 | 2025-05-03 04:02:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 87287056-5b99-3a97-a518-68d5ed6e6b75 | -11.39457 | -52.94443 | 2025-05-03 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2a9dd46-c95d-39df-a44d-74359e38662d | -18.25383 | -53.00374 | 2025-05-03 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bb465748-1606-33a1-8527-4bd537ad141f | -20.37635 | -45.60163 | 2025-05-03 04:02:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a53be70-63e8-37e0-9315-446998870488 | -20.32081 | -40.36744 | 2025-05-03 04:02:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3a29a30b-8f23-31a3-8807-0270b82d9ee3 | -17.86795 | -44.56567 | 2025-05-03 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72848ae9-bea5-3fcd-a6f4-07e2271b9466 | -17.17162 | -48.39093 | 2025-05-03 04:02:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a5b0a06-55d9-3dd8-9562-9edd8bd28e24 | -17.75285 | -42.8929 | 2025-05-03 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b912bda-c690-3290-8d48-844b2656091d | -18.2483 | -53.00245 | 2025-05-03 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b682d694-c669-3ffe-a108-c5566b10b5d7 | -17.38591 | -42.65971 | 2025-05-03 04:02:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50530ec4-401c-36bc-95ff-c3f0574e9b30 | -20.41563 | -43.55404 | 2025-05-03 04:02:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2d065801-ea1e-390f-bf9e-a9d7b2686994 | -15.30869 | -43.12972 | 2025-05-03 04:02:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 54e03290-0d0b-3ac8-9237-a7f5cb66f6b2 | -19.96887 | -44.21622 | 2025-05-03 04:02:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 248c5f03-5946-3f43-a847-74cf96ea8667 | -20.31104 | -45.58504 | 2025-05-03 04:02:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9344c01c-b6e8-34d4-86ec-addfdd94b1be | -20.41622 | -43.55035 | 2025-05-03 04:02:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 92f7b083-b73a-3a89-b574-34195cb5f1a6 | -17.86452 | -44.56505 | 2025-05-03 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9f905c3-b61b-3509-8a24-c189baa85132 | -18.24914 | -52.99855 | 2025-05-03 04:02:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 252926a8-ca59-3b6d-bc6b-4d80e7570f80 | -18.50234 | -47.59828 | 2025-05-03 04:02:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4bfd79e-ba74-3fc9-99d7-948621b0e171 | -19.43741 | -44.33823 | 2025-05-03 04:02:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edf1c601-5f9b-3d09-8ac0-8dac176f1bd8 | -11.3987 | -52.95601 | 2025-05-03 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ce0699d-9b0e-31cf-8d32-9fbf1054bbef | -18.6649 | -47.36841 | 2025-05-03 04:02:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba74792a-200d-3967-80e8-b0fdf88d576e | -16.67973 | -43.88433 | 2025-05-03 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05536c64-50de-32da-8dc3-b9719a69a18c | -22.85741 | -42.97998 | 2025-05-03 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 51104eb9-8716-307a-9d38-c0e543522458 | -23.40461 | -46.55602 | 2025-05-03 04:04:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 089ee40f-10e7-3fa8-891f-690348709f7c | -22.02202 | -55.82944 | 2025-05-03 04:04:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ab788c9-0bd0-30e0-9f41-a78f3a8c2bcb | -21.13062 | -47.80351 | 2025-05-03 04:04:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ec6c619-99ef-3dbb-b542-f88be5eeca8f | -19.95423 | -49.82481 | 2025-05-03 04:04:00 | NOAA-20 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a89fd074-b4a1-3e6a-9e24-81123f364661 | -22.24796 | -52.98188 | 2025-05-03 04:04:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a84296ce-7895-37bd-90ed-7083633d4cc0 | -21.08711 | -45.07572 | 2025-05-03 04:04:00 | NOAA-20 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 796dd319-f9df-366b-b07e-4420d76d2e01 | -21.13567 | -48.62005 | 2025-05-03 04:04:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fa90201d-768a-3225-97d6-02dac90ec3a6 | -25.08346 | -50.52928 | 2025-05-03 04:04:00 | NOAA-20 | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1a14ba5a-fdcc-3ea6-b8ef-a5f953713eaf | -20.81541 | -55.53406 | 2025-05-03 04:04:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7e332c1-3eb3-352f-af46-8a6a9deb28cf | -24.34774 | -51.57745 | 2025-05-03 04:04:00 | NOAA-20 | ARIRANHA DO IVAÍ | PARANÁ | Brasil | 4101853 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| af92f5e4-2d16-3376-941b-86e7436d2d65 | -22.24358 | -52.97723 | 2025-05-03 04:04:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e18faab3-0298-322d-a115-2708689e4882 | -21.14573 | -48.61075 | 2025-05-03 04:04:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 720c5a44-3c69-3c83-a70a-b42767ccc060 | -23.40378 | -46.55696 | 2025-05-03 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ba3490cc-af1b-30b9-9033-6ccbcb6b4ccc | -22.02317 | -55.82453 | 2025-05-03 04:04:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8a84b67-9b2f-37ed-b7ad-141e7616598f | -20.71893 | -54.412 | 2025-05-03 04:04:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70ed0fc9-457d-3e86-ba89-9a30fcc76f8d | -22.24288 | -52.98051 | 2025-05-03 04:04:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 36e746b4-bebb-340c-b2ee-1d9066a1d769 | -22.24434 | -52.98113 | 2025-05-03 04:04:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0b9c38d9-6712-34f6-b93a-67d4233cf93c | -23.59225 | -47.43638 | 2025-05-03 04:04:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 651b962e-51d4-3821-8148-8bf7630f88bb | -20.46407 | -46.207 | 2025-05-03 04:04:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ec9f6ec-2514-3fe3-aaeb-c69139e9fd56 | -22.02256 | -55.82603 | 2025-05-03 04:04:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8279a862-f6ad-3e7d-a879-de2a8bc551b6 | -21.19452 | -44.93854 | 2025-05-03 04:04:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0c86908f-7b41-3430-bb74-e5b6e1a3cce7 | -21.1504 | -48.60796 | 2025-05-03 04:04:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 43d26c98-93e6-339e-a27a-471501290a40 | -20.74016 | -50.53834 | 2025-05-03 04:04:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fdeab5ae-869b-3d6d-8c94-f98400a8e703 | -20.71963 | -54.40815 | 2025-05-03 04:04:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19ee77e9-ea9d-3116-959c-b3f37fad3326 | -21.98709 | -46.82111 | 2025-05-03 04:04:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
