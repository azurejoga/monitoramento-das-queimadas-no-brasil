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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e4ad9bd-d654-3e77-801a-32b2485804e8 | -5.78031 | -50.19037 | 2026-08-24 00:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8e2ee5f0-fea3-3701-bcfe-544a01989cee | -9.1988 | -49.11528 | 2026-08-24 00:09:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7b962da5-7ddb-365e-9e71-bb18e21eb81d | -6.62896 | -58.48426 | 2026-08-24 00:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.5 |
| bd2e4767-f76f-3579-bea7-610df66b9f74 | -5.91945 | -52.13772 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 68c5d6a7-b2e3-3fd8-9ff6-0242c99b23ab | -11.11265 | -49.88774 | 2026-08-24 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 50a11b14-8cb9-3818-96c0-441fd358b199 | -9.68102 | -55.1064 | 2026-08-24 00:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4c95abd2-1793-3c99-ba4b-192670fac3aa | -2.55799 | -47.24615 | 2026-08-24 00:09:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0a24e84d-9b36-34e6-8780-c4e4674bd9fb | -10.70054 | -47.74533 | 2026-08-24 00:09:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4587bc26-fc00-3ede-bddd-47359f7d1be8 | -7.26379 | -49.91147 | 2026-08-24 00:09:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4c05e766-2a2c-3120-b0d7-4f0e4baf2d1f | -5.86614 | -50.14475 | 2026-08-24 00:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e0786fae-9706-3fe5-a00e-5470d4ef9bc3 | -6.34187 | -54.77222 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 03f3e13f-3b23-38e8-916d-586e87fd7e49 | -5.6476 | -51.77258 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| eb034df2-21d3-3171-abca-56624af38bf3 | -9.03586 | -50.72448 | 2026-08-24 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4fe1fa83-2006-3bde-a250-355428595ca4 | -5.62414 | -48.4205 | 2026-08-24 00:09:00 | TERRA_M-M | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e8739826-9dd3-322d-a17a-d106a8c50089 | -3.27179 | -49.52671 | 2026-08-24 00:09:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| af546f53-3d8e-34a9-bc51-40a531c50e7c | -1.50304 | -53.87712 | 2026-08-24 00:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6873490a-c5f4-3335-8080-51958e37a7bc | -1.86714 | -47.98385 | 2026-08-24 00:09:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dca4a96e-d4ee-31c3-b0a6-0f71fbce5732 | -6.81406 | -58.66067 | 2026-08-24 00:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.9 |
| a220c8a0-1a9d-36f9-9d71-7e9c79a1ad8e | -6.34827 | -54.76506 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 0e3d434c-676b-3b05-a984-ddf96d648aac | -8.58401 | -49.99135 | 2026-08-24 00:09:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 89f0cb81-a48b-3e60-9961-3131db7ea3e9 | -5.8785 | -52.1123 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f0a45d4f-8070-3a47-907f-907f981c350d | -6.34666 | -54.75254 | 2026-08-24 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8cc1c2ef-946c-3ab1-8f5a-2b2dcb546bf9 | -6.63862 | -58.48951 | 2026-08-24 00:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| fecb584d-354a-3d8e-aab5-3200e21cf708 | -9.67909 | -55.09137 | 2026-08-24 00:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 2a677e4c-dc91-3f57-800e-ac7503904990 | -6.55689 | -58.5252 | 2026-08-24 00:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 520941f4-f3d8-37ec-a4f0-48f43c319b52 | -5.87726 | -52.10324 | 2026-08-24 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c7d0708c-2077-3736-8e10-a599f12baef2 | -8.34061 | -47.70786 | 2026-08-24 00:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f8de7aa4-ee8a-31d1-9d98-810dd7b9b7ae | -11.10343 | -50.01636 | 2026-08-24 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 1da7f784-277f-3574-8592-034577680653 | -9.03465 | -50.71561 | 2026-08-24 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 866ffc1c-e8c7-3b49-b376-3aa446cd59ef | -8.9875 | -65.4006 | 2026-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 999343aa-fe20-3d35-a9d4-6246a00d9f6a | -17.6815 | -46.4143 | 2026-08-24 00:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 4cbc2825-fe2a-3ff9-963d-12e7ef328298 | -5.78 | -57.5605 | 2026-08-24 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6cc58823-36a3-3d19-80df-8653fa10f740 | -7.3788 | -45.8344 | 2026-08-24 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| bf1a1700-98c0-390b-bedf-1fffce4512b3 | -6.3505 | -54.7665 | 2026-08-24 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7a011783-2cce-30cd-8477-a063972f4edd | -8.5707 | -49.9729 | 2026-08-24 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| b8c6465c-b714-3b5f-befe-e9788dbdc62b | -7.3791 | -45.8119 | 2026-08-24 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 226.9 |
| a30448cd-926d-3f51-be28-13db1965eec5 | -7.3605 | -45.791 | 2026-08-24 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 212.9 |
| 0e1dcc7d-353e-3256-9fa8-79a12b97a29c | -9.006 | -65.4 | 2026-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 1ced4136-714a-3c3b-ab02-29809364f33a | -6.8491 | -52.505 | 2026-08-24 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 4f260bc2-2235-34c4-93fe-f4ba66da784a | -16.3952 | -51.8159 | 2026-08-24 00:10:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9332c5da-07f7-3766-bfed-e995e8d4d023 | -17.6621 | -46.3951 | 2026-08-24 00:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 1416773f-0e47-3c10-b83d-ffbf8cc84ff7 | -8.5895 | -49.9713 | 2026-08-24 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 47cd6818-935b-3226-b3e8-469673a15aba | -16.3947 | -51.8375 | 2026-08-24 00:10:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1bdfb009-44be-3a05-9fcd-bb99186b33e2 | -6.6048 | -58.3838 | 2026-08-24 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| df1fcaf8-dea1-3a48-934f-93fc4f0b9311 | -17.6821 | -46.3908 | 2026-08-24 00:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 083be4cf-510d-33d9-bcae-a69e9c98f438 | -6.5227 | -35.1118 | 2026-08-24 00:10:00 | GOES-19 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| f201949b-5111-3a72-9951-ece922be2c3f | -7.3793 | -45.7894 | 2026-08-24 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 5e0384aa-8340-3b46-b6ca-a8b3d3a06046 | -9.0061 | -65.3813 | 2026-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| b3093e72-a75b-392b-b645-63d7776841d4 | -17.6615 | -46.4185 | 2026-08-24 00:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 186.5 |
| b8c60e92-2e92-3ebd-8522-75da26725fe5 | -16.4148 | -51.8129 | 2026-08-24 00:10:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 1583372e-a5a1-368b-84f8-6f2a77eaae31 | -7.7707 | -61.087 | 2026-08-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 71d3051c-772f-35fd-b83a-18bc515f20c3 | -10.8364 | -50.9479 | 2026-08-24 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 293f214b-77e5-3805-8484-25608377cc4d | -6.6233 | -58.383 | 2026-08-24 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 17bd15b6-b3a7-31f1-9293-0d3ed9d399d6 | -10.8174 | -50.9498 | 2026-08-24 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| fdd9c572-4447-3582-94dd-dcc45be27727 | -8.9876 | -65.3819 | 2026-08-24 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 378918d1-a558-3966-af9d-a5156674db1f | -8.5892 | -49.9926 | 2026-08-24 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 1c8ab1fa-34a5-3eb9-8a56-0c2d0a45aa1a | -7.3603 | -45.8136 | 2026-08-24 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 263.1 |
| 5f843af0-28da-3eb7-ad14-fb90aee168a7 | -7.7706 | -61.1061 | 2026-08-24 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1046a11e-bad4-3945-a58c-bfec2cb4da13 | -17.68 | -46.42 | 2026-08-24 00:15:00 | MSG-03 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 675ba433-c795-38b3-930a-654c30f3ab95 | -7.37 | -45.8 | 2026-08-24 00:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c5636dc-23f0-3716-a06b-d349a1843a75 | -17.67 | -46.37 | 2026-08-24 00:15:00 | MSG-03 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7f9869ac-40f0-38bd-98c6-bee9cd37ec46 | -7.37 | -45.85 | 2026-08-24 00:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86386514-b5d8-3c80-accc-26b6a4f46cf5 | -12.0941 | -50.5951 | 2026-08-24 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 188316be-88f3-3c60-a30f-211d4e3e1089 | -17.6821 | -46.3908 | 2026-08-24 00:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 552afacc-4569-3e8e-982d-3f64fa313b20 | -6.8008 | -59.5934 | 2026-08-24 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c6b5f493-16e4-3c05-adfc-a13a747c67bf | -3.5406 | -48.1889 | 2026-08-24 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| a7da09a6-8aa9-31af-be0b-bdfcfcbd2bc9 | -8.7784 | -62.8514 | 2026-08-24 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 71aba208-4aea-33bc-8f4d-59a3a40178fd | -8.5892 | -49.9926 | 2026-08-24 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b8c10f6f-d66c-3c38-bfda-8084739d52cf | -7.3605 | -45.791 | 2026-08-24 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 43c27e05-ba9f-36f8-a596-1492b79b7957 | -7.3791 | -45.8119 | 2026-08-24 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 16b93d30-5a05-3a83-89a5-72783b557dcf | -8.7785 | -62.8324 | 2026-08-24 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c67deb20-c911-3de0-84d6-669369ae6393 | -12.075 | -50.5974 | 2026-08-24 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 24d476f6-f15e-3690-a35b-89bd128698f6 | -5.78 | -57.5605 | 2026-08-24 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 5c92fa73-73c2-3eed-9720-21c764587b95 | -23.0142 | -49.3779 | 2026-08-24 00:20:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| b2f9de93-c561-3574-a070-1855e91d589d | -12.0938 | -50.6166 | 2026-08-24 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 7bcba289-2e6c-35d9-9c5e-36c10777701a | -7.3793 | -45.7894 | 2026-08-24 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 43f450cf-48ea-3680-8cd8-064ec2f81b7c | -6.3505 | -54.7665 | 2026-08-24 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 38eb5db6-a7e4-3980-99e9-0dfa4340bf2a | -7.36 | -45.8361 | 2026-08-24 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d8f21e6b-b11d-3352-9590-3b559898c47c | -16.3952 | -51.8159 | 2026-08-24 00:20:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 27ef5cc3-276c-3aa8-af9f-9e4da408de1e | -6.6233 | -58.383 | 2026-08-24 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a523114b-5c69-3d0f-8845-a233fb847eb7 | -9.2398 | -60.3871 | 2026-08-24 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 73831e89-ffc5-3577-bca6-1fe379b069d7 | -16.4148 | -51.8129 | 2026-08-24 00:20:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| df82708c-ea28-3c10-ac87-7c4e6510ed38 | -17.6621 | -46.3951 | 2026-08-24 00:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 283.8 |
| 2229135b-5f99-3ef8-8311-1b381c7f6442 | -17.6815 | -46.4143 | 2026-08-24 00:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 353.5 |
| a82734e8-18f4-3a9e-b9a7-bba5031635d9 | -17.6615 | -46.4185 | 2026-08-24 00:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 518.6 |
| a276dba9-8269-33ad-8346-8a9b00b6baf3 | -7.3788 | -45.8344 | 2026-08-24 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c19a2366-1885-348f-81ce-901538040706 | -12.0944 | -50.5737 | 2026-08-24 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 12c2cfe1-3c50-356e-a912-56f73efae1b4 | -7.3603 | -45.8136 | 2026-08-24 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 281.6 |
| 0ad9fbee-6f19-3675-a0a4-f1c9a230cd62 | -9.0061 | -65.3813 | 2026-08-24 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| e1f4fabf-5d05-38bf-992e-d86f06a0d33e | -6.5487 | -58.522 | 2026-08-24 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 5f4a6157-c2b1-3fac-bdf7-6d70cb3df33d | -12.0753 | -50.5759 | 2026-08-24 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 45c71997-0e4d-3cf4-9a59-a7b496acac23 | -16.4144 | -51.8345 | 2026-08-24 00:20:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| c77c6818-e1a7-3e44-a75b-e59288878baa | -16.3947 | -51.8375 | 2026-08-24 00:20:00 | GOES-19 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| d4c36968-8b4c-38e4-b761-8ce135f8b384 | -6.6048 | -58.3838 | 2026-08-24 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 4c61d6df-a7e0-3deb-aa36-f1a268abfa29 | -8.6673 | -62.8369 | 2026-08-24 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ed3be5ad-fc81-3203-8301-215a52fbbd0d | -9.006 | -65.4 | 2026-08-24 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| aa2bc0a4-63e5-3196-a683-b3fc79ef7d7b | -7.3793 | -45.7894 | 2026-08-24 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| de32735e-0f75-395c-be9b-e6fb01a20d2a | -8.5892 | -49.9926 | 2026-08-24 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 118fac16-031a-353d-b2e6-7fac5211efb4 | -7.36 | -45.8361 | 2026-08-24 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 78ea0680-fba1-34a4-b05b-a28f1ad02df0 | -12.0941 | -50.5951 | 2026-08-24 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 182.9 |


[Clique aqui para ver as próximas entradas](README5.md)
