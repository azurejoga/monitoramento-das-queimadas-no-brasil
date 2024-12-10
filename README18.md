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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a4585f6-6f2f-347a-adbf-b649ef54fa17 | -14.97826 | -44.41196 | 2024-12-10 04:01:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6f47b60-5510-33ac-ba90-3728ef6bdab1 | -15.15819 | -43.5797 | 2024-12-10 04:01:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9d269637-8d38-3f8e-b69a-5fb994601224 | -14.97123 | -44.4107 | 2024-12-10 04:01:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb910882-7133-3d80-985e-3d510f894ed7 | -17.46635 | -47.86491 | 2024-12-10 04:01:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b524008a-e467-3d23-8597-e041b0a2a6af | -18.73855 | -39.91275 | 2024-12-10 04:01:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0438ca63-4f0a-34bf-8410-164ff67e07eb | -17.46648 | -47.03073 | 2024-12-10 04:01:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6958e5ef-c8c9-334f-afa4-f9d480a36849 | -19.43715 | -44.34069 | 2024-12-10 04:01:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13193d84-f2c2-3aed-bc92-bd97542b77c0 | -17.46495 | -47.87248 | 2024-12-10 04:01:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f02a3ac7-3810-3f13-8166-081930e4b1fd | -14.96773 | -44.41004 | 2024-12-10 04:01:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77f12f4b-2531-3f74-8f14-d4b5e38883b5 | -14.38228 | -46.79672 | 2024-12-10 04:01:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72a685fd-e8a8-3252-994d-46e7dcc06376 | -19.98046 | -44.68594 | 2024-12-10 04:01:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3352c2e2-9249-365d-9351-ca83f47b23ee | -20.41465 | -43.55318 | 2024-12-10 04:01:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 97ae2cf0-d0b8-3c61-ada0-ed4c74ee8b90 | -15.80057 | -42.38952 | 2024-12-10 04:01:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 97558efa-8823-31a8-aa83-9363a1c837c9 | -16.83124 | -42.59332 | 2024-12-10 04:01:00 | NOAA-20 | JOSÉ GONÇALVES DE MINAS | MINAS GERAIS | Brasil | 3136520 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4e1089e-b432-32f6-9c52-2ac43114ba93 | -13.31461 | -52.41786 | 2024-12-10 04:01:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8cb805d-247b-378b-9192-4bca24a75f6e | -18.76675 | -39.86623 | 2024-12-10 04:01:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9483fe60-a652-3cef-b41c-bae38d680eb0 | -12.5615 | -58.3546 | 2024-12-10 04:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| c6664cf2-e6bd-3581-9432-1e58456de1fd | -3.0043 | -52.8549 | 2024-12-10 04:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 09265948-a732-3277-8412-fd3fd14c8392 | -12.5425 | -58.3561 | 2024-12-10 04:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 5b1742a3-d4ee-3302-b43e-317557e6806a | -12.5427 | -58.3362 | 2024-12-10 04:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 77b132a1-59ab-3c9f-9d80-f7fec26b995d | -12.5427 | -58.3362 | 2024-12-10 04:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 5b150e13-6d17-3898-9851-16b6d547ce51 | -12.5425 | -58.3561 | 2024-12-10 04:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 08ec7489-1496-33f9-9291-2cd607600b85 | -3.0043 | -52.8549 | 2024-12-10 04:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b03206d4-dbd0-3f06-ae75-e90c62747760 | -12.5615 | -58.3546 | 2024-12-10 04:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| c3d5a4a2-6c7a-3e8a-a798-9808cc987465 | -12.5615 | -58.3546 | 2024-12-10 04:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 47857ef7-5a38-3aa3-819c-a3898bd8b8d9 | -12.5427 | -58.3362 | 2024-12-10 04:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1e521741-387a-3efb-89b4-eb61707f4ffd | -12.5425 | -58.3561 | 2024-12-10 04:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 6aec1ffb-27e8-398f-8fcd-60b786d63f8f | -3.0043 | -52.8549 | 2024-12-10 04:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 5e71fcc5-1b19-3b88-a731-f2a8cd90654c | -4.3959 | -47.7618 | 2024-12-10 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a9be9e71-7ca2-3b43-9041-f55be91c5103 | -12.5427 | -58.3362 | 2024-12-10 04:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7f2ce9ca-8943-38eb-b102-5ae83e63a843 | -12.5615 | -58.3546 | 2024-12-10 04:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 45194f04-5892-3be2-a156-f4004c64cd6d | -12.5425 | -58.3561 | 2024-12-10 04:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| a8c80660-8fbc-3767-8fa3-4074737e8aef | -4.3774 | -47.7627 | 2024-12-10 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| d33fb9c7-5672-310e-bcf1-30ed8f184d79 | -2.9859 | -52.8554 | 2024-12-10 04:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 448c9a8b-028e-3f77-9ea3-133c1aee79c2 | -3.1105 | -54.0657 | 2024-12-10 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| ca51a1bf-4d73-3435-a816-9d3bf2794b87 | -6.82633 | -44.38557 | 2024-12-10 04:48:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 5f4c8dc2-b65e-3366-9e11-994645c249d1 | -6.92058 | -43.50694 | 2024-12-10 04:48:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4ec8320c-c152-3c40-aa14-a3ccab4bcfe6 | -6.90802 | -43.5049 | 2024-12-10 04:48:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 205bee52-b279-3d9e-86ef-b06344705989 | -3.85142 | -40.44163 | 2024-12-10 04:48:00 | AQUA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 25435e38-c3fb-3ca4-9ae0-d5675803a66c | -5.68385 | -37.35167 | 2024-12-10 04:48:00 | AQUA_M-M | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 31.1 |
| 539e57ea-8f72-39a3-b35a-87a40a877659 | -6.68261 | -34.97224 | 2024-12-10 04:48:00 | AQUA_M-M | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 1c13fedb-0468-3439-abca-cdd39db0700c | -6.69202 | -34.97366 | 2024-12-10 04:48:00 | AQUA_M-M | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 0aecc17d-1f28-3899-af21-3d301f2f4162 | -5.68252 | -37.3605 | 2024-12-10 04:48:00 | AQUA_M-M | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 66be9941-a892-3ffa-8af8-2b92caffe802 | -6.8335 | -44.37957 | 2024-12-10 04:48:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| bead134a-a459-3cd2-9575-6348a5174240 | -12.5615 | -58.3546 | 2024-12-10 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| eb32f310-aa73-3244-94fc-5422ae0e500e | -4.3959 | -47.7618 | 2024-12-10 04:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a361dc31-aafd-317a-980c-2631dfcaa279 | -12.5427 | -58.3362 | 2024-12-10 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a96760bf-2564-310f-a6d8-c2535a643eb8 | -12.5425 | -58.3561 | 2024-12-10 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| dccc96d6-a91b-3871-8382-9a5c03f44730 | -9.93513 | -36.44232 | 2024-12-10 04:50:00 | AQUA_M-M | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| ffb2d27d-c0ec-35f0-8a4e-fbbdc44fcd4a | -9.92467 | -36.45043 | 2024-12-10 04:50:00 | AQUA_M-M | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ee2a49e2-6984-3145-bfd9-72a7454fa637 | -9.93376 | -36.45182 | 2024-12-10 04:50:00 | AQUA_M-M | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 55cc8f1b-f0ba-33cc-8945-52996d8f8e73 | -10.45707 | -36.7857 | 2024-12-10 04:50:00 | AQUA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 511dcdad-1fd7-3a7a-bb15-a88b71de1d12 | -9.92603 | -36.441 | 2024-12-10 04:50:00 | AQUA_M-M | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| bcbaccc1-5bd3-35a8-9d81-83004caab9d0 | -9.83812 | -36.16149 | 2024-12-10 04:50:00 | AQUA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 797fd9ad-e367-3b14-8d88-9f0583efdfba | 3.15039 | -60.72211 | 2024-12-10 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ea0d1bf-1d80-3f99-8843-e8563e40df1f | 3.22912 | -61.18959 | 2024-12-10 04:50:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c68c2507-1889-3a82-8edc-62f6b348e39d | 3.15336 | -60.72283 | 2024-12-10 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d21b45e-2cd0-3ed6-bf65-534bbe1f4107 | 4.12724 | -59.95416 | 2024-12-10 04:50:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f44cd69b-9fbe-3f84-9ac3-e1c94c872d46 | 2.4304 | -60.65002 | 2024-12-10 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c9b6c5c-8e6f-3a57-8834-eb323ce9844f | 3.2297 | -61.19365 | 2024-12-10 04:50:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af122dba-7a9d-3e9c-870f-90310f1c81f4 | 3.22385 | -61.19452 | 2024-12-10 04:50:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 238a85c9-bd29-346a-bcec-4e5a49cd9d66 | 3.21869 | -61.19596 | 2024-12-10 04:50:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33c77280-16ba-3bc7-a06f-679800fb1fb4 | 3.22453 | -61.19504 | 2024-12-10 04:50:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdc73eb8-9475-3da4-b440-64dc85a08054 | 3.23039 | -61.19421 | 2024-12-10 04:50:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 577925a7-58ff-3661-8494-ecaa90e10bea | 3.22392 | -61.19098 | 2024-12-10 04:50:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2ad5480-0a2e-3001-8adb-f2f02df5ea0e | 3.22977 | -61.19013 | 2024-12-10 04:50:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09108cfe-0b06-361f-b510-36d4e1a32c97 | 3.21801 | -61.19545 | 2024-12-10 04:50:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72db6d6e-750f-3d80-839c-9c080abaf0bb | 2.42483 | -60.65091 | 2024-12-10 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb2d9001-e478-336b-8bc5-32dbbae74d78 | 3.15605 | -60.72126 | 2024-12-10 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69e27c1e-a3de-3cdf-99cc-3aaada3c189b | 3.15278 | -60.71894 | 2024-12-10 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5467bad-cf1c-385f-aff7-0267a1d721a5 | 2.42984 | -60.64625 | 2024-12-10 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7c3717b-1b3e-3bfa-8ff6-e45b682874e0 | -3.87562 | -50.36437 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 14e12487-2b6f-3f96-a220-1b1dd4280a26 | -6.91659 | -43.5208 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a571eb28-5d4a-354c-b54e-3ad5db0419fc | -2.35375 | -53.86608 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eff2f0f3-3a47-3c67-a6dc-833ebda986b0 | -12.85595 | -51.93105 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3ef4d08-f210-3e2e-afa3-c2fbe997fced | -3.28553 | -54.14568 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c822929-df41-35d3-b9e6-3abe83fda055 | -2.4584 | -53.98137 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 212f6919-71ff-31a4-99ed-2d5bd7114ccc | -4.04504 | -54.09626 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 513e0f9a-385d-3380-92f2-79420bb81fb3 | -6.91162 | -43.51645 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6bc2a755-74a1-38e0-a2db-4178ebef8668 | -4.63425 | -49.4921 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e439bf0-b360-33a6-a560-713b9e0faaae | -10.50954 | -44.93174 | 2024-12-10 04:53:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a33aa298-66c0-3a65-82c0-e9788cc8a0a1 | -4.60988 | -49.48423 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f558729-a471-3969-86ee-ec325dc9de9d | -6.97488 | -42.99115 | 2024-12-10 04:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 21a2ac86-5a42-349b-91e8-172562ea0ec2 | -2.82321 | -48.08217 | 2024-12-10 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ea7652e-a1c6-3ca5-af3f-2b9c163f0d0b | -2.81509 | -53.03692 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b348efba-7e7c-3a41-8f9a-150dd78acf04 | -4.3901 | -47.75018 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7820399a-bdc7-3c8b-b55a-b5ae011cde7d | -2.92172 | -52.96405 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c9e9023f-5258-39ba-9bd0-decc530b4e17 | -3.52648 | -52.14342 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51cefb1e-1f7e-350e-ba88-1ba82ee3e585 | -2.8339 | -53.00411 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 691066f4-856b-3ff6-a590-86e59e7b5332 | -3.52318 | -52.14291 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ce7334f-d0d8-33dc-bebc-94df32f49195 | -2.72444 | -53.18155 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6e37fc2-8396-34e0-b46a-545aabc33fb5 | -3.28039 | -51.07983 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97865f16-ce6d-3e3f-9aa1-83c374f96197 | -5.99392 | -46.16022 | 2024-12-10 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c4153ef-9b4f-3218-9bda-a0bc0c2028d5 | -3.47339 | -53.46148 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 010b0f33-978d-3b9a-a922-ebc668260293 | -3.53221 | -53.9425 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 473b2327-5187-31e0-ba17-777302a2e88e | -1.67174 | -52.08438 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b58eeb3-cb37-3a85-92f1-f5e114e69434 | -2.45881 | -53.64202 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ebd3a77-4670-3f5d-ba99-e40808561be1 | -11.41651 | -54.32216 | 2024-12-10 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 923be4ed-542d-32ed-aedf-6d8b2aa5aeee | -1.64177 | -45.90751 | 2024-12-10 04:53:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 420097fc-cf88-353a-9cf2-f25eb2f6732a | -2.36635 | -53.8529 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README19.md)
