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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b31b7b73-410e-3239-a663-4b7ae89244d2 | -7.24866 | -45.3872 | 2024-10-13 00:39:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 493ce947-2bc3-3650-b828-ed4b72f7d4e7 | -7.1389 | -47.61539 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2717321f-a756-322a-86e4-3489ebfeb5f3 | -7.13717 | -47.60262 | 2024-10-13 00:39:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| a5fffe5d-b10a-3fa7-a566-9b7b9ca407d0 | -7.02087 | -46.81893 | 2024-10-13 00:39:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 96ea0da6-d9c6-36c0-ad74-fbc34a521caa | -6.98541 | -47.08581 | 2024-10-13 00:39:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9c63ab0d-6197-3fff-8735-ca08f75036c8 | -6.84461 | -44.38594 | 2024-10-13 00:39:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9008f94e-ae85-3447-b965-5caf4fa50c0c | -6.80928 | -44.46997 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cd1b1020-1842-341d-a50a-8f03185d5c91 | -6.7609 | -44.1866 | 2024-10-13 00:39:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 072b8a5f-6b3c-3a2a-a306-4bb6d31ca192 | -6.75967 | -44.17773 | 2024-10-13 00:39:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 74eff65e-026e-3f33-88ab-c4fe14faaea1 | -6.75206 | -44.18785 | 2024-10-13 00:39:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 98113849-8336-3e1d-bbaa-9257dcf79c14 | -6.74485 | -48.18186 | 2024-10-13 00:39:00 | TERRA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 9fd11db6-ca5c-3e94-9c8f-11eadfe8bdbe | -6.74322 | -44.18912 | 2024-10-13 00:39:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be343c90-e07d-383d-a2a5-07ba1b39dc2a | -6.74299 | -48.16797 | 2024-10-13 00:39:00 | TERRA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 83651cff-57ab-360b-8900-96c6a1c98980 | -6.68504 | -44.63075 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a443f956-9a16-36af-a2f2-31e641b8bd8a | -6.58446 | -44.17862 | 2024-10-13 00:39:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 89766436-7b94-3610-9273-f63c6750bad5 | -6.54467 | -44.022 | 2024-10-13 00:39:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 25145741-20d2-39bb-9823-a8a6d8b6d1cd | -6.53926 | -44.43855 | 2024-10-13 00:39:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7d25563d-9edd-3676-a4d5-ae000bbae248 | -6.53803 | -44.42963 | 2024-10-13 00:39:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 67b12670-1274-347a-8450-c2e28e054a94 | -6.52704 | -44.42801 | 2024-10-13 00:39:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 596bba03-01fd-3945-91b6-853ced9ad462 | -6.48336 | -46.06548 | 2024-10-13 00:39:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eefe84c8-83eb-39aa-a48b-00d4c9cbe876 | -6.4768 | -46.06244 | 2024-10-13 00:39:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6457ea4a-0a31-31d5-904e-0b4fb9ae6166 | -6.45176 | -44.27567 | 2024-10-13 00:39:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7fce21f5-bf15-30be-b582-18b57748147b | -6.45053 | -44.26679 | 2024-10-13 00:39:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e9d7e19c-c103-3297-8c5b-b62628e97e2a | -6.32577 | -44.97003 | 2024-10-13 00:39:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 31bd0cdd-31bd-359d-a5ab-8cf528cd765c | -6.32082 | -44.27036 | 2024-10-13 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 78c8a94a-4576-3816-8464-07359b9e89b8 | -6.1742 | -46.75428 | 2024-10-13 00:39:00 | TERRA_M-M | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| cf40c4c7-3b78-3cc3-8bd3-a92fe7816014 | -6.13762 | -44.73533 | 2024-10-13 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 53b0eb14-744b-35da-ac93-7bfd17a65737 | -6.13639 | -44.72636 | 2024-10-13 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| ded990e9-e943-33fc-9e1b-673e9d1a93ce | -6.133 | -47.27999 | 2024-10-13 00:39:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| ec6e99dc-3a44-3f37-9573-6aae32c9c1a5 | -6.13145 | -47.26834 | 2024-10-13 00:39:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| b96a4b20-0b78-3a44-956d-8523809d3b9a | -6.08839 | -44.84943 | 2024-10-13 00:39:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 660966e8-4336-3995-afd2-2f61365cd782 | -6.07641 | -44.63163 | 2024-10-13 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 21da74e1-49d3-34ec-8233-46b3b82439cc | -6.07517 | -44.62268 | 2024-10-13 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d707029b-4908-3c12-921f-5707885b2112 | -6.07074 | -44.0567 | 2024-10-13 00:39:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b9e7b308-e689-3d6d-bb83-d5857b555f57 | -6.06877 | -44.64184 | 2024-10-13 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 1355236b-9993-319d-9def-fefcbc6b0159 | -6.06753 | -44.63288 | 2024-10-13 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9bc342ff-0c53-3a68-a445-504b558ebfa6 | -5.86769 | -46.45895 | 2024-10-13 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| db1fb050-0c4b-35ae-907b-74817f7e0649 | -5.86625 | -46.44846 | 2024-10-13 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 510c430f-05d4-38be-8214-02ffb22cc946 | -5.77249 | -46.11143 | 2024-10-13 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 490076f5-42e6-3b02-b2a3-2de3dd9c200d | -5.76339 | -46.51133 | 2024-10-13 00:39:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dd02bb7c-7f97-3062-84f6-711c7340a129 | -5.74994 | -45.94443 | 2024-10-13 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 583b6c40-98f7-3b15-b596-1a39c1766a88 | -5.70431 | -45.67649 | 2024-10-13 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6d90bfe8-1d36-348b-9eb3-319032d3ae51 | -5.6299 | -44.33012 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e2112955-4f84-379b-bdab-68da30e3b400 | -5.59855 | -44.96711 | 2024-10-13 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 51946c8d-093d-38b6-9ce3-502900247121 | -5.57059 | -46.16803 | 2024-10-13 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5c6f3aab-3fd6-307f-8fda-677ac085f9d4 | -5.56859 | -44.22781 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0f94a7c3-3fed-30d1-839e-f61c6e72bf70 | -5.54395 | -46.18194 | 2024-10-13 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8ccc8361-9bec-36c4-8893-672b767a3b89 | -5.53805 | -47.10704 | 2024-10-13 00:39:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a8a7a54c-829c-3b3b-ad7c-1244818920e4 | -5.52768 | -45.80068 | 2024-10-13 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0d7a1c56-3043-3bf8-b0c1-aed8290b63f5 | -5.49725 | -46.80169 | 2024-10-13 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8a373364-6404-3c11-a7df-6df423d9dced | -5.49725 | -44.97516 | 2024-10-13 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ca2226b6-fb66-30c3-a53c-02ffcdbc260d | -5.49582 | -46.79097 | 2024-10-13 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 128d6062-6a55-37ac-afb9-39aa2d19dd91 | -5.4774 | -45.83325 | 2024-10-13 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 44522d34-7de0-3125-bf04-7de2083a9a6b | -4.09875 | -43.92598 | 2024-10-13 00:39:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 54939912-f195-3433-a74a-da5e62ae153c | -4.80404 | -42.71523 | 2024-10-13 00:39:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 7df1dd85-3e1c-38f1-953f-6f7958b82f49 | -4.80536 | -42.72461 | 2024-10-13 00:39:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 4f04a4f5-f581-329d-8f04-fef7a04183f3 | -4.81314 | -42.71393 | 2024-10-13 00:39:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 8078a87e-7c79-33f1-b2f4-6fd51dc4704c | -7.2043 | -42.28727 | 2024-10-13 00:39:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| f73a56c1-632a-3475-b2d1-7813121213e0 | -7.21337 | -42.28596 | 2024-10-13 00:39:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 0e95bbbf-9e0b-377c-91cf-ad18145a6a2f | -7.2147 | -42.29531 | 2024-10-13 00:39:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b8444943-7773-3a64-8c93-bb0e23116050 | -7.70236 | -43.20149 | 2024-10-13 00:39:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2311c05a-97cf-3713-9b07-1e07f4445b9c | -5.46821 | -45.83448 | 2024-10-13 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 784b3236-a4e8-347f-a1bf-44714894dd4b | -5.38716 | -45.04289 | 2024-10-13 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cb3bb2ef-ed64-3bcf-b177-1cb537491a2f | -5.37257 | -44.40271 | 2024-10-13 00:39:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 55efeb3f-3fe1-3a63-bce2-caec5a7a3725 | -5.35613 | -44.41405 | 2024-10-13 00:39:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ca81e9b4-c101-3669-bb9d-841eae27c8e1 | -5.32251 | -45.30784 | 2024-10-13 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d4e3adca-dfaa-3c80-99ac-ef5585ff1294 | -5.30705 | -44.4003 | 2024-10-13 00:39:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8b6d70bb-6dc1-31dc-b740-d014dbf96502 | -5.30582 | -44.39147 | 2024-10-13 00:39:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5a4d5079-652e-3324-b44d-0a293b5bf25a | -5.19951 | -44.9531 | 2024-10-13 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6acb1ce2-ccf4-39b1-b599-f8051aca46be | -5.19827 | -44.94414 | 2024-10-13 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 78a55a81-6aee-360f-8b6f-ff9315613523 | -5.19075 | -45.48844 | 2024-10-13 00:39:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c61a4740-10c0-3b92-8e38-a31f093eb77f | -5.18937 | -44.9454 | 2024-10-13 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 03c054bf-c095-37d7-ba8a-a251ededa533 | -5.18692 | -46.19476 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4633a8bb-2fcc-339b-a827-1cf842fdb51c | -5.17085 | -46.14679 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 91b8a54a-e025-32a5-bb4f-4409a2037a2e | -5.16599 | -44.37214 | 2024-10-13 00:39:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b5b06d06-f192-35c6-aaf3-e1f86b67946d | -5.16477 | -44.36331 | 2024-10-13 00:39:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5631ee8f-770a-362e-bc22-1a3329049d6c | -5.1629 | -46.15787 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 4b717ff2-6606-312e-9df6-738c1c43e721 | -5.16157 | -46.14813 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 35cd1021-00d4-359d-9afd-88d93d19e6b4 | -5.14323 | -45.41061 | 2024-10-13 00:39:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0a22ee32-5e7b-339c-8fac-949197f5ce4d | -4.09114 | -43.9361 | 2024-10-13 00:39:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a5db1109-bfe8-3c15-8d2c-8f64b8e7445b | -4.0975 | -43.91712 | 2024-10-13 00:39:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 08751ce5-0003-38db-abda-dcb6f6d8b161 | -5.14197 | -45.40145 | 2024-10-13 00:39:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ac4fde54-d2e8-312b-a223-65537411a1a6 | -5.14071 | -45.39224 | 2024-10-13 00:39:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| de180669-f131-3e09-ab51-1f3e6e176a0f | -5.13423 | -45.41192 | 2024-10-13 00:39:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fd82fcbc-d3a4-3119-9f6b-cb616c5f0e58 | -5.13297 | -45.4027 | 2024-10-13 00:39:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 5c3fdc4a-4756-30f8-a45f-663418520284 | -5.1317 | -45.39349 | 2024-10-13 00:39:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 85e0f5ed-7223-3a69-82fd-e9159b77f3ad | -5.12163 | -47.3555 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 08f6a974-74ad-346e-b532-25d604366637 | -5.09308 | -45.85268 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 480ba0a7-33b9-3987-89ff-9e71c4badc60 | -5.09178 | -45.84314 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 953f6ede-cc1c-3fa9-bc3f-0d2a5ff31bcb | -5.08264 | -45.84447 | 2024-10-13 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7678609-1530-316b-a6aa-1b04312fa8ca | -4.0899 | -43.92725 | 2024-10-13 00:39:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 3ed29ccc-cd8d-3818-ae94-9516013fb65b | -5.07434 | -46.85801 | 2024-10-13 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 9c075099-93ef-3a5c-a701-f89b2691ca90 | -5.07288 | -46.84726 | 2024-10-13 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| c3490b58-e359-361c-85a0-a595de3e8f68 | -7.70995 | -43.1913 | 2024-10-13 00:39:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d2158d24-8d55-3583-b121-0dfba68788ac | -5.06325 | -46.84867 | 2024-10-13 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f62ae77a-4ba6-3f8d-a8f3-08fd2293bb88 | -5.04944 | -44.86153 | 2024-10-13 00:39:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 40cc27e5-8288-34ff-8b94-bbbd600d74ff | -5.04821 | -44.8526 | 2024-10-13 00:39:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 48a295b0-5aa1-33ff-b433-c0f66b6f101e | -4.99501 | -45.47173 | 2024-10-13 00:39:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 20175c1e-4804-3915-a9ec-30bd8450ac33 | -4.97618 | -46.81239 | 2024-10-13 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3bf42626-2d6e-35e4-92da-caf73cc71062 | -4.97473 | -46.80173 | 2024-10-13 00:39:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 32.5 |


[Clique aqui para ver as próximas entradas](README10.md)
