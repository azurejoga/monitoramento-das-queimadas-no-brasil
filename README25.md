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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9acc61c3-f991-36ec-b93d-b4702987b124 | -6.8466 | -52.8132 | 2025-09-01 03:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 69d053fd-386a-3450-abd9-ad6a1b938fbd | -12.9387 | -56.9454 | 2025-09-01 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 919d3590-dd9c-3e10-81fd-c2de2aeffb4a | -9.135 | -65.5453 | 2025-09-01 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 88c37835-202a-31c5-a189-13bf71e0350b | -6.8281 | -52.8143 | 2025-09-01 03:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8f6adc30-b7a3-39be-9e70-c2d3f107cdd4 | -7.0948 | -44.3358 | 2025-09-01 03:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 4ea7b826-bae8-324b-8cba-76539b313f7e | -7.0946 | -44.3589 | 2025-09-01 03:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5ce1d47a-78ae-32c3-bb9d-56da35f19727 | -12.9194 | -56.9672 | 2025-09-01 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 244.9 |
| 1fd61677-4588-35cf-bf70-6d6e7ee919be | -12.9004 | -56.9689 | 2025-09-01 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| fdf8c284-4ed5-39b6-b1fa-8238f084d666 | -7.6783 | -61.0908 | 2025-09-01 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 63c7fef6-a2ba-3dc7-a989-313effb2e200 | -8.7499 | -61.4269 | 2025-09-01 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 453d970f-bf02-3586-a107-d057324aad9e | -7.0757 | -44.3606 | 2025-09-01 03:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| f8d8dd57-7e60-3335-9196-0bccb85c1457 | -7.076 | -44.3376 | 2025-09-01 03:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 2185187e-391f-32b2-adc0-94e7c5a8fb1c | -12.9385 | -56.9655 | 2025-09-01 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| fc3ee7ab-e3b9-305f-b8ea-92cd3f2ededc | -12.9197 | -56.9471 | 2025-09-01 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 283.5 |
| afd9e480-9cf1-3651-8f47-5d78ee4cc42f | -9.1165 | -65.5459 | 2025-09-01 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| bc84c3de-5959-3cfe-88b0-b226a7dd80e3 | -12.9197 | -56.9471 | 2025-09-01 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 274.4 |
| 2928091f-d673-3985-a2fa-0d0ceaf9c45a | -6.8281 | -52.8143 | 2025-09-01 04:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 195d2f00-38f1-35d8-ba53-2dfea87036ad | -7.0946 | -44.3589 | 2025-09-01 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| a77d6203-247a-314a-a034-0bd5058f276c | -7.0948 | -44.3358 | 2025-09-01 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| c9cba54b-9e49-3432-a562-cf957b898024 | -12.9194 | -56.9672 | 2025-09-01 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 258.0 |
| f13b326b-2ea8-3070-841a-a714795aba72 | -7.6783 | -61.0908 | 2025-09-01 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b08201f3-2b34-3a9e-bc67-6e6477d9464b | -9.135 | -65.5453 | 2025-09-01 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 1331b69e-71c5-3e9e-9a37-236c362a310a | -7.076 | -44.3376 | 2025-09-01 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 10b1fa61-4f58-3597-85a0-4964b465d74a | -12.9004 | -56.9689 | 2025-09-01 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 18189980-6ddb-3088-94d2-6467936fa1ea | -9.1165 | -65.5459 | 2025-09-01 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 2117d2e9-5bb6-3f42-bd73-f9057e70c2bd | -12.9385 | -56.9655 | 2025-09-01 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 177.5 |
| 02d11373-278f-36fe-b9c5-fa446bbf83a7 | -12.9006 | -56.9488 | 2025-09-01 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 52bd0d13-2dc9-3279-883c-511b49561d36 | -6.8466 | -52.8132 | 2025-09-01 04:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 58d8607f-bf4f-3927-b8d2-ac42d3d37e02 | -7.0757 | -44.3606 | 2025-09-01 04:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 39b04ff7-6bd4-3f7c-82af-092f59a524e7 | -12.9387 | -56.9454 | 2025-09-01 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 194.4 |
| 127c380f-bd82-3510-b135-0100e919199b | -8.7684 | -61.4261 | 2025-09-01 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| a645507a-420f-30c8-a494-3ae2fa31b63e | -4.33833 | -43.05161 | 2025-09-01 04:08:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 708d4d10-2f0b-3c20-952c-d3d32c8eb0c5 | -3.59256 | -47.52272 | 2025-09-01 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82aa3420-6a64-36b8-be65-81fd8c99b547 | -3.42383 | -43.33371 | 2025-09-01 04:08:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db77f711-ccb5-3802-acce-11bb1f84507e | -2.42088 | -49.34834 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16c27cdc-d5e2-356b-bfff-876065b986b0 | -2.44555 | -49.36228 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db56bf7f-a7f1-36b5-9bfb-9416b814c217 | -3.93769 | -48.44999 | 2025-09-01 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcf5aa9d-ca6e-3dd2-8d87-4d64d1096af6 | -2.40932 | -49.35301 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f45ea54-c8cb-3b59-88d1-5c53c6f2a334 | -3.21742 | -46.82856 | 2025-09-01 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c033b72-44a4-3231-8d9c-d75dfd31f788 | -3.42736 | -43.33426 | 2025-09-01 04:08:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0559601-a33e-383d-9bb8-49f7939b8089 | -3.68199 | -49.1958 | 2025-09-01 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7af2bb1b-6e32-3c09-9a36-6fc023a9042d | -1.54194 | -47.55902 | 2025-09-01 04:08:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7507fe99-ba5f-3fb3-b2d8-976e5b0cd400 | -4.15515 | -46.78049 | 2025-09-01 04:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f90ff0a-58ea-34c9-ad73-35cdc0e66461 | -2.40986 | -49.3498 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e3eb256-0ebd-3e70-a929-6917cf6f8aba | -2.41617 | -49.34426 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6a4842e-98b6-3cff-81f3-b875ea47e885 | -4.1538 | -46.78867 | 2025-09-01 04:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93008449-5d8a-39db-8355-92dc6c396c0c | -4.92048 | -43.18423 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 572741aa-4ddb-3159-896e-8417adef649a | -4.07294 | -47.96204 | 2025-09-01 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c54941a-0edc-3993-9cfa-3d7d2e611079 | -4.41078 | -40.48408 | 2025-09-01 04:08:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| be3f15cd-fa4a-38bc-942e-916d1ae49f41 | -4.91234 | -43.19065 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d18db505-7447-319a-a3d6-97ff81f23c4b | -4.92454 | -43.18103 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7b5fcb0-8740-3c22-9208-220aabfcb6f9 | -2.4508 | -49.36318 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f291de43-fe1b-3fb6-8712-e24a710b0171 | -3.63537 | -49.20895 | 2025-09-01 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1d7b7da-503b-3ec5-84b7-a5dcb652195a | -2.44451 | -49.36869 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 998f2ad6-e402-3d25-afe3-36801fdbe434 | -4.74791 | -41.43069 | 2025-09-01 04:08:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9713307b-bd32-3e5c-b5e9-cff9f1ec331e | -4.9095 | -43.18632 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f512736-5cf5-347c-9fb6-558591b5fde8 | -2.74232 | -42.79139 | 2025-09-01 04:08:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 27d59055-3ffc-34d9-b37c-bb69bc48ad21 | -4.14885 | -46.79202 | 2025-09-01 04:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 289aa6c0-b963-3b13-8285-67f6440aa581 | -3.63586 | -49.206 | 2025-09-01 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e7135d5-3fed-3f28-a3ae-cc72779efed9 | -4.91702 | -43.18368 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52cdaf05-9166-3b06-a140-38df8f6724b0 | -4.88339 | -43.13996 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c267e618-7bc4-3e98-9683-bef9a5037e52 | -4.14951 | -46.78801 | 2025-09-01 04:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d909d9bf-968b-3aa1-8d57-df041ae8c526 | -2.45028 | -49.36638 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40d3b3c3-b249-3d6a-b059-4833c1a4bed8 | -4.15877 | -46.78517 | 2025-09-01 04:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f533bec-7973-3c2d-b51c-eb5196343517 | -3.00727 | -47.83897 | 2025-09-01 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 761d3af2-5330-3999-a875-8188edc23ccc | -4.91295 | -43.18688 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cf9a6fd-fc51-3d9d-9df9-0b22f580e209 | -4.73317 | -44.44818 | 2025-09-01 04:08:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad19f5c9-e345-332b-8130-ced763b34ba9 | -3.68464 | -49.19586 | 2025-09-01 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a558325-aaef-34f5-a6bd-cc06bc966767 | -4.92109 | -43.18048 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4206340c-72af-39a6-8465-34a0bef10ab1 | -3.6825 | -49.19281 | 2025-09-01 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55f169db-ee8d-353f-b17a-5e99b9a23839 | -4.64577 | -41.39341 | 2025-09-01 04:08:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2cd75806-add3-3419-8e6e-3e1b1de8439f | -2.43978 | -49.36461 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94f6854f-9e09-3a4e-b9bc-f353f82dddd0 | -2.44503 | -49.36548 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2db796a8-70b1-338e-8ed5-aa7388709eec | -3.21697 | -46.83023 | 2025-09-01 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ef6b948-be3f-31e5-9e6a-20ed0644ea3a | -4.61873 | -41.39575 | 2025-09-01 04:08:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0eaa2088-cb03-3dc5-b53e-d9c0a9dba189 | -2.34535 | -47.58699 | 2025-09-01 04:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cdc827f9-7561-3f0e-969a-356107ced013 | -3.67956 | -49.19495 | 2025-09-01 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de0ed258-c863-3323-85e9-7f0f21dc9d5c | -3.42158 | -49.04701 | 2025-09-01 04:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c8885b0f-2989-3fa8-bd84-ddb53cd70964 | -3.93857 | -48.44479 | 2025-09-01 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f718077a-3034-38b2-ac03-71c95a53581a | -3.42109 | -49.04996 | 2025-09-01 04:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c2316271-b1a7-38e9-9cf0-e524c7358b4d | -2.34773 | -47.58512 | 2025-09-01 04:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5438b113-d44f-3f57-993b-09f1466c9f8c | -4.1234 | -47.65667 | 2025-09-01 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50b88004-4283-3f98-8dec-a2edcd170e4f | -3.60474 | -42.85778 | 2025-09-01 04:08:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 571f21ef-867a-34d3-8fb9-3db769bd3af8 | -1.41882 | -48.38677 | 2025-09-01 04:08:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e6449791-cb35-3af0-a52d-3af6e2870ee8 | -2.41564 | -49.34746 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 255e376f-f318-325b-a410-c9a893221341 | -2.41511 | -49.35067 | 2025-09-01 04:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ee8b14f-bdb7-363a-ba32-22d1aa97a252 | -3.42446 | -43.32978 | 2025-09-01 04:08:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea96b753-811a-36f3-abb2-009b2217c26c | -2.7458 | -42.79194 | 2025-09-01 04:08:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a69ca96b-def2-39e0-b42a-fdf7494eb1e8 | -4.15447 | -46.78459 | 2025-09-01 04:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 592d8037-0195-344f-94c2-e6232dced65a | -4.33893 | -43.04787 | 2025-09-01 04:08:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b13f8674-35b8-309c-a16f-64cfe0cea55e | -2.34307 | -47.5844 | 2025-09-01 04:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a36b95b1-779e-3c45-8948-322fb2781cdf | -4.90888 | -43.19008 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a99908d-2bfd-38a5-b963-180eb222d520 | -2.34068 | -47.58631 | 2025-09-01 04:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70f19514-ea91-3905-ae83-d7bd6c6d7e3e | -4.92739 | -43.18534 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a85c4439-fbc5-3ce7-bccc-db4f7a161c99 | -4.643 | -42.52079 | 2025-09-01 04:08:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 827e3f74-3e79-316a-9244-21577eb20d3a | -3.16719 | -42.77496 | 2025-09-01 04:08:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ae09471-603e-39bf-a254-37c0d3b53385 | -3.93417 | -48.44754 | 2025-09-01 04:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48167487-b2a3-374b-83e6-7345d9af587b | -4.91763 | -43.17992 | 2025-09-01 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b47899c-d41d-36ee-9bda-a0d11fe46054 | -4.12417 | -47.652 | 2025-09-01 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc6b074b-fc04-3055-862e-9809061f6e3a | -3.74141 | -40.82536 | 2025-09-01 04:08:00 | NPP-375D | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README26.md)
