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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddaf1b6c-848b-3d25-9c8d-4b1955c746e2 | -19.0765 | -49.7432 | 2025-09-08 14:40:00 | GOES-19 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 124.0 |
| f2d71e26-8a98-3d8f-943c-55df996ec7c0 | -9.8087 | -53.3197 | 2025-09-08 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 2252c006-0f64-37f4-aed6-22c930898e2b | -9.8278 | -53.2976 | 2025-09-08 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 9dd0036d-2354-394c-8324-f42c44fbf89e | -5.8081 | -45.6448 | 2025-09-08 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d56522c8-fd77-3465-9827-e217bf79cf6c | -6.2036 | -43.3709 | 2025-09-08 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 0857ebee-29c3-3f2b-a230-163a93d24e13 | -7.522 | -48.2318 | 2025-09-08 14:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| be67db8b-5588-3436-944d-0086124a12c6 | -4.9013 | -42.2226 | 2025-09-08 14:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| ce10fe84-f4c0-39a1-a6c5-a63a5b8a3a3c | -9.978 | -51.6856 | 2025-09-08 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a8e2080c-26b5-3f25-a12d-00466c816ba5 | -8.3239 | -46.9533 | 2025-09-08 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 3949b141-827a-343c-b824-a55c09697f2b | -5.7765 | -40.9303 | 2025-09-08 14:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 181.4 |
| 2687e306-d400-3ab7-895d-6f25df8bea40 | -5.7725 | -45.4447 | 2025-09-08 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 3ff1fc33-9ebf-3a53-a634-7cc2d3a03035 | -11.2007 | -54.9992 | 2025-09-08 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 447d2df4-68bc-350c-a287-f04521e96153 | -9.4611 | -46.4566 | 2025-09-08 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 9821ab35-ac2d-361e-919d-d80e0b8b1374 | -16.9024 | -45.83 | 2025-09-08 14:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 35ce0df6-6415-383f-b4c6-074d5e3ccc77 | -6.4976 | -43.9963 | 2025-09-08 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c969efec-877b-350b-a522-60b0a24a37ef | -8.0592 | -45.4998 | 2025-09-08 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 541.9 |
| 2740bd70-dbe9-301d-a666-3cbf3e6eca16 | -5.6445 | -45.1146 | 2025-09-08 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 2a16e18a-4a24-3e3d-b5be-205ea91e2e08 | -9.4809 | -60.5095 | 2025-09-08 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 672079fb-0be6-31da-9759-f53301b7181c | -11.8827 | -50.7267 | 2025-09-08 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 144.9 |
| b2b83819-c873-35b0-b107-0f4c071d7b32 | -12.967 | -54.7705 | 2025-09-08 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 186.8 |
| af4c5469-630b-3818-89c6-36b4c3a8797d | -16.9416 | -45.8452 | 2025-09-08 14:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| f210cef9-ec8f-3e13-9ed3-73a5d6874faa | -11.4093 | -43.5573 | 2025-09-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| f8630835-87f7-3f12-9c3d-05d05a1ea789 | -9.8275 | -53.3181 | 2025-09-08 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| b316bff2-72ed-34b3-b971-d13474e8ad11 | -16.9615 | -45.8411 | 2025-09-08 14:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 671a3354-886f-36eb-8791-f9eacb7b9b08 | -5.9752 | -45.7677 | 2025-09-08 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 2f6dc24d-c0bf-3754-acb5-3d73f4d5d15e | -13.3178 | -51.7477 | 2025-09-08 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d960d27c-024a-3600-ab5e-56000a8e7e03 | -5.211 | -43.2833 | 2025-09-08 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 4922fdf6-1dd2-3b67-a46a-c4effcab4fa5 | -11.2005 | -55.0195 | 2025-09-08 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e45239e2-3575-32a7-809f-b5d64d4601fa | -5.938 | -45.7479 | 2025-09-08 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 340.0 |
| 56251728-0874-3b7c-952e-6c4e6dfdc318 | -6.3989 | -44.4878 | 2025-09-08 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f7fd0247-ab02-3ea3-ac0d-539fbaa1a130 | -5.9565 | -45.769 | 2025-09-08 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 189.6 |
| dddcfa39-58f5-3552-b6eb-480b2d9b0fa5 | -11.4089 | -43.581 | 2025-09-08 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 7f99da9e-0572-3852-b51b-6661469f07f4 | -10.7876 | -47.7279 | 2025-09-08 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 724c10f1-38f7-301c-b450-098aabb2c984 | -5.4532 | -43.4292 | 2025-09-08 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 44171302-bbc2-3321-af94-fcd8d3f360cb | -7.7296 | -44.735 | 2025-09-08 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9ecd4d9f-57c6-3633-ba94-8443bd5fbf9b | -8.3179 | -47.4621 | 2025-09-08 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| fde36e83-82e0-3fb6-b625-61d4ee270821 | -12.8651 | -62.1074 | 2025-09-08 14:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 06a53575-7ef5-3aa5-a4da-185d69f7917c | -12.6343 | -56.9725 | 2025-09-08 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 57b15bb7-6800-3e0e-b7cb-f6b3eaa2e61d | -15.758 | -53.548 | 2025-09-08 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 4b730058-f4be-3413-9a6f-7a846294651c | -9.9971 | -51.6629 | 2025-09-08 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| c46e81d1-6826-3be8-b3ec-6f5e19ec973d | -12.9289 | -54.7744 | 2025-09-08 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| c452b2bb-8c34-3687-af54-09c527e645e7 | -12.1988 | -53.9024 | 2025-09-08 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 92806b21-4f6a-3c7c-97dd-fe2ac12f90e2 | -6.1904 | -40.9668 | 2025-09-08 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| ffae9b66-2217-3a4e-a176-5fba8cf989cc | -15.044 | -50.1118 | 2025-09-08 14:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 1eaba690-8e25-3cf9-9090-4167e00ec566 | -16.9422 | -45.8217 | 2025-09-08 14:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 3b9a35ce-0ed7-3e32-af8a-b77385f9bbe9 | -15.1435 | -48.0594 | 2025-09-08 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 5d3e5e98-e83a-33cc-beac-706c138e1afa | -5.9567 | -45.7465 | 2025-09-08 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 26dd4af6-ea98-3f81-b389-c7cf192271e1 | -9.9251 | -49.8898 | 2025-09-08 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 402b1ab9-6819-3cf7-8131-f5723908df52 | -12.9482 | -54.7519 | 2025-09-08 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 145.1 |
| df8a52af-69b1-3d4c-8707-f758741f7d96 | -5.7912 | -45.4433 | 2025-09-08 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 162.1 |
| dd626155-0811-35a6-b0eb-c3d88b8f490b | -12.1319 | -50.6121 | 2025-09-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 887d1785-f9cd-3ead-b307-12c2e10cfcaa | -12.9477 | -54.793 | 2025-09-08 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 3bfa70cc-7eb4-37ee-84ce-9d8e2a386111 | -11.864 | -50.7075 | 2025-09-08 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| f295487d-b088-3dfa-9581-17f8d60ce3f3 | -14.5648 | -53.0925 | 2025-09-08 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b591645c-cb3f-35ca-94f3-4d12776a613d | -9.9969 | -51.6839 | 2025-09-08 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| cb95dfbf-e9f0-32f7-9fb5-b5b7f1ce0b6a | -15.2302 | -53.7641 | 2025-09-08 14:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b3674449-ef11-3cd2-b35f-6842ba0f60bc | -9.4621 | -60.5297 | 2025-09-08 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |


