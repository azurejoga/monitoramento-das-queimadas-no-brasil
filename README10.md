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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 613f3036-031a-3f9d-8524-7147a8c43581 | -3.26701 | -44.70065 | 2025-09-18 04:12:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcb1ee01-adf7-39fa-b27b-712463e15b54 | -5.8055 | -45.90434 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 173a5fca-63d4-32a9-8395-3519634714ec | -2.92033 | -48.30605 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16678a13-d161-3c53-a07b-a80fb877ea38 | -3.01932 | -41.72993 | 2025-09-18 04:12:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aa73ce85-b651-3df5-9915-c929d1560a78 | -4.80743 | -42.73555 | 2025-09-18 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6aeee249-eb0a-3443-9dd3-0668fc3cb8c9 | -5.81141 | -45.90399 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a904fac8-6835-360f-9432-63345b01bf90 | -6.95732 | -44.77197 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ab725c4-2068-3045-8fbe-21edb7b03f64 | -5.81074 | -45.90807 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 126137dc-d40c-3330-86be-6427796b5ff9 | -5.9503 | -47.09751 | 2025-09-18 04:12:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 489d40fb-54b0-3be3-a270-51215c34c472 | -6.98833 | -44.44793 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ae06f1c7-5a46-3e52-a5b8-8b94524bc4ce | -6.3982 | -43.33065 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13dcc062-b96c-32be-857e-0dfaff656012 | -6.39161 | -43.35089 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1577b50-2bbf-353c-9309-822b6fc523ab | -7.00692 | -44.60169 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4f82537-4525-3161-bbdd-e1dbcbea185a | -6.31064 | -42.39761 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ff9d08d3-550a-34b9-b1bc-a2ea5d17bbc4 | -6.87192 | -44.17477 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01f2ef73-da3b-3aaa-bb55-9a41045d08a6 | -6.18313 | -41.23227 | 2025-09-18 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5143ee44-69fd-3adf-a753-d7ac9f043f5d | -5.76925 | -43.69714 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e67eaeb7-5e4c-3665-8e2a-9fb9a49583f2 | -5.81722 | -45.91329 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 399d4861-b250-3c67-a6c7-9572e231eb7f | -3.2971 | -41.00072 | 2025-09-18 04:12:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8664e300-79ac-3773-b738-c75a33e66fad | -6.25309 | -43.45285 | 2025-09-18 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8a259b3-96d9-3cfc-aceb-b3967f493fca | -2.64819 | -48.0527 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7c6048b-c939-3b65-a87a-d3ac1b228f4b | -6.20741 | -45.11892 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97ab5d24-94af-3868-80e1-977c74429f38 | -5.48801 | -45.40126 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2fb0bc4-99df-3fa4-9776-e81d52d61f70 | -3.34968 | -39.27606 | 2025-09-18 04:12:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 380fe88a-1fdc-3a5d-82d8-6350e145dba8 | -5.2088 | -45.17904 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6079c39-e240-37be-be62-d1b60597092a | -5.7656 | -44.83565 | 2025-09-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75849996-86f9-3f54-91ec-367269a4fea9 | -4.24251 | -48.26847 | 2025-09-18 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bb2f2d0-0020-385e-9f06-f23a966229bb | -4.80521 | -42.72814 | 2025-09-18 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1761399f-c8db-3c60-9a4e-db42d950e4be | -6.59143 | -45.5877 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18d5c38f-0317-3570-b651-66b7e2320a22 | -5.77355 | -43.90632 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c1af3c6-61ff-3f9d-b7cb-30aeeb393bea | -3.8477 | -40.3495 | 2025-09-18 04:12:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9232b01c-2f95-3b0a-80b2-58f8b1f5a988 | -5.83239 | -45.26774 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15b70043-048a-3521-81e5-3346a2033f53 | -5.77548 | -42.77879 | 2025-09-18 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 759282cc-3792-3f76-b12f-abfa05d43b66 | -2.16073 | -48.86164 | 2025-09-18 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3565e46f-00c7-3ab2-96e4-1d2fa32b0705 | -6.38884 | -43.34691 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56d3ce82-94a9-3c51-869a-1ec640561eb9 | -6.03742 | -43.14188 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 94d11734-8725-3d6e-99d5-a6dd773e5e70 | -5.59216 | -43.80878 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e058cc8-726c-3016-9744-7fe6da7a7167 | -5.57886 | -43.54868 | 2025-09-18 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39f1f798-0210-385f-8b42-265fba37a493 | -5.68714 | -45.35955 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5278b21-1127-385b-b9d4-db869427af06 | -6.6855 | -46.30333 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d25da02e-b00f-3fda-b6bf-85f31680d804 | -5.21227 | -45.17966 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8561b3ed-4632-323c-8a81-c10ce92e5526 | -3.8965 | -40.81909 | 2025-09-18 04:12:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 89b0736b-9a4a-34df-ba49-baea0910df8d | -5.79269 | -45.71173 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdd753a9-b635-3db9-b7b7-f4e361783b87 | -6.31396 | -42.39813 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2dde40c2-378d-32d4-9135-0f3761cd054d | -5.1272 | -45.03283 | 2025-09-18 04:12:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f7fb2db-ffbb-3d37-a702-2f1625b4e99e | -5.17357 | -45.66678 | 2025-09-18 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ebda0d5-4d19-3dcb-93bf-3647b0073c99 | -6.35215 | -46.10022 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81c71f96-4738-3207-87c6-8f1897b4ffee | -6.97534 | -42.07257 | 2025-09-18 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f84d0e05-ea93-3f67-93bc-0253f43c0366 | -6.85863 | -44.15093 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4da8ce5e-dae0-3d86-b13b-dae0eb1ee9f5 | -5.85536 | -45.88196 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bde95a60-ca0d-3c6d-9de4-4c911b89ce97 | -5.83586 | -45.26832 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 933eaf57-a399-3457-bb03-4e2f8bc713d1 | -6.88461 | -43.96759 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33c70bad-9384-3e45-b990-28a294a314a0 | -6.00436 | -44.33224 | 2025-09-18 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7f2c4e1-2f90-3537-9538-587dce5c8081 | -3.79334 | -44.12142 | 2025-09-18 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc8c2cbb-2948-3d96-a23a-8b42bf9a695c | -3.96717 | -38.51541 | 2025-09-18 04:12:00 | NOAA-20 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b6ef292f-eaed-3e92-baa0-5f3ed02c992e | -5.88138 | -45.85699 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e52e7194-be17-32bd-a49a-1e23f467c2f8 | -5.88743 | -45.72989 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88b8d78d-f23f-380c-ac92-069aebc2c13a | -6.20335 | -45.12215 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dac811a-5656-3b14-9eac-43d51486ca49 | -6.72996 | -44.15248 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc4d85f4-3ef7-3e44-b7f2-6365afb81fbc | -3.13801 | -44.42823 | 2025-09-18 04:12:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b616ae4d-05b4-37f5-9213-6c14c328e610 | -6.42304 | -43.34522 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1be1bf9-38f7-3f81-acd4-feccc0942dda | -2.44531 | -49.36381 | 2025-09-18 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e7332d6-906c-3578-8f85-cb3270c7492e | -4.6184 | -46.34866 | 2025-09-18 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73b1cf55-0eaf-3b3f-b0ba-466a0746a27f | -6.20113 | -45.11407 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e1b3769-269f-3520-b011-fdbb7aa0166d | -7.08522 | -44.15816 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89fdf2eb-70dc-38e5-b143-c56a32284caf | -6.77667 | -44.70179 | 2025-09-18 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a204a14-0b9f-3da9-b8e5-5e36ab4f2871 | -5.90646 | -45.72462 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2383b0a7-4869-3900-b987-a3be9655426e | -6.85807 | -44.15444 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1684fab9-4a4f-3324-8a7d-538af917f035 | -2.91776 | -48.30802 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38f48443-2b3d-3017-84fb-0b725cb26f4f | -5.95436 | -45.03366 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d55bd103-4d14-3413-9c2b-bf5f22dcb4b8 | -5.88211 | -45.6512 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fca71c11-3fc5-3580-b22f-8c40e3cc5cd2 | -6.4932 | -46.65437 | 2025-09-18 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 161b8e17-3d6e-3184-90c0-8e620cef9486 | -5.79308 | -43.76183 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ce8f873-6735-3e18-9758-79196a97f7d6 | -5.5905 | -43.79772 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e48d3b2f-20ff-34c4-8f00-1b2bd97c7a7f | -5.06571 | -41.16743 | 2025-09-18 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 14006c23-6b11-3d67-9627-fa475c825cfb | -5.80754 | -45.70984 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6de763f4-070a-3675-84d7-be8bbedf11d5 | -5.76666 | -46.15175 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a31c91f8-a6b3-3788-b3b8-dfb430486a42 | -2.16526 | -48.86238 | 2025-09-18 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35ecd5b0-129a-36b8-bc48-1fdfe910875d | -3.11174 | -46.77248 | 2025-09-18 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a21527a8-87cd-31b4-8389-860038dfc9cf | -5.87744 | -45.88133 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13e1fb94-07a3-3f47-a3fd-4196f0a3d545 | -6.60722 | -43.5767 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0e8142a-ce8e-3a2d-94d1-376f517bfa88 | -6.48838 | -45.99903 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0c72096-b4ce-3280-9666-ba3078b5d697 | -5.79555 | -42.45555 | 2025-09-18 04:12:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| da6330a4-8de1-311f-81c8-4f040e436a40 | -5.1922 | -35.86732 | 2025-09-18 04:12:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e94b30a4-17b7-3736-b0f1-0e5a4ba48f31 | -5.08939 | -41.14893 | 2025-09-18 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4a5b2e38-6cb8-3f1e-9e3c-85df8d7c7543 | -5.0811 | -44.95284 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62d6060e-8306-350f-931a-794be6f37da8 | -6.12322 | -43.9472 | 2025-09-18 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d004a6af-f6fc-3df8-b1a0-b3b6fa654903 | -6.5995 | -45.64911 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9593993c-5f86-3d22-9f21-afa3a3cac9c8 | -6.68774 | -46.31229 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9fda6b5f-d1cb-35a5-95b1-243d500d68cd | -3.79673 | -44.12196 | 2025-09-18 04:12:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38b5897c-387c-3624-ae03-9f97e28be49e | -5.75418 | -43.17171 | 2025-09-18 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f11fa60c-39ae-3b15-b6c5-cfb25ee28993 | -6.63131 | -38.55033 | 2025-09-18 04:12:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe3d0914-92a2-35a8-8c02-5abe7e6f9e1c | -4.61406 | -47.02228 | 2025-09-18 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebe5b2b2-9f1e-3a97-bab0-2eb806a716f9 | -6.95237 | -42.4407 | 2025-09-18 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b13c384-b8fd-3b8b-8709-43486d644072 | -4.1123 | -49.15286 | 2025-09-18 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31c83ce9-5f19-3532-8cce-ec760090bdad | -6.69204 | -46.30867 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 9b595b4b-9783-335b-9979-542ceffa17ca | -6.21085 | -45.11947 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31756ba4-3268-33e4-81ec-79a27e785a54 | -4.81014 | -46.81466 | 2025-09-18 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8f9ee19-9a1b-3793-bb01-fec7b526da99 | -7.03857 | -44.17586 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddac3dd6-bb8f-3bd8-bd8f-3cd970e3f6b0 | -6.14936 | -45.98889 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
