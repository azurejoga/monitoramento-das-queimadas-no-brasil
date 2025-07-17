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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1a99fa8-c71b-3b46-ad61-41067a07a075 | -2.9071 | -48.241001 | 2025-07-17 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a810ad2-1c80-385a-9e27-044417a43f28 | -12.4723 | -46.9104 | 2025-07-17 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94962a95-c7ef-3a35-ae40-c0687d0ac967 | -11.9454 | -48.41 | 2025-07-17 00:21:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0eb428f8-483d-3ef1-acd3-4de038d09057 | -11.4942 | -48.939499 | 2025-07-17 00:21:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fabbb445-c316-3fee-a732-4c61bcbf592d | -12.0178 | -47.77 | 2025-07-17 00:21:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c3484b0-5c9b-3a37-947d-30adfedea660 | -12.4215 | -50.0238 | 2025-07-17 00:21:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23ac6cf7-6ba6-3f98-b7da-f1ebb05c99fc | -9.2437 | -48.549301 | 2025-07-17 00:21:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb79d440-0c01-3726-b3c8-269da6266c2d | -3.8415 | -47.736 | 2025-07-17 00:21:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 311a6481-0aed-3d0e-a894-a2b5e06399d4 | -5.6501 | -43.716301 | 2025-07-17 00:21:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2a58cbd-3173-354a-8eef-cbf19a44cb71 | -22.5947 | -47.213902 | 2025-07-17 00:21:00 | METOP-C | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 008a4189-fbe8-3fb6-b563-9b83bd5cc246 | -8.8739 | -50.132999 | 2025-07-17 00:21:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcd38a5c-3efc-31a4-8d22-35ba002b8d37 | -5.907 | -45.5774 | 2025-07-17 00:21:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad9723c5-a7b2-3493-b37a-90e71f12abb1 | -7.6087 | -44.3097 | 2025-07-17 00:21:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5396cb57-de8b-3cf3-b7e7-ae7d248f914c | -8.0357 | -49.873798 | 2025-07-17 00:21:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7e46351-4538-3a2f-b96a-bdb9fe52fa6a | -6.7139 | -44.315601 | 2025-07-17 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d31cc077-9b34-37e3-a4fe-acf2043f448c | -3.3855 | -47.492001 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56e34433-605e-3dea-97e6-6abb5cc26e8e | -9.2411 | -48.537102 | 2025-07-17 00:21:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a73150eb-38b5-3dc5-a893-b331f0664a51 | -4.646 | -43.115398 | 2025-07-17 00:21:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a1a19ba-a3fe-3f93-96f0-849928796455 | -5.7936 | -45.0746 | 2025-07-17 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 032ac031-da22-32ab-9c4a-39b353789f7a | -20.1772 | -48.6996 | 2025-07-17 00:21:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a1cc95e8-9ed3-33e4-8e23-ebb360595424 | -6.9669 | -42.8008 | 2025-07-17 00:21:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e765941-ecdd-32fe-8a12-f9a7845e4682 | -5.5946 | -45.789902 | 2025-07-17 00:21:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a34bd735-e9bb-38c9-9ea5-a708950422c8 | -3.4071 | -47.496399 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6d11fca-ffd3-305d-bc85-57bdbc6971af | -5.5107 | -41.3223 | 2025-07-17 00:21:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61a033ac-05ee-3b32-aad9-af46644c261d | -12.7013 | -46.784599 | 2025-07-17 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02c3e2d8-6365-30e4-9ade-b14d86947f85 | -11.504 | -48.9375 | 2025-07-17 00:21:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b332f53-45cc-3412-a0d4-63d353d73831 | -5.509 | -41.3148 | 2025-07-17 00:21:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4829e825-7864-3bfc-9dc4-baac49e17e75 | -22.3936 | -49.776299 | 2025-07-17 00:21:00 | METOP-C | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 20b6fd02-575a-39ae-aee9-934c0c878aba | -6.7025 | -44.3106 | 2025-07-17 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79f4b6db-192b-357f-aa23-0651b289b2da | -6.7057 | -44.324699 | 2025-07-17 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0267cda1-a078-3ee7-9455-14e2a65dd3ec | -12.4181 | -50.006699 | 2025-07-17 00:21:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1b8c8f-630c-3ce6-bd34-cafb9bbf2118 | -12.4821 | -46.908298 | 2025-07-17 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 937288ba-62e5-3397-a8a3-19cd5771b9cd | -3.8435 | -47.745098 | 2025-07-17 00:21:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb378c3-9c4d-3da6-b5ae-23c698e77332 | -14.028 | -51.196201 | 2025-07-17 00:21:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b07eb32-d1cd-32f4-bcec-922f5e9c976c | -6.8809 | -47.228901 | 2025-07-17 00:21:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ac362f0-9f5b-3152-88cc-f9b49dd5bdcb | -8.1183 | -43.146999 | 2025-07-17 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95b961ad-80f3-3abf-9275-c47199095ac4 | -6.8417 | -42.749599 | 2025-07-17 00:21:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f0b72896-979f-37f3-9bf0-e35207ce41f9 | -11.3984 | -42.293098 | 2025-07-17 00:21:00 | METOP-C | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ef460165-19dc-3a2b-a7ee-f8756d19cc40 | -5.6583 | -43.707298 | 2025-07-17 00:21:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bced4641-f18d-3e65-afbf-2a8360c32c6b | -8.8803 | -44.795399 | 2025-07-17 00:21:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 42b3b98e-10ef-3bee-9f22-d3de704d50ad | -11.2278 | -49.4776 | 2025-07-17 00:21:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b4c8780-cc39-3398-a7f3-5c3f8c268168 | -3.3816 | -47.474701 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d19ad6c-baaf-3fd6-8cdf-4a7614f275e5 | -11.1061 | -48.832298 | 2025-07-17 00:21:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03d05769-1e92-33a6-b7f6-dc2c01be2ec7 | -7.2098 | -45.330299 | 2025-07-17 00:21:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2be6c50-3902-331a-91b0-b76356abb529 | -2.905 | -48.231602 | 2025-07-17 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a41ab051-3605-37ba-9eac-89e6ae404adc | -9.2339 | -48.551399 | 2025-07-17 00:21:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aaf4b8b6-5b05-39e0-8b12-f5b17ee4edcc | -11.2414 | -44.878399 | 2025-07-17 00:21:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d90decc3-6698-3393-b8a1-70bf7eef3795 | -5.6485 | -43.709499 | 2025-07-17 00:21:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cceed053-a1bc-3a9c-8a93-a6d5253f7b21 | -7.0892 | -49.169701 | 2025-07-17 00:21:00 | METOP-C | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d22f32ed-d38b-3568-a14b-03cdef2ef916 | -7.617 | -44.3004 | 2025-07-17 00:21:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 089dd254-55df-3a93-906c-7e5f96a608a5 | -11.2431 | -44.886398 | 2025-07-17 00:21:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd488983-31da-3c4f-b64a-6cd7045fadfe | -7.1909 | -43.103401 | 2025-07-17 00:21:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4ce4f757-575b-3887-8a09-e7e6595e8285 | -2.9148 | -48.229401 | 2025-07-17 00:21:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2960a5-c687-3145-ae77-b87a0a575bf1 | -3.3836 | -47.483398 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47490a88-7930-36e5-865d-f9684f3c9f48 | -8.107 | -43.142399 | 2025-07-17 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 25c84860-7d82-3036-9736-cd8dbfa6a861 | -3.3973 | -47.498501 | 2025-07-17 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2886c2a9-2f15-3c75-b9f6-1ad02a268b71 | -12.4919 | -46.9063 | 2025-07-17 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad41c006-7319-3590-bc8b-105b055b1fad | -11.9427 | -48.3969 | 2025-07-17 00:21:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6419fd4-7305-3110-b080-20b7c2fbe406 | -5.6614 | -43.721001 | 2025-07-17 00:21:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9283fd8a-755c-39a2-b907-b27d660e5f6e | -8.8307 | -44.203499 | 2025-07-17 00:21:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bf951f6f-547d-37c4-977a-e4032e9ccd66 | -9.3108 | -44.835602 | 2025-07-17 00:21:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b6cc11bb-0fb7-3ff3-b291-342dc28f1fe3 | -11.9329 | -48.398899 | 2025-07-17 00:21:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23bfafd2-2a65-3881-8042-38f5572cea8b | -6.9767 | -42.7985 | 2025-07-17 00:21:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| efe0be3a-67b6-3c34-b964-1b72cb8bcd77 | -5.7953 | -45.081799 | 2025-07-17 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b71f4c70-26d0-39bc-a93d-35d23fbb8b51 | -6.0003 | -42.6796 | 2025-07-17 00:21:00 | METOP-C | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 17355b34-dbbc-328b-bbd0-445992e42926 | -12.6937 | -46.797199 | 2025-07-17 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45d2b48a-c97d-348c-969d-3cd1448cb422 | -6.8463 | -44.7654 | 2025-07-17 00:21:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7b98079-eba9-3496-b663-da5e6b00b964 | -5.7855 | -45.084 | 2025-07-17 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5bfdddb-715b-388d-af93-f658ae3f85a5 | -8.1152 | -43.133202 | 2025-07-17 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d2948f5-5ca0-319c-ac92-7dc071ffd336 | -9.9237 | -47.999901 | 2025-07-17 00:21:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4f08b8d-3dbd-3e3f-b570-53922ae84cbc | -5.9053 | -45.569901 | 2025-07-17 00:21:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f8f9e28-015c-3777-b206-d71d6509804f | -7.1811 | -43.105598 | 2025-07-17 00:21:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0438a3a3-42f7-3e03-8e6c-1bb5113f18e1 | -5.9135 | -43.4702 | 2025-07-17 00:21:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98d2363f-ed6e-3bc1-befc-f0527b68206e | -7.2064 | -45.315102 | 2025-07-17 00:21:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e62336e-f1b0-3a4a-afa1-25e52fb4361c | -6.7269 | -44.3274 | 2025-07-17 00:21:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02003958-2d0a-35d4-97e7-2ec23bcaae9a | -5.493 | -43.931599 | 2025-07-17 00:21:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34a75433-09d9-32fe-83d4-8583dcfe07bc | -8.7502 | -46.584999 | 2025-07-17 00:21:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d69a6a4d-804a-3e26-9cd1-83f70cda76d9 | -3.5875 | -47.520802 | 2025-07-17 00:21:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f17fbae4-67c4-3506-93fd-8e61291b8940 | -5.5847 | -45.792099 | 2025-07-17 00:21:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b089aad-5438-3fe2-a930-648a9eb6214f | -22.380199 | -49.754501 | 2025-07-17 00:21:00 | METOP-C | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa0fbad8-bbbc-348d-9adb-e8b55cd8762f | -4.5872 | -43.308601 | 2025-07-17 00:21:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4400d43c-3627-3bf4-9327-4917e26ec94b | -22.3899 | -49.752899 | 2025-07-17 00:21:00 | METOP-C | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e037e485-4b1f-3f76-a2cc-b1056e91cbd6 | -8.1085 | -43.1492 | 2025-07-17 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 80d6ade2-3f4f-38b8-9e7a-773b6d4dbfdf | -7.1983 | -45.324902 | 2025-07-17 00:21:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0aa9cc2-1f58-35e2-9101-1fce1403189b | -9.2313 | -48.5392 | 2025-07-17 00:21:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c373d4ec-c82b-371d-90ba-2eb15d5f261e | -8.1054 | -43.135502 | 2025-07-17 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 427ad282-fa8a-3796-8c99-be6a4847cad4 | -13.0043 | -44.871101 | 2025-07-17 00:21:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 173beb84-3413-36f7-9335-cebb402b1ef8 | -4.7704 | -45.3316 | 2025-07-17 00:21:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e9ffbfc-1b39-3543-9e69-2439b6836125 | -22.76009 | -47.06138 | 2025-07-17 00:22:00 | TERRA_M-M | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 167e68cd-7d9d-33a4-b2f5-65b91da12ca6 | -22.39193 | -49.79905 | 2025-07-17 00:22:00 | TERRA_M-M | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| 6d480fcc-47ab-3554-8534-069fa94e0d53 | -20.18418 | -48.72863 | 2025-07-17 00:22:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 031b1a89-33d4-3b1d-964a-fabbc158efc2 | -23.42134 | -47.95142 | 2025-07-17 00:22:00 | TERRA_M-M | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 811cec64-ab33-3503-ac7c-4ed1be98ae40 | -20.17212 | -48.73021 | 2025-07-17 00:22:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 658841ee-db05-366f-91a6-3f52c04de2c6 | -19.44663 | -48.54239 | 2025-07-17 00:22:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 3a46f912-e303-3ce1-933c-645104814b0e | -22.60736 | -47.23358 | 2025-07-17 00:22:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 99656c9d-ed1f-3845-bf56-21a01cc749d5 | -22.59621 | -47.23515 | 2025-07-17 00:22:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d7d28486-3651-363b-bcb3-52d14b1805c5 | -18.85207 | -45.20961 | 2025-07-17 00:22:00 | TERRA_M-M | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 81c3175a-d2ba-3b4a-b9b0-ad060a6eb90e | -22.75921 | -47.06731 | 2025-07-17 00:22:00 | TERRA_M-M | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 2aa24714-5494-33de-9218-0f615538c0c8 | -22.60559 | -47.22387 | 2025-07-17 00:22:00 | TERRA_M-M | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7cb9dc0f-e164-3696-9408-d69eb69c4aa9 | -22.39752 | -49.80507 | 2025-07-17 00:22:00 | TERRA_M-M | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.0 |


[Clique aqui para ver as próximas entradas](README4.md)
