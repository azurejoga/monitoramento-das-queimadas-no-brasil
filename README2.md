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
| 79827a8e-099a-3ea0-82c6-414bc6c692eb | -7.0695 | -44.9335 | 2025-05-20 01:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| edb2e9cb-acd8-3d72-b8c8-e90f69e38ae2 | -20.9601 | -56.5967 | 2025-05-20 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 4bec9b8e-3cb8-3836-834a-8d43b2dc39fd | -20.9393 | -56.621 | 2025-05-20 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 53.5 |
| b711905a-dd01-313e-a5c4-c202158c2daf | -5.9748 | -43.7613 | 2025-05-20 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a334f5d6-18ab-33c8-8ac0-d77d6c0167db | -12.4433 | -43.7242 | 2025-05-20 01:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| a70654dd-feab-3c09-810c-ebeeded3ef73 | -12.424 | -43.7274 | 2025-05-20 01:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 93af8a30-e2e8-362c-a0a2-40f6b09cf899 | -12.2946 | -52.4785 | 2025-05-20 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 7a81e35d-c6be-39c6-8096-9aab375f631d | -20.9398 | -56.5998 | 2025-05-20 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 1ec5b994-c729-3626-8eaa-ac61afef9bfe | -20.9597 | -56.6179 | 2025-05-20 01:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 8342665c-21e4-30bb-b27e-3a1652b439a5 | -14.0297 | -55.136902 | 2025-05-20 01:08:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10f3223c-4035-3f82-b065-8b6327878765 | -14.0369 | -55.124401 | 2025-05-20 01:08:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d7db4da-65b5-3f53-99ba-02d681e1f5cf | -12.2708 | -57.262402 | 2025-05-20 01:08:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a09b76b-2db3-3409-abea-be311a8a785a | -17.498899 | -46.749298 | 2025-05-20 01:08:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4a3bbc1f-d9f9-3af1-939f-188310021faf | -12.4703 | -57.1884 | 2025-05-20 01:08:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43a9245f-ebdb-31e9-9b53-f33cd961032b | -12.2818 | -52.459702 | 2025-05-20 01:08:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5a6c932-18f6-3730-ad35-beeb4a09fb06 | -21.2423 | -49.265301 | 2025-05-20 01:08:00 | METOP-B | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af3b797a-b8fd-31a0-a147-e2cca06ead77 | -12.4684 | -57.180199 | 2025-05-20 01:08:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fef50071-93e6-33a3-87ab-588759f9cb40 | -20.9557 | -56.5914 | 2025-05-20 01:08:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6726d740-45e8-3524-8497-f6c7483d1f4e | -12.2825 | -57.268101 | 2025-05-20 01:08:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8e76578-ac71-3e88-8326-c8dada2248fd | -12.2915 | -52.457199 | 2025-05-20 01:08:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98082f14-ea41-384b-8fd8-d57da13f2751 | -20.9592 | -56.606602 | 2025-05-20 01:08:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4b36021b-1fd8-38dd-a331-fdd29c7b1b29 | -14.0272 | -55.1269 | 2025-05-20 01:08:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dccbc63a-813c-312b-9f16-c8406f72d052 | -14.0345 | -55.1143 | 2025-05-20 01:08:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f3f6b2c-7c42-3e45-ae6d-c3603547656e | -11.0766 | -54.763699 | 2025-05-20 01:08:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37aff34a-ab32-314a-885d-f810c3e4e7aa | -14.0248 | -55.116798 | 2025-05-20 01:08:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94aa6ece-4c22-39d0-8c1a-59322708a5d7 | -20.9575 | -56.598999 | 2025-05-20 01:08:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 109a8085-523f-3cca-94ff-90375f08001f | -12.2954 | -52.4729 | 2025-05-20 01:08:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1815048-a028-32b8-ab98-c77358a32dd4 | -11.3595 | -55.121399 | 2025-05-20 01:08:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c61038c4-b512-35df-9143-8cb49ebfee6f | -14.0199 | -55.139301 | 2025-05-20 01:08:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23784ad6-d914-3abb-8dbc-a69791bf4de0 | -12.1253 | -54.6586 | 2025-05-20 01:08:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0db59754-7f12-3e32-a1c4-34f1d53bcb0e | -19.1472 | -47.7939 | 2025-05-20 01:08:00 | METOP-B | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c33ef2e2-47a7-35b7-8c8a-b78edab56eb4 | -12.2806 | -57.259998 | 2025-05-20 01:08:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b073b686-acfd-392d-a440-189ab122eb89 | -17.490101 | -46.718899 | 2025-05-20 01:08:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1af2d5d1-8309-3f9d-9eca-5c81cdf07da5 | -20.945999 | -56.593899 | 2025-05-20 01:08:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f0401ef3-ca82-31da-85dc-6ce394d30971 | -12.2857 | -52.475399 | 2025-05-20 01:08:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a88c61fb-3f5f-3547-aa3b-74cfb527ea47 | -11.0794 | -54.775299 | 2025-05-20 01:08:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8413236-f28b-3162-86ac-095cd35885b4 | -9.9299 | -59.923 | 2025-05-20 01:08:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91fc078b-8646-3c03-80a4-5d2592643213 | -19.153999 | -47.8181 | 2025-05-20 01:08:00 | METOP-B | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f8a1351e-15f1-3256-9363-edf91381879e | -13.0401 | -53.713001 | 2025-05-20 01:08:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d90d15c3-a44e-3f43-be97-4d0fb6118065 | -14.0174 | -55.129299 | 2025-05-20 01:08:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c67b125-4d20-30e7-a353-9ffdc9c5db52 | -20.947701 | -56.601501 | 2025-05-20 01:08:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e6b06024-1296-3eb9-a710-8ca1f1bc8ad4 | -20.949499 | -56.6091 | 2025-05-20 01:08:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a35a19d3-da1e-3fc5-ba55-4bdf5ebe422b | -10.8152 | -56.9547 | 2025-05-20 01:08:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36f7044f-4638-3edd-9675-134f7f962805 | -20.9393 | -56.621 | 2025-05-20 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 46de438c-08e4-394c-9e96-4f798c1356b7 | -20.9398 | -56.5998 | 2025-05-20 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 59489c90-a55a-3ca2-8bb1-e86eca62f82c | -20.9601 | -56.5967 | 2025-05-20 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 8757187d-0581-3d6a-972a-050458507124 | -20.9597 | -56.6179 | 2025-05-20 01:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9266cae7-5281-3225-b6e4-22ee89f814a6 | -12.4433 | -43.7242 | 2025-05-20 01:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 19624efb-b967-3079-a295-e754e28f08b6 | -12.2946 | -52.4785 | 2025-05-20 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d3b03ef9-34e9-3b16-8d1f-4395ac4e5ac7 | -12.424 | -43.7274 | 2025-05-20 01:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 10303f0e-ff89-3f6b-bdd1-7ac4b94c7095 | -14.0328 | -55.13 | 2025-05-20 01:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| b186e42d-4272-3c68-bdcc-d975668d0e9b | -5.9748 | -43.7613 | 2025-05-20 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 2ce08fc9-ab07-325f-ad9f-9c623baa8026 | -12.2946 | -52.4785 | 2025-05-20 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 847fd6cd-5470-34d1-9b28-26ce8935adfe | -20.9597 | -56.6179 | 2025-05-20 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 5e593f39-e958-3e66-b9d3-03051fce21c5 | -12.424 | -43.7274 | 2025-05-20 01:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 2f105b60-d001-3f9e-b896-2e304ddaafed | -20.9601 | -56.5967 | 2025-05-20 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 8dfb2a31-272c-3998-ae87-2f4d223bb340 | -12.4433 | -43.7242 | 2025-05-20 01:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| f879f534-e014-3e4e-b5fb-5124c14df966 | -19.166 | -47.8122 | 2025-05-20 01:30:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 39c76119-03d8-39a5-a71c-b88d4f74ef30 | -20.9597 | -56.6179 | 2025-05-20 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 040b9d3a-8466-3e04-9768-7607e9d7d703 | -20.9601 | -56.5967 | 2025-05-20 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 718bd47d-b809-32d5-85af-9b505412082f | -20.9398 | -56.5998 | 2025-05-20 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 00b9be7d-3211-311b-b515-6fdb6a957fe2 | -12.424 | -43.7274 | 2025-05-20 01:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7b7996da-bbb2-340a-b702-1731a939f734 | -12.2946 | -52.4785 | 2025-05-20 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 37d3d50d-f42f-3ea7-bf24-18212fb951bb | -12.4433 | -43.7242 | 2025-05-20 01:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 590a9738-ceed-3d26-b184-d957cf2eb7ff | -20.95007 | -56.59974 | 2025-05-20 01:32:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 14b98966-29a2-3b40-ab0d-209dd0bebb02 | -20.95807 | -56.61451 | 2025-05-20 01:32:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 22eeafda-df91-325f-ab13-4532e78a15e7 | -20.95641 | -56.60379 | 2025-05-20 01:32:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 5530a139-8fb4-3046-a966-c177b669efda | -23.31828 | -55.4457 | 2025-05-20 01:32:00 | TERRA_M-M | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 7ee376e6-3dba-38de-8674-7473d76fdef2 | -20.95168 | -56.61046 | 2025-05-20 01:32:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 442d4952-ee0a-351f-9031-b1fdf0d4af3f | -14.03347 | -55.138 | 2025-05-20 01:34:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 3c3af969-827e-39dc-a22f-4219b827c3c1 | -12.29892 | -52.47527 | 2025-05-20 01:34:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ab6b96cc-d53c-32a0-bbbb-5e4832191215 | -12.27644 | -57.26289 | 2025-05-20 01:34:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 9cb963f0-10db-3ccc-b2ce-37e1b79b07c9 | -12.46883 | -57.18792 | 2025-05-20 01:34:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 60c8dc87-adb5-3f64-b891-080534ca0d03 | -9.41387 | -58.33114 | 2025-05-20 01:34:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 52b3edc6-93d4-36f7-b9e1-a3295ebcd843 | -14.03081 | -55.12159 | 2025-05-20 01:34:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| e8098026-3990-3276-a64e-4edf3bf35511 | -14.02192 | -55.14002 | 2025-05-20 01:34:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| badb9627-a7d4-3052-8a39-ae102e211dd4 | -12.28421 | -52.47792 | 2025-05-20 01:34:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b6ea2032-0f2c-3282-9a5f-7de52cd3cf13 | -11.07708 | -54.77439 | 2025-05-20 01:34:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b827a2e3-8c83-3e26-b007-f834e197cbea | -13.04769 | -53.71419 | 2025-05-20 01:34:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4b1d09f2-bdd4-39ac-851d-320468396909 | -12.27826 | -57.27503 | 2025-05-20 01:34:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 6ef93d86-5a54-3fe5-b6d5-f8b8ab833d43 | -12.12455 | -54.65819 | 2025-05-20 01:34:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1fe1c1eb-76c9-35a2-b717-ffc3d228c50f | -10.81632 | -56.96388 | 2025-05-20 01:34:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 68d4401b-7557-36a4-9a6e-734408e7a884 | -20.9597 | -56.6179 | 2025-05-20 01:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 567408e7-bd27-3150-8038-630b443caf73 | -12.4433 | -43.7242 | 2025-05-20 01:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d5af7ad1-0dcb-32a6-b576-8c2519ae5021 | -12.2946 | -52.4785 | 2025-05-20 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 15e8f6e0-1ba8-3085-b20a-ecedea4c4a5b | -20.9398 | -56.5998 | 2025-05-20 01:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 49.4 |
| d22d6022-af96-3cfd-9c9c-d034510f57b5 | -19.166 | -47.8122 | 2025-05-20 01:40:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 74d03f8c-9065-3737-81f7-aef7b390dd50 | -20.9601 | -56.5967 | 2025-05-20 01:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 921fd032-d1c3-3092-8011-c7f6a7db99a5 | -12.424 | -43.7274 | 2025-05-20 01:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b50ff14b-61c1-3029-bf3d-4dfa06f3f1c5 | -19.166 | -47.8122 | 2025-05-20 01:50:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 587d9a66-127c-3522-965f-64ce1c090e8d | -12.2946 | -52.4785 | 2025-05-20 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 735992af-4f4b-32b7-9178-9f6a67ccbde4 | -20.9597 | -56.6179 | 2025-05-20 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 46a75ed9-594b-3203-810f-3c746951538c | -5.9748 | -43.7613 | 2025-05-20 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 0cd45801-6892-3eaf-bd0f-131836a82787 | -20.9601 | -56.5967 | 2025-05-20 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 107.7 |
| e1190402-15d7-398b-a5bf-a7f82de1bf9c | -12.4433 | -43.7242 | 2025-05-20 01:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| a55b345b-c546-32f3-9637-83f71d6f89f5 | -12.424 | -43.7274 | 2025-05-20 01:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 19b3896a-4d83-3b64-9649-b202a1fe1690 | -20.9601 | -56.5967 | 2025-05-20 02:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 106.4 |
| c73af550-d421-3bdb-8f68-9cb561a069a7 | -12.2946 | -52.4785 | 2025-05-20 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 328281de-1231-3076-a847-6d3679f079e6 | -20.9597 | -56.6179 | 2025-05-20 02:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 53d907b0-1620-3aa2-8910-051d1c08a616 | -20.951401 | -56.596298 | 2025-05-20 02:00:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
