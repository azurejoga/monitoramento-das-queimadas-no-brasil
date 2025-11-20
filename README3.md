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
| cb7d1648-09ca-3470-a34d-e30bf7155df2 | -3.01367 | -44.45626 | 2025-11-20 03:40:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daaea5a0-4f21-3ff6-acc0-5a45165cbb4d | -3.55531 | -43.47494 | 2025-11-20 03:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0af17ae0-f044-3cd5-acc4-8a01b6e75a21 | -3.01302 | -44.46015 | 2025-11-20 03:40:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0df40fe4-521c-39dd-bc58-233cbfeedbd9 | -3.25266 | -42.55731 | 2025-11-20 03:40:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8e35609-88fd-3c5c-ab7b-e82c7e67e54d | -2.93963 | -40.28768 | 2025-11-20 03:40:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 578fac6d-e4f7-3733-967d-41c42c9f6dfa | -2.51101 | -47.80654 | 2025-11-20 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4ec0b151-6fde-32c2-b5af-d07dccabd5cc | -3.55999 | -43.47472 | 2025-11-20 03:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ef0becb9-3d3f-342e-86e3-50c5556e0060 | -2.93265 | -45.04829 | 2025-11-20 03:40:00 | NOAA-21 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f1504fd2-dc34-3b40-b88a-d458b75fe93f | -3.23419 | -44.84963 | 2025-11-20 03:40:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c74494fc-62a3-3d5f-b24e-cda802143926 | -3.57271 | -39.78224 | 2025-11-20 03:40:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 89bb1394-653d-3e4f-85f6-554d04fe0b51 | -2.12816 | -46.19146 | 2025-11-20 03:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 730fe98b-051f-32a0-922d-d708463805b3 | -3.66153 | -40.90284 | 2025-11-20 03:40:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b8ba81b1-01f6-3ac5-9119-ba7a77734cd5 | -2.9124 | -40.40063 | 2025-11-20 03:40:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1afd87e9-473b-3b93-8e47-da71a342a20a | -3.55477 | -43.47824 | 2025-11-20 03:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 12bc1cdc-6bf3-319e-91aa-cecbe073d34c | -2.93193 | -45.05262 | 2025-11-20 03:40:00 | NOAA-21 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2769049e-c2fc-38d2-9675-3b5bca42975e | -3.55943 | -43.47801 | 2025-11-20 03:40:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5d81467f-0270-38e3-9836-0f41eb2698cf | -2.51347 | -47.80363 | 2025-11-20 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1406a30-6b75-36f9-b06d-f5ac49ad7d28 | -4.67393 | -43.21829 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 89ae86de-9b14-37c0-8716-0e39dfeebce0 | -6.85077 | -35.17566 | 2025-11-20 03:42:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 080046da-16a4-3eea-99c6-5289aa417987 | -7.27175 | -48.03034 | 2025-11-20 03:42:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 855c81af-e289-3f94-bcf9-dc470cd94887 | -6.23464 | -48.05635 | 2025-11-20 03:42:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b67a441-79fb-30c4-88f3-5559c84e37ff | -6.66773 | -39.77901 | 2025-11-20 03:42:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83728441-f452-3b6c-97c9-15f31869c93d | -4.68413 | -43.21995 | 2025-11-20 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c9ca3c7-1639-38d2-8d00-adeb051f9bfc | -4.14681 | -43.67701 | 2025-11-20 03:42:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 342ca6f6-82bd-3ff1-94b6-5b4f76206f88 | -4.67061 | -43.21949 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1b76b8f2-b1f1-3172-a2f7-88c307ae03dd | -4.66832 | -43.2204 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68bddb87-657a-3bc7-a116-b560a4f29e5c | -4.65974 | -44.10969 | 2025-11-20 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb35943a-299a-3ed0-bf91-52b493ff4977 | -6.69038 | -38.06275 | 2025-11-20 03:42:00 | NOAA-21 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5af70eb6-3125-3124-804c-4f4d82a48982 | -5.93362 | -35.64359 | 2025-11-20 03:42:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 27cfec5e-0237-376f-bbbc-3a5e06f7347f | -6.23345 | -48.06277 | 2025-11-20 03:42:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86de2992-e5b3-385a-93a3-af514789469b | -6.68683 | -38.06217 | 2025-11-20 03:42:00 | NOAA-21 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dcdc16ed-8af4-3e3c-9eb1-f2693efc6b14 | -4.67342 | -43.22125 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6c68f101-b504-353a-ace8-77e015528db5 | -7.02901 | -35.19008 | 2025-11-20 03:42:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 331bb9f6-76d7-3bfe-9e8c-016f5db221c7 | -6.85023 | -35.17912 | 2025-11-20 03:42:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 26782bfc-0f87-3986-a23a-29dacb17c1e6 | -6.76467 | -37.84903 | 2025-11-20 03:42:00 | NOAA-21 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce567cfd-7025-32c4-b0e2-621894a0e366 | -7.33884 | -35.08 | 2025-11-20 03:42:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 111f08dc-67e1-36f6-ae20-f047f6cfd559 | -6.76539 | -37.84826 | 2025-11-20 03:42:00 | NOAA-21 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0613d701-a522-3eb9-912f-240d4101c04b | -4.66962 | -43.22547 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0fd59490-bd5b-3f18-a8f2-e262d9c3a982 | -4.68081 | -43.2212 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5699f95a-72b0-35d4-aec1-f6eac16b66c1 | -5.91815 | -35.84847 | 2025-11-20 03:42:00 | NOAA-21 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 307e64c0-3433-3495-a527-67822f3a8cd4 | -4.13497 | -43.83257 | 2025-11-20 03:42:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 702e5a35-986c-3e7e-85b6-d1832a4e3c7a | -4.66032 | -44.1063 | 2025-11-20 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f87c72dc-4d35-3e90-8d2f-396d28cac6f3 | -5.99677 | -35.39417 | 2025-11-20 03:42:00 | NOAA-21 | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 34d3544f-4438-36d8-a47d-d8afb7473256 | -6.66456 | -39.77556 | 2025-11-20 03:42:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0f58471-3b57-3509-800c-375141576651 | -8.14522 | -35.01168 | 2025-11-20 03:42:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 3b89bf1b-fd8e-3688-a770-17d38a8a3e0d | -7.26509 | -48.02928 | 2025-11-20 03:42:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19f35ffc-39cb-3532-a42d-7f7bdc208b26 | -5.81505 | -35.55318 | 2025-11-20 03:42:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db7497eb-1820-3275-ab8b-35c92c3942a6 | -6.68973 | -38.0668 | 2025-11-20 03:42:00 | NOAA-21 | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dea27b90-c297-3019-8dad-2123c94a50e2 | -4.1404 | -43.68278 | 2025-11-20 03:42:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1430f24b-e462-3593-8aa2-5475caa971de | -4.67852 | -43.22211 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 485ecfc4-a5c4-3c03-bb9a-4c8aec68233b | -7.02847 | -35.19353 | 2025-11-20 03:42:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1d0ba1b5-6e25-3a9b-8826-8fa7b9c2d436 | -7.38557 | -35.25737 | 2025-11-20 03:42:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| c475914d-0923-3861-b303-88787cf741c2 | -4.14095 | -43.67946 | 2025-11-20 03:42:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac6e2083-6d08-333a-adbc-5ccfefd211bd | -4.67571 | -43.22033 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e7ad554d-03a4-33f1-a735-da2e278a408d | -4.68361 | -43.22298 | 2025-11-20 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b96d773-fde7-3d90-96d9-ba88c4b9af0e | -4.6678 | -43.22338 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7694fce8-538a-3e3a-9904-8324b00d3b56 | -4.67903 | -43.21911 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38e43d7b-5682-3cc2-8492-a8ba2d3a3848 | -4.67521 | -43.22335 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ade93bbc-d8c6-388a-8970-399d078449b3 | -5.61384 | -37.46951 | 2025-11-20 03:42:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 237d8ea3-cec3-3d63-b17a-e05a8f33d208 | -5.49677 | -39.16541 | 2025-11-20 03:42:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d1552c3f-679b-3768-863b-a24cdf9344d5 | -5.90799 | -39.23851 | 2025-11-20 03:42:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d79b7d1d-d7d5-32b2-a41e-401608e6389c | -4.6729 | -43.22424 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 49a9ad0e-4d55-3116-b7ba-7af5c5145a73 | -4.66883 | -43.21745 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ef9320b-81d9-39ba-bf4d-7286b677895c | -5.99401 | -35.3902 | 2025-11-20 03:42:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 637e6b72-59a1-3a84-b44a-a00721f8acd8 | -4.67012 | -43.22247 | 2025-11-20 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 52b1ed4d-993f-3eef-a4eb-f9c0c54d72d5 | -6.84969 | -35.18257 | 2025-11-20 03:42:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7c55519a-a80e-343a-8316-f998eb7948ae | -5.64707 | -37.42631 | 2025-11-20 03:42:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d0ea027b-a678-3003-b862-7259acbb4798 | -13.4887 | -46.70821 | 2025-11-20 03:44:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6ba47adb-e272-3d6c-a663-a235350fd3a3 | -15.78651 | -43.35901 | 2025-11-20 03:44:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3ff4d4c-b68d-35f5-a0d9-d1287e224629 | -10.36092 | -48.89663 | 2025-11-20 03:44:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8cd1ff69-c491-35cd-949b-eeae9121952b | -15.54008 | -50.66518 | 2025-11-20 03:44:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a73c63ef-dad9-32ee-8405-4c924e421103 | -12.88259 | -50.15239 | 2025-11-20 03:44:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cdca5d61-cde7-357c-8363-a461ef63434b | -12.94299 | -47.70956 | 2025-11-20 03:44:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94dd703d-4623-3b30-bed1-5bc367118dbe | -15.8865 | -43.45553 | 2025-11-20 03:44:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6708bea5-6c26-3189-981e-e8ec4828aa4b | -14.67269 | -46.52327 | 2025-11-20 03:44:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccfb2e6d-051c-36fe-b8d3-2b99eecd740d | -14.53012 | -48.62308 | 2025-11-20 03:44:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9348f1ec-8cde-3e05-9fd0-6d9728216b58 | -13.93983 | -47.45449 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8dc8198-3bc6-3063-a1cc-f7d9963c94f0 | -13.9299 | -47.47433 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8bbf1c7-f6b6-3c21-925a-3540a2474d90 | -13.93907 | -47.45826 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f827700-a2ae-3df5-ab72-f6a30c1cf744 | -13.94137 | -47.45369 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f836e9e2-8a74-3634-a478-edc2e5208088 | -15.89077 | -43.45634 | 2025-11-20 03:44:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ca2b349-e3b8-3a7b-8afc-f72140727766 | -15.45917 | -45.96047 | 2025-11-20 03:44:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1a22eee-94c3-37ef-8b09-85bb955806ed | -15.53813 | -50.66312 | 2025-11-20 03:44:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7421441a-59f8-3779-950c-9141bece90ac | -11.26226 | -48.49123 | 2025-11-20 03:44:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bf5c012a-80d5-3eb3-a024-c9c2a7cad5d3 | -10.36759 | -48.89773 | 2025-11-20 03:44:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3dccf87c-bc0a-33da-95a3-ca34159dc662 | -15.54673 | -50.66686 | 2025-11-20 03:44:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 98bc13d9-42e6-3765-af70-4ac002c04390 | -11.26381 | -48.49081 | 2025-11-20 03:44:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 290c1282-9874-3ccf-8601-ce57fcfbcd2f | -15.54148 | -50.65897 | 2025-11-20 03:44:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2804cf68-d76e-34d6-9eb3-3068b374c5b8 | -11.26273 | -48.49613 | 2025-11-20 03:44:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| afab823c-7d81-3406-9742-92454a9cb238 | -13.94322 | -47.46727 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e83f089-d815-30a5-a607-badedf424d42 | -10.48672 | -49.37155 | 2025-11-20 03:44:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27718830-1f18-32b3-a51d-4f5b8fbc53e9 | -10.35976 | -48.90242 | 2025-11-20 03:44:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 132aa6b4-355b-36b9-96ce-30fb175ca5f9 | -10.36643 | -48.90351 | 2025-11-20 03:44:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1cb6b9a9-55ba-3e2b-bceb-dc0e20ba99c9 | -14.6668 | -46.52509 | 2025-11-20 03:44:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28fca5a4-123d-38db-a6c7-577fb43544bf | -15.54343 | -50.67097 | 2025-11-20 03:44:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8ee6eccc-c2d9-3a0f-8970-3d379b0f500f | -14.5423 | -48.62542 | 2025-11-20 03:44:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96728ba9-c01f-361b-8c6a-c5118bceb210 | -11.25741 | -48.48968 | 2025-11-20 03:44:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b00e4c12-8c07-3f42-a696-032032721172 | -11.26121 | -48.49652 | 2025-11-20 03:44:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ac843f1c-53af-3359-8c71-bbfdbe5e1668 | -13.51701 | -47.91231 | 2025-11-20 03:44:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0668d9c2-e8ab-36f8-aa82-e4acd821bff7 | -15.54814 | -50.66062 | 2025-11-20 03:44:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README4.md)
