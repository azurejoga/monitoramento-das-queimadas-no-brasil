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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73302cc5-c000-365c-8479-3251b8981958 | -6.9712 | -43.6066 | 2025-08-19 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5d1cac00-9880-30ad-a049-0c7551488946 | -6.9339 | -43.5868 | 2025-08-19 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 6dcf6b50-3295-3f79-b044-246262d72b40 | -6.9527 | -43.585 | 2025-08-19 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 3e89f0fc-f349-38ac-ac50-35885cc96f03 | -6.9715 | -43.5833 | 2025-08-19 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 49cfc7b0-e646-3617-81c7-85ff9e0fb827 | -6.9524 | -43.6083 | 2025-08-19 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 0942182f-ea43-3645-badc-cc63341911c0 | -6.9712 | -43.6066 | 2025-08-19 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 61993feb-37a5-3e70-ac9f-c6163e49bb2b | -6.9527 | -43.585 | 2025-08-19 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e5255597-e956-3e2e-8e6c-912a1aed772c | -13.1555 | -54.9357 | 2025-08-19 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| e590a9aa-ab9a-38a5-bc9a-586453678cd4 | -6.9336 | -43.6101 | 2025-08-19 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d6e88c51-571c-3284-b1ec-85960aa552eb | -6.9339 | -43.5868 | 2025-08-19 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 89e4befb-3028-3e3e-97ef-1df3b5995ad8 | -6.9527 | -43.585 | 2025-08-19 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 1f33b77c-ff05-3f9d-9dea-c5893efc0b99 | -6.9524 | -43.6083 | 2025-08-19 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c5aac921-79d0-347b-9119-ba786ba7d6ca | -6.9715 | -43.5833 | 2025-08-19 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 70844c0a-a2e3-3771-af8f-8fbd04e909b7 | -6.9339 | -43.5868 | 2025-08-19 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| cee14df0-8920-39bc-82cb-11c662adefd6 | -6.75031 | -41.5413 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3cdf6706-dcb4-3227-bf9a-7cc5a41c23cb | -6.95451 | -43.60875 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f41d2932-4bc2-3251-a2be-543fce6925e8 | -6.93966 | -43.58558 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d85930d6-035c-3dc8-afec-8887e06c09e2 | -6.9356 | -43.59504 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f55da9df-f700-3d37-b478-d371b9380ad7 | -2.58517 | -51.92436 | 2025-08-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb293019-2a20-3b8e-a298-9499be099804 | -4.1474 | -46.45176 | 2025-08-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf81c3ba-c1c7-3273-bcc5-da5fb09cd44c | -6.51808 | -45.49056 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 325ef874-434e-304d-bd25-45b1ba206a50 | -7.59314 | -44.39938 | 2025-08-19 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86778c09-4412-3c24-8813-cbfe6228edd5 | -5.23429 | -44.60371 | 2025-08-19 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b701bc0-409b-3730-9b3f-47c7fcdf6aa6 | -6.08964 | -44.40202 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d809738a-283c-303d-94c5-313d2af4a080 | -6.96111 | -43.58888 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c50c5795-d026-3292-9505-86ba46233630 | -6.94858 | -43.59949 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb4cfbfe-ef24-39f6-8d7a-6ff17e11020a | -7.58365 | -45.43375 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8471cd0-d5cb-3544-b3e6-fdf6b9136af5 | -6.04859 | -44.89785 | 2025-08-19 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 60934e3f-e45e-3761-9569-99fe76282d6b | -6.94621 | -43.59079 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be2d99f3-44e5-39b1-b3a3-526bd0e0bd81 | -5.05701 | -43.85947 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b51c7d92-f718-35da-8cbd-a8990fa7d6ae | -6.08929 | -44.58768 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fe8a44b-ce30-31d1-b163-d9cd26d42c49 | -2.54558 | -47.72186 | 2025-08-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d940ef81-1daf-3071-ac6c-836df4bb854f | -4.2604 | -40.28538 | 2025-08-19 04:25:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3eba9278-fc2b-30ff-beb7-a47e85a887b1 | -7.19791 | -43.96497 | 2025-08-19 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a80eb053-51ab-3350-a96b-bb62f3c1790d | -5.98598 | -44.13624 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e97deb99-8b49-3316-9593-ab0d7c26f6ac | -6.9593 | -43.60112 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce275898-d9b2-318e-90c4-435c1b46639d | -7.16772 | -43.42416 | 2025-08-19 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfc9374f-5405-35f9-a1a2-23a51ced3cf7 | -5.87743 | -48.12032 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dd0a2e52-a68d-3879-85c8-4808623d7e2d | -6.67668 | -43.67792 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac68c0de-f13d-3039-be38-f413c06a97b9 | -4.47863 | -47.50533 | 2025-08-19 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdbeec33-d05e-3a7a-819d-4db9953a5576 | -5.92229 | -46.00037 | 2025-08-19 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07aaa086-88b0-345c-bb90-bbc08bbd39a6 | -7.67126 | -45.96824 | 2025-08-19 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44657a44-b834-3ff5-bc76-f6cf6c8b733f | -5.97349 | -44.13128 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c46b655-4023-3dc0-9ce3-23f3be2dda00 | -6.40006 | -47.33271 | 2025-08-19 04:25:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04c5743b-b997-36e6-bd40-ce226e733a81 | -5.97651 | -44.29294 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6eb82e2d-4d71-3151-a92d-fd3096ec52a6 | -6.54297 | -49.5164 | 2025-08-19 04:25:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3e2a1de-8859-3c04-8e61-28b42144beb2 | -6.93666 | -43.60601 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9a8a0bd-93df-3288-a87d-78ee0208c40d | -6.51638 | -43.42342 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0b3ed91c-b53d-3b72-a880-64c7780638a4 | -5.6478 | -43.3973 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59279aa8-7dee-34cd-9056-c7c711409c08 | -6.95275 | -43.59596 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ded94ec-e1a9-357e-a829-8b7bd2ec9769 | -5.97465 | -44.12376 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41e417ae-c280-3b9c-8281-0a95f715624b | -7.02095 | -44.27249 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96a597ac-c100-392a-a404-5b3c6c8a24ab | -3.28341 | -48.81249 | 2025-08-19 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 27c9f3e9-0eec-3f5d-bfe2-c1f7b1234fd6 | -6.54656 | -49.51696 | 2025-08-19 04:25:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1c2917c1-4534-356f-a2b2-b9ecc273ea88 | -3.08749 | -48.85064 | 2025-08-19 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeb5532c-9c7f-3a13-a34e-41db163f6e9d | -4.91462 | -43.24329 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f3c79d6-f094-34f9-9d37-59bc1817255d | -4.02493 | -48.06773 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e522393-9fd8-3741-8adc-15eef619fddd | -4.01458 | -48.06617 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f1b0174-941e-3873-b964-c4574e4eaab7 | -5.78593 | -43.60784 | 2025-08-19 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3da73e49-b3a9-39d2-a69a-29ae34c61d74 | -6.95391 | -43.61285 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b2c3af5-4c12-3d16-b06b-fbb6617b73db | -5.98326 | -44.13672 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ceb26d3d-56fb-3b45-b8dc-9ca77fb30ff6 | -7.59537 | -45.42456 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 378c97cc-6911-3827-88e8-59158e4b6da5 | -5.97694 | -44.13184 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a293eefa-616a-3030-b7e3-e1fb44013fde | -6.96704 | -43.59815 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 518488eb-7db5-3fee-b7bf-7c33eebc5df3 | -3.45037 | -48.96844 | 2025-08-19 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6be95662-9a66-35b0-9090-002c169184c0 | -6.16382 | -47.2771 | 2025-08-19 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 159c7192-ec16-3c7f-be6e-9477d530235f | -4.65012 | -43.12311 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70386889-26de-31c1-a53b-a81e3d5bbf71 | -5.55554 | -44.29543 | 2025-08-19 04:25:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a59424e6-aca9-395c-af2b-38f5ebfc3c50 | -6.03835 | -44.34824 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8bbb8d4-d334-3058-b4dc-175eb0c90266 | -6.24913 | -44.828 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0410f0e-e063-3f69-b730-622fb60b225b | -6.93486 | -43.61822 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3799289-5abb-3dc0-a992-9658801cfa36 | -7.44481 | -44.87365 | 2025-08-19 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f247f1cb-eb6b-3191-8dcb-041ef7e98a6a | -6.93794 | -43.6037 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9670ff6a-07b1-3802-a7f1-e08b09ba5b63 | -4.40888 | -44.38194 | 2025-08-19 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c9d1280-50f0-3ae2-b354-ad147f0bf6e2 | -6.93017 | -43.60672 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3273d6d6-c39a-3c6a-a835-12b08e12de56 | -6.52286 | -43.44451 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 948e2e8c-fc12-3901-b78f-4a751135174d | -5.93631 | -46.62823 | 2025-08-19 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0c6f364-173b-3a95-871d-a874ea405904 | -3.83006 | -47.74727 | 2025-08-19 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2246fa0-f7df-327f-bc57-679ff3135aea | -4.29927 | -48.06369 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08cf5c4e-d50b-3a4a-bb27-dc1cde6d8f9e | -5.42258 | -42.36123 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2cf601a0-51af-3be5-9245-08f036bb927a | -5.80426 | -46.60043 | 2025-08-19 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6f49d04-1efb-33fb-85f5-59d100368c8c | -5.7824 | -43.6073 | 2025-08-19 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5dca528b-1f52-3a29-b2c4-32e87fccbf6a | -6.94199 | -43.61935 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28fa7a39-680a-39e4-a51c-75f68add6f4c | -4.30986 | -48.10761 | 2025-08-19 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7b5e3c4-74c1-3e40-b209-349e45b1a490 | -7.16954 | -43.50941 | 2025-08-19 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 63d53a32-3181-33ca-9285-3397e30b467d | -6.93251 | -43.61535 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72925408-56bd-3f40-b34f-ab25639d4269 | -6.93436 | -43.60318 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53925ac8-402a-3892-849a-c7a11c9e25ab | -6.55106 | -43.9873 | 2025-08-19 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98c97273-5511-3476-ae37-0b0a974237ee | -6.95693 | -43.59243 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61e9d9e0-dbdf-3f85-95e2-1703f1039fb9 | -6.44908 | -45.45095 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0899453f-2590-3a9e-ae8f-616e00b9e529 | -6.86524 | -43.12305 | 2025-08-19 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1ca1264-5be9-30a9-b68a-6a2786d568bb | -2.90734 | -48.29989 | 2025-08-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed65bd59-a3c9-3d9b-b70f-1f17d59da528 | -6.94023 | -43.60655 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8708c9ac-21d5-3316-aac0-8f2c6ae646bc | -7.20495 | -43.96605 | 2025-08-19 04:25:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 701f068c-20db-3593-bad5-eab65d5c972f | -5.75102 | -46.68061 | 2025-08-19 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d3288fe-600c-3a82-afb8-bf89bada378c | -4.59281 | -43.31129 | 2025-08-19 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfd1765a-05f8-3b11-a86e-096407062ccc | -6.94203 | -43.59435 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02083021-c97b-3ebc-a635-996b7aef4263 | -3.31717 | -48.70791 | 2025-08-19 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fddfeb2-478d-3796-8785-4d4e32f7ce91 | -6.95808 | -43.60931 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4a0ba17-467a-3fd0-bc9e-d7830552c831 | -4.96104 | -43.04969 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README20.md)
