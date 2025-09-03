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
| bb0e8c4c-bb1c-3efe-bcff-be5274be5369 | -6.9562 | -42.964901 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b1096833-fd91-3477-8dff-1529c613376a | -6.2432 | -42.607498 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c4c610c2-1c40-30c6-a318-ae6d3390fa16 | -7.5309 | -47.439701 | 2025-09-03 00:24:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bba85ddd-25b4-3a3d-a493-9f4c809ce329 | -7.7105 | -48.719799 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b3b21e48-dd20-3d80-a09f-ff0048015ff7 | -6.5733 | -47.387798 | 2025-09-03 00:24:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a08cb9ce-2135-3602-8772-39fdfd018e06 | -11.5685 | -52.095001 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4aa5778-2452-34d1-9e12-eaad96b1d843 | -6.8141 | -52.799599 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a86b093f-7e53-3d5d-8a3a-e14fb7b9505b | -13.4812 | -46.8195 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 363c1184-e92d-3521-9be6-d4dd9e957833 | -8.1937 | -44.799801 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9549a282-d3a1-3858-a80e-79421c313c73 | -7.4791 | -44.830898 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ae52510-3cfe-35e6-a42a-56dc44cac497 | -6.7566 | -45.915199 | 2025-09-03 00:24:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 782cb54f-b981-3ffd-8ca9-e84bb64177a1 | -9.1387 | -49.641701 | 2025-09-03 00:24:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f57acef6-aa46-33ca-b37c-b8168b340ceb | -14.802 | -48.212799 | 2025-09-03 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 774fb04b-a13d-384e-85f3-5f1643cc5285 | -9.727 | -48.9972 | 2025-09-03 00:24:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5becc00-87e9-3c60-820a-54f197541ac1 | -6.8309 | -52.830601 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ddc8505-fe9e-3dfb-ab7e-2bec5a41d31d | -6.9464 | -42.967098 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 27fd717e-8ff3-3cbc-9a61-ba681903366a | -15.8911 | -48.1581 | 2025-09-03 00:24:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 903e200a-df03-3a6e-9691-cb15c3e958fe | -11.1119 | -44.672699 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c63b9f1-e740-3843-bd14-2f13f74adfce | -6.4641 | -45.398399 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95c662e8-2d04-3ffe-8a20-f0d5e715a05d | -8.0238 | -44.0564 | 2025-09-03 00:24:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 87630ef8-42e1-3e26-a13c-d1214c7d5a06 | -9.6308 | -47.038399 | 2025-09-03 00:24:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a90a66c0-7acb-3645-bdfb-e1389553f0a8 | -8.3758 | -48.291401 | 2025-09-03 00:24:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ff4fa6b-c0a9-3377-8487-af1274f14b79 | -11.3737 | -43.5513 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| edd07560-e6c1-30e7-9932-70d21bbbfbbb | -6.4528 | -49.530201 | 2025-09-03 00:24:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14be0381-a457-3621-a204-3172d2a08ede | -12.9798 | -48.084999 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3cb7714-7fab-3646-857f-0330dbdbdce5 | -6.1116 | -47.210201 | 2025-09-03 00:24:00 | METOP-C | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48374471-8dcf-3052-be31-a08b2797ed8f | -10.9828 | -46.835701 | 2025-09-03 00:24:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5551071e-2939-3f2e-a7d5-c3c602e22c02 | -3.9873 | -43.243999 | 2025-09-03 00:24:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56a479e7-57ef-3ecc-b601-fc2928e9a460 | -11.6234 | -52.065899 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6433163f-7ced-318f-ab06-d9569a4f0253 | -7.8965 | -46.4501 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ca0fb18-9c60-362e-b6d3-e1e58e652077 | -13.722 | -46.941898 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b31eba71-e398-39ec-b642-77805643fe87 | -10.5366 | -50.417099 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd37e5f-94b3-3ab8-9400-06dd78d5e5f6 | -6.9787 | -43.106098 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b96de11-24a6-3c57-bbdd-7060c5f82643 | -15.5634 | -48.403 | 2025-09-03 00:24:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea198a5-7533-3131-aa91-b207eea136ac | -5.7018 | -45.130299 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a80c3457-f5a2-3c50-98da-ffb795ab6516 | -6.7912 | -52.787201 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14126eef-1e51-3c26-a4ad-162193ad2652 | -5.7339 | -39.758801 | 2025-09-03 00:24:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 10baa6e1-1a7a-350d-b6cb-cc9cf1654760 | -11.6136 | -52.067799 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc1f3b18-011b-3616-8092-8f0cb0c5b72d | -6.8212 | -52.8326 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e22304a7-ca9c-319a-b3fc-5e1821db18ab | -12.7511 | -47.676601 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1dc8d68-5d6e-3134-8262-fcf95e546b6e | -5.8498 | -48.153301 | 2025-09-03 00:24:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 278161c4-ebaa-3aa8-88a1-0fe457324f4e | -11.5844 | -52.073601 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9421bf09-bd9e-3178-ac8e-67813e873ac9 | -5.8 | -43.230099 | 2025-09-03 00:24:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc303bac-40c8-34a1-98b5-fa8e229fa12c | -4.6642 | -41.9454 | 2025-09-03 00:24:00 | METOP-C | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2df5d58b-146b-3b37-b47a-4de7cc38a510 | -6.5614 | -51.104599 | 2025-09-03 00:24:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99be0276-3b73-3b65-8634-cbbc2967ce4e | -13.2779 | -46.827202 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1f8260c5-8df0-3a46-8477-ac4cbf7758cc | -5.4355 | -42.905499 | 2025-09-03 00:24:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7143a6dd-7e6a-38c8-9f23-20014c581208 | -12.8282 | -48.044201 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b4ce8d3-9972-3fff-96ae-78143d6a6f2d | -9.1785 | -45.189701 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a95fd637-590e-32e6-99aa-3b6532a46547 | -12.9916 | -48.092999 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74737649-c010-366e-8f88-8fdde6c9780a | -13.7024 | -46.946098 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20ecfb6c-b357-3848-9300-a284d4c24c79 | -4.5566 | -40.353901 | 2025-09-03 00:24:00 | METOP-C | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b1aaee46-4226-3b1c-ba65-d0a92a30ee5a | -11.4833 | -43.217602 | 2025-09-03 00:24:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3ab1ca31-f919-31bf-a8eb-a284154bfa50 | -5.7757 | -46.451401 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35e7ca63-b9cf-3926-92de-9372343496cb | -10.7409 | -45.269798 | 2025-09-03 00:24:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af68c13c-4c7f-3d0e-9a94-f5199aab456f | -7.4858 | -44.814999 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 70b7eb2d-ebe7-3c59-bc60-97454535963a | -11.375 | -43.6021 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c86eecca-7bd6-3eac-a9a7-0040859d30a4 | -5.8516 | -48.161499 | 2025-09-03 00:24:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 20d9b4fb-c47d-3acd-a73a-e4e627d69bdc | -5.7983 | -43.222801 | 2025-09-03 00:24:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14877333-dc46-33dc-b279-d6ea9135c8f6 | -14.7812 | -48.160801 | 2025-09-03 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c226aab1-52fe-37b5-9a46-dc890335def2 | -5.4995 | -42.6488 | 2025-09-03 00:24:00 | METOP-C | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c701650-2043-3134-bef9-077a4900581e | -6.6899 | -44.177799 | 2025-09-03 00:24:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b50b30f-a02f-3112-b907-8a2ada506e6c | -8.0137 | -44.102299 | 2025-09-03 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ea15fb1-f19b-3605-8f6c-dc5f7cba8f1f | -13.3073 | -46.820801 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a51a83f3-7d2a-3e6d-bf32-43a0d2d13966 | -8.8792 | -45.828701 | 2025-09-03 00:24:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 580af9f5-936e-3785-828c-e7351cffac00 | -4.8878 | -44.953899 | 2025-09-03 00:24:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe8339f0-10d5-3180-b3c9-8ba7639442c8 | -9.1734 | -45.212799 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0634db71-9db4-3dd1-b8de-11fc95954aa9 | -15.8934 | -48.1693 | 2025-09-03 00:24:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| dbd97159-d430-3b98-bbf2-5d83326fe305 | -7.427 | -46.0098 | 2025-09-03 00:24:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dc3c23a-fc56-301c-af53-b9aba098f51e | -5.881 | -43.001301 | 2025-09-03 00:24:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b1873c8c-42ad-3d44-a00d-622de74d7bf5 | -2.8961 | -48.2869 | 2025-09-03 00:24:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa419cd9-c5ec-3a26-a516-136da40e0fe4 | -9.6458 | -47.859402 | 2025-09-03 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 213a8927-50b3-3050-9e21-c3ed62d651a1 | -13.2797 | -46.8358 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a025cc49-6a1a-375e-b265-e24833ae385b | -12.0219 | -45.573299 | 2025-09-03 00:24:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc3e11ea-eee3-3f4d-8952-51cb64eff69e | -6.8372 | -52.812 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4caeb2cc-8028-3bcb-9945-f19af14ad4cc | -4.6681 | -41.962299 | 2025-09-03 00:24:00 | METOP-C | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e6df8ad-e6ff-386b-ae08-e0ccce3e2cfe | -8.4571 | -45.0522 | 2025-09-03 00:24:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c6570599-f7ff-3536-8cd7-ee8187e8f0b0 | -5.8933 | -46.151699 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ffa3e68-7e56-366f-9a97-94ec38028dee | -4.3899 | -49.3451 | 2025-09-03 00:24:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62775cdc-1a99-30dd-95f2-fc30cb22a605 | -12.4926 | -47.4702 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68485843-c09e-39b9-8a40-1ad6e35b77eb | -4.7299 | -44.446499 | 2025-09-03 00:24:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8f0059a-9ca1-30f3-8700-4c760b9a0da1 | -6.7717 | -52.791199 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a3f3d19-da85-3054-bb88-6df3a66ed9c0 | -3.7901 | -49.419601 | 2025-09-03 00:24:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3078ef4b-685e-3976-bf61-b4fb501b3215 | -13.5043 | -47.0261 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 003ae284-2486-3315-9fff-1213bf54a11a | -10.0544 | -48.089901 | 2025-09-03 00:24:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40ecd24e-2734-3cd6-a366-bd125122db07 | -11.3753 | -43.558201 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3fd0b797-089d-3084-baa5-2627a21126d7 | -15.0061 | -50.060699 | 2025-09-03 00:24:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f4f71797-3736-3734-bdd4-883d2859bbcc | -5.8948 | -46.158699 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc4fd9c4-fa8b-31b9-b2c0-568ecdc1f015 | -6.8044 | -52.801601 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 202e2671-f8d2-3936-bf68-41a0dc4ecb19 | -8.1952 | -44.806599 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4c5e07b6-22ec-3eb9-b06a-edb51e6025c0 | -13.2903 | -46.9338 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e27e7ba-aea7-3f06-86b8-b8c0d178e9a0 | -6.7292 | -42.2584 | 2025-09-03 00:24:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9d7e7d69-4929-3586-b042-41816f4c9e2a | -5.8596 | -48.151199 | 2025-09-03 00:24:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5c11490d-ba05-3286-87cb-bb997c71dca0 | -11.6039 | -52.069801 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2eec106-3c26-382c-b623-772262554e99 | -6.7814 | -52.7892 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c2045be-b46e-3c1a-bc24-ee29a1eb526a | -7.5005 | -45.3326 | 2025-09-03 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 952c68dd-4b2d-3503-9062-68aead38b6d7 | -14.5651 | -48.050701 | 2025-09-03 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bda8d66b-be00-3d92-9a80-8e10fc6b61a4 | -7.4693 | -44.833199 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ad346bb-ffc2-30f1-b655-b2117149585a | -11.3766 | -43.6091 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c26b7ad-edff-39b5-a743-b8d84f4435f6 | -9.1363 | -49.630699 | 2025-09-03 00:24:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
