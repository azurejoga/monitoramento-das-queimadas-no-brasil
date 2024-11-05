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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 061797ba-fa74-3192-9e58-6f4b27c900e5 | -2.1876 | -48.8531 | 2024-11-05 06:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| b2b79ccb-8ada-39d6-8fa4-762e7cea74a6 | -2.8065 | -51.4855 | 2024-11-05 06:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d2f11bb7-de7c-3cb7-a561-9539207ea1c5 | -3.5446 | -47.3855 | 2024-11-05 06:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f19f7b4a-85a0-33ec-aa11-81e62c625213 | -3.5631 | -47.3847 | 2024-11-05 06:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 3e49af47-a9f9-394c-9926-f06ca809a657 | -2.6507 | -48.5629 | 2024-11-05 06:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 40ac1b0f-5c24-32da-9cff-99961d8e322b | -3.5446 | -47.3855 | 2024-11-05 06:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 29c8515a-d527-33b4-90a2-f0895ac7c4fc | -2.8065 | -51.4855 | 2024-11-05 06:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| cd38c08f-6479-3bd3-a280-41c9e9330f4e | -9.20263 | -71.92599 | 2024-11-05 06:37:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8b3dd64-7460-3833-9790-4288d29d50ec | -9.20765 | -71.92671 | 2024-11-05 06:37:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8974a7b4-b0e9-3b0f-abd9-42473c8447a1 | -2.6507 | -48.5629 | 2024-11-05 06:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 10ded4a0-415f-3b14-b11e-761b340d550e | -2.8065 | -51.4855 | 2024-11-05 06:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b73e7cd3-0f03-33d5-add5-6a0037d18ac9 | -2.1692 | -48.8536 | 2024-11-05 06:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 94baca0f-52b7-3dc5-a354-719f39c2a24c | -2.1876 | -48.8531 | 2024-11-05 07:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| e77b5b10-112d-3289-af42-42621a91e0e7 | -8.49619 | -42.09933 | 2024-11-05 11:59:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 00025f54-df35-3734-8bae-dc2d5c219893 | -7.95301 | -37.19828 | 2024-11-05 11:59:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 475822bb-586e-3339-a9df-d32990d5a1f8 | -8.25489 | -40.21057 | 2024-11-05 11:59:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 1fea99bd-954c-38a1-a02a-3a8faf5f7c1c | -7.75504 | -38.72152 | 2024-11-05 11:59:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 13.1 |
| b6428fe9-91fc-3ac9-81c4-f1f07753e6e8 | -8.35365 | -36.91757 | 2024-11-05 11:59:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9299ab41-cd9a-35a1-8716-b23f0f6c33c8 | -7.74806 | -38.72414 | 2024-11-05 11:59:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 6ca4815f-e98d-3c1f-89a5-eb22c8b2d827 | -5.01492 | -38.30221 | 2024-11-05 11:59:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 29.9 |
| b57c8ce8-b0a9-3582-9d77-36e93ad4ddce | -8.12871 | -37.51676 | 2024-11-05 11:59:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| f9831237-10bb-3c62-99c2-0da669fafd02 | -8.49878 | -42.08269 | 2024-11-05 11:59:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| d3c574eb-5c67-3163-8623-a8f80d19c3fd | -5.01345 | -38.31221 | 2024-11-05 11:59:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 1d97bdf3-fd9e-3074-9057-d1f9d092560c | -4.42609 | -40.64822 | 2024-11-05 11:59:00 | TERRA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 14.9 |
| caef822e-dcd1-3c72-9ba7-973c722e37b4 | -5.69283 | -39.06154 | 2024-11-05 11:59:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 7930f8fe-c528-340b-bbd6-ea5906dd96e0 | -7.95431 | -37.18937 | 2024-11-05 11:59:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 75ac7c88-b0c4-357d-aa39-c94e5bb3dec9 | -7.17005 | -37.88451 | 2024-11-05 11:59:00 | TERRA_M-M | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 71188589-b662-303c-a705-470e6d5f1d65 | -7.83352 | -37.38499 | 2024-11-05 11:59:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 054afc61-286c-37ab-a20a-0f6a15f1061b | -5.8869 | -39.54005 | 2024-11-05 11:59:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 62.4 |
| bf6ada17-ad83-3b78-9b6e-f8f73296430e | -7.60387 | -35.06974 | 2024-11-05 11:59:00 | TERRA_M-M | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 9c51d643-5be7-3cd2-8857-bc70b6be40aa | -6.79601 | -35.30857 | 2024-11-05 11:59:00 | TERRA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 13.3 |
| db767061-2d2c-3ea9-a632-bf72d8baba3b | -9.7681 | -36.38229 | 2024-11-05 11:59:00 | TERRA_M-M | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 835e8e5f-9412-3d8a-8e98-bcbfaf477f25 | -7.75354 | -38.73138 | 2024-11-05 11:59:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 12.7 |
| ac1af4f3-62e5-372f-9fac-7de3f561ce02 | -5.30646 | -38.62899 | 2024-11-05 11:59:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 3cf7e31e-820d-3c76-9dec-877852adf7fc | -8.40494 | -37.01286 | 2024-11-05 11:59:00 | TERRA_M-M | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 5b24b090-9d08-3cde-8e0d-33800150c8bd | -7.2329 | -37.33438 | 2024-11-05 11:59:00 | TERRA_M-M | MATURÉIA | PARAÍBA | Brasil | 2509396 | 25 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e094cc10-abfa-308e-bbc8-dc6e40bf2f2a | -7.83222 | -37.39394 | 2024-11-05 11:59:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 6cc799a4-524a-33a6-9a13-4b01133b817e | -3.83735 | -44.11459 | 2024-11-05 11:59:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 5ccd3770-8081-3062-baa0-7166e63d80fc | -8.13004 | -37.50777 | 2024-11-05 11:59:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 24b0fabb-8cc6-3a4c-8dee-729f4547df5c | -5.88863 | -39.52869 | 2024-11-05 11:59:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 45ce0d64-6bf8-3245-913d-a5ff0d4a0deb | -8.25309 | -40.22261 | 2024-11-05 11:59:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 44.7 |
| 944edc2a-a92f-3536-a79f-989453d4b0cb | -6.68811 | -36.76741 | 2024-11-05 11:59:00 | TERRA_M-M | SANTANA DO SERIDÓ | RIO GRANDE DO NORTE | Brasil | 2411429 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ff025d0a-b2c1-3619-b8f6-307845ad14dc | -9.77701 | -36.38354 | 2024-11-05 11:59:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 97.9 |
| 4d0ed0ae-7c54-3d21-af49-eb97cd038f80 | -7.61303 | -35.07097 | 2024-11-05 11:59:00 | TERRA_M-M | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 45fea4a4-cf35-3f98-99e0-90287dfdc3ef | -3.7003 | -42.7426 | 2024-11-05 12:00:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| a5e09328-7ebe-3276-af4b-8cc18a2bbc1b | -13.66191 | -41.56775 | 2024-11-05 12:01:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 52b3b7aa-36d0-3eb6-a7ed-d380228e0045 | -10.01326 | -43.79757 | 2024-11-05 12:01:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| f0c10bab-7fc0-34ba-a7c9-04de5acb59d1 | -12.59388 | -45.47799 | 2024-11-05 12:01:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 6a48e8c4-da71-386d-afeb-8ab970f34b0f | -10.20952 | -39.34768 | 2024-11-05 12:01:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 54429eca-3943-3f1d-a853-e95edb1b153d | -12.59431 | -45.44558 | 2024-11-05 12:01:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 71fda6f5-7e3f-3d66-b6a4-224ceac0f2ae | -10.01486 | -43.79214 | 2024-11-05 12:01:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| c026de14-e339-3f63-83b5-56badabc9518 | -14.14753 | -43.21718 | 2024-11-05 12:01:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 068466a8-687a-32f8-bdc4-68c2314579e8 | -11.3998 | -40.0833 | 2024-11-05 12:01:00 | TERRA_M-T | QUIXABEIRA | BAHIA | Brasil | 2925931 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 3b489178-74de-3a92-ab11-893eea89735f | -9.87454 | -44.96325 | 2024-11-05 12:01:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 1a127ff4-5c21-3c54-8925-7e1dd38ba170 | -12.59825 | -45.45312 | 2024-11-05 12:01:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 015cb0e3-8bdb-309e-be97-566a1595e417 | -9.87743 | -44.97093 | 2024-11-05 12:01:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 3de73b88-087c-3af0-b8c9-02d848b6106f | -2.3061 | -46.5046 | 2024-11-05 12:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| a287b322-99ee-3b80-a171-dbb4eeda828f | -3.7003 | -42.7426 | 2024-11-05 12:10:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 086ec09c-582f-3fec-8fd3-75239b588faf | -2.2875 | -46.5051 | 2024-11-05 12:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 419e1c32-afbe-3322-b81c-f4bdf2b3b7ea | -2.3061 | -46.5046 | 2024-11-05 12:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 17a588b9-16f9-3183-ae3a-ac352cf8a13a | -2.8065 | -51.4855 | 2024-11-05 12:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| b9ab1509-492b-32ca-ac2f-0c34d727c4e4 | -2.3061 | -46.5046 | 2024-11-05 12:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 24bbea33-5e38-3ef5-95c4-c922f7a26746 | -2.8065 | -51.4855 | 2024-11-05 12:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 829bd020-a57e-3269-ae1a-c2203f5de8b9 | -4.3222 | -44.743 | 2024-11-05 12:40:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| f8953588-9787-3008-8843-578ec0d0bbc8 | -4.0667 | -46.9246 | 2024-11-05 12:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 719efa19-b8b3-3abd-9b9e-1f39e21b444c | 3.5264 | -51.257 | 2024-11-05 12:50:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4aa6d639-2e9f-3e7e-a18b-81a0f8827f18 | -2.8065 | -51.4855 | 2024-11-05 12:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| b0b3864d-3920-3c67-88be-8bcd5467046b | -4.3222 | -44.743 | 2024-11-05 12:50:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| e0ae97d9-1805-3c99-b777-71f36a36b7e8 | -4.3222 | -44.743 | 2024-11-05 13:00:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 222.7 |
| 74b7e909-6753-3d0c-91da-70ffcb509e11 | -2.8065 | -51.4855 | 2024-11-05 13:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 153.5 |
| a2f3cbf8-fd61-351a-805c-7a5c0de1ac5d | -2.8064 | -51.5061 | 2024-11-05 13:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 95b63237-6bd3-3cc9-b873-9ddd44901400 | -4.0667 | -46.9246 | 2024-11-05 13:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 08c74c38-a39b-37df-a474-7d3c4862f98c | -2.8065 | -51.4855 | 2024-11-05 13:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 2f944a39-1cf5-3041-aaaa-74a7b54ebff7 | -4.0667 | -46.9246 | 2024-11-05 13:10:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 72ecde3e-ae1a-3afe-899e-a349f392ff08 | -2.8064 | -51.5061 | 2024-11-05 13:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| fa88acef-fd77-33b3-9d66-890c8312c2f9 | 0.2116 | -51.0249 | 2024-11-05 13:10:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 5d336133-e4bf-3b1c-b6b7-ba39401e851d | -3.8227 | -44.1293 | 2024-11-05 13:10:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| dbd3ac1d-5c90-33bd-8212-17b27ea2867f | -4.6877 | -45.8056 | 2024-11-05 13:20:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 0336a0ca-7a00-390b-b4c9-5c90875251f4 | -3.4956 | -46.0649 | 2024-11-05 13:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 49fa1117-0d49-3b5c-959f-019a73f58de6 | -4.0667 | -46.9246 | 2024-11-05 13:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 6dbba88a-9327-3129-9903-7a838ff72a6f | -2.8065 | -51.4855 | 2024-11-05 13:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 214d1292-31eb-3b76-98a7-66bf5f1d59c8 | -2.4197 | -45.8355 | 2024-11-05 13:20:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 102.8 |
| e91bde5d-304e-3f31-81f4-84182670f3c8 | 0.2116 | -51.0249 | 2024-11-05 13:20:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f76c44b2-dcf7-3e5d-b5e6-ef8ce6b2bf52 | -2.4197 | -45.8355 | 2024-11-05 13:30:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| e1706b9b-9bd7-397d-aa98-a13308c46157 | -8.5002 | -42.0747 | 2024-11-05 13:30:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 9fff3c3c-4917-3b7d-b09b-2c3b3a63ab15 | -4.6877 | -45.8056 | 2024-11-05 13:30:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 3f83ceb0-e236-35a2-9d5b-d58af95c6422 | -1.514 | -53.512 | 2024-11-05 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 29182744-eb7f-38e7-b42b-fc56f2a8838c | -3.4956 | -46.0649 | 2024-11-05 13:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 211.8 |
| 95986f7e-c3fc-37c7-b135-bd32838d6325 | -2.6507 | -48.5629 | 2024-11-05 13:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 0cb02fee-214d-30e0-91cf-d982d81ceecb | -2.8423 | -51.7942 | 2024-11-05 13:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| c811d78e-bee2-3500-b068-ec891bab935b | -1.514 | -53.512 | 2024-11-05 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 9d11f7dc-ebec-3bfb-8e40-8809f5f3620b | 3.5264 | -51.257 | 2024-11-05 13:40:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 30c0cc20-540d-3fd8-a043-3b82f80c3a95 | -1.514 | -53.4918 | 2024-11-05 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 034e1d59-5314-3145-af06-a3f681e1da96 | -3.9445 | -45.5755 | 2024-11-05 13:40:00 | GOES-16 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 123.1 |
| a1c6a0a9-db72-3558-973d-a659dd11a3d1 | -8.3281 | -43.6091 | 2024-11-05 13:40:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| fcd8a2a1-b5b6-3e64-92cc-203aa7d52365 | -3.4956 | -46.0649 | 2024-11-05 13:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 767f18ee-7576-3eec-af4a-f85a9a60ecc5 | -2.6507 | -48.5629 | 2024-11-05 13:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| a7e75fd6-cb7f-3b42-ab47-bb332561c946 | -3.4956 | -46.0649 | 2024-11-05 13:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 126.0 |
| aff21139-9f27-349a-9815-0b0ff1a4c357 | -1.514 | -53.4918 | 2024-11-05 13:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 85afbfd8-a01d-3cd3-819f-5f5ca1799ac6 | -2.8423 | -51.7942 | 2024-11-05 13:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |


[Clique aqui para ver as próximas entradas](README34.md)
