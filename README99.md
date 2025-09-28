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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aeddcafb-e1b7-3741-91c2-a66300e4bc7e | -6.6005 | -44.9509 | 2025-09-28 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 178.6 |
| f451d287-5068-3cb1-949e-ed1f5ea01e75 | -14.885 | -45.5708 | 2025-09-28 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 754df6ab-fe59-32c3-931f-2efe64314c71 | -11.9644 | -47.9557 | 2025-09-28 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| b9fa8fce-543a-383c-a995-58e69a8746d0 | -11.9794 | -47.0622 | 2025-09-28 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b7b00ba3-eb86-3c0e-9501-c8760e53f720 | -11.3892 | -46.9622 | 2025-09-28 13:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 4b69a23e-a9a8-3745-9f1c-c007e55f76fa | -6.6192 | -44.9493 | 2025-09-28 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| a343e967-f494-3022-8586-58cbe741d828 | -14.7846 | -45.7051 | 2025-09-28 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| f723ab06-256c-3ed5-add2-31839f49e357 | -12.9547 | -45.1618 | 2025-09-28 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4ef9bf47-6cb7-370b-8622-c887d2ff3584 | -9.9585 | -43.5752 | 2025-09-28 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| d8fe306c-257c-3b27-a463-4c60731af659 | -9.3013 | -45.7082 | 2025-09-28 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.6 |
| a6a73b26-cefc-3518-8c89-5a937f504632 | -11.3654 | -44.9645 | 2025-09-28 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 96d861e9-c32f-3667-8f4e-7a1118b53166 | -6.6192 | -44.9493 | 2025-09-28 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4ca87cae-e91a-35e1-aca9-bc41b2db3d5f | -12.0214 | -47.9703 | 2025-09-28 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| b00f27c5-8e2a-3a40-8856-c6226056551c | -7.7555 | -45.7324 | 2025-09-28 13:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 53b51d81-181a-3878-a5c5-d5002e167094 | -7.3849 | -47.0157 | 2025-09-28 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 9ccc70de-01a3-3088-a032-ecc65b3fa0fc | -11.4083 | -46.9597 | 2025-09-28 13:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| ceee71c1-a7de-3cda-94a1-eb14a91cf2bb | -7.2216 | -44.7601 | 2025-09-28 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 57393637-395c-3b16-ba39-e9785c2a8ce3 | -9.4266 | -47.6163 | 2025-09-28 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 0e775893-cff0-302d-bd41-6f85ba3ff603 | -9.9581 | -43.5987 | 2025-09-28 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 5a5ecd05-2d55-33c4-8ea3-e0e0f4a9cef1 | -5.9004 | -43.6976 | 2025-09-28 13:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 3841412c-1eb5-354b-b536-ce27caf7c87b | -12.791 | -47.7533 | 2025-09-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| df0cde1b-e783-37f9-a4a2-bfc75df142e2 | -8.8415 | -46.2095 | 2025-09-28 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ca1f683b-94d7-318b-97ca-2a5b4b6905c6 | -5.3057 | -43.1599 | 2025-09-28 13:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 83681b63-5b20-3f4c-b44b-ca37ecc8ad0f | -6.6005 | -44.9509 | 2025-09-28 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| e8b44947-58a3-3317-80b0-972f33b5f0f5 | -9.2824 | -45.7104 | 2025-09-28 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6a094c07-b9dd-3a02-9853-bb65e8b2c347 | -14.5336 | -48.4268 | 2025-09-28 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 136.0 |
| c2a80ec2-d3e1-3b3e-8348-76950cfe722c | -7.7412 | -47.007 | 2025-09-28 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 5893795c-14af-396c-a4e9-8aca9dad03f2 | -6.3154 | -43.4548 | 2025-09-28 13:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 588bdcc7-2a10-3926-9abc-0491140d2f3a | -11.3658 | -44.9413 | 2025-09-28 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 67ae3434-d5d8-35e5-b65a-172b3cf275dd | -11.9633 | -48.0223 | 2025-09-28 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 009bf349-534c-35cf-9076-59decd1ddd64 | -7.3661 | -47.0173 | 2025-09-28 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 26202807-a022-390f-8757-9ec5274688a2 | -8.1611 | -46.4122 | 2025-09-28 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 3f4990fe-6537-3e69-858e-bcc06264b5ba | -14.885 | -45.5708 | 2025-09-28 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| c94a4be1-e8cb-3223-8324-8aa76e616a16 | -7.8823 | -44.5594 | 2025-09-28 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| a16ef686-21dd-3545-b003-1efc78c15294 | -7.7782 | -47.0479 | 2025-09-28 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 13ad1149-789a-3d82-a013-34c318a5d475 | -12.9552 | -45.1385 | 2025-09-28 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 92cad387-9e1c-3156-9598-d88699e9942e | -15.9076 | -46.2139 | 2025-09-28 13:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 156.2 |
| c7bbf121-27bb-3414-b1fc-d760d5b676e9 | -5.6273 | -44.9343 | 2025-09-28 13:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 68ed0f89-2913-3503-87b4-1adb1cc6d292 | -12.9363 | -45.1184 | 2025-09-28 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 6265b271-0f78-39e9-b88e-8e11f6704613 | -6.6002 | -44.9736 | 2025-09-28 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| d1b2df2d-7bdd-3f55-93d0-1f293198e0ad | -14.534 | -48.4045 | 2025-09-28 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2edd2662-bade-3ae7-af40-7dba36fcc7e5 | -13.6122 | -48.0787 | 2025-09-28 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3cf776d2-b1d3-3c39-89c4-21ddae2b2fd0 | -15.8879 | -46.2177 | 2025-09-28 13:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 135.4 |
| a0e33c0d-7c21-3c77-b54a-f5a76bee834b | -11.9456 | -47.936 | 2025-09-28 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 59a32f9c-b971-3fa9-824c-2ba2fae73fee | -14.5535 | -48.4014 | 2025-09-28 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| bc2d46e3-58fe-3cd9-9c34-47d5e13e3a36 | -8.2668 | -45.4564 | 2025-09-28 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 276202c4-ddeb-3d09-a8a3-d77c5397df7a | -9.9578 | -43.6222 | 2025-09-28 13:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e303a861-3969-359a-989b-ed8b18e2e2eb | -12.9156 | -45.1912 | 2025-09-28 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| b2119c93-79b2-3244-9bdb-a793968f12b4 | -11.9824 | -48.0197 | 2025-09-28 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 53061f54-c8f5-3593-8071-897520ec1585 | -9.4455 | -47.6144 | 2025-09-28 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| cd76509b-ee38-3db8-8047-82a015a14282 | -15.8873 | -46.2409 | 2025-09-28 13:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 8c1d265d-1932-31ec-b488-0aaedded1b32 | -13.011 | -49.4423 | 2025-09-28 13:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 4a487c9f-a6a3-3ce4-89e6-875bf22ef4bb | -13.77 | -47.8987 | 2025-09-28 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 31ca3e4d-3af9-3acd-8d58-ce50cdfeb422 | -11.4217 | -45.0257 | 2025-09-28 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 7480fff1-ede7-3290-b682-7115520d51e8 | -11.3889 | -46.9847 | 2025-09-28 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 24a398c2-8303-3378-a4ae-603d9c5852a0 | -8.8759 | -45.0274 | 2025-09-28 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 02358c74-261c-3a4d-8bf9-c8a081d8a4a1 | -11.4413 | -44.9998 | 2025-09-28 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 4e29b3a5-1a70-303d-b7f1-8f000c3f0531 | -7.1571 | -45.5158 | 2025-09-28 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ea418f48-193f-312e-8aa1-26309684c5f5 | -5.1885 | -43.7495 | 2025-09-28 13:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 64c47556-579b-39f6-b565-4e8e0532b7e8 | -5.6461 | -44.933 | 2025-09-28 13:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4793552f-7a51-3ec9-9cfd-7e2b41440086 | -11.4409 | -45.0229 | 2025-09-28 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 33e96b16-7546-3865-a33c-664a55fa2dae | -5.7583 | -42.8447 | 2025-09-28 13:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 9f32df33-a515-3188-9c02-71f3ae16487e | -8.9185 | -46.0889 | 2025-09-28 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d6ffa1a5-39cf-3623-971a-6fd46fd0524e | -5.7396 | -42.8461 | 2025-09-28 13:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 5f2c9300-636b-3879-92df-1e63eecc1c8a | -13.7893 | -47.8957 | 2025-09-28 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| d70d2347-0417-391a-a524-75996ac7835b | -14.8845 | -45.5941 | 2025-09-28 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 2d9da362-e71c-3834-8b3c-9244af8a00c0 | -8.2856 | -45.4545 | 2025-09-28 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 696104b4-110c-3c7a-8e09-669effec0160 | -11.3642 | -45.0339 | 2025-09-28 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 56553a19-325a-3496-930b-e3f11fb13453 | -7.3659 | -47.0394 | 2025-09-28 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 0f8c3a77-d131-3bdd-9a7d-88b5bc962d7b | -8.8226 | -46.2115 | 2025-09-28 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 223.6 |
| 2fc833c8-838b-355a-ab44-e23a1d28cfb3 | -6.619 | -44.9721 | 2025-09-28 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 37990a02-dfbf-3f7c-b7af-23e193f95a40 | -11.4604 | -44.997 | 2025-09-28 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 580ba40e-6978-3fd5-860d-aa1e01a548cd | -9.7643 | -47.7786 | 2025-09-28 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 7c252a86-fdff-3648-9828-6ae59eddbdb3 | -11.9644 | -47.9557 | 2025-09-28 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| bf50c84b-25c8-36e1-b512-377326c320ac | -7.3847 | -47.0378 | 2025-09-28 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 251.1 |
| 8c0023a9-39c2-342d-954c-840db791cb9c | -11.904 | -44.8161 | 2025-09-28 13:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 5d3afb9d-e979-3c77-819b-76d97f179458 | -12.1031 | -43.4008 | 2025-09-28 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| be2d5113-462f-3f2d-843d-4913c3b7a36b | -7.7782 | -47.0479 | 2025-09-28 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ae27ad54-1810-3a23-ae3c-3f947f0f24c6 | -11.3658 | -44.9413 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 9cfc1268-0a88-311d-b03f-424cd13ad90f | -11.9986 | -47.0596 | 2025-09-28 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| d76f76ca-9cd1-37c1-a62e-9ffeda6a7609 | -14.5336 | -48.4268 | 2025-09-28 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| eecb9bd9-5528-3b5a-a312-3542304fc9dc | -12.791 | -47.7533 | 2025-09-28 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 277.0 |
| 25710e01-35a8-39d8-b2f6-f6379364e47b | -7.7555 | -45.7324 | 2025-09-28 13:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| dc7111ba-3ba3-35ee-9359-49973efd1838 | -14.7846 | -45.7051 | 2025-09-28 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 310.5 |
| 9f4d492d-b8a8-3ee0-b821-233ac9ef449d | -18.1778 | -53.3239 | 2025-09-28 13:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 7dd1c910-682c-34e3-aeca-2815fbe4cf1e | -12.9156 | -45.1912 | 2025-09-28 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 575bada9-95f5-3e6f-bf18-6f21d167b7ef | -8.1614 | -46.3899 | 2025-09-28 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| c07d9aa3-e4f2-3b79-aa18-99c291e0870f | -4.6946 | -37.661 | 2025-09-28 13:30:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 229.4 |
| bed66f5a-e25c-3a12-b9a3-100aa94964fe | -11.9633 | -48.0223 | 2025-09-28 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| cfc9a35a-413f-3f61-a96d-75785be7e778 | -9.9585 | -43.5752 | 2025-09-28 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| e9608e69-b3c2-3489-a945-8218ae3899e3 | -11.3846 | -44.9618 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 82e60ed5-83ce-3751-af7e-8387b03b388c | -8.8415 | -46.2095 | 2025-09-28 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 5e6cb5fa-1673-36e5-8eef-97c6a1772cdf | -9.9578 | -43.6222 | 2025-09-28 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 4507f3fa-f593-3c1d-846a-fe21172f278d | -10.9137 | -45.7375 | 2025-09-28 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| b30aa64b-57c7-3d88-b403-62be3d6cc6c6 | -4.6757 | -37.6624 | 2025-09-28 13:30:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 589.9 |
| 53dbcd6b-6730-3ebb-9a03-869fae79755c | -8.8393 | -44.9399 | 2025-09-28 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4c377cb6-4fb1-3caa-a2f2-d4d31af222e3 | -11.4413 | -44.9998 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b9422ee3-9c12-3a4e-85c4-660f86bc5516 | -11.3654 | -44.9645 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| e5d6adc9-4665-37a6-8bbc-02d307d34dff | -11.4213 | -45.0488 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| e9f0ecf9-af5b-3b35-998e-7d4964717dee | -8.1611 | -46.4122 | 2025-09-28 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |


[Clique aqui para ver as próximas entradas](README100.md)
