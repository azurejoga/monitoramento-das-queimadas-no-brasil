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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 083b67de-79f6-37bd-bc28-20ea719516fc | -21.57989 | -56.47596 | 2025-11-25 01:09:00 | TERRA_M-M | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 29150544-a756-387a-98f0-87f91dfa4b6d | -19.33016 | -54.34638 | 2025-11-25 01:09:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 95cb83ed-8cd6-30d5-bc78-4294aad85d75 | -21.70672 | -57.66293 | 2025-11-25 01:09:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bf9b860a-256e-352f-baf2-13607644ceaa | -18.57343 | -53.46037 | 2025-11-25 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6abe7a58-cc7c-3810-81b9-da6db663e8c2 | -18.11726 | -54.51959 | 2025-11-25 01:09:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2a26ccc2-fe8b-385a-9fc2-88dd93ba8aff | -17.24814 | -56.02166 | 2025-11-25 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 178c33c9-24df-3597-bf1c-04e37df6cb62 | -20.36012 | -57.9734 | 2025-11-25 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 7695d118-d6e0-33ee-9471-55ac7dbca0e4 | -19.33194 | -54.35797 | 2025-11-25 01:09:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 413c8f06-2d61-3d2a-ad52-35650ed33de9 | -20.36905 | -57.97202 | 2025-11-25 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 82a29caf-4729-3a84-99fa-0f8c5cf5fdef | -17.01502 | -56.57194 | 2025-11-25 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 50f3f2e6-5278-3489-b75e-7c46ba3fed9c | -16.15773 | -59.97128 | 2025-11-25 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 70b540d7-f0ba-303a-9383-83a08847f5e9 | -17.0136 | -56.56228 | 2025-11-25 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 2240d76a-ac67-3d99-a42d-b6b54260f10b | -12.23885 | -63.48211 | 2025-11-25 01:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9d1131d0-ecbc-3078-aa17-9284263e07bc | -4.8327 | -43.8191 | 2025-11-25 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5cacef7e-ec3e-391c-a362-54bff60181f4 | -2.5053 | -47.8337 | 2025-11-25 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| ac11df7a-141e-310e-b110-a95f15b783b5 | -4.814 | -43.8203 | 2025-11-25 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 704bdfd8-2c47-3762-b31d-f87f82e57aba | -2.4867 | -47.8342 | 2025-11-25 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 4077e76e-db0b-3b35-8370-64bf57a271dc | -6.6859 | -43.9339 | 2025-11-25 01:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 6b83f17a-bb37-313e-b7cb-bd82ae1fd31d | -2.4682 | -47.8347 | 2025-11-25 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| cdc99364-1592-3302-b795-4fee7b0d23aa | -2.9294 | -48.2319 | 2025-11-25 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 6d63e5bd-e716-32ff-9a81-fe84d26f2f55 | -2.4868 | -47.8126 | 2025-11-25 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| fa2a5933-fd46-3383-8f70-c64dfc6d58c0 | -3.2134 | -46.8283 | 2025-11-25 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 64518762-93f5-30d7-a9d5-18e05cc90414 | -6.6857 | -43.9571 | 2025-11-25 01:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1324aa5b-37f0-3809-987e-18324ff80c99 | -3.1948 | -46.829 | 2025-11-25 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 19719a55-d4c9-3279-9f8a-1b524ac21195 | -6.59856 | -35.24491 | 2025-11-25 02:57:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| be09b7ff-7f30-3018-a471-db1f8e241e10 | -6.60075 | -35.24399 | 2025-11-25 02:57:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e75bb18b-1267-3476-916d-f1817aa4c330 | -9.34966 | -35.54646 | 2025-11-25 02:57:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a800b3a0-71fd-3e9f-9c97-976f89f03cd2 | -9.35048 | -35.54223 | 2025-11-25 02:57:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 43783fcc-197d-3751-abc7-674f7a2947d7 | -9.49996 | -36.10676 | 2025-11-25 02:57:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| c538f0b0-7f6f-35a2-a4c0-8ee87a334100 | -6.60154 | -35.23973 | 2025-11-25 02:57:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e822ce44-d057-340b-9451-9618fa853d22 | -9.50084 | -36.10219 | 2025-11-25 02:57:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| a07d9d77-ff15-3a8b-a452-635ef775fec4 | -6.59932 | -35.24062 | 2025-11-25 02:57:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 72672f18-3f61-3b7c-9e67-06061b5fee9d | -8.051 | -43.1237 | 2025-11-25 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 274.4 |
| 1ce1cf62-61e1-3151-8fda-9502f0dc8ad0 | -2.4867 | -47.8342 | 2025-11-25 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| b42226fa-2a9f-3c44-a348-4f459db302b2 | -6.6859 | -43.9339 | 2025-11-25 03:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a56f88a3-a8a7-32f1-9c7a-bf57ccc2dc80 | -8.07 | -43.1216 | 2025-11-25 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 147.2 |
| a6a1f6e9-ad80-3166-a776-26b6b35b1e70 | -4.8327 | -43.8191 | 2025-11-25 03:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c8ec9111-23e6-3e64-bc9a-9487260d5789 | -8.0507 | -43.1472 | 2025-11-25 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 240.7 |
| ed57f8f8-0980-3550-8d22-53874c82cf73 | -1.9704 | -54.7094 | 2025-11-25 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 5e7f7583-aef6-3f23-b7ea-1a86dd8dc8ee | -6.6857 | -43.9571 | 2025-11-25 03:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| bb12b20f-470f-3197-92c8-68c12faceb37 | -8.0696 | -43.1452 | 2025-11-25 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 140.6 |
| 8443930b-774c-34b4-a050-3274e6d7396e | -12.77733 | -38.50254 | 2025-11-25 03:00:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d1899d01-b411-3f00-94d8-b970d7e6df89 | -8.0696 | -43.1452 | 2025-11-25 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 31325eb4-04db-3a68-a554-9b7b2c163244 | -8.0507 | -43.1472 | 2025-11-25 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 168.2 |
| 571deb06-9dec-34ad-84fa-05022333ab01 | -2.4669 | -48.2238 | 2025-11-25 03:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 28a635d5-47c5-385e-bc56-d1922755e398 | -8.051 | -43.1237 | 2025-11-25 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 178.1 |
| d4667f2b-79a4-3e97-b5df-bf1a064758f6 | -6.6859 | -43.9339 | 2025-11-25 03:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 5073a8e3-46a2-3c28-9489-2d9c8591516e | -8.07 | -43.1216 | 2025-11-25 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 3bf43000-2a8b-3fd6-ac16-3cf8a4535e19 | -5.35119 | -44.88658 | 2025-11-25 03:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b308fdd-058b-3009-8152-87a259f53f95 | -7.56891 | -45.86973 | 2025-11-25 03:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b14ed60f-52b5-399d-8410-283a116518ae | -7.45644 | -45.19376 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5484ce28-bbe7-35b5-977f-0c22aae8f9e8 | -6.68058 | -42.47497 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5a5f92cc-ef1b-30a7-9e76-bcb5f21bd9c3 | -6.68332 | -42.48407 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1a369655-f983-3f2d-8cad-2e9046e0e9db | -8.04818 | -43.14519 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9c7ebc69-e677-3d82-bf93-6c9b7c29f91a | -5.5886 | -45.17605 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74e29ee6-6348-3e44-8830-4a62632b3991 | -6.00317 | -44.72077 | 2025-11-25 03:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9aec3f80-109c-3e85-8e53-b29acf182555 | -8.05886 | -43.13437 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 1a6eaa80-4aba-36c1-9cf4-1a2a5fce7d4e | -5.31284 | -40.8747 | 2025-11-25 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74bff89e-610d-3174-8745-c915faba68c6 | -7.53559 | -46.56734 | 2025-11-25 03:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08fbcef0-edd9-3ee2-b0bc-c6db4d1abd13 | -6.00268 | -41.91879 | 2025-11-25 03:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5ffa6e6c-8b9e-3a60-bc17-8f49531364c1 | -5.42543 | -38.79757 | 2025-11-25 03:46:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0dd70f5f-284b-3016-9349-c4427100a9e4 | -6.00678 | -41.91945 | 2025-11-25 03:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4fdf44e6-9ac3-3e45-932f-943a2af2ec55 | -4.81891 | -43.82493 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9f1c4f0a-6e6e-3cad-8fba-6ea96053f222 | -6.89128 | -42.8454 | 2025-11-25 03:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 38cf166c-11cf-3133-bcbd-a23cea13c712 | -7.46244 | -45.18886 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 11216bb4-46f8-37c6-a765-2bfe574c3be3 | -5.04133 | -44.80178 | 2025-11-25 03:46:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3375dda-df10-308d-8734-f1286b8809fa | -6.86684 | -39.1127 | 2025-11-25 03:46:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d1b51e6-590e-3e7c-acac-4bac78977783 | -6.46299 | -43.55966 | 2025-11-25 03:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ea6fe8c-baa7-3b85-a2e8-8b858bacfaf1 | -8.05675 | -43.14677 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2e527786-d512-3244-8292-2f4fd933ca86 | -8.05317 | -43.14184 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 541d5644-cb18-34e2-a05f-b93741f42577 | -4.83251 | -43.82501 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c08cf81e-d581-37e5-8db7-61b3dbb5141c | -6.67987 | -42.47522 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 397ce1d5-d204-3d89-9715-51bc3fc19ed2 | -7.22748 | -42.19138 | 2025-11-25 03:46:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cfbc6b40-4ead-306c-88a4-ef004a955c4b | -5.58807 | -45.17911 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c8a98c8-6482-3fb3-9eb1-0c7fa256a0f7 | -4.35491 | -44.32738 | 2025-11-25 03:46:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66e7f064-1898-3549-96ae-80d652d7dc51 | -4.81716 | -43.83511 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c40f458e-ac2a-37de-8e80-b5e8167ec013 | -5.03768 | -43.26162 | 2025-11-25 03:46:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7b376ee4-cd4e-3f47-857b-46ff6624436a | -6.68879 | -43.94809 | 2025-11-25 03:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 2d5c1db6-93cd-3668-b662-e74295bd8a1e | -5.56783 | -44.97527 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e11eb20-a9f4-3e0e-99fa-b987ad15a1b2 | -8.06173 | -43.14343 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e636fd3f-e11f-3e70-84be-11e083907916 | -6.24307 | -40.29906 | 2025-11-25 03:46:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ecbd22d5-083a-343b-8a05-791a46ec305c | -7.46346 | -45.18306 | 2025-11-25 03:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 200952bc-3dcc-397e-9e29-60ecc4e3f70a | -6.6792 | -42.48295 | 2025-11-25 03:46:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5ec1ebf2-0fbd-3884-9c67-056c3db29dbf | -5.90488 | -44.00938 | 2025-11-25 03:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f831fb11-e51f-3621-b6f4-0ba5f5c7c88a | -5.95798 | -43.92538 | 2025-11-25 03:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 014e8c51-53df-3d76-8c22-4131bbc8148b | -6.70495 | -39.66716 | 2025-11-25 03:46:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 91144f2f-0bab-33e2-81c0-4798d0cacdc9 | -8.16682 | -43.18981 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9b1a3bfb-f73c-3d21-b08c-0dc452407180 | -4.82692 | -43.82939 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38e68e64-2bb1-36cb-aa9e-f95a9eb76542 | -6.00471 | -44.17166 | 2025-11-25 03:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1468e2a-cc29-37f3-8d65-5d331d0aff4a | -7.53495 | -46.57088 | 2025-11-25 03:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c086040f-b589-36b6-8b97-fe8a14240340 | -4.59554 | -44.88194 | 2025-11-25 03:46:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ec4fc61-aec2-3bda-9d51-0e8a467813f0 | -6.57074 | -37.278 | 2025-11-25 03:46:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f632056c-363e-3c35-8489-878190d1ba0f | -4.81741 | -43.82787 | 2025-11-25 03:46:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 318080c2-008f-3874-b2e3-68e309ef6769 | -4.94264 | -41.15954 | 2025-11-25 03:46:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c87f4910-9053-32c0-bebc-58d894e41679 | -5.58753 | -45.18221 | 2025-11-25 03:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffdce760-392c-3f4c-b4eb-fd39aa9cdc52 | -5.12914 | -43.0266 | 2025-11-25 03:46:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 058fe40d-20f6-3089-b0fb-6a038a6f8f78 | -6.69043 | -43.93856 | 2025-11-25 03:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4cd1cc0f-a9b5-3c5a-ab36-de048e9904d8 | -8.05816 | -43.13849 | 2025-11-25 03:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| ac18f65d-3c0d-3968-af9b-21661e5a2144 | -6.9826 | -39.29226 | 2025-11-25 03:46:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a48e42a8-5f4d-3295-8761-d1bb59f0ba69 | -4.60066 | -44.88281 | 2025-11-25 03:46:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README2.md)
