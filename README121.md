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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7ec4ef4-c6d8-3f39-b88f-843a4deb95ba | -8.541 | -44.6515 | 2025-09-30 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 82b1f878-fc79-3fb2-aa96-a03f23892ebe | -9.1434 | -47.6457 | 2025-09-30 14:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 52ae401b-79d4-3d26-9b54-6ad144ef368c | -8.672 | -47.7144 | 2025-09-30 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 38ab1122-c34b-3b9f-8a2d-3b0e9d36987b | -6.523 | -45.207 | 2025-09-30 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 5fb3f987-d881-3c3e-933f-ec12f9af2bb6 | -11.4608 | -44.9739 | 2025-09-30 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| c1be9edb-15b7-3107-913a-3cbcc476e40b | -11.8868 | -48.0323 | 2025-09-30 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 560f9ebf-1076-36c9-8521-d4efdbd5c8c2 | -5.8616 | -45.9327 | 2025-09-30 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 84280391-d79a-3456-949c-37a0a2c34fe1 | -5.2869 | -43.1613 | 2025-09-30 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| e46d4703-aaa4-3f68-8315-57b3b6919770 | -6.7811 | -45.6154 | 2025-09-30 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 573bf3e7-b793-3b08-8090-c7492d84da09 | -9.939 | -55.1632 | 2025-09-30 14:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4141e592-e3c9-356b-95da-5279ff83c302 | -7.9191 | -44.6245 | 2025-09-30 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 279.5 |
| c63f008e-5206-3467-bf80-2b3ec6e83111 | -12.4246 | -50.19 | 2025-09-30 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.6 |
| f0c936a3-2470-3aae-97bf-fc94c83f412d | -10.1234 | -47.783 | 2025-09-30 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 55485206-d5d3-378f-9d1f-6c86f4e9f94d | -15.9273 | -46.2101 | 2025-09-30 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 13569b27-a9c7-3eae-9288-6ad75fb9e933 | -14.7171 | -45.2291 | 2025-09-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 187.1 |
| b76b4910-716a-31b5-961c-7d72147e1bea | -8.4557 | -46.9405 | 2025-09-30 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 562a4282-96fd-3f43-b3eb-3ba8b5c1e0ec | -7.8348 | -47.0207 | 2025-09-30 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 189.2 |
| c24cf59f-9d67-3f9e-9a1a-7e89013d197d | -8.9287 | -49.8348 | 2025-09-30 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| fe087e8c-33d0-33ae-bb2f-b6aa0cf9e341 | -7.835 | -46.9986 | 2025-09-30 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 17b6191e-0550-3780-82f2-60a7084abf6d | -5.475 | -43.0774 | 2025-09-30 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 357.8 |
| b8e06580-22a8-31b9-8c95-471ce8aae938 | -7.0481 | -45.1856 | 2025-09-30 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 84b7ade2-1900-3d8b-bc67-1615929198b9 | -8.1428 | -46.3693 | 2025-09-30 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ad5d3b5f-30fd-3282-8733-5555ae52a24b | -6.5227 | -45.2297 | 2025-09-30 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| a53fa669-7e84-3d2a-b52a-c3e7e8e61360 | -15.4835 | -45.9006 | 2025-09-30 14:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| a9ba9272-eefd-3d06-8ed6-4f11568bd080 | -5.2867 | -43.1846 | 2025-09-30 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 285f0579-f32b-3265-8557-4672bf8a19d3 | -9.4005 | -54.7186 | 2025-09-30 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 5e1c35f0-988e-31ca-9a88-c56049bd62cc | -18.2171 | -53.3392 | 2025-09-30 14:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 3f34fbfa-71ad-31a4-b06b-596922601dd2 | -5.7601 | -42.6561 | 2025-09-30 14:20:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 3dd53318-b2ca-364b-bc98-c42bf9e75447 | -13.3808 | -48.0908 | 2025-09-30 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| a41135bd-52b8-3d3d-bde0-cbcb7981da43 | -7.4758 | -47.2728 | 2025-09-30 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3f0c1223-0d33-39b0-84a7-7845e557e140 | -7.8538 | -46.9969 | 2025-09-30 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| e3865ed5-05f2-3935-b0f7-21c78e1865c2 | -11.7023 | -44.3113 | 2025-09-30 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| d6dd022d-1b7f-36f9-acdc-8f1886ebc63f | -11.2138 | -47.2086 | 2025-09-30 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5452e45c-06f7-3d2c-9ae4-7a753e0297b5 | -6.504 | -45.2312 | 2025-09-30 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 5fb5031e-6f4c-3edc-a23c-22bac9f3fe52 | -5.8144 | -42.8637 | 2025-09-30 14:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 5bc98f4b-dfba-39ea-8c49-73468c5a19b2 | -9.9581 | -43.5987 | 2025-09-30 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 6e33ec07-3ba6-31fa-af68-044997d02e30 | -9.0685 | -47.6093 | 2025-09-30 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 06b87382-6238-3c3a-a6c4-1184813f9c1d | -16.7575 | -51.3482 | 2025-09-30 14:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 162.0 |
| f1311f4d-c320-3993-8e4d-c74acc03b355 | -5.751 | -43.6395 | 2025-09-30 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 8f971af8-034a-3123-99f8-6799469d11d8 | -7.0291 | -45.21 | 2025-09-30 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| d12aa411-5988-3823-9408-90ddb8506802 | -11.7537 | -46.8461 | 2025-09-30 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8f1cf2d9-23fa-3f57-a2df-2aced3b5867e | -7.8375 | -46.7766 | 2025-09-30 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| a66e0aa5-3b67-311d-8e19-edf659f62cab | -10.1042 | -47.8072 | 2025-09-30 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 84d1a4ed-9827-31d1-b62f-01d8cfc50ae1 | -7.5146 | -45.4385 | 2025-09-30 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| a9e41bcd-fb8c-3604-a3f6-781a334b7d37 | -6.815 | -45.9723 | 2025-09-30 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| f8971b74-dba6-3495-a0ce-0d22945159f7 | -18.218 | -53.2962 | 2025-09-30 14:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 31d3bb0d-6a34-3ca2-9e39-3032878e48e9 | -12.9524 | -48.3963 | 2025-09-30 14:20:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| e801f520-4280-355f-88d0-e6c48c74b977 | -11.6835 | -44.2908 | 2025-09-30 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| bf3d54ae-012e-3686-9b44-34b665583016 | -9.4007 | -54.6984 | 2025-09-30 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 30468d59-819b-31b9-a5ed-f773d7b077aa | -9.7684 | -46.1293 | 2025-09-30 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a5b91c8a-9381-330c-acb1-6fc72e5566eb | -9.5703 | -54.5843 | 2025-09-30 14:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 378d4a92-491b-3134-9554-171f1b591979 | -9.0236 | -46.7052 | 2025-09-30 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| bb9e49c0-2d07-3dd8-b04a-b066f6722100 | -5.9192 | -43.6961 | 2025-09-30 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 83943ec3-a5b1-39ab-a1ba-a0bac54c18f0 | -5.7223 | -42.6826 | 2025-09-30 14:20:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 159.5 |
| dedaf8bc-36f2-36c4-b063-1a1d84834bb2 | -15.7917 | -43.6672 | 2025-09-30 14:20:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 694.2 |
| 4b3a4104-c70c-3b94-9f6d-c3bf1e5f4af2 | -6.3694 | -45.6033 | 2025-09-30 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8356ee63-c6f3-3275-8645-7d8d9a7e6c4a | -7.938 | -44.6226 | 2025-09-30 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 280.3 |
| 9bebdda1-8274-3be7-b32f-e4547bdfb3ba | -12.7022 | -45.2715 | 2025-09-30 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| c39e6f46-0a3c-35e0-b813-822068ce90b3 | -10.0528 | -50.2192 | 2025-09-30 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 214.8 |
| b2a2a477-d0c1-3795-afb0-e2651d6613bb | -8.1705 | -44.1145 | 2025-09-30 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| aae9cb57-844f-371f-9cea-faaba3b36df4 | -12.2153 | -47.8112 | 2025-09-30 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 5fcf0faf-43c3-3c5f-a2e0-3c246f50bd74 | -12.7634 | -50.5136 | 2025-09-30 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 164.5 |
| abbe0311-6bd8-354a-9557-7274a433002e | -18.4862 | -44.0191 | 2025-09-30 14:20:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 122.8 |
| cc49b9ca-016c-3c63-8bb8-5347ced3de02 | -7.4414 | -46.9888 | 2025-09-30 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 7258ba58-79a8-3e13-8ad2-f7df15e1a88d | -8.1616 | -46.3675 | 2025-09-30 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ec84e895-867f-3062-ac88-6c767663b07b | -7.8353 | -46.9764 | 2025-09-30 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| bb54f745-c89c-3de3-9e43-d6bcd304a232 | -14.7361 | -45.2489 | 2025-09-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 07f65063-9aae-3d15-95ff-f7f1e2f96da1 | -10.1855 | -44.8709 | 2025-09-30 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 3d6fca08-9a72-33f7-821d-f5a1610f5cb2 | -9.9585 | -43.5752 | 2025-09-30 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| da29e906-9f84-39f1-9c4c-1430fa1e3206 | -8.8516 | -51.6998 | 2025-09-30 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| bcfb7874-31c7-38b4-8d4e-c8f6003c5c33 | -3.8269 | -40.4598 | 2025-09-30 14:20:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 153.2 |
| 172d4864-5647-3916-b258-a4150021d2e2 | -18.1981 | -53.2993 | 2025-09-30 14:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 250b2149-909a-3628-a3e1-8abb43e8e724 | -14.7166 | -45.2525 | 2025-09-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 647.8 |
| 48d9e53a-9411-3a72-bb5d-9a53c7aad401 | -7.819 | -46.7561 | 2025-09-30 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| b995d109-f28a-35c4-8071-a73920382fb3 | -5.8612 | -43.8858 | 2025-09-30 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ee4ef0c9-32bf-3319-a833-d4ad0d50950d | -12.4055 | -50.1924 | 2025-09-30 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 525.8 |
| ee0919a1-91e0-38d7-ace9-f07a3e819bd1 | -14.6603 | -46.9663 | 2025-09-30 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 249.3 |
| 2d63bf06-4382-38b1-8e6c-f21c1eadc83e | -5.7413 | -42.6576 | 2025-09-30 14:20:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 0837b670-a000-3179-badb-059d0ddf8219 | -12.863 | -46.9582 | 2025-09-30 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 5bab0188-6547-3334-ac6d-8862ade76c94 | -11.071 | -47.8262 | 2025-09-30 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1cf9ab60-622d-353b-9ed2-b74bdceeb047 | -11.1948 | -47.211 | 2025-09-30 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| f79fcf59-5366-39cf-8775-43e7bab8d2b3 | -14.7367 | -45.2255 | 2025-09-30 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 4f4b7887-eb9a-3a8a-af67-b62f51314c68 | -5.7599 | -42.6797 | 2025-09-30 14:20:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 65bda289-dad5-37ea-83d1-01576d53a477 | -6.2142 | -44.2041 | 2025-09-30 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c82ffa2e-7346-37e3-81b9-f6f81efc78d5 | -14.5141 | -48.4299 | 2025-09-30 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 132.9 |
| ba03b54f-ee69-361c-a970-21949aa5b933 | -15.7719 | -43.6714 | 2025-09-30 14:20:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1295.2 |
| e3062430-334c-3789-971b-32fa28f2af2c | -7.2999 | -42.8486 | 2025-09-30 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| 438e968f-e863-3d3f-a540-c1f75339e538 | -7.8188 | -46.7783 | 2025-09-30 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 94d5b0ea-9fd2-3d66-acec-ad10b668ede2 | -12.3862 | -44.6953 | 2025-09-30 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 40fcbdab-1d51-33bc-b303-1108b1fd64c1 | -7.0103 | -45.2116 | 2025-09-30 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b48301f6-ff94-3c2a-83de-7a29516a399c | -7.9194 | -44.6016 | 2025-09-30 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 529de8b7-3265-3b98-8bcd-e0ee88b36f98 | -7.115 | -47.785 | 2025-09-30 14:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d0347ab3-75e5-3af2-b326-eb56cf635983 | -9.1246 | -47.6476 | 2025-09-30 14:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a76aa23e-b177-34ef-8f04-803701ad50d2 | -5.4752 | -43.054 | 2025-09-30 14:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 158.9 |
| df75df2d-cd87-374e-b4a5-5f21be2a189e | -7.281 | -42.8505 | 2025-09-30 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 72e5abb2-f8fd-35a1-be3b-cb5c9fa3a330 | -5.8615 | -45.9551 | 2025-09-30 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 618559cd-8773-3c1b-804d-682cbb6642cd | -8.8514 | -51.7207 | 2025-09-30 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 84fb38ce-115c-3d4d-8632-7b28e5d0af0d | -9.8198 | -47.8606 | 2025-09-30 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 43d287c9-e587-30ef-8abc-85b590b8795c | -12.9548 | -47.1922 | 2025-09-30 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 63ace294-737a-3c3d-8843-41edaf1db83e | -15.1688 | -52.8241 | 2025-09-30 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 203.8 |


[Clique aqui para ver as próximas entradas](README122.md)
