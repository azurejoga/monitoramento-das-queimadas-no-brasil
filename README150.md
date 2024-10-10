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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44c27e56-cf25-37cc-a97e-0953f2413408 | -11.29 | -51.0059 | 2024-10-10 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| e7174fa3-2a1d-3945-a1d0-119a4c548ba2 | -11.309 | -51.0038 | 2024-10-10 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 33824aae-e19b-39fa-8b93-09c3426c3265 | -11.2894 | -51.0484 | 2024-10-10 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 606aea82-6c5a-3999-a55b-8316d06a1053 | -11.3087 | -51.0251 | 2024-10-10 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 191.7 |
| c49ff3c0-6e3f-30bf-b5f0-b9ed33dcd105 | -11.7745 | -44.5568 | 2024-10-10 13:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 71ee7ec7-3a61-3d1c-a9f8-022277bb9d76 | -11.7749 | -44.5335 | 2024-10-10 13:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 5469cb00-efff-3355-9def-028e4128ddb9 | -12.0718 | -50.8116 | 2024-10-10 13:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| fade1b1e-dedb-3d6d-b322-ba6feb8eb1ad | -12.1895 | -50.5838 | 2024-10-10 13:06:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 8cd545be-9fb9-3fdd-aeac-38e524f6e418 | -12.1274 | -50.9118 | 2024-10-10 13:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 0e67269d-c380-324c-83a8-b38bba1374bc | -12.1277 | -50.8904 | 2024-10-10 13:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b94c8fd1-fa3a-381b-9cc9-2ef670590a17 | -12.1086 | -50.8926 | 2024-10-10 13:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 5095b405-c990-3b22-8ca9-9b28a1a53601 | -12.1892 | -50.6053 | 2024-10-10 13:06:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| e83e0375-9e18-3537-8bb4-aed36e40b201 | -12.1523 | -50.524 | 2024-10-10 13:06:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e9a00e84-ee7f-3b11-90b5-d6b2c90007c2 | -12.0714 | -50.833 | 2024-10-10 13:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 80883205-a551-3ce0-904b-7dc109ecc3fd | -12.8902 | -53.4569 | 2024-10-10 13:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 2efd30f8-a6b7-3594-8caf-0c3982d48d86 | -12.8202 | -50.5495 | 2024-10-10 13:06:19 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 4b181873-9c38-3db5-96c3-989a4b12d79a | -13.8774 | -44.4914 | 2024-10-10 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 099782a9-3dea-3e3a-bb09-2b88f0cdfbeb | -13.8769 | -44.515 | 2024-10-10 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 56474520-7fcd-3929-bb5b-f5fddacd65c9 | -13.8579 | -44.4949 | 2024-10-10 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| a6118ea1-e351-3511-a80f-f1dd3d415648 | -8.6305 | -46.5001 | 2024-10-10 13:15:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 43cae385-4d67-39b4-929f-22e714cb514a | -9.2536 | -46.4346 | 2024-10-10 13:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 1497fdc1-8542-306b-a155-e36aa46569f5 | -9.3064 | -45.3441 | 2024-10-10 13:15:59 | GOES-16 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| b352860d-2338-3a0d-aaae-a13455963728 | -9.3067 | -45.3212 | 2024-10-10 13:15:59 | GOES-16 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 31337691-c27d-3b63-93ab-11bdb5ebc72b | -9.5655 | -44.441 | 2024-10-10 13:16:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 9d2eee02-591a-39e1-bf59-7d7dd9bc1f0e | -9.5659 | -44.4178 | 2024-10-10 13:16:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 292.0 |
| c1379788-5a60-377c-bf3b-eaa07cbdd69e | -9.657 | -51.7984 | 2024-10-10 13:16:01 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| d704343e-0fb8-3fda-b2b7-ebf6603f6725 | -10.2048 | -42.4744 | 2024-10-10 13:16:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 328cdf19-7db3-3bf0-b683-6ebe2ecb04bf | -10.3116 | -53.7085 | 2024-10-10 13:16:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 229.6 |
| c4161cd5-5d7c-34d8-9823-3085e7fba637 | -10.6041 | -47.3065 | 2024-10-10 13:16:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| ad75cc11-728c-3db6-98ac-c0557970a804 | -11.2894 | -51.0484 | 2024-10-10 13:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 139.7 |
| ce1b65db-f20b-338a-94b8-8dbaf0c2b8d3 | -11.29 | -51.0059 | 2024-10-10 13:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| da88d8cf-73b7-31c8-92a4-32a6ce616ec8 | -11.3084 | -51.0464 | 2024-10-10 13:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 139081ed-f088-308f-96ec-c8e2894f5621 | -11.3087 | -51.0251 | 2024-10-10 13:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 226.7 |
| f9265095-e0be-395e-88ed-7a519c65af6b | -11.309 | -51.0038 | 2024-10-10 13:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 177.9 |
| fb7265d4-4ec3-31c7-a1a6-7f90797ab309 | -11.7745 | -44.5568 | 2024-10-10 13:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 34cd2026-9a50-37da-bd72-5ba77ac3d09a | -11.7749 | -44.5335 | 2024-10-10 13:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 78326dbe-16c2-3630-a1b9-b2cc4d3c6912 | -12.0714 | -50.833 | 2024-10-10 13:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| cab6972a-7dde-39d1-85c8-fbd9864437a9 | -12.0718 | -50.8116 | 2024-10-10 13:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 153.9 |
| aca4c1df-2099-3fc2-b5db-f91516717d9b | -12.1059 | -48.6428 | 2024-10-10 13:16:15 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 4c075040-769b-332f-af6e-2220ecb9b7b1 | -12.9919 | -46.2359 | 2024-10-10 13:16:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 4db770a0-50cc-3179-8321-ca9b709b1b52 | -12.8902 | -53.4569 | 2024-10-10 13:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 8de76442-8d02-3b91-bb16-92ab98055e3b | -13.8774 | -44.4914 | 2024-10-10 13:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 9567423a-71ca-3991-9576-b497a3695746 | -13.9353 | -44.5046 | 2024-10-10 13:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 32f6882d-009c-345c-b831-501589306840 | -13.8963 | -44.5116 | 2024-10-10 13:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| b9a9f2dc-f647-3142-bbe7-8c4d9bc30ccb | -11.26 | -44.26 | 2024-10-10 14:04:19 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 450b40e5-37d2-3576-9097-e7ce1da3cb06 | -11.26 | -44.22 | 2024-10-10 14:04:19 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dc47c96c-172e-3b0f-90e1-6698cce743d2 | -11.29 | -44.27 | 2024-10-10 14:04:19 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e8d3768-12d9-3fcd-aac9-2460c00ae827 | -11.29 | -44.23 | 2024-10-10 14:04:19 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74e5126e-0787-3f2f-a8af-778ff6a5f29e | -8.64 | -46.47 | 2024-10-10 14:04:37 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21834c79-1bb6-33c3-890a-f6940cc18443 | -2.1963 | -46.0644 | 2024-10-10 14:45:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| db9a873b-962f-3f67-b72b-50755fce1a94 | -2.1777 | -46.0648 | 2024-10-10 14:45:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 84.5 |
| fc50dd75-af38-365a-82cb-aff4e0c12190 | -2.1781 | -45.9313 | 2024-10-10 14:45:19 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| e8b5a88d-8e18-31b0-ae82-34459042d6fe | -2.7426 | -48.6889 | 2024-10-10 14:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 2e698914-e247-3d9d-8a2a-ddc51959b97c | -2.7591 | -49.2434 | 2024-10-10 14:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 2d710e50-ae19-3732-bae7-6a570211f187 | -3.4915 | -50.8004 | 2024-10-10 14:45:26 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d36d111e-277e-39c7-9141-0c51b509e98b | -3.7264 | -44.6595 | 2024-10-10 14:45:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 172.6 |
| 8c12972d-c43c-313c-8e69-c6f9badc64b2 | -3.7263 | -44.6822 | 2024-10-10 14:45:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 338.0 |
| d79969ee-4890-3d2a-a281-5c58623636ec | -3.7077 | -44.6831 | 2024-10-10 14:45:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 205.3 |
| 71cc2d4d-5bfe-36ec-9662-a60103ec9107 | -3.6746 | -51.1274 | 2024-10-10 14:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 575c7f8b-820f-3e95-8130-91eeb4abd42f | -3.9514 | -41.4706 | 2024-10-10 14:45:29 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 10d735c8-4756-327d-b26c-13c6a41ed1e8 | -3.9702 | -41.4695 | 2024-10-10 14:45:29 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| b0e9fb51-cb94-31ac-a981-e02802808585 | -4.0456 | -44.2555 | 2024-10-10 14:45:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| d1536b1a-b1ff-3b8d-8d05-e63283ca490f | -4.0961 | -48.2739 | 2024-10-10 14:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 2ac946f6-ccad-3333-b370-4ec877954284 | -4.0962 | -48.2523 | 2024-10-10 14:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 9ce665dc-2bb8-338d-b28d-b51ad6472e8b | -4.1471 | -43.0 | 2024-10-10 14:45:30 | GOES-16 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 8aadc375-0100-3e95-b758-98c6a1a97dc5 | -4.1146 | -48.2731 | 2024-10-10 14:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 257.0 |
| 50f52c4e-3b8d-3a85-96e7-89e2e8ab48e8 | -4.2871 | -44.4029 | 2024-10-10 14:45:31 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| c77a843c-74cd-3593-a9db-97ff2e8323e9 | -4.2873 | -44.38 | 2024-10-10 14:45:31 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 05777ba5-ada1-3eef-9efd-f28b5acc7254 | -4.3432 | -47.2844 | 2024-10-10 14:45:31 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1265db72-2767-3acf-bba1-b80c442877fe | -4.9049 | -46.6829 | 2024-10-10 14:45:34 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 41d4c627-b899-3580-b996-093be631bd4e | -5.0212 | -46.0544 | 2024-10-10 14:45:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 112.9 |
| ed6f3b26-bc9f-3d70-be5e-7a759fdfd87e | -5.2783 | -44.2045 | 2024-10-10 14:45:36 | GOES-16 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| b44abf9e-9a63-3f41-89e6-03082404d4da | -5.4326 | -45.8946 | 2024-10-10 14:45:37 | GOES-16 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 961ebb37-4486-3cf9-abef-78a295e9ab9e | -5.414 | -45.8958 | 2024-10-10 14:45:37 | GOES-16 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 718c953b-7f24-35c1-b97d-19d586914b77 | -5.4833 | -44.2822 | 2024-10-10 14:45:37 | GOES-16 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 28579138-b635-3b36-9002-6d889c3617b7 | -5.6948 | -43.6437 | 2024-10-10 14:45:39 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| b850a7a0-5850-39ab-a546-442c7f1c5b78 | -6.1138 | -44.9213 | 2024-10-10 14:45:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| afdaf227-1a49-3138-909e-4bcdea838e32 | -7.3944 | -46.1248 | 2024-10-10 14:45:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| ab71fd49-a1f7-382b-9ca4-f0bd88948e06 | -7.6155 | -44.8376 | 2024-10-10 14:45:49 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 90eb1e64-0416-3bb5-9fdc-96442bd5bbdb | -7.6343 | -44.8358 | 2024-10-10 14:45:49 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 087a55c3-ffdc-3163-aab6-c4422f96099c | -7.7597 | -47.0274 | 2024-10-10 14:45:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 42a9e952-18db-3445-b71e-ca9f62cdec71 | -7.8027 | -44.9108 | 2024-10-10 14:45:50 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 4c78e781-e4bc-3424-bf5b-046e20715e8e | -7.9164 | -44.8539 | 2024-10-10 14:45:51 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| c377b24c-728a-3652-b855-0d7ca4e6dbbd | -7.9352 | -44.852 | 2024-10-10 14:45:51 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 4cf600f2-29d8-3883-943f-7fc121978718 | -8.1478 | -44.4171 | 2024-10-10 14:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| aea8e33d-6c05-32f8-9b9a-e73ee90e33bd | -8.0678 | -44.7929 | 2024-10-10 14:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6598284c-638b-3087-8f2f-20b24eedaf0d | -7.9639 | -54.7764 | 2024-10-10 14:45:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 3e9306ee-ce34-3def-9320-1688caa49be4 | -8.1667 | -44.4152 | 2024-10-10 14:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 53a1839c-4f57-3807-964b-78e17c075314 | -8.2203 | -55.2427 | 2024-10-10 14:45:53 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 7605fdfc-984e-3957-ae55-7515045b73ba | -8.2842 | -44.0792 | 2024-10-10 14:45:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4a9086e2-3bb6-3d2d-af80-cb39d74ffcb2 | -8.3217 | -44.0983 | 2024-10-10 14:45:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 21c4f5a1-7fd9-361f-94b0-735db478ade5 | -8.3406 | -44.0963 | 2024-10-10 14:45:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 9e948b42-dcf3-311e-942a-9c6afb9e0d06 | -8.1878 | -47.342 | 2024-10-10 14:45:53 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| dd1b330b-a04e-395a-a44a-a77e3778e547 | -8.4816 | -55.1657 | 2024-10-10 14:45:55 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 078f30fd-c36e-37f3-8732-6ccaa5349da1 | -8.5003 | -55.1645 | 2024-10-10 14:45:55 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 6abe9450-b74c-3f9f-901b-79231c525990 | -8.5004 | -55.1444 | 2024-10-10 14:45:55 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 44c10e5b-f23d-32ba-a5c8-f1b37b219b2e | -8.5304 | -45.4746 | 2024-10-10 14:45:55 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| cfed2313-6441-33fe-b8a1-1499944ab22a | -8.9674 | -45.2456 | 2024-10-10 14:45:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| cad4a3a2-62de-3cbd-ae6e-f9edc89e01ec | -9.1221 | -61.276 | 2024-10-10 14:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 35dd5670-80d3-3d60-b501-c42785550601 | -9.8709 | -48.2719 | 2024-10-10 14:46:02 | GOES-16 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |


[Clique aqui para ver as próximas entradas](README151.md)
