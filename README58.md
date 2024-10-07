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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44f00793-7e41-3a34-9d28-113b3c7a1c13 | -12.40301 | -47.05616 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0487b30f-8958-3cb3-8dc3-f16b2d54176b | -12.40231 | -47.06017 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cdf4a60-c0ec-3664-aff5-6ce954dbc13a | -12.40161 | -47.06414 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8dfae68b-2613-3b70-b7e9-51c740d1f671 | -15.16818 | -47.07636 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aeb755f5-e9e7-3b32-ab9b-59d50d535f1c | -15.1675 | -47.08011 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43107ebc-6baf-32a7-bb4d-3923abd662d8 | -15.1668 | -47.084 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9eb8b572-c110-33fa-a4a1-f08f679e1ec8 | -15.16416 | -47.07561 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6b2f149-b456-3344-b8da-76df0dcc3092 | -14.27942 | -47.41056 | 2024-10-07 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d6ec32b2-5103-36db-b599-38d31128122a | -14.27875 | -47.41434 | 2024-10-07 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 088e8612-6363-3a67-8106-bcd9ec63c2bf | -14.04341 | -47.27482 | 2024-10-07 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 87ff9ce8-15db-3009-be50-27d0fcd5febc | -14.03932 | -47.27378 | 2024-10-07 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4009919-4e99-3725-9572-5a5a987b478b | -14.03869 | -47.27722 | 2024-10-07 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 41e68bcc-b1d4-38fd-b19c-368b5561ef90 | -14.02402 | -47.28711 | 2024-10-07 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 740f5966-ad5b-3913-9489-0ca5c79765fe | -14.01994 | -47.28601 | 2024-10-07 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a1e5918a-54b8-34a5-b0ac-b76dc16e8a12 | -14.75339 | -48.05326 | 2024-10-07 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b88c72fa-2f0e-3954-8ce7-dcdf7e168546 | -14.74905 | -48.05267 | 2024-10-07 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 908a79ff-6902-3254-93a8-4b9cff7cd93b | -16.48872 | -48.02477 | 2024-10-07 04:02:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0210c1cd-5f1f-305a-8278-ed7fa4a3313d | -15.91828 | -48.18259 | 2024-10-07 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61d75db2-1c4e-374b-86a5-a883dff76488 | -15.91746 | -48.18694 | 2024-10-07 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0284bff-b9ae-3eb3-81da-64c65378ba63 | -15.91402 | -48.18182 | 2024-10-07 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37e1ad3d-6358-3340-8feb-84b198a502c7 | -15.56951 | -47.85761 | 2024-10-07 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2035206-28e5-39ed-9b1b-c40e0fa24040 | -16.2042 | -47.30094 | 2024-10-07 04:02:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7458d6df-fb3d-30e1-bdb4-24bcffbbc3c1 | -15.70278 | -47.15365 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c07c90d-82a6-3a84-9471-361f1b2b39ca | -15.70213 | -47.15723 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 417960ed-5cbd-3b94-a415-75320c13165c | -15.69878 | -47.15289 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33d5254f-e824-3d14-91d5-625b854a4e1a | -15.6361 | -47.72984 | 2024-10-07 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 749bfa4a-fc02-3b72-bfd6-15bc5a70ab69 | -17.91171 | -48.61633 | 2024-10-07 04:02:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a153632-ba33-3564-afe6-f2aa440ff723 | -17.90827 | -48.61138 | 2024-10-07 04:02:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a75b0625-9888-3c6a-aa85-dd5dbfe0e53c | -17.90749 | -48.61546 | 2024-10-07 04:02:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc14d015-4b56-3872-ba9c-64b0822be275 | -17.90088 | -48.60622 | 2024-10-07 04:02:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd0e2a10-8623-3f19-ba5c-53929272aa32 | -17.90066 | -48.60536 | 2024-10-07 04:02:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d819e14-0891-32e1-8e3f-721c1aea5ea0 | -17.88987 | -48.61588 | 2024-10-07 04:02:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f26f2dec-22b1-38cd-860f-3b961e27eae3 | -17.88177 | -48.6148 | 2024-10-07 04:02:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9088cae7-32ef-3486-b991-aa4a4e36c7dd | -17.87757 | -48.61383 | 2024-10-07 04:02:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96d3e343-37ca-3562-b085-0d4d68a03bf9 | -18.09198 | -47.83907 | 2024-10-07 04:02:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24560588-eff9-3180-b42b-755cb9af3a0f | -18.63906 | -48.66693 | 2024-10-07 04:02:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0781f56c-6d5b-35a3-9edd-5c3c04480015 | -18.63832 | -48.67094 | 2024-10-07 04:02:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef8ea987-3827-309c-9834-2e63dbb5ad20 | -18.90661 | -48.19466 | 2024-10-07 04:02:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ba2ae29-ca57-3953-82f5-2b110b6b02a3 | -11.63507 | -48.44691 | 2024-10-07 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ccab8a8-cb75-3098-a148-5575283d5f74 | -11.6304 | -48.44605 | 2024-10-07 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd452a35-bd6b-332d-b5cd-1a7d9e1e8f9f | -11.62754 | -48.33254 | 2024-10-07 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2e646cb-554d-3e6b-ab77-2a63a7af73d5 | -11.62662 | -48.33747 | 2024-10-07 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bce3ed83-b338-35c1-afed-a6e27d98083d | -16.57383 | -49.0828 | 2024-10-07 04:02:00 | NOAA-20 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75fdde0d-14ae-37bb-a0bf-e90890142ced | -16.35706 | -49.93388 | 2024-10-07 04:02:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 619bcac9-43ed-3f51-8cf6-7451026ef797 | -16.14208 | -48.89304 | 2024-10-07 04:02:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6b6fb4e9-28b1-37f2-89f8-658c493f0552 | -16.14122 | -48.89753 | 2024-10-07 04:02:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 50e9f5be-28d6-3cef-886c-46a4a6b4b329 | -16.14038 | -48.90198 | 2024-10-07 04:02:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be30c87e-aca2-32fb-8d29-a796256fa740 | -16.13764 | -48.89221 | 2024-10-07 04:02:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 392f4ef7-a787-3c5b-980a-4bc1ac8a2ab8 | -16.13677 | -48.89676 | 2024-10-07 04:02:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 10bfe5d0-52cd-3fdb-a629-a6cd3d8bc91f | -16.10025 | -50.23361 | 2024-10-07 04:02:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bed3568f-dc3d-3159-85fa-72f65d42ec02 | -16.09766 | -50.2212 | 2024-10-07 04:02:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b1a4bf1-7264-38fb-ab04-7950e88f0046 | -16.09655 | -50.22682 | 2024-10-07 04:02:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b5626be-8c2f-3300-8631-03322c48d088 | -16.09296 | -50.21947 | 2024-10-07 04:02:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 669a1e15-14c3-3a7f-b145-e570d862dbfd | -16.0883 | -50.21757 | 2024-10-07 04:02:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7dbaac1-649f-350a-adc0-f4f3b18cfaff | -16.08362 | -50.21579 | 2024-10-07 04:02:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7f009f7-a02e-3274-8de8-3703d54c468c | -16.07888 | -50.21432 | 2024-10-07 04:02:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8af09a8e-d0a7-3ab5-875d-c0fd18213633 | -16.07607 | -50.21239 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e3fe708-3af4-33b3-9086-51e39f9c95a1 | -16.07487 | -50.2187 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b82575d-da6e-384c-86f2-ba61b010410b | -16.07374 | -50.21487 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71b9317f-c447-34db-8a2c-81c88e6b7f54 | -16.07371 | -50.2248 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c434f90-4804-37bd-b695-d47037c908e4 | -16.0725 | -50.2211 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb0090c8-368e-3bb9-8782-bf19dbe7ce57 | -16.07132 | -50.22701 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6cce4ec-b6c8-3d91-a1b6-d54369d8d40b | -16.06865 | -50.22497 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f346d0f7-b85d-3372-bd48-812de586905a | -16.06746 | -50.22112 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68542391-4dae-33b8-b500-9ad4c02cdde1 | -16.0663 | -50.22691 | 2024-10-07 04:02:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ddd5674-e2cf-34d8-9fa9-511d47396d83 | -17.62134 | -50.19972 | 2024-10-07 04:02:00 | NOAA-20 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ea58a48-b9a8-39a3-b4bc-f09b5e06263c | -17.26392 | -49.21906 | 2024-10-07 04:02:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b61f4041-5621-3df3-bc60-7837eba816f3 | -17.26304 | -49.2236 | 2024-10-07 04:02:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cadddc6-bfaa-3dea-ae52-8eba2bc6d3ac | -17.25863 | -49.22256 | 2024-10-07 04:02:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2b084078-929b-3bf3-8312-9e485086c1be | -17.00794 | -49.78438 | 2024-10-07 04:02:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5113a5c8-dff4-324a-8185-f6b149baf5a7 | -16.72847 | -49.17087 | 2024-10-07 04:02:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef7e4bcb-26c8-307e-a5de-c989c264e8b1 | -18.10907 | -50.15806 | 2024-10-07 04:02:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a83a5ce-bc52-30f1-a2b2-8dd40cb61905 | -12.20597 | -50.54716 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1c8ddf8-8747-3a10-9433-33b7fa025e45 | -12.20531 | -50.55055 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1ac19c2-9219-3660-b3dd-4795d76e8491 | -12.2026 | -50.5466 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16911635-0960-3c47-bc64-7d4612868f0a | -12.20196 | -50.54999 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1d01dc8e-ea5e-33b6-b804-98e1cba61473 | -12.20067 | -50.54609 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14967aa2-eef2-325a-ab3b-8b78463806a4 | -12.20001 | -50.54947 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 504f7dfe-ef89-3616-a188-4e23f00634b5 | -12.19665 | -50.5489 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d08ed632-7b9b-3725-b5f1-bd1e65a291a8 | -12.1947 | -50.54839 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 429fad6c-f7e5-3a3f-8311-274663a65ade | -12.19199 | -50.54441 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43d9145c-c4d6-3ea8-8be0-f5e1398cb56c | -12.19135 | -50.54781 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5415dd4a-7aca-37db-94f9-abcc9a63d08d | -12.19007 | -50.54393 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4226767-0810-39c3-a88f-7b7847aa1531 | -12.1894 | -50.54731 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 738e2a96-49e3-3ae9-bb6b-e48d5883024a | -12.18733 | -50.53993 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41d0ba93-61fb-3370-be56-1213921f5761 | -12.18669 | -50.54332 | 2024-10-07 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae282a9a-7d6a-3466-8098-47348805ee0c | -12.14993 | -50.89027 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da3fd5bf-6479-3ee8-98f8-70ab9e603877 | -12.1431 | -50.89632 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 446b6aa1-39cd-359f-8c09-9f1be0b9577c | -12.14218 | -50.89661 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f12fcb1c-a8da-3c2c-882d-f7081f96051c | -12.13201 | -50.89077 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08c9f59c-e89e-3a16-8cc4-db2f73041eb8 | -12.128 | -50.91561 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee3fbbbb-a5a8-3237-9b49-8f5636735bf4 | -12.12753 | -50.88941 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 560e0be0-d992-3da9-b85a-5d98c59e48cc | -12.12723 | -50.91593 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22c1ad08-da0b-304a-93df-7fd650b6bbe1 | -12.12682 | -50.89299 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65e6b5a6-7169-3ae9-a347-130d367daa22 | -12.12658 | -50.88964 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e153aee3-ae35-3391-9a90-74274abec253 | -12.1259 | -50.89323 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 740d859b-8235-3784-ad4c-613175d00111 | -12.12522 | -50.89682 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efe82ac8-095e-3972-a237-e4a7e0cc6c3d | -12.12139 | -50.89188 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f595bd1c-5e71-34df-81c9-64b52acb679e | -12.12068 | -50.89547 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 773367e3-fa89-3293-8d2c-b5c31991c124 | -12.11979 | -50.89571 | 2024-10-07 04:02:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README59.md)
