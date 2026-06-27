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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67c980d0-e6a5-3bb6-b390-f4d8ce1555f4 | -12.4462 | -58.5023 | 2026-06-27 11:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 3ee7ccd1-6898-3ad9-892e-78380dfc86ec | -12.4462 | -58.5023 | 2026-06-27 11:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 88996eeb-0a3b-3985-97b9-a75c27db3937 | -12.4651 | -58.5009 | 2026-06-27 11:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 454.2 |
| be0b0cf5-3a80-3537-ba94-3e0c3d142bd3 | -12.4654 | -58.481 | 2026-06-27 11:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 86a98ecb-c051-33df-bf08-b18c859ca7c3 | -12.4654 | -58.481 | 2026-06-27 12:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 37d73c6f-2fcf-367a-9ef1-72a3182f7e94 | -12.4462 | -58.5023 | 2026-06-27 12:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 183.5 |
| db482031-5514-3112-b8fd-29bbd62f1658 | -12.4651 | -58.5009 | 2026-06-27 12:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 504.8 |
| e01a0118-5e4b-399b-95ec-452ff768d7f4 | -12.4462 | -58.5023 | 2026-06-27 12:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 234.0 |
| 8aaa45d1-63f9-33ff-bbc9-eebdcba858e4 | -12.4651 | -58.5009 | 2026-06-27 12:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 651.4 |
| 7a678e37-0a2d-396a-9bb4-2d45f22e3df0 | -12.4654 | -58.481 | 2026-06-27 12:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 8aa8ce7e-919d-3a37-a462-3c13999d461e | -3.72199 | -48.82296 | 2026-06-27 12:27:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 955ae3ef-6b4f-38e0-9782-081718714a88 | -8.30067 | -48.1801 | 2026-06-27 12:27:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b0f30810-6571-3d65-9b88-74ead8aced47 | -8.30986 | -48.20238 | 2026-06-27 12:27:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 332.7 |
| 6af59345-21c8-3a45-8096-a61da1ffa50d | -8.29757 | -48.2066 | 2026-06-27 12:27:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 27b60490-342c-30be-b3b8-569df22c224b | -6.93085 | -51.94392 | 2026-06-27 12:27:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4f9b18aa-5ca6-3a3c-aa0b-d04c6ea935a0 | -8.29532 | -48.20094 | 2026-06-27 12:27:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 3f0f4fb6-4354-3717-b950-9e2b40f08758 | -8.3121 | -48.20808 | 2026-06-27 12:27:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 230.2 |
| f03a9d59-2484-33be-b0eb-29b348010e64 | -15.40435 | -51.0622 | 2026-06-27 12:29:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d0a3b2b2-65aa-3b7a-af36-758fd72f9b7f | -12.47029 | -58.50137 | 2026-06-27 12:29:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 496ec5fa-11b9-3c9b-abbc-317789b8e63e | -12.45982 | -58.50954 | 2026-06-27 12:29:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a0d053a5-7e41-387d-99ff-e879378e8a20 | -10.93649 | -56.85747 | 2026-06-27 12:29:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3a40d7f6-2618-3208-a0ca-afe72edd7d4a | -11.91954 | -58.66441 | 2026-06-27 12:29:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 194.2 |
| e4e69108-db11-30a7-9564-e74a3780a082 | -11.62813 | -59.07734 | 2026-06-27 12:29:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| db1a9a2a-7f73-3bf3-9e30-1e4043868219 | -11.52264 | -56.12125 | 2026-06-27 12:29:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2c03dc28-5772-3488-b2a1-91578c971e46 | -10.90131 | -56.85241 | 2026-06-27 12:29:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| dbc11a06-f027-3678-b3c1-1f788c9f60f2 | -11.64669 | -54.88791 | 2026-06-27 12:29:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1926fdae-30d5-3cc5-a975-4b03bf50f3ee | -11.91036 | -57.41086 | 2026-06-27 12:29:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 3d1106ec-2b7b-3945-9c9f-5cd852c578da | -11.91918 | -57.41215 | 2026-06-27 12:29:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 485024f9-4c14-3d8a-90d6-f3631aa1632b | -12.46551 | -58.47165 | 2026-06-27 12:29:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1f670419-78f6-3e3b-bfd8-d0d8ca0fc61b | -11.95409 | -58.62033 | 2026-06-27 12:29:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 74fbef37-472f-3185-a4ab-a75ace4fe9a5 | -13.23713 | -54.4049 | 2026-06-27 12:29:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0953ca7c-d009-3f18-80e2-547ac57d5417 | -11.93011 | -58.65621 | 2026-06-27 12:29:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 52bb3e29-7b6e-3bb9-8bff-0bcaf7ae797a | -10.78354 | -54.10644 | 2026-06-27 12:29:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 5bfb8dd3-41df-3e05-906b-25ead7358dbd | -15.41721 | -51.06368 | 2026-06-27 12:29:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 1c290fcc-772a-31db-89b3-48cb48e8b59f | -11.9464 | -58.60939 | 2026-06-27 12:29:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 182.9 |
| c55fc909-91d2-3c6c-8665-ea32527195b1 | -11.51379 | -56.12 | 2026-06-27 12:29:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 96552e25-990f-3567-83ea-77cbb588975e | -11.66483 | -57.25586 | 2026-06-27 12:29:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e0e40b99-49e8-3887-b21e-c512d06b15cf | -13.25646 | -54.40748 | 2026-06-27 12:29:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9f20cb97-11b3-3998-b1eb-576f64f5c4ef | -11.61879 | -59.07588 | 2026-06-27 12:29:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 082e5843-da73-31d3-92e1-6360812ca2eb | -11.33228 | -55.29881 | 2026-06-27 12:29:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9da5bc4f-2c8f-3638-928c-d85ce624b1b9 | -15.05838 | -53.05025 | 2026-06-27 12:29:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 40d4aa96-807f-3d3b-9257-0e33af7e4f62 | -12.61564 | -57.88795 | 2026-06-27 12:29:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 0d34b4f6-1264-3ee7-946c-199d4be03913 | -12.45305 | -58.49269 | 2026-06-27 12:29:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 2b5ceaf8-94d8-3145-8c04-35bebbf73597 | -13.66408 | -53.94349 | 2026-06-27 12:29:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 32bad127-90bf-3304-9a1c-64ca9ce1ebb5 | -15.44572 | -59.23338 | 2026-06-27 12:29:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f8dbbe92-4566-3fef-837f-bae5b6f29cbd | -10.30621 | -57.13878 | 2026-06-27 12:29:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0040754f-2df2-30cb-ac5e-554d5121c01f | -12.54632 | -54.61691 | 2026-06-27 12:29:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6ae906d0-ea59-3924-b991-af16f24ac7ec | -13.24679 | -54.40621 | 2026-06-27 12:29:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 4186b5bf-4009-3087-b123-b9c3a993238f | -13.66559 | -53.93162 | 2026-06-27 12:29:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 35f8f010-b0a1-38e0-ba26-967f32b9276c | -11.94497 | -58.61898 | 2026-06-27 12:29:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 233.9 |
| 5ee3bd67-10aa-3abf-94b7-dd7924c2ed5d | -11.6399 | -58.24678 | 2026-06-27 12:29:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6593374c-508c-329a-9ead-6662b3306b72 | -13.22606 | -54.41445 | 2026-06-27 12:29:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 924ee3df-c34f-3939-afea-51e21fabf9f4 | -11.52137 | -56.13029 | 2026-06-27 12:29:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e71533aa-7486-3d9c-a098-2c3e0ec3d480 | -13.22747 | -54.40357 | 2026-06-27 12:29:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| d62db269-11d5-384e-9002-d08d991db5b1 | -10.81691 | -53.53529 | 2026-06-27 12:29:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| dac40a86-0796-3c40-bfdc-b3c83bb4e5fb | -11.92867 | -58.66587 | 2026-06-27 12:29:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| caeeaadb-1fee-3301-8082-87f949651f46 | -12.62451 | -57.88926 | 2026-06-27 12:29:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 11b04e21-7d8a-33a5-8da4-ba6927428ffa | -15.43665 | -59.23201 | 2026-06-27 12:29:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2e83afae-0ad5-38a3-a86c-dbf198860bdb | -12.45165 | -58.50223 | 2026-06-27 12:29:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 5a94af7a-0aad-365e-94a5-44264688d6cf | -15.06928 | -53.05178 | 2026-06-27 12:29:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c05b3eac-83e4-3a97-aff6-1265e36312d7 | -11.92098 | -58.65477 | 2026-06-27 12:29:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 7ac0401c-74d7-3fd7-9b8f-3c62d2db5040 | -12.92259 | -51.87568 | 2026-06-27 12:29:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| d3740d66-f6ba-3d27-a123-12ec80ff39db | -11.92049 | -57.40316 | 2026-06-27 12:29:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f12cc31d-d9eb-31fe-89a2-92b2c668d403 | -9.59007 | -56.92207 | 2026-06-27 12:29:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 547199e7-0d39-3397-8c67-95869593806f | -11.29763 | -51.39731 | 2026-06-27 12:29:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2172905c-e3e3-36f5-93dc-64f3521da64c | -11.91167 | -57.40188 | 2026-06-27 12:29:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7429394a-775c-3c9b-8b17-08e8fbb3cef7 | -12.46125 | -58.50002 | 2026-06-27 12:29:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 885.9 |
| 68158d60-5eaa-3fc7-9e33-e8d508b62892 | -9.59889 | -56.92333 | 2026-06-27 12:29:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 93941a49-e333-3689-8fec-2309c745a21d | -12.47171 | -58.49185 | 2026-06-27 12:29:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 62a438a0-9a0d-3382-a5e0-21a14816b9e7 | -12.60676 | -57.88665 | 2026-06-27 12:29:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 83e477d9-6089-37dd-8a02-828ee477c239 | -10.77399 | -54.10518 | 2026-06-27 12:29:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f4dc789c-34ba-31cd-bffb-d58696fae273 | -10.3351 | -50.15196 | 2026-06-27 12:29:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5727f005-9d49-3d27-978f-23da6225c5ba | -12.46268 | -58.49051 | 2026-06-27 12:29:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 890ae6c7-3774-3109-9e71-34ea04f1d6a0 | -9.76422 | -56.93227 | 2026-06-27 12:29:00 | TERRA_M-T | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| c1f3e7ac-d39b-32b9-8e85-82a501901df9 | -11.51252 | -56.12904 | 2026-06-27 12:29:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| addd18a7-d595-39f3-812e-2aedc3f7fcd2 | -11.95551 | -58.61073 | 2026-06-27 12:29:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| f7c745d8-4d1f-33c2-8e9b-f34f542b894f | -12.60809 | -57.87753 | 2026-06-27 12:29:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| edcf6a68-9f35-38ee-8b28-752f154b4576 | -10.93776 | -56.84856 | 2026-06-27 12:29:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| bc735ada-af80-30d8-a8a9-b041404c50dc | -11.21354 | -54.33339 | 2026-06-27 12:29:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a70e21ed-8401-3502-a078-7e2bffe720e1 | -12.4651 | -58.5009 | 2026-06-27 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 858.7 |
| c2b46f00-6980-3eb6-a697-c280b82a232f | -12.4464 | -58.4825 | 2026-06-27 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| d1fe5484-608c-3569-a831-b96af450c1bd | -12.4462 | -58.5023 | 2026-06-27 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 334.6 |
| d46c0234-c3dd-30ce-bf0b-3aafc33d0f87 | -12.4654 | -58.481 | 2026-06-27 12:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 280.7 |
| e5459d1b-aa82-3212-90d7-0df77fda6b19 | -11.9095 | -57.4134 | 2026-06-27 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 82bfcc7a-66f9-303a-80a5-26c97b820949 | -13.2392 | -54.4129 | 2026-06-27 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| a651c7b5-57f9-3425-8874-dbe969507820 | -12.4654 | -58.481 | 2026-06-27 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 448a9b97-795f-30ca-be4a-26241121423a | -12.4651 | -58.5009 | 2026-06-27 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 855.0 |
| 9d5faa27-d8f9-3292-84e7-7d32ee7f8bba | -12.4464 | -58.4825 | 2026-06-27 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 8276d0b6-61d4-3816-abe0-c94946eeeb75 | -11.9097 | -57.3935 | 2026-06-27 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b8e86489-2bd8-3a80-ac9e-53732820019c | -12.4462 | -58.5023 | 2026-06-27 12:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 334.2 |
| 0a54ba1e-7b35-3cd6-94cf-79e0ae5cee13 | -12.4464 | -58.4825 | 2026-06-27 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| ce91913a-403b-3d73-bc34-13a7b20cea10 | -11.9095 | -57.4134 | 2026-06-27 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| ce8cc426-bd84-36a7-9388-77fedcfaffd3 | -11.9284 | -57.4119 | 2026-06-27 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| efec356a-f82f-36c3-901f-c57a500abe78 | -12.4651 | -58.5009 | 2026-06-27 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 692.9 |
| 2d14aabc-ec4a-307e-9cb3-4fec06bade0a | -11.9097 | -57.3935 | 2026-06-27 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 51c9595e-4d63-3f19-b341-a631c3414c90 | -13.2201 | -54.415 | 2026-06-27 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 50ea4743-01ac-39e3-96da-54f75727c9b9 | -12.4654 | -58.481 | 2026-06-27 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 129f22e9-8412-3df5-88ac-568b404c92c3 | -12.4462 | -58.5023 | 2026-06-27 12:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 409.0 |
| d1c0a988-882e-3981-8494-0581e5f28a2d | -13.2392 | -54.4129 | 2026-06-27 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| e6865073-18a3-3bbe-b008-10ed938d09b5 | -12.4462 | -58.5023 | 2026-06-27 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 399.1 |


[Clique aqui para ver as próximas entradas](README23.md)
