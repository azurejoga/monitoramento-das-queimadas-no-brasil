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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c85e483d-5244-34d7-90bc-b6286790a4df | -16.9673 | -53.63085 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dbe6e0d-67c2-38e2-a9c3-ba6d19af5124 | -18.18595 | -53.32624 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16b01699-c308-30b4-907d-e442ca5e47ec | -16.95388 | -53.70147 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0477895d-89f9-3f44-91d4-734da0bfd832 | -16.96227 | -53.68791 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 60616c71-59fd-3269-a8c7-886326c3e83f | -15.27544 | -56.80351 | 2025-09-28 05:48:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71d1e704-92f2-39ea-ba1e-b2ffb2ec6a8f | -15.9785 | -59.50029 | 2025-09-28 05:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d577873a-93de-3dcc-9af6-818437ef9cee | -16.96603 | -53.61881 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3ef6fb5e-697c-3bf4-8320-1b7ec1d4eec4 | -16.96538 | -53.62573 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9359e460-2e52-3eef-b03a-2a1dd8b274ac | -16.97459 | -53.60482 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aeb54af7-770d-347d-bd60-319c958096e7 | -16.95754 | -53.63229 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee8b59c9-d868-3809-9a86-dd90561044b5 | -15.81171 | -56.4252 | 2025-09-28 05:48:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98b5c357-875a-306f-ab5e-074f32632029 | -16.96741 | -53.60419 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 78fc9dcf-8a90-3ef6-8657-285d2053f6bc | -18.17773 | -53.32307 | 2025-09-28 05:48:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f47ea56f-3884-365c-9086-f4b387c380cc | -16.96915 | -53.60977 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42e91f64-ff0b-378d-9a47-361b9e7ca452 | -15.99315 | -59.50295 | 2025-09-28 05:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7773902e-b059-3f60-aa91-fd284a134e42 | -16.96134 | -53.66863 | 2025-09-28 05:48:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 374aa92e-c4f4-3e47-ac22-b2fc04868b6e | 2.87053 | -60.26325 | 2025-09-28 06:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aadbe5e2-7f6f-3e31-a6d7-553c59403eca | 2.87588 | -60.26236 | 2025-09-28 06:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0987276f-d8eb-3467-adaa-88108585581d | 2.87109 | -60.26659 | 2025-09-28 06:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8010c685-fcbb-3146-bd25-f4c0f0f2ae73 | -7.86096 | -63.3138 | 2025-09-28 06:05:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d6307bb-9b28-3941-9eb3-86e2502bb107 | -7.86347 | -63.31409 | 2025-09-28 06:05:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6388369c-76ce-3df1-98fb-f0456c6c79ea | -7.86306 | -63.31717 | 2025-09-28 06:05:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51a81dde-4396-388f-838b-d931d2d6c74c | -7.8661 | -63.31452 | 2025-09-28 06:05:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6559525-f165-3c6d-b1e6-b654a6969c87 | -7.86053 | -63.31686 | 2025-09-28 06:05:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7712dca4-9790-3caf-b883-ddea4fcfa238 | -9.91237 | -65.01347 | 2025-09-28 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6bb1815-31a0-34e9-9e0c-50977fd7f90f | -9.80012 | -61.49468 | 2025-09-28 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46ea9b1a-0033-3fa6-a22c-78045b649bff | -8.94597 | -65.92778 | 2025-09-28 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 660527de-22a7-36b8-a4b0-bf660e898042 | -9.56604 | -63.21093 | 2025-09-28 06:08:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e875fe0-6ce5-3723-830e-26daf915013b | -9.80607 | -61.49551 | 2025-09-28 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70a476d4-a48a-3305-9efb-01023cd09e71 | -9.64844 | -62.84074 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 26b2ad78-a332-3e6e-91e8-32d2694e3ea1 | -9.64457 | -62.84092 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bd01613a-9f0b-32a2-8ade-97e6abf5b51f | -9.6489 | -62.8373 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d9d4893a-ed89-3100-8abf-65e3da2ca271 | -9.65046 | -62.83809 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a5cd4769-102c-3958-b3b7-43bf5725c580 | -9.81201 | -61.49635 | 2025-09-28 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1761cc6a-08b5-33a1-9d95-5490cbb2079b | -9.56117 | -63.20699 | 2025-09-28 06:08:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d35831aa-b64a-3f1b-951e-0b3b2e51cf10 | -9.64751 | -62.84764 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1c5dbff6-2e4c-36ad-b87d-1620d3884f8d | -9.94745 | -66.86366 | 2025-09-28 06:08:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a22d55c-682a-3e60-b42c-ca178916f590 | -9.90766 | -65.01282 | 2025-09-28 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ea949b6-f83e-3983-84b0-412f4c068104 | -9.65003 | -62.84154 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 606ff884-d700-3d1f-bc1b-720e3ea9a30e | -9.80847 | -61.49685 | 2025-09-28 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc20d176-ecdf-3ca5-8f0e-723ec9ceeaaa | -9.56648 | -63.20761 | 2025-09-28 06:08:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0e6539f-5441-32bd-9861-eddb670b3cd2 | -10.41539 | -67.51395 | 2025-09-28 06:08:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2673d479-61c7-31f8-9981-e58b03e6e31f | -9.75701 | -65.03476 | 2025-09-28 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7ae8a7b-97f8-3224-9ce1-e5a746fb7b68 | -9.64414 | -62.84434 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 18.4 |
| b092b48b-9161-3261-b977-60bd457e352e | -10.39258 | -64.92049 | 2025-09-28 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a928b9f8-cc2d-360e-a385-5dad320a36cd | -8.9422 | -65.92292 | 2025-09-28 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d1e51a3-dfcd-33a4-aae1-2639c478815f | -9.56073 | -63.21028 | 2025-09-28 06:08:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fc9e850-773f-38ff-a3b1-1c52bf1663b4 | -10.39494 | -69.05093 | 2025-09-28 06:08:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acf4ba7e-b7ad-3c7c-9a16-351fe441dfc6 | -11.24656 | -61.17033 | 2025-09-28 06:08:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7e42ce4-2446-3c9b-b0be-d4bf512facc2 | -9.79658 | -61.49517 | 2025-09-28 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d12f769e-6d24-3321-907a-cd05765131ae | -10.81852 | -69.09196 | 2025-09-28 06:08:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf5870d2-d22d-3943-a1b7-e08b718c3ef9 | -11.25275 | -61.1711 | 2025-09-28 06:08:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 518d760b-aa48-30c1-9412-a27d5b6790a1 | -12.19258 | -63.66773 | 2025-09-28 06:08:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ba55a76-0d5e-3368-a930-ce70857735e6 | -10.51524 | -69.04532 | 2025-09-28 06:08:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ef6bf9d-8ef4-3686-a4bd-9eebd3f88cdb | -9.56161 | -63.20368 | 2025-09-28 06:08:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e19db56b-a93a-3024-a53e-4fc411480bec | -9.65343 | -62.84479 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8e4baaba-71d9-3d8d-b1bf-10821c144a9e | -12.01779 | -63.23228 | 2025-09-28 06:08:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 876a826e-4dec-3468-947a-e1d6f7a73856 | -9.64959 | -62.84497 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 12b9836d-ee48-3910-a33e-a8dab63e775e | -9.64798 | -62.84415 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 4c3f457e-5e29-3e0d-b532-a82dda3ac591 | -7.19581 | -71.50176 | 2025-09-28 06:08:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 224324de-fbcc-3bbe-9a8b-16bbf8a356fd | -9.73959 | -62.35881 | 2025-09-28 06:08:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2779f26f-5d9b-3e59-b1dc-63a560b13e51 | -9.65295 | -62.84833 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| fc542a98-a07d-33d2-a5ba-a5b6b747cbba | -10.28643 | -67.27684 | 2025-09-28 06:08:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5f5c63c-0427-39e9-9d84-9baa4517d5e7 | -10.42617 | -64.88812 | 2025-09-28 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f868fef6-5ee2-3d9e-b567-24a75dcf30d2 | -8.94161 | -65.92715 | 2025-09-28 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0aa86c18-48d9-3f00-ba26-483655f63718 | -9.80252 | -61.49601 | 2025-09-28 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ca7eea8-3064-358d-8050-b2e6db23f9d1 | -10.29049 | -67.27741 | 2025-09-28 06:08:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcd211f9-abdc-32a4-88ce-8bf5acdaa7cc | -9.64914 | -62.8485 | 2025-09-28 06:08:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 0b0c0535-536e-3bad-ab87-f453f7c901fa | -8.8083 | -72.75304 | 2025-09-28 06:08:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 679e69f0-4bd0-3d5d-b204-7a784809ad8d | -9.7452 | -62.35965 | 2025-09-28 06:08:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ecb0849-b40d-3eb2-9243-c901406f22aa | -9.57179 | -63.20825 | 2025-09-28 06:08:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c719a574-e9d9-3026-84c7-81956693d81b | -12.01734 | -63.23589 | 2025-09-28 06:08:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99e02f65-ae5f-376b-8c31-db3e718f2dc2 | -9.78048 | -64.98298 | 2025-09-28 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59159281-58cb-35e7-a61b-46eb2fd3318c | -9.76171 | -65.03535 | 2025-09-28 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ef347b2-96b9-3eee-b2ca-92b9a3b99b46 | -9.6511 | -62.8526 | 2025-09-28 06:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 12baea61-a54f-3c55-9f36-ec76b6b80257 | -16.9864 | -53.6947 | 2025-09-28 06:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 3d34f017-092c-38f5-b5ed-73dd2e6429f0 | -9.6512 | -62.8336 | 2025-09-28 06:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 94a53b6e-ea95-306b-8d6f-934b42fc9811 | -18.1977 | -53.3208 | 2025-09-28 06:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 123.6 |
| d61f2405-6e7a-3fa4-b1d4-94043f908948 | -16.9671 | -53.6763 | 2025-09-28 06:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 5446d9b7-e879-3477-b86c-62ca0c419917 | -9.6511 | -62.8526 | 2025-09-28 06:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| cd8c72a6-8528-373d-bab1-7b9d72dbba7f | -16.947 | -53.7003 | 2025-09-28 06:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7bc8cbf0-1f20-3f3f-ad91-c5f34ad50eb5 | -16.9474 | -53.6791 | 2025-09-28 06:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| f688a564-cdf9-3cfb-94e9-5baed4b9fbae | -16.9667 | -53.6975 | 2025-09-28 06:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 186.9 |
| f9115a6d-0d6d-36a6-b44a-1c5e9f6d52ab | -16.9868 | -53.6734 | 2025-09-28 06:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 16036011-7576-32e7-bc78-ad1a2bbeb484 | -16.9667 | -53.6975 | 2025-09-28 06:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 186.2 |
| fadbdfae-b5b6-383e-afdf-befea310d104 | -18.1977 | -53.3208 | 2025-09-28 06:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 91166136-f03e-3262-9c8c-f45eb82bdb88 | -18.2176 | -53.3177 | 2025-09-28 06:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 294f0c31-e2a0-3828-b7dd-784f3a393654 | -9.6511 | -62.8526 | 2025-09-28 06:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 09a4654b-a825-3043-b09f-8711c6f9ead8 | -9.6512 | -62.8336 | 2025-09-28 06:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a17a7188-c2da-3dc5-aebb-581f8af859d1 | -16.9671 | -53.6763 | 2025-09-28 06:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 127.7 |
| d7346658-062b-3a99-9bf7-47e9bdc20519 | -3.32204 | -52.53416 | 2025-09-28 06:35:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b825a0dc-75dc-3f94-8281-06cad457dd28 | -2.57587 | -48.40569 | 2025-09-28 06:35:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| b427a959-857a-34f1-a7c3-cae0a6e4fdb0 | -1.627 | -55.16441 | 2025-09-28 06:35:00 | AQUA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b651993c-4644-3b9e-ab4a-c9da3bf991af | -2.58198 | -48.41383 | 2025-09-28 06:35:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 226a67ad-fded-3944-ada4-67073ef46e5f | -2.58522 | -48.39089 | 2025-09-28 06:35:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| fe6a69b8-ea0e-33e1-9f6a-4c76e92fe88d | -7.79842 | -47.01572 | 2025-09-28 06:37:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ac335da2-291d-3784-93eb-d97ae5ac9cbe | -7.7424 | -47.00378 | 2025-09-28 06:37:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 2b0edc09-cd5c-31d3-8622-2b785b15195f | -9.91225 | -58.56369 | 2025-09-28 06:37:00 | AQUA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8ff48b90-c776-3512-9fc8-22536e74164e | -7.80887 | -47.01258 | 2025-09-28 06:37:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 3dead062-6946-3b80-b121-68058e821692 | -8.67939 | -49.92996 | 2025-09-28 06:37:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |


[Clique aqui para ver as próximas entradas](README93.md)
