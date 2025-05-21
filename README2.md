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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87d4f950-4c43-3125-8580-162649c6adcb | -11.0903 | -54.7648 | 2025-05-21 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 0ae65153-7758-380c-a504-3d31ed940e6e | -11.0712 | -54.7868 | 2025-05-21 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 88d39fbd-8523-3baa-bb8b-3cf32b721185 | -23.50303 | -47.79212 | 2025-05-21 00:33:00 | TERRA_M-M | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| eb821714-33ae-3be4-8ca9-06322ba28277 | -12.07896 | -47.33109 | 2025-05-21 00:35:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 237f0bf7-7b14-3870-ad6a-df05b4923d59 | -12.83312 | -47.39565 | 2025-05-21 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 316be455-1c0f-3028-bd0c-4141da2b8e8f | -12.84217 | -47.39438 | 2025-05-21 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bf04e97d-1f2d-3576-bd9b-c4d8313ef37b | -11.29957 | -53.97421 | 2025-05-21 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| bf66190f-a219-34be-a73d-0208d54e3b37 | -11.15478 | -48.68499 | 2025-05-21 00:35:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 281d685c-1227-35f6-85e1-0362795a3323 | -12.71812 | -54.97402 | 2025-05-21 00:35:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 2361ad02-de89-3733-a1d1-cf957ea93a28 | -12.29563 | -52.4963 | 2025-05-21 00:35:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 37df8020-60e4-3537-9cc6-57ebbe563e34 | -11.29279 | -53.99394 | 2025-05-21 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 84f68008-bbff-3a21-b629-d529ae99702b | -18.33545 | -49.87235 | 2025-05-21 00:35:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d8de19f0-d421-3707-8a57-863be81c894d | -12.83439 | -47.40512 | 2025-05-21 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cccd848c-d0a5-3cf8-98dd-1aa510952b34 | -14.15407 | -45.47355 | 2025-05-21 00:35:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| beb5669c-757f-3a15-81b7-3bff34a31ebf | -10.90741 | -48.5398 | 2025-05-21 00:35:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7a231362-0842-3563-9697-f231d9621635 | -12.43751 | -43.71907 | 2025-05-21 00:35:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a8a021c0-79c3-38c8-bd64-b9c126f78878 | -11.24067 | -49.5022 | 2025-05-21 00:35:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 54d44839-8897-3eb0-a7a6-8aff96f1c8b6 | -12.08021 | -47.3404 | 2025-05-21 00:35:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c14b1a34-2f9c-3d07-9d85-f7d1381f2bf3 | -11.80636 | -44.27359 | 2025-05-21 00:35:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c7cd080e-5206-38d0-99fa-51d07d1de6d5 | -20.22482 | -50.76116 | 2025-05-21 00:35:00 | TERRA_M-M | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 7d249ba5-6da4-3601-a6e6-e0e0dea25d33 | -11.78168 | -44.28325 | 2025-05-21 00:35:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0fee2cd4-96c5-32f6-bd7b-42a0e87c7132 | -11.14079 | -53.92977 | 2025-05-21 00:35:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| df84ec36-d92d-3b42-abd9-f11629ad41dd | -12.33989 | -49.96603 | 2025-05-21 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 7b54695b-bb46-3c8c-9243-484b947f1363 | -11.79091 | -44.28183 | 2025-05-21 00:35:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 29a6a7b3-e6ef-3e8b-ba88-cfe8df684aa4 | -14.69378 | -45.10815 | 2025-05-21 00:35:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4a44e281-642c-31d2-b45d-5812e7b7a409 | -12.4296 | -43.7309 | 2025-05-21 00:35:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f81339ea-e950-3f1e-8774-b627023477d6 | -10.12899 | -47.55341 | 2025-05-21 00:35:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f13991f5-5804-3a0b-8143-6cfa27f1b9d7 | -12.29329 | -52.47665 | 2025-05-21 00:35:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 92794e9a-0e57-33a4-9f18-5bf641b9d847 | -11.30254 | -53.99923 | 2025-05-21 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 3ffa76b7-d80a-3670-919f-abf35afbdbd4 | -12.87344 | -43.18902 | 2025-05-21 00:35:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 6ab1c85c-b935-32d8-8b2b-c0924fca650d | -12.84344 | -47.40385 | 2025-05-21 00:35:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e3090b40-e290-399d-a1e0-2a5e7d1354e6 | -12.43902 | -43.7294 | 2025-05-21 00:35:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 45def342-5360-362d-b8ad-51a361eb1cbb | -10.10826 | -47.12556 | 2025-05-21 00:35:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d4905356-eea1-35c3-bb1d-c52cf583243b | -11.07874 | -54.80292 | 2025-05-21 00:35:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 33677b3b-9658-3ffa-81a5-dde446b6cd0c | -11.42901 | -44.71902 | 2025-05-21 00:35:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6a30c946-3c28-30ae-bd2e-00e04227d0a6 | -12.42809 | -43.72057 | 2025-05-21 00:35:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 72e1336f-ffeb-3822-9cf1-0356a4e3fdca | -10.23653 | -48.00465 | 2025-05-21 00:35:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3999e79c-b35b-3a45-a7c0-15ba55ffc3a0 | -20.22643 | -50.75456 | 2025-05-21 00:35:00 | TERRA_M-M | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| b3868c41-453c-3b51-ac7d-f2aa0810621e | -11.29003 | -53.9689 | 2025-05-21 00:35:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 078947d8-2af9-3415-94a8-3b40ec13e102 | -12.33827 | -49.95319 | 2025-05-21 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b88868ab-3309-3cf5-8d58-6b2ec2e2113c | -14.16415 | -45.48127 | 2025-05-21 00:35:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| e89f3480-e125-3f69-ad66-43318179bc8f | -14.16289 | -45.47222 | 2025-05-21 00:35:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 5d75bfa4-840e-3c59-9dcd-02f68ea48e78 | -16.04777 | -43.81501 | 2025-05-21 00:35:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a2f0ff3a-c4b8-3f83-a210-5cb1a17ef66e | -11.80781 | -44.28346 | 2025-05-21 00:35:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 605572e3-0dd7-3dba-bedd-8cc1264c5591 | -13.19378 | -47.27122 | 2025-05-21 00:35:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 586e30c4-c7c9-31d6-82c6-02bd3184c8b4 | -19.96952 | -45.16812 | 2025-05-21 00:35:00 | TERRA_M-M | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 03c46f5a-e9b7-3185-b465-4e9e1ad523d7 | -16.04637 | -43.8053 | 2025-05-21 00:35:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 9452a6db-1e84-324b-985a-c03d5e60e8dd | -10.90876 | -48.54984 | 2025-05-21 00:35:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 310e5b06-64da-3cdb-adf6-69e81386ec96 | -11.20462 | -44.50904 | 2025-05-21 00:35:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 430fdd06-eaa9-38a6-bd02-d41d9fe20925 | -11.07556 | -54.77482 | 2025-05-21 00:35:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 222.5 |
| 5ec7210f-03c7-3c5f-8c62-92023444e889 | -11.77478 | -47.326 | 2025-05-21 00:35:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 348e4d91-b39f-3196-baa4-b07160c3de24 | -11.78473 | -47.40036 | 2025-05-21 00:35:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fb09b5db-8e40-31c9-84b7-a0f67217fb8b | -15.89467 | -46.00613 | 2025-05-21 00:35:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 48ceb095-3a39-333c-a4af-5fc4b6efb1f6 | -14.68495 | -45.1095 | 2025-05-21 00:35:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7b8182df-a1a5-3c3a-b2f1-d5b030023030 | -11.81559 | -44.27218 | 2025-05-21 00:35:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 91d6e9d5-4a2b-3671-b8e4-be8b3f5285eb | -12.07771 | -47.32179 | 2025-05-21 00:35:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 51d3520b-f5c3-359f-8a7b-c2d4dbc3b343 | -11.81704 | -44.28205 | 2025-05-21 00:35:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| bdc6c80b-1e10-340e-86f2-cb0222b8b264 | -12.30599 | -52.47507 | 2025-05-21 00:35:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| f3ffdbf9-2609-30a9-800e-a67e0d5cee85 | -13.32396 | -45.40394 | 2025-05-21 00:35:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 97b4b4ff-e232-3a44-9f56-b47828034a8a | -15.89593 | -46.01538 | 2025-05-21 00:35:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4f784928-cfba-31ed-97ad-2156f5c18902 | -11.15342 | -48.67466 | 2025-05-21 00:35:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0fe1fd6f-9ab7-385d-8aae-afce44ee9b95 | -18.33369 | -49.85651 | 2025-05-21 00:35:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b7b5a5df-277f-3b93-9d98-3aca118ffaf9 | -11.68193 | -47.80188 | 2025-05-21 00:35:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e13350d4-8e49-3c30-914c-35ef49c41bf7 | -13.67447 | -53.9372 | 2025-05-21 00:35:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 27.6 |
| c52a59a2-f3cf-3d85-a44e-ea737521a3a7 | -10.34969 | -47.82048 | 2025-05-21 00:35:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8b54a5e5-2aec-3de4-a22f-f298820ac5a8 | -11.69103 | -47.80063 | 2025-05-21 00:35:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7f7298c9-d491-32b5-bd33-f98c9cb3547e | -11.20734 | -49.16392 | 2025-05-21 00:35:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1cc3cc83-eab9-3746-8798-62be20218760 | -12.30836 | -52.49478 | 2025-05-21 00:35:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a870343b-c0c4-3750-b9dc-2b5a753dd1aa | -12.36236 | -49.97601 | 2025-05-21 00:35:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| d7fd50c0-31a5-3993-b4d1-613afb65b97a | -16.02808 | -43.67915 | 2025-05-21 00:35:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 419302c4-96cf-3655-995c-28c5baf03fd6 | -16.02949 | -43.68884 | 2025-05-21 00:35:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 50caf091-9a96-3661-a19c-034994c6ae84 | -12.87181 | -43.17817 | 2025-05-21 00:35:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 27.2 |
| a3865f54-f847-3cf0-b7c8-10ec1b82bfeb | -11.09052 | -54.77282 | 2025-05-21 00:35:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 1c4c4ddf-18bf-3791-a80d-19b47e9bbe3f | -14.16542 | -45.49033 | 2025-05-21 00:35:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 63de3572-ec2d-3554-bfe1-00fca60de64a | -9.94462 | -49.74376 | 2025-05-21 00:37:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cee249f3-b294-313b-92ee-f76e05f0df5a | -9.02384 | -47.75467 | 2025-05-21 00:37:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3a0fe2dd-7c7c-35f5-9d5d-49771ae01ba2 | -7.09251 | -44.3682 | 2025-05-21 00:37:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a48f6b10-f329-31f7-99ef-7eddec384db0 | -8.79568 | -49.07299 | 2025-05-21 00:37:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| df9d37d2-d9b5-3f57-8539-9fe30019e053 | -7.41175 | -49.66311 | 2025-05-21 00:37:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| afa81e2e-4ef3-39a2-ba51-6d1a07c0d388 | -5.89346 | -45.54206 | 2025-05-21 00:37:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a2624b34-56ec-3064-9c78-7918bbaf79fd | -9.67004 | -47.565 | 2025-05-21 00:37:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 91a6706e-400b-3363-86d2-f2a6d6cc51d0 | -8.90687 | -46.90441 | 2025-05-21 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 61671a2a-2c26-3323-b0fd-0ae2f0faab17 | -5.58628 | -45.19886 | 2025-05-21 00:37:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7ecfbd2d-8eeb-3696-8f3c-dc52271edc1b | -6.62868 | -48.02063 | 2025-05-21 00:37:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8974b713-aae0-3b05-9ad5-b2200ab062d3 | -5.57685 | -45.20024 | 2025-05-21 00:37:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4c2b871e-1c22-3045-96de-ce76f5fc8096 | -9.03401 | -47.76249 | 2025-05-21 00:37:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e37a0fb0-2842-3af5-b1ec-e1a64d9bcfc5 | -6.21214 | -43.33101 | 2025-05-21 00:37:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f44359a4-447e-383d-8ee5-ab4a7eb1a7a0 | -9.03635 | -48.94941 | 2025-05-21 00:37:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2b4802ea-6793-366d-af2a-edd8b6f63164 | -7.09408 | -44.37918 | 2025-05-21 00:37:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5487bf07-2d20-3f35-b407-e073ae5d2192 | -9.04293 | -47.76124 | 2025-05-21 00:37:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c11f7640-3069-3f1c-a012-8a2599251bdf | -5.58775 | -45.20903 | 2025-05-21 00:37:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 81c6bdf4-5b77-3236-a56f-724041d73f59 | -9.03152 | -47.74433 | 2025-05-21 00:37:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 398d76fb-b180-3b93-aad0-c683f8868a18 | -9.03503 | -48.93935 | 2025-05-21 00:37:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| cedf112c-b50c-3af5-aa89-3ebe781c47a7 | -8.9081 | -46.91328 | 2025-05-21 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 129da22f-fdf8-31de-ab37-7c1131d2f8dd | -9.76241 | -48.58823 | 2025-05-21 00:37:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b4c2553d-90cd-3a9b-8586-76831df87bb1 | -9.03276 | -47.75341 | 2025-05-21 00:37:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 93b8cdcf-cd9c-3e16-9153-d467b734aa96 | -4.81871 | -44.35873 | 2025-05-21 00:37:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1e2dec94-3865-3c77-9a8d-4f5f5c38d5fe | -9.66114 | -47.56628 | 2025-05-21 00:37:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7dbfa1f8-520f-3995-88ad-a2eb6881e32c | -9.04168 | -47.75214 | 2025-05-21 00:37:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4e681e9b-602d-3529-8b3e-05a6538bf177 | -7.08439 | -44.38074 | 2025-05-21 00:37:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |


[Clique aqui para ver as próximas entradas](README3.md)
