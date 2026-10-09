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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfaff991-266e-35d4-8758-905ff5a0e2e0 | -9.4637 | -44.6063 | 2026-10-09 00:06:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b4b0044a-0db4-339f-b8e2-a51ad804d18a | -10.7437 | -46.608799 | 2026-10-09 00:06:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b46275b-24d6-376d-8391-06e1639686ff | -8.264 | -46.908699 | 2026-10-09 00:06:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee8e8149-c32c-3b3a-a0b2-ab3424a2fcb3 | -8.5206 | -46.903099 | 2026-10-09 00:06:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3507a2fd-980d-3766-b42b-a95484650df9 | -2.9794 | -54.111801 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c978cd73-7a8d-3ec0-a039-55e42a6e9599 | -8.9749 | -45.917801 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c72b7073-ee7c-3c81-89e7-2f4fe63f6f7f | -8.4944 | -54.620201 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a02faa1-98f3-3b59-8d38-d6a8079ca455 | -8.9945 | -45.9132 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8129c952-8be7-3409-868c-27d61e0c0ae2 | -5.7459 | -43.846802 | 2026-10-09 00:06:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96a5f201-797d-386a-9c73-ac2247bb09a1 | -6.0993 | -55.691299 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 843828e7-2809-3a45-9098-7cd3c612771e | -7.0554 | -50.004398 | 2026-10-09 00:06:00 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 045ee13e-c351-3da3-ac71-68c9f14167c5 | -4.7972 | -56.138699 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b184849-13a2-354c-a772-0ac4e498d11c | -6.0016 | -40.9603 | 2026-10-09 00:06:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6fa91287-53af-3f53-8c25-c0722496e0b5 | -3.529 | -54.646599 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2188b02-fbe3-30a0-bc88-9df917982bfb | -4.9451 | -49.413898 | 2026-10-09 00:06:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c182c76f-7036-3be3-844a-e0e165288d97 | -5.2637 | -47.9077 | 2026-10-09 00:06:00 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c818bd76-31e1-3abb-aa76-545472d4ab9e | -16.9911 | -41.168201 | 2026-10-09 00:06:00 | METOP-B | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5a82cdff-3a80-39af-ac3c-bf61a74f1772 | -5.7071 | -53.450901 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83192974-4f4f-3f7e-b7b4-52204ce1af86 | -10.0155 | -48.5457 | 2026-10-09 00:06:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41a7ffd8-71cf-3ac2-b206-7bb7d0c3e9d8 | -0.6592 | -52.527 | 2026-10-09 00:06:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e3b0092-e2bd-3031-b447-686b9001ed64 | -3.6942 | -47.6726 | 2026-10-09 00:06:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd08287d-b1f0-3be4-a576-629ef87b7cfc | -11.635 | -43.699402 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 22165d8c-686e-3af1-975d-29f610fc1b66 | -12.0114 | -43.457901 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0244bf03-910e-34ab-8195-5cfe5a7f3921 | -5.79 | -43.859299 | 2026-10-09 00:06:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e79d410e-6f6b-3943-9e90-ae77c090967c | -7.5046 | -47.3321 | 2026-10-09 00:06:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9edf8d8f-4492-31ac-ad8c-7e666d1daeaf | -16.511299 | -42.509499 | 2026-10-09 00:06:00 | METOP-B | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 56289a20-83a8-394f-a875-294f50dc64a4 | -2.5262 | -58.068001 | 2026-10-09 00:06:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8687022-9fc5-3d16-9cc8-1ba3e090f8c8 | -3.0847 | -53.938999 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef2e5481-6ec3-3306-aa84-25fccd989502 | -3.5192 | -54.6488 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03faccaa-14c8-304a-b3fa-09c774816959 | -8.193 | -45.794701 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38dfd500-8f3d-39c9-b52c-d6b6d1271967 | -2.9918 | -53.8904 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33bc90e3-759f-3747-9dd5-e76e6397cc37 | -8.7326 | -45.142601 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6bd82f77-c90e-31af-a8c2-ec6e673161bb | -2.955 | -49.183701 | 2026-10-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5729b1f0-10a4-33e9-a833-d7ace7629ca0 | -3.1901 | -50.544701 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0047c7a-b926-33f8-a6ba-d09c62bb6110 | -6.4368 | -55.026001 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d64f8a2-ae41-30ef-81e6-245becce73b0 | -5.2622 | -50.137001 | 2026-10-09 00:06:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ef801cb-0eaa-3fc6-8e9c-39e166aa5790 | -10.2767 | -47.825001 | 2026-10-09 00:06:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d8003e8-bd87-324c-bfe4-4f4dc2243106 | -8.9002 | -44.932701 | 2026-10-09 00:06:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae3d26af-4768-34c5-845e-20247a07ceee | -4.2928 | -54.810501 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63dd67bc-a6d2-3dfd-81ab-ec482527197f | -11.3218 | -46.6553 | 2026-10-09 00:06:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d42465b4-cb58-3430-a522-7234209708d1 | -1.1112 | -54.166801 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a43b9b69-45ef-3da4-8555-3ad4f63dabd9 | -11.7817 | -43.534599 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1be340-c97f-350a-b657-857fb2e2e57f | -10.7381 | -52.020302 | 2026-10-09 00:06:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39ceaa76-6034-39df-949c-8efec530e630 | -2.4883 | -56.147301 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5b7369d-1478-39c5-ba85-eba460f5b566 | -14.0046 | -48.767502 | 2026-10-09 00:06:00 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 47fe7853-7b3e-3333-88a5-67a8a8a9ec60 | -3.5957 | -54.577099 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9ddca49-3d68-347a-abd5-c572a2157dbf | -6.9587 | -45.279999 | 2026-10-09 00:06:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d114bdb-057f-3d95-863c-af4b19d9c1b4 | -8.1891 | -46.358101 | 2026-10-09 00:06:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e590c86-3f12-36ed-bee8-08f5358165da | -3.2343 | -52.257099 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e654c519-359a-375e-8543-aa5404618058 | -3.1692 | -54.735699 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b19a878-0d79-374f-b232-8c1d92630009 | -5.2833 | -47.903301 | 2026-10-09 00:06:00 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb5b59b3-9314-357d-abb6-39e324eadb2a | -6.1552 | -47.9282 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8196b84f-4958-31bf-8a1c-01a6d5c71403 | -8.7287 | -45.170101 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5655545a-b0e0-34cf-9cfe-bbe210787bc2 | -10.2978 | -46.598701 | 2026-10-09 00:06:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c14f8f55-ea2c-33ad-ad69-7a1581421e42 | -6.4465 | -55.023998 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93991c99-280e-3da5-9521-86534ff65fbc | -3.1669 | -50.578899 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd0f8656-1132-3ad5-b8ef-3c90390163c7 | -8.2508 | -54.723202 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 097187e4-540c-34a0-985c-80a9c782cc8b | -4.804 | -54.665699 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71223e95-fc4d-3c82-9c63-8bd234ab24a0 | -6.5146 | -45.410702 | 2026-10-09 00:06:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 347ab4b5-cb8d-3f95-8876-8c10ab7941fb | -14.0729 | -43.7789 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7535798-f2cb-35bc-a263-2805d05214a6 | -3.7109 | -59.6222 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85b87333-0ea8-395f-a099-76005efbf8a7 | -14.971 | -47.535702 | 2026-10-09 00:06:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f663c1bd-ac8d-3707-9218-8b68b807fe20 | -2.7588 | -54.0896 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04ac2697-34ee-3788-a333-d993f665acd9 | -4.0923 | -44.1292 | 2026-10-09 00:06:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd1d38a2-3b0d-3d60-aa9e-5b67da922997 | -6.4836 | -55.292999 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7bae431-854f-3d2e-a253-0395aac7ca45 | -2.8861 | -54.061901 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3be10ea-879c-3bee-84db-68e62535fc2e | -18.6698 | -44.251701 | 2026-10-09 00:06:00 | METOP-B | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 86dbb9c6-73d9-303d-beb4-4fec58a0fc90 | -11.6127 | -43.606098 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d20dd3e-451f-3791-b625-406886cb7efe | -2.1858 | -48.247299 | 2026-10-09 00:06:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f412b6ce-fb49-3f2d-9c67-29ad8a3b1cc5 | -14.0441 | -43.8316 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c479701-77d4-357b-b135-536b3eca86a8 | -10.736 | -48.543999 | 2026-10-09 00:06:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f65219e-9fc7-3969-8d50-7ffeafa95f01 | -6.7251 | -48.121498 | 2026-10-09 00:06:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| eb806330-45b4-3f32-81f2-d27b9e2b9c54 | -9.1028 | -48.794601 | 2026-10-09 00:06:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e3bfc226-3afc-3ab1-b424-00b705319d1c | -9.7827 | -44.777302 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f8be31db-5047-341a-b8a4-e4ee7a8743a5 | -14.4301 | -43.933998 | 2026-10-09 00:06:00 | METOP-B | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 84629c57-4234-346f-80d2-1c9dfa18e789 | -4.9422 | -45.655499 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb12739e-3aa3-3d22-93de-dfc3c3aa6660 | 3.7287 | -51.633598 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 206bd1fa-b5ac-393e-8c91-01cbec3a2f00 | -12.0009 | -43.5005 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef21745b-f29e-362d-84dd-ec03844b0033 | -6.0356 | -44.026402 | 2026-10-09 00:06:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 927c66cd-f5c2-388f-845f-79b1e3bd9914 | -3.0152 | -54.1343 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb724f83-4dff-31f1-80c2-6ca7a23f5e1c | -9.8022 | -44.772598 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 439bebfe-d72c-3b8e-9d94-c0ca0746f4ea | -9.0161 | -44.372101 | 2026-10-09 00:06:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 125bd702-7c21-3330-9ba8-a485b8a4906a | -10.8795 | -49.147598 | 2026-10-09 00:06:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c302c74-fe78-34b1-aea9-8ca7217d2928 | -12.0017 | -43.4603 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| efcb58c3-d1e8-3219-9dd9-6b06d5adcc67 | -1.4686 | -54.7509 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3c78943-379b-3ac2-ae44-329755192ffa | -2.9347 | -54.141701 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7e6f041-477c-314c-afd3-a9012f76d554 | -3.4877 | -50.493401 | 2026-10-09 00:06:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b381077-4446-3188-babf-27629799667e | -2.3771 | -48.2271 | 2026-10-09 00:06:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 480fad42-7290-3e62-ac21-47f8ebfa2748 | -3.0987 | -53.955799 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7a91b74-3381-3f59-b24d-cf912e23a3a8 | -1.5483 | -54.5569 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 178da5fe-e07c-3ab5-8e55-b45e3739e6df | -8.9655 | -45.167198 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 048edaa2-2507-39d7-840c-7cb75e46f7a4 | -9.8431 | -47.4566 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4ae03b7-932e-3f71-bf57-c5500f172369 | -3.7012 | -59.624298 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| beab4507-5ab5-3df3-a4ac-7475fa585ae0 | -2.7564 | -49.536098 | 2026-10-09 00:06:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fbc2a6e-7b6f-3abd-863e-ead8356c83e6 | -13.7222 | -49.125999 | 2026-10-09 00:06:00 | METOP-B | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1215fe3a-e604-3e4e-abcb-7407aabb857f | -14.8734 | -50.306099 | 2026-10-09 00:06:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6186d57a-1ce9-3f31-af5b-5bc13b1969f1 | -12.0443 | -43.379299 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7306d332-5624-3a81-b955-7255c576f0ea | -8.7306 | -45.134201 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a765d6a-eba7-32b3-8daf-80d2ad6018dd | -10.521 | -47.308399 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a41cb8d1-d895-3b36-83ee-6a555def426d | -14.8796 | -50.2868 | 2026-10-09 00:06:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README14.md)
