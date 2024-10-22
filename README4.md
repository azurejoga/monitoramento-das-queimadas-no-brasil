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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c02b1989-e73f-33ac-b9d7-a602a32a533b | -4.5078 | -45.1488 | 2024-10-22 00:17:20 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32aa768d-4ef7-33d2-bfdb-48ca468a11a6 | -4.3558 | -44.564602 | 2024-10-22 00:17:20 | METOP-B | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aac3aa91-dead-3ae9-aa4d-bbf4c1b1147e | -4.3574 | -44.5714 | 2024-10-22 00:17:20 | METOP-B | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9281fc8c-edf8-3c83-a590-19bdd97f902e | -3.9282 | -43.266701 | 2024-10-22 00:17:22 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 051eeed5-6cb7-3135-abf2-1c3afcc07104 | -3.8974 | -43.221401 | 2024-10-22 00:17:22 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f05769c8-e53a-3ceb-ab99-300331eecbf0 | -4.5747 | -46.045799 | 2024-10-22 00:17:22 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a21e2375-26ec-32ab-9b78-2d03aacb06de | -4.5763 | -46.052898 | 2024-10-22 00:17:22 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f074e4f2-653b-3b36-b846-5e1bb96d5120 | -4.5092 | -45.798901 | 2024-10-22 00:17:22 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d5c7d81-d1da-37f8-abfb-0dc38960b402 | -4.5108 | -45.806 | 2024-10-22 00:17:22 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c3d027b1-fbd6-391a-adfe-61f41933ec3f | -4.5124 | -45.813 | 2024-10-22 00:17:22 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58c5275d-d911-334d-920b-95d3cb238af2 | -4.4979 | -45.793999 | 2024-10-22 00:17:22 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6aed3ed-8df4-3e8d-b111-abd01ce8e47b | -4.4994 | -45.800999 | 2024-10-22 00:17:22 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb41d814-ac22-3acf-b93a-e777d91b9c69 | -4.501 | -45.808102 | 2024-10-22 00:17:22 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca3bb684-92bf-3d28-9d52-115dae08a604 | -4.5026 | -45.815201 | 2024-10-22 00:17:22 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30da9f56-297e-3886-87ee-5f5232929722 | -3.3875 | -41.261002 | 2024-10-22 00:17:23 | METOP-B | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e757abc0-63be-3726-8aac-f3cf3f06f2e3 | -4.1207 | -44.344501 | 2024-10-22 00:17:23 | METOP-B | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbb9f87d-0a06-3ca3-b1fb-34d6fad93866 | -4.0439 | -44.232399 | 2024-10-22 00:17:24 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4fece4a6-5832-3dc1-90f8-317a48b1277e | -4.0454 | -44.239201 | 2024-10-22 00:17:24 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b12a73f2-dea3-3aea-bbcb-c5548195bb58 | -3.8765 | -43.7202 | 2024-10-22 00:17:25 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74c7328e-15e1-32de-8a5d-bfc6729c9956 | -3.7143 | -43.232601 | 2024-10-22 00:17:25 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b60b695-e07d-374c-90f4-2bd84c52e2de | -3.7159 | -43.2397 | 2024-10-22 00:17:25 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 037ae11e-73f4-384e-a8a4-4ad16fdc2811 | -4.2157 | -45.591202 | 2024-10-22 00:17:26 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 083287e2-b097-3fd1-961b-5475a08557d4 | -4.2043 | -45.586498 | 2024-10-22 00:17:26 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f8cd970-29f6-36d1-82e7-ad60e25ceac3 | -4.091 | -45.3568 | 2024-10-22 00:17:27 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a91ef22-2bb2-3a4f-9ca4-90c9f2f01179 | -4.0925 | -45.363701 | 2024-10-22 00:17:27 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 403fce28-0ca3-33db-b09d-ed353e78c33c | -3.3583 | -42.709999 | 2024-10-22 00:17:29 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92acf1e9-6843-3450-8932-2a4786498fdb | -3.36 | -42.7174 | 2024-10-22 00:17:29 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3506d6a7-2f2a-3cf7-ab10-c07a2729ff79 | -4.1608 | -46.1745 | 2024-10-22 00:17:29 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1627e609-7e51-322b-bae9-c32343891fc9 | -4.1624 | -46.181599 | 2024-10-22 00:17:29 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3956b059-9b61-3f30-87df-eec3db4c48ed | -4.151 | -46.176601 | 2024-10-22 00:17:29 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 65dc2a12-e119-31ac-9a37-a8b59592e24a | -3.7107 | -44.399799 | 2024-10-22 00:17:30 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d706e7d-c870-39d2-9caf-b5896526c1ae | -3.7009 | -44.402 | 2024-10-22 00:17:30 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e9f3219-4c36-3952-ad97-37f963dbb17a | -4.1243 | -46.379601 | 2024-10-22 00:17:30 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62b5c4da-e22d-3695-b1ac-35d37a5c82ed | -4.1259 | -46.386902 | 2024-10-22 00:17:30 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61c7d609-a79f-30b1-9ea9-ba8599c66ced | -3.4693 | -43.606201 | 2024-10-22 00:17:31 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0c91f40-b5ed-3330-b548-12bf070f424d | -3.4709 | -43.613201 | 2024-10-22 00:17:31 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20ebf7e9-c6ba-3dfd-869e-2f65ec432a0a | -3.4725 | -43.620201 | 2024-10-22 00:17:31 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bfc89eb-23c7-30cc-af0d-ad331ca0f289 | -3.4595 | -43.608398 | 2024-10-22 00:17:31 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78a5e667-89d0-3faa-895f-632c6b1eba93 | -3.4611 | -43.615398 | 2024-10-22 00:17:31 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02b37380-7b1e-3363-a0d6-a91814f564a1 | -4.0483 | -46.1315 | 2024-10-22 00:17:31 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee73d995-ea8e-3cc4-8107-c98a13550c61 | -4.0499 | -46.138699 | 2024-10-22 00:17:31 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 271e8381-4bf7-3fb3-a6cb-064217807568 | -4.0515 | -46.145802 | 2024-10-22 00:17:31 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a4efb33-ff3d-3361-863d-e63c7b63d6c0 | -4.04 | -46.1409 | 2024-10-22 00:17:31 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd645309-22be-372e-82ee-828b73912ff4 | -3.9623 | -46.023399 | 2024-10-22 00:17:32 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6649bc44-60a7-3679-9e39-18e07f8ce1ad | -3.9639 | -46.030499 | 2024-10-22 00:17:32 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f49b656b-44ac-39ad-9c7c-5968091fff1f | -3.9525 | -46.025501 | 2024-10-22 00:17:32 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 02c22ae0-d2c8-3c8c-8f8a-840e3290b2ec | -3.9541 | -46.0326 | 2024-10-22 00:17:32 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c42e78a6-8089-374e-abcf-c9530659bc44 | -4.0761 | -46.8563 | 2024-10-22 00:17:33 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d677e14-7b69-3780-abe1-9072fb3deb25 | -3.7266 | -45.7066 | 2024-10-22 00:17:34 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dac8a512-3ab2-35cf-95da-0c21e049a263 | -3.3927 | -44.269501 | 2024-10-22 00:17:34 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4f46476-5fba-3f42-b3a5-7a0e5a15c1e2 | -3.3943 | -44.276402 | 2024-10-22 00:17:34 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 151e8d3d-53db-356f-aed3-fed68f446333 | -3.5917 | -45.243401 | 2024-10-22 00:17:35 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45fdef6c-05e7-3054-bdc1-a8e9fba44f71 | -3.5803 | -45.2388 | 2024-10-22 00:17:35 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8ae6309-5066-364c-9b4b-5bee1d0fe214 | -3.5819 | -45.245602 | 2024-10-22 00:17:35 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16a83f57-9047-3409-8997-e9d2bf9a117f | -3.2683 | -44.1749 | 2024-10-22 00:17:36 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79f652c9-6519-33ae-8410-3f84454c7b8f | -3.2698 | -44.181702 | 2024-10-22 00:17:36 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2cc3b23-ddba-3c86-abc5-2643a8439cf3 | -3.5566 | -45.7295 | 2024-10-22 00:17:37 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4d747ee-dbc7-3439-a027-dee0b451ecf8 | -3.104 | -45.640202 | 2024-10-22 00:17:44 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52115941-9d57-3cd6-834d-3f3daa42c6c5 | -3.1056 | -45.647099 | 2024-10-22 00:17:44 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f8ae050-0d7a-3d1a-aaf6-8ce60db76835 | -2.9314 | -45.6059 | 2024-10-22 00:17:47 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 893dcc09-b0b3-3246-8e3b-384ff6685d2d | -2.933 | -45.612801 | 2024-10-22 00:17:47 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee655fbd-ab20-3be5-8eca-ae087c263cbd | -2.9345 | -45.619701 | 2024-10-22 00:17:47 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e91aab0-6760-3037-851f-88aa99396a14 | -2.9232 | -45.614899 | 2024-10-22 00:17:47 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0df344a-a930-34e3-be83-e0f94e78fbe0 | -2.9247 | -45.621799 | 2024-10-22 00:17:47 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6da5e561-13c6-3658-9071-efbcff051923 | -2.806 | -45.460499 | 2024-10-22 00:17:48 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da875b0e-594d-34d5-a98b-81949f4b034f | -2.8076 | -45.4673 | 2024-10-22 00:17:48 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 182eda55-93a8-3773-87bf-0aa7b4d33d2f | -2.7947 | -45.455799 | 2024-10-22 00:17:48 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6cf86fe3-3fdb-3c55-9fdb-d31eb594e319 | -2.7962 | -45.4627 | 2024-10-22 00:17:48 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa990356-ab84-3def-bb0a-f9496bbbcb55 | -2.7978 | -45.469501 | 2024-10-22 00:17:48 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 684c318c-a7b1-3809-9c09-2d6d52331aa7 | -3.0304 | -46.551601 | 2024-10-22 00:17:49 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b812711a-9bce-361d-a340-8472d1de8420 | -2.7435 | -45.777901 | 2024-10-22 00:17:50 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c385342-d192-3538-9905-4243021a26de | -2.745 | -45.784801 | 2024-10-22 00:17:50 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c12ed2f6-6227-36a6-8158-3a56e357de43 | -2.7466 | -45.791698 | 2024-10-22 00:17:50 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 552d4dd2-9396-3a12-8503-44b07f8d5af5 | -2.5129 | -45.989101 | 2024-10-22 00:17:55 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66b48255-df28-3721-aec2-c3fb1b6d177c | -2.503 | -45.991299 | 2024-10-22 00:17:55 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8088968f-d21e-3ef7-bc69-af2e31d60161 | -2.5046 | -45.998199 | 2024-10-22 00:17:55 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53f129a6-deed-3a28-b024-b1a009978a0b | -2.4584 | -45.884399 | 2024-10-22 00:17:55 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2473728-1a27-379a-88dc-d464a747f583 | -2.46 | -45.891399 | 2024-10-22 00:17:55 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d3682763-82e4-3835-a11a-940212a054da | -2.4439 | -45.865898 | 2024-10-22 00:17:56 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13a977c3-3164-3009-b7ec-027364eea16e | -2.4455 | -45.872799 | 2024-10-22 00:17:56 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d932c132-b5df-3c4e-8c8b-baf7a20fa837 | -2.4471 | -45.8797 | 2024-10-22 00:17:56 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d37b7af-40d3-322e-81c8-3f0a3ed27090 | -2.4486 | -45.8866 | 2024-10-22 00:17:56 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0cab5464-fa80-3df9-bcdd-a2b710732a1d | -2.4326 | -45.861 | 2024-10-22 00:17:56 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d7af95a-4074-3d3f-8c12-c2bef4e7a586 | -2.9101 | -47.9935 | 2024-10-22 00:17:56 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5da1374e-c6a5-31c2-a926-8c459101577e | -2.912 | -48.001701 | 2024-10-22 00:17:56 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2425860-a388-3380-b771-1b8e27b79b0a | -3.063 | -49.512798 | 2024-10-22 00:17:59 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 540ef260-8e31-3e0b-92fe-7073a58a14f3 | -2.2788 | -46.506199 | 2024-10-22 00:18:01 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7e30c77-1c50-3ebd-8557-e459f745fe1e | -2.2804 | -46.513302 | 2024-10-22 00:18:01 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9962c3cb-2e22-33b7-955f-69c2c0dd17e2 | -2.1483 | -46.475201 | 2024-10-22 00:18:03 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4679d588-f11c-3988-bad6-8a01b8f27b91 | -2.1499 | -46.4823 | 2024-10-22 00:18:03 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92a57ff8-6e0b-39ce-b152-2502587cb3a4 | -2.1515 | -46.489399 | 2024-10-22 00:18:03 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55782ecf-53cb-345a-9612-9eb415c28194 | -2.2062 | -46.733101 | 2024-10-22 00:18:03 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f39fff48-9097-3902-94db-ae0d281950e1 | -2.2078 | -46.740299 | 2024-10-22 00:18:03 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dde91886-5912-3214-b3e2-cd949da08844 | -2.2045 | -46.771301 | 2024-10-22 00:18:03 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06a505fe-212f-30b2-bfff-539a98c962bd | -2.5752 | -48.427601 | 2024-10-22 00:18:03 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44711004-6f33-3673-9986-12cb7fea1acc | -2.5771 | -48.436199 | 2024-10-22 00:18:03 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6075183-fe05-3b88-962b-f182982674bd | -2.7257 | -49.2878 | 2024-10-22 00:18:03 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16d4c85d-8559-3dba-83aa-514ef740a2c9 | -2.7159 | -49.289902 | 2024-10-22 00:18:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ced6684-4a5a-3a06-9979-90b774b2b2c5 | -2.718 | -49.2995 | 2024-10-22 00:18:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cc26013-c763-3b6b-8d32-4d6be99433e5 | -2.1311 | -46.719299 | 2024-10-22 00:18:04 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
