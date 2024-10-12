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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb48ba89-317f-348a-99c6-c0c71342d67b | -5.10642 | -46.18568 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a47cc171-619d-3d2a-aa71-bf1e738e3148 | -5.10582 | -46.18929 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a222135-7e14-3848-87f6-323383d21ea7 | -5.08645 | -45.84702 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 31893072-bbd6-3a41-b3e3-f0d518bfc9de | -5.06549 | -46.07534 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bd3ba59b-45c6-3398-8630-94a8d19d5eca | -5.06493 | -46.07882 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3965097e-0f46-3492-9576-dc07b2d0a18b | -5.0621 | -46.07101 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66d20d51-608f-3e10-a953-5cd73b354df0 | -5.06153 | -46.0745 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88b0467d-b9d6-3b05-bbbf-eed53265cb20 | -5.00799 | -46.02684 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9a101dd-3ca1-32ba-84bc-17b5527f4aa4 | -6.80316 | -46.47651 | 2024-10-12 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03f82839-2158-3e14-9c34-cd1b338bf9e0 | -6.77333 | -46.07853 | 2024-10-12 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd1efe32-e52d-335f-9fda-d1e065a3c55a | -6.70846 | -46.46765 | 2024-10-12 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6379a35e-db05-306f-8739-2311fdb35e2c | -6.54667 | -46.46576 | 2024-10-12 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4556c66-71af-3dba-8eb3-afd5d74fd369 | -7.51983 | -46.59039 | 2024-10-12 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bcaf074-199d-3d8c-8c5e-af1a1421f61f | -9.31639 | -45.90958 | 2024-10-12 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2862775f-56e6-3256-af7f-1383377f6136 | -9.31267 | -45.90899 | 2024-10-12 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8acab538-fb48-31d7-bbbf-d19b6ba5b45a | -9.047 | -46.48089 | 2024-10-12 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90c9c789-2b21-39d8-8d7a-a829a4c07271 | -9.04431 | -46.48299 | 2024-10-12 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af2d96df-3afa-3d6c-a351-2994dc212499 | -9.04314 | -46.48022 | 2024-10-12 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 672eafa9-f7e9-34e5-8478-272f5afaa41f | -9.04129 | -46.47752 | 2024-10-12 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3159850c-b3a1-36eb-a970-e147e143fb07 | -9.03929 | -46.47955 | 2024-10-12 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2421647-ab49-3c86-ba70-359421da67ff | -8.29708 | -45.94677 | 2024-10-12 04:06:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46207172-a0f5-3012-8315-8d9d9e55085a | -8.92263 | -47.05695 | 2024-10-12 04:06:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 273ce02d-dc42-3eb6-a2d8-01e0b009fce2 | -8.91862 | -47.05626 | 2024-10-12 04:06:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbae97da-8828-36dc-909a-c1d3e31bd4b5 | -8.67931 | -46.5895 | 2024-10-12 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23bd48b6-55f3-3ad7-96bf-411bba161327 | -9.52525 | -46.1458 | 2024-10-12 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 277a9c42-6f9e-3487-a42a-72339e16a0cc | -4.85993 | -46.85682 | 2024-10-12 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7b70fa1-5073-3177-b308-0feb13c1771d | -4.85991 | -47.41636 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0bba104-d18b-3bd6-9993-cb62cb05e2c2 | -4.85972 | -46.85952 | 2024-10-12 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ade16e00-7e88-3c5f-acf6-8235d4bcb1c8 | -4.85617 | -46.85488 | 2024-10-12 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d3998fb-2100-35e1-8a88-9a12ccb3e1d3 | -4.85571 | -46.85618 | 2024-10-12 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06617493-9066-3057-8544-53a9cd39656b | -4.6157 | -47.36587 | 2024-10-12 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f7c3c90-0548-33a6-ad23-f4e82446b0df | -4.58661 | -47.09977 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 1aedaaa5-9884-3896-a658-940fd4643d60 | -4.58595 | -47.10383 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| b8cdd4fc-f8e0-3ea0-956f-3cafd1a604e0 | -4.58299 | -47.09482 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fc9ef6a-1dbf-3856-952e-cc5f529a188e | -4.58233 | -47.09888 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| b94edca3-f0a3-3fd8-be9e-413b83d8c17c | -4.58167 | -47.10294 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 6d12757b-1fdc-3cf2-a734-8ac8f564e018 | -4.58101 | -47.10698 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77b52356-241a-3119-a25b-e2682f57e96a | -4.57804 | -47.09809 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66e474cd-244e-3bfb-9224-5b9f62f8a240 | -4.57738 | -47.10213 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05b7bda3-3d3f-3299-a671-4469b3994388 | -4.91558 | -47.65352 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eea390ae-b227-3597-be6e-d231261ed3eb | -4.91112 | -47.65285 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22ba91f5-48ea-37fa-9333-ead40cd78287 | -4.4741 | -47.73479 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae678f7c-fcb3-34e6-b2f7-aec6b29c5843 | -4.47333 | -47.73948 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dbcbd9c-8937-3bea-a5f1-afe8620d93c8 | -4.46959 | -47.73409 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ea3bf7f-eb10-34d4-8422-7d583d5a7b0e | -5.12165 | -47.49807 | 2024-10-12 04:06:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e29fba92-bf3e-3ce5-beba-25c859cfc14d | -5.08396 | -47.18116 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 085fb281-ff7c-368b-a066-4e306b51aa73 | -5.08331 | -47.18506 | 2024-10-12 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5220c3bc-f025-3672-bf52-3dcdf903fc40 | -6.44502 | -47.54721 | 2024-10-12 04:06:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 627160c7-d075-3194-bc3b-d9ccedab4777 | -6.44432 | -47.55137 | 2024-10-12 04:06:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f2ae3ba-c407-303a-98e4-a8ff9519cd49 | -6.44001 | -47.55066 | 2024-10-12 04:06:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d29f83b-9761-3b0b-952d-d1a58f565de7 | -6.13121 | -47.27004 | 2024-10-12 04:06:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16d53540-5b57-3202-aabf-1d66d065cc48 | -6.12358 | -47.87435 | 2024-10-12 04:06:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec3d3a95-912f-3645-ae82-21b3108b2b0e | -6.11917 | -47.87355 | 2024-10-12 04:06:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b2626245-38d5-3749-898a-11592a060251 | -5.74316 | -47.0493 | 2024-10-12 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f4c37e1-1fa4-3887-aa5a-df8ef177fe7d | -5.65119 | -47.92661 | 2024-10-12 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 657f440f-cf50-3089-bf4c-402c859e7c01 | -5.64939 | -47.92411 | 2024-10-12 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45608632-5f26-34fb-a08b-2d4f99bc5242 | -5.64671 | -47.92589 | 2024-10-12 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d7ac8b63-46c1-3a0b-9477-4e630da69d11 | -5.6449 | -47.92342 | 2024-10-12 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13f367d2-1574-3340-af5a-ba83e3bac3fd | -5.63916 | -46.9448 | 2024-10-12 04:06:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ec5d50e-031d-3baa-9664-7ac4bbd4d66b | -5.52157 | -47.69739 | 2024-10-12 04:06:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef09d803-e023-3942-96d1-099099bd2f9f | -5.52084 | -47.70171 | 2024-10-12 04:06:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a62fcd64-a567-3b88-a55f-b4f85b0ca76d | -5.40273 | -47.92511 | 2024-10-12 04:06:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 846ad15b-6880-32c1-954a-5fbbd3e178d3 | -5.40198 | -47.92965 | 2024-10-12 04:06:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9de762f8-8d37-38ec-a4f1-870a41ca4bbd | -5.40121 | -47.93423 | 2024-10-12 04:06:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e08ae563-2685-3175-a2da-f57d1b02fe72 | -5.19524 | -47.84323 | 2024-10-12 04:06:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b3f2d34-4447-3263-8757-10b5f9c150a1 | -7.53841 | -47.09093 | 2024-10-12 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ec34397-3976-38f2-b764-08431c0bac8a | -7.43182 | -47.3541 | 2024-10-12 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c40f0973-8634-32c2-b67f-fda273f02509 | -7.10659 | -48.32699 | 2024-10-12 04:06:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8207e416-7974-3905-ac31-dd4dd33aa9bc | -7.10505 | -48.32446 | 2024-10-12 04:06:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fa47262-f294-374b-b997-d8915c4e02ee | -7.1043 | -48.32894 | 2024-10-12 04:06:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c34f6e8-114c-36e9-9e03-89c2f742ade8 | -6.51534 | -47.82877 | 2024-10-12 04:06:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c7da25b6-824b-33d6-8964-586fe9d61765 | -6.51097 | -47.82798 | 2024-10-12 04:06:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 801ff7c7-20c0-3b5e-8e8b-b15a89784dda | -8.91204 | -47.91524 | 2024-10-12 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f83d5d8-4c07-3c6e-aeb7-9425ed6ab5b9 | -8.91163 | -47.91397 | 2024-10-12 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d59ca63c-8dc6-3354-b449-36331385ef01 | -8.88048 | -47.81953 | 2024-10-12 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92692fa5-e977-3cf6-aaf6-450c025c995e | -8.8798 | -47.82349 | 2024-10-12 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b915168f-3018-3aaa-92ae-217550ac513f | -8.85295 | -47.95419 | 2024-10-12 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afc58c01-d647-3b66-91db-c1eda79caed6 | -8.85224 | -47.95826 | 2024-10-12 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c84c8a7-563f-32cc-92d5-aa3a6d85ddd5 | -8.848 | -47.95748 | 2024-10-12 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64d66433-aeef-3ec3-a0ba-e561cf4ff546 | -8.73483 | -47.18156 | 2024-10-12 04:06:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a04fd4b-7ccd-3280-9f5d-2f6dc8e89578 | -8.73418 | -47.18536 | 2024-10-12 04:06:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2911bc68-c12b-30b3-b202-9dbc1587e2a6 | -8.67512 | -47.21241 | 2024-10-12 04:06:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 270cc004-db11-39ed-91d1-69540ec833d2 | -7.93185 | -47.97799 | 2024-10-12 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 997a87b3-76be-3cb9-8bc9-0c5cc5fc5438 | -7.93112 | -47.98213 | 2024-10-12 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29327e23-8e90-3ae5-9d5a-c8df84ef471d | -4.11121 | -48.24825 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aafcc886-f4f2-31df-a222-8727ec2e0cfa | -9.74737 | -48.30227 | 2024-10-12 04:06:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76c224a4-eae7-33c5-8779-ecb4b93523d7 | -9.74316 | -48.30108 | 2024-10-12 04:06:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7748c08-f6e6-30c9-a96c-a3fcbe5fd51b | -9.53283 | -47.81424 | 2024-10-12 04:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d3357af-0d0e-317d-8e5c-f32f3644fef8 | -9.53217 | -47.81801 | 2024-10-12 04:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e2bfbfd-4056-3130-a665-84522d86ef3e | -10.10073 | -47.69421 | 2024-10-12 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 177ec784-30c4-3bc8-adbe-8042b337c8cf | -10.10009 | -47.69791 | 2024-10-12 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea757944-1251-3113-a2b6-4d7078a24005 | -10.09663 | -47.69353 | 2024-10-12 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b050ef36-d5b5-383b-b841-bae1ecbc9165 | -10.09599 | -47.69724 | 2024-10-12 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d642680d-8753-3d6a-aefa-f47f4c68884e | -5.09121 | -47.929 | 2024-10-12 04:06:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ee42a43-f709-3c12-8bbf-6ecb1d1235ae | -5.09046 | -47.93358 | 2024-10-12 04:06:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94c0b19b-abf2-336a-b3da-ed6cad8dc806 | -5.07051 | -48.08292 | 2024-10-12 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 946aae14-428d-33e6-9fb6-88d3b32cfc06 | -4.69629 | -48.62531 | 2024-10-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a22bf756-cd65-3669-8263-9809180304da | -4.37874 | -48.61493 | 2024-10-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f092b575-6cd3-3a1b-b9a2-d6bc1fde92d3 | -4.37786 | -48.62016 | 2024-10-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b3b84b2-93c7-3ccb-90ee-d68ad89b6da4 | -4.28788 | -48.62943 | 2024-10-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README47.md)
