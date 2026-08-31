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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7533363f-abc0-30d4-aba4-ac1c0bce702e | 2.04766 | -50.96792 | 2026-08-31 16:35:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53cb8863-9e55-35d2-ab38-cfe3d3f25f63 | 2.53994 | -50.94354 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6ddcc21-d0be-361a-90f2-c52b2003482a | 2.0439 | -50.96293 | 2026-08-31 16:35:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 91e4acd1-06a2-3728-b273-b98ed0cade80 | 1.56111 | -56.06303 | 2026-08-31 16:35:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| ef59e6b2-c1e0-37bf-a614-5ae5709556b8 | 2.04834 | -50.96361 | 2026-08-31 16:35:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 88acfbd5-f575-3587-a024-48099d112124 | -0.84581 | -48.68629 | 2026-08-31 16:35:00 | NPP-375 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb0433bb-6c04-385f-a55e-d867433846f7 | 2.04458 | -50.9586 | 2026-08-31 16:35:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0008f813-ab96-3a61-8742-39a4a09d2b0e | -0.82841 | -48.09056 | 2026-08-31 16:35:00 | NPP-375 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c02a6ad2-bd5e-3de2-9d39-5f9f084d5aca | 2.24365 | -50.7485 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d792d93-8860-35b7-bcab-bc819aa2092a | -0.80373 | -49.20173 | 2026-08-31 16:35:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1ca26a57-4168-347e-a068-a0a993302a7d | 1.5572 | -56.06438 | 2026-08-31 16:35:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| c65bb9fc-7e09-3499-8767-be96dff13cfb | -3.9707 | -60.0258 | 2026-08-31 16:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 8ae5578d-08e8-39d6-9508-9135bc788ca5 | -11.1726 | -51.2728 | 2026-08-31 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e5c9fda0-4b64-3f5b-a410-feb4112c2511 | -3.1997 | -61.1799 | 2026-08-31 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| b078f071-80e0-3c6f-9789-014584f183ab | -10.1528 | -45.7665 | 2026-08-31 16:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e7fefc14-1d3c-3dc5-aa0c-563e2692d3c9 | -10.8025 | -50.6539 | 2026-08-31 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| e6ef9218-ede6-3895-88c5-eec0b7d955c3 | -11.1723 | -51.294 | 2026-08-31 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| a0433719-367a-36f8-aa8f-1c8613963400 | -6.6541 | -59.4452 | 2026-08-31 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b8b81641-1cad-3ebb-b2f0-3fbe58aa7631 | -3.4002 | -61.3276 | 2026-08-31 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 897ddeea-e0e6-3ed2-a672-95e2e643c602 | -3.1267 | -61.1811 | 2026-08-31 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4854877b-8bd5-358b-a2c3-fb3a82f4c5e4 | -11.6786 | -54.5484 | 2026-08-31 16:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 0c0bdc3c-6220-3d88-95c1-d11d99e0aa32 | -10.1084 | -50.299 | 2026-08-31 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 8af05864-c474-33b2-b449-115c42283c38 | -9.6676 | -47.9429 | 2026-08-31 16:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 6a79635e-87ab-38fd-86f9-155ebf0c6382 | -10.7081 | -50.6425 | 2026-08-31 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| c4f70cc9-7e3a-37e4-9714-84932a71f04b | -10.8212 | -50.6732 | 2026-08-31 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 22247cf9-ba23-3d5b-afc4-7de4ca4f472e | -8.5739 | -66.9754 | 2026-08-31 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| e0dca91b-e761-32f2-bdb7-a609df861385 | -6.1295 | -57.6637 | 2026-08-31 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2a22a434-20e0-356e-a5bf-c6083eb8ff03 | -10.8614 | -50.4985 | 2026-08-31 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 50c39870-1d87-3772-b3a4-6e8ae201c127 | -11.0563 | -51.4751 | 2026-08-31 16:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 8a7b90bd-ca23-3c54-bcf8-7b19104b6b00 | -9.6939 | -65.1145 | 2026-08-31 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 738eba9e-d859-3d70-a1eb-074fb70b5504 | -10.844 | -45.3356 | 2026-08-31 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 245.1 |
| 87c8c73f-782c-39dc-9cce-e7ac609495ef | -7.5659 | -61.362 | 2026-08-31 16:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 135.0 |
| a3d05b67-0ba8-3d8e-944c-4c46bfef005f | -10.1087 | -50.2776 | 2026-08-31 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ff3ed0fe-0367-3c6c-b6e7-48fd10e4c913 | -13.4767 | -51.4086 | 2026-08-31 16:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 19967602-da2d-3322-9806-ef52a45eee62 | -14.2989 | -51.7072 | 2026-08-31 16:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 27fc8e6c-d7af-3ce6-ab5e-ea2c2791bf6a | -8.631 | -66.5473 | 2026-08-31 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 792bbd46-e1f5-3106-bb14-a85664eecda1 | -9.1711 | -49.9835 | 2026-08-31 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1ef1d12a-b527-3888-81c3-65bdfefba120 | -10.7833 | -50.6772 | 2026-08-31 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 665837f3-d6d9-3b3d-9d3b-44eb5230196a | -6.9872 | -59.2582 | 2026-08-31 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| cdbdf9bf-5c53-3ade-a1d4-ccd0e45e5247 | -8.87 | -66.8935 | 2026-08-31 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9b776922-ea82-3bba-87cc-8344a1c61928 | -9.4342 | -45.6704 | 2026-08-31 16:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.4 |
| ffa57c8e-61a7-3559-8c98-40feb854eb30 | -10.5598 | -50.4236 | 2026-08-31 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| aa1476f6-3c3c-3efc-9088-0aceb32890a4 | -12.209 | -50.5601 | 2026-08-31 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| a04edd37-ed8e-3870-8522-45cfe3f6d9e9 | -5.9636 | -57.6704 | 2026-08-31 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 895db585-235e-3aa3-97c4-44c80aae9d5b | -8.5555 | -66.9574 | 2026-08-31 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 4277bca1-65a2-30c4-acde-3d96c2d9f3a1 | -11.8208 | -51.0535 | 2026-08-31 16:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 4196ff52-3cb7-3e86-af24-1a42a18e55f9 | -10.7856 | -50.5066 | 2026-08-31 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| bc0827c9-7537-3172-9598-175638fddb10 | -8.7579 | -45.3823 | 2026-08-31 16:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| d7bf80ee-eb0f-3635-ab39-b1d1f26a8c74 | -19.11136 | -39.75698 | 2026-08-31 16:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 6be58770-0151-361a-867f-a62b6561000a | -20.65136 | -47.24458 | 2026-08-31 16:45:00 | NOAA-20 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 80cd0489-1c68-3622-962c-6532bc5ef5af | -19.84437 | -47.92661 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1e2869bd-c653-31ce-b98c-02874a5f0eba | -19.83698 | -47.92374 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 95a04857-aa3d-3179-87f4-ab6b9341943a | -20.19711 | -44.45304 | 2026-08-31 16:45:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 5a8c1ded-ffb1-34cc-b3e5-43dfd3730a51 | -20.90889 | -42.13715 | 2026-08-31 16:45:00 | NOAA-20 | TOMBOS | MINAS GERAIS | Brasil | 3169208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0f33d50c-54ce-3c44-8560-6feaf0a73508 | -19.8404 | -47.92322 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 71e2f784-9bd7-3517-b226-6311e2a467a0 | -19.81317 | -48.07563 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9d5b080a-ad86-3035-b864-42f1e4ba8349 | -19.69032 | -43.28136 | 2026-08-31 16:45:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 88887fa8-808e-37fb-abde-98f2459f7661 | -22.49231 | -52.83002 | 2026-08-31 16:45:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 509cc72b-a8ad-34ed-8313-6077a38fd07a | -19.85121 | -47.92555 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 2422d52c-b196-3304-b53b-338eaedab77d | -19.83066 | -47.9281 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7536cf16-2844-3e94-8c02-6615e4cd774e | -19.8341 | -47.92819 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 3511b8d5-c065-3658-a277-2129f6859e89 | -19.8318 | -47.93599 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8d21214c-7906-39a8-ac36-af2b1dc2d77d | -18.52612 | -40.26323 | 2026-08-31 16:45:00 | NOAA-20 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 551798ed-3dd0-321a-89a5-7e23270226f7 | -19.80974 | -48.07619 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 83464204-4863-347f-8e97-7525baf6a006 | -22.49319 | -52.827 | 2026-08-31 16:45:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| bc980d36-f5bd-374c-b5eb-287261c525af | -19.91268 | -47.96418 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| eb73bac4-2c67-3a5b-b1bb-bc01ea729bae | -20.88519 | -44.63197 | 2026-08-31 16:45:00 | NOAA-20 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b69a5c8b-c0a3-3eb5-b5cf-20ce6f3ca754 | -21.72555 | -46.92046 | 2026-08-31 16:45:00 | NOAA-20 | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea47f975-a4d0-33b6-b1f5-3ab9d374b0d4 | -21.23106 | -44.12271 | 2026-08-31 16:45:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 344a4bd4-7963-3990-9394-ac5ede48cf88 | -19.84669 | -47.91827 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a1654029-9381-35f5-8557-dd8822e44c82 | -18.7717 | -40.20118 | 2026-08-31 16:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 61f06e99-e30e-34b9-8578-a3ac377e7f07 | -19.37281 | -43.4413 | 2026-08-31 16:45:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0d8e8b2-9788-355a-a39a-d7859f9f5cbf | -20.37841 | -46.51326 | 2026-08-31 16:45:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed6f1b15-bd29-31f3-9931-417c8771d971 | -20.95197 | -42.6085 | 2026-08-31 16:45:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 46220faa-0d34-383d-b61b-06a522e661a3 | -24.20354 | -53.57626 | 2026-08-31 16:45:00 | NOAA-20 | BRASILÂNDIA DO SUL | PARANÁ | Brasil | 4103370 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 25eb74e9-7ec6-3d77-9b86-dd4c11132356 | -20.5493 | -47.43306 | 2026-08-31 16:45:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 12088c06-f0ce-34f3-89a1-3f3b382b1b71 | -19.37002 | -43.4461 | 2026-08-31 16:45:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fa4a9e9a-7810-3168-8cb2-9b4445d93e49 | -19.80574 | -48.07277 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0f94918e-e7dd-3e33-9220-85aa9c01ace0 | -19.85176 | -47.92945 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 46.4 |
| cadecfb6-6fcf-35da-84d5-46d98720231b | -20.31303 | -47.83357 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| d68bb06c-0d86-3494-84e7-e6344c90f828 | -21.56752 | -49.21481 | 2026-08-31 16:45:00 | NOAA-20 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| c98d2513-0b38-32ae-845c-231e635ca8b9 | -19.83236 | -47.93991 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b5dc0ba3-560e-319c-99ea-738ce98f7851 | -20.13564 | -44.89738 | 2026-08-31 16:45:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ce4340f1-8255-3784-a008-b83d23603bf7 | -20.29934 | -47.83575 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5e2edec4-2de4-360a-87c9-0446e60b9c1b | -19.83686 | -47.94786 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 3e86ba93-f859-3fac-a3d6-eb1967ded717 | -20.33074 | -46.582 | 2026-08-31 16:45:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b563c6fb-321a-3645-8b60-3e254e7ca00e | -19.6659 | -40.22346 | 2026-08-31 16:45:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 10fb90f7-11a9-3a18-9f1e-191c6fa510fc | -20.02009 | -44.20895 | 2026-08-31 16:45:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| eb3e3ba4-fb69-315b-a046-d112922ae2b7 | -19.84724 | -47.92218 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 639654bb-f558-33ca-b479-21265a4bb2f5 | -21.15449 | -44.17183 | 2026-08-31 16:45:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8560b5e4-4887-3aba-b452-39674b8f2a9e | -20.3022 | -47.83128 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9c8469d5-d175-306f-8842-b15a905dbd8e | -20.53173 | -47.45571 | 2026-08-31 16:45:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c623f487-5071-3e4a-8efe-64c56d53ebfe | -20.01947 | -44.2051 | 2026-08-31 16:45:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| a1538c92-0acf-3cf5-9909-f2cca984d737 | -19.8295 | -47.94435 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b2a6dbb8-a2c3-310a-91dd-c49f842fd7d4 | -19.76985 | -47.89383 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aee3c599-e529-39f3-aea2-acafc75db286 | -19.11056 | -39.75267 | 2026-08-31 16:45:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| d10f8e0e-3503-35b8-b837-e19fb625d2e6 | -20.2125 | -42.04794 | 2026-08-31 16:45:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b1e41ebc-d886-3581-a117-253ece511458 | -19.84492 | -47.93052 | 2026-08-31 16:45:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 25f43294-f386-33c0-b614-5a964622fa8c | -20.31016 | -47.83805 | 2026-08-31 16:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 98.1 |
| aa9a0d69-36d8-344a-8e99-a36a0c71a01e | -19.98343 | -43.96347 | 2026-08-31 16:45:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |


[Clique aqui para ver as próximas entradas](README136.md)
