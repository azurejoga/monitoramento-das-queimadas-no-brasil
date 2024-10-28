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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f207d53-3a58-3306-8680-f4ea7184df6d | -5.8492 | -44.7635 | 2024-10-28 00:48:55 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9fe23e9-ae29-35f4-9827-da92dada28e3 | -4.4689 | -45.737598 | 2024-10-28 00:48:55 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4c0ae39-a90d-3eee-9c59-aeeba32b43a8 | -4.6824 | -46.652302 | 2024-10-28 00:48:55 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64eeb207-f80f-3c8f-b4b1-cf26e1201a65 | -5.9802 | -45.362301 | 2024-10-28 00:48:56 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0aa4ad4-ef0e-3cec-8761-334f65a32bd6 | -5.9821 | -45.370602 | 2024-10-28 00:48:56 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e323ccb1-e266-33d6-a9e4-ab3929056d93 | -6.4433 | -47.527 | 2024-10-28 00:48:56 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2c70ee2-f8b4-3176-b3e9-9c0c6b24e97f | -4.4239 | -45.633598 | 2024-10-28 00:48:56 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d34f375-41d3-3581-9e18-b9078b6bf3f6 | -4.4259 | -45.641998 | 2024-10-28 00:48:56 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 568e9d0c-7312-3e66-b28a-41b20250e53b | -4.4279 | -45.650398 | 2024-10-28 00:48:56 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18e68842-692b-327f-9860-e3cf5639b611 | -4.4141 | -45.635899 | 2024-10-28 00:48:56 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f3eb7f4-5dbb-3a76-ab25-94941c33598a | -4.4161 | -45.644199 | 2024-10-28 00:48:56 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff3f2b4-e5be-3073-abc1-258f13e429e0 | -4.4181 | -45.652599 | 2024-10-28 00:48:56 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f049995-c694-30cc-9892-50a117c914ce | -6.1898 | -46.566799 | 2024-10-28 00:48:57 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f51e824-ab96-37fc-a5e9-a6b0afdb8be6 | -6.1916 | -46.5742 | 2024-10-28 00:48:57 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53ca57e8-ebbc-3059-880f-413c7a803289 | -4.4194 | -45.879002 | 2024-10-28 00:48:57 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a191084b-4f66-33a7-ae6f-1cb5ae4a51f4 | -4.4214 | -45.887199 | 2024-10-28 00:48:57 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 564a79e3-0c2a-3d53-b4df-530d85ede6ed | -4.4189 | -45.964802 | 2024-10-28 00:48:57 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e9ac780-4ee7-3981-9fb3-8c901c6db495 | -4.5214 | -46.448399 | 2024-10-28 00:48:57 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24a1d34e-b712-30d9-a177-87ad875f81e4 | -4.5232 | -46.4561 | 2024-10-28 00:48:57 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5cab8bcd-b747-3a26-aab3-21e9bec89471 | -4.525 | -46.463699 | 2024-10-28 00:48:57 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2f97dc9b-6e8a-3571-97d4-0b3790ed44e2 | -4.0792 | -44.605499 | 2024-10-28 00:48:57 | METOP-C | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d723aa0-a9ec-3baa-82a7-7563d22557d4 | -4.0815 | -44.6152 | 2024-10-28 00:48:57 | METOP-C | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0087f55a-8614-38ce-b38e-403de194c111 | -4.3669 | -45.830601 | 2024-10-28 00:48:57 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd8d9100-4e71-367c-8882-f0745b9f4f22 | -4.5454 | -46.595901 | 2024-10-28 00:48:57 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fbb898e2-3550-32c9-96d5-31162be41058 | -4.5472 | -46.6035 | 2024-10-28 00:48:57 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1f97c9f5-c6c3-3fc0-a53d-a707a8415ebf | -4.5489 | -46.611099 | 2024-10-28 00:48:57 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf8d197-ffd7-3572-be3f-4908f587a3af | -6.3679 | -47.9161 | 2024-10-28 00:48:59 | METOP-C | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b841ac2b-a13f-367b-b113-83461eca3366 | -4.9213 | -48.624599 | 2024-10-28 00:48:59 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83781d72-06dc-3e98-8226-9d4d9edc1958 | -4.9228 | -48.631401 | 2024-10-28 00:48:59 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43bd517f-bdac-3eaf-8ba8-82443c214bab | -4.24 | -45.728802 | 2024-10-28 00:48:59 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| abff79a1-74ca-3513-9696-136d3c47ed3c | -4.2419 | -45.737099 | 2024-10-28 00:48:59 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dd3b02ca-d5dc-378a-aff4-f0b88571f79b | -4.8934 | -48.6381 | 2024-10-28 00:48:59 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94d1d1ea-cb49-3d8e-b09c-71f72e871034 | -4.895 | -48.644901 | 2024-10-28 00:48:59 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff4c1cea-922b-303b-90cb-6eea06935417 | -4.8966 | -48.651699 | 2024-10-28 00:48:59 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0d4d6d3-97ec-3d04-b232-690443705964 | -4.9272 | -49.0107 | 2024-10-28 00:49:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de69b83c-25e2-3e94-a538-6e54a4214fea | -4.9288 | -49.017601 | 2024-10-28 00:49:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db1bb1d9-ba21-3071-952d-5f4105c6e266 | -4.9127 | -48.9925 | 2024-10-28 00:49:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd01dbd-6d8b-3e47-83b8-e327f2b110ac | -4.9174 | -49.012901 | 2024-10-28 00:49:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9f1af84-e745-3195-872f-ed7d551a7719 | -4.919 | -49.019798 | 2024-10-28 00:49:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce9d5aef-813d-35d0-8156-0ca90999d5f5 | -5.3878 | -51.085999 | 2024-10-28 00:49:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17c2d1d6-7987-3fd8-a9f2-9354e4da634a | -6.0892 | -47.2001 | 2024-10-28 00:49:01 | METOP-C | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7abc0893-61b4-3995-97be-69846851a319 | -4.1834 | -46.370399 | 2024-10-28 00:49:02 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4dbfca10-7608-3931-b289-54b04b6a5a2e | -4.1852 | -46.378201 | 2024-10-28 00:49:02 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 33aa05a9-d7eb-3dcb-a27e-5300cea1fe5b | -4.187 | -46.386002 | 2024-10-28 00:49:02 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de4fbfdb-68ad-343f-a660-94c0760bac4a | -4.9564 | -42.919601 | 2024-10-28 00:49:03 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c38848f5-dcbf-306d-98b6-83c0ee2d4b57 | -4.2364 | -46.864399 | 2024-10-28 00:49:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a20cd715-8ba5-3429-a5dd-a790de293b76 | -4.2381 | -46.871899 | 2024-10-28 00:49:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b0b52cf-d608-3adb-a036-ada2df3414d6 | -4.2398 | -46.879398 | 2024-10-28 00:49:03 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37973328-5b69-3d1c-8ca4-e65db03ef495 | -4.9694 | -43.189201 | 2024-10-28 00:49:04 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40af0f3f-4f8c-390a-9b4a-f970718926ed | -4.9569 | -43.18 | 2024-10-28 00:49:04 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a657a9c-31c5-3b0c-b9dd-09f7271539d4 | -4.9597 | -43.191502 | 2024-10-28 00:49:04 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf920ef6-6e52-38d5-b90f-08c59ba81f7c | -4.9624 | -43.2029 | 2024-10-28 00:49:04 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60fa586a-d7bf-39f1-b77d-906ef790137d | -4.9499 | -43.193802 | 2024-10-28 00:49:04 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69714d5f-d766-3c97-80ce-bfd9144dfd5a | -4.0623 | -46.248901 | 2024-10-28 00:49:04 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6647fc36-5727-304e-bdba-5d308ad14cb6 | -4.0641 | -46.256901 | 2024-10-28 00:49:04 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9579fa36-07fa-340b-a8d8-259cf6d89aa2 | -4.4929 | -48.107399 | 2024-10-28 00:49:04 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d3e1a0c-f90d-326a-b839-9a7078892100 | -4.4945 | -48.1143 | 2024-10-28 00:49:04 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 832b094a-c70f-35da-8f65-8cf2e3de5287 | -4.4831 | -48.1096 | 2024-10-28 00:49:04 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c190f0b4-5dbe-309e-8dbd-6a73ad2ede43 | -4.4847 | -48.116501 | 2024-10-28 00:49:04 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cfed281-b565-3420-875f-bf3c4ff15a23 | -3.9344 | -45.8339 | 2024-10-28 00:49:04 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69d20b42-4c02-3da0-a3f6-f1572ea070aa | -3.9363 | -45.842201 | 2024-10-28 00:49:04 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eaa9a0ef-15e1-3f26-81a3-b99e36693fa0 | -4.988 | -43.698898 | 2024-10-28 00:49:05 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c947fa11-1324-3c76-8fa8-ea0ae149a82e | -4.9905 | -43.709499 | 2024-10-28 00:49:05 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49c5d879-3d1e-3753-935a-2c90b2625e93 | -4.9808 | -43.7118 | 2024-10-28 00:49:05 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbb9f574-67f2-3258-a777-774594953333 | -4.7342 | -49.384602 | 2024-10-28 00:49:05 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5269961-9fd3-3059-95f7-68f425719e5d | -4.7358 | -49.391399 | 2024-10-28 00:49:05 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbf8ae7c-c5fb-3c25-9ea2-86142f9a7d2d | -4.7374 | -49.3983 | 2024-10-28 00:49:05 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 681725f3-e944-3e01-b78a-8fb23252e75f | -4.1052 | -46.744099 | 2024-10-28 00:49:05 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 117ce2d3-0071-3024-8cc8-c5ddbc813406 | -4.107 | -46.751701 | 2024-10-28 00:49:05 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b10cee4-66c7-3825-938d-b739506bb923 | -3.8561 | -45.719501 | 2024-10-28 00:49:05 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a4d5534d-7295-3d88-b1c5-47443548301b | -3.8581 | -45.728001 | 2024-10-28 00:49:05 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb8189a3-b653-3b64-8f0d-c4da8d3f24b4 | -3.9691 | -46.203201 | 2024-10-28 00:49:05 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 213b48e0-2796-3520-9ad7-0ee8ca00c4ea | -3.9709 | -46.211201 | 2024-10-28 00:49:05 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 929b6bad-4ce0-3db1-bbcd-1bb7035afb67 | -4.1286 | -46.889 | 2024-10-28 00:49:05 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d63b48d0-4c79-357a-9e04-1bac5b2acaaa | -5.0685 | -44.210701 | 2024-10-28 00:49:06 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ceaed27-d654-389c-bac5-bdd4e24d93c9 | -5.0708 | -44.2206 | 2024-10-28 00:49:06 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5137a99-6800-33ea-806c-b241736f5095 | -5.0587 | -44.213001 | 2024-10-28 00:49:06 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdf574b1-4d97-37c5-9ef5-65debaad7097 | -5.061 | -44.2229 | 2024-10-28 00:49:06 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8bffad1-ec48-350e-ab06-35094c4de877 | -5.4535 | -45.887901 | 2024-10-28 00:49:06 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a763936c-3e40-3ff0-ba72-837ebc9cf0a8 | -5.7162 | -47.104698 | 2024-10-28 00:49:06 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8d8e30-5019-3f48-97ec-391250cef073 | -5.7179 | -47.1119 | 2024-10-28 00:49:06 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86222629-6e37-37eb-9d0f-99c2456de737 | -4.4089 | -48.235199 | 2024-10-28 00:49:06 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f70e896-c7c1-3939-9536-6128c34a2909 | -3.9904 | -46.471901 | 2024-10-28 00:49:06 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 65146d96-cf6a-3b71-9c58-5bd0628b9e10 | -3.9922 | -46.479599 | 2024-10-28 00:49:06 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| df49631d-911d-3b6c-85ba-569f2d2a0138 | -3.994 | -46.4874 | 2024-10-28 00:49:06 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7cda84ff-59d5-3870-a429-a446dd7d75af | -3.9625 | -46.396198 | 2024-10-28 00:49:06 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52f857c1-6ab5-33a3-8a79-249b78cc4e6d | -3.9643 | -46.403999 | 2024-10-28 00:49:06 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e93ae57c-efa7-3e69-8879-1593beb0e639 | -3.9545 | -46.4062 | 2024-10-28 00:49:06 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 165ad492-4ef5-3678-b5ed-2788fff11d6d | -3.9563 | -46.414001 | 2024-10-28 00:49:06 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a24fbe24-9ee1-3087-8726-fbaa176a95d8 | -3.8262 | -45.989101 | 2024-10-28 00:49:07 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ccd50f98-e897-30c5-9b65-480827f5095e | -3.8281 | -45.9972 | 2024-10-28 00:49:07 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 860a4920-db2c-3762-ad52-f4634129e8da | -4.1242 | -47.314999 | 2024-10-28 00:49:07 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a4f7524-6444-38da-90c2-ca7cbf7266eb | -4.1259 | -47.322201 | 2024-10-28 00:49:07 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b1f8833-0e69-3ad1-b07e-f28c70cfff31 | -4.1276 | -47.329399 | 2024-10-28 00:49:07 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd2b47c-c375-35d6-b0c0-0bd9863fe9ef | -3.911 | -46.4408 | 2024-10-28 00:49:07 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| faa26c82-1d06-3df9-a94a-a9716df2c9d4 | -3.9128 | -46.448601 | 2024-10-28 00:49:07 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82d76da2-d609-390d-8d91-03c2d6a754bb | -5.244 | -45.391201 | 2024-10-28 00:49:08 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 470ae053-6028-3d0a-9940-376bb9220b08 | -5.246 | -45.399601 | 2024-10-28 00:49:08 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58104091-b3db-3c47-b41b-8a205fa24a4f | -5.248 | -45.4081 | 2024-10-28 00:49:08 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e24d5199-e09e-3bdb-923a-afe1d663b125 | -5.4148 | -46.340801 | 2024-10-28 00:49:08 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
