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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ec0e6a9-5b6e-3854-bf6b-7963b37b3089 | -3.1551 | -51.484901 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dd3c957-a13c-3710-bd23-28f7a2752cdc | -4.1689 | -44.2118 | 2025-11-18 00:55:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc77da81-66bb-3a90-bdb5-8905b13449ca | -5.8775 | -49.875099 | 2025-11-18 00:55:00 | METOP-C | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1d50110-793c-3ca4-a314-f66feebf2a23 | -10.792 | -47.635799 | 2025-11-18 00:55:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3dc57f13-95da-3965-afbb-1e8c0b2363a5 | -7.0725 | -46.041698 | 2025-11-18 00:55:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df440c1e-9529-3bf2-9d8f-51fe0130f67d | -8.2956 | -44.0131 | 2025-11-18 00:55:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7e5536bf-b39e-331c-afc2-6801c0e97a6b | -4.0942 | -45.6059 | 2025-11-18 00:55:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1e6037f-06e9-3650-9d41-4fa0c9c7c57a | -4.1884 | -45.612999 | 2025-11-18 00:55:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37e51988-e3c3-3f82-a03d-4c1e1fd65783 | -9.7299 | -49.132198 | 2025-11-18 00:55:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a07e9093-d322-340f-9977-aa71d7fc2f55 | -2.8542 | -45.2313 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71fa6eed-a55d-37c5-929c-d74d701c770f | -6.672 | -42.0144 | 2025-11-18 00:55:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 74a63917-6374-3edf-b518-4174f98b833d | -2.8261 | -45.414902 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa052a3e-f0ed-3dac-b166-195364365acc | -10.6413 | -49.7216 | 2025-11-18 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07b109cd-5cdf-3497-b16c-448d2d38f02e | -3.1567 | -51.491901 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 787ac5cc-0324-3966-a140-d67744f11964 | -8.2782 | -43.984798 | 2025-11-18 00:55:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 83bdbfb7-2a56-3831-8f4b-7f112e70c28d | -5.754 | -49.257999 | 2025-11-18 00:55:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c213fb0-cb3b-3ed7-92dc-40434aba493e | -3.1171 | -45.731602 | 2025-11-18 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37462ae5-f9ad-3e5e-a98b-9626e3de0897 | -6.6776 | -42.036701 | 2025-11-18 00:55:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6936345c-d2e7-3785-9e13-0e62cfa3444e | -4.5964 | -45.9417 | 2025-11-18 00:55:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6daf402d-a9a8-3aeb-93c7-26cb80701689 | -6.1276 | -42.952801 | 2025-11-18 00:55:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ad6ee00d-94a0-3679-8a3c-fc560f12f974 | -4.1371 | -46.344601 | 2025-11-18 00:55:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78d3761c-c7d6-37a8-8840-5183ca323d0d | -10.3502 | -48.9146 | 2025-11-18 00:55:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1ffc1f6-f525-33fa-b12b-8d43d75b2abe | -9.402 | -48.439499 | 2025-11-18 00:55:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7bf5712-e05c-373f-bbc9-f2bf4d9415c9 | -2.9864 | -51.0667 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb421e10-d328-3d8e-81f3-04106c4302ec | -5.5649 | -51.198502 | 2025-11-18 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adf109e3-bc3c-3c66-979a-7fd252144a34 | -10.6429 | -49.728802 | 2025-11-18 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2783d333-6cd3-3238-99f1-ac1b2f481c5e | -7.4331 | -48.935902 | 2025-11-18 00:55:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 40631573-a93d-374c-acd0-f7261ff1985e | -3.1469 | -51.494099 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32bce1c9-7109-3911-9038-b8a5287168a2 | -9.7201 | -49.134499 | 2025-11-18 00:55:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ae9a09a-7cca-3efc-a20c-855360fe7a15 | -6.4422 | -43.805401 | 2025-11-18 00:55:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0634669b-01f9-311f-b331-820ddcb1abe1 | -4.7034 | -46.302502 | 2025-11-18 00:55:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5878a2bf-1119-3d11-8493-091bb96b5229 | -3.7983 | -50.117901 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b991fb75-16d5-3ac7-a7fd-b673ce7977e2 | -3.4744 | -46.067001 | 2025-11-18 00:55:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 55680b19-b285-3e5d-934e-b7de76066bfb | -7.8267 | -47.158501 | 2025-11-18 00:55:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6da599b7-da7b-330e-9fad-d2bd95f6ebce | -10.6527 | -49.726501 | 2025-11-18 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c032a2e-3dc9-3385-ae81-0565edd37575 | -6.7114 | -40.801399 | 2025-11-18 00:55:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c71df921-911f-3128-b2c2-1b7087396bec | -2.2884 | -47.227798 | 2025-11-18 00:55:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa1ed315-8dc4-3cd0-9130-3dce1855e0b0 | -3.0166 | -47.830601 | 2025-11-18 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e912c5f7-46b4-3bec-ba2a-0a00063ed3f4 | -3.0793 | -50.353298 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4784e52-819c-36e3-bda1-1dbf3b1896c9 | -4.5485 | -48.472801 | 2025-11-18 00:55:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 436da3e7-de72-3afd-b819-b5d862bdb5e1 | -7.6914 | -46.852901 | 2025-11-18 00:55:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e193c49-e82a-31c3-a2ab-999363d95f4e | -3.4678 | -46.0825 | 2025-11-18 00:55:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5127466-ac34-3a00-90e1-5a10f503dd78 | -7.4323 | -45.191101 | 2025-11-18 00:55:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a0575ff-fe7a-3284-b7b9-3f33a6b7d3b4 | -2.8289 | -46.727299 | 2025-11-18 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 084bca02-90f4-399a-9fb9-2a1ca23cfce4 | -3.4674 | -49.9813 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce8c3fcd-af1c-3c31-839b-1ec8ac17fb2f | -2.8639 | -45.229099 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cccf3f0f-fb88-3ce5-8e76-4a287e5efe98 | -5.3798 | -50.486698 | 2025-11-18 00:55:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62f02cfa-c8e4-3382-a5b4-76dea4e040f8 | -10.36 | -48.9123 | 2025-11-18 00:55:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd125955-768c-33cb-8483-315352947815 | -8.9359 | -49.8452 | 2025-11-18 00:55:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd76c75-f500-3516-bcb0-5a3cfa893a4e | -2.7213 | -45.147099 | 2025-11-18 00:55:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bfb08680-bde3-3991-8aa5-454849ab4fdc | -6.9441 | -49.669498 | 2025-11-18 00:55:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7947acac-abb3-366d-b98c-4509f9f6cb14 | -10.352 | -48.922199 | 2025-11-18 00:55:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97e4f93d-dafc-35b6-b033-1bd95f04ab44 | -9.0963 | -44.3293 | 2025-11-18 00:55:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e94d36c1-1e7a-3a95-a508-7cb2047053be | -4.2278 | -46.336399 | 2025-11-18 00:55:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1be8de38-e7f5-30f1-bbc0-85c4db1e07e6 | -7.0628 | -46.043999 | 2025-11-18 00:55:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62b2c092-7bc7-380c-ae5d-3b6cd4b48649 | -3.5158 | -50.2785 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 608f38c5-9f40-3a1e-9ea7-a843600e65f8 | -3.3864 | -46.129299 | 2025-11-18 00:55:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7e7d27-cbe9-34bf-a790-556e6c4c975f | -6.211 | -46.874599 | 2025-11-18 00:55:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b910b8fb-7288-3b88-81b9-dac28711ba56 | -5.3781 | -50.479401 | 2025-11-18 00:55:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0677af2e-e9cd-3704-ba89-9b4ff138129c | -3.479 | -52.355301 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d71233d-88da-309b-b6d1-3527ade15ebf | -4.1748 | -50.184601 | 2025-11-18 00:55:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49603ba9-ce55-3daf-8076-4e7eb25137b2 | -10.5129 | -49.523899 | 2025-11-18 00:55:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0d7e48-5d38-3fd8-b77b-5a3c485c91bd | -1.7732 | -54.183899 | 2025-11-18 00:55:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c98fcb1-0d4f-3e20-84f5-c16451285a42 | -4.6365 | -45.637501 | 2025-11-18 00:55:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7189a096-b39e-319f-af1d-efd771a89021 | -3.3361 | -44.373199 | 2025-11-18 00:55:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 925028b8-14f9-3f6b-b7d7-e311380f2530 | -1.8 | -54.7071 | 2025-11-18 00:55:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4e7e44-d103-31a8-a8bc-8a9999f54cbd | -6.7044 | -40.7743 | 2025-11-18 00:55:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7f655e73-b52c-3a08-a333-564e13a64a63 | -3.4888 | -52.3531 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 775d2151-7ef1-3ab2-8dbc-82c5efe35aa8 | -2.9164 | -47.8428 | 2025-11-18 00:55:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b097e2c-a22f-3905-bc23-896135d652c0 | -3.6552 | -51.775101 | 2025-11-18 00:55:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0861355-53d7-3b98-8df7-298d9c9d628d | -4.9125 | -48.530201 | 2025-11-18 00:55:00 | METOP-C | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7ff422e-56fe-35bf-b4e8-278c6160c07a | -3.2371 | -50.500301 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1011461d-5746-3177-941a-d770779326c8 | -3.7215 | -52.0639 | 2025-11-18 00:55:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f31a822-e959-352b-960b-312fa2957ec0 | -3.7784 | -47.741501 | 2025-11-18 00:55:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4edbe2a-0204-3d66-ac40-8bebdd4785b5 | 1.5165 | -55.978298 | 2025-11-18 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7106d99-50e2-3e91-8b3b-652838f75bd7 | -5.7424 | -49.252201 | 2025-11-18 00:55:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 179228c1-a795-3405-90e8-1a1ab2e3730c | -3.1665 | -51.4897 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9291aede-520e-33df-a26c-d5cda6c6afbe | -3.2446 | -43.020199 | 2025-11-18 00:55:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d531a10-8fb6-3eab-8e47-ee958b57f843 | -4.3998 | -49.7771 | 2025-11-18 00:55:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7f1206c-76f4-34eb-94ef-6792d5530c6c | -2.826 | -46.715099 | 2025-11-18 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8824b5f8-6b2a-324f-9385-13ef6c421d2f | -4.1828 | -44.226799 | 2025-11-18 00:55:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d8f1fd4-c51c-3a7a-8067-a3364ef42426 | -2.4753 | -50.238899 | 2025-11-18 00:55:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcf0021a-44c5-3c16-966b-6cd30cbeacfc | -10.6621 | -49.366299 | 2025-11-18 00:55:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15b2417d-3672-3b5f-a221-c1895d3cd7b0 | -5.9611 | -52.931 | 2025-11-18 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 400b5201-6d2f-3837-94f5-019342c2dd30 | -3.0705 | -50.226398 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c231af6-c346-318d-a1ed-9aaf061cb2ef | -3.4872 | -52.346298 | 2025-11-18 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b3d1b8b-fad9-3f72-bdd5-f1f1bac1a4a8 | -6.9326 | -49.664101 | 2025-11-18 00:55:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1226289e-716e-33ad-9f8e-f8156a91a54d | -7.54 | -47.038898 | 2025-11-18 00:55:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6552cba0-085f-32d3-972d-3a633816ad34 | -5.7442 | -49.260201 | 2025-11-18 00:55:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed487223-5af1-3677-84ed-8108904d2651 | -4.398 | -49.769199 | 2025-11-18 00:55:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d0c7bc0-c702-3e0c-a4b6-90f1c5513b5b | 1.5298 | -55.9655 | 2025-11-18 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e43a72f-f5c2-344d-872a-6778561c88de | -3.7514 | -50.939602 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d5bc8e5-e861-3d3e-984d-8620739e0c1e | -1.8016 | -54.714298 | 2025-11-18 00:55:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bff93aa-9206-3ffe-b049-2ef0661ed5d6 | -10.3322 | -49.6348 | 2025-11-18 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56cc7bf9-9213-3636-89af-20c7e96e7831 | -2.8225 | -45.399899 | 2025-11-18 00:55:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20fa5c30-7f14-3773-abd3-241867ea336c | -3.1453 | -51.487099 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23785568-d411-36cb-91e4-db3ffc1dc346 | -3.4647 | -46.069199 | 2025-11-18 00:55:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 937ae4d5-02c4-3d6d-aa5c-ed363c2b1097 | -3.0833 | -51.263302 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75265655-7ec8-336f-aaaa-fc15795ef8fd | -3.4692 | -49.989101 | 2025-11-18 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0446a38-02d1-3e95-802c-ad784da25553 | -3.1683 | -46.596802 | 2025-11-18 00:55:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
