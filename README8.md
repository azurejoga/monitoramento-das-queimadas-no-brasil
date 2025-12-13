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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c83f5184-adf8-3bd9-96cc-432c1fd76b56 | -5.06903 | -43.66946 | 2025-12-13 04:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7414e185-0107-3133-9ce5-ca2c64a18623 | -7.62158 | -39.06431 | 2025-12-13 04:01:00 | NOAA-20 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 835ee5b8-4a5a-37bd-b122-7d3d73d784ba | -7.98262 | -41.43273 | 2025-12-13 04:01:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 013206de-e6bf-3277-bffc-73b5d49711de | -10.14886 | -36.19624 | 2025-12-13 04:01:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 06519746-10ab-3437-a53f-c65195b95d07 | -8.59182 | -39.44398 | 2025-12-13 04:01:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 53a727c9-7ab2-3e67-94b9-63567e75e492 | -5.1025 | -37.56844 | 2025-12-13 04:01:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2a2b2fbc-2751-3060-8f62-17673ca5005d | -7.54237 | -35.22909 | 2025-12-13 04:01:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 423ba81f-6995-33fa-9f0e-6ca2f5b852a7 | -4.32176 | -44.80309 | 2025-12-13 04:01:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be966993-fd04-30ae-b126-f86b4ff57b67 | -8.02912 | -43.10051 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 00eda393-4600-3b82-8a5f-1515d5fdc519 | -8.04256 | -43.10684 | 2025-12-13 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0cacef72-1ed8-30b2-8870-7ea2f8bff20a | -5.26705 | -37.90691 | 2025-12-13 04:01:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 19fbe50c-69d2-3b08-a88a-52ce55b18775 | -3.68464 | -43.94437 | 2025-12-13 04:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| c7b151ad-8205-3da2-b96b-5d292f23eada | -12.27366 | -38.41305 | 2025-12-13 04:01:00 | NOAA-20 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6546d750-dc69-3a20-aa20-553ebc67e5fe | -5.60137 | -40.76984 | 2025-12-13 04:01:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da57fc31-4cb9-3346-b44d-dc5d69de5fc8 | -6.96577 | -39.98449 | 2025-12-13 04:01:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c5d569ed-4eb8-332e-b1ac-3cc950cb3411 | -7.13893 | -39.68147 | 2025-12-13 04:01:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d565816f-1642-3614-bc4b-dad5b617965a | -8.40607 | -44.04512 | 2025-12-13 04:01:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a09ab51e-cf9e-3a3b-a4cd-b0fd0e416d71 | -6.95861 | -39.9869 | 2025-12-13 04:01:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa7cb815-ea0c-372f-b3b9-abe56210ff2f | -10.37214 | -45.05347 | 2025-12-13 04:01:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2ffcc37-0eb0-3cb1-b290-d66dc5a773e6 | -6.7839 | -39.62884 | 2025-12-13 04:01:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dddc7842-8e33-306b-a7e4-e9cecdec2bc8 | -4.47967 | -44.88547 | 2025-12-13 04:01:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b46a46d-c24f-3a70-b948-f50b66011826 | -3.81496 | -47.05241 | 2025-12-13 04:01:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cbebda5-6b55-3c1f-8eae-529ba0566044 | -12.87409 | -38.34936 | 2025-12-13 04:04:00 | NOAA-20 | LAURO DE FREITAS | BAHIA | Brasil | 2919207 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ebdce8d9-73a7-3175-9900-15a0b1069532 | -15.98097 | -49.95366 | 2025-12-13 04:04:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78a7cb2e-4b1b-39dd-98c2-77a58b61208a | -11.88869 | -43.70777 | 2025-12-13 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfaeb0dd-ae97-3d8e-90f9-1c5d60c74aa9 | -15.35978 | -39.32077 | 2025-12-13 04:04:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3b42d8ba-0e3b-359f-8f9a-c4c632187dc0 | -15.97997 | -49.95891 | 2025-12-13 04:04:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fb346de-8a1b-32c1-bc8b-4a1a1c82b467 | -11.9483 | -43.95737 | 2025-12-13 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84722c91-be76-32e3-8f51-363d74907b87 | -11.90479 | -43.86865 | 2025-12-13 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4383682-de88-3e63-9d01-9475b72fd136 | -15.98164 | -49.95539 | 2025-12-13 04:04:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89f1f7dc-5bc3-3f46-898b-3e88aefd943c | -11.8471 | -43.73446 | 2025-12-13 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31777545-6a74-3433-a3ff-0417393656d6 | -14.07407 | -39.47547 | 2025-12-13 04:04:00 | NOAA-20 | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fe12fe22-ce2b-3e51-b283-ccdc3a167e16 | -29.40104 | -52.41126 | 2025-12-13 04:08:00 | NOAA-20 | SANTA CRUZ DO SUL | RIO GRANDE DO SUL | Brasil | 4316808 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 41c59206-bd27-3b78-85ab-b22960e8b1a8 | -8.0321 | -43.1257 | 2025-12-13 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 5069bc5d-feea-32a4-ad19-d07e804be5ed | -3.2196 | -41.8431 | 2025-12-13 04:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 67121850-63e9-3550-8689-bd61d3b307c3 | -3.1822 | -41.8448 | 2025-12-13 04:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 1aa01363-b42b-3e05-a52f-59b90795ef63 | -3.2009 | -41.844 | 2025-12-13 04:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 1797939a-a491-3ab6-bff6-3c7e0d750d51 | -8.0324 | -43.1022 | 2025-12-13 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| e08bf1d4-6eac-34de-a8e7-16d2d2d32268 | -3.2007 | -41.8678 | 2025-12-13 04:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 31229ad1-aa5e-353a-8ec1-77eff6261405 | -3.182 | -41.8687 | 2025-12-13 04:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b35412ed-5e43-3acc-8173-4e0e7eb788f2 | -8.0513 | -43.1001 | 2025-12-13 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 5582dced-0df9-38d6-ba8c-937f70e7fadf | -2.487 | -47.7692 | 2025-12-13 04:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| a3bfbeb7-7261-385e-8bdf-bb8f6b3a3835 | -10.1633 | -36.1914 | 2025-12-13 04:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| d396ed96-5e3b-376f-9d19-2c70adf0d33e | -10.144 | -36.1949 | 2025-12-13 04:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 107.5 |
| 49b7a034-265b-3f45-9053-5c0711e0b8c9 | -3.2194 | -41.867 | 2025-12-13 04:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 85d82ae8-f2b5-36f8-a967-6898c5970339 | -3.2009 | -41.844 | 2025-12-13 04:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 141.0 |
| d3496a1d-a16c-378a-b109-59ad78302319 | -8.0324 | -43.1022 | 2025-12-13 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| d96c3c3b-0d54-3aa2-b339-28c3a9b09cf9 | -3.1822 | -41.8448 | 2025-12-13 04:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b1e8fe18-6c93-372b-ab13-fe04ba2c78a5 | -3.2196 | -41.8431 | 2025-12-13 04:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| ec19a0a3-7c41-3867-a165-94f34043f9bc | -3.2007 | -41.8678 | 2025-12-13 04:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 84eb9167-5622-3e9e-9539-40ef04cbb48e | -8.0513 | -43.1001 | 2025-12-13 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| 3149d3f5-e87b-3fce-a1bc-6a0acf94066b | -3.182 | -41.8687 | 2025-12-13 04:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 746754f6-9ae2-3017-8c43-1f0d38814688 | -3.2194 | -41.867 | 2025-12-13 04:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6dd4feeb-5bb6-34b5-a568-d41e008a9f94 | -3.2007 | -41.8678 | 2025-12-13 04:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 158.7 |
| e0a32ba4-9ebc-3692-9a74-df8ba8cb3b1b | -3.182 | -41.8687 | 2025-12-13 04:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1b3b8a98-1b28-30d0-926d-dc20df8cd5bb | -3.2196 | -41.8431 | 2025-12-13 04:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| ffd49959-2b24-3a1a-a678-1069d9f42a2a | -3.2194 | -41.867 | 2025-12-13 04:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 61d7d08b-4bb9-30d5-96a7-63c23e00c8ab | -2.487 | -47.7692 | 2025-12-13 04:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| ebdd7eb7-b2c2-30cb-b686-7400ead7aa38 | -3.2009 | -41.844 | 2025-12-13 04:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 608f103c-14b0-339f-b761-8f4e5e4d6b61 | -3.2196 | -41.8431 | 2025-12-13 04:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 2b922dd7-6991-3c40-a3e2-e6834a40118b | -3.182 | -41.8687 | 2025-12-13 04:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| d50021b8-fec0-3c39-a022-eddb419604db | -3.2007 | -41.8678 | 2025-12-13 04:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 45931d5d-046e-37a0-8646-df189f95d57d | -3.2194 | -41.867 | 2025-12-13 04:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| c8936f16-5fd6-3682-83c0-d6fe8e948be8 | -3.2009 | -41.844 | 2025-12-13 04:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 124.0 |
| e2ca09ca-3add-3bac-a7d8-0bfcfcf04acf | -3.182 | -41.8687 | 2025-12-13 04:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 5f8e936e-44b1-3c9a-8d04-8471a7ef79c9 | -3.2196 | -41.8431 | 2025-12-13 04:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| d1c6cbf7-9849-3516-884c-ff4a4ab82aee | -3.2007 | -41.8678 | 2025-12-13 04:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 11bab764-3f66-3c24-875d-b41b293e6246 | -3.2194 | -41.867 | 2025-12-13 04:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| eeb7a581-c1b1-3888-95f6-70223fd0284d | -3.2009 | -41.844 | 2025-12-13 04:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 95b3b76c-e76d-3452-b381-fff82f87d357 | -1.3226 | -50.64195 | 2025-12-13 04:50:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d135037-8db1-34ab-adb6-71ef9b451153 | -1.01669 | -53.72651 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f71a0b7-d5c2-3b06-a8a8-f047ce900091 | -1.68093 | -53.85609 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7567c6ab-58d8-36b2-a408-c5dd8689048f | -2.48757 | -47.77242 | 2025-12-13 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8fe61443-4b24-332b-8a95-04e8583dcd5c | 0.10429 | -51.12861 | 2025-12-13 04:50:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 778e863f-53fd-3181-afe3-6104755e9b30 | -2.6685 | -46.89042 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ac17c91-454a-30fe-ab0d-4ab99064a002 | -1.18087 | -52.09084 | 2025-12-13 04:50:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 146630ea-49ef-3669-a0d4-bd30545671e1 | -1.87887 | -54.68692 | 2025-12-13 04:50:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e08ef69d-8ca4-3728-8206-d939107d7a33 | -3.20402 | -41.84631 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0f1052b0-0c8f-3fe0-93c5-f5b6d1156653 | -2.08155 | -52.05249 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 701fbde7-3c10-3349-ae08-6353ca28f767 | -2.51351 | -47.80685 | 2025-12-13 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82efe8d8-fe28-33f6-aa00-2165f1580bc2 | -1.58 | -54.12345 | 2025-12-13 04:50:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b84bdd8a-dc38-37be-81c6-d93b762f48cf | -3.45307 | -44.73359 | 2025-12-13 04:50:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71157be6-0223-3c63-9ba4-6e8868b794f2 | 2.51048 | -61.02853 | 2025-12-13 04:50:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b7850cc-20ce-32f3-9b76-9632b4ddf030 | -1.43211 | -53.47704 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bb4edf0-f83a-33b1-80bf-e3e9a03f1e39 | -2.29376 | -53.71138 | 2025-12-13 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a2f2e7fe-c0ae-3f1d-80aa-1ea8d266d99e | -1.42869 | -53.47652 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6de57995-9d2b-3999-a4a3-e1b7e2d8c922 | -2.23765 | -46.51729 | 2025-12-13 04:50:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00148d16-ffa8-345f-b159-55a43b4f3386 | -2.73516 | -45.07536 | 2025-12-13 04:50:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 24debe39-78f5-33f5-8bad-59e1cb871138 | -1.66608 | -52.03313 | 2025-12-13 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72c86a3a-63ec-38c4-96ca-c096c78f424f | -1.35765 | -52.95189 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db051b54-d48e-3c40-81f9-8dab5315ca3a | -2.7397 | -45.07607 | 2025-12-13 04:50:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| df004dc8-c31d-3b31-8290-16c1c1179d42 | -2.41521 | -44.03776 | 2025-12-13 04:50:00 | NOAA-21 | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 268fbbe3-7613-3585-afef-b420d581def3 | -1.66802 | -54.57599 | 2025-12-13 04:50:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aad7b78c-4943-3139-a9e9-12004d25c862 | -1.84995 | -54.52887 | 2025-12-13 04:50:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f808e44-1e52-3feb-a3e1-fc0a066f7a7b | -2.6593 | -51.6441 | 2025-12-13 04:50:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4169588a-3e2f-3d85-bae2-d5f7017510fb | -2.78259 | -45.78362 | 2025-12-13 04:50:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7708b2ff-cc97-3187-a11e-ea6434bb727c | -3.20914 | -41.85105 | 2025-12-13 04:50:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 81dc02df-5b9d-3c0d-9694-4a78f9554c60 | -2.35203 | -47.46731 | 2025-12-13 04:50:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e9a4c6-c73b-3aad-8eaa-ebb1379c5019 | -3.23796 | -47.47643 | 2025-12-13 04:50:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4eb1b746-2df1-3bdf-b8da-4a8b2b98b5c9 | -1.28439 | -53.16547 | 2025-12-13 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
