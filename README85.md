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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 991f46fa-04d5-3f1d-bab0-1caea9b3536b | -11.9726 | -51.0788 | 2025-09-09 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.8 |
| b4793ed2-d021-33cc-845c-3530014e225f | -17.2967 | -46.7032 | 2025-09-09 14:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 83f0bfd3-600b-3b2a-9b36-0a1961640550 | -12.1993 | -53.8611 | 2025-09-09 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| c65a3b2f-daa9-3b7c-8e8f-735ace2ff461 | -5.6015 | -48.1082 | 2025-09-09 14:30:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 067e3776-edfa-36c6-88c9-5875b71c546c | -9.0229 | -49.8048 | 2025-09-09 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4864d0e7-ac68-3dd7-bc2e-ca740fec7022 | -14.4468 | -53.2334 | 2025-09-09 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| aa225332-e87c-3ab0-aa49-e5ab01031dbb | -9.6289 | -48.0129 | 2025-09-09 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 544dee93-f2fa-3675-aa41-db5b271e2aa8 | -19.9545 | -49.2928 | 2025-09-09 14:30:00 | GOES-19 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 185.9 |
| 0eaac6f8-b603-3cd0-999f-055cffa13672 | -12.1988 | -53.9024 | 2025-09-09 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 190.5 |
| 6e3127d2-a9c2-320b-9352-667016277179 | -9.1207 | -58.9023 | 2025-09-09 14:30:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5dceeeb0-83bb-3585-bd21-7fe298d43693 | -12.9673 | -54.7499 | 2025-09-09 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 265.1 |
| 46ebff0e-531e-3d02-a160-a9b1cc000627 | -11.3014 | -46.5018 | 2025-09-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| af1a7869-2e49-36c0-8dd8-1f5bb46ac855 | -5.7364 | -45.2892 | 2025-09-09 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 22a6eaea-4db5-3f9f-89cd-6cea0c909dbf | -8.0604 | -48.664 | 2025-09-09 14:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 19557842-97ab-333c-b947-4e89f3355251 | -6.9134 | -45.5142 | 2025-09-09 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 695d4a80-ce96-3786-817a-323658860a13 | -6.9321 | -45.5126 | 2025-09-09 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 6acaa05e-2baf-31f7-af23-2d0f4f51a177 | -17.7328 | -44.4637 | 2025-09-09 14:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 202.0 |
| 51bf1666-07c7-3780-bfae-35800a7d75e5 | -5.6603 | -45.4525 | 2025-09-09 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 983ff432-abb2-36bc-82e2-a27a6087b221 | -11.9539 | -51.0597 | 2025-09-09 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e23ddae7-0e91-35c4-8185-4ef0890c53d7 | -5.9901 | -46.1917 | 2025-09-09 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 476029f6-4419-3348-85bd-f5d6757de17d | -6.2036 | -43.3709 | 2025-09-09 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 7f032b92-0e04-3877-8828-14bda900af96 | -12.6341 | -56.9926 | 2025-09-09 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4e2fd77e-a769-3110-aac8-9eb8461f2be7 | -11.3389 | -46.5419 | 2025-09-09 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5cb18bef-b733-39c4-b60b-c2296dd081b2 | -4.7345 | -44.4685 | 2025-09-09 14:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 65173a45-a9a4-36b9-9612-2d7e9e9c9c58 | -7.5799 | -44.6579 | 2025-09-09 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| eabc3f82-4d15-3df7-a207-f60809eed62d | -5.9748 | -45.8126 | 2025-09-09 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b56dba49-e817-3008-875a-0d1bcf9cd0ed | -5.2263 | -43.7006 | 2025-09-09 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 5239b3ba-349a-3081-8df1-012faee6c6b8 | -5.8397 | -44.1872 | 2025-09-09 14:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 4bcff7b8-2768-3748-9f93-07e07f077aaf | -8.4116 | -49.1085 | 2025-09-09 14:30:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 816b3209-d35b-31c3-8ad9-4afff0aaba0f | -9.0934 | -45.7088 | 2025-09-09 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| eb554109-b519-3852-a808-d84bbeee0caf | -5.6418 | -45.4312 | 2025-09-09 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| aa39f951-1686-3b84-b480-db6c568ace02 | -4.7346 | -44.4457 | 2025-09-09 14:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 237.8 |
| fc85004a-89fb-3c9b-8cd5-97d408d0daf1 | -12.967 | -54.7705 | 2025-09-09 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| d00c7eb6-0171-3ff6-9175-db7921b28eca | -17.7127 | -44.4684 | 2025-09-09 14:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 294.2 |
| 0e8045e9-bbf3-33c4-b40c-b462f258d9d3 | -17.2973 | -46.6799 | 2025-09-09 14:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b090eb8a-4470-303e-87d6-7ca8626dcfac | -5.9191 | -45.7717 | 2025-09-09 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 23fa2530-2fff-3295-a510-cb65362f165b | -6.3078 | -44.2196 | 2025-09-09 14:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 7ec6aaad-c414-380c-95a0-b0702e039dea | -5.975 | -45.7901 | 2025-09-09 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 8fdaa405-3747-308d-8c6c-8d6c44304321 | -13.9564 | -48.2493 | 2025-09-09 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 5b25a5ec-5239-3f04-aa10-99aa9aefcf5c | -12.529 | -45.2756 | 2025-09-09 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 254.3 |
| cbfbd9b3-4ebd-33b3-8d0f-616f50382de4 | -11.4277 | -43.6017 | 2025-09-09 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 90f22383-181b-39ff-bf2b-965a50e73037 | -11.4281 | -43.578 | 2025-09-09 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| fb95d022-bdb8-3111-ab49-47ebc243cb69 | -18.6904 | -52.594 | 2025-09-09 14:30:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 43a70be6-8313-34bf-a128-87b0c53c1229 | -9.3742 | -65.9484 | 2025-09-09 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| be9b3e40-0c19-3d6d-aaa1-c199ce9ab2fd | -9.7017 | -46.8323 | 2025-09-09 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 233e0eb3-07cb-357f-9626-b4d793cbd584 | -5.453 | -43.4525 | 2025-09-09 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 2241bfa3-12b8-3a1a-af14-b2cd9cebec02 | -8.4119 | -49.0869 | 2025-09-09 14:30:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 965a2dfe-336e-310f-adc1-9f4b70266128 | -5.7168 | -45.4035 | 2025-09-09 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 514b086b-41de-36f7-b5a9-6466301a69a4 | -16.8842 | -45.7635 | 2025-09-09 14:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 6014bde5-3224-30dd-a2ee-7d6594bb0d65 | -7.5611 | -44.6597 | 2025-09-09 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 6ee16d1e-8523-3a59-ba2a-dcef2c35627b | -5.9563 | -45.7915 | 2025-09-09 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| b3da4d9c-1438-3417-b40f-927d5b268109 | -9.9498 | -60.1367 | 2025-09-09 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ae5de318-e478-301b-9bef-9577e0fbbe09 | -9.3742 | -65.9484 | 2025-09-09 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5b0b6ae6-0cf4-3629-b0f4-367160b90d07 | -5.8585 | -44.1858 | 2025-09-09 14:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 95ad5572-f38b-3dd2-94b5-83e59a4435dd | -11.3549 | -50.4447 | 2025-09-09 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| bdc12454-85c2-38a6-8361-764df354e6e7 | -5.7553 | -45.2652 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| babe98eb-4bc6-3222-b3ce-ed437a12c5df | -9.3395 | -65.4451 | 2025-09-09 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| b93dc721-6e74-35e7-a0a0-59baa1282569 | -6.2198 | -45.5922 | 2025-09-09 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| ea2dcad5-9ca0-3a17-8d85-51849ce0bc92 | -5.9899 | -46.2141 | 2025-09-09 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 194.1 |
| ce233215-9d37-393e-8fb1-1c0ce17b70b3 | -17.2967 | -46.7032 | 2025-09-09 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 021a8d0a-e8ac-38d5-b2fb-489b71b1b84d | -5.0438 | -43.1314 | 2025-09-09 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 153cde89-1e71-3333-aae6-d9821579f42a | -6.199 | -45.8186 | 2025-09-09 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 232.5 |
| fbfafa71-8463-3b2d-ba05-5ec239632026 | -5.6738 | -43.9 | 2025-09-09 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 307.5 |
| f286e8fe-7bf6-333a-8e4f-01331aa5a52c | -5.6736 | -43.9231 | 2025-09-09 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 191.7 |
| d6ab9ac7-8e75-3468-a3ca-89e79367a6e9 | -4.7346 | -44.4457 | 2025-09-09 14:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 302.3 |
| 15fad4fb-7247-36ce-9bc7-b0e5aaea0f8c | -8.3929 | -49.1101 | 2025-09-09 14:40:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ecd396cc-db0c-3586-b70f-c3eda90eaa28 | -10.2309 | -48.2107 | 2025-09-09 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e554664c-200b-3dff-929e-db42e9caa637 | -11.4272 | -43.6254 | 2025-09-09 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| d81790c2-0546-3e15-bb5a-a93c4819829c | -5.679 | -45.4512 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ebd41190-4da9-3e4f-b3bb-4fb922a85e4a | -11.9351 | -51.0405 | 2025-09-09 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b6c2f6c5-9627-3c0e-8fe9-7621aec267c1 | -5.7364 | -45.2892 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 20f51491-b70b-327f-b9c2-32dba48ca5de | -17.7328 | -44.4637 | 2025-09-09 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 205214b5-0875-38f4-9857-b57d9ec448f2 | -11.1502 | -45.271 | 2025-09-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| e4edb058-67d1-376e-9205-2bda8a6d94ba | -6.8449 | -44.8847 | 2025-09-09 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| bdaa0ae0-7922-3565-8327-257d73c61b88 | -9.7017 | -46.8323 | 2025-09-09 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| aaab1bdc-7df4-3446-9ccb-20791db4ce98 | -12.1988 | -53.9024 | 2025-09-09 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 3f4298b5-07df-3b4f-83ad-7a1491f5c946 | -11.4482 | -49.2704 | 2025-09-09 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 5dc7ab1a-2016-3f71-9f09-71d9b1f4bf77 | -5.2263 | -43.7006 | 2025-09-09 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| f9cdc3a9-1f0b-30bc-ac9a-a9f66ee4fcd7 | -12.948 | -54.7724 | 2025-09-09 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 231.0 |
| 1114784d-c603-3308-a017-3e7d48bec2c3 | -8.0604 | -48.664 | 2025-09-09 14:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 873f30c4-df49-3c4c-850a-ec89eab7e9b7 | -4.8827 | -42.2002 | 2025-09-09 14:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 117.2 |
| b33b1126-f4d8-3158-ba85-fff546db2307 | -11.4672 | -49.2681 | 2025-09-09 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 319e6094-6605-3465-856b-444352141ccb | -6.1899 | -41.0154 | 2025-09-09 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 159.8 |
| bdc1fcd1-85d8-3be2-8fc3-b4defae51453 | -8.0606 | -48.6423 | 2025-09-09 14:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 181.9 |
| f3424e6a-6760-3dee-a738-2bdab2d03df4 | -5.9901 | -46.1917 | 2025-09-09 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 95d9ca0f-fd26-34e5-815c-af5879e5559f | -5.4343 | -43.4538 | 2025-09-09 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 525.4 |
| 970f47c9-c558-3b4e-a719-a9e8d017bf71 | -5.6017 | -48.0865 | 2025-09-09 14:40:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 90.5 |
| b35cf760-eb52-30a6-8699-f996d9144070 | -6.2038 | -43.3475 | 2025-09-09 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| f041ca55-bab3-3a56-857a-8f59d3e767f9 | -17.7127 | -44.4684 | 2025-09-09 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 379.3 |
| e6cfdb9d-0c54-3875-98fe-a793d198912c | -15.8201 | -52.2659 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 50cc0ea1-05ef-366b-9fdf-eaa2651104e2 | -5.7168 | -45.4035 | 2025-09-09 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 2ab0372d-f1d7-3fc5-9e42-4a41fe0ebcce | -11.3905 | -43.5365 | 2025-09-09 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| d238dfa0-ecfa-364a-8617-90f3c3c5aa86 | -4.8825 | -42.2239 | 2025-09-09 14:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 14762752-1f18-3bfb-8cf0-b9608db0295c | -5.975 | -45.7901 | 2025-09-09 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 61f3a69f-b193-3282-b17f-27ba2a02e3be | -7.5799 | -44.6579 | 2025-09-09 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d0c9c855-1e43-3f95-a3d5-2d6a62bf4db8 | -9.7857 | -46.24 | 2025-09-09 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 0aecfe79-8e4c-39c6-bd97-157eb64d6eb2 | -11.1693 | -45.2683 | 2025-09-09 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c8e3a0c6-9376-3b9d-a020-7daf00f454be | -7.789 | -46.0891 | 2025-09-09 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 3fa898c1-3b0d-3bc5-90bd-3048bb752092 | -12.1993 | -53.8611 | 2025-09-09 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 4bb57a2e-f411-399b-aec4-570c33a1857b | -9.0931 | -45.7314 | 2025-09-09 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |


[Clique aqui para ver as próximas entradas](README86.md)
