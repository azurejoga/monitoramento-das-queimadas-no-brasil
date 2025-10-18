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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc79a25b-394b-3423-bb4d-7680f9c05720 | -4.88325 | -46.70488 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 295547ad-f304-345d-b4e1-e45f0d1ef223 | -7.16347 | -46.21466 | 2025-10-18 04:29:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 294db643-f962-35de-8b6a-0f71186368b9 | -7.53798 | -43.93645 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95ae051e-97ff-386c-8ccf-20fd3de3b765 | -4.25081 | -48.56513 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16fbec16-3aa3-3266-bcbd-068ff1cdf3f2 | -10.43476 | -45.01845 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d3b9a28-7f39-343d-8d67-949a85b6284f | -10.70375 | -44.56685 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac689afa-cd99-3828-b248-aeca4e841c8f | -3.86496 | -51.41481 | 2025-10-18 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e91827ee-23c2-384d-9be5-da82f23e11ad | -8.46087 | -44.16621 | 2025-10-18 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d64fd68d-5175-30cf-b2be-d973582fd1d6 | -10.50911 | -43.40034 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 934292d6-dffa-3e75-94b1-e90f450000f9 | -8.21949 | -46.8316 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82fab8f3-2b85-3c27-86b8-3e05a07a0097 | -10.70657 | -44.56652 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1560c18f-80cf-349d-8ae0-9e06e390a263 | -7.66858 | -44.63029 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d63e8e8-202a-3722-8e43-f199cb4d431a | -10.30041 | -44.03387 | 2025-10-18 04:29:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce2fcecb-6d62-367d-9f1c-11724bcb2ddd | -5.8975 | -43.9026 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eaadf176-fea5-37fa-8147-18c7d8528600 | -10.81712 | -43.93341 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 134fc58f-d9ef-32bc-88dd-ac977dfe09c9 | -10.12037 | -44.54475 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f955001c-fc74-3c2f-bbc2-ca603c16f434 | -5.70987 | -44.18873 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08ccb06e-549d-3dec-a381-d8bc39454388 | -5.7163 | -46.51228 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7be258f-2068-3d05-8088-1a13b00f7383 | -7.17685 | -42.17908 | 2025-10-18 04:29:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a7c7484-3e4c-3f37-832f-b6261cd4749d | -5.33584 | -50.99662 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4908d4b4-fd69-3151-8bed-ae7110a3a008 | -6.36839 | -45.76469 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e7bffe7-8cee-3fb5-bbf7-802270a6b8bb | -6.36048 | -58.21045 | 2025-10-18 04:29:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f054deef-19f7-3548-92b8-35252bced888 | -5.60032 | -47.50149 | 2025-10-18 04:29:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 761a0bd6-8c94-3c75-aa0f-3dad11949c5a | -8.41281 | -46.26819 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88c107eb-25af-31cd-9cd4-f7f83ecc9638 | -6.52658 | -44.90732 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2929b57b-934d-3984-8f3f-fdb0304516aa | -5.90976 | -44.7682 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a769ed5c-f543-3847-b8ef-e37172b15e25 | -5.4641 | -46.09545 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f8ffd7-3da2-3375-a965-9d48491deeb2 | -6.79091 | -46.47611 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c97d7c4b-7f09-3596-9de7-e4f74f051b5e | -6.95098 | -44.8708 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed52b6c6-4ec7-3101-bd0d-f7eb1c7642b8 | -8.77317 | -47.84214 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 656a6124-f3e0-394a-b9b2-05bbe04a34fb | -6.38714 | -44.639 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5082b66-fa58-3ed1-8fe0-839f52be528e | -5.71532 | -49.10159 | 2025-10-18 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d3894df-a281-3a8c-aeeb-2a227fc821b7 | -5.22498 | -46.19588 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c53a3ddb-76b5-398c-b530-df7f2ace5511 | -6.05322 | -44.52179 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea789b56-4f90-3778-af18-07bdcd9d7cf2 | -10.23104 | -44.05103 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1d8a2bbd-3ab1-35fc-b332-a6449f7d53b8 | -7.63231 | -48.39509 | 2025-10-18 04:29:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23225d98-3a80-38f9-b9a9-2e02978cdf55 | -5.75837 | -45.85794 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a79cdf10-eead-390e-aa18-76b6ae891441 | -6.68747 | -44.27254 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4270d0f7-03bc-3f76-89be-1870c625436e | -6.76595 | -56.86668 | 2025-10-18 04:29:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9453405-0331-3626-a0d4-138fc4f1c78c | -8.09901 | -45.4351 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6682f9e3-5bd8-3808-9416-3e868696b5ea | -9.15701 | -37.29874 | 2025-10-18 04:29:00 | NPP-375D | OURO BRANCO | ALAGOAS | Brasil | 2706109 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 942b9431-b906-3ec7-aa9f-1d310cfa7fb7 | -6.2372 | -44.15942 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1f74e368-caf2-36fc-ba46-11a54e2556d7 | -5.20836 | -46.19326 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac258e8f-7582-3abc-8dfe-52cf4dbd8bd3 | -10.43042 | -47.74017 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 396527d3-3c79-3206-aa93-84d80e87bb0f | -6.84304 | -42.41946 | 2025-10-18 04:29:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1b883374-4410-31a7-80bf-3ab169428800 | -6.31682 | -44.32116 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7531464-7b78-3d35-b15e-8ee3ac5c3f35 | -5.84292 | -45.7323 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82e77983-6713-3870-b21d-eef3c51e8024 | -9.01055 | -47.84073 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc71ce91-1d2d-3885-9a42-1b1bb43632a1 | -8.85382 | -41.0279 | 2025-10-18 04:29:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b004e3c8-f724-35e6-9ca9-556e761f1678 | -8.85963 | -46.01381 | 2025-10-18 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94c297a5-b2df-3518-b671-a8dd7350d60b | -8.23918 | -44.0116 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c2967fd-798e-36d8-b4ff-553ed6a5fc92 | -9.5551 | -47.77573 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7bec32f-c814-3cc3-8e91-d35ca35b8624 | -6.69827 | -40.87065 | 2025-10-18 04:29:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| da60f675-b7b3-3117-9ded-ebef366cd9a0 | -10.48891 | -43.4335 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8e24ef25-1414-38c1-a8f2-12474f967185 | -7.44988 | -42.68918 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e8b0c169-114c-3543-910b-72174f8c83cb | -10.25562 | -44.03591 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83149b7b-1e48-338c-be4e-0744dc184f09 | -7.11856 | -44.80187 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 90c59100-da5f-3608-b72d-7a0e961e06e8 | -7.81944 | -44.12199 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cba7dc0-c613-3089-9bfb-6c1e70903afe | -5.92818 | -45.44125 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc4ffc4c-5238-331d-9571-9ee331951a28 | -8.26051 | -44.01478 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8768124-b3a9-325c-9c1e-22ea03b6f593 | -10.42838 | -45.01355 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63fef143-954b-306d-b687-54dbf5f43f04 | -4.91823 | -45.0901 | 2025-10-18 04:29:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f7a5e8e-abce-3ede-88db-b4d83eda10c7 | -10.22544 | -48.93046 | 2025-10-18 04:29:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4217c167-b850-3d5e-a821-1fecbac6d176 | -8.19948 | -43.31059 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a96d4fe7-c9e6-319f-b8bf-addd11a651bf | -7.17836 | -42.17634 | 2025-10-18 04:29:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f85e97b-7204-30a4-9919-05f86972f4ae | -6.2278 | -44.13929 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2f9e031-58c6-31bc-964e-1144897ae10f | -10.50316 | -43.36185 | 2025-10-18 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 089bbf62-4369-31da-8a69-162954dab43f | -6.89782 | -45.4549 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bd1abc9-dbf9-3522-b8b9-06102fc5f6d9 | -8.11416 | -41.21677 | 2025-10-18 04:29:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1171a47e-6461-3b1b-aa39-75d21f7fc75d | -7.01613 | -41.83718 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 66f9c6a3-8762-3226-bec6-48db18d9f47c | -6.01887 | -43.72116 | 2025-10-18 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94e88406-70eb-37a2-9067-cd77a57c2d3a | -6.5436 | -43.91778 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5f9ed7d-179f-3d99-b855-31e583836599 | -6.16995 | -40.89357 | 2025-10-18 04:29:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d0fb6898-f4ad-3672-87c2-18ae0373a150 | -7.99368 | -44.15964 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9074fb9a-10c6-3973-8ea2-b2dfbb12026c | -6.78139 | -40.89302 | 2025-10-18 04:29:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a55a056-3aff-3618-a3a8-dd1c71464c50 | -8.14052 | -41.18188 | 2025-10-18 04:29:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5e5bfaf6-0ef8-3163-8c36-044e5c3ca42c | -10.10325 | -44.56252 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5161ab87-7274-3c20-ae50-7107c7d923c0 | -6.32255 | -44.30672 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efcbaf6a-c520-3af8-a3fd-206570275020 | -9.91432 | -47.66019 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d68180ee-688b-3969-aca1-ae5914f067f8 | -8.24127 | -43.32372 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 248e85b4-1956-3e80-852a-cf41cedb7dc7 | -5.29761 | -47.93267 | 2025-10-18 04:29:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cc10eb3-087f-3629-b505-352f291a481e | -4.83384 | -48.08252 | 2025-10-18 04:29:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ee4ea89-9669-3f50-834f-2dc4ae3e28ca | -7.01529 | -55.26369 | 2025-10-18 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7158747c-c6c9-3ccb-882c-365be3745edf | -9.91488 | -47.65667 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2563f5e4-544d-3f0a-963e-48f8dae27d74 | -5.88347 | -43.9242 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9d320ad-b6e2-3051-b896-a128980b20b3 | -9.773 | -48.74663 | 2025-10-18 04:29:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87dcbc13-73e6-3a6f-9f60-5632d39beeb6 | -10.24784 | -44.06243 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a776e36-249f-3ba3-9ca1-55666654bba3 | -6.84236 | -42.42408 | 2025-10-18 04:29:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4a7626c1-e9d1-3f51-9619-0265edb39a86 | -10.62123 | -42.30795 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d94f7c93-741a-3bb3-9285-74c91bf29397 | -6.65967 | -46.53362 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6263143-ac91-35b1-b9ea-a967314e2466 | -5.45379 | -45.41051 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c737653f-9460-3028-a058-52662e3b3336 | -8.25102 | -43.33397 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f928538a-b4fe-3477-bb37-2f35ecdcdc50 | -8.09956 | -45.43155 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44bbc1f2-3c84-3f5c-8251-34f2ade3e065 | -5.18619 | -46.18267 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddb3e818-52a4-3ed6-bf98-8e44c30236b9 | -8.56413 | -44.60321 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84d7223a-ca33-3529-9ffc-ca165914d4ce | -8.53358 | -44.08558 | 2025-10-18 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee28a32d-91bc-3677-870a-dd5afcaf71e7 | -7.08552 | -44.25342 | 2025-10-18 04:29:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c6e35eb-a387-3b77-96ec-e4e353504880 | -9.72516 | -44.54099 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5fa4adf-4eee-3aaf-931b-cdd072a5c571 | -4.93905 | -49.76014 | 2025-10-18 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5cfe764-6c5a-33b0-86bb-dd5cc5636fde | -5.2156 | -45.2439 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README45.md)
