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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b735691f-ea54-33a9-9d22-ca06a80bfe77 | -15.14183 | -48.61076 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3bfb558-575a-3cf7-91e4-e02f434b92f6 | -19.98712 | -47.6263 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9d976989-834c-3620-a97d-7120d8991ef1 | -20.0744 | -47.52799 | 2025-09-11 04:25:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9388ad6a-017a-3a34-8479-a752c4b39285 | -18.15244 | -48.10015 | 2025-09-11 04:25:00 | NPP-375D | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49c8876b-561d-39fc-a0c1-7e1a9f7d9dde | -17.90238 | -44.60463 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf5fd7d5-8fd6-3687-b9f8-c1ec7e62f776 | -14.28489 | -54.76237 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb518c5c-0bf4-3e36-9493-21d9d0b5c48e | -18.06009 | -50.73011 | 2025-09-11 04:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cd01694-9ff7-3aa4-831f-a812279413b6 | -16.55859 | -49.74007 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd15a15a-957a-38dc-9a5b-43ae76e729d6 | -19.65894 | -44.89913 | 2025-09-11 04:25:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7711c740-42cd-3491-9f90-c1edff22dd29 | -15.59461 | -49.39352 | 2025-09-11 04:25:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a6b56c6-fec5-3159-9e6d-86602896087d | -15.61343 | -52.77017 | 2025-09-11 04:25:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdfd06ba-d0fc-3a5d-aa55-afd4767af2a6 | -15.28294 | -53.78874 | 2025-09-11 04:25:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e18ea737-720b-3fcf-b04b-13731b680471 | -18.91376 | -46.83394 | 2025-09-11 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36b36661-1299-3f1d-92da-19e4ca77ffa0 | -16.30197 | -50.06152 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 81a4f7f6-9831-3d60-a12e-0b6197b56f68 | -15.13905 | -48.60628 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38e36ff1-9e3e-3128-a996-58b8ab992632 | -19.66772 | -45.8534 | 2025-09-11 04:25:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 037392f6-3906-3ce5-a0c9-a3c8b321e674 | -16.06765 | -49.96859 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de557a0f-9feb-32f6-a805-a7e6a127b0f3 | -17.83707 | -46.73788 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8d7e9bc-4a93-32bf-9b36-49dcb5950271 | -17.82316 | -46.73927 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90d379c4-b799-3f60-9bf1-4835b9516da2 | -16.05898 | -49.97594 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27e8d1f8-1fc6-3997-a725-746487659c85 | -15.11826 | -52.401 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 253b8a32-3c2d-35d1-9625-f13908b7aa88 | -18.93746 | -48.70568 | 2025-09-11 04:25:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0abbac23-a34f-3cc6-8f87-bf2468046558 | -16.88763 | -45.76186 | 2025-09-11 04:25:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9ddbf8d-5a34-3155-a934-e3cbcced9411 | -17.50893 | -43.74856 | 2025-09-11 04:25:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a422330-428d-3015-b23b-9d0f1ff67520 | -15.9568 | -50.22054 | 2025-09-11 04:25:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3d515f4-8d28-3f93-969a-b87467fc208f | -20.35878 | -46.65746 | 2025-09-11 04:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 707a80ff-ecf8-3eb6-ac6b-a124898d37bb | -17.83374 | -46.73732 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df76199b-5cb8-3880-affd-a1acd64d3746 | -15.12248 | -52.40159 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92704710-8ba9-3369-8c19-d376212e2065 | -20.91 | -45.29002 | 2025-09-11 04:25:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 23b20a02-7918-3114-ac6c-85a8ff728b12 | -15.10071 | -50.07301 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32210a37-7a85-378c-96e7-05765bc54e9d | -20.54128 | -47.62613 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad06dde7-52b6-3e7e-942a-b41ef3bcab15 | -15.09785 | -50.06771 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4cb20a2-d145-3488-81e7-02d25b12f485 | -16.64174 | -47.73544 | 2025-09-11 04:25:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9595b126-fcb2-38cb-a3f6-4af25628cd5c | -22.83897 | -47.46881 | 2025-09-11 04:25:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 7f35871c-44f5-352b-9c4c-518ca93583f0 | -22.84175 | -47.47325 | 2025-09-11 04:25:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 7a8f341b-dac2-3f37-a5a7-b494e0d33139 | -15.16183 | -52.42253 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75d5820d-994a-301e-afb4-98fdac52698d | -15.51734 | -47.57853 | 2025-09-11 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f253bcb-53d8-3290-8acf-e42857522d35 | -22.69852 | -46.82177 | 2025-09-11 04:25:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| aa47bc36-1374-3bcf-973c-f754a92e923d | -15.14055 | -52.4438 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3cc8ff7e-4148-3585-b9ee-176ebcb56a9b | -18.57366 | -47.41928 | 2025-09-11 04:25:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5adbd696-e011-3528-8755-e84d1d4911fb | -16.06333 | -49.9722 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95537536-b877-3cb1-85db-fe996faf310e | -15.12178 | -52.40547 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08a245e5-d2c5-3b74-82c2-e2457f7d3572 | -18.45301 | -49.57035 | 2025-09-11 04:25:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9ece0db-70da-3076-bccf-aed5bf05244b | -16.65235 | -47.73353 | 2025-09-11 04:25:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 483f4402-11a0-3731-b9da-b89b999b290e | -22.31968 | -48.82841 | 2025-09-11 04:25:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2e1e301-363d-31ec-bb40-7ed039f4bb7d | -15.13207 | -52.44273 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 537de201-cb80-31f7-a732-04598c325e54 | -17.8474 | -44.21126 | 2025-09-11 04:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4f51245-9a31-39d9-b196-5b7a1ba041e6 | -15.0861 | -50.07036 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69353e9a-8915-3fdc-b180-e16c2e69fa39 | -14.72807 | -55.61528 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b691af0c-3234-32cb-be51-ec8dff1586af | -19.79978 | -47.16308 | 2025-09-11 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be4ca820-f03c-3fd6-975a-ae6a59c295e7 | -14.51771 | -53.93172 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86c5adc4-bdee-38ca-b44d-eb1092824930 | -20.70086 | -46.06626 | 2025-09-11 04:25:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 909bc37b-b180-34c4-930d-cf802f807f75 | -18.91616 | -41.11645 | 2025-09-11 04:25:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6a8a0a57-417c-3319-897b-cbabf7433916 | -15.66295 | -53.89507 | 2025-09-11 04:25:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdd924e9-8cd7-36fa-8eff-2d8d583dd5c8 | -16.08462 | -47.35091 | 2025-09-11 04:25:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 066b59f9-4ce6-3bbc-a141-ceb9d490bec7 | -19.98437 | -47.62202 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a15a61d-179a-3952-a905-4e43504f5564 | -22.52158 | -49.08997 | 2025-09-11 04:25:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 39557aac-0ae0-3f7b-94aa-7c2a61ad6a04 | -17.50464 | -43.75233 | 2025-09-11 04:25:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1b41233-574b-3045-842a-aefe84702ada | -20.90706 | -45.28522 | 2025-09-11 04:25:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 381f8368-4865-3dc5-abc6-ac40323554f2 | -16.54429 | -55.17817 | 2025-09-11 04:25:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| f184c6d3-038b-3c52-b225-6013ccf07c18 | -19.99103 | -47.6232 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 18a919d5-4421-32ac-b2dd-281e0e1690c1 | -20.3893 | -46.24129 | 2025-09-11 04:25:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2161687-7451-3f7d-8e3c-c03951b545ee | -17.73692 | -44.49922 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 386248fa-d1fc-3f4a-ab69-734c9da8ad80 | -15.55679 | -54.74711 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c9d257e-abdc-37cf-bc1d-2987f048ac72 | -15.80294 | -52.23179 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0682da62-203c-3000-8379-8ab883acb8fc | -19.65835 | -44.90331 | 2025-09-11 04:25:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bec5cdf7-9f3d-3e95-88a4-f23bbf11bee5 | -22.70325 | -46.33723 | 2025-09-11 04:25:00 | NPP-375D | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 150530c2-43da-3e68-8185-a5f501c6ffbb | -19.52279 | -44.68715 | 2025-09-11 04:25:00 | NPP-375D | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f38ece7f-7a56-30a7-aaa7-cfae6b51f42a | -19.20696 | -47.98574 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2f027c0e-12e6-302f-950b-4bc20b9f5a84 | -15.79546 | -52.24987 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bcd140e-9558-3696-979e-84b48d27ecf2 | -17.99565 | -47.10849 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c03d36d3-c829-34c2-9096-7e536f8ad9db | -15.89227 | -48.17666 | 2025-09-11 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31aa6d46-91bf-380f-ae1c-5ba600e7b056 | -16.49119 | -51.97952 | 2025-09-11 04:25:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dceb297a-8bd5-3e60-809a-42edc960f26e | -14.89327 | -55.84842 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67aad090-9402-3b5d-8454-d69f76cd09f4 | -16.26607 | -46.78286 | 2025-09-11 04:25:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d65b4b6-cc9e-378a-b93c-056e4ad5064b | -18.57423 | -47.41563 | 2025-09-11 04:25:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39757b08-356c-355d-b120-cd753ccfa530 | -16.2808 | -49.54305 | 2025-09-11 04:25:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 424d9624-8967-3016-a66c-2977260290fd | -19.64581 | -45.04228 | 2025-09-11 04:25:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee1db96a-5d1a-381c-a381-4486a69780ad | -15.1363 | -52.44334 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f628a764-08d7-3dd4-84d9-dfcb57857f43 | -17.84976 | -44.22045 | 2025-09-11 04:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7090d26d-6968-304f-997f-9e128ffad827 | -19.01274 | -46.25009 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61d4575d-90cf-3561-a0cc-1e5cd917fd79 | -16.5734 | -49.73868 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98f16b17-0c02-3042-b8d6-aac081bef695 | -16.51341 | -55.14714 | 2025-09-11 04:25:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 10587ddf-9171-383c-81ed-17324a7370fb | -19.99769 | -47.62438 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e23e227c-7448-30a3-a465-ffc107d241ef | -15.56062 | -54.75319 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 28e146ea-339e-30c3-b8f7-482d776a6fef | -22.26717 | -49.56264 | 2025-09-11 04:25:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c94a5eed-2ee7-3b78-a9bb-f4b3fe6d0e37 | -18.33184 | -44.35996 | 2025-09-11 04:25:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7decc26f-14eb-367e-873b-5a8403beacd8 | -19.98654 | -47.62998 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ce8d1f8f-8e3e-3987-b661-efdd66cfb375 | -15.80432 | -52.28292 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ca1f9c3-5e70-3cff-9328-bbecf16cdf56 | -18.5578 | -46.55913 | 2025-09-11 04:25:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b296d815-c1b5-32bd-8977-8032542c722d | -17.06878 | -49.67203 | 2025-09-11 04:25:00 | NPP-375D | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d854585e-6ebc-303c-a781-6f1bf04c5ea0 | -20.23856 | -44.81599 | 2025-09-11 04:25:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e2d9f5f-e3d8-3cfc-8825-2c119e0a201a | -19.95164 | -46.88046 | 2025-09-11 04:25:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0dc2cce-b5c8-3f62-8d70-acebccff2809 | -19.01838 | -46.25873 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 665340ec-b1ed-3c51-98ea-3599d1e1fb7f | -16.05973 | -49.9716 | 2025-09-11 04:25:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99679ff3-14d4-33d6-b483-a82449a70e9f | -14.3129 | -54.75039 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 763fbc22-5359-389d-888a-9050c15204e1 | -20.51954 | -47.63374 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b5d414e-aff0-384e-9c64-057cd6514137 | -16.42507 | -45.68828 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37ff6178-f495-3bba-a61f-8723c36e8021 | -18.15971 | -48.09766 | 2025-09-11 04:25:00 | NPP-375D | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9aa6860b-1173-3b61-bffe-b3e1ed97f3dd | -20.40178 | -46.2752 | 2025-09-11 04:25:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README76.md)
