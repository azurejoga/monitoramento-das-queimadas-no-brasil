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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af4f1bf4-c13b-3688-82c1-2ed0ff9a37b7 | -7.28158 | -39.23289 | 2025-05-17 12:00:00 | TERRA_M-T | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 95bafc55-410e-3572-9a1e-4adffdb8d735 | -6.71362 | -42.12717 | 2025-05-17 12:00:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 70b10b7d-ba9f-3bc7-a722-4d1398a1cdcc | -6.71214 | -42.13718 | 2025-05-17 12:00:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 2f9545db-5ce6-390e-b797-5d5b180c0073 | -7.85629 | -41.00622 | 2025-05-17 12:00:00 | TERRA_M-T | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 62bb6672-db92-33ff-9591-5c13658d17b1 | -7.24847 | -44.78136 | 2025-05-17 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| dce9dfe9-c2e9-33cd-b36e-c8a22346bb84 | -6.23382 | -43.35606 | 2025-05-17 12:00:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 149d8bf9-7cfe-3baa-aabf-1b8bc92ae036 | -5.63172 | -39.60809 | 2025-05-17 12:00:00 | TERRA_M-T | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c736cf14-4d79-3820-acea-42ff03f92e7c | -12.33947 | -49.96913 | 2025-05-17 12:02:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| fb63a88b-9c69-3334-9764-25be51da5c9d | -10.50725 | -46.17844 | 2025-05-17 12:02:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| f6a9e378-bf37-3229-9bc9-cb3b381a4412 | -12.36 | -49.9417 | 2025-05-17 12:02:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 37b6892c-acf4-327d-a60d-a399e9d75bc2 | -10.50465 | -46.1946 | 2025-05-17 12:02:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 5cd20813-af05-3476-a808-2321ebfabf51 | -16.08847 | -42.28823 | 2025-05-17 12:02:00 | TERRA_M-T | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| f164aaa0-da38-3a13-9262-c0563c961c79 | -10.51071 | -42.51959 | 2025-05-17 12:02:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 82450175-0d9d-3f10-89bf-c4e0a0ce7b87 | -10.51216 | -42.5099 | 2025-05-17 12:02:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 7cd0892b-a402-3a7d-8aee-1b816879522d | -14.51672 | -43.00231 | 2025-05-17 12:02:00 | TERRA_M-T | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| f47f2f42-9853-3495-85d1-9d037404df9c | -10.50153 | -42.51823 | 2025-05-17 12:02:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 29b8bf11-c845-31f0-bee6-e04f9cc7b0a1 | -12.35471 | -49.97169 | 2025-05-17 12:02:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 191fb3aa-7da2-322a-8eb6-0672706c56d9 | -13.53831 | -44.04462 | 2025-05-17 12:02:00 | TERRA_M-T | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 20024dd9-d112-37e4-aad4-ab0b75966f54 | -13.52873 | -44.04317 | 2025-05-17 12:02:00 | TERRA_M-T | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fcef60e9-6a72-3fab-8787-896efd723cb9 | -11.8049 | -43.78627 | 2025-05-17 12:02:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f15c02b5-3d84-30d4-9cb6-ec770efbe988 | -14.24622 | -43.1476 | 2025-05-17 12:02:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| b640db29-a511-3038-bb95-7053189df808 | -18.3891 | -44.1842 | 2025-05-17 12:04:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 23064516-535f-3a27-ab8c-81f66af67051 | -18.39824 | -44.18571 | 2025-05-17 12:04:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 10560cc1-3d20-3e16-9e11-c165aa6a76f3 | -18.39672 | -44.19569 | 2025-05-17 12:04:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 87dd2c24-95f2-324e-a739-1bc8e183e7ad | -18.38758 | -44.19416 | 2025-05-17 12:04:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a18f9edf-bfa7-3b48-b40f-2852ab2fc438 | -20.34519 | -45.72429 | 2025-05-17 12:04:00 | TERRA_M-T | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e8b9ebb2-ad87-3d67-9b42-a89481873275 | -12.4418 | -57.2096 | 2025-05-17 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 8d7e72ac-adfe-3ac6-8dec-7d200d8a946a | -12.461 | -57.1879 | 2025-05-17 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 193.3 |
| a7e5d62f-8c76-33c4-9a8b-e58c63e8da23 | -12.4608 | -57.2079 | 2025-05-17 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| e80c3808-1a0f-361d-8227-1372c08889d3 | -12.3519 | -49.9617 | 2025-05-17 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 13d37c9c-b0ce-3fd7-8c20-4eed72bbe221 | -12.3327 | -49.9641 | 2025-05-17 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| b82aef36-d7a0-3de1-a36a-5431d7631bc3 | -12.442 | -57.1895 | 2025-05-17 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 174.4 |
| 59bea61d-0786-374b-9528-30e0567c74e7 | -12.442 | -57.1895 | 2025-05-17 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 96888537-f0a3-31cd-98e9-5f42814272af | -12.3519 | -49.9617 | 2025-05-17 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 233.6 |
| 7c530b7f-c463-3e83-b6ca-272437294582 | -12.3327 | -49.9641 | 2025-05-17 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| fe73b59b-5466-3d9b-a841-40c187cad5dc | -11.2887 | -53.97 | 2025-05-17 12:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| ee102e84-aec3-31df-ac7b-61ea467b2888 | -12.4608 | -57.2079 | 2025-05-17 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 508d56d6-f0a4-3b4d-9335-9ecade947af1 | -12.3515 | -49.9833 | 2025-05-17 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.7 |
| f99614af-917a-365b-b663-a575169969b5 | -12.4418 | -57.2096 | 2025-05-17 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 27da8861-ae55-35fc-b46c-3d6a19214ef1 | -12.461 | -57.1879 | 2025-05-17 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 268.0 |
| 8d3d016d-3a97-3752-80cb-e7fd738d5c5a | -11.2887 | -53.97 | 2025-05-17 12:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| f1787d02-471b-3a19-98e4-179cc8cccc91 | -12.442 | -57.1895 | 2025-05-17 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 225.7 |
| 328fd1a8-0cd0-32e6-ba4d-15e9eafa04d8 | -12.3519 | -49.9617 | 2025-05-17 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 028a55d6-1a72-311c-af86-7f17f38778c0 | -12.3327 | -49.9641 | 2025-05-17 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4a556152-2fb8-36be-a6d9-8946caedba95 | -12.3515 | -49.9833 | 2025-05-17 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 3d47a3bd-d5d0-3b26-94e8-f83d6aa04b77 | -12.4608 | -57.2079 | 2025-05-17 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 35f515e3-944a-39ba-987d-44badbd2173f | -12.4418 | -57.2096 | 2025-05-17 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 878eae22-231c-3c87-971c-774179e6cb16 | -12.461 | -57.1879 | 2025-05-17 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 271.5 |
| 630c5a84-33fa-397a-915c-60c5d7c79cf9 | -12.4418 | -57.2096 | 2025-05-17 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 2522ec23-66a4-3bd5-a279-1874f1f72702 | -12.3515 | -49.9833 | 2025-05-17 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| b47e4e69-7a95-360f-bc2a-550a9d0d7859 | -12.3519 | -49.9617 | 2025-05-17 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 574d36d1-31ce-3368-a334-a1e6509bea1a | -12.461 | -57.1879 | 2025-05-17 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 349713d3-219c-3fc3-a742-e514a47772d9 | -12.442 | -57.1895 | 2025-05-17 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 250.1 |
| f481163b-f415-3e6b-9c7a-eb12cd67bad1 | -12.4608 | -57.2079 | 2025-05-17 12:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 6cb5556b-df3a-3729-81fb-0f760ee69a56 | -12.3515 | -49.9833 | 2025-05-17 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 7b708ba4-6719-319f-9061-3bca1e39d32b | -12.442 | -57.1895 | 2025-05-17 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 208.8 |
| 7020e627-ac85-3d93-8df0-1aa65b07a618 | -12.3519 | -49.9617 | 2025-05-17 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 195.0 |
| c4f5eaaa-8c64-3b19-b06f-7042b6f5bd05 | -12.4418 | -57.2096 | 2025-05-17 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d015534f-7305-3da7-a6fb-9c43228a9326 | -12.4608 | -57.2079 | 2025-05-17 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| fd1341cc-3ee2-33ad-934e-bf5a8bde420f | -11.2887 | -53.97 | 2025-05-17 12:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 98cfa222-7f97-3b3e-b401-7b3a157d6c58 | -12.461 | -57.1879 | 2025-05-17 12:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 279.6 |
| fa070528-1169-39e5-b1e5-5ea973b7cc99 | -11.2887 | -53.97 | 2025-05-17 13:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 601c2157-a199-3355-b2a0-d75180e9dd4e | -12.4418 | -57.2096 | 2025-05-17 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 9ff7008b-3f40-30c3-8fd5-eaaa5a12b67f | -12.4608 | -57.2079 | 2025-05-17 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| dc617545-eefa-3402-9c7b-377561b7210b | -12.3519 | -49.9617 | 2025-05-17 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 216.6 |
| 44aba439-0ace-3716-b488-1abec3c128dd | -12.461 | -57.1879 | 2025-05-17 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 220.2 |
| a1e35817-8211-3526-9609-a047e7b254f3 | -12.442 | -57.1895 | 2025-05-17 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 276.7 |
| 6645b47b-dfb0-392d-a24e-63d9b23c0308 | -12.3515 | -49.9833 | 2025-05-17 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| abb929c0-ca85-312f-87dd-11f94d3cb38d | -11.2887 | -53.97 | 2025-05-17 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| f655d88a-b84d-3946-a2e0-c17a944fd122 | -12.3515 | -49.9833 | 2025-05-17 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 163.5 |
| a05f8b00-537d-309c-a9a6-859ca6e2a925 | -12.4608 | -57.2079 | 2025-05-17 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 0eddb58f-cd29-387d-ad2b-eaf033ee6a59 | -12.442 | -57.1895 | 2025-05-17 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 296.2 |
| 8a9d5ffa-2a8f-39dc-a473-82bd641a373d | -12.4418 | -57.2096 | 2025-05-17 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| a565297b-de32-36e5-90c9-2ca53c346267 | -12.3519 | -49.9617 | 2025-05-17 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 1ef726d2-f86b-3976-b88d-9622d645c529 | -12.461 | -57.1879 | 2025-05-17 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 234.8 |
| e41cdca7-8ca7-3eed-a1f0-8db675c7727d | -12.4608 | -57.2079 | 2025-05-17 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 9809ab02-71bb-354b-9c6e-08cf64f0f5cc | -12.461 | -57.1879 | 2025-05-17 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 208.6 |
| 7b2c8103-d211-3f34-893e-90fb9fa0d8fa | -12.3515 | -49.9833 | 2025-05-17 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 80f7340a-08cc-30bf-9a67-dbb6408d5d1d | -11.2887 | -53.97 | 2025-05-17 13:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 464c9e2d-360c-3205-904f-a058bc6b5c4e | -12.4418 | -57.2096 | 2025-05-17 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| fb6a29c7-f0f9-3c18-9612-8e9ea79d6a4c | -12.3519 | -49.9617 | 2025-05-17 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 214.1 |
| dcb140ce-f40c-36d3-9b6e-dee025a7202b | -12.442 | -57.1895 | 2025-05-17 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 224.7 |
| 3d026034-904f-393d-abea-196ba5252cde | -12.3519 | -49.9617 | 2025-05-17 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 220.3 |
| a2edf66a-3ad4-36e9-9f53-e9e257ec9597 | -12.3515 | -49.9833 | 2025-05-17 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 226.2 |
| f7126b2b-dbe4-32d2-a467-3c099fafb933 | -12.442 | -57.1895 | 2025-05-17 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 215.6 |
| 85cc634b-7988-3564-8dce-f6eefda35c03 | -12.4608 | -57.2079 | 2025-05-17 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 5d06e7cc-f4da-30dc-9a9e-ada0444c8735 | -12.4418 | -57.2096 | 2025-05-17 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 19de26e9-897d-3d83-95dd-d6d9624ec971 | -10.27 | -46.8113 | 2025-05-17 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 07f54b0f-aa91-34da-b49e-00317737d360 | -12.461 | -57.1879 | 2025-05-17 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 186.2 |
| 906683f5-f178-3e56-89b8-ebda230c7eaf | -11.2887 | -53.97 | 2025-05-17 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 2fe93a5c-3445-3947-a8d5-b85a4fd48122 | -12.3515 | -49.9833 | 2025-05-17 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 203.7 |
| a3ef115f-f1cf-3f39-b74f-9c3ef83ff92b | -12.4608 | -57.2079 | 2025-05-17 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 605da332-a692-3706-9f7e-bc9259053b59 | -12.461 | -57.1879 | 2025-05-17 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 206.0 |
| f251c3ba-e8a0-363b-86ff-5df88d1304b9 | -12.3519 | -49.9617 | 2025-05-17 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 228.4 |
| 96c7373a-794b-33d1-95a5-4e32bc46f7a4 | -12.442 | -57.1895 | 2025-05-17 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 228.6 |
| 2556e025-aadb-3d69-bf44-7204f48d56bc | -10.27 | -46.8113 | 2025-05-17 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 8fd105af-74e6-317b-9c0e-664af4cf89ce | -12.4418 | -57.2096 | 2025-05-17 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5906ce99-2ac6-31ff-98bf-dfd4f32757bc | -11.2887 | -53.97 | 2025-05-17 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| d0ed4fe3-80f1-3818-badc-c8c710a176e9 | -12.461 | -57.1879 | 2025-05-17 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 199.2 |
| 543acdf4-cdd0-32a5-b1f9-e590bb3f77bd | -11.2887 | -53.97 | 2025-05-17 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |


[Clique aqui para ver as próximas entradas](README16.md)
