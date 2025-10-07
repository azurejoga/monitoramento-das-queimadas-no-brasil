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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98f357b5-6fed-39e0-9e6f-c7386677140f | -14.7384 | -46.037 | 2025-10-07 11:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 5a0bef83-240d-3195-ba5e-6f2e3e035e1b | -14.7585 | -46.0104 | 2025-10-07 11:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 3ac2d2ea-bc2a-375e-b7b5-fe4641caa293 | -14.9224 | -51.4292 | 2025-10-07 11:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 034370cc-3d1d-3f3f-a490-0a62facb2fb4 | -14.7389 | -46.0138 | 2025-10-07 11:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 0c1fdfb9-3fe9-39f5-a308-c28555b55f00 | -14.2953 | -45.8382 | 2025-10-07 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| fdc95cb9-499a-3166-9ae3-d16f79ea96e2 | -14.777 | -46.0532 | 2025-10-07 11:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| d0630e28-da33-348e-a19f-f993133e2ec7 | -14.2953 | -45.8382 | 2025-10-07 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 0c579a98-cb90-31a5-adea-3dce70c1b651 | -14.9228 | -51.4076 | 2025-10-07 11:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 0892f658-729d-3576-a429-f5b885e21ace | -11.8447 | -44.9176 | 2025-10-07 11:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| a1e51fc2-23ce-3598-91df-1b7b99fae357 | -14.758 | -46.0335 | 2025-10-07 11:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 196.5 |
| 2c1656cd-7c24-3e1b-b6ac-038902be3a94 | -14.777 | -46.0532 | 2025-10-07 11:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 07994e89-7907-36ed-b97b-ce6f977c0110 | -14.7384 | -46.037 | 2025-10-07 11:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 6e341221-8e00-3b9b-b1eb-24fd40d877ca | -14.9224 | -51.4292 | 2025-10-07 11:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 831ac288-520b-399c-9d6e-0711ab956279 | -10.4245 | -45.3907 | 2025-10-07 11:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 95846388-1c98-30d4-93ad-13118551c196 | -14.7389 | -46.0138 | 2025-10-07 11:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 146.7 |
| af0b07f1-22b6-3522-92fa-324ada2beb59 | -14.2949 | -45.8613 | 2025-10-07 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 55b037d8-ac55-308d-8ab2-9c688e00debc | -14.7585 | -46.0104 | 2025-10-07 11:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 5ffeda02-d945-302d-9c82-7a4337f9474c | -18.0187 | -44.9725 | 2025-10-07 11:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 547fe11b-9ec5-3927-96bc-594e8fb092e7 | -14.7585 | -46.0104 | 2025-10-07 11:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 1dbef919-8fec-37f5-b6d1-9ea4f7d27b81 | -10.4054 | -45.3931 | 2025-10-07 11:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 0f286f28-42eb-31e6-9c56-84d2afb270cc | -10.4058 | -45.3702 | 2025-10-07 11:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 0fd12853-d465-31e3-9b6d-a3ec600b2311 | -14.7384 | -46.037 | 2025-10-07 11:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 246018bf-8c86-338c-a6a0-b50fb5cd3a0a | -14.758 | -46.0335 | 2025-10-07 11:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 143c56a1-7316-3b14-918f-8d12f2e6d325 | -20.1139 | -44.4085 | 2025-10-07 11:40:00 | GOES-19 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| 5136eece-4090-3ba6-9655-ae596be6485f | -11.8447 | -44.9176 | 2025-10-07 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| ea7848d3-d79b-351e-87c8-7ab9216d582c | -18.0187 | -44.9725 | 2025-10-07 11:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 18aa8a49-d61e-3687-9832-7d25b7b129b9 | -10.4108 | -50.2683 | 2025-10-07 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 81eb4895-082e-3a0a-adf6-5dcbd183641e | -14.7389 | -46.0138 | 2025-10-07 11:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 46bfa63d-e818-3c34-bdad-4516835f1dfa | -12.6159 | -44.7519 | 2025-10-07 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| c16dec13-110f-3ad7-941b-9bbd36c016c3 | -14.903 | -51.4319 | 2025-10-07 11:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 9a31462e-8470-3a29-9251-032bc47f48d1 | -14.9228 | -51.4076 | 2025-10-07 11:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 97aab74a-828d-3938-9b16-4b90ade00e66 | -13.3241 | -48.0324 | 2025-10-07 11:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| af8e998a-028d-3502-b0a7-c5a8a32a0817 | -12.8913 | -54.7372 | 2025-10-07 11:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 0c244ec5-5910-3807-8b96-fb5f6e5b5294 | -10.456 | -48.3607 | 2025-10-07 11:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 323359cc-8285-3794-8bdb-468dcd575037 | -10.4245 | -45.3907 | 2025-10-07 11:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 336.0 |
| 88171297-efb2-33db-8ec6-a523e178d9c3 | -10.1943 | -45.5339 | 2025-10-07 11:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| a103f1e6-a3ca-350a-a7e2-a38a6f931e62 | -14.2949 | -45.8613 | 2025-10-07 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 9c5e9a8b-733e-3be7-be9d-30d631394961 | -14.9224 | -51.4292 | 2025-10-07 11:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 30f871f4-1b5e-3b20-a3b6-8fea2e468be8 | -14.2953 | -45.8382 | 2025-10-07 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| ceea71f5-8ea4-317b-ba8b-62a0403f9825 | -11.8447 | -44.9176 | 2025-10-07 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 12c7704f-8ef4-3f8b-a70e-747944ff7b6e | -12.6159 | -44.7519 | 2025-10-07 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| a282ad8f-0e58-3bed-a9ff-9ce3ec2a8828 | -14.9224 | -51.4292 | 2025-10-07 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 734ed625-c6d6-38b0-8441-d9bdeb6df167 | -10.4245 | -45.3907 | 2025-10-07 11:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 431.8 |
| b608c8ab-d5a0-35e9-88fb-03db0e9aa28e | -13.0231 | -51.0171 | 2025-10-07 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 9b83fb4b-54de-3e75-a45c-4a2df8a19a33 | -12.9426 | -46.8109 | 2025-10-07 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| c4494102-6a98-311d-9004-553dedec04e7 | -10.4108 | -50.2683 | 2025-10-07 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7e462826-2727-372d-9c9b-bc47ce8882cc | -10.4058 | -45.3702 | 2025-10-07 11:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 435baf91-7b2d-3d98-b52b-3a1e6273bbdf | -14.903 | -51.4319 | 2025-10-07 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 517eb936-aa40-38db-b81e-74ede9f5c14e | -12.8913 | -54.7372 | 2025-10-07 11:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| d4fcb357-5546-32cd-80c5-35748495a078 | -12.891 | -54.7577 | 2025-10-07 11:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 40da1c2f-599d-38bc-a60f-76c3316b6571 | -12.3796 | -47.1633 | 2025-10-07 11:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 4baabc74-9cdb-314b-9113-b3ad02275f0a | -14.9228 | -51.4076 | 2025-10-07 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 8bd7c358-09df-32f0-b8a1-668a0bdc160c | -11.6859 | -46.3366 | 2025-10-07 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| f07a4e16-556d-3e79-b1dd-845cb9de5aef | -13.3241 | -48.0324 | 2025-10-07 11:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 66164ed3-3df4-3fa2-9544-f5a12a4fd961 | -11.6855 | -46.3593 | 2025-10-07 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 37f97ca3-214a-3eed-b803-47409ca8b03d | -14.2953 | -45.8382 | 2025-10-07 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| e36b85ad-ee29-3e97-9c3a-444589c032ed | -10.4054 | -45.3931 | 2025-10-07 11:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 5f54f4dd-4a8a-3f5a-9bc7-854999eab6a7 | -11.8447 | -44.9176 | 2025-10-07 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 4031c938-c021-3fb8-9789-4ecac20d8c96 | -11.6859 | -46.3366 | 2025-10-07 12:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 47bec806-939d-37d8-8f51-9d413bdf0ade | -13.2232 | -51.6744 | 2025-10-07 12:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f53bd0bf-2aaf-32ed-8e89-4952b4868b60 | -14.2949 | -45.8613 | 2025-10-07 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 73fdbc63-c0f7-3826-ad1f-257bfb598f64 | -10.4058 | -45.3702 | 2025-10-07 12:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 3277abb3-a4db-3154-8092-7f2283c0ab1b | -10.4108 | -50.2683 | 2025-10-07 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| e783f994-d321-3932-bd0b-cf1ec0127300 | -15.3742 | -47.2973 | 2025-10-07 12:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4d4a02dd-cff6-31f2-835d-f2f52b967af7 | -10.4245 | -45.3907 | 2025-10-07 12:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 784b3f92-7cda-3bb3-919b-c153eaf7af29 | -12.9426 | -46.8109 | 2025-10-07 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 9212290a-ce25-31e0-8c16-5983ab69fc3c | -12.8913 | -54.7372 | 2025-10-07 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 2378087b-da95-3e6d-8a3c-e9f399abe037 | -10.4054 | -45.3931 | 2025-10-07 12:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| f204b28c-183c-36df-b1a5-d5c397e438b0 | -12.9619 | -46.808 | 2025-10-07 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 301647dc-5ad1-389a-afb5-0c4f3e5499f5 | -14.8645 | -51.4158 | 2025-10-07 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| b51eb602-c3df-35b1-9662-46c7f38db48a | -11.0262 | -50.9067 | 2025-10-07 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| f7b8377f-ca09-3d44-98f1-242b07685504 | -14.2953 | -45.8382 | 2025-10-07 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| fe99a843-ee3c-3a51-83d6-152912d7dd0d | -18.0187 | -44.9725 | 2025-10-07 12:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 131.0 |
| d9f5da6d-41e7-345e-a7c0-2e12532cee5d | -11.1185 | -47.2207 | 2025-10-07 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 57debb57-97bc-31d8-8cf4-f42a0751ce05 | -14.9224 | -51.4292 | 2025-10-07 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| b489fa55-f90e-3241-b90f-c7503cac4436 | -13.3044 | -48.0575 | 2025-10-07 12:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| aee5f4e2-a076-3987-9b73-7dc1656e5517 | -11.6855 | -46.3593 | 2025-10-07 12:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 3c235677-8e68-313e-b97c-fe302f3e1ca3 | -10.7278 | -46.6658 | 2025-10-07 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 3f5614ec-15aa-3f03-8e8b-d35877167540 | -11.8221 | -45.1059 | 2025-10-07 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 1afec0a2-7926-36a8-b41d-33324a58c4fd | -14.9228 | -51.4076 | 2025-10-07 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5bbc14f1-16f8-34dd-932e-169fb03ac6ed | -14.8839 | -51.4131 | 2025-10-07 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2f6bc242-367a-3f27-a2cb-2d87bda2ea67 | -12.9615 | -46.8306 | 2025-10-07 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 90085f63-b53b-385e-8c23-4a7f311ccd1a | -13.3241 | -48.0324 | 2025-10-07 12:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 91e64b59-e452-3737-a663-95ba8d16655b | -12.891 | -54.7577 | 2025-10-07 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| cba9098b-642b-3d35-9715-bc3b7f8ddd4c | -12.4044 | -50.2571 | 2025-10-07 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c9a4c1be-9f5a-37c7-b7c4-c3305105195f | -10.456 | -48.3607 | 2025-10-07 12:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 49d02f6a-4297-3e56-8ff3-c1603fa9f842 | -12.9426 | -46.8109 | 2025-10-07 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| c15c9a19-f42a-3608-9d62-55cd9d06cbdd | -10.2506 | -44.3538 | 2025-10-07 12:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a448b684-6766-3bcc-bd5c-d243c6264849 | -8.5584 | -46.2387 | 2025-10-07 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 043f60b4-e5b8-3b1d-b6da-4bd669cf7a83 | -10.4058 | -45.3702 | 2025-10-07 12:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| bee9642f-4e15-3f1e-aa48-96d6f38b7b8e | -14.2953 | -45.8382 | 2025-10-07 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 227.0 |
| 84ab15b2-df5b-3ec0-b312-6be82941d757 | -8.5395 | -46.2406 | 2025-10-07 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| d8569603-39ea-3640-9e7a-890de66d602c | -14.8839 | -51.4131 | 2025-10-07 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 825a197f-6e95-3e5b-9619-1536a7503f9d | -14.8645 | -51.4158 | 2025-10-07 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 0a619dbb-1232-361c-9514-ecb70df958cd | -8.4824 | -46.2912 | 2025-10-07 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1625f83a-0448-37ec-a5fa-c7fa6ebf1404 | -11.8221 | -45.1059 | 2025-10-07 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| e4875376-50f7-3ec4-8d02-e61cace12a62 | -12.9103 | -54.7352 | 2025-10-07 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 86a54a11-6071-32cc-b570-f9b952b1e002 | -14.758 | -46.0335 | 2025-10-07 12:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 14852d6f-9900-37f0-8747-baff2e96523d | -10.4245 | -45.3907 | 2025-10-07 12:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 4b8645d5-5136-366f-93a4-3ff075b6e50f | -8.6519 | -46.2964 | 2025-10-07 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |


[Clique aqui para ver as próximas entradas](README112.md)
