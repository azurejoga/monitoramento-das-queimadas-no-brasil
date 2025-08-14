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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbe37725-66b0-39e4-b802-6f181e9152db | -10.5326 | -42.550301 | 2025-08-14 00:41:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a73d68cd-fde1-3841-bae3-948dafc8e6d5 | -17.049601 | -51.7845 | 2025-08-14 00:41:00 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 96fff373-8f8e-3316-937d-8e1ab201331c | -3.4273 | -49.041801 | 2025-08-14 00:41:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cbc794b-4e67-3ce5-aba9-25de69136ca7 | -9.0505 | -45.073502 | 2025-08-14 00:41:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae57facc-0d5c-3750-91c8-4812fa8b2a54 | -18.5436 | -46.0508 | 2025-08-14 00:41:00 | METOP-C | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 03898e60-a71c-3929-9dbc-f8017d1cab05 | -22.6791 | -47.457199 | 2025-08-14 00:41:00 | METOP-C | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 128f3890-49e5-3668-a454-3f1929b9e8f0 | -6.8923 | -59.100101 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9bcf3753-5e97-3197-97da-4f28e3e5870f | -22.677401 | -47.4487 | 2025-08-14 00:41:00 | METOP-C | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d0600bfb-0628-3478-8bbf-72ce116bfc4f | -6.2703 | -53.676399 | 2025-08-14 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1581d008-bc41-3172-8484-3c290a22ef27 | -5.8852 | -43.918499 | 2025-08-14 00:41:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b41a24cd-a43f-3222-b993-745f178c219b | -12.3019 | -50.009701 | 2025-08-14 00:41:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0efb305a-8025-3a2f-b696-f272f561f35c | -6.6214 | -43.890598 | 2025-08-14 00:41:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aae113eb-ff08-39ab-b230-f771c2d67275 | -22.3016 | -49.547798 | 2025-08-14 00:41:00 | METOP-C | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a9224b45-372e-3fb7-b1ba-374cee60deda | -7.9456 | -46.841599 | 2025-08-14 00:41:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8e9ae8b-0a5d-32ab-a0a8-b352062fc6d5 | -10.9736 | -49.569302 | 2025-08-14 00:41:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 336b2276-369c-3fcc-add7-64c9f061148f | -5.7565 | -46.660198 | 2025-08-14 00:41:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af6143a5-a580-3853-973e-1c9bf84bbb76 | -6.8742 | -59.158298 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b131ba16-5747-30ea-9137-cdc1c826617d | -22.667601 | -47.450901 | 2025-08-14 00:41:00 | METOP-C | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ab59c311-86ca-3763-ab5d-f63353055af8 | -8.7386 | -44.021702 | 2025-08-14 00:41:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6b384bb9-edd3-3142-a0c8-ebf4b0c078b2 | -12.6896 | -44.951199 | 2025-08-14 00:41:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3708de9-eead-3afd-952a-a42ad10ce2d8 | -18.2523 | -47.2672 | 2025-08-14 00:41:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a7ffa7ca-323c-3d76-9c67-dd847d68ff73 | -5.7582 | -46.667599 | 2025-08-14 00:41:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c273dc7-77da-39a4-80da-1df0ff9a39dd | -6.0719 | -59.894901 | 2025-08-14 00:41:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7460c098-7849-32ce-b53a-32ee7ca639f6 | -9.1487 | -59.620499 | 2025-08-14 00:41:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1edb828b-a524-3df0-947b-06525754c6b7 | -6.5295 | -56.1898 | 2025-08-14 00:41:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12314037-d339-32b3-bbec-c7f9f82d2d55 | -13.5735 | -46.955898 | 2025-08-14 00:41:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e8f90aca-6be8-364f-b1f1-00656181a34a | -15.5787 | -47.312401 | 2025-08-14 00:41:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2bff9482-e69d-341b-a140-205f1f0ab721 | -6.902 | -59.098099 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bdc3c3e-37e4-3166-a6cd-c3705c98893e | -15.5614 | -43.1479 | 2025-08-14 00:41:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| a27a272f-98af-3ae5-9fb7-464f89ed41d2 | -12.4255 | -48.691002 | 2025-08-14 00:41:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50b3ffd2-d776-321c-8eee-87e36538ff92 | -12.3184 | -46.064999 | 2025-08-14 00:41:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c73a84de-835d-3352-bbe0-76897abff7e4 | -17.6161 | -46.7029 | 2025-08-14 00:41:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b6ebc1a6-746d-36b4-afaf-26cbb0dd3043 | -12.4271 | -48.698299 | 2025-08-14 00:41:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7bc9d203-de55-383a-a30c-94bb758994e7 | -6.8978 | -59.126202 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e58a312b-cf44-3ee0-8171-f4019bee9a64 | -4.2224 | -47.2094 | 2025-08-14 00:41:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9ce4a96-66d6-33e8-8b24-8fd6679ca3f1 | -8.5216 | -43.290401 | 2025-08-14 00:41:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 107e9af5-56cd-3235-8e04-96caefd56db6 | -6.0779 | -59.923698 | 2025-08-14 00:41:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a591ec1-8cdd-39f0-a7c2-590cb60e3d92 | -7.9537 | -46.832199 | 2025-08-14 00:41:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 356fbce6-bccc-3c31-8a7e-f534b4c68df9 | -6.8633 | -59.105999 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dfc16112-8eb2-33ad-90d1-239d9f7a0d13 | -8.5265 | -43.310299 | 2025-08-14 00:41:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db69ae3e-043a-3629-bbb0-dc97ef4941ae | -6.9419 | -44.542599 | 2025-08-14 00:41:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab9f7818-9294-37e9-8908-977b65be66c9 | -6.9538 | -44.549099 | 2025-08-14 00:41:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a036817a-cd9a-3aec-a8ab-ec01fa6fa142 | -5.9779 | -44.134499 | 2025-08-14 00:41:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3957e4b4-5e80-3a83-bced-281328211a47 | -6.9117 | -59.096199 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03311fe9-0361-3e64-9a19-5b4b66efeefc | -15.9276 | -43.511501 | 2025-08-14 00:41:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7961aafa-7873-38db-b71b-35567e9f0722 | -22.6022 | -46.726898 | 2025-08-14 00:41:00 | METOP-C | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2d8dad4b-acb3-39eb-9da9-77c76df588d8 | -6.8591 | -59.133999 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9f3b29a-0efa-3f9f-bd8d-20e1577887e7 | -19.8925 | -44.6092 | 2025-08-14 00:41:00 | METOP-C | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed50c387-2efa-3952-a040-3c72c3061326 | -4.2322 | -47.207199 | 2025-08-14 00:41:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98b8587e-5bbd-3bcf-97a8-3255d814a8da | -5.9923 | -44.151501 | 2025-08-14 00:41:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fbf5f2c-8906-334e-a002-4f86b77044d0 | -15.5818 | -47.326801 | 2025-08-14 00:41:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fa01f8dd-0b04-369f-a3c5-486ec62585b6 | -20.003901 | -42.195599 | 2025-08-14 00:41:00 | METOP-C | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 73324dae-748f-3380-ad41-670af806652f | -9.1548 | -59.651199 | 2025-08-14 00:41:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b714a1dd-4d93-3375-9239-66e77f0baa88 | -5.1625 | -39.502499 | 2025-08-14 00:41:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 50c1e07d-58d0-34ef-8181-75306a55ce3f | -23.576799 | -47.242401 | 2025-08-14 00:41:00 | METOP-C | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd600d25-ae87-3f0a-9431-295f08c07944 | -23.5751 | -47.233898 | 2025-08-14 00:41:00 | METOP-C | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5314d7bf-01a9-34e0-bb79-056a49d678b2 | -17.051901 | -51.796398 | 2025-08-14 00:41:00 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 585358c3-ad0f-3339-b6e2-f20289cd3ce0 | -6.9461 | -44.560299 | 2025-08-14 00:41:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffd0892f-9e2e-38a1-bfbc-d6a0698d1950 | -12.3167 | -46.057899 | 2025-08-14 00:41:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 32d57710-7e97-3734-a249-974a20397ab8 | -5.7903 | -43.607399 | 2025-08-14 00:41:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64489930-69ff-3fea-859f-043b337c8283 | -8.5191 | -43.322601 | 2025-08-14 00:41:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b8e7fd09-7b90-382c-8905-520b20952194 | -12.3151 | -46.0508 | 2025-08-14 00:41:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55db7483-8c95-362f-9cfd-47846dbd16a8 | -18.2507 | -47.259701 | 2025-08-14 00:41:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 767b0109-d013-3c4a-8c44-753d12a7288a | -6.944 | -44.551399 | 2025-08-14 00:41:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e842f37a-9a81-3993-bd19-bbab0368aa50 | -14.3247 | -48.633202 | 2025-08-14 00:41:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 16e51bc4-ca0c-3b77-a8b6-cba096b398c4 | -5.99 | -44.1418 | 2025-08-14 00:41:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6f30b25-0e9a-3962-ab16-f9df8b3ef45b | -6.8784 | -59.1301 | 2025-08-14 00:41:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19e003db-d472-3ac9-88ab-fe4082c5ded8 | -14.4849 | -46.062 | 2025-08-14 00:41:00 | METOP-C | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7bd914c1-f9fd-3b03-86fb-619261658738 | -4.7732 | -45.3237 | 2025-08-14 00:41:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f6f4a2b-2d00-3a61-b45f-c7de255b1e56 | -4.7752 | -45.332298 | 2025-08-14 00:41:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd7d5fd6-ef7b-30c9-8cc0-5b7774b22f10 | -12.5872 | -46.971001 | 2025-08-14 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f449333-9dad-3700-a119-c0eea4407eb2 | -16.077299 | -43.618999 | 2025-08-14 00:41:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 32d178be-9f42-352a-b340-310c49b181a0 | -5.8806 | -57.713001 | 2025-08-14 00:41:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8616e4-d56e-35b4-88b5-bc09f4d139c9 | -6.0876 | -59.921799 | 2025-08-14 00:41:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73853416-1702-385d-86bd-9112437d0039 | -8.7506 | -44.0284 | 2025-08-14 00:41:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d33d5612-981f-3681-aa32-92ffe2c27681 | -14.4865 | -46.069099 | 2025-08-14 00:41:00 | METOP-C | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 53cb13d4-1e54-38be-b220-361a1d1d55e1 | -18.5322 | -46.045799 | 2025-08-14 00:41:00 | METOP-C | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 090151d3-cfc1-3387-9976-9965ff74e8c6 | -10.5301 | -42.539902 | 2025-08-14 00:41:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0eda41ac-8997-3d9f-9864-cf69bbffd5c6 | -6.9517 | -44.540298 | 2025-08-14 00:41:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86495fe0-357c-3726-be1e-6fdf18aae083 | -20.617001 | -55.452099 | 2025-08-14 00:41:00 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9018fdfb-31ac-350a-9d86-eb31a8b0fee9 | -9.7713 | -48.742802 | 2025-08-14 00:41:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ffa6d8e-6400-3a3b-a98c-d94d5dabf5b3 | -10.3605 | -50.805901 | 2025-08-14 00:41:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 38dfa158-23ab-3967-b7a6-0f08671d7f18 | -6.2679 | -53.6656 | 2025-08-14 00:41:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b5eacc4-a05e-3f43-853a-727e0e88343c | -12.5856 | -46.9641 | 2025-08-14 00:41:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 364ec742-a48d-3e57-880a-c142f65f557b | -5.9802 | -44.1441 | 2025-08-14 00:41:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3fdb1bbd-937f-3d31-9309-c8cf854af642 | -22.309401 | -49.535099 | 2025-08-14 00:41:00 | METOP-C | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9d44aef9-532f-349f-88d5-99f29bb34139 | -22.67322 | -47.46436 | 2025-08-14 00:43:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 829b378b-a8fc-3e9f-9e7d-89f68bf28542 | -23.57076 | -47.23648 | 2025-08-14 00:43:00 | TERRA_M-M | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 25bca820-03dd-350e-bdf5-6f6c6ebc86f4 | -22.56111 | -47.32764 | 2025-08-14 00:43:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 619f40e5-53e7-3dd7-9804-64930aaea7ce | -22.66281 | -47.45613 | 2025-08-14 00:43:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2749f345-833b-3869-b5e3-d457d34dde1d | -22.67178 | -47.45451 | 2025-08-14 00:43:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 9b8d205f-75da-3a2f-b360-d0965c56d77e | -22.60115 | -46.72336 | 2025-08-14 00:43:00 | TERRA_M-M | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| f3feb8d2-ad95-3089-82be-18e4cb99ca70 | -23.5722 | -47.24643 | 2025-08-14 00:43:00 | TERRA_M-M | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 4f4a80c0-43fb-350c-8cef-b93dbef79e59 | -21.80401 | -48.14126 | 2025-08-14 00:45:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5592966e-30fc-3b2e-befb-f2db55a499a7 | -20.00704 | -42.20591 | 2025-08-14 00:45:00 | TERRA_M-M | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| 012a21eb-ab3e-3b5b-a05f-0dedf7f8224a | -19.25786 | -44.16865 | 2025-08-14 00:45:00 | TERRA_M-M | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| deffbd5d-4353-3d4a-9ece-0452670887d2 | -18.54441 | -46.06202 | 2025-08-14 00:45:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 43bc9d88-f712-3831-8cb9-1fcd881bff16 | -18.53243 | -46.05165 | 2025-08-14 00:45:00 | TERRA_M-M | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 36.3 |
| e66ceab6-54ad-310c-a8da-794fce04e4b4 | -18.53215 | -46.04515 | 2025-08-14 00:45:00 | TERRA_M-M | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1d34da83-643a-316c-a8fc-47269c17351f | -20.61876 | -55.4859 | 2025-08-14 00:45:00 | TERRA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 46.8 |


[Clique aqui para ver as próximas entradas](README4.md)
