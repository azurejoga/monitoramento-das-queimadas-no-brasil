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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7073ac7f-8ef9-3cf9-af56-295b588800a9 | -18.94556 | -41.0075 | 2026-10-02 03:21:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 011a50a0-7c4a-3f5f-a517-c6265ee14838 | -18.94491 | -41.01065 | 2026-10-02 03:21:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ceb5e619-e5b6-3009-96a9-e8534c6f3739 | -11.6579 | -43.5899 | 2026-10-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 433.4 |
| b355e16a-568f-3477-865f-3eb2e530033a | -11.6771 | -43.587 | 2026-10-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| bd7cc9f6-cd9a-36e5-85a7-c3fc0de2641c | -3.1655 | -54.0844 | 2026-10-02 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 44f8c3fa-5ca7-3940-a804-17df376c3780 | -13.154 | -51.2145 | 2026-10-02 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 5fafa476-aa73-3e60-9a5a-22f0e6dc01c0 | -3.1299 | -53.7633 | 2026-10-02 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 1b76be8e-1379-387e-9123-e7cca6363784 | -6.914 | -43.6816 | 2026-10-02 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 1f201fba-4d09-372a-84e4-0ba5d61ccc6f | -7.4188 | -55.5902 | 2026-10-02 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 3c14824e-b15b-3e96-b9e4-d40edb409fd0 | -3.2767 | -53.84 | 2026-10-02 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| fbf399ff-70d8-3645-b30c-332ce7ad0b5a | -7.4031 | -55.2114 | 2026-10-02 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| f9461d52-b638-31bc-baa8-38f14f5c235c | -3.1483 | -53.7426 | 2026-10-02 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 4ffe77db-02c0-35e3-aa85-e08b47677631 | -11.7545 | -43.5512 | 2026-10-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a6e57ea9-902d-39c9-b647-dfb1423ae303 | -13.1348 | -51.2169 | 2026-10-02 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 59c35bd3-80f5-3c5c-ba6f-4e1c0212125c | -13.1351 | -51.1955 | 2026-10-02 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 29165e80-322b-3c1b-bec1-7ea097683fe4 | -3.1299 | -53.7431 | 2026-10-02 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 430608be-2736-3f2a-a0b6-def70fc4a813 | -5.7563 | -45.152 | 2026-10-02 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ee0b828e-7984-3c7b-becf-3caab798899f | -11.7541 | -43.5749 | 2026-10-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 38bd3a3d-7b9a-357c-9af2-c813dbe80493 | -11.1615 | -44.6002 | 2026-10-02 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |
| d36b1ee1-408a-3d24-8f0d-6e30ffe9524f | -4.2676 | -50.7506 | 2026-10-02 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 2281ab14-beff-3401-9191-106f28eef5c4 | -2.0576 | -56.8786 | 2026-10-02 03:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 6e2a2020-76eb-3ed0-b6bd-522a37c19d4e | -11.6767 | -43.6106 | 2026-10-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.2 |
| adfed73c-3efa-3232-8440-a3e316d16bd1 | -5.7355 | -43.2916 | 2026-10-02 03:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 04590eb7-dbc9-3dcc-b595-52b40dbb137a | -7.4186 | -55.6101 | 2026-10-02 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6ef2e437-0e1b-36be-9f67-52bf340368eb | -12.9803 | -51.3 | 2026-10-02 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 04c0081f-c0a9-3c68-a57c-30852ab44192 | -12.9995 | -51.2976 | 2026-10-02 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.5 |
| b0bacc1e-4e73-3aae-9741-5583378ce53a | -4.4506 | -47.9329 | 2026-10-02 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7ae668dd-bbd2-312f-885f-3a6f7ec91408 | -11.7348 | -43.578 | 2026-10-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| f02f9ddc-8e3e-328b-b221-9b966151de2e | -6.3952 | -56.4158 | 2026-10-02 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2399403c-94b4-30b8-9647-4e34cd4ba751 | -11.7353 | -43.5542 | 2026-10-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 4c1fe9b3-cc4c-3b81-81d8-e5d64edc2b8b | -7.3846 | -55.2124 | 2026-10-02 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3be1ae28-ce0f-3520-9722-df42954adcf7 | -11.7733 | -43.5719 | 2026-10-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 6ec2ff1a-0d68-398e-ae0e-8505f606ae13 | -2.0577 | -56.8591 | 2026-10-02 03:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4bb71464-6a20-3823-9946-9554e2806499 | -11.7537 | -43.5987 | 2026-10-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 72979df5-5c69-3394-89b5-45d17d57523b | -3.295 | -53.8597 | 2026-10-02 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 32706e32-cdde-31d4-961f-457dcfbd576e | -11.142 | -44.6261 | 2026-10-02 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| f3864c44-06d9-31ff-ac42-7c5df284e651 | -6.858 | -59.2636 | 2026-10-02 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 526ca4e8-62c0-3b62-b39c-7d5142390091 | -3.1839 | -54.0839 | 2026-10-02 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| dc608c46-94fe-3034-9d3f-5a7ce6c92a14 | -12.9807 | -51.2786 | 2026-10-02 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 62a4e642-2ae5-3e4a-ba02-6444a151201b | -3.2951 | -53.8395 | 2026-10-02 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| b3134eef-3591-31f6-8bfd-e0c928883b6f | -11.1424 | -44.6029 | 2026-10-02 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 96f4d62f-c4c3-3973-8f9b-50623e28ea5b | -11.6575 | -43.6136 | 2026-10-02 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 454.5 |
| 80e91272-8584-3c45-8c85-0640b9caf28f | -3.0008 | -53.8874 | 2026-10-02 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 8e13c158-1723-3336-9d30-66fde40c9482 | -3.1838 | -54.104 | 2026-10-02 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c843c445-7eee-389b-aadb-96bc17905188 | -7.7364 | -49.2082 | 2026-10-02 03:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 1fdc5357-b6f7-381f-bdeb-d95afca7c242 | -4.4507 | -47.9112 | 2026-10-02 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6d9c05ba-471a-3c07-89f2-9f680d772ac1 | -13.0187 | -51.2953 | 2026-10-02 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f6baee89-1885-3d2a-9560-77d5ad109c80 | -12.9998 | -51.2763 | 2026-10-02 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 2c1beba4-a9a9-3814-8719-e6659a1d126b | -11.1611 | -44.6234 | 2026-10-02 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 32cd799d-70b0-36b4-81c7-d9ecf32ee249 | -4.2676 | -50.7506 | 2026-10-02 03:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 22ce48d9-2247-3f3d-ae12-1e083cec177f | -3.1655 | -54.0844 | 2026-10-02 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 453b3288-4a20-34e2-bd52-832697f500fa | -3.2951 | -53.8395 | 2026-10-02 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| b7c4ebf1-0ff5-3a6c-bd3a-9ecea2b60024 | -6.914 | -43.6816 | 2026-10-02 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 8b47f5b8-1f22-34b2-9f0a-9037381fa9d1 | -11.6767 | -43.6106 | 2026-10-02 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 7c3bf28a-3898-312e-b1ff-6a4de0d788a1 | -2.0576 | -56.8786 | 2026-10-02 03:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| ee31da82-bcbf-3962-8bf6-e34d8ddcf02a | -11.1611 | -44.6234 | 2026-10-02 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| e657daee-7b30-3c14-a9bd-c9af86408b04 | -12.825 | -51.4466 | 2026-10-02 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 7659735c-412f-30b4-8008-dc2638635e42 | -7.4188 | -55.5902 | 2026-10-02 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 2b16c9c0-77ed-367d-8c81-b83571df13be | -7.4031 | -55.2114 | 2026-10-02 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 81bde4e3-1908-3071-b112-10c325718297 | -4.4506 | -47.9329 | 2026-10-02 03:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| db54cf89-2517-3bd1-a6a5-41b837329ca6 | -11.7733 | -43.5719 | 2026-10-02 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| b549f334-5522-344b-8cb5-dd07fbd9eaed | -12.9995 | -51.2976 | 2026-10-02 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d177e335-bde5-34dd-aba7-74db8c00feae | -12.8439 | -51.4656 | 2026-10-02 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c0f114ad-1acb-368a-bdd3-b9222268d1b8 | -11.7541 | -43.5749 | 2026-10-02 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.8 |
| a518340e-87ad-336d-973b-d7ef429aff14 | -11.142 | -44.6261 | 2026-10-02 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| a1608ba8-3a07-3fe9-8904-026e1b415290 | -11.1424 | -44.6029 | 2026-10-02 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| a5e085c7-5758-3e9c-8685-8c33796cf73a | -3.1299 | -53.7431 | 2026-10-02 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| b04dcf44-b695-3c70-a3d1-a24f6405a71f | -3.2767 | -53.84 | 2026-10-02 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 0bd81393-7ec2-3846-8a5e-0eac653938a4 | -2.0577 | -56.8591 | 2026-10-02 03:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 90988087-b0d7-3a82-9c85-0186ba9d1832 | -11.7348 | -43.578 | 2026-10-02 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.6 |
| dd92d429-56fc-3116-971b-8c369e7760c9 | -11.1615 | -44.6002 | 2026-10-02 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 7e1b33e7-a961-32e0-8d65-2c6ad1e2580e | -11.6579 | -43.5899 | 2026-10-02 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 421.8 |
| 28347bdb-d682-311d-9934-7c5b2b56e99e | -3.295 | -53.8597 | 2026-10-02 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 4d8e8351-3868-32ff-aa81-86345e824c93 | -11.7537 | -43.5987 | 2026-10-02 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 27abf0b3-83bb-3e6c-9fed-28efaf3b944d | -7.3846 | -55.2124 | 2026-10-02 03:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8d271583-5948-34a7-9a77-ac2b36065433 | -12.8254 | -51.4253 | 2026-10-02 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 48cf29fc-ee0e-31e6-88db-5fbf754a127a | -3.1838 | -54.104 | 2026-10-02 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 057d0574-79e7-3613-8e3a-36d99753572e | -12.9998 | -51.2763 | 2026-10-02 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f2ab53b1-cf2c-311e-aeb5-c6eb02b75ac2 | -5.7563 | -45.152 | 2026-10-02 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| d4438c93-c3f2-3080-95af-5a27c58e18a7 | -11.6575 | -43.6136 | 2026-10-02 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 520.9 |
| 9706c598-56bb-39cc-826f-7bdb2c8d0bf6 | -5.7355 | -43.2916 | 2026-10-02 03:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 88dd93cc-2445-324b-b6d7-88044855ccfe | -6.3952 | -56.4158 | 2026-10-02 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 40f1e9f7-d92f-3741-af27-86044d4c9112 | -12.8247 | -51.4679 | 2026-10-02 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 8f5419f9-81fd-3780-b791-59f97aefba16 | -11.6771 | -43.587 | 2026-10-02 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 5a00af80-aa21-33f5-8ed3-5477fcef4e1b | -3.1299 | -53.7633 | 2026-10-02 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| e654b118-b32b-3416-b6f8-1c2a2670b5aa | -11.1611 | -44.6234 | 2026-10-02 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 410.3 |
| 6f8cc85c-21c5-3904-8dc0-3e7e45757fb3 | -7.3846 | -55.2124 | 2026-10-02 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 913f39fb-ecbd-3b24-93a5-cf4bbf4a88b9 | -11.6771 | -43.587 | 2026-10-02 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| aa6db4c1-1f88-37f8-91cb-05fbe1079f9e | -2.0576 | -56.8786 | 2026-10-02 03:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| c343cdea-b4b8-3f86-a4fa-8b9373021dce | -6.914 | -43.6816 | 2026-10-02 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b1637038-3c27-3bb9-bf22-d8adb4293e34 | -11.6579 | -43.5899 | 2026-10-02 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 297.5 |
| 215ed246-6502-32cd-9b67-51b65ee5dbfe | -7.4031 | -55.2114 | 2026-10-02 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 1fd5b9c2-b8cc-3d5a-b29e-ba07126f2332 | -5.7563 | -45.152 | 2026-10-02 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c6e742f8-b781-3117-8161-f637c11cd25f | -11.7733 | -43.5719 | 2026-10-02 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 2478cc2b-cb02-3c80-8541-5ffb202fe33b | -4.4507 | -47.9112 | 2026-10-02 03:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| bb9b6e91-242c-397c-aedb-e93abfbeb0f9 | -2.0393 | -56.8789 | 2026-10-02 03:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 94821ed8-1750-3b17-91e1-0f2c304f40c0 | -11.6575 | -43.6136 | 2026-10-02 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 373.1 |
| dfb365f0-4e75-356f-a795-b6ac6709b73d | -11.7348 | -43.578 | 2026-10-02 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| accea3a1-5a9c-365e-b36f-2d1cc94fee0d | -3.1655 | -54.0844 | 2026-10-02 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 4aa4cc8e-7aff-3d69-803f-333f37c73782 | -7.4188 | -55.5902 | 2026-10-02 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |


[Clique aqui para ver as próximas entradas](README26.md)
