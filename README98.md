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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08877978-cfaf-3850-833e-7d1320262bf4 | -11.9986 | -47.0596 | 2025-09-28 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 923edc5e-8eb0-3d40-8c80-52b274e83c4d | -14.7846 | -45.7051 | 2025-09-28 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 77895962-cc1b-32aa-ac71-c46e031f6d80 | -9.2824 | -45.7104 | 2025-09-28 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 945d0ea9-bc93-3239-ad64-a49865a8b1d2 | -11.9828 | -47.9976 | 2025-09-28 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 810d9921-7011-38da-9453-d787c879807f | -9.0913 | -45.8673 | 2025-09-28 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| c487c215-55cd-3bcc-9ad6-45812564a5c0 | -11.4409 | -45.0229 | 2025-09-28 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 73424879-de52-36ce-955f-15d446771db0 | -11.3892 | -46.9622 | 2025-09-28 13:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 55852e83-1944-362e-ae50-43ffc58f463a | -11.3889 | -46.9847 | 2025-09-28 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| d57df7ab-3044-3a19-b1f3-64eb5a149c5e | -5.9004 | -43.6976 | 2025-09-28 13:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1fd3a664-1c5c-3400-ae50-ab854a7e8592 | -11.4604 | -44.997 | 2025-09-28 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 1f3981da-0f83-31e8-bff2-5d56633573c2 | -12.791 | -47.7533 | 2025-09-28 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 93b101bc-f9dc-363f-a75b-3e070659775a | -11.9982 | -47.0821 | 2025-09-28 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 7b1bda83-f05e-3677-88d8-2305f2cd148e | -12.2335 | -46.7568 | 2025-09-28 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| d8e20e06-271e-3255-bd09-50e1d4391abb | -8.2668 | -45.4564 | 2025-09-28 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| aa312cd0-502e-3376-8457-45c9d36b6a3f | -6.6192 | -44.9493 | 2025-09-28 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 95d5fc06-18f2-30db-894d-143f9f42b6f4 | -7.7555 | -45.7324 | 2025-09-28 13:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 32aee0cf-67d1-3cc9-be7a-d999e8f75c21 | -9.9581 | -43.5987 | 2025-09-28 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 39c490a5-3daf-3b77-970f-a7cc8d868751 | -8.8759 | -45.0274 | 2025-09-28 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| ee899342-4e30-325c-b673-caa0bf429db0 | -11.9824 | -48.0197 | 2025-09-28 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| ffc2883c-ce4f-38b6-9254-c0206294f00b | -7.7414 | -46.9848 | 2025-09-28 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 8ce83c7c-ff96-3138-af20-2fb91340c57b | -11.9633 | -48.0223 | 2025-09-28 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 70035b09-1fc4-37d4-9ba5-4d543e7b9379 | -11.4217 | -45.0257 | 2025-09-28 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ec7e3ec8-a4de-35e6-aab9-b805baae401e | -7.8823 | -44.5594 | 2025-09-28 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 3f2c398d-2a49-3f75-b040-817d23c95f7f | -12.9156 | -45.1912 | 2025-09-28 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e87c535d-82ac-3bf0-b708-18ae4a24b946 | -7.3847 | -47.0378 | 2025-09-28 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 296.1 |
| 5efbb317-b86e-36e1-a053-adf8c3461ba3 | -13.2966 | -50.7036 | 2025-09-28 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 217cd9d5-2382-363c-8594-b8dade2c7599 | -7.7972 | -47.0241 | 2025-09-28 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 798084dd-a0e7-383e-9c1b-d89bdd97a567 | -7.7604 | -46.961 | 2025-09-28 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 619ca27f-ec41-30ba-8147-e249c6f1eb38 | -11.979 | -47.0847 | 2025-09-28 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 5f7cb99e-cae1-36e2-95c7-3057aff5460d | -7.7785 | -47.0258 | 2025-09-28 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 8ecf2548-8b1e-38a8-ac82-1a7204a9c614 | -7.3849 | -47.0157 | 2025-09-28 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| f4b72a7b-5b87-347a-a5b5-d85edef7843d | -6.6002 | -44.9736 | 2025-09-28 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| cae4e904-38dc-307d-93e4-95f20c12243b | -6.6005 | -44.9509 | 2025-09-28 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| bf0ebdd4-cba1-343f-95b8-273a57f57465 | -15.9076 | -46.2139 | 2025-09-28 13:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 2d1a1e7b-5aee-3ce3-98cf-c46f51110590 | -18.1977 | -53.3208 | 2025-09-28 13:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 7e767286-61ba-3a24-a1f8-5fe68a4a20d2 | -7.7602 | -46.9831 | 2025-09-28 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| db954951-934a-3050-ae13-2050f3a85ae8 | -7.3659 | -47.0394 | 2025-09-28 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 5cfae889-dbde-3403-844c-ba4628101c57 | -7.3661 | -47.0173 | 2025-09-28 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5def340e-4a55-3bd0-a3cd-cdff8475228b | -11.4413 | -44.9998 | 2025-09-28 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| cc7d9bea-4154-3eee-b429-06d3f8629505 | -8.8226 | -46.2115 | 2025-09-28 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 272.6 |
| 52671553-ecf4-302c-b0ce-0dca94e1addf | -11.4083 | -46.9597 | 2025-09-28 13:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 62a4ac54-4268-3333-9448-81f77ea60c73 | -7.7782 | -47.0479 | 2025-09-28 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 880b6d68-7e8e-3d54-b3e4-083986048036 | -15.8879 | -46.2177 | 2025-09-28 13:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 81.8 |
| eaca836e-3b32-3228-8652-2c392937c178 | -12.2825 | -44.0804 | 2025-09-28 13:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 1d25f9f6-fe22-3465-ae20-404da63fb05e | -12.0218 | -47.9481 | 2025-09-28 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 93251e29-7932-3d72-bf1f-38afa4882d52 | -7.882 | -44.5824 | 2025-09-28 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f80767cf-697f-374c-9913-c6c761520c09 | -14.5535 | -48.4014 | 2025-09-28 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0c40437e-33eb-3fa3-853d-206b447626bb | -15.9076 | -46.2139 | 2025-09-28 13:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 5baae1e6-6858-37f3-af72-b4f499263a90 | -12.0218 | -47.9481 | 2025-09-28 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 67dc23d5-d93c-3ebf-ac57-233b869b03ce | -7.3661 | -47.0173 | 2025-09-28 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d1a26ed4-ac5b-379f-b836-b32fc38038b9 | -12.791 | -47.7533 | 2025-09-28 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 277.3 |
| 96262d5d-8641-3cb8-bc36-b70658c7ab98 | -7.7412 | -47.007 | 2025-09-28 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0128cb44-2068-3f99-8d4b-bf0d4a62a703 | -5.7583 | -42.8447 | 2025-09-28 13:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 48244138-b6e4-39a4-8b45-e81a73a47f0e | -9.9585 | -43.5752 | 2025-09-28 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 99091429-89af-315c-af82-87a711d44914 | -18.1977 | -53.3208 | 2025-09-28 13:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 597f3a3b-41f2-34bd-939c-8ecd4eb86091 | -5.9006 | -43.6744 | 2025-09-28 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| bc1e4128-77a0-343f-8abc-ec550207f838 | -6.6002 | -44.9736 | 2025-09-28 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 705ce5da-d379-337a-b702-78487eb8e115 | -12.9156 | -45.1912 | 2025-09-28 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 8ca691c7-f71b-36c8-9fb9-fe32838071cf | -6.619 | -44.9721 | 2025-09-28 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| d02b66d3-8f8c-3d3f-bd7f-91a7c527bc29 | -7.7972 | -47.0241 | 2025-09-28 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c07133db-2f23-3cf6-aa55-12e654532c60 | -7.8823 | -44.5594 | 2025-09-28 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| c323a385-b82a-3e71-9134-cd30ced4c5c9 | -9.9581 | -43.5987 | 2025-09-28 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 763efc24-a9a5-35a7-b962-f6949e4bddb2 | -11.4604 | -44.997 | 2025-09-28 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 5e2e142e-2029-312a-895f-81864af2e89d | -11.9824 | -48.0197 | 2025-09-28 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 153898fe-9661-3811-974f-716cd5ac959b | -15.8873 | -46.2409 | 2025-09-28 13:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 66.2 |
| eb6b36c6-a80f-356e-8bce-03da31d2fb89 | -18.1778 | -53.3239 | 2025-09-28 13:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 933f33c2-0e70-3f14-8d4a-887ddaba4886 | -7.7604 | -46.961 | 2025-09-28 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 1d7096f1-b579-343c-a8bb-5fd8f2255eb5 | -13.011 | -49.4423 | 2025-09-28 13:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 6c10af8d-9b59-38b9-96e5-6e6f9684873d | -11.9986 | -47.0596 | 2025-09-28 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| fd63f169-a408-3893-a647-102a9ffbfb5d | -7.2216 | -44.7601 | 2025-09-28 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| aa64a8b3-d3ef-3642-b5f8-89add637166b | -11.3889 | -46.9847 | 2025-09-28 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| acd2bedc-aaf2-3e0d-a252-dbc77aac4a62 | -7.7555 | -45.7324 | 2025-09-28 13:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 918fc4b9-bb2e-304e-abd8-01a271a8c6cd | -12.9363 | -45.1184 | 2025-09-28 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 771d43a2-c53c-3a55-9bfa-db1bbdc84b91 | -8.8226 | -46.2115 | 2025-09-28 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| d9a7d7c0-b664-3514-a270-f3beb2a34fa1 | -5.7396 | -42.8461 | 2025-09-28 13:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| dbfb88b3-4608-3a20-a782-2a5e02f8966a | -7.816 | -47.0224 | 2025-09-28 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 481a2fd6-93e2-3fd1-a995-3ffa0e4eddea | -8.9185 | -46.0889 | 2025-09-28 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d2ad0926-53b9-3347-bd58-847cd7f7209d | -11.9982 | -47.0821 | 2025-09-28 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3b73d335-075f-3229-b3bd-b2297e559c79 | -11.4217 | -45.0257 | 2025-09-28 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| ee94be49-f198-3f53-a4de-bc6c8821c2a1 | -11.4083 | -46.9597 | 2025-09-28 13:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 240.6 |
| 8ea1d76a-b529-391f-a2a0-34be20f9c6f2 | -11.979 | -47.0847 | 2025-09-28 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 331702e4-9e38-3fa2-97dd-49f455f66400 | -7.7782 | -47.0479 | 2025-09-28 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| cc28f053-969a-38a9-962d-7d8ea8601b0b | -7.8634 | -44.5612 | 2025-09-28 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4f2272e7-90ed-3f5f-bb3d-418b4210af5e | -15.8879 | -46.2177 | 2025-09-28 13:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 104.8 |
| dc04034c-db5e-327c-af4f-ac38363d8ee2 | -9.9578 | -43.6222 | 2025-09-28 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| dd434a1b-84b9-34ab-a601-c0e3720976e7 | -11.9456 | -47.936 | 2025-09-28 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 1a510d58-8cac-370b-a7bb-3b2dbe396d32 | -5.9004 | -43.6976 | 2025-09-28 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 7c36e5dc-0911-31e7-9875-6827f58adcaa | -8.8759 | -45.0274 | 2025-09-28 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 5ac0c9b0-c9ca-3dce-9355-b6fdc51a20fd | -7.3849 | -47.0157 | 2025-09-28 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| a0f271a7-7ea7-3388-a4af-15dac96777b8 | -7.7602 | -46.9831 | 2025-09-28 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 672cc1d8-5caf-3643-9387-acf9f7e9a9ec | -11.4409 | -45.0229 | 2025-09-28 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 2ada3a8f-25ef-38ec-99c4-cac11b23581b | -12.0214 | -47.9703 | 2025-09-28 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| f2b21711-4f74-3831-92f7-9fccbd7c99bf | -8.1611 | -46.4122 | 2025-09-28 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| b961b0b5-ad67-3f99-87e2-dc09b5146fe1 | -11.4413 | -44.9998 | 2025-09-28 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| eadd1a8e-9164-3a06-9a7e-f2c474d7d464 | -11.9633 | -48.0223 | 2025-09-28 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 036ca3b7-9ef5-3fb3-aa7c-5a3cad60740e | -7.3659 | -47.0394 | 2025-09-28 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 3f7d17a6-43bf-3723-a9c4-6d5cfba28957 | -7.7414 | -46.9848 | 2025-09-28 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 1241e5a5-c432-322d-a6c2-833da01c42e0 | -7.7785 | -47.0258 | 2025-09-28 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 1cb9e613-a816-303c-bd3e-a9848036878c | -7.1571 | -45.5158 | 2025-09-28 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 1a9f3732-8ca2-3835-abb4-8188a5949832 | -9.2824 | -45.7104 | 2025-09-28 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |


[Clique aqui para ver as próximas entradas](README99.md)
