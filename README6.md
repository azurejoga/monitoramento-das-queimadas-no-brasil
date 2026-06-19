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
| 22cd0002-71b6-3361-945b-2c98a735f74f | -12.78221 | -44.5135 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8847d673-94d8-31f3-8cc7-76c0a3317b28 | -10.5409 | -47.70985 | 2026-06-19 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 35bd436c-a42d-3b8d-9a60-52adda40e83d | -13.94087 | -53.5621 | 2026-06-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 54cb404d-7a12-3d75-b757-919d829fb3b7 | -13.49241 | -47.50657 | 2026-06-19 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 769b990d-cc25-3ce9-b1cd-570f724073c0 | -8.5715 | -45.98248 | 2026-06-19 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8140c404-6570-3cab-9991-084239cec8d5 | -11.06745 | -52.46396 | 2026-06-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d4a08e4-c7e3-317c-a4a1-e7c32e4b47fc | -10.99041 | -47.75103 | 2026-06-19 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d8b4bbf-ecd0-3067-89bc-7bdc1f60bbb5 | -10.12459 | -52.17776 | 2026-06-19 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e03166a3-e8e9-34a1-a208-f3e45b21d08e | -7.83264 | -55.40863 | 2026-06-19 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b71fa13a-72d9-3a54-a508-58cf827e85f0 | -10.99096 | -47.74753 | 2026-06-19 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e46cbf3-f5fa-39d0-b6e9-3aaaa337132a | -10.06261 | -48.08527 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| be9f62c2-5d69-309c-ab4d-ebdf7d2d135f | -8.57428 | -45.98648 | 2026-06-19 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f252a520-4872-3ed3-b630-2cdb46801223 | -12.77983 | -44.50462 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92f1b896-a89d-3fbe-b58f-1fc096661012 | -12.54847 | -54.59111 | 2026-06-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dc2310ec-298a-3394-8a3f-ca4fe981a75f | -9.67949 | -47.04118 | 2026-06-19 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8cdfc0e-18cd-39a8-abb5-10a10f6b359f | -11.33815 | -48.00623 | 2026-06-19 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fd1d616-28ca-3001-b884-affa6301f927 | -13.64517 | -55.29133 | 2026-06-19 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cb37fbd-7ce0-3681-a9e7-fdb31968b08f | -10.5442 | -47.71039 | 2026-06-19 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2977c2a4-e78d-3d88-99e4-34283cf42cd6 | -10.15845 | -56.61948 | 2026-06-19 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34daf33c-1c07-3711-be87-9d5f00e1eadf | -9.75227 | -47.87494 | 2026-06-19 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8727ba09-7bbc-36bd-b711-c567552c0c6c | -12.87329 | -44.35284 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f82fc618-9bd9-300a-a3fe-c1b79f1adc6e | -8.68928 | -48.30382 | 2026-06-19 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 420049bf-12a2-3021-acb9-6c061f970359 | -14.20771 | -54.71439 | 2026-06-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c3b5a39-1891-34ca-99d6-f8c5a1866aeb | -12.54933 | -54.58637 | 2026-06-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5ba716ed-a90d-3f42-b527-873cfcd3b5ee | -10.16455 | -56.61694 | 2026-06-19 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbc2949f-37cb-32a9-a17c-27c95f4f1688 | -8.91554 | -46.94389 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 58b6f962-a2b7-323b-b33e-6b518c7941ea | -13.31764 | -45.16108 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cb0f8a2-b020-33ca-84a6-47e37680f729 | -10.98104 | -47.74593 | 2026-06-19 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7578a9fe-0578-3cba-81da-8aae0ae07556 | -14.21916 | -54.70251 | 2026-06-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cfec0d3-aca7-3f50-8fd1-d00c98f40fe8 | -10.24995 | -47.35439 | 2026-06-19 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ca1ba38-2cc2-3f49-8e1d-e595a6f1eb6a | -8.91224 | -46.94337 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fd19da55-1314-3301-bb81-342b284e0ac4 | -11.05935 | -52.4625 | 2026-06-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 556572b8-2575-38a3-8839-02499db8b316 | -12.49542 | -43.77032 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 474f3d62-f6a8-3ae2-bd15-4a44ea974e61 | -12.40983 | -43.82389 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 483acc41-b92e-331e-b54b-2013daecdf72 | -13.50301 | -56.5765 | 2026-06-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3798716d-4eef-3778-8d18-c294e37d81ce | -11.06061 | -52.45527 | 2026-06-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d23fdd3c-4258-356f-8572-bb98ddb7dc9d | -12.44742 | -44.75185 | 2026-06-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29f84bfc-c3b2-315f-9590-a0f61a191f9b | -12.41417 | -43.81987 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa8fde1f-954d-36a9-af88-0c241e611ace | -10.15234 | -56.62207 | 2026-06-19 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9ce1071-cee4-3223-9e57-510ff372f09a | -12.87269 | -44.3571 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a824c795-cfc0-3565-bbd2-c94811a56274 | -13.94018 | -53.56596 | 2026-06-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7d63b8ec-9c76-39a1-a405-0254d43f630e | -11.35955 | -55.82179 | 2026-06-19 04:27:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 144efc03-66bf-3bea-bc3a-d2775f267592 | -7.83322 | -55.40539 | 2026-06-19 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7c049a4-a9a2-31cc-98db-37d998bfb29d | -12.91978 | -49.48433 | 2026-06-19 04:27:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ebed94b-e80b-3dc0-9c50-77f6a7fa8bde | -10.91151 | -56.8537 | 2026-06-19 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bae2a07-ae4c-34d5-822d-311ae9ad4278 | -8.89807 | -48.00322 | 2026-06-19 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d27b786-a489-3935-a1b8-a2da20db5477 | -13.32289 | -45.17408 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 895cdefc-6fc0-35b7-9c84-ab46d48a2aea | -10.15065 | -56.62203 | 2026-06-19 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 697fd5c1-f58f-3cd7-952c-8f1da0ca4c68 | -12.87449 | -44.3704 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| f7224203-ae3c-3b0a-b216-bf0a5091ae53 | -12.77623 | -44.52959 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27423808-2c39-31cc-b621-b0e8c8f6f454 | -12.55019 | -54.58166 | 2026-06-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0709cacb-4e1d-3182-8190-adfb59eca108 | -8.89864 | -47.99965 | 2026-06-19 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26aec7f1-914a-3e01-af37-4f5d8f0a1118 | -11.52074 | -54.25948 | 2026-06-19 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bc1ee84-e914-3bc6-99b0-d5dbe645fefa | -11.91623 | -55.91487 | 2026-06-19 04:27:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 138e8c5b-fa25-36ce-a90d-27330f6455dd | -9.60197 | -48.19827 | 2026-06-19 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0eaa4d14-76e8-3b05-be66-607f2ca8c3cb | -11.55196 | -48.267 | 2026-06-19 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27add68a-34fb-3a65-9fc5-6d8096c5ef82 | -13.32639 | -45.17458 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 159bd287-3602-3192-bc64-0070c3ab6448 | -10.75353 | -50.20301 | 2026-06-19 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e9049ec-c4db-3266-aa72-8626f28492fe | -10.80974 | -56.59875 | 2026-06-19 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a552232-ab78-3494-8a98-6c9777eb7fb9 | -11.87463 | -47.1011 | 2026-06-19 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 538e4ca5-abdf-3346-bb98-bb6e404bbdfe | -10.06538 | -48.08941 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 403e8d74-9c92-3d24-ab6b-5e8f4fa4b36b | -8.68869 | -48.30747 | 2026-06-19 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| debb77fc-8830-3e28-a8fb-d7166745ee37 | -10.91123 | -46.33619 | 2026-06-19 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 140aeaca-54f1-3dad-84f7-8c6f8654546a | -12.49787 | -43.76322 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c34cf002-fc5b-35b2-aa92-8ad9a1da5fc0 | -12.41352 | -43.82447 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8b53559-493f-331e-abac-7d28ecdd7e4e | -8.90952 | -46.9607 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2ebfb38-560f-3a94-8e92-9f178b2b6efb | -11.457 | -47.40307 | 2026-06-19 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6fb0299-62e5-310d-8371-862173f9198a | -11.33428 | -48.00923 | 2026-06-19 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81809142-e8e6-3986-943f-0a587f78e8a6 | -9.55043 | -48.56306 | 2026-06-19 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a02b37fc-4bea-38c1-b298-7a3e8ae9d759 | -12.8781 | -44.37093 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1198dd83-79ba-3fde-afc6-70bce2b31370 | -10.05482 | -48.09129 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afd56646-e5dd-3a32-b2a0-51374035a578 | -10.90609 | -56.8526 | 2026-06-19 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d6d6bee-6ca2-3fb1-acce-1bb166e19601 | -8.90623 | -46.96018 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9b67e6d-db30-32bb-83e8-be76ae309b32 | -9.15477 | -47.2425 | 2026-06-19 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f6dca03-31fb-31ce-8047-1d7ee473edaa | -12.78161 | -44.51767 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7d02c92-31a4-3bf3-bb8c-9eb57f9f9e8d | -9.68004 | -47.03771 | 2026-06-19 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53a5fa3f-3394-3b9a-8a9a-c337e7f9a9fc | -10.69642 | -49.60375 | 2026-06-19 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98198359-fa8d-33d7-9b48-5f62490901e2 | -10.05701 | -48.09901 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c128f06a-b1d9-33a6-afcd-1269a7633f53 | -13.94433 | -53.56672 | 2026-06-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2d5d2e98-2e7e-3536-bf8c-2665f95744b0 | -10.98766 | -47.74699 | 2026-06-19 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33ea4664-127f-3552-8bfb-d90b8ff1582d | -12.78281 | -44.50933 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15779d32-5b94-39d6-aef1-4f9dc3773ffc | -12.13413 | -48.26712 | 2026-06-19 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2e0616c5-920b-3b09-b005-ce220fe882ba | -12.83589 | -44.37111 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 029fa281-e347-3107-b2a9-18f7eb5b83de | -12.49912 | -43.77087 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 52162496-2ee2-3574-a9a3-a84cf37233bd | -8.90898 | -46.96417 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c6145aa-fb5f-37b2-a580-489dd13de6d3 | -16.02782 | -43.4233 | 2026-06-19 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| dfde6d47-642c-3a1a-a161-3a0d0db4c6e7 | -12.35743 | -47.43084 | 2026-06-19 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fe197c7-8048-36bb-ac80-41bb58729d57 | -12.69173 | -54.58158 | 2026-06-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18df4537-999d-3638-9f14-b8183222d5a3 | -13.48912 | -47.50603 | 2026-06-19 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da918b0a-f53f-3266-8e76-b4ec557cdb8f | -13.33628 | -45.20454 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9b61cef-9630-34aa-a80b-ee3e0e21230b | -8.78755 | -46.62845 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 693aecd6-1210-3739-847a-829f926576a5 | -8.89529 | -47.99912 | 2026-06-19 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69ff6d6a-2e04-3f4c-be20-792436439aaf | -9.69163 | -47.69882 | 2026-06-19 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73dca4fa-8fd0-341b-844e-c81df485c4b6 | -18.97702 | -52.45829 | 2026-06-19 04:29:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbfce82e-bd9e-37a2-958f-51691dc950d4 | -20.31565 | -49.36366 | 2026-06-19 04:29:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ea27814a-4973-3bcc-b14e-0e20ab8d376f | -22.32199 | -41.79539 | 2026-06-19 04:29:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7475541d-9a74-3151-beef-ad7f385ad789 | -20.31953 | -49.36058 | 2026-06-19 04:29:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dbca499a-27e9-3463-a701-c1366ca60ae6 | -14.95139 | -52.87294 | 2026-06-19 04:29:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 761e197d-8d7d-3034-9bb2-392f25ecf7da | -17.34794 | -53.81564 | 2026-06-19 04:29:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11ebf917-19bf-39e0-aa8c-c1abd5a5c325 | -18.48889 | -51.67526 | 2026-06-19 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README7.md)
