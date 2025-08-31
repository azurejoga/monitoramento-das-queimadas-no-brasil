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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f259cb73-2242-3c1d-bb07-25a1071983f3 | -14.61044 | -54.54585 | 2025-08-31 12:57:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b7f8efe0-3085-3bb5-b600-23c96ccb5874 | -13.4707 | -46.97242 | 2025-08-31 12:57:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| b7c0ad4c-2643-3b6d-b0f5-7851abd530eb | -14.80984 | -46.7451 | 2025-08-31 12:57:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 47660124-a40b-33de-8ffd-17abad29b7cc | -15.71568 | -48.9786 | 2025-08-31 12:57:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 113.8 |
| b00f9774-a2f8-309a-8fca-0940484cc2fa | -20.09753 | -50.5491 | 2025-08-31 12:57:00 | TERRA_M-T | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| fd197373-1d7b-3424-af15-d05266befbdf | -15.23903 | -56.07045 | 2025-08-31 12:57:00 | TERRA_M-T | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 571d9659-1745-3000-aaa3-ad622bc84544 | -23.3767 | -52.06883 | 2025-08-31 12:59:00 | TERRA_M-T | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 29.9 |
| cc7546b2-9716-36b5-b688-b3b2636130bf | -23.37079 | -52.09763 | 2025-08-31 12:59:00 | TERRA_M-T | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| fe6307f7-3127-3170-a96e-6b4291804978 | -22.26736 | -56.06689 | 2025-08-31 12:59:00 | TERRA_M-T | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 09f1d2b2-61ac-3356-b046-d3736df1667b | -22.26591 | -56.07843 | 2025-08-31 12:59:00 | TERRA_M-T | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5885ba90-d404-3d7a-a366-42e1c8089488 | -21.19947 | -51.7948 | 2025-08-31 12:59:00 | TERRA_M-T | PAULICÉIA | SÃO PAULO | Brasil | 3536406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 5826baae-a6a6-3096-8e07-f6d7b45df075 | -23.38406 | -52.09874 | 2025-08-31 12:59:00 | TERRA_M-T | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 723.4 |
| 41016d3b-ed5a-32e8-9e5f-8fc0863dd711 | -23.38773 | -52.0925 | 2025-08-31 12:59:00 | TERRA_M-T | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1030.1 |
| 59e87334-c8f9-30b3-bb45-7428d45c6862 | -23.38615 | -52.07619 | 2025-08-31 12:59:00 | TERRA_M-T | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 389.8 |
| 6013ac09-80ba-3dc7-851e-43702ed132e0 | -21.20169 | -51.77302 | 2025-08-31 12:59:00 | TERRA_M-T | PAULICÉIA | SÃO PAULO | Brasil | 3536406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.5 |
| 479cde17-a8f5-3ebd-90b8-ad2ed7f433dd | -22.00628 | -56.03554 | 2025-08-31 12:59:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9cf33485-ef67-3d94-99fc-1d029452605e | -22.00772 | -56.02409 | 2025-08-31 12:59:00 | TERRA_M-T | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 0a85d15b-598a-34ae-9bf0-ef3ec237ba0d | -22.25031 | -56.12381 | 2025-08-31 12:59:00 | TERRA_M-T | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 3e7c7bd5-0a49-330d-a13b-d76cbb5645a1 | -28.9232 | -50.87594 | 2025-08-31 12:59:00 | TERRA_M-T | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| aab3d69e-54ac-38df-8554-fd55c0fb5553 | -21.99794 | -56.0228 | 2025-08-31 12:59:00 | TERRA_M-T | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d7f94cd0-b758-33bb-af26-66f5de32401d | -23.08698 | -54.36686 | 2025-08-31 12:59:00 | TERRA_M-T | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 83e6a446-42a0-3dd7-8fe0-739953d44e36 | -23.37446 | -52.09143 | 2025-08-31 12:59:00 | TERRA_M-T | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 198.8 |
| 4a94b573-77b2-3c68-b30d-d5937324c6c6 | -23.38997 | -52.0701 | 2025-08-31 12:59:00 | TERRA_M-T | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 94.0 |
| e13f8eb2-6110-3a93-884c-5576f5ae10b7 | -22.25178 | -56.11207 | 2025-08-31 12:59:00 | TERRA_M-T | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e0f35938-c51d-3805-b6a1-be9072587c63 | -23.37222 | -52.11404 | 2025-08-31 12:59:00 | TERRA_M-T | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 4a11b625-0eb3-3ea0-a5ac-8ab1489518a9 | -20.38631 | -54.62819 | 2025-08-31 12:59:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 16.3 |
| de77ee5d-ad02-3d32-ac76-f8ed48079b41 | -14.5448 | -51.9943 | 2025-08-31 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 6de93ab1-0d49-351f-b702-f4fd65f8693b | -13.3443 | -46.953 | 2025-08-31 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| ffb7d64a-38a5-3410-bb51-0a5a6c028109 | -14.8013 | -46.7371 | 2025-08-31 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 311.3 |
| 96f27a57-f80b-3c3f-a5d9-91f3af0cc324 | -12.6298 | -48.1979 | 2025-08-31 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 262.0 |
| 12d9e453-e74f-3274-96b6-3aa90ba47946 | -7.4174 | -44.0749 | 2025-08-31 13:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f8f6d79c-8807-30a6-8398-7687d0b0832c | -11.0849 | -44.611 | 2025-08-31 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 55bae04e-f3ad-3918-abf8-1c09daf12b64 | -15.7098 | -48.9702 | 2025-08-31 13:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| cd970362-0b1d-3f28-8388-1b3ea78b01db | -9.2642 | -47.0582 | 2025-08-31 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| fa15dacf-b2c4-349e-9c64-286e50ad6955 | -7.8541 | -46.9747 | 2025-08-31 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 441.9 |
| 4c28be42-27cd-366e-9ee2-82b1cd89e1a6 | -11.8357 | -46.5194 | 2025-08-31 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 921c8403-5bff-38ad-bef7-e4ec13a7eba4 | -8.8939 | -45.094 | 2025-08-31 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 1fb8568e-f36b-3ba2-b104-d1dd842cdb67 | -15.7102 | -48.9479 | 2025-08-31 13:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 7fbcc224-2943-335c-a1b5-30a64e049e81 | -15.7107 | -48.9255 | 2025-08-31 13:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 07898743-7e01-3655-befc-55a8b040b19f | -8.294 | -46.3099 | 2025-08-31 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| c9703212-b208-3261-8ee2-b52307c1848b | -5.8884 | -42.9753 | 2025-08-31 13:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 276727c6-8240-35b7-9a4d-6cc4c05ebdea | -11.3116 | -43.6664 | 2025-08-31 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| bad04b79-5632-3d4b-88fa-e383c1b6efc8 | -7.8543 | -46.9525 | 2025-08-31 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 19e30c28-fd04-3179-a8d4-83b9b713b5d8 | -7.1139 | -44.3111 | 2025-08-31 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| a3b6699d-b168-3d06-bb04-ef7a1007bbb7 | -11.3701 | -43.6104 | 2025-08-31 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 194b31ea-ca5e-33c4-9a8c-f10777250774 | -5.4824 | -44.3969 | 2025-08-31 13:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e8cfc802-59b4-3c1d-b4c4-8ffbe9a960c1 | -14.8008 | -46.76 | 2025-08-31 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 4c205e0c-3ee9-3a24-b06d-76a0545ab8df | -11.3112 | -43.69 | 2025-08-31 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e0bb7d20-a8bc-3257-9413-0f8e5595b448 | -12.5571 | -44.8078 | 2025-08-31 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 67ce7c3f-75bd-3e80-9866-87bb5b2498e5 | -6.5021 | -43.5553 | 2025-08-31 13:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 3c9951f2-b74d-353e-b520-95da214cfc8e | -13.3636 | -46.95 | 2025-08-31 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ecd271af-c7ea-34df-a49d-ef78f2473dd4 | -9.245 | -47.0824 | 2025-08-31 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| b5702c7d-fa40-3585-a01f-a6721488cb28 | -5.8696 | -42.9768 | 2025-08-31 13:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 305.2 |
| 98379559-ca39-3ae6-997c-aec4449a456e | -11.3308 | -43.6635 | 2025-08-31 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 354.5 |
| 0681152a-faa8-3c1f-abb7-4ee336e34cdf | -8.875 | -45.0961 | 2025-08-31 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| c11e49cb-6c79-370d-adfb-91ccf135d03a | -11.8181 | -46.4314 | 2025-08-31 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| c034c3a8-a450-36de-acfe-dad041682e3d | -11.3509 | -43.6133 | 2025-08-31 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 87882124-928e-39a2-b0c2-f8d755555ef6 | -4.7346 | -44.4457 | 2025-08-31 13:00:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 258.2 |
| 4e906fe2-3bce-351e-bcd6-a4166ce21c61 | -12.5764 | -44.8047 | 2025-08-31 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| bcad323c-9143-3698-b206-245e50d00208 | -14.8208 | -46.7337 | 2025-08-31 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 53dcd644-8d10-33f3-8644-391169a5d91a | -6.5209 | -43.5537 | 2025-08-31 13:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| cd72f8b3-8510-3a40-960e-5f92a1ef6f4d | -12.6294 | -48.2201 | 2025-08-31 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 149de948-568c-343f-8927-0eac60d8684e | -11.3504 | -43.637 | 2025-08-31 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 403.4 |
| da5b214e-a1ae-3942-b889-2c6c08d0f35f | -7.4466 | -44.8079 | 2025-08-31 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 74abd095-a881-3a76-bf4b-3ba289606558 | -7.0951 | -44.3128 | 2025-08-31 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 0d61c461-1a99-3e42-9440-810287a3d8ce | -6.306 | -44.4036 | 2025-08-31 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c6802159-5fd6-3daf-b11f-79f3dd160a49 | -11.3312 | -43.6399 | 2025-08-31 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.0 |
| 9800a60b-aa75-376b-88ca-05c0ef71d527 | -11.3705 | -43.5868 | 2025-08-31 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| bce1f3fc-9759-323a-987e-337cbe191145 | -4.7346 | -44.4457 | 2025-08-31 13:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 503a8e2e-6899-3b2a-a3d7-f1307cb9d84c | -11.3116 | -43.6664 | 2025-08-31 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| ca38d9d2-45e0-3206-a63d-92b12be6447f | -12.3095 | -45.723 | 2025-08-31 13:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f7b47619-1a75-3bab-bfb8-a156596ab946 | -9.245 | -47.0824 | 2025-08-31 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 1c1850a9-b4db-3684-a43d-81e110e160ae | -7.8541 | -46.9747 | 2025-08-31 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 887.6 |
| b8f2be39-8d05-3eeb-806a-51adad3053c2 | -15.7102 | -48.9479 | 2025-08-31 13:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c7bdc0fd-18b6-35b6-bc17-f2ee0c26d37c | -6.2409 | -43.3911 | 2025-08-31 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4254d930-f9f0-3b97-9c03-02000e9add34 | -7.4466 | -44.8079 | 2025-08-31 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 0b2bd1d8-5b0c-3c89-acab-70a8be362ca5 | -11.8357 | -46.5194 | 2025-08-31 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 57f43186-142d-344b-93cf-60eb66aa5861 | -7.1139 | -44.3111 | 2025-08-31 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 1f01ec42-fad8-3af4-9b3c-94e4dd0fde0e | -14.0307 | -44.5814 | 2025-08-31 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f0986fba-6282-3a10-a3ee-530de29bd355 | -14.8208 | -46.7337 | 2025-08-31 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 57c808d6-b0f1-3670-a850-d36a8e9848a8 | -12.3287 | -45.7201 | 2025-08-31 13:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| f6dfeafd-c64f-3a71-ba94-01f3be1cdb6b | -6.5209 | -43.5537 | 2025-08-31 13:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 61ec55fb-c953-3434-9826-2825bd24ed74 | -7.4463 | -44.8307 | 2025-08-31 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 37708826-f487-33c7-8753-6696d46fcd2b | -5.8884 | -42.9753 | 2025-08-31 13:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 69dc61ea-7fd9-3445-baab-ede86a0cd6b5 | -11.0849 | -44.611 | 2025-08-31 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 97306765-eb29-3466-90c6-1ff56267485d | -15.7098 | -48.9702 | 2025-08-31 13:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 45f0a28d-5ae7-307b-9a53-806060b398fe | -5.4824 | -44.3969 | 2025-08-31 13:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 5d0694f8-7563-3039-805d-679b8246fa0a | -12.3099 | -45.7 | 2025-08-31 13:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| deaf3af4-f4df-3f79-a110-fdfca8c96424 | -12.6298 | -48.1979 | 2025-08-31 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 460.8 |
| 11ffebac-f210-3814-b2c5-34dd3ef9aa3d | -13.3636 | -46.95 | 2025-08-31 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ac88fa39-0005-3609-b1dd-02e4a687f116 | -7.0951 | -44.3128 | 2025-08-31 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 19643682-e694-3205-8cd6-99a43e396ede | -11.8181 | -46.4314 | 2025-08-31 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 204969d2-a854-3d79-9e7e-1c5404384336 | -12.5764 | -44.8047 | 2025-08-31 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b12a4813-5392-3e23-ae82-498826841440 | -5.8696 | -42.9768 | 2025-08-31 13:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 373.5 |
| 28533d60-bc04-398e-805b-9e74f0cc9c95 | -14.8013 | -46.7371 | 2025-08-31 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 09c753c7-4b4a-323f-bb86-cc75a91d92a4 | -11.3112 | -43.69 | 2025-08-31 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 130996f1-b5bf-3955-85e4-a8e8785e7b60 | -11.8361 | -46.4967 | 2025-08-31 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d72aa410-cb67-33e2-a364-5c28c68eeae5 | -12.6486 | -48.2175 | 2025-08-31 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a441e28d-db95-3826-8cce-420e46d29da4 | -12.6294 | -48.2201 | 2025-08-31 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 417.0 |
| db99ff0b-9d1c-3c56-a00d-c7c6411f12e5 | -15.7107 | -48.9255 | 2025-08-31 13:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |


[Clique aqui para ver as próximas entradas](README89.md)
