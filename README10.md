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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd2413dd-9ec7-39b9-bd74-887611e8ff78 | -12.1174 | -45.0397 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 235a5b5f-8dea-3bb3-92bd-3f52c42f0bd0 | -11.3747 | -45.175701 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac2d974a-44a6-356b-a238-9d543ecae0c2 | -8.2414 | -49.0494 | 2026-08-31 00:35:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 85f102ba-9bab-3724-af13-18b8fac47a61 | -8.099 | -45.4711 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 75c0babd-4162-3a19-91dc-71979d330cd1 | -10.7368 | -50.6549 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7f5eefb5-f844-34e9-baf4-5cbcb266121e | -5.9282 | -57.675201 | 2026-08-31 00:35:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 818626a4-a7b4-361d-92d9-08706f28ad7d | -8.1548 | -45.488998 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67789949-3865-323f-9a91-64d02a3bc566 | -8.3371 | -45.652699 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c18d05c3-d082-33d0-807f-2b7808a35f18 | -7.5439 | -47.3223 | 2026-08-31 00:35:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9797f8f8-3c30-3b26-aab5-28125a4b20b6 | -16.287901 | -42.587898 | 2026-08-31 00:35:00 | METOP-C | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6bfc48cf-2a89-3c38-8dc1-c47bf06c7c1a | -12.9226 | -45.856098 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 549abbef-d304-3a28-a446-0c9f38366d6e | -5.2478 | -55.875401 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b56afa7-3ad8-381d-9de3-5c277b0f2995 | -11.6884 | -47.614399 | 2026-08-31 00:35:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81da5f47-744f-324c-8e88-371152f790c3 | -12.7791 | -46.455101 | 2026-08-31 00:35:00 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf499ce2-4253-35f0-8b3b-f2158f6bc147 | -11.3552 | -45.225601 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bfbbc26e-c5f3-3998-8da5-ef4bb43ace71 | -14.2359 | -52.8624 | 2026-08-31 00:35:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 449b3ba0-0f9b-3812-b312-a84c26351f08 | -14.2042 | -46.566101 | 2026-08-31 00:35:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4d8af2df-c458-3f4a-ba94-8c5b150247f6 | -1.587 | -54.394699 | 2026-08-31 00:35:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f0ab01d-6dea-39fb-85eb-b9ad7423ce1f | -14.1773 | -52.874199 | 2026-08-31 00:35:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 389dffb8-f9d7-3a06-970d-6b907be89b13 | -11.329 | -45.201401 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f6ff0a3-bab7-3e5e-8d0e-a42f21f713b2 | -8.3734 | -45.765099 | 2026-08-31 00:35:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d62bf8b-ec97-3ec3-ba7a-6fa63d27287c | -5.5934 | -42.3251 | 2026-08-31 00:35:00 | METOP-C | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd3dc1dc-d81b-3236-af69-601625cec76b | -13.9282 | -54.412899 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd3214c0-af03-390d-9b16-49be0137d481 | -8.3818 | -45.000099 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1f56604e-9dfd-36f2-a6d0-c5d291561f29 | -8.3997 | -44.987999 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7fd0b1c0-d305-3c99-b05e-880882f529ba | -10.748 | -54.041 | 2026-08-31 00:35:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 753f49aa-5205-3a90-a2db-b0b8fd29cbef | -15.0712 | -48.003899 | 2026-08-31 00:35:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3522e4b8-0805-3f19-a660-9952594c43a8 | -11.3502 | -45.204102 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6a04dee-0f71-3d20-9a4d-df4c97c1006b | -10.7388 | -44.8811 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| beecf91e-a759-31bb-b14f-eec31db3f447 | -12.9447 | -45.953999 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05a3b0a7-cbaf-3e00-90db-4f3a7642e472 | -15.4009 | -52.7061 | 2026-08-31 00:35:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25232bf7-8d10-326f-aded-3058027445eb | -12.1093 | -45.049099 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 084ce6ff-35e9-31f7-b08a-bd5a5cae453a | -8.1352 | -45.4935 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e842d75-37df-358f-9fc6-e7b19908dfff | -10.727 | -50.657001 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c517fdc7-dc55-32dc-afe2-b9e9bf725805 | -10.7584 | -44.876598 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7da61dc3-3fa4-3f7d-8662-eff0cc44e4f6 | -11.3322 | -45.170502 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce9f680c-c9fc-33a6-bd07-7967b3959219 | -7.2883 | -52.377602 | 2026-08-31 00:35:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd8ba52-8c84-3bcc-a78e-25b16d097e64 | -10.7449 | -54.025799 | 2026-08-31 00:35:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f62fa4e0-7f92-3dc2-97b0-7bd4c3b37600 | -11.8827 | -45.817101 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3946e89-d38c-3b3a-a2e3-aec10c1e92a1 | -11.2389 | -45.1241 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c26ee42-421d-3081-ac2f-db5565ca46c0 | -12.106 | -45.034801 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 553e19ab-635d-3935-a0f9-ffa5c0c89a33 | -5.6093 | -44.0023 | 2026-08-31 00:35:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b268c0a6-b412-3044-9996-42a1a51e951a | -20.366501 | -47.464699 | 2026-08-31 00:35:00 | METOP-C | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 44c9235a-5888-301f-a852-fb6687bd1389 | -10.0554 | -48.696098 | 2026-08-31 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92de577d-3d20-376b-8d85-95dc7a383b8c | -5.2515 | -55.8923 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00b9cad7-d57d-37a5-bd17-f322c23d9b88 | -10.7452 | -44.864101 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 275254d3-0893-3338-be9d-b709b0cecd61 | -13.3698 | -46.935501 | 2026-08-31 00:35:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4947eb3c-5de7-33e1-9dd8-ebcb902b0efb | -15.6678 | -45.923 | 2026-08-31 00:35:00 | METOP-C | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1d4a68c2-b0dc-3f70-915c-384942504fc1 | -14.6079 | -54.113899 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 30499c72-8933-300d-9940-40f0e728f820 | -9.4368 | -45.677898 | 2026-08-31 00:35:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 61b78499-c09c-3cab-87f0-038e6dd7a29c | -11.3273 | -45.194302 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13bee504-c0d1-3841-9e24-d00cbc96718e | -14.4372 | -52.543701 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40e3b552-1667-3f47-981b-b4633078d3ee | -8.0909 | -45.480598 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b05c498-f096-3ad5-9021-015177c85773 | -9.4237 | -45.666 | 2026-08-31 00:35:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6db516b0-1683-34b2-be7f-3d421ea40e2a | -11.373 | -45.168499 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb217713-fd9a-3c26-b9c9-1bcc8d3aabcd | -9.4351 | -45.670799 | 2026-08-31 00:35:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 96724883-fe02-36fe-8244-36e117e14aab | -5.8606 | -57.785801 | 2026-08-31 00:35:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cbf5e7c-a409-3544-962d-4898086f4a00 | -14.2261 | -52.8643 | 2026-08-31 00:35:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc6e146b-7f64-3383-b8dc-5892da9f254e | -15.6277 | -50.091801 | 2026-08-31 00:35:00 | METOP-C | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d217b705-df42-3a81-b11b-28e84c16fa10 | -10.8508 | -45.3657 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7ab0fdf-0ab3-3ec9-be94-af850b618fad | -12.0846 | -44.986698 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 690a2ba3-2f0a-344c-9fe8-78051cf00795 | -5.4778 | -57.1306 | 2026-08-31 00:35:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d8eea85-1341-3bc5-a048-04e71f1cafb9 | -10.7352 | -54.027699 | 2026-08-31 00:35:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a4c1b7b-1493-334a-8a91-d048feb5fa8e | -7.7695 | -44.060699 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5e256a50-51f6-3e06-82cc-4989443a1f37 | -5.232 | -55.8964 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40afd687-7bb2-3b93-8976-e52a07dd3b8d | -18.3118 | -43.241901 | 2026-08-31 00:35:00 | METOP-C | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 522e9648-20ef-30be-819b-b97b61acd3c9 | -7.9262 | -44.994202 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a403a849-79c2-3f44-8106-0f82f898bfc6 | -7.0552 | -52.718498 | 2026-08-31 00:35:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59abd1d7-a549-364a-ba95-8c6d0815f90c | -10.7414 | -54.0583 | 2026-08-31 00:35:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6165176-b12d-376d-8f1a-c2a903e8fc99 | -17.5394 | -44.611698 | 2026-08-31 00:35:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ae763083-cf7b-36b2-8a94-18cb8ab92298 | -12.0995 | -45.051399 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 131c472b-9436-3893-ae5f-3d8e0569359a | -11.3388 | -45.1992 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a540a07-10b1-311e-93fa-5470a858328d | -12.7807 | -46.462101 | 2026-08-31 00:35:00 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abb7f60a-aa8b-322b-96a5-0e723437aef1 | -11.0833 | -51.519901 | 2026-08-31 00:35:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d2d1d36-0e47-3933-a73b-1a724b580c2f | -11.2193 | -45.1287 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6342bee0-747a-36a7-bd3a-731ac291b79f | -3.6873 | -52.0037 | 2026-08-31 00:35:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e542e54-21ee-35c1-bd1c-867accb071e3 | -10.8541 | -45.379902 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29a06725-9496-3acd-a845-c6723859c439 | -9.6673 | -50.873798 | 2026-08-31 00:35:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fed6856-4808-3b08-b07c-740a7bd55bb3 | -13.0887 | -45.180099 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 758a8979-fa57-301b-8726-6547625038ab | -15.6298 | -50.101898 | 2026-08-31 00:35:00 | METOP-C | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c558049-f9aa-3f80-91d8-63541eb214fe | -7.1255 | -46.0807 | 2026-08-31 00:35:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7c1966b-9718-3478-aae0-12ec5944d473 | -14.2057 | -46.5732 | 2026-08-31 00:35:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2ea6f1bf-7f83-3523-bb78-9e68755ada3f | -10.8393 | -45.315601 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3de1eb3f-b6ce-3133-b7c4-76a93ce60450 | -8.2316 | -49.051601 | 2026-08-31 00:35:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d8328bf3-0050-35a2-b81f-4218549594a6 | -10.8173 | -50.696098 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1dcb41a-b4b0-3d5c-9df1-59267e92a1ee | -12.9514 | -45.937801 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d2e702d-5cd6-33d5-8b63-aa7aeb72d632 | -10.1454 | -45.753101 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ce63442b-e130-31aa-90d9-54e183f50510 | -8.2397 | -49.042 | 2026-08-31 00:35:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 81a35ff9-3a3c-3f96-8f2e-79193adf09d6 | -11.3338 | -45.1777 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e74e9673-0704-3b6c-afc8-05709814b36b | -1.6021 | -54.415901 | 2026-08-31 00:35:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73ff79f0-13a5-323e-9140-9d7725335bc7 | -5.6072 | -43.993401 | 2026-08-31 00:35:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30584e2a-715c-39fe-bd74-6ae609828f76 | -20.3682 | -47.473301 | 2026-08-31 00:35:00 | METOP-C | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| db517bd7-b249-3e8d-a373-db4fdaf0f63e | -10.7469 | -44.871498 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1de47b27-6b07-38e6-abea-9164cbcdd66a | -4.9536 | -55.833099 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff4ea4ae-69df-318a-849f-b6264afb0e0a | -7.9781 | -44.2892 | 2026-08-31 00:35:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b74211d1-e012-3e1a-9f31-db2ff7f6d0c2 | -4.9669 | -55.847599 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d6ba03f-d87a-3ba4-a681-7aa9e1a5fce5 | -11.8761 | -45.833401 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ccdea0e9-3362-3171-bbcc-50b9a54f9286 | -12.3977 | -46.4543 | 2026-08-31 00:35:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67d067b3-9738-367e-a3c5-c29dd168a42f | -8.0875 | -45.466 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c3c10ef7-b541-34fb-a14e-f64602ae363e | -5.8703 | -57.783798 | 2026-08-31 00:35:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
