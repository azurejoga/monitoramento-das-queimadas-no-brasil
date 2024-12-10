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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 924d3f39-42e1-3810-a0e1-098b758d252b | -12.78206 | -38.49846 | 2024-12-10 03:38:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 273fa915-395d-3a28-9bfc-35dfbb7e923c | -14.97188 | -44.41125 | 2024-12-10 03:38:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 412956ac-5476-3bbd-9b7c-7f77a32857b5 | -13.62392 | -44.37029 | 2024-12-10 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b05cfb2-7c1a-37e8-bf84-1c49d2214cf1 | -14.9725 | -44.40814 | 2024-12-10 03:38:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86679373-5098-3288-8b31-6860117de550 | -17.90916 | -39.86145 | 2024-12-10 03:38:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6c9bc3ec-c1ee-3fc4-8dc8-ea148ff70d1a | -14.8811 | -42.29161 | 2024-12-10 03:38:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4bb7722d-f45e-3800-acef-a7067c67f362 | -16.75864 | -41.05355 | 2024-12-10 03:38:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 83d2050b-2784-3816-98a4-31c507a8e53a | -11.06586 | -45.38359 | 2024-12-10 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9024cbd8-aaa9-3d18-9197-23f5b761036e | -13.83043 | -41.79573 | 2024-12-10 03:38:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a0d0e02c-78b3-34a2-a420-080051c4af3b | -16.34829 | -43.69709 | 2024-12-10 03:38:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dab7a47-eafc-3d55-b56c-a12641f7d41c | -12.85468 | -43.82093 | 2024-12-10 03:38:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2e21afc-8f4b-3552-903d-463c9c8837ce | -17.4656 | -47.03128 | 2024-12-10 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f326b15b-2ac4-30bb-85d8-48339c3362ab | -16.37441 | -47.40171 | 2024-12-10 03:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 182ed007-3edd-3cec-9542-e779258414b1 | -13.94403 | -44.36 | 2024-12-10 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 926eedfe-c545-34d9-998f-879334867bef | -15.65878 | -39.18909 | 2024-12-10 03:38:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5fc1d00a-fcd7-3780-b04b-d1758a95ccc1 | -11.06494 | -45.38146 | 2024-12-10 03:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7da9f8e6-0bae-39b6-98f8-cb1ee15eb31f | -15.99315 | -43.2903 | 2024-12-10 03:38:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| deaf87aa-2754-3af9-825d-8e4466c5719c | -12.6566 | -43.83959 | 2024-12-10 03:38:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a2ae850-6658-3166-a69a-869a28bf18ec | -17.4665 | -47.02711 | 2024-12-10 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee2eea50-ddd3-3de5-8c3f-c10837728d0e | -14.79852 | -47.42104 | 2024-12-10 03:38:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28b4e289-48f6-397b-8c51-4d1f49e60c3f | -13.11912 | -39.81012 | 2024-12-10 03:38:00 | NPP-375D | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d677f4fa-8fd8-34e2-9c39-d67c26596ffe | -13.62917 | -44.37121 | 2024-12-10 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 724f11d3-491f-3875-8486-769cfc5a6396 | -13.08525 | -44.00082 | 2024-12-10 03:38:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15daea33-efac-3ad1-afa8-17f6c422f9e9 | -14.53024 | -45.47947 | 2024-12-10 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7eb75cc-1458-35c3-913e-ec0d0b35211a | -13.12305 | -39.81076 | 2024-12-10 03:38:00 | NPP-375D | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| af8d0831-7ea6-3929-9450-99e30c0bcb6f | -13.10513 | -43.31454 | 2024-12-10 03:38:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 291e8eef-ffde-3769-bc5a-eeb948ef4ebd | -10.87742 | -44.34336 | 2024-12-10 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee3663d2-9304-3348-8324-aa93634fb032 | -16.19902 | -41.07672 | 2024-12-10 03:38:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5aef69cc-c32b-3da6-80b1-6b8656f24fcd | -17.4674 | -47.02293 | 2024-12-10 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97a591c8-1635-322a-ac89-448121fc7053 | -13.93887 | -44.35881 | 2024-12-10 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b14478a-0f9e-3487-a126-f8c6e7997608 | -11.86982 | -43.72179 | 2024-12-10 03:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8fb5dea1-f105-34a6-b2ff-04aa7f336fa6 | -14.53498 | -45.48444 | 2024-12-10 03:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7f96b0f-38c0-3e7c-8794-25e9b445fe01 | -16.37031 | -47.39822 | 2024-12-10 03:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b44a22a1-7a9d-3357-a44c-2bd541674e1d | -16.37629 | -47.39962 | 2024-12-10 03:38:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5769550-44da-3acd-95b6-139cec5524df | -5.9185 | -48.0449 | 2024-12-10 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 397523f7-93db-3d63-a274-4b824079d4ac | -12.5617 | -58.3347 | 2024-12-10 03:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 45fa2ad2-2554-325a-b9a5-83bd1d6fe2a3 | -9.7587 | -36.2093 | 2024-12-10 03:40:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 120.6 |
| 5effee7d-e6be-34b8-83a4-f9a177867af1 | -2.9859 | -52.8554 | 2024-12-10 03:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3263577d-2f65-3087-ad9f-5aab7fb3d567 | -3.0043 | -52.8549 | 2024-12-10 03:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 641938cc-18e9-30e3-b54d-f18cbda8c5a4 | -12.5425 | -58.3561 | 2024-12-10 03:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 26075866-26df-3edb-a07e-d95c36baf85f | -12.5427 | -58.3362 | 2024-12-10 03:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3978def9-cf43-3679-9569-165b4f79595e | -12.5615 | -58.3546 | 2024-12-10 03:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 23aee59c-0f9c-31db-aa46-8b7780922181 | -2.7758 | -44.9931 | 2024-12-10 03:40:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0708dfb0-89c6-3b91-a08a-2c294c490267 | -5.9183 | -48.0667 | 2024-12-10 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 266068cd-220b-3f07-8daf-e750c30c977c | -21.07178 | -43.69977 | 2024-12-10 03:40:00 | NPP-375D | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 863ebc34-bea6-35b1-9e07-61aba14bcbf5 | -19.06321 | -41.03417 | 2024-12-10 03:40:00 | NPP-375D | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c6a2e9d7-63b2-344e-9cca-12037a6c1f9e | -20.3479 | -40.35933 | 2024-12-10 03:40:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3a54567f-26ca-3727-b91d-919b4298afa5 | -12.5425 | -58.3561 | 2024-12-10 03:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ea7accdd-f2e7-3328-9bb2-1c55c7f3264a | -2.7758 | -44.9931 | 2024-12-10 03:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 476688df-56ba-3303-a256-f6443142d2d8 | -2.8199 | -52.9816 | 2024-12-10 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| bcc8efd4-3449-33c5-8a23-a4f79db2c154 | -12.5427 | -58.3362 | 2024-12-10 03:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 296944b6-c31c-35f2-be75-cbc295ad092c | -5.9185 | -48.0449 | 2024-12-10 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 396d0981-f0d3-3cbf-ab7d-45f920d36296 | -5.9183 | -48.0667 | 2024-12-10 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| a85eb90e-cd57-38c8-a516-cbaacb6a977d | -12.5617 | -58.3347 | 2024-12-10 03:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| cf45bfd0-965e-3b4b-a77d-7bd05503af50 | -2.9859 | -52.8554 | 2024-12-10 03:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| f3f433d5-3c77-3ce8-a83e-835ded9e5b16 | -12.5615 | -58.3546 | 2024-12-10 03:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| cb3ae6fe-49c3-31fa-b69f-c9bc1e473528 | -4.8273 | -47.31778 | 2024-12-10 03:57:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70beaec1-571a-32d0-aa8e-7b4d1765aae3 | -3.83456 | -52.3563 | 2024-12-10 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3181ff2f-ef81-34f3-8344-890225fdc3a3 | -6.83214 | -44.38784 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3bbbf410-4073-39fb-9e0b-8e162da76625 | -5.70986 | -46.5511 | 2024-12-10 03:57:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 567c5807-42f4-34a3-9999-5e9e2b18ff4c | -3.3723 | -42.32605 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 42c9dd78-f2ed-37b1-a04d-5b2135e9f6b4 | -5.29038 | -44.91465 | 2024-12-10 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72fae9b6-ee60-3e04-97cf-120f6f5cb111 | -4.56733 | -48.92268 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee1b1f11-7e67-38e9-a239-269f4fbd02ff | -4.84579 | -37.78773 | 2024-12-10 03:57:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3030443c-36d2-3b31-933f-ed08e0c255be | -6.91423 | -43.50832 | 2024-12-10 03:57:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 83a2c96f-8b52-3f39-a044-efecbdd34fa2 | -6.25754 | -43.5604 | 2024-12-10 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9826167-1427-332a-b041-bcd956c40035 | -5.57606 | -45.20618 | 2024-12-10 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8305b0f-7093-365b-83ac-581d532981db | -4.83011 | -47.31386 | 2024-12-10 03:57:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 595cb454-2ac6-3814-b55d-af6b9ead15cf | -4.65645 | -48.50398 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d72520d1-482b-3244-81c5-84c67c711592 | -6.43358 | -39.70362 | 2024-12-10 03:57:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6b48b70f-c3c5-35a5-8be6-4db0f7b80f65 | -5.70961 | -46.55271 | 2024-12-10 03:57:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9abc13ec-d7e2-32c1-a1a5-ca104095bb31 | -6.83607 | -44.39051 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ff9be0e1-0ad8-3889-a7c8-4fd10040dda3 | -3.85306 | -40.44923 | 2024-12-10 03:57:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3d35b7a7-f825-3fba-887a-b10d2aced200 | -2.91784 | -52.96355 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ec20b5ee-c80f-3383-8cbf-6e24f3caef9e | -7.75734 | -35.13316 | 2024-12-10 03:57:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| aff4d624-5752-3f09-8353-df82adc88233 | -2.91995 | -52.96532 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d6330683-beaf-3aba-87a5-2846e0800a62 | -6.95899 | -42.99013 | 2024-12-10 03:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 315c26db-84c3-37f2-ac5d-bda218c0b742 | -7.07221 | -39.0486 | 2024-12-10 03:57:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dc2bf94f-7f0f-37fb-a6f9-bc87f3c46844 | -5.18946 | -47.73423 | 2024-12-10 03:57:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a886e3ec-9533-3925-a98f-f8395cb1d65f | -6.8369 | -44.38562 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 53fb0d56-ffe8-307a-863c-612ddbdc20c0 | -2.9094 | -52.96978 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd448b1f-2d96-3451-b1be-e11974e57c8a | -5.71419 | -46.55348 | 2024-12-10 03:57:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12be9797-008d-3714-add9-460e856572c0 | -5.91649 | -48.05055 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 58b3d341-c8df-3de0-ab7f-3e8e27895fed | -5.09372 | -40.44107 | 2024-12-10 03:57:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5257abc3-694d-3ebc-9299-c0bc99bd2ebd | -3.78359 | -50.00455 | 2024-12-10 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adb0dcb4-b91f-3389-81f1-583ccd3e9fe6 | -5.51384 | -46.26 | 2024-12-10 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84da8f99-d596-3fe4-9852-5729ed681c07 | -3.21244 | -42.08611 | 2024-12-10 03:57:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 617916fd-28d3-37e3-9dcf-09b0293e4697 | -6.39843 | -35.2043 | 2024-12-10 03:57:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 35e32c87-772b-3e49-81b6-5ebed2926b2d | -5.34799 | -39.34832 | 2024-12-10 03:57:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 707c3693-8d81-351b-b7a0-9df532ae40e6 | -2.98382 | -52.85193 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ceafc3a5-6106-3f1d-ba77-512961180c9f | -7.74759 | -35.25786 | 2024-12-10 03:57:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 06979910-e4db-3e29-87a1-1e6364c283c8 | -4.56087 | -48.92577 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64079b09-d059-3341-8926-6099aca41463 | -6.90619 | -47.83796 | 2024-12-10 03:57:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d0e72c23-33bb-3c92-82bb-f4aef2a265e5 | -7.29287 | -39.61639 | 2024-12-10 03:57:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9345804-12b4-314e-8e30-a601343ca464 | -6.90352 | -47.84185 | 2024-12-10 03:57:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a888999d-8d85-3369-a392-77abba8c6287 | -0.84728 | -47.56488 | 2024-12-10 03:57:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73ce3c7e-5c89-3c8e-be32-66fd7efb406b | -8.47888 | -40.68991 | 2024-12-10 03:57:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9f19355b-3663-36ae-aa49-8af6813fa809 | -8.44411 | -40.60934 | 2024-12-10 03:57:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 42211fe3-f651-3cd8-88e2-205512bafe23 | -2.77186 | -44.99989 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b6ec7dfc-2249-3987-9539-7c633b919dab | -5.57543 | -45.21004 | 2024-12-10 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README13.md)
