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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa70a9e3-bb60-357b-b0c2-3edd5c73f61b | -3.60297 | -47.25311 | 2024-10-25 05:25:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8c6fdbee-05c5-3c69-9038-756eeb713335 | -3.60163 | -47.26204 | 2024-10-25 05:25:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 889b64e4-5a08-3ed2-900b-30c3ffd554c9 | -5.64685 | -47.90749 | 2024-10-25 05:25:00 | AQUA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fae5a482-156a-3e6d-8b1a-3eeae4bcbd11 | -5.84367 | -47.28244 | 2024-10-25 05:25:00 | AQUA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 15a067ac-078d-3fe5-ac07-a3667c472770 | -5.63237 | -46.96202 | 2024-10-25 05:25:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e361186e-d484-3df1-9bbe-304dbaf7bc9e | -5.63104 | -46.97084 | 2024-10-25 05:25:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 72e399c7-4d6f-3d37-b59d-ce43e6dc2009 | -5.27461 | -46.70444 | 2024-10-25 05:25:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0dab9d62-178a-3e19-8003-44416774a7b0 | -6.64161 | -47.85841 | 2024-10-25 05:25:00 | AQUA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6f6fca21-e281-3dd7-9a31-addc8d7f2317 | -6.64025 | -47.86738 | 2024-10-25 05:25:00 | AQUA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 28c4c6da-05ef-3b35-8c21-baa1417b4736 | -9.26637 | -47.90929 | 2024-10-25 05:25:00 | AQUA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b60083f9-b865-3886-9cc9-ff78c61eccef | -9.06882 | -47.99501 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3a70e6d9-4f1f-3755-8ce8-61511e9ca4fa | -8.95607 | -47.63771 | 2024-10-25 05:25:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 41bad17f-e51b-34f7-8ef2-7aca8fbe9535 | -8.90284 | -48.53627 | 2024-10-25 05:25:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 2fb55435-f4d0-3250-b33d-85a85aad5ac9 | -9.93212 | -48.87127 | 2024-10-25 05:25:00 | AQUA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a72f3c41-a0cb-3394-8138-0bc7234c1a8f | -10.64896 | -47.9184 | 2024-10-25 05:25:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 102a1956-9c0d-3bb2-897d-c1820b29dbca | -10.64762 | -47.92734 | 2024-10-25 05:25:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17a49ec2-3050-3188-bbdd-d1aace0d8cf7 | -10.47573 | -48.27932 | 2024-10-25 05:25:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a0fca9e-6a63-3cac-8de9-28f319a25071 | -10.44075 | -48.07574 | 2024-10-25 05:25:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7e424f39-85eb-3daf-8bd0-912783f20878 | -10.43941 | -48.08467 | 2024-10-25 05:25:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| be52611c-2c70-3482-893a-5842166e3257 | -10.94438 | -47.79789 | 2024-10-25 05:25:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2dbf39eb-48ec-38b7-b0c7-52af39910a30 | -10.93552 | -47.79658 | 2024-10-25 05:25:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3dadfa24-ce34-3b0f-8b6f-41b6ea1c74e8 | -2.00908 | -48.53144 | 2024-10-25 05:25:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1ceea149-ed83-3276-80a2-ae1a246d488d | -1.19724 | -47.60152 | 2024-10-25 05:25:00 | AQUA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| db1d3374-6856-37df-a2cc-90ea5eb344bd | -1.03886 | -47.61464 | 2024-10-25 05:25:00 | AQUA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 13521ecb-6761-3486-8c2f-e43e767fa00d | -3.45768 | -47.66822 | 2024-10-25 05:25:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6f94c3c6-73d9-37ed-83be-880817c53055 | -2.88679 | -48.27483 | 2024-10-25 05:25:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 600906a0-d413-34b2-8059-d5abd4479e74 | -2.88531 | -48.28467 | 2024-10-25 05:25:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 26fee08c-909b-3ff4-9dd1-2e0651489170 | -4.24308 | -48.33984 | 2024-10-25 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 32569ebd-97f3-33ef-a11d-2ed1ee81415b | -4.13062 | -48.40619 | 2024-10-25 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a5268cf0-b4cd-3f21-b13c-cd4dd9055c9b | -4.12913 | -48.41595 | 2024-10-25 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c5a69f05-7dbd-3db2-9710-886a40adf2ab | -4.09294 | -48.2365 | 2024-10-25 05:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c79d4102-84bd-312b-ab1b-20afaf9d86e1 | -4.06732 | -48.28161 | 2024-10-25 05:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5b073b2c-4957-35d7-a21a-7d0b4242e96a | -4.06587 | -48.29121 | 2024-10-25 05:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ff39157-6e38-3ff0-9b45-b9069fb13b46 | -4.06393 | -48.24193 | 2024-10-25 05:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3733c6bb-2f39-3dc9-840a-e81fe1d76a66 | -4.04753 | -48.10349 | 2024-10-25 05:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4128584f-8e90-3ce7-a3ac-84b167a214ce | -4.0461 | -48.11285 | 2024-10-25 05:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 79399f67-4729-364b-8c42-97a2ea305353 | -4.0384 | -48.10209 | 2024-10-25 05:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 279dd373-ddd3-392f-9a44-c6279dcb65b8 | -3.92858 | -48.33416 | 2024-10-25 05:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 685a6a14-f5be-36bf-9c77-fd52912a88a3 | -3.9056 | -48.36055 | 2024-10-25 05:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dc93b0fd-aa37-3e18-bf11-3cfe528f8731 | -3.9041 | -48.3703 | 2024-10-25 05:25:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 280a3ee3-8133-303a-8016-822e9f2f3f3c | -5.20371 | -48.21579 | 2024-10-25 05:25:00 | AQUA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d1ef6111-31a9-3288-884c-aba1bfb9d2fd | -8.98048 | -48.81764 | 2024-10-25 05:25:00 | AQUA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3ae1cb73-357b-3a65-935d-60474429d959 | -8.68154 | -50.03033 | 2024-10-25 05:25:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3a9b0683-add3-3ebd-bb30-cbdb1894e6ae | -8.54339 | -49.5469 | 2024-10-25 05:25:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ae5a6782-f238-349d-9411-1dcd4d042bd1 | -8.53405 | -49.54545 | 2024-10-25 05:25:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b3fbd401-1c7c-3b49-98b0-b3525ba9ca5e | -8.02359 | -49.63532 | 2024-10-25 05:25:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8af4cb10-c452-3a79-8262-8bf3ac3d8304 | -9.58287 | -49.64448 | 2024-10-25 05:25:00 | AQUA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8410b6c5-62c0-3ac1-971c-edc6e7abe948 | -3.40555 | -49.53086 | 2024-10-25 05:25:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e9600d32-c6b1-3743-b1bd-bc794f5f223b | -3.29855 | -50.16064 | 2024-10-25 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c8a6e127-7541-37aa-8fae-0575f7fa1999 | -3.25485 | -50.19899 | 2024-10-25 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ab49693f-60c6-3af1-84fd-4259811ab042 | -3.25085 | -50.19214 | 2024-10-25 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 26c961e9-94ea-331a-86e0-f2db6be20057 | -3.24885 | -50.20483 | 2024-10-25 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5838eb78-eee9-37ca-8ab1-24055d414f6c | -3.21679 | -50.16748 | 2024-10-25 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5f7dc73b-3022-360f-8ca2-895f9fe29ce7 | -3.15199 | -50.4478 | 2024-10-25 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a5dc280c-38b6-3aa9-82be-ba1f352d538b | -3.14995 | -50.46099 | 2024-10-25 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| e17c2589-639d-3f56-9276-45de3ec160c4 | -3.1413 | -50.44619 | 2024-10-25 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| dcd2b8b6-7734-33d5-9e40-9c604e2f79d6 | -2.96303 | -50.40695 | 2024-10-25 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e435e474-acbd-399e-9cb9-1d5a20392633 | -2.96097 | -50.42017 | 2024-10-25 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| bb4e4813-557d-30d6-b117-625a629bd8dc | -2.95891 | -50.43342 | 2024-10-25 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f794f9b8-baf5-38ce-906a-adee070b1de4 | -2.86478 | -49.44757 | 2024-10-25 05:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bdfaf8ea-3057-3f89-8e52-0bc93fa79265 | -2.80371 | -49.24749 | 2024-10-25 05:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 519968b8-0c89-3039-9aa3-a052e5bed40e | -2.79384 | -49.24601 | 2024-10-25 05:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0cd1711d-e136-3a1b-a7cb-238914354355 | -2.63988 | -49.24478 | 2024-10-25 05:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 219ea23e-1690-3329-ac58-cba8d6993490 | -2.62998 | -49.24333 | 2024-10-25 05:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| cfed8eb1-f345-3c7f-ac59-9f5f2ae6a883 | -2.62229 | -49.09538 | 2024-10-25 05:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| bbfc4126-9f1c-3452-8e3c-04955a6a8fb3 | -2.62068 | -49.77061 | 2024-10-25 05:25:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c5b8549e-e002-3863-93e7-400c1d9654e5 | -2.61883 | -49.78267 | 2024-10-25 05:25:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b4b521d9-ec7b-3d20-88ef-c98a992604f6 | -2.58054 | -49.23596 | 2024-10-25 05:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2b49a0c1-ff87-395b-b007-685d54cbbc86 | -2.57065 | -49.2345 | 2024-10-25 05:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 432e2a67-8ccc-33b4-b897-ca8c987629e6 | -2.56952 | -49.22878 | 2024-10-25 05:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 39f3fb1e-9b90-3340-994c-2b6c19d3ce5e | -2.1153 | -50.13737 | 2024-10-25 05:25:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d086ed84-69fc-3bcd-a251-e11e6f47ab2a | -4.58162 | -49.49218 | 2024-10-25 05:25:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4628badb-5e5a-3b2a-87e2-1ce5502e176b | -4.22985 | -50.63188 | 2024-10-25 05:25:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| edf3b900-2b53-37d8-aafa-2fee65a28b15 | -3.95046 | -49.98914 | 2024-10-25 05:25:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 76610e02-2de4-3f58-963d-353df0f3d592 | -3.87996 | -50.04665 | 2024-10-25 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 743a4330-e0e5-3d3b-a1ec-d485cb78b85f | -3.87812 | -50.05861 | 2024-10-25 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| edcf59e8-21b2-31ef-88ac-ea382f8d1263 | -3.74323 | -49.9397 | 2024-10-25 05:25:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f865ab33-93a8-3979-a2fb-8830473c804c | -5.11078 | -50.71645 | 2024-10-25 05:25:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8a078350-47e8-378d-9854-71b7ecb823b1 | -6.67873 | -49.97736 | 2024-10-25 05:25:00 | AQUA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 91bb93b0-48bb-3169-9c7f-4394c2348c3b | -2.83725 | -51.79418 | 2024-10-25 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ce992d76-0572-33b0-8a45-b8bff430691b | -2.8346 | -51.81107 | 2024-10-25 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| ca72c1a0-0ec9-3ba1-979c-e3c74ae57a46 | -2.83056 | -51.80364 | 2024-10-25 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 7ab8539a-70b2-33e9-ac35-d173b469d7fb | -3.08289 | -51.25436 | 2024-10-25 05:25:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 122adf37-57db-33b5-bdb0-a664fafc62f5 | -3.94466 | -52.2499 | 2024-10-25 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d8c52075-67b3-36cf-9376-4bf4c94d4aff | -4.67152 | -50.96304 | 2024-10-25 05:25:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 65c11510-ccaf-37a2-995a-5b54ffc6fa42 | -4.6694 | -50.97678 | 2024-10-25 05:25:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 560b0be0-cf58-3fef-9859-3f676f04f40c | -1.60538 | -53.29763 | 2024-10-25 05:25:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| c651624a-960a-33da-bee4-89eedb2df300 | -1.5986 | -53.29062 | 2024-10-25 05:25:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 7c700834-f446-3f01-bd5a-f409fed49fbb | -1.59489 | -53.31577 | 2024-10-25 05:25:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e366c720-10a4-341b-a44e-dd2241d30730 | -1.59164 | -53.29495 | 2024-10-25 05:25:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| b7701ec9-0b47-3f5a-844e-64706a40ac18 | -1.58779 | -53.31959 | 2024-10-25 05:25:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| bd97f08e-70c8-39c7-a5c7-6c779a4330c1 | -2.73609 | -53.19783 | 2024-10-25 05:25:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| d57a7432-05df-3e73-863d-add6dcea5f3d | -2.61958 | -52.43413 | 2024-10-25 05:25:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 07998e4a-625d-35c1-96d8-3a62f97fda5b | -2.61821 | -52.42851 | 2024-10-25 05:25:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| efe52da7-cd4a-36dc-a096-fda823c459b1 | -2.61654 | -52.45321 | 2024-10-25 05:25:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ee873b92-df7e-3092-a253-0f35e32fc40b | -2.6153 | -52.44769 | 2024-10-25 05:25:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 55cd0935-2444-307b-bbbe-901dde926d08 | -1.18339 | -53.65479 | 2024-10-25 05:25:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 01bd132e-5c42-3c8b-9d0f-9a7dbdefdd83 | -1.17962 | -53.67921 | 2024-10-25 05:25:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 68007338-47db-3a8b-ad5c-270b3553c2b6 | -1.1795 | -53.64947 | 2024-10-25 05:25:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 59780f81-87a5-3bac-9fa1-9c9d2fac0c6a | -1.17588 | -53.67401 | 2024-10-25 05:25:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |


[Clique aqui para ver as próximas entradas](README107.md)
