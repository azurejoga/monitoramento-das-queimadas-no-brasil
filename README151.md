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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8b64165-86fe-350b-9cf2-cb7b76063492 | -17.59977 | -46.97843 | 2024-10-04 04:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d648097e-eb2f-3d3b-853a-ecd2dd7d1080 | -16.93443 | -47.12854 | 2024-10-04 04:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17ea99e1-2950-3ed1-be92-57f3a73d79e8 | -16.93403 | -47.13211 | 2024-10-04 04:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e8ea066-f9c9-3fc3-8aaa-8172032db4d1 | -16.93363 | -47.13565 | 2024-10-04 04:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4be6c819-657b-3b4d-9693-c18b06722901 | -16.93324 | -47.13921 | 2024-10-04 04:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36810e15-9282-3db4-ac8d-91cc2f4c4f79 | -10.9085 | -46.30976 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 248a5d16-81e0-308f-b4f7-24656f0adf78 | -10.90886 | -46.30688 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 237baf25-0a6c-3499-945b-2b3944d39426 | -11.98108 | -47.36776 | 2024-10-04 04:57:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 28413773-e07f-3cb4-8d54-c3b1dc378436 | -11.78946 | -47.57405 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| efd5ca0f-7207-376c-9f2d-eafabb3aab88 | -11.72911 | -47.69772 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b14cfcb7-ae53-3f10-affa-dae3cf358b52 | -11.72842 | -47.70304 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3bab546e-5e86-39c4-b6da-e672bd9bfbea | -11.7243 | -47.69725 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| df076f9a-619f-3b15-b2bc-8550c911d052 | -11.72366 | -47.70218 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 198f60b0-f35e-3f35-9860-c683a7b5b16c | -14.79875 | -48.09774 | 2024-10-04 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a23b0bc7-df1f-38b5-a357-e116574c1f0a | -11.71951 | -47.69664 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e6eb291a-a84b-3986-a186-7e7d30199252 | -11.7189 | -47.70137 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 16a74b37-2e3f-36b0-a871-f8aca263f8e6 | -11.71474 | -47.69585 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0ec11caf-b06c-3fb4-83fc-59fcb4d31aed | -11.71414 | -47.70053 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ebb0f359-a100-34da-b0b2-448a1f02a071 | -11.71377 | -47.74089 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a8f2e7a-5e11-331c-90ef-702ad38d3b2b | -11.70872 | -47.70472 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8911fa3d-c7c4-3992-9108-e2ebd473acc9 | -11.70111 | -47.68822 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f05f1e5-f475-3363-8f0a-3f862cd6dbc6 | -11.70025 | -47.69494 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 857dccb4-b729-3def-9ddf-2390c3746a50 | -11.69627 | -47.68796 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b0f689e2-7763-3129-acb2-1e55a94a7952 | -11.67677 | -47.68894 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 29c26eb0-a392-3fbc-9c6a-f30a6ea8244d | -11.67646 | -47.69053 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc3889f8-b1af-3733-8e09-48cd52298e78 | -11.67402 | -47.70972 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d5531364-7a39-3de0-8193-71d13ddf7977 | -11.67358 | -47.71278 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2456735b-5592-30f4-81a1-5b2a35058a9f | -11.67173 | -47.68942 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57b3a77c-df39-3b68-8498-e7af4d429516 | -11.67132 | -47.69326 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ed60cef-9514-354b-a80d-cd928a8cb138 | -11.67104 | -47.69482 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0da7bbad-ca23-3a47-82fc-2daf0f83d640 | -11.66883 | -47.7119 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58fba4c0-49b3-314d-b060-e0335d9e7e1c | -11.66634 | -47.69352 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a0887a28-c171-36ae-baf9-92f6269cda6e | -11.66593 | -47.69714 | 2024-10-04 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0c26b6da-e37e-3bb5-a5d2-b746f44448f3 | -11.38865 | -47.21321 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 891df29a-31fb-3e44-9389-a2f6c4394475 | -11.28452 | -46.91948 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ccc06b0-8246-3b80-8248-5c9ef21cb5b7 | -11.22256 | -46.96342 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8d92b1fe-024b-3232-bb62-95686d976193 | -11.22194 | -46.61254 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11a0c460-f672-3bba-b43a-7b54db880911 | -11.22155 | -46.61558 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1d7e30e-cb16-3bc6-80fc-3231281c57e6 | -11.20377 | -46.91264 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9afa084-cc03-387e-b6b0-1097cb96ce43 | -11.20338 | -46.9156 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 757306a3-3ac1-3c6c-abb2-759e65e7f433 | -11.19877 | -46.91179 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d01a9cbb-0617-307c-813d-443a9a3202d5 | -11.1143 | -46.49679 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8b013bd2-c5cb-3a7d-a175-c5b4a92504aa | -11.10914 | -46.49617 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7831fd93-2e77-3e72-82c4-167df7d017bc | -11.10402 | -46.49519 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a0a12979-c30e-31e6-81a1-0de37ca0784b | -11.09885 | -46.49464 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54827d3e-deb4-3dd3-a78e-037141b724e2 | -11.0985 | -46.4974 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11f3bbc9-ebc4-39e4-b160-5b0ea69d058d | -11.09512 | -46.5243 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 183fa797-9564-375e-a622-933b44849fcc | -11.09025 | -46.5214 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 43b26d06-4eae-3a96-ba7b-3d87b731f1bf | -11.08992 | -46.52405 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 27a30ebd-5337-3f6d-903e-41617725b75e | -11.08959 | -46.52666 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9991397b-b038-3195-89a8-3e9a4464a6ce | -11.08851 | -46.53524 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22f2b45d-d5ea-3fe2-bcfe-072da437b791 | -11.08445 | -46.526 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9229b4ac-e00e-3cad-bad0-df593c917de0 | -11.08219 | -46.52423 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba63ee88-b632-3d61-8638-0a1fd13aa563 | -11.08183 | -46.52694 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e53f8ad-b86b-3e63-ac5e-d0bf6a92f05f | -11.08106 | -46.53271 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8683d2d-e57c-301e-a3a7-63112992fe10 | -11.07862 | -46.5308 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dd975404-8446-3770-b8ae-11c63e37473c | -11.07824 | -46.53384 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 57e2bba6-79cc-3226-b862-0c9687170ca5 | -11.07778 | -46.51797 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9b5ba70-1448-3090-a5e4-f20708649295 | -11.07745 | -46.52051 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91ff82a0-36d3-3604-89f9-7678ec44d38b | -11.07491 | -46.51869 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02d195e9-b59c-3adb-9990-e3102680d54a | -11.06978 | -46.51788 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 922fadb0-d7d8-3368-a20e-0fbac493acff | -11.06528 | -46.53353 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff368a71-9a9d-3bf9-8b69-863e94de2c95 | -11.06015 | -46.53281 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c424706b-8ca4-3167-a3c9-2ba2377c00a2 | -11.05502 | -46.53209 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2209944-a3da-36e6-b29a-aba18a143086 | -10.91181 | -46.6118 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 12a72533-b4df-3614-a596-42713fa35704 | -10.91142 | -46.61478 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3dacff9-75cc-33ee-abd7-d33fd991a071 | -10.88951 | -46.62391 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8869694-f100-3ab0-81af-e0f971b52d5e | -11.38372 | -47.21259 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 974c6b6f-6f85-3969-b6e1-7602fd69c85d | -11.37879 | -47.21196 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f1db620-0254-347b-815d-c656cc317c93 | -11.37806 | -47.21755 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce5b99c5-29cc-3c03-8865-b040fe519777 | -11.29221 | -46.93895 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce9e9b84-5d21-38e4-a47e-ad77e1aa2623 | -11.28952 | -46.92031 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2671e289-e8ff-312b-9796-17d4d873de79 | -11.28835 | -46.9294 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32cafee6-1cd8-32d0-a0df-7d40e38ea9dc | -11.28337 | -46.92845 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4472060-ad55-3275-9409-905bd256b241 | -11.22178 | -46.9693 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 64f2589b-3c0f-37c0-9ace-e009fa36c157 | -11.20915 | -46.91051 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6864522-d6cf-370c-ab05-7d6804f6a7c1 | -11.19838 | -46.91478 | 2024-10-04 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5674dc42-6323-3527-b75b-ffa59144f862 | -11.11466 | -46.4939 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e164cf6-f1b0-3d2c-8945-4f7a3db48c26 | -11.11395 | -46.4995 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a184ef48-2237-3846-a147-d16b921a5db9 | -11.10949 | -46.49337 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a7f930db-15a7-3c19-9148-3c17d852e2a5 | -11.1088 | -46.4988 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 67f3595e-998b-3bb5-abbb-9638c899ae22 | -11.10437 | -46.49244 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d52bab07-4654-33d3-8964-ea43cbd8a886 | -11.10368 | -46.49788 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5f953a5a-b20a-3010-8411-c104d8cd2e5d | -11.09548 | -46.52143 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9bf752fb-df0f-31af-bd94-4bc0d53792da | -11.09477 | -46.52708 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c201ecf3-16a4-3606-bb5a-5ff125474728 | -11.09441 | -46.52994 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b39f11b-030c-36ab-a92e-94994684aca3 | -11.09366 | -46.49426 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b939719c-8ff4-362d-b802-cb43031ad64b | -11.0933 | -46.49715 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9a95eb9-b19d-31af-95e9-66508a36f5e6 | -11.0851 | -46.52079 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41fd7548-d986-3862-bd02-a3ee43732ec8 | -11.08477 | -46.5234 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c157031-bb46-3dc0-8a8b-6431c8a7e044 | -11.08375 | -46.53155 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eb0cb770-548b-3121-89f9-113fb3d2e430 | -11.08337 | -46.53456 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6bf740a1-216e-327c-87f1-84a2818ef2f9 | -11.083 | -46.53758 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| dc21206d-977c-3330-9397-c3e3f63b065d | -11.08288 | -46.51896 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85379f3d-c0a4-3fa2-b2e5-e1166832e880 | -11.08254 | -46.52157 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f7f5194-4ae1-376a-b187-9620201fd8b3 | -11.08146 | -46.52974 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 574f0544-f3b1-3095-8220-65177d4971e5 | -11.08066 | -46.53575 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| af9842f2-cfc1-391d-a7e7-20a5980c1804 | -11.07969 | -46.52228 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edad3e0d-551e-30eb-814e-9f3e8f542e56 | -11.07899 | -46.52785 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f832f44-8829-34d7-a093-fc11dcfc8547 | -11.07634 | -46.52895 | 2024-10-04 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README152.md)
