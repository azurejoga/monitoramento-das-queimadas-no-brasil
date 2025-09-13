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
| 0fba8306-4c5c-3a54-8e92-e090552bc516 | -17.3622 | -42.7029 | 2025-09-13 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 728f3d8a-9242-3247-a4a2-d642cef0eab1 | -22.2271 | -48.5684 | 2025-09-13 00:30:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.7 |
| a8208c7d-7024-3619-baff-60120867c8bf | -3.2282 | -47.6371 | 2025-09-13 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 166.7 |
| d5a8f681-1e3c-3c9f-a620-de4e0a86ae32 | -10.9283 | -47.2223 | 2025-09-13 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 4d984769-2625-338f-85f1-e270a9401762 | -9.2658 | -59.3997 | 2025-09-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| e635176f-bc1d-3ef7-9294-bef999d00f2f | -9.2843 | -59.418 | 2025-09-13 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a9ab939b-33b4-3210-8c77-831e6431817e | -11.1706 | -51.4209 | 2025-09-13 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 225.7 |
| d632fe1c-71de-37d3-8a7f-37cf60e5f857 | -9.5004 | -55.9788 | 2025-09-13 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 39ade260-844c-3264-b16d-dc2e58656382 | -9.4993 | -46.4299 | 2025-09-13 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 3acde65c-bd15-3e17-adf9-d5caa422d609 | -11.1321 | -51.4672 | 2025-09-13 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5936a552-5a78-3c91-82a3-e3c4b18013b3 | -20.5958 | -50.3814 | 2025-09-13 00:40:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| 282f921c-c478-3593-af8e-1fad255b1490 | -3.2305 | -47.135 | 2025-09-13 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| a5068de3-b731-3b0f-b589-54434a976a39 | -16.4906 | -55.1276 | 2025-09-13 00:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 176.3 |
| 30f22370-ba7d-35f3-972d-3e12ad6f0d51 | -7.9488 | -46.8996 | 2025-09-13 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| cf74c3b2-b6b0-35ba-9662-d467e5fe4e5e | -16.0257 | -47.9294 | 2025-09-13 00:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 89302872-dbf0-33a2-93ed-74b30f254468 | -17.3622 | -42.7029 | 2025-09-13 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 74ff4793-ba5d-34e4-937a-4c385d85acb5 | -12.9292 | -54.7538 | 2025-09-13 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 19b4cb7f-73c3-3137-8742-637ebf3808ba | -11.8281 | -50.562 | 2025-09-13 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6178a12a-37e8-3f88-b2f7-02a6beed7347 | -9.5135 | -54.6494 | 2025-09-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 68ee2a31-b999-3aba-a0e3-5cb799148b4f | -11.1709 | -51.3998 | 2025-09-13 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 4134cb43-93c7-33c9-a204-eb584b7840fc | -16.0061 | -47.9329 | 2025-09-13 00:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 6878856e-12d8-32b1-a5c9-ea66951ae2ca | -20.6156 | -50.3998 | 2025-09-13 00:40:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 187.6 |
| 2b9fdf74-49a3-36fb-8f62-f635696fd4f5 | -9.2656 | -59.4191 | 2025-09-13 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 162.7 |
| f9947e31-c3c4-3930-b898-8b5d1f3f91bc | -9.2503 | -51.2472 | 2025-09-13 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| d039b13d-008b-3435-9f56-2658d7f8c1a1 | -16.4903 | -55.1484 | 2025-09-13 00:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 989e8e04-bb43-3655-8217-134a04b4ae48 | -9.5006 | -55.9588 | 2025-09-13 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 3e31f7fc-3e5f-3e14-8394-3bbebf5f209d | -14.4394 | -47.3206 | 2025-09-13 00:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 7ecb679e-65cc-3cde-af87-58f878071d5f | -9.7108 | -47.5418 | 2025-09-13 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1fb289a1-b732-3f82-b273-05b86cbe8ffd | -12.006 | -47.7505 | 2025-09-13 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f9d3f08b-7f9a-309c-9c36-5152d7f0670b | -16.2541 | -50.0745 | 2025-09-13 00:40:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 98e131f0-e549-3696-ab92-20fbd7a1305b | -17.2836 | -47.2364 | 2025-09-13 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 2894bc15-9418-39de-afc5-021452d7976d | -9.2844 | -59.3986 | 2025-09-13 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 4378c07e-e257-3403-b1e1-3f291103af59 | -10.7661 | -50.5513 | 2025-09-13 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| daaf9d86-848d-317f-a217-cf0bef1d6168 | -16.0454 | -47.9258 | 2025-09-13 00:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 48caadb5-38e6-3aad-bbef-b5c0f692d053 | -9.4817 | -55.9801 | 2025-09-13 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| ecc52c6e-2439-34fd-ab4f-ce7656ab9389 | -9.5191 | -55.9775 | 2025-09-13 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8d465622-e6a7-30f0-b8a3-644c7439599c | -9.5137 | -54.6292 | 2025-09-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 167.1 |
| ccb2ea66-0fea-32da-865d-6d89079cff4f | -3.2321 | -46.7836 | 2025-09-13 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 852b788f-ffe1-3220-b9e6-be794df94528 | -19.6639 | -45.8713 | 2025-09-13 00:40:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 7674ce6b-1633-39ca-8020-d83dfe7a96dd | -20.6162 | -50.3771 | 2025-09-13 00:40:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 453accbc-34a7-3739-86dc-5eade53925e1 | -9.247 | -59.4201 | 2025-09-13 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| bceb9d55-24dd-3e45-b900-b2c21babb148 | -11.7232 | -44.2146 | 2025-09-13 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b8740e52-d202-30af-9349-dd95cffce1a3 | -9.2472 | -59.4007 | 2025-09-13 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 2ce6ef8b-f2e6-314b-aff2-f1a8e8c4820a | -9.2505 | -51.2261 | 2025-09-13 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 278b266d-f874-30dc-b515-54b8bd18d949 | -12.0056 | -47.7728 | 2025-09-13 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 397bfb93-bc6f-378d-af43-cee3ce2b846e | -9.2658 | -59.3997 | 2025-09-13 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 161.8 |
| e9f1db53-feda-3f73-832b-727dbff6258d | -20.5952 | -50.404 | 2025-09-13 00:40:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 194.2 |
| a5be37ba-83e1-3c1a-9d0a-25f7daa51525 | -9.2843 | -59.418 | 2025-09-13 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| cb425500-5c0d-368e-815a-10211f22c4a8 | -22.2473 | -48.5869 | 2025-09-13 00:40:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.1 |
| ee55c01e-9159-3f7b-aa1a-4d6c8974a01d | -22.248 | -48.5633 | 2025-09-13 00:40:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.0 |
| 839e815c-6e1b-34d4-a8c5-ca3b2c099d75 | -9.4819 | -55.9601 | 2025-09-13 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 11540e7a-0fa5-329d-be8a-aa7f30c05975 | -16.5102 | -55.125 | 2025-09-13 00:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 116.9 |
| 0a40b517-8f20-3526-aa2d-84ddc99784d2 | -9.5324 | -54.6277 | 2025-09-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 36c03e75-ec9c-33c7-bf45-207250c9f810 | -15.6966 | -50.5793 | 2025-09-13 00:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 529fd273-90dd-3637-a37e-f0dac32c078e | -18.6139 | -48.2044 | 2025-09-13 00:40:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 25565928-ce68-3b27-98db-776777b5f983 | -11.1703 | -51.4421 | 2025-09-13 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 41751518-bd08-34dd-82f7-f1e0f068a411 | -14.4588 | -47.3174 | 2025-09-13 00:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| d3a1df17-307c-3583-9460-8fbc4a4cdde4 | -11.1519 | -51.4018 | 2025-09-13 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2c9a252b-7cd6-3eee-9a98-4e4b6403a4bc | -12.9294 | -54.7333 | 2025-09-13 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0524ed0a-a1cc-33ff-8a69-f0e5f347a9a9 | -14.9772 | -49.5523 | 2025-09-13 00:40:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 23bf75f7-7180-3100-a0ea-568a388281e2 | -16.0252 | -47.952 | 2025-09-13 00:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 97.5 |
| b4baa57b-2950-334b-a71b-a69d5bc1ef33 | -11.7196 | -46.6031 | 2025-09-13 00:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 48d26a34-8b88-375c-a3b0-c49edc4ebc1f | -16.0997 | -49.9677 | 2025-09-13 00:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 9f880fd0-b56a-328b-b6cb-e20688b43b73 | -10.7664 | -50.5299 | 2025-09-13 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 267.5 |
| f9f0769a-4cf0-3e6e-8234-87a9c1414753 | -10.7474 | -50.5319 | 2025-09-13 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| c3c7b421-40c4-3f84-a2fb-5fe9f1d7f07b | -3.2306 | -47.1131 | 2025-09-13 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 1303c8e6-4582-3f5f-affb-47f45c06699d | -3.2282 | -47.6371 | 2025-09-13 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 27e6ac79-acbe-3570-aa99-2ba2e874b619 | -11.7424 | -44.2117 | 2025-09-13 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 785157e3-f6ce-30d6-9d20-0f39f7cc55cc | -22.2264 | -48.592 | 2025-09-13 00:40:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.8 |
| 66010d21-b61f-3541-b990-ca53c990c68c | -16.2546 | -50.0524 | 2025-09-13 00:40:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c604570d-0766-3ea3-8bbf-1eee6b076b21 | -16.5666 | -49.2247 | 2025-09-13 00:40:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 59d4772f-a3d8-30f9-9592-7d7dd7bb57b2 | -19.6435 | -45.8762 | 2025-09-13 00:40:00 | GOES-19 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 2d1f8d1b-f2aa-36d4-a8c1-5297c9757e4c | -16.08 | -49.9709 | 2025-09-13 00:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 965cf3c4-29a5-3c58-9e0b-c6470981b976 | -3.2283 | -47.6154 | 2025-09-13 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 753cb031-e24e-3173-9114-de4aa0917999 | -11.1522 | -51.3806 | 2025-09-13 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| ba5a15cc-b0db-37c4-80ab-6339c438ce66 | -22.79846 | -47.80879 | 2025-09-13 00:48:00 | TERRA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e55f28c1-3805-324e-a456-1bfcc84e60fb | -23.61321 | -51.38986 | 2025-09-13 00:48:00 | TERRA_M-M | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.7 |
| 1ba98f4e-ece6-381d-8e85-cf25e9774e5d | -21.11965 | -47.04623 | 2025-09-13 00:48:00 | TERRA_M-M | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2675a774-d365-336c-afbb-0abec194f856 | -25.16296 | -49.68908 | 2025-09-13 00:48:00 | TERRA_M-M | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| a5ba641e-aa5d-3dc0-8203-b184620ae486 | -21.17751 | -47.54105 | 2025-09-13 00:48:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9dba9a30-46ed-3a42-afce-c35f308703e0 | -21.65069 | -50.12428 | 2025-09-13 00:48:00 | TERRA_M-M | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 409e0f54-b232-3aa0-a194-3350563c0eb3 | -22.25082 | -48.58862 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a02916e0-64d5-3efe-ab58-503006f3d01d | -22.23882 | -48.5702 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| af77d561-9868-38bc-a93c-70a88c3f0b2b | -22.20993 | -49.9771 | 2025-09-13 00:48:00 | TERRA_M-M | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d5845210-8d28-3b97-9162-1560f804ce57 | -21.62554 | -46.80493 | 2025-09-13 00:48:00 | TERRA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 1621390f-3e02-3684-9445-261b0aaf2dda | -22.25331 | -49.56511 | 2025-09-13 00:48:00 | TERRA_M-M | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 378acd58-cc9b-3ce4-bedf-02397c1a1093 | -23.25702 | -47.06336 | 2025-09-13 00:48:00 | TERRA_M-M | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c25c44ad-3411-3fb7-a0bf-7fed848ec7f7 | -22.2403 | -48.58017 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.1 |
| 178b37e5-cd42-31e4-a3aa-7b63db9d66a8 | -20.59254 | -45.10524 | 2025-09-13 00:48:00 | TERRA_M-M | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| e666d776-e284-3c9b-bec8-c33621345610 | -22.23274 | -48.59161 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 22755fe2-2154-3f68-be14-00f4338256ea | -22.3278 | -49.76078 | 2025-09-13 00:48:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 61b5ae77-009b-3f35-b1f5-7fc09e35a4e6 | -21.17579 | -47.53004 | 2025-09-13 00:48:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3c1d4ab2-1f82-3e6f-8519-9a205386d31f | -23.4346 | -51.42942 | 2025-09-13 00:48:00 | TERRA_M-M | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 915c2f9a-c121-3e52-9e4a-15fc23b449f6 | -21.02538 | -48.41672 | 2025-09-13 00:48:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3eb85465-320d-37fa-bdad-625770994b83 | -21.61563 | -46.80657 | 2025-09-13 00:48:00 | TERRA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.4 |
| d2f4d239-4389-3435-a1b4-a91c98a33a2c | -22.26216 | -49.56361 | 2025-09-13 00:48:00 | TERRA_M-M | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 20fc2ab3-a759-3407-8138-5be48a1c0455 | -22.23571 | -48.61156 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| fb4f07be-a767-3c11-a5b0-a0a3466bebca | -21.61759 | -46.81883 | 2025-09-13 00:48:00 | TERRA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.8 |
| 9566cd37-47ae-3ac4-af74-6e235b327aed | -21.03039 | -47.12909 | 2025-09-13 00:48:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 20aee72d-08b1-33ea-8e75-4a70f8d5b180 | -22.22639 | -48.60877 | 2025-09-13 00:48:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |


[Clique aqui para ver as próximas entradas](README5.md)
