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
| 8ef15ff3-b796-3171-a327-b346153c26bf | -2.3178 | -48.5717 | 2025-10-31 00:50:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| bd94ea5b-078c-34f8-a0ad-1f81bcbd102b | -10.5455 | -48.7221 | 2025-10-31 00:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1edec217-bcb0-36a1-9ad7-8d936d3f8240 | -4.5584 | -45.6335 | 2025-10-31 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| a8690ef8-3903-3063-b1b5-15d022558566 | -14.253 | -46.0068 | 2025-10-31 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 7e679073-abe2-3165-86fa-b7a3b0917389 | -14.2335 | -46.0101 | 2025-10-31 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ba6a459b-e95d-312b-a665-4cc9966df3ae | -9.8627 | -44.8656 | 2025-10-31 00:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 72f1dba6-f5d0-3eae-9aca-7054eb1cde8a | -9.7232 | -48.0248 | 2025-10-31 00:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2062adbb-aa73-3679-8290-a5c020bce6e0 | -10.5483 | -44.7773 | 2025-10-31 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 8204735a-f037-36cd-b034-6475a06ddfb9 | -11.738 | -50.2295 | 2025-10-31 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| e244c790-9f91-3f5d-8f11-4eae06633fbe | -7.6491 | -43.5876 | 2025-10-31 00:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| fc78325d-2b62-3e16-868e-3db441c5f66a | -14.2725 | -46.0034 | 2025-10-31 00:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| bf94e0c8-29eb-30ef-808f-2d43dbf31adc | -9.8631 | -44.8425 | 2025-10-31 00:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| c9aaece4-c1f1-3800-9e70-822d1c700e5e | -5.0399 | -43.6205 | 2025-10-31 00:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 731fbf6a-420c-3257-9b3b-8a9cddeeaaaa | -11.7189 | -50.2318 | 2025-10-31 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 9b24ce30-3e55-3792-8aa0-87f3308fc591 | 1.2852 | -60.4265 | 2025-10-31 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6aff644c-b9ed-346d-a526-6eba338290fa | -4.8402 | -45.3249 | 2025-10-31 00:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d8521006-1a91-3754-a5d4-3e6b2b16b711 | 1.2852 | -60.4454 | 2025-10-31 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| a3adf630-f83a-36ac-a13d-9880915a56aa | -4.4869 | -45.1872 | 2025-10-31 00:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a7354cd7-c01e-3347-b855-cde0a6fc24a7 | -9.8817 | -44.8632 | 2025-10-31 00:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 48d5efed-0839-3a67-a71f-7cdbcb1177d1 | -9.4761 | -40.3862 | 2025-10-31 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 239.8 |
| 745ff96e-22f9-3937-9b6b-42f7540b49fb | -7.668 | -43.5857 | 2025-10-31 00:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 159.6 |
| e311a637-cfa8-3fc2-88d3-4453aa234968 | -9.7421 | -48.0228 | 2025-10-31 00:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| d887f80c-d23f-3f09-b1fb-b3a63306179e | -4.0449 | -47.4951 | 2025-10-31 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 95fbfc4e-bbb5-3efa-b5e2-67f53baf518c | -14.2525 | -46.0299 | 2025-10-31 00:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0ef3c214-9a42-3811-acc3-a22d683ffacf | -10.9397 | -44.1663 | 2025-10-31 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 21037bc1-e372-3a9b-9ac8-9aec361033fc | -14.1365 | -44.1851 | 2025-10-31 00:50:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 66ecee52-0758-3657-9d0f-4b594998f398 | -4.0634 | -47.4943 | 2025-10-31 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| cc269ba6-f02e-3643-ab4a-67ef82f7c1fa | -10.5293 | -44.7798 | 2025-10-31 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 5ff8d07f-1df2-3da2-9f7c-5828230d9b53 | -3.017 | -49.4482 | 2025-10-31 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.1 |
| daa2ad67-3e32-30b7-9baf-63674d3a6de1 | -5.0793 | -45.7601 | 2025-10-31 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| ce384e1a-e92a-3798-bc42-2be1871afe0a | -4.3649 | -46.778 | 2025-10-31 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9e215a7a-daaf-326f-9254-747b1b3cf823 | -7.668 | -43.5857 | 2025-10-31 01:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 41f6c8c4-73db-3b95-ae95-3f545c5f445a | -4.5584 | -45.6335 | 2025-10-31 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 784918fe-4a8e-3f48-9bab-20280027a9ae | -2.3178 | -48.5717 | 2025-10-31 01:00:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 66025e6c-dab5-3c3a-b0bf-b6a401755819 | -10.5483 | -44.7773 | 2025-10-31 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| d8e8827f-b391-3f57-9b08-45c7843d3cff | -3.4326 | -43.8948 | 2025-10-31 01:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| d9f59ea0-7edb-3ff3-bc5e-3d4960cb3fb1 | -3.5252 | -47.5389 | 2025-10-31 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4df8001c-f4ee-3fd7-a956-21ce1b7c5e21 | -5.0212 | -43.6218 | 2025-10-31 01:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 9227b243-6b19-38c3-9897-2774d57db308 | -4.4869 | -45.1872 | 2025-10-31 01:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d5235a17-2262-31b7-a89a-b5276ee02bd0 | 1.2852 | -60.4265 | 2025-10-31 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2b01911f-6340-31d6-97fc-16e96658e1ef | -3.0355 | -49.4476 | 2025-10-31 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 4616f04e-bf4b-327e-be5c-6cc116220e7d | -2.3178 | -48.5932 | 2025-10-31 01:00:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 95a90e1e-ea72-3122-af20-1603e52eb160 | -14.253 | -46.0068 | 2025-10-31 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4a366d52-677c-3586-9a4a-9e10e77910c9 | -14.2535 | -45.9837 | 2025-10-31 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 14c34897-68d7-3de7-9665-6a67a93d91f1 | -9.8631 | -44.8425 | 2025-10-31 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 0be1d31a-0286-37e2-83ea-5bb831387694 | -5.0401 | -43.5973 | 2025-10-31 01:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f1009893-dc17-3c7a-a845-664f743da8ef | -7.6491 | -43.5876 | 2025-10-31 01:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 43d2c22b-58c0-3e43-9cc0-ae5fa3292331 | -9.8437 | -44.8679 | 2025-10-31 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 47.5 |
| c632d45c-624f-3c17-9c2e-a142ac028403 | -3.5251 | -47.5607 | 2025-10-31 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a2c85e8b-6e3c-3f72-8fb9-580d2e953acc | -9.8627 | -44.8656 | 2025-10-31 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| efbf8079-99e0-34ee-8d77-57950d2faa06 | -3.0171 | -49.427 | 2025-10-31 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 3571b61b-a996-3ba8-8572-b807fb9ad590 | -4.8402 | -45.3249 | 2025-10-31 01:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 6c27188d-2322-3e22-b604-6fa3d6809088 | -5.0399 | -43.6205 | 2025-10-31 01:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| fc2f91d8-562a-3394-8de8-d8332da99a9f | -17.1303 | -55.74634 | 2025-10-31 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| cba18bdd-58d6-36ef-8a0a-cd1ffce1a6dd | -18.29285 | -54.28428 | 2025-10-31 01:09:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b2025451-425d-36fd-9f8c-4e2a6c1ff240 | -18.2831 | -54.28596 | 2025-10-31 01:09:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a99064f-cd98-39f6-842d-4d464c5d06c3 | -17.12883 | -55.73637 | 2025-10-31 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 23b0b50d-4fa8-3aa0-a00b-fdcb16b8fc17 | -18.28487 | -54.29733 | 2025-10-31 01:09:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 12c2bc25-0cf3-300d-9ab6-8271affa8e84 | -18.29461 | -54.29567 | 2025-10-31 01:09:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a491ed49-0985-3ec5-8f15-16c1273847cc | -5.0401 | -43.5973 | 2025-10-31 01:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d4184026-7018-3283-9469-649263d431a6 | -9.844 | -44.8449 | 2025-10-31 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 2d05d00d-c7cd-3fa0-b510-dcaeac4fd67c | -10.5293 | -44.7798 | 2025-10-31 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| ad2ce87d-121b-3b8f-a875-07e3408ecf58 | -4.5584 | -45.6335 | 2025-10-31 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| aeab1c20-c7e2-397e-8858-1b167048bb8a | -14.234 | -45.987 | 2025-10-31 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| ccfcff7e-bfd9-3814-ac67-8e979f1ac776 | -2.3178 | -48.5717 | 2025-10-31 01:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 07ba3082-9fa7-329a-9061-ac7d77b542d5 | -2.3178 | -48.5932 | 2025-10-31 01:10:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a4846a32-2616-351a-bbc3-29b51d6db101 | -14.2535 | -45.9837 | 2025-10-31 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| ca36a110-60b2-39b8-bf8d-786ebf252180 | 1.2852 | -60.4265 | 2025-10-31 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| ac297cde-310c-35ab-b010-992fef0f4000 | 1.2852 | -60.4454 | 2025-10-31 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 65cab344-1390-3390-9e2f-33dfa61c699e | -9.8627 | -44.8656 | 2025-10-31 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 262.6 |
| 34b4b232-74a6-36ce-800f-3d021d823409 | -10.9397 | -44.1663 | 2025-10-31 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| cadb21a1-4d0f-3d35-ae8c-bb0f4b99bcf5 | -5.0399 | -43.6205 | 2025-10-31 01:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| c221a461-cbf6-33de-8c17-84f53d69e0ef | -3.5252 | -47.5389 | 2025-10-31 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ff70c24e-24fd-37ae-b57f-b8196c7590ff | -9.8631 | -44.8425 | 2025-10-31 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 256.0 |
| 1da1347e-ddf7-3002-acb5-a2d4c90768e9 | -4.3649 | -46.778 | 2025-10-31 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1a804ec3-9b07-3bf2-a150-cdbcdc599415 | -9.8437 | -44.8679 | 2025-10-31 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 64503c87-1371-3a51-8ed1-0664c6bc6827 | -10.9401 | -44.1429 | 2025-10-31 01:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 797d5bb1-eff1-3f33-9405-8c91680eaa5a | -10.9206 | -44.169 | 2025-10-31 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| e40514c3-084e-3b8f-a6ee-f4a3ed7c6646 | -14.2725 | -46.0034 | 2025-10-31 01:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| def7700d-6266-3bb3-b20c-150e5a75a42c | -14.253 | -46.0068 | 2025-10-31 01:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 16dc2a7e-8c6f-3f07-8abd-040cec47f418 | -10.5483 | -44.7773 | 2025-10-31 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| f941991c-7a15-37af-b021-e64e75fd378c | -5.7072 | -48.8784 | 2025-10-31 01:10:00 | GOES-19 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d7a847cb-a695-3278-8788-922964ce796f | -11.62531 | -61.45969 | 2025-10-31 01:11:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cb42724f-14fe-3f65-8370-8bc8161ba502 | -11.72703 | -59.30105 | 2025-10-31 01:11:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d93cb7a3-e36e-3e28-a66f-6ff0c2009823 | -11.73591 | -59.29977 | 2025-10-31 01:11:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7892c112-560f-3ab9-b445-fce9e68e3e66 | -11.73714 | -59.30882 | 2025-10-31 01:11:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| ce98f1a9-942c-3bea-ae20-a41b597961cf | -11.72826 | -59.3101 | 2025-10-31 01:11:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c0296251-2322-3094-8e69-13e542841c40 | -10.54055 | -48.70692 | 2025-10-31 01:11:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 9d8f45e4-31e1-37cb-9a45-0eb407383a5b | -14.45965 | -55.83856 | 2025-10-31 01:11:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| cc758ae1-4607-3626-91a3-d34cca41934f | -10.53786 | -48.71239 | 2025-10-31 01:11:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 0b395d49-a608-3a1d-af69-831c55acfd18 | -1.53168 | -55.87434 | 2025-10-31 01:13:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 95b98f24-6a84-3c74-b8d8-40f4de1ec505 | -2.91345 | -53.94454 | 2025-10-31 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9447cacf-f29c-3031-bec0-a56ed1469439 | -3.44549 | -54.63691 | 2025-10-31 01:13:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 01df194c-4d1e-3e37-a855-de26db005d85 | -1.53176 | -55.86427 | 2025-10-31 01:13:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 27e89805-4cd6-3b42-baaa-11ab09e4bd68 | -3.32551 | -54.08057 | 2025-10-31 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f91585e6-d730-3925-ac9c-7281b0b13c01 | -2.93253 | -51.46665 | 2025-10-31 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 78f5d95b-b99a-370a-bfac-97d8c6b9d758 | -2.92385 | -51.47336 | 2025-10-31 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| e2adb748-d09b-3263-8b5d-1aa8f9235d49 | -2.91381 | -53.9599 | 2025-10-31 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a3918533-4405-3bd9-ad04-796c9489046d | -1.53389 | -55.8796 | 2025-10-31 01:13:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4e8b1f11-e08c-3687-bf94-f554d57313e5 | -2.05203 | -52.08129 | 2025-10-31 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |


[Clique aqui para ver as próximas entradas](README4.md)
