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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd4a4405-56ff-30ef-95c7-1f6ee995aa3d | -11.73484 | -54.247 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08cb330f-9340-3f3c-8a2e-d2dfeea7bd91 | -14.12518 | -45.31146 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5cd6e40-d7ba-375e-b3ff-61320feef68b | -14.11907 | -45.32141 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2400a689-d600-3767-9548-1d1f4c6dac9b | -14.14689 | -45.41089 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a37ae75b-65c8-3853-8df6-4d3c11d30c88 | -16.43428 | -54.91454 | 2026-05-13 04:55:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42d577cf-8d55-3594-8e4a-35145bcd9d6b | -13.68429 | -44.29209 | 2026-05-13 04:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caf8f5ec-f8ed-30d2-8a4c-7084d7e1db4e | -13.68469 | -44.28893 | 2026-05-13 04:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ae5871d-425d-38fb-a2c4-e66364207041 | -11.73889 | -54.24383 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66cb81ff-7b21-39cc-9211-292b7aa17e19 | -12.23126 | -49.39151 | 2026-05-13 04:55:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9566d861-0223-3d99-956e-3875c1751ce6 | -10.40199 | -46.65071 | 2026-05-13 04:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8dc3f57-1be3-3ef6-8e40-e5d555eee630 | -11.96803 | -46.78384 | 2026-05-13 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28e27cdf-eb33-3c2b-b52e-1fd18df28296 | -10.40506 | -46.65884 | 2026-05-13 04:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8359cb00-ed25-3ff9-baa1-787758ba5e03 | -14.12442 | -45.32125 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be0f0bce-df9e-3b76-a130-aa640e0883f7 | -11.57981 | -54.5688 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7aedb901-4887-32a4-9c9f-9cc39656334b | -11.84196 | -49.44024 | 2026-05-13 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd343c8b-943e-374e-a5e0-1a8d05482575 | -10.40247 | -46.65435 | 2026-05-13 04:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d125a3be-ddc4-3740-9e6f-31e96dad5afd | -12.62025 | -44.52069 | 2026-05-13 04:55:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27d44a30-728b-3d81-815e-36028d06b7c3 | -14.13347 | -45.32339 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e756079-e381-3d19-8fe7-e7e318247b93 | -10.28736 | -53.97513 | 2026-05-13 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b346932d-48de-32fd-8079-9f9ea2df05c0 | -14.31129 | -49.24695 | 2026-05-13 04:55:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0967352-edc1-30e4-804a-70450090bd32 | -11.92726 | -54.09855 | 2026-05-13 04:55:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e6f140a-f03b-3c71-9551-b3980f80b268 | -12.1115 | -43.6435 | 2026-05-13 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a77d4971-fd85-3863-8f13-8019bdf662fd | -11.98437 | -46.79008 | 2026-05-13 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ae20a69-7d95-38bf-9d68-b028fb718324 | -10.56186 | -45.06056 | 2026-05-13 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f0d3a89-85cd-352c-87a3-113fad26b7a7 | -10.6627 | -49.70752 | 2026-05-13 04:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b7f12c83-ee5f-3179-a2aa-ffc21e505688 | -12.07925 | -51.25542 | 2026-05-13 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 984d4aa9-08fd-3199-a4fd-bc2a0e82fa72 | -12.85728 | -43.76128 | 2026-05-13 04:55:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6bcd811-d6cc-32ea-b313-847f020f43e2 | -10.18739 | -49.59113 | 2026-05-13 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53238104-cb82-3c25-a850-3900cc5cf907 | -11.73546 | -54.24324 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dfe6940b-bc47-3ac7-82a7-9ad470f13f05 | -11.97225 | -46.78443 | 2026-05-13 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44f7e60f-5151-371b-9de2-76f1968c5594 | -10.48815 | -49.3602 | 2026-05-13 04:55:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 124a7912-31e3-3d26-8175-19614cf5170d | -11.26722 | -55.79255 | 2026-05-13 04:55:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 663e46a0-1350-30dd-8930-f5965efb4a5d | -11.74014 | -54.23633 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e471ec58-7771-355f-bdea-8ecfde2e49e1 | -10.48398 | -49.36369 | 2026-05-13 04:55:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19aec0fc-68ec-393c-afff-b162d9666da2 | -16.42427 | -52.79612 | 2026-05-13 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c7b4e64-ec8a-3690-9339-1f4b63d08e24 | -12.05189 | -45.28795 | 2026-05-13 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6143a8c8-1fd5-3847-8c21-75020990716a | -10.48754 | -49.36426 | 2026-05-13 04:55:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d975c83-5e25-3b81-98f2-6f300e1934ec | -14.12031 | -45.31529 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44a11709-df02-3f42-abdf-84344f488173 | -11.63437 | -54.15711 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e06ccc2b-400e-30e2-98e3-b6a96776ab4d | -14.14013 | -45.42604 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5966972-5185-3c74-a1c7-1d472648541d | -11.631 | -54.16053 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26a807a8-8cdc-3b9f-903e-467aad5ea0df | -11.63313 | -54.16459 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c96c44e5-5193-35ae-9326-fe005390926e | -11.93729 | -43.37866 | 2026-05-13 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2db43f0-3ca8-3d49-9643-e20d3ea407ed | -11.80014 | -43.62944 | 2026-05-13 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 006c3821-8a2b-3ae9-b3f6-6c661e03ef71 | -11.67196 | -49.00139 | 2026-05-13 04:55:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 916052aa-115a-3621-a1f6-2ad417a30fba | -12.11594 | -43.65063 | 2026-05-13 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 993b2115-853d-39ae-b675-2d8b1ef911fa | -11.74231 | -54.24443 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 703c45b2-7c49-3705-a5e7-dc798caa6292 | -11.63375 | -54.16085 | 2026-05-13 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d58759e-714b-34d4-bd05-d8ca05ae450a | -14.11482 | -45.31992 | 2026-05-13 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4419164-7f0b-37aa-b83c-300925b83327 | -11.40847 | -48.44213 | 2026-05-13 04:55:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff98f979-5b53-3384-a715-cea597c8adaf | -22.87574 | -48.63147 | 2026-05-13 04:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abdc4cbf-cfdf-331a-836b-86af4150ba96 | -23.40786 | -46.42038 | 2026-05-13 04:57:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b9c069bc-7fba-3a0c-8150-ea1fc36fc8ef | -22.87627 | -48.62706 | 2026-05-13 04:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dae28f81-922e-32e4-a19f-4bb03485ad1e | -18.37022 | -48.57101 | 2026-05-13 04:57:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 373d828d-e646-3719-8cc3-564d9c020252 | -21.97746 | -57.58907 | 2026-05-13 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be179658-c5c1-37cf-ac3e-ea1592c8e013 | -21.97395 | -57.58836 | 2026-05-13 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 766a03a1-58c3-3097-bcc5-8c0822e50715 | -18.37283 | -49.27068 | 2026-05-13 04:57:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56fdf0a2-6183-3de3-9e0a-72c87da84b02 | -21.33585 | -47.02353 | 2026-05-13 04:57:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 10790c0a-ffcd-3fd4-9277-06a0ee90b53f | -21.33524 | -47.02893 | 2026-05-13 04:57:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3962bf6-7893-3464-a94c-3679fc4d4bc8 | -18.36612 | -48.5704 | 2026-05-13 04:57:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 19955556-3f50-3e67-9ef0-04447c3c2bda | -22.87669 | -48.63021 | 2026-05-13 04:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4deb889c-f1e4-3c8f-bb3c-a4c2c89da4e7 | -18.03445 | -54.57304 | 2026-05-13 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2336b134-2b3b-3bb7-99b0-69b2ddb4f6f0 | -18.03504 | -54.56937 | 2026-05-13 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7401bd7c-fed0-352a-995b-201497e0e23f | -18.22297 | -54.59771 | 2026-05-13 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc9b0ed7-1d8d-3a39-9753-ab07e09cbc3b | -19.96792 | -47.20714 | 2026-05-13 04:57:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e20ee2d-2643-3dd4-ae8c-9624f8af6f90 | -19.20104 | -49.12709 | 2026-05-13 04:57:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39db59ed-100c-3aaf-a2b6-d3adc3786e2d | -18.03288 | -54.56147 | 2026-05-13 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 096edc09-3b48-372d-bb5d-7191bbf603ab | -27.23164 | -48.76601 | 2026-05-13 04:59:00 | NPP-375D | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 174f2057-592a-3a28-9053-371e8601a08b | -27.22778 | -48.76429 | 2026-05-13 04:59:00 | NPP-375D | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1124fc5b-48c5-391e-8af1-21679e6aedb7 | -27.23236 | -48.76475 | 2026-05-13 04:59:00 | NPP-375D | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 46446abc-11c1-36cf-8177-90c7cc0ff294 | -7.28043 | -46.79802 | 2026-05-13 05:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95b1bc8c-beb1-38d5-a5e9-07b910139bf4 | -7.27985 | -46.80242 | 2026-05-13 05:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae7a573b-946d-3ed5-8079-8902377d7644 | -14.13255 | -45.31418 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19405817-a871-3db9-8227-535e092e9847 | -14.13027 | -45.31688 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 169cd557-1ebf-3814-92a5-42632269630f | -14.13344 | -45.42666 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 881f2ef6-cd22-39d8-9d30-4d906f936205 | -11.97156 | -46.78747 | 2026-05-13 05:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69edcf8c-d1cb-372d-b79e-79a5b0aa6d90 | -12.07994 | -51.25569 | 2026-05-13 05:14:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c054381-b0f7-3547-893f-0fc22978a26f | -11.4075 | -48.43935 | 2026-05-13 05:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 901a526c-b9cd-36cb-94e6-bd0604bbea87 | -11.96946 | -46.7849 | 2026-05-13 05:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe8ec062-4b1f-3ee4-86fc-a65a7fa1779a | -11.74012 | -54.24128 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca36dd43-3bfb-3aca-9315-6e8eab2fcf31 | -8.70251 | -47.97924 | 2026-05-13 05:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2362152c-3dfa-38a2-a803-b7ab9c92fe73 | -10.40509 | -46.65421 | 2026-05-13 05:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 24f00de2-1678-3e3b-9e69-b7af2a5dfb4f | -11.29673 | -54.01976 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d34a6d4c-086f-384a-a623-2ec5e5060105 | -11.73246 | -54.2402 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a53da1e3-2524-33ae-a13d-a14aed55c7b0 | -11.81328 | -52.51986 | 2026-05-13 05:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19c90855-868b-3d79-a8eb-f62c6073abe8 | -11.18729 | -55.92344 | 2026-05-13 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cce35b3-3b0f-3cfc-b978-5985cbc8efe3 | -14.13095 | -45.31004 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11a1464d-de35-3b6a-beb3-8fcab9eca166 | -11.73629 | -54.24075 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44ab7617-fb1a-3db7-b021-0b7c9e5445fc | -10.6639 | -49.70771 | 2026-05-13 05:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1290f8df-23c6-3619-9364-1cad4e810994 | -14.1185 | -45.31267 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 504926fe-5d8d-3709-818d-2ce8db7d07f2 | -11.84081 | -49.43921 | 2026-05-13 05:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a1f36c4-ed85-3520-8339-c530fb24a867 | -9.45548 | -47.79496 | 2026-05-13 05:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2e55d73-bfac-3f79-addc-e552234f71ab | -8.54138 | -45.98233 | 2026-05-13 05:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 424d5cca-490d-3f89-b327-04014941272b | -8.54075 | -45.98715 | 2026-05-13 05:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4e8fa07-3b99-3329-84e8-39741db973d9 | -14.12325 | -45.31609 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbb1fba1-0542-36d3-abfe-c267ba86c29e | -11.98414 | -46.78876 | 2026-05-13 05:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d6d9a14-7e7f-3e6d-9af3-9c923e8ad579 | -11.95732 | -54.68572 | 2026-05-13 05:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47cabf97-019d-3ac7-b5bb-e499900e3875 | -11.73899 | -54.23839 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 179423ab-b852-3615-9cbf-a1889ed73d41 | -11.268 | -55.79051 | 2026-05-13 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59965454-8e77-3d38-8e42-b801f74eac17 | -10.66429 | -49.70467 | 2026-05-13 05:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)
