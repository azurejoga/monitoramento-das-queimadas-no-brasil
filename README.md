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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5d6acf1-6c30-3c3d-b902-606f8df037f5 | -3.2686 | -46.9142 | 2024-12-13 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 307d1991-e720-3cbc-a7c3-ce086da22f17 | -14.7655 | -52.6446 | 2024-12-13 00:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| eb3f9e8e-866c-39c5-a904-6d1520ae5420 | -2.4923 | -51.8233 | 2024-12-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 9a4f89d0-1bd9-3358-9535-ae30d9558fe2 | -2.8196 | -53.0832 | 2024-12-13 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| d250c474-11b6-3c38-b0ad-5d4c7ace0505 | -2.5108 | -51.8023 | 2024-12-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 118cf356-bfcb-3843-a851-d8cdf5d68ab1 | -3.2936 | -45.5817 | 2024-12-13 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| fe69fafd-de4a-339d-94e6-28821cc2c3c1 | -11.1962 | -53.8142 | 2024-12-13 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| ebdc8e7e-24b6-3e97-a4e5-eb549471e3b1 | -11.2148 | -53.833 | 2024-12-13 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| f2912a36-2d07-3fba-99ff-5ce1bdefb0e3 | -13.0836 | -52.0304 | 2024-12-13 00:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a155c790-88ae-3c2e-963b-3ce2118a0ff6 | -12.5497 | -57.7196 | 2024-12-13 00:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 40c0e754-d04b-3ff4-9fb2-22399f3f6c06 | -3.2685 | -46.9362 | 2024-12-13 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 52b45635-a098-3b42-b003-1aaef401a8ce | -11.2151 | -53.8125 | 2024-12-13 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 84b4f761-572e-3498-a24e-1923b194a401 | -2.5108 | -51.7817 | 2024-12-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| ada8bd3c-e1e3-3ab2-b5ae-ad321140ad95 | -5.2296 | -43.3054 | 2024-12-13 00:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5f8fc330-d08d-317b-9ebb-8625afa67615 | -1.62 | -46.6747 | 2024-12-13 00:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 431be901-6594-306c-852a-ce529d538f79 | -5.2108 | -43.3067 | 2024-12-13 00:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| e793d43e-9c2f-3cce-a94d-27ec8800cc49 | -5.211 | -43.2833 | 2024-12-13 00:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 248e1302-f3d9-3762-ae72-947fdef1b790 | -2.1173 | -54.6472 | 2024-12-13 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 56599e84-778a-3b3a-b4a1-b1ebf1defc90 | -10.1373 | -36.5459 | 2024-12-13 00:00:00 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 8128b1da-b9a2-302a-95ee-c74799d92b59 | -2.8196 | -53.0629 | 2024-12-13 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| cf3265f9-3597-33e6-9032-b7c243f5ecb7 | -5.2298 | -43.282 | 2024-12-13 00:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| bfe6b3de-77cc-3215-987c-4baa9312830c | -2.7464 | -52.963 | 2024-12-13 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1f5e545e-6dc2-3988-ab2b-9e4ac0bf8a05 | -14.7848 | -52.642 | 2024-12-13 00:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| e1175633-67f2-3f2f-bd32-00ae9642dd14 | -13.6933 | -54.7555 | 2024-12-13 00:00:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d1b14179-8989-3bfe-bf2c-999543ea40a7 | -3.1449 | -45.5875 | 2024-12-13 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 58a9c3fb-4a29-321e-90cc-452a84bee99b | -2.0989 | -54.6674 | 2024-12-13 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| c541024e-6573-3071-adf3-72f192ffcce7 | -2.4923 | -51.8027 | 2024-12-13 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 240.8 |
| 62aea538-38b9-3921-8beb-9a64cd53ff27 | -2.1173 | -54.6671 | 2024-12-13 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 4d04cabc-4e99-3d58-95b7-aea764cc8fba | -3.2935 | -45.6041 | 2024-12-13 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 6a14d531-99e7-3c49-8f73-29cd38bb5a69 | -13.0644 | -52.0326 | 2024-12-13 00:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 166.4 |
| d9ca2525-d8e4-3816-a951-0a03e4ac7e81 | -11.1959 | -53.8348 | 2024-12-13 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 0bece370-ff7d-3d3d-bc83-7b83f553f96e | -3.15 | -53.2776 | 2024-12-13 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 19d7ab62-dbfd-326a-ad1d-8e2a45d30b22 | -6.9346 | -43.5168 | 2024-12-13 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 4b78e5fc-cca0-3dac-9397-72ddd2c2187d | -2.099 | -54.6475 | 2024-12-13 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| d4768829-90ae-3ef6-871f-d81ff890598e | -13.0641 | -52.0538 | 2024-12-13 00:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 56c77ced-743d-32b3-a9bf-510645800c23 | -6.9349 | -43.4934 | 2024-12-13 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 6793f67c-f62e-37bf-87c4-d9180bff1409 | -5.22 | -43.3 | 2024-12-13 00:00:00 | MSG-03 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7263f356-7812-3719-9b7a-334de0e15521 | -2.5108 | -51.8023 | 2024-12-13 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 71756985-ee01-3b94-8cc0-0a0e2bc73b1a | -6.9346 | -43.5168 | 2024-12-13 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 178.2 |
| fdae2321-b47b-3869-8601-71520a7d35b3 | -2.7464 | -52.963 | 2024-12-13 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 4cce5dd5-80e5-3909-93a8-73ac88491ccc | -13.6933 | -54.7555 | 2024-12-13 00:10:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 68f5c1fb-baba-3aff-8bde-5a00e8cdb7e8 | -14.7655 | -52.6446 | 2024-12-13 00:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 559e82b9-9302-3766-81b9-76ae576c6b82 | -13.0453 | -52.0349 | 2024-12-13 00:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 87f4e09e-be85-3e91-a724-7553f188e506 | -5.2298 | -43.282 | 2024-12-13 00:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 28ff1de9-cae2-31a5-af28-b308c3b449b2 | -14.7848 | -52.642 | 2024-12-13 00:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 998b0791-bcbc-3778-963d-c049f0e293c7 | -13.0644 | -52.0326 | 2024-12-13 00:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 7acaaf01-836b-32fd-8877-36e5df379ef4 | -2.1173 | -54.6472 | 2024-12-13 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9d7b2db4-2040-3f2d-961d-f6d1a74a08fd | -5.2108 | -43.3067 | 2024-12-13 00:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3a78f867-4e2c-3199-8c28-7630f773bf80 | -2.1173 | -54.6671 | 2024-12-13 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| efd490dc-f15b-3db0-841c-9ea1cf420133 | -5.211 | -43.2833 | 2024-12-13 00:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| fe8dccf5-61f4-3a8c-afef-41c89af54335 | -6.9158 | -43.5185 | 2024-12-13 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| a3597871-c4be-3522-a850-b492fe8b2858 | -13.0836 | -52.0304 | 2024-12-13 00:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d5634353-3fdf-3258-ba57-2e7154246943 | -1.62 | -46.6747 | 2024-12-13 00:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 943c8e5a-f235-36f9-8927-4777d0695754 | -3.1414 | -46.3452 | 2024-12-13 00:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 637ddc96-5c67-3638-a05f-375b518c483e | -3.3301 | -45.7146 | 2024-12-13 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ba30007f-cf55-3c06-a4f7-bbabb06185d9 | -2.099 | -54.6475 | 2024-12-13 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 897b857e-6123-3fa4-8e85-f6d4d5735bf2 | -2.5108 | -51.7817 | 2024-12-13 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 80f72fca-6b56-318d-8d6b-a4272bc43859 | -11.1962 | -53.8142 | 2024-12-13 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| fc701754-c0e1-362e-a116-9cfce5c10b4d | -6.9161 | -43.4952 | 2024-12-13 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b15783e8-d430-3128-ab65-1d90351c0556 | -7.2288 | -35.0765 | 2024-12-13 00:10:00 | GOES-16 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 60.3 |
| 815e2064-a9e1-395c-b2db-c63dbd2b45d0 | -13.0641 | -52.0538 | 2024-12-13 00:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| a35b5d66-08bd-3d39-971c-6423a2a155d1 | -3.2935 | -45.6041 | 2024-12-13 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a069b29b-d15c-3f93-b6b0-00631fa4ee7c | -11.2148 | -53.833 | 2024-12-13 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| b01bc3bd-c7c2-3802-8caa-f1a3d686f757 | -13.0648 | -52.0115 | 2024-12-13 00:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f6ceaa5f-8850-357e-affc-871e7240eef1 | -2.4923 | -51.8233 | 2024-12-13 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| d4ecddbd-4868-3aa2-b6f7-1d3e6c8e23e3 | -6.9349 | -43.4934 | 2024-12-13 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f0f0969a-d67b-3acc-84e7-741df3af2061 | -11.2151 | -53.8125 | 2024-12-13 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| cef1ba90-6523-3cdc-aa9c-c1e2f62cdd4d | -2.8196 | -53.0629 | 2024-12-13 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 00866d46-81e9-3fac-b5e4-d3f0b010cfa3 | -11.1959 | -53.8348 | 2024-12-13 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 0be415de-5a64-34e1-996c-6413f3f079f9 | -3.2685 | -46.9362 | 2024-12-13 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 42eaa58c-9d18-3a49-a12a-b30cd9d80629 | -3.15 | -53.2776 | 2024-12-13 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| aeadc22f-7387-3ad3-aa2b-10630b5f0913 | -7.2097 | -35.079 | 2024-12-13 00:10:00 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| 6f08eeb1-8bc4-3099-924c-c3b9433d43fa | -12.5497 | -57.7196 | 2024-12-13 00:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f373e916-ddd0-38f5-86b9-20fbb9bb09d7 | -2.8196 | -53.0832 | 2024-12-13 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9126f3dd-36f3-3492-b5b0-2999de648596 | -3.1449 | -45.5875 | 2024-12-13 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 5c9b94d1-bdd7-398b-a485-f1823214e116 | -3.2936 | -45.5817 | 2024-12-13 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 49242987-c222-3850-b191-216d9586fdc1 | -3.2686 | -46.9142 | 2024-12-13 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7b472dcb-b770-3af6-8b67-963bbff7f607 | -2.4923 | -51.8027 | 2024-12-13 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 221.3 |
| 5986fafb-446e-3d19-b9ab-cea44a25ab5c | -11.75274 | -41.13849 | 2024-12-13 00:17:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 09d9140c-6422-3ce9-8f78-7ffbefdbe15c | -11.75411 | -41.14874 | 2024-12-13 00:17:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 41c36e35-cd90-3a0d-8b35-acf95ac57f3b | -12.3591 | -44.71682 | 2024-12-13 00:17:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 1277b504-bb50-35e5-94e9-3b6d145b4d5e | -2.4924 | -51.7821 | 2024-12-13 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 410156da-e7e3-3b16-a1f7-96afeb438709 | -13.0836 | -52.0304 | 2024-12-13 00:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 08453216-51d7-3611-8152-4992f6fd3917 | -14.7848 | -52.642 | 2024-12-13 00:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 93dab67b-4214-3af1-9c3e-68fd798dc1e7 | -2.7464 | -52.963 | 2024-12-13 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 79c59f93-d91d-3ab0-8774-672f0ab52edf | -2.1173 | -54.6671 | 2024-12-13 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e313daa9-3a09-3f73-8463-a62cb23c24ff | -1.6385 | -46.6743 | 2024-12-13 00:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 676b9bb8-533e-382e-8876-ccda393b23c4 | -4.7811 | -48.4999 | 2024-12-13 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 4346dd6f-f7c5-386f-b028-7529aa15afa6 | -6.9349 | -43.4934 | 2024-12-13 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| ec84e6ee-62f0-306f-8780-a1e017f02565 | -2.099 | -54.6475 | 2024-12-13 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f7ca1a35-f3c3-38dc-a318-b67c8c5f53f8 | -5.2108 | -43.3067 | 2024-12-13 00:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 5b9641c0-831b-3e8f-9802-e5d8e4fc14a5 | -3.15 | -53.2776 | 2024-12-13 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| fff9f2c9-4b60-3fd0-be2f-1e142b941e63 | -13.0644 | -52.0326 | 2024-12-13 00:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 7097b7f0-5ee0-3390-be57-35a5142e9afd | -3.2935 | -45.6041 | 2024-12-13 00:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 76cacc1e-c38b-356c-b657-1e313daef7ba | -2.4923 | -51.8233 | 2024-12-13 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 066d8a28-9750-3e5b-8525-ad16d19369c2 | -2.5108 | -51.8023 | 2024-12-13 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| dae760f6-fa82-3ce4-bfe7-db3752ce85db | -5.1923 | -43.2846 | 2024-12-13 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5f62da6f-87ea-3941-ad3f-3154a042d339 | -5.211 | -43.2833 | 2024-12-13 00:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 6c8c2db8-88e0-3e4e-a4e1-167ee1fcf120 | -1.62 | -46.6526 | 2024-12-13 00:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 3c9605fe-21c3-3e55-ab59-d02b39b93ef5 | -2.5108 | -51.7817 | 2024-12-13 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |


[Clique aqui para ver as próximas entradas](README2.md)
