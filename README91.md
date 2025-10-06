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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae0859af-aff5-39b8-897c-c5b7244d07f0 | -8.6891 | -49.4494 | 2025-10-06 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| c7ac1039-1d6c-395f-a28d-8f4282076803 | -11.4421 | -44.9535 | 2025-10-06 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ae0e8542-a279-314b-94d0-5dc2b1a00f77 | -14.9161 | -46.8312 | 2025-10-06 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 72213386-b4db-3692-8ea4-81aaf102f75d | -7.4672 | -43.0438 | 2025-10-06 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| e0ec9b01-5dfb-3405-bd88-5ef4f6a4b78c | -10.6335 | -50.5651 | 2025-10-06 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 35082784-800f-38ab-9557-c88b16529266 | -8.0866 | -44.791 | 2025-10-06 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 9233ef16-e95e-320d-8bb6-27036de4149f | -14.5438 | -46.9633 | 2025-10-06 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 9126bd27-9b1d-3ac0-a6fa-b5d2533cf0e7 | -8.5193 | -46.3547 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8e4571e2-04c5-3888-885a-ce0c891b5efb | -15.5896 | -47.2819 | 2025-10-06 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 19908094-6b35-3bd9-afd9-acfbe6504c42 | -19.5986 | -44.639 | 2025-10-06 13:50:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 115.6 |
| f386b88d-6d18-31fb-b4ed-c3a9eccaa96c | -15.3541 | -47.3235 | 2025-10-06 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| af57c658-25a4-3b05-be27-2f477d39f266 | -8.6703 | -49.4511 | 2025-10-06 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| ae8c32e7-50b5-3ed2-8d25-b138008cc5f7 | -11.0104 | -50.6744 | 2025-10-06 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 231.9 |
| 828854b9-7d31-3347-a1af-eec4231f016e | -7.4669 | -43.0674 | 2025-10-06 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 98761715-1956-3492-8b8e-d73a0aba6cde | -12.9844 | -51.0433 | 2025-10-06 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| f3324c81-2a9c-3f99-b736-5b34036086fe | -7.2389 | -44.8955 | 2025-10-06 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 1199fb21-a387-3811-9ec2-41e9f6c9c1b5 | -8.5584 | -46.2387 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 35523682-cd59-3b55-8181-dac84bff3f51 | -11.655 | -47.039 | 2025-10-06 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 44a43d96-a060-3dfa-9b55-7e880cadb5fd | -7.2094 | -45.8942 | 2025-10-06 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| cc003c24-3b91-3005-a3ec-0cbffc4a6134 | -12.4853 | -45.5587 | 2025-10-06 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 99f0c61a-a264-361c-b596-2cc2e28e4272 | -13.3237 | -48.0547 | 2025-10-06 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 148.0 |
| d0ec0c33-ba85-33b7-8d98-9bb50fa8d24e | -6.837 | -43.8511 | 2025-10-06 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| d16b3bd1-7397-3829-b48e-b639a46d0b83 | -7.2776 | -44.8007 | 2025-10-06 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e9334f2d-eaff-3f27-80bb-1dfc943ed678 | -14.6897 | -48.3797 | 2025-10-06 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| cf9a0775-78fe-368a-956b-d1cf8776a368 | -6.6976 | -42.8354 | 2025-10-06 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| a898e4dc-846a-3058-8f81-8338e9b33d31 | -16.0083 | -56.0155 | 2025-10-06 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 112.3 |
| 1ed5ec25-f50e-3d15-9a13-e8cd8624724b | -11.9327 | -46.438 | 2025-10-06 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 87e4ebdc-1938-3797-8fb0-a1b5b8618817 | -17.3816 | -53.5947 | 2025-10-06 13:50:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 139.0 |
| bde6756a-22e1-3da1-85d3-08b6ef62628b | -15.6616 | -47.5642 | 2025-10-06 13:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 68ec4354-ed40-30c4-8f0c-cdbc5907e266 | -9.6793 | -49.9569 | 2025-10-06 13:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 8e21a8cb-b046-3960-81d0-e4913825c675 | -11.8033 | -45.0856 | 2025-10-06 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| dc3f0c51-1bc4-381b-a60b-e104a678f310 | -8.5196 | -46.3323 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 71ea47b9-8309-3e1c-bee4-6ac444d07fcc | -7.8074 | -44.5209 | 2025-10-06 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 3ed44d64-4d77-336a-8a1f-1e5365f18cef | -15.3546 | -47.3007 | 2025-10-06 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 512e9de7-ac1f-3f64-b080-12228e60e514 | -11.9175 | -46.2135 | 2025-10-06 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 035a3cd8-b915-353b-81b7-6ef75305d772 | -10.1684 | -45.9913 | 2025-10-06 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 02b82796-7ed0-39b1-92b0-9003022e32ba | -7.272 | -45.3019 | 2025-10-06 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3a6bab33-2fdc-3ae1-bb36-1128e705e997 | -7.7684 | -46.2479 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5f1ed5e4-ef0b-3154-ba76-9e55ad2ebea4 | -16.0086 | -55.9949 | 2025-10-06 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| eceadbc8-a016-3fce-8a12-a64c83b32595 | -12.9653 | -51.0457 | 2025-10-06 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7dee80d0-f656-39d3-8228-acf7408830a0 | -14.2754 | -45.8647 | 2025-10-06 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 51665980-3483-3704-a112-73e8bbf1e4be | -10.1874 | -45.9889 | 2025-10-06 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 6e0c0ad2-7f44-3c5d-9f5f-134a2f8e177f | -7.2577 | -44.8938 | 2025-10-06 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| e1c5728f-6ab4-344d-8e9d-af51c48157b0 | -6.7164 | -42.8337 | 2025-10-06 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 603fd00c-cf38-3eb0-8f61-d5118dd0f553 | -14.6325 | -52.5137 | 2025-10-06 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 118.8 |
| ee3a0cf0-0f90-3958-9caa-a6481f270603 | -7.7014 | -42.4043 | 2025-10-06 13:50:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |
| 4cf90b84-eb71-3b31-8587-c8fb02bb6c85 | -11.1289 | -47.7748 | 2025-10-06 13:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 4150c2c9-af90-3d6c-bf26-234e3c62d21e | -8.5387 | -46.3079 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 431cc469-d938-3c88-9c07-15dc66d95fe4 | -10.6184 | -46.3646 | 2025-10-06 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 67125d69-24bc-3323-bb29-ae73beb10d86 | -7.0178 | -42.8054 | 2025-10-06 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| 554fd2d1-5586-3e5c-bfe9-d7124fb6dad1 | -10.7281 | -46.6433 | 2025-10-06 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 5b55a3ed-db19-3f90-a2ba-7642b4ceb433 | -13.2515 | -47.7979 | 2025-10-06 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 3e6ac5cb-f56c-3751-900b-940ca660f515 | -13.057 | -47.9155 | 2025-10-06 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d98340a9-220b-313b-a552-710b759177ed | -8.6141 | -46.3003 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 91b0ea16-075a-373b-8af4-74dc0fcfa195 | -7.7932 | -42.6082 | 2025-10-06 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 82fd4fdb-efdd-353c-83bf-0170fc0d6015 | -12.9841 | -51.0648 | 2025-10-06 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 189.8 |
| dbc80e42-57e1-3b4e-b30b-39067eba19c5 | -10.1383 | -45.4725 | 2025-10-06 13:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| bc020952-1bc6-3024-a737-6a8aaeecafa7 | -18.018 | -44.9965 | 2025-10-06 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 4f57ab63-21ba-37e2-960c-b60038ff4f05 | -17.8614 | -57.623 | 2025-10-06 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 73ed8d56-8bb1-3117-b904-c58e50348ead | -9.4863 | -46.0039 | 2025-10-06 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 1f17636a-a7cd-31f6-8759-6ecce88f4e61 | -10.3721 | -50.3363 | 2025-10-06 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| fe79c652-9acb-3c4c-b6a9-fabc90916f17 | -8.6139 | -46.3227 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 29c11484-9be4-3dd7-aaa5-819c89955563 | -11.7029 | -45.3536 | 2025-10-06 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 947a417a-5440-393e-81a7-d272228c591a | -8.5004 | -46.3566 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 5f6559a0-ca9b-379c-a67d-f27036e46660 | -7.4276 | -46.5239 | 2025-10-06 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 81a2780f-3a9d-3493-84f4-6254b353224a | -12.4102 | -51.113 | 2025-10-06 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| abbe092e-db12-3320-840b-86b5c9d04dc3 | -11.0101 | -50.6958 | 2025-10-06 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 4d367783-3e53-3e5e-b9b6-8d1e47b452cd | -7.8687 | -44.1227 | 2025-10-06 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 93fe9cba-0edb-3da0-aee8-c6256cd27299 | -11.7217 | -45.3738 | 2025-10-06 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ecc6723f-0f44-3cf7-8669-39b699496ed0 | -11.7221 | -45.3508 | 2025-10-06 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| d7e354c2-947d-3d0b-b7a9-f227bad05d7b | -6.6978 | -42.8118 | 2025-10-06 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 60.3 |
| d636c629-afee-35bf-a81a-a62dcc0d62f3 | -14.8637 | -51.4589 | 2025-10-06 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 216.4 |
| f968af46-92ad-3644-8ed2-260f5cc5fa1d | -14.5433 | -46.9861 | 2025-10-06 13:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 122.3 |
| b8f2d27c-8665-38a8-ba0d-67dca1bb22c9 | -7.7203 | -42.4023 | 2025-10-06 13:50:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| 7dc16def-3052-390d-817f-7b95d0a24559 | -7.2911 | -45.2775 | 2025-10-06 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 97e6b5b3-b962-39d4-bfe7-e0c4c7690535 | -13.2421 | -51.6933 | 2025-10-06 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| d4ee1d75-653a-3ad3-ba19-0a238119fc24 | -9.4866 | -45.9813 | 2025-10-06 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b1ef34c6-79aa-3ce0-ba9e-2af7b81b2517 | -7.7496 | -46.2496 | 2025-10-06 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 7c667090-6f2e-34ce-af31-57dde460c685 | -14.6893 | -48.4021 | 2025-10-06 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 49.7 |
| cf0ec76d-f87a-37cc-bfc5-cd3314867440 | -9.8495 | -45.7579 | 2025-10-06 13:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 947fad4c-c4c1-3570-afb0-ad50b6309913 | -14.8634 | -51.4804 | 2025-10-06 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 660888c1-9322-3b98-95af-0659bd0b4345 | -12.1458 | -50.9523 | 2025-10-06 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 251.5 |
| be4092e3-34fd-36b3-9fb4-5bee31a55f3b | -13.3044 | -48.0575 | 2025-10-06 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 15b575b1-7e61-332d-8f7f-d3ef6ac8cce3 | -9.9018 | -50.2341 | 2025-10-06 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 1ff29b13-07ac-351a-a31d-44b2881e465d | -19.49 | -44.8839 | 2025-10-06 13:50:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 117.2 |
| e10a0782-6f97-312b-8fe1-a2ca985b60af | -17.842 | -57.6048 | 2025-10-06 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 9e761d2d-2ef4-3dc8-9b50-c63a3ebc0bb2 | -14.882 | -51.5207 | 2025-10-06 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| aef1d420-165f-3a98-ad1e-38653bdef86e | -15.2351 | -49.2914 | 2025-10-06 13:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e5bc005f-7c46-3618-be59-288c5b3143bf | -7.348 | -45.227 | 2025-10-06 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 8684d9b1-0d80-3b98-9031-f76ff013e276 | -6.7167 | -42.8101 | 2025-10-06 13:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 86341414-d638-32fb-9592-4c05c34669bd | -14.6321 | -52.535 | 2025-10-06 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| b7593d19-5825-3b7f-a207-ba74fb4bb1ec | -7.7206 | -42.3784 | 2025-10-06 13:50:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 69956748-35f7-3719-ac60-da7df4af0f79 | -8.6253 | -43.9952 | 2025-10-06 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 0995531b-1001-303a-964c-8ed5e5ff69cc | -7.6801 | -42.5966 | 2025-10-06 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 110.6 |
| 9b278147-598c-3e89-8490-f6011542b60d | -18.2862 | -45.4348 | 2025-10-06 13:50:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 546d2f33-6da1-348d-bb9b-624b14f7e69a | -19.5111 | -44.8545 | 2025-10-06 13:50:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 922cdc32-fb23-38b0-b63f-d83bf9d21d07 | -9.6614 | -45.6667 | 2025-10-06 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 55e0aceb-59cd-35cc-87a8-f388be8d4b00 | -6.6303 | -45.7178 | 2025-10-06 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8fafe6ba-6c8f-38b3-96af-1a0cfce9dd87 | -14.3339 | -45.8545 | 2025-10-06 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| b721d92b-b644-3d69-b1db-b5fc3e51f515 | -15.5704 | -47.2625 | 2025-10-06 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |


[Clique aqui para ver as próximas entradas](README92.md)
