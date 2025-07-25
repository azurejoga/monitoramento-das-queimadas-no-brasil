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
| 1a4a7f48-d576-3f64-bb4d-ff58cf0a4b33 | -13.40371 | -46.8088 | 2025-07-25 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3805d93-527b-3701-986b-10fbf85e44bd | -12.65928 | -45.04117 | 2025-07-25 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59671fc9-6fb4-3152-8d4e-545186a8151a | -13.64646 | -45.71943 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13ec3e95-9d1e-31e8-a35b-2621ebae6d41 | -14.94698 | -46.97716 | 2025-07-25 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| beae5e9a-fe37-31d6-876c-86e5e51156e3 | -14.74606 | -46.30023 | 2025-07-25 04:23:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56b84833-d337-3911-a294-faef606bf10e | -12.2527 | -44.78142 | 2025-07-25 04:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a751787-9f8e-336a-977c-9961ad0f7686 | -13.71406 | -45.69348 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13e863d4-814e-33a3-b5d0-d2a8de7627d5 | -13.71294 | -45.67864 | 2025-07-25 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bf384ce-b860-35e5-bdae-a369ba45bdbc | -20.68026 | -46.3107 | 2025-07-25 04:25:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b3ac4ea-0210-3ee2-b4cf-3a89a2b03d76 | -18.22515 | -54.55176 | 2025-07-25 04:25:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca561f73-3056-3f00-b7b3-8de9986b0fcf | -19.16383 | -46.59148 | 2025-07-25 04:25:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d7f1132b-d9d0-31cf-8204-45b351ccda1f | -22.14355 | -47.40453 | 2025-07-25 04:25:00 | NPP-375D | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e16a3a8f-819c-3963-9aef-3eb595d4aabe | -19.28757 | -47.42369 | 2025-07-25 04:25:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e6985a6-9687-3abb-9f91-5bddb6c90f61 | -20.00377 | -45.39563 | 2025-07-25 04:25:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d2f88d6-bebc-3782-b75f-2e266083770d | -20.60619 | -46.31568 | 2025-07-25 04:25:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92c1a8ca-5d92-3dab-9eaf-b66eadf6d639 | -19.43026 | -44.81342 | 2025-07-25 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| bec67d10-f2d6-3f69-a1ce-5c3544c1382e | -19.16718 | -46.59203 | 2025-07-25 04:25:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28c71c6c-48de-3962-96d9-bc3944a2731e | -21.60731 | -57.57714 | 2025-07-25 04:25:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05f46d7a-61dd-34bb-bea1-5561c12a4ff8 | -19.28814 | -47.42004 | 2025-07-25 04:25:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7387a3a1-a99c-34f9-bebb-31f5069c9481 | -19.75366 | -54.00012 | 2025-07-25 04:25:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff5acb4d-1d12-3a08-b9f7-e311da0cae6b | -19.02048 | -54.66201 | 2025-07-25 04:25:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fb489d0-7f94-3f97-97a9-9bff3af0a60d | -20.00027 | -45.39507 | 2025-07-25 04:25:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d01d247-dd1b-3366-affd-2bc0b4f70adf | -19.19256 | -44.15555 | 2025-07-25 04:25:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55d5c3e9-46ea-3bcd-ad5d-d4e8d39efc37 | -20.68423 | -46.30744 | 2025-07-25 04:25:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26e621f7-6e61-3de2-becd-9d552f637244 | -18.4211 | -54.56325 | 2025-07-25 04:25:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbeb86ab-170b-3f62-b01d-58cd41cb7378 | -18.83815 | -41.96659 | 2025-07-25 04:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 56470e68-8f62-378b-b7a5-be82887a0a6a | -19.67938 | -43.8849 | 2025-07-25 04:25:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed26a257-dff3-316e-8115-14b06741861c | -20.53263 | -46.10851 | 2025-07-25 04:25:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11fcec07-869a-3c19-ae1b-47d2e597dd3d | -21.46998 | -44.96515 | 2025-07-25 04:25:00 | NPP-375D | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e01ccf62-f49e-39b3-b5ea-86a757e89a20 | -19.1889 | -44.15495 | 2025-07-25 04:25:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba189606-4f60-32e4-93c2-20ea22bf3290 | -19.54218 | -46.76406 | 2025-07-25 04:25:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c3bf9fa-30b9-3ec3-8df5-ac9378e40c49 | -18.97124 | -54.38261 | 2025-07-25 04:25:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdf0c312-8929-36ba-a8c1-aa4aefc29cc6 | -18.97214 | -54.37797 | 2025-07-25 04:25:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fac412aa-07e5-368f-b247-39ee487d4ec3 | -21.60804 | -57.57371 | 2025-07-25 04:25:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d2f8109-6f02-3a0c-bd82-eadffd030354 | -18.42204 | -54.55842 | 2025-07-25 04:25:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc498a7c-afed-382e-a243-9508c1e8b74a | -19.41223 | -44.96422 | 2025-07-25 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4ab4802-7492-313b-9fbd-e3d6aec7b401 | -20.68366 | -46.31126 | 2025-07-25 04:25:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9702ce00-3b9b-3a58-a576-1f59ec235c81 | -18.70598 | -48.25898 | 2025-07-25 04:25:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9aa4cf5-7c1a-344d-930f-7ea34bc442d0 | -19.24905 | -46.95375 | 2025-07-25 04:25:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1c8c0fd-f0db-3159-a89d-81b0aee8e5f3 | -20.29177 | -42.87619 | 2025-07-25 04:25:00 | NPP-375D | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a9592170-eed1-30be-860a-65b4842fb40a | -19.16439 | -46.58778 | 2025-07-25 04:25:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4a2b3b32-d512-3371-95fe-694fabd74279 | -21.07497 | -49.86477 | 2025-07-25 04:25:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e57ccc68-8133-3b9d-9ba6-f27a98eb8706 | -20.47497 | -50.90805 | 2025-07-25 04:25:00 | NPP-375D | APARECIDA D'OESTE | SÃO PAULO | Brasil | 3502606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b44e03fb-e878-396a-b05d-65ff5d26a0e7 | -20.05352 | -44.61054 | 2025-07-25 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51d1a2e3-f039-382c-8da4-e46f8647ea3a | -20.22331 | -50.91494 | 2025-07-25 04:25:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| cac2d1d3-e502-3012-9071-9fad46660aeb | -18.70265 | -48.25837 | 2025-07-25 04:25:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6cb8e6a8-8d7c-30f6-bfd7-449b019888a9 | -21.61419 | -45.13217 | 2025-07-25 04:25:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f7799371-dd84-3e89-983c-835ed6438af9 | -22.39873 | -49.79691 | 2025-07-25 04:25:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b3170ad4-6289-3791-b5dd-9bab2e6057be | -23.08363 | -54.25337 | 2025-07-25 04:25:00 | NPP-375D | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 426f96e7-e284-345c-8196-3605e825d0d9 | -20.68082 | -46.30689 | 2025-07-25 04:25:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7db8a3b-0fec-366c-9949-a69fcbb2600d | -22.14785 | -51.38212 | 2025-07-25 04:25:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 14ea72c3-7473-3a4b-9d63-10170630a4a6 | -20.22687 | -50.91567 | 2025-07-25 04:25:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 61896d2a-56dc-3eb4-a050-7c754d17e2c9 | -19.54274 | -46.76035 | 2025-07-25 04:25:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f6864c7-91c8-35bf-a7ca-41eccf64f351 | -19.16496 | -46.58404 | 2025-07-25 04:25:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd867fa0-01f0-3053-8f42-a7e39674883a | -19.77311 | -47.97319 | 2025-07-25 04:25:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f0f8de5-e220-302e-9b2b-9fd37d7e7eac | -18.85162 | -41.99262 | 2025-07-25 04:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8918ff45-f868-3a50-ad87-a41f363d0ade | -20.55596 | -49.30639 | 2025-07-25 04:25:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 47ec35ec-579a-378f-9234-cf095fce3127 | -23.07956 | -54.25244 | 2025-07-25 04:25:00 | NPP-375D | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 27cd3537-bab6-3c3f-80f2-f3d21c813744 | -19.75514 | -54.00201 | 2025-07-25 04:25:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a26b3db4-393d-337b-9c71-32cdea790bd6 | -20.35045 | -45.53798 | 2025-07-25 04:25:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 05f846e2-8254-3cd1-9e54-38a94bfdefc3 | -20.49829 | -45.48128 | 2025-07-25 04:25:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 610a03d8-79a3-34b5-83ff-ec14f0e2df86 | -21.4706 | -44.96074 | 2025-07-25 04:25:00 | NPP-375D | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b2cdbecf-198b-3e76-99f7-2478c258d8d3 | -23.20795 | -49.41072 | 2025-07-25 04:25:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d633714b-0127-3361-b406-c6583012f82f | -11.4584 | -45.1126 | 2025-07-25 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| be3feb65-eaf0-3ed4-bcce-74b39b361a7a | -6.5939 | -45.6081 | 2025-07-25 04:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| a9292b10-1acf-3d5a-a4f8-25eae20d06a1 | -6.5752 | -45.6096 | 2025-07-25 04:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| fa06a2b9-56ba-3fff-b829-033d3d49ccc7 | -11.458 | -45.1357 | 2025-07-25 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ab5ee4e8-bcb6-3ea2-9195-7051c845e827 | -6.5631 | -51.1126 | 2025-07-25 04:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 854de392-3c94-35fb-ba2b-5fd836d10d5e | -7.2597 | -43.0645 | 2025-07-25 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| ecd6eb0a-decb-3d06-9f62-cbd92dace7b3 | -11.4584 | -45.1126 | 2025-07-25 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| e1b3a92b-fb3e-398a-b4cf-8504d83cc2e9 | -8.9064 | -45.5706 | 2025-07-25 04:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 6dbe03c6-20ef-3104-bcb0-bf4403d5059d | -2.91031 | -48.24488 | 2025-07-25 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f05cee2f-2b46-3b02-896f-0fb0fea63d18 | -3.18069 | -49.45095 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64a9162a-97ca-3b59-83fc-d0bf0097b9ee | -3.18014 | -49.45444 | 2025-07-25 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00b69884-73d9-33a1-ab5c-8fd869cbca77 | -7.85867 | -48.22482 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 601a3d98-3f60-3158-9c25-eea93cfef930 | -3.12318 | -47.01384 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2750d165-ee93-3d8f-a7a6-838b8454cc7c | -7.85313 | -48.21845 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2800275c-5feb-316e-8391-5f5fb360b08a | -6.65269 | -43.05355 | 2025-07-25 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d6a42de-24eb-3b8a-b4df-37afec10c774 | -5.98894 | -45.72589 | 2025-07-25 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6331abb-7a4d-392e-8fef-b89e84a90ea5 | -4.35015 | -47.68836 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| adb03fa2-0918-3daf-bf79-2a5d5ee36f19 | -8.08401 | -43.15316 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ba45a714-321e-38d0-828c-f42510b8d852 | -7.86825 | -48.2165 | 2025-07-25 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeb9a32f-0c7b-3273-841d-1b353e2928fe | -8.51146 | -43.31268 | 2025-07-25 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| a6b557c6-8471-37df-b2d3-ce8dbe0c014a | -4.64611 | -46.46817 | 2025-07-25 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d46c6cbb-3fed-3ca3-b601-c5a1e16adf06 | -6.4903 | -50.26552 | 2025-07-25 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee5683b3-ef28-3656-a58a-71bf218c0b5e | -8.33264 | -46.29365 | 2025-07-25 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de468fdc-946b-3d80-a90b-1717b3a5a1b0 | -6.87876 | -43.12075 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc4c36db-9070-35b9-beda-247d5ce31e93 | -7.90586 | -44.08987 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2d66b21-24a9-365a-afc5-82adea6ecd75 | -7.88554 | -45.53899 | 2025-07-25 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a8d92bc-adb5-3aff-8e64-440a81b24a25 | -7.92157 | -44.08146 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c0f1b19-cf73-3768-a6c6-1bd5baa64180 | -7.24969 | -43.05934 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 64f60cfd-b35e-3465-9330-65b5dafa7804 | -2.28237 | -48.56527 | 2025-07-25 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ea0b784-d7e7-35da-87d3-bc2f761f071a | -4.2921 | -48.06038 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f0c0b5c-51ff-300a-8927-72785a919b99 | -2.86176 | -46.77113 | 2025-07-25 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f045c611-e514-3017-894f-750f663142ad | -6.93736 | -42.80712 | 2025-07-25 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a5a47501-564a-3dec-9125-848e65118f49 | -4.57412 | -48.01554 | 2025-07-25 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 27b1abd0-8b55-3597-8139-bb2b3a55e8c1 | -4.03511 | -48.06253 | 2025-07-25 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb5c0760-8f5f-365a-b4af-5ba623802878 | -7.48342 | -49.23069 | 2025-07-25 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b2f201a-d25e-3f85-bf3b-0cbe1cbd1695 | -7.90809 | -44.08149 | 2025-07-25 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c59b9fde-6227-3aa4-b314-f4830c8c0d61 | -7.26355 | -43.07033 | 2025-07-25 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README20.md)
