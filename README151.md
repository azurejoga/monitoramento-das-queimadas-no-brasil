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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a9cc550-54c9-3ad3-8a89-a67bee5d6e05 | -7.7308 | -46.2513 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 569b7674-a7f3-3444-808d-2a71ec159e34 | -11.1444 | -43.3845 | 2025-10-03 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 0c8c1172-1f86-3bf1-9291-a3b37ff00425 | -7.7755 | -42.5152 | 2025-10-03 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 377.9 |
| 556cc513-7ed6-3422-8a3f-55375f903762 | -5.7033 | -42.7077 | 2025-10-03 14:00:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 124.9 |
| 40319574-609d-38d2-9f21-717ce4ea304e | -11.8818 | -44.9815 | 2025-10-03 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| b2a5c77c-27cf-3895-9d7d-050898777396 | -7.7687 | -46.2255 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 715fb50a-78b2-30b4-aa34-ba0669f26515 | -9.9563 | -43.7162 | 2025-10-03 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| dd243577-3fe8-3510-8f1d-a37201446a09 | -11.9159 | -46.3044 | 2025-10-03 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 8d60a58f-dd1c-3b2d-ab62-e9711647c641 | -8.8729 | -46.6985 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 08faf2c1-4258-3880-8a96-7a21fd0f8d20 | -13.6724 | -51.1911 | 2025-10-03 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| eca331ef-0e99-3028-9427-3a3a27839c17 | -6.6978 | -42.8118 | 2025-10-03 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| ce1dc2d3-9703-3dd5-840b-7b66600ebb6f | -13.8058 | -51.2593 | 2025-10-03 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 5de2d692-69b4-3bc3-bc8e-33f0c979b514 | -11.1271 | -47.8856 | 2025-10-03 14:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| b0462c18-40bd-3e44-8dc1-4531e495c28a | -8.8543 | -46.6781 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 5645c2a0-9d38-3dd8-a117-057e2ed8f517 | -14.6497 | -44.7499 | 2025-10-03 14:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| acb28a72-8f97-3637-9be3-50ee73775b89 | -6.6604 | -42.7917 | 2025-10-03 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 08fa4b9f-50c9-34a0-932d-218e39186b3b | -6.7167 | -42.8101 | 2025-10-03 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| e6b80c94-4dc3-3f28-9360-2d728cd1a753 | -7.646 | -45.4489 | 2025-10-03 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ff6947b0-8745-32d1-b80a-f6d68e5abb16 | -14.367 | -46.1251 | 2025-10-03 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 385a8202-9f74-3dfb-b24b-544c3c8695d4 | -9.1813 | -46.1956 | 2025-10-03 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 81550bf7-b18c-38c9-8644-cd472e67886f | -6.5551 | -43.8758 | 2025-10-03 14:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e790b7f9-e001-337e-bd7f-16ca142f2c4c | -14.3675 | -46.102 | 2025-10-03 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 360cd165-68c3-3954-ba24-15032c094559 | -10.0148 | -50.2443 | 2025-10-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 5cd2b17d-4cfd-3630-bae0-9444d903047e | -10.297 | -50.3013 | 2025-10-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 62ce07bd-05d4-39dc-8a63-200bd3fe329e | -8.1699 | -44.1608 | 2025-10-03 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 201.8 |
| f49b2db9-a23e-39c7-a7b3-ec94d3b714fd | -12.1215 | -43.4453 | 2025-10-03 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 134999ea-b121-30c3-8dd3-9acd0afa3cb3 | -18.9667 | -48.5198 | 2025-10-03 14:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 7ce635d7-7216-3a5d-8212-6470b3c1eed1 | -9.355 | -45.9284 | 2025-10-03 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0128b871-6711-3b95-8129-bb8f042d8037 | -6.6787 | -42.8372 | 2025-10-03 14:00:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 19d90f6c-7ed3-32d3-93d2-ec1fd8c56f12 | -9.9369 | -43.7422 | 2025-10-03 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 208.9 |
| 9360e67b-52bd-3c4e-8bf3-dc5957129f66 | -10.1569 | -45.493 | 2025-10-03 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ed89e28a-425a-3971-be72-aaa3e829267d | -8.9118 | -46.6052 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 1484d09e-0934-3adc-a815-d8e9e765d37d | -9.3389 | -45.7266 | 2025-10-03 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| a2367013-47a0-3fd9-91e2-362fdf092189 | -13.1534 | -47.9015 | 2025-10-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 60b2d661-6631-3f73-97c1-1181eed8b06f | -10.019 | -48.4964 | 2025-10-03 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 5d6858d3-3a02-3a70-83c6-965df8d7985a | -8.6908 | -47.7126 | 2025-10-03 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e0fe7d83-d9a4-367e-8021-bae34c87bb7f | -8.5599 | -44.6494 | 2025-10-03 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| de79eacb-4efc-3d55-a22e-249d93a160e5 | -14.0037 | -44.9376 | 2025-10-03 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 8eae7974-d529-3185-a9ea-7e20beb676d0 | -13.6711 | -48.0253 | 2025-10-03 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 81749c1c-874b-3cb5-8ae3-25dbb7f06659 | -11.9155 | -46.3272 | 2025-10-03 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 409.6 |
| 266afd3f-4641-35ca-8c9b-a800880171ae | -7.7125 | -46.2082 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 496e701f-75d3-309c-baeb-32a763327304 | -12.7819 | -50.5543 | 2025-10-03 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| e6b6c9e7-0f23-33cf-a067-6e9f83740970 | -9.3547 | -45.951 | 2025-10-03 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| d55cea72-9741-3d30-bb3e-b0bbc65c10a1 | -9.0989 | -46.7195 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 8b650c44-9cc8-31ce-9c26-6bb68e51fe47 | -9.062 | -46.6565 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 703a92d1-f168-3830-b63d-66c9fd9ddf26 | -16.0583 | -51.0454 | 2025-10-03 14:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6502b261-a6b9-3ff3-8292-75f4faa896c7 | -7.4469 | -46.4777 | 2025-10-03 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| db2540de-7382-31bf-88c0-defcb9dbfc69 | -8.5458 | -47.264 | 2025-10-03 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 4a97bca1-c0ff-399b-99d6-107ad906e223 | -6.5549 | -43.8989 | 2025-10-03 14:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 0602aeba-9f0a-3e84-959d-0aa003a1a7f7 | -13.8247 | -51.2782 | 2025-10-03 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c4356c9b-ccf8-3166-a849-477e0526e1ae | -18.9673 | -48.4968 | 2025-10-03 14:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 433.3 |
| db885071-1f39-3605-8b27-bc82909388a2 | -13.1152 | -47.8848 | 2025-10-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 48ab5cfd-bb7d-3b90-be91-f343f25da4b5 | -13.9771 | -48.1793 | 2025-10-03 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 3b386331-d138-3977-b964-480047c0679e | -6.0806 | -42.5118 | 2025-10-03 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 9b0c128a-2afb-3ecb-af7c-14851c82c059 | -7.756 | -42.5648 | 2025-10-03 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 483.4 |
| c4890df5-6fac-386d-99b7-a2dde7f7de02 | -13.3418 | -48.1188 | 2025-10-03 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 57db2023-3a15-3a4f-841a-2796d84503b0 | -9.9035 | -45.9553 | 2025-10-03 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 8e082da0-c6d5-31d8-92a4-7c257196e6dd | -9.4548 | -45.5545 | 2025-10-03 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c63422cb-697d-328b-a838-7f4107bbf509 | -7.3101 | -45.2531 | 2025-10-03 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 02129ab0-cd66-3350-a842-7a3677f8259c | -9.8769 | -47.8324 | 2025-10-03 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7d1735e6-3d92-3135-aa1c-45d6b08600ac | -12.7623 | -50.5782 | 2025-10-03 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 74b0480c-2b6b-33df-a8b8-f5d249fa4a4e | -6.6976 | -42.8354 | 2025-10-03 14:00:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| be3086c6-3267-340a-aee4-d34b16a11578 | -14.0227 | -44.9576 | 2025-10-03 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| fd130474-aa15-3028-a72c-a4ddb5b55a8b | -10.0523 | -50.2619 | 2025-10-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b1220b84-3523-3500-a0c2-3cd3ad322d0d | -13.155 | -47.8121 | 2025-10-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 97471d91-f0d3-3dec-87ec-f8afc8a3baee | -13.9775 | -48.157 | 2025-10-03 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 7a1d23f0-c320-34ca-b844-e7283ff8142a | -13.7865 | -51.2618 | 2025-10-03 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e8072558-d506-3dd5-b827-707b7b2426c4 | -9.9182 | -43.7212 | 2025-10-03 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 227.7 |
| b9a0636b-8ea1-31a5-813c-ba10a70c539a | -10.1573 | -45.4701 | 2025-10-03 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c8cbaca1-e598-372c-8c64-f0619cb4c3f0 | -14.3904 | -45.9369 | 2025-10-03 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 0537c4ab-b485-3142-9eb9-9decb1ddf084 | -7.7684 | -46.2479 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 229.4 |
| 85980316-060c-340d-b8fb-be721ae56d06 | -8.5959 | -44.7833 | 2025-10-03 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 0ba88d92-a33a-362a-9349-7c5d1396e3eb | -15.7905 | -43.7155 | 2025-10-03 14:00:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 344.5 |
| 017b4838-305a-3abd-a0fa-94f91914a443 | -9.9394 | -43.5777 | 2025-10-03 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| ff525f53-62d5-383c-b2b8-b155dd39e9bf | -7.7746 | -42.5865 | 2025-10-03 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 255.8 |
| b6c5dee5-0819-320f-8d48-5930234a60ff | -8.1917 | -47.0101 | 2025-10-03 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| eaa250e0-f1bc-384a-8b48-a8952e5dc85d | -7.7941 | -42.5369 | 2025-10-03 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 179.7 |
| 106e0039-9496-37f3-89a1-24ac5de84fb5 | -10.345 | -48.176 | 2025-10-03 14:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e664334f-fe8d-36ad-a3a5-27e673996c17 | -9.9031 | -45.978 | 2025-10-03 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| f29aef80-f92d-3b48-ad3b-6a4943d1f2e0 | -7.7499 | -46.2272 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 70e7c4d5-acc9-3b65-b2f6-21857a28a9c5 | -12.6131 | -46.9725 | 2025-10-03 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 6ebfa5d5-28b9-319a-a289-f3b30881b446 | -7.7752 | -42.539 | 2025-10-03 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 251.9 |
| 4d832595-049f-30b6-b30b-7bc2046f4c6a | -9.8772 | -47.8103 | 2025-10-03 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 2515af19-d31f-31c5-93c9-06174b321e45 | -6.0809 | -42.4881 | 2025-10-03 14:00:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 1a713c01-23d0-3305-a8fc-c1d702e480cc | -9.3357 | -45.9532 | 2025-10-03 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ea2371fe-4123-3c09-b75c-ec2e87d91676 | -10.1759 | -45.4906 | 2025-10-03 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b2a00821-bad0-356f-856d-a7b9e45765e4 | -7.7496 | -46.2496 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 182.9 |
| f8261a1a-5793-3ac1-89e1-46cb27e8ecb7 | -8.527 | -47.2658 | 2025-10-03 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 6650e007-da6e-3eff-bd69-b3a0c1f154aa | -10.0709 | -50.2814 | 2025-10-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 324a9f88-5af8-3374-b0d3-afb166af20c4 | -7.7749 | -42.5628 | 2025-10-03 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 153.3 |
| 2b180a3b-8e01-34c1-a516-f021e79b3260 | -8.1702 | -44.1377 | 2025-10-03 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 417dc1e2-f342-3864-8526-66c3a1731efb | -8.8343 | -46.7694 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| cc9c6fd1-c635-3675-acf0-8a8e28ad4b18 | -14.0032 | -44.961 | 2025-10-03 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 76445e5b-ab50-3354-a121-1f18952effc4 | -9.9959 | -50.2462 | 2025-10-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 5d548fcc-5f9c-3fdc-9564-76d8db501cb8 | -11.5687 | -47.6526 | 2025-10-03 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 812eea35-2235-3279-857e-f27616fd7df8 | -13.3422 | -48.0965 | 2025-10-03 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| d04225da-dea3-3b41-83b9-89d19c403c27 | -7.2845 | -44.18 | 2025-10-03 14:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ea16a05f-22f9-34b0-bddb-9e34edff8a5b | -13.38 | -48.1354 | 2025-10-03 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 00e4e1d9-f304-36f9-b8b6-fcc2a2db2e14 | -7.7494 | -46.272 | 2025-10-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 3768db46-a3ce-3a4c-b70e-163710629fc6 | -12.7435 | -50.5591 | 2025-10-03 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 188.6 |


[Clique aqui para ver as próximas entradas](README152.md)
