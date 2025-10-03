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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5859d12a-f353-3515-87f1-5a2327c9a10f | -14.94164 | -46.88197 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 24283ed8-80a1-3fa2-b9ea-c94c40cdcf6d | -14.73619 | -48.11691 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |
| b6413174-bcdf-3750-8371-e4514afe1ef5 | -18.40669 | -50.78443 | 2025-10-03 00:50:00 | TERRA_M-M | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e52330ab-49b3-36ec-a65d-513e4ec8ec9e | -14.74024 | -48.14239 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 7ab27a26-d96b-3ac8-ad42-615baef07c2b | -14.69697 | -43.88255 | 2025-10-03 00:50:00 | TERRA_M-M | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 99.5 |
| efb2631d-3d78-3ad5-a387-673d40425fcb | -15.92126 | -43.35029 | 2025-10-03 00:50:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 19a4ee17-787c-3252-ab19-6d3bbe8cd50f | -15.28203 | -49.31437 | 2025-10-03 00:50:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 936dd540-e8e6-32d8-9af3-975f6cf36cb8 | -14.89939 | -46.98875 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| c83d7eb2-1df5-366c-b80c-eea49accf7f0 | -15.21096 | -47.19625 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5d4cabcf-e4ed-3e0e-b82c-61f63e07b800 | -16.35099 | -47.10948 | 2025-10-03 00:50:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 72362a84-2c10-3012-9154-8544ca2953a6 | -15.30794 | -46.30045 | 2025-10-03 00:50:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2e8dcbb1-aa0f-35ad-bbeb-dd2220de3479 | -14.88904 | -46.97912 | 2025-10-03 00:50:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f2d46c28-133b-3215-86a3-3553f4afe9f1 | -14.98274 | -49.96559 | 2025-10-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d0eaf317-2e38-32f8-89d7-e17eea325fdf | -16.32944 | -49.94637 | 2025-10-03 00:50:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1ce85750-f5d8-3186-b2f0-574b423eb14e | -15.94669 | -46.22508 | 2025-10-03 00:50:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 38.9 |
| e339ae1e-0beb-3093-a48b-86f8634caac3 | -14.86959 | -48.30779 | 2025-10-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 68af7bdb-c08d-36e2-9f2e-d64b35521ffd | -15.24054 | -50.1338 | 2025-10-03 00:50:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 76b8d395-8ad3-3aa5-8d21-b5df139255b8 | -15.28002 | -47.91493 | 2025-10-03 00:50:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 7dffdbc6-ba72-3ab6-bbcf-1f8b28b311b2 | -16.09478 | -51.05545 | 2025-10-03 00:50:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 34fe2713-4be0-3321-9824-a5bb75e49176 | -16.04428 | -48.07983 | 2025-10-03 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9567b873-9849-375c-a2b9-56b35a1a66c9 | -9.9405 | -43.74866 | 2025-10-03 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 8b44f301-42e1-39ed-b849-8db38970e196 | -15.2541 | -56.77522 | 2025-10-03 00:52:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 8bad13ae-3272-3177-aed8-f2dfdcf6303f | -12.48511 | -54.41118 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6b0c89a4-eb6e-3829-b765-ddd76027dfce | -12.38331 | -46.53112 | 2025-10-03 00:52:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 443242e0-e5d5-3f76-bc35-1af68a7412c9 | -7.79969 | -46.01859 | 2025-10-03 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 8a8f046e-865d-3982-b56d-986ea78d0dc3 | -10.33881 | -54.19209 | 2025-10-03 00:52:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8a626f1f-1152-3d57-b96e-f2761524beff | -10.8786 | -53.76581 | 2025-10-03 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8034cdb0-e76b-3e8d-a39f-0a3080428d46 | -11.27162 | -47.79632 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| be7273fe-041f-3b57-8708-13ca62c9325f | -10.59674 | -48.71334 | 2025-10-03 00:52:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| bc8fb1cb-94d5-38fc-b153-1c9df52491b6 | -11.81414 | -45.0276 | 2025-10-03 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 431c568a-20f9-3628-926f-018fb060b187 | -11.62427 | -47.98919 | 2025-10-03 00:52:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 36329ca2-1388-36af-8e05-cedc82aafc08 | -12.9415 | -48.44233 | 2025-10-03 00:52:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9462ab8c-9868-3a3e-8b85-f64825bc07ff | -7.79984 | -49.8647 | 2025-10-03 00:52:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5fa42f5b-5432-3234-8142-62b6e600f1b6 | -11.0205 | -46.5663 | 2025-10-03 00:52:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 1b63f6e8-e933-32ec-a72b-152b3b40b6f1 | -13.34612 | -48.08135 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd914161-b594-35bf-b695-c54f9f2177f6 | -10.41429 | -54.41402 | 2025-10-03 00:52:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 21c365d2-3ae9-3443-9b8b-b7760e3473b1 | -14.66628 | -48.25788 | 2025-10-03 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ed7ad881-fe11-3887-bba6-ba45cba5146a | -9.90772 | -43.75405 | 2025-10-03 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| ba5ca0a7-ef17-3016-9e64-00c609683a5e | -10.29925 | -48.28389 | 2025-10-03 00:52:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0d5d91eb-6087-3545-b97f-5ec380d8e909 | -13.5463 | -47.30606 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4a3ac02c-5aa5-3d72-8a1e-f3f46ddc9480 | -10.86052 | -47.03585 | 2025-10-03 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6b9f5560-3822-3cf6-9cc6-461b67d716ee | -13.76704 | -47.5374 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 79548727-7132-37e9-ac67-03545ab10217 | -13.20047 | -47.88984 | 2025-10-03 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0b0b67ba-7672-3beb-b3cb-72d99939b13d | -13.30681 | -47.26154 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| b57f029f-3ee1-36b5-8612-342288c97f68 | -13.56565 | -47.29726 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f237aa26-fd89-3fab-bbea-2b20416b7bac | -7.24979 | -49.42198 | 2025-10-03 00:52:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 04a93b65-9426-35c8-adf0-acbb9355179a | -13.23985 | -47.34351 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 805a89d8-e324-3283-bd24-57649e3f1c62 | -9.91785 | -43.75741 | 2025-10-03 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 5a214b27-e9af-3b23-a45d-3646bb54f1cd | -6.95781 | -45.3559 | 2025-10-03 00:52:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| a2a79db0-e61b-3791-9c8c-766d99c7c79f | -14.2 | -46.12393 | 2025-10-03 00:52:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| fd6e5845-fb9b-3aca-bee1-2557d246f8ad | -9.10115 | -46.72213 | 2025-10-03 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1c7ef0ce-bbb7-3a27-9272-e5a52194b221 | -7.909 | -43.54145 | 2025-10-03 00:52:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 44b082d2-13fe-38db-83b4-5d9274c68024 | -13.27116 | -47.23895 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 4ea38a54-3dfb-36cd-9ab1-8729ab1ce2f4 | -12.75723 | -50.55244 | 2025-10-03 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2ac8f8d3-c8c8-358d-9ad3-382a50f0ae5f | -9.91286 | -50.49269 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 17a22eac-e8dc-3c1f-b75d-412372d8a6be | -11.62397 | -47.97971 | 2025-10-03 00:52:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 94420c90-7819-36eb-b6c5-efabe98833a2 | -13.77671 | -47.52979 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 38.7 |
| fcc6f680-99c8-378a-97dd-517912ae9dfc | -13.68464 | -48.02964 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 027bb4e0-82d3-3ed8-af73-82217afd14a6 | -13.86644 | -47.94181 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c858e987-5e3e-3eaa-84c5-b4b0c7dbf60e | -10.67908 | -48.57476 | 2025-10-03 00:52:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 140601cb-ef91-3bfe-95ac-54a7c479705b | -13.96768 | -48.16014 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 642b06f4-bd5a-37c9-96ed-30089ec0ea33 | -13.33676 | -47.22364 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 00e56a2b-954d-3e47-927e-93f1e37804d4 | -8.61075 | -54.96754 | 2025-10-03 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| c470f9c8-a486-3402-8937-884e2e805716 | -13.6893 | -48.63891 | 2025-10-03 00:52:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5f35b533-a9cc-3bfa-abfc-6d2ee6507aab | -13.14286 | -47.89167 | 2025-10-03 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 8532c8c5-86e4-3bc8-8e42-aff8f6173724 | -12.90612 | -46.91423 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ad47563d-a426-3dbd-b84b-f1add82a41c2 | -13.32743 | -47.60612 | 2025-10-03 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1bb12058-7b30-31c6-8f52-1e5c7e6214d6 | -13.19945 | -47.8122 | 2025-10-03 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 30973db3-0348-38a3-aed6-93806d4fd31b | -11.05568 | -47.80102 | 2025-10-03 00:52:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 72c3ca27-b826-3bba-90c2-f5941d9b3188 | -8.66087 | -50.69105 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f12a4035-ffa7-3538-99e9-5557d160c28b | -13.63955 | -50.27753 | 2025-10-03 00:52:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6d452626-7083-3790-957e-65355ef072fb | -8.64995 | -47.71238 | 2025-10-03 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| d6da85d1-d24d-32db-a944-fa3e6b5b334d | -13.12916 | -47.87753 | 2025-10-03 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| ed83bd94-0c61-3fd6-bf5c-13ca8581dc83 | -14.578 | -52.4633 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5be8c4ca-be37-3dcd-aefd-d9c34e52ef60 | -12.61529 | -46.9795 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 10c5e7bd-786d-3989-af48-de0983425bb8 | -11.84849 | -44.96842 | 2025-10-03 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 9e0df25e-712f-301c-b908-b346b12eaf5a | -13.18936 | -47.89194 | 2025-10-03 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4be323b8-498d-3845-ba76-a30c7c4da066 | -13.12431 | -47.84716 | 2025-10-03 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ae1ca7de-40f2-358d-8d0c-7c59cbe63bf1 | -11.48831 | -44.9964 | 2025-10-03 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 1c1b7820-3593-3e62-9aa8-0fc90c78cb48 | -11.48683 | -45.00333 | 2025-10-03 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| c082f64f-d7d2-3b4e-b543-f0bc8c6ef8fc | -6.73012 | -44.14596 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 8cc152ca-397a-3452-b5ec-22cdfb347511 | -11.56268 | -47.66158 | 2025-10-03 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 31f4518d-a2e1-3b2b-bb00-fe389fede760 | -12.83037 | -46.90796 | 2025-10-03 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 94374cd7-037e-3644-adcd-1bc1ac22e3e5 | -8.54128 | -50.15605 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 34a308c6-3232-3496-b810-576e0d0b62ae | -14.29285 | -45.89556 | 2025-10-03 00:52:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 63337caf-e71d-307a-ab8d-a3a9853e1c0c | -10.06569 | -48.18161 | 2025-10-03 00:52:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d34168ba-dfbe-3547-95f0-efa1b3bda638 | -10.85397 | -47.22875 | 2025-10-03 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ce9498d0-dbf5-33f6-a19e-30da9592034d | -6.2434 | -45.39055 | 2025-10-03 00:52:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 832de203-76b8-383e-aa04-c54b927ab247 | -12.35038 | -54.15723 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 866dc03b-ab3e-3fe6-9cf9-0c15c38692b5 | -13.26896 | -47.25061 | 2025-10-03 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 654b43df-2b35-3e7a-bd8a-2cc4bea14c54 | -11.54436 | -49.82467 | 2025-10-03 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0a55c273-64d7-3676-9403-a34799250672 | -10.28432 | -50.3075 | 2025-10-03 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| be9f40cc-fa9f-3b17-b273-94a36cba63fb | -11.06539 | -47.80967 | 2025-10-03 00:52:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 70ed0ddb-c7a0-3ba5-b84c-9ee2ce7ca78f | -14.40148 | -52.11673 | 2025-10-03 00:52:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 78ce22ab-967a-3a4d-96fd-8289b3f57f81 | -11.23017 | -50.79371 | 2025-10-03 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bfb922d8-b2d5-375c-b29e-c0c9de3411da | -7.668 | -47.29547 | 2025-10-03 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d237fab0-5e61-30c6-9991-445f59264e77 | -9.9241 | -43.7513 | 2025-10-03 00:52:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| b4e95f2d-2676-3ad8-bb88-59bc256cfdc0 | -10.12786 | -52.34628 | 2025-10-03 00:52:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3c74dab9-991e-33c3-bfcd-60429bdcfe14 | -13.9637 | -48.11217 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 01aa2edb-df21-35d6-970c-66c2c221b361 | -13.76995 | -48.07367 | 2025-10-03 00:52:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |


[Clique aqui para ver as próximas entradas](README7.md)
