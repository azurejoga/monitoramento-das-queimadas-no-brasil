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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da517780-305a-3506-979b-7861fe0b7398 | -9.2082 | -59.6354 | 2025-08-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 0866323d-f393-369f-9213-f64cd4951158 | -18.7569 | -45.1107 | 2025-08-17 01:10:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 68865767-2930-3f77-924b-226da9ab78fc | -9.4992 | -60.547 | 2025-08-17 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0fc54c9f-8561-36b7-a902-391790791411 | -9.5179 | -60.5461 | 2025-08-17 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 6301b9ec-b5c6-3714-a899-8d3486d1e31b | -6.5453 | -43.0138 | 2025-08-17 01:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a99ff3d4-450e-37d1-b987-c6f3ba7e4909 | -8.9788 | -60.4964 | 2025-08-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| e137f361-a3a1-31ed-a967-4dd49707e1f5 | -18.7575 | -45.0866 | 2025-08-17 01:10:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 227.4 |
| 248009c6-c092-3728-9686-204725cc7f41 | -18.7778 | -45.0818 | 2025-08-17 01:10:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 147.9 |
| d913d7fa-5bea-3195-8fb6-bd915f599feb | -10.8444 | -45.3126 | 2025-08-17 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| e9f0be68-3e24-38e2-9360-77759fdee5b6 | -9.4994 | -60.5278 | 2025-08-17 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c5a6a6eb-b532-3c62-b1c5-7f9bd62a166e | -9.1894 | -59.6558 | 2025-08-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f54a2cae-4d49-3fb9-af64-d1dd8b3b3a47 | 0.96981 | -60.40731 | 2025-08-17 01:11:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d2e408fe-2032-3b94-bb38-c75c6898db0d | 0.9685 | -60.41676 | 2025-08-17 01:11:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| dddf86d4-8408-3c7c-9284-1a6dffb1bb12 | -13.4419 | -45.8974 | 2025-08-17 01:18:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87b01358-8c48-3b4c-9e2d-b02003272e3e | -14.99 | -54.7416 | 2025-08-17 01:18:00 | METOP-C | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d296291-fff6-33b9-9678-58176edd9b91 | -9.2232 | -59.651901 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 662c2c03-eca4-3db8-ad3c-1eab969ea789 | -9.5166 | -60.518398 | 2025-08-17 01:18:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7be552e9-4fc8-3f26-be85-2f4e774951cc | -14.9453 | -54.682899 | 2025-08-17 01:18:00 | METOP-C | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| def851c8-68ef-3d4b-b34f-c0acaea3b85b | -6.145 | -57.925999 | 2025-08-17 01:18:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a363e60-f67c-32aa-ab81-5b5d381769be | -15.0592 | -56.0411 | 2025-08-17 01:18:00 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e2069b5d-e4bd-34e8-aeab-e0710646c28a | -10.5428 | -50.381901 | 2025-08-17 01:18:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad973786-3563-3211-85be-3da575467bd9 | -9.2083 | -59.631302 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e348b9f-efe0-319f-a158-25f3b870fef4 | -9.1921 | -59.650799 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1afde27e-c514-3464-8b71-ce373886399e | -9.1624 | -59.609699 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee225497-e1df-3379-bb29-826c355a6910 | -11.3624 | -55.399101 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69e65bb9-6e4c-3956-a66a-a2664973747d | -8.9794 | -61.679501 | 2025-08-17 01:18:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e1d4489-64a0-3885-b87e-7f0fadf111c2 | -13.1378 | -57.1231 | 2025-08-17 01:18:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a37b1e9-c9d7-3ff3-af7b-229cb1f62ee1 | -10.5462 | -50.395401 | 2025-08-17 01:18:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c13c2edc-3611-3ebb-b78a-88480dca6d51 | -9.5122 | -60.545502 | 2025-08-17 01:18:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 026ed645-2ce9-35d7-8b7c-5d7835763fca | -16.846901 | -48.9058 | 2025-08-17 01:18:00 | METOP-C | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 614bd6f6-525f-3404-8d6d-5cec31c5e7f0 | -9.2215 | -59.644299 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 939cc4e9-aa6d-3baf-b615-994e0658d6dc | -11.3705 | -55.3895 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 968040b5-8233-3611-9054-23d4699d48f7 | -10.1209 | -57.772999 | 2025-08-17 01:18:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2eabd228-aea8-3442-81b2-cfecf90067e1 | -14.939 | -54.699902 | 2025-08-17 01:18:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 39b4296a-3c6e-3c3b-9f28-5f0907c9ef8d | -9.1985 | -59.633499 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf67501d-1445-3f68-9d10-a0614833e99e | -9.1924 | -59.698601 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a542c78a-545d-3d9b-8328-bb50d6e8dab1 | -9.2066 | -59.623798 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb8f8a63-a318-3131-bd28-0f91f30a3423 | -13.1346 | -57.109001 | 2025-08-17 01:18:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1658114-6ffa-3a6a-afa4-621b87e5d6e0 | -14.6431 | -54.894199 | 2025-08-17 01:18:00 | METOP-C | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37f4a213-3005-3c4e-a5ae-ff9ab08e1883 | -9.189 | -59.683399 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85c98039-563a-32b1-9470-ae990801a0ee | -9.5184 | -60.526699 | 2025-08-17 01:18:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8894f10-d69b-3801-85e2-93b672a59224 | -6.1351 | -57.9282 | 2025-08-17 01:18:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86770d8e-f17c-3f15-b398-54578f51214e | -14.0455 | -58.872299 | 2025-08-17 01:18:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a62b90eb-c24e-314e-81f2-c74991d2f39f | -9.5061 | -60.5644 | 2025-08-17 01:18:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 371cb0ba-6b3f-3756-840f-299562c576cc | -11.3739 | -55.403999 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6d74151-efb6-3ad9-94bb-f71e1693e13c | -14.9339 | -54.677898 | 2025-08-17 01:18:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be60fec3-58ac-3b7d-b267-1cfbb2c4f75e | -11.3675 | -55.420799 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1e8ea8-bcf1-34cf-b6aa-008cf47e5c36 | -10.1178 | -57.759102 | 2025-08-17 01:18:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c58ab6a-4ebd-315e-b4de-f5cffd19a0da | -9.1808 | -59.6931 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e885afc-03ad-3eb5-b5f5-0ebe0de82938 | -15.1851 | -48.780102 | 2025-08-17 01:18:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3eb8188a-9620-349b-99ee-4fe561f8ab5b | -8.9696 | -61.681599 | 2025-08-17 01:18:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8309dbc1-59cf-3c1b-b9f2-a7ab216c832d | -9.1756 | -59.6227 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04d1568b-aa1e-394f-a28f-b71c81b09e2d | -9.522 | -60.5434 | 2025-08-17 01:18:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 494bd73d-3bce-3cc7-b2ff-9c309ce694c6 | -11.3722 | -55.396801 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c81267f6-fa87-348d-a336-df1ea73df5ca | -8.9774 | -61.670101 | 2025-08-17 01:18:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a691afb-1906-3ae2-889a-769ae3d82b5b | -6.1481 | -57.939701 | 2025-08-17 01:18:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc71c5d9-c4d3-3892-9660-9a533b07ec64 | -9.1907 | -59.691002 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d203c94b-9d08-332a-be90-753bdb25f191 | -14.9483 | -47.061401 | 2025-08-17 01:18:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cc0bd494-8a4c-36df-a75c-a9aca9c3a065 | -13.0063 | -56.858101 | 2025-08-17 01:18:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3bba1cf-f046-3237-80e0-050617423f1b | -8.9896 | -60.503502 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 251355a2-7a45-38c0-9875-b252b4fd9ecd | -10.8481 | -45.311401 | 2025-08-17 01:18:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80f2a508-2fb7-3063-a267-0f57cb6d1004 | -8.9951 | -60.528198 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f54ad94-5f6f-3914-8d91-508f363a1352 | -13.1693 | -55.7131 | 2025-08-17 01:18:00 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7bfb46ec-17c3-3cec-83e5-6b0c55edbc83 | -9.5159 | -60.562199 | 2025-08-17 01:18:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5843a6f-af26-3cb6-959c-eaf900e8c73c | -14.9356 | -54.6852 | 2025-08-17 01:18:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d73722c-b6bc-3a68-8162-59da11cd9e28 | -13.1393 | -57.1301 | 2025-08-17 01:18:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 137305d4-73be-3a92-8e2d-914e26f182cc | -11.3641 | -55.4063 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3eb87f3-2411-3337-902c-45541fb60514 | -14.6043 | -47.948898 | 2025-08-17 01:18:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a59d577b-8348-3a17-a7ee-ead263105ebf | -14.9802 | -54.743999 | 2025-08-17 01:18:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e65e96c-d888-34fd-bd3e-96f4e5a9da09 | -13.4515 | -45.8946 | 2025-08-17 01:18:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 493c041a-9ce4-3cf6-be54-6f6fe1ec1ad0 | -10.3266 | -54.1562 | 2025-08-17 01:18:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f28942ac-ccb3-37d3-8903-87a7a7b719d9 | -10.3143 | -52.554798 | 2025-08-17 01:18:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f285f581-7dca-363a-93eb-e6e60a181fe7 | -9.1739 | -59.615101 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f60b52e-3817-304c-8510-b227bcbead3d | -9.1968 | -59.6259 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be4b008a-cda1-3437-b15c-36abca1d6ebf | -9.1657 | -59.624802 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61cd7af6-65cb-3e76-9741-8b7ab804532e | -11.3607 | -55.3918 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71dd80ce-5920-3400-9a58-046100904186 | -15.1947 | -48.777401 | 2025-08-17 01:18:00 | METOP-C | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e0caa668-4577-380f-a7e1-594b00dd0eee | -18.782 | -45.1022 | 2025-08-17 01:18:00 | METOP-C | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf27a251-c045-3c80-9a8e-b2df567d77b2 | -14.9639 | -54.763302 | 2025-08-17 01:18:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b946e4d-ba25-3404-95a9-e8ecf92aba25 | -14.9622 | -54.756001 | 2025-08-17 01:18:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 09225156-ce4e-31c0-bf83-7d71aa23ec1e | -9.2313 | -59.642101 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38580733-d45f-3c08-8144-32fd908aa77a | -14.9737 | -54.760899 | 2025-08-17 01:18:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc42cc44-acbd-3abc-b2d4-d8b4b65eceff | -10.1193 | -57.766102 | 2025-08-17 01:18:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 300498e2-ea85-359e-8c23-21511c35ca13 | -8.9861 | -60.487202 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae6dea7e-90b4-3573-8fde-4eaa40e923ec | -9.1904 | -59.6432 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee0c573e-682b-3922-b9ce-d30bbbf184eb | -10.3286 | -54.164398 | 2025-08-17 01:18:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd6e400-d2ad-3faa-ac2c-9f60ff10e2ff | -8.9798 | -60.5056 | 2025-08-17 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc4ef833-7276-391c-b5b3-bb6f7bfe3bcc | -11.379 | -55.4258 | 2025-08-17 01:18:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38e83223-03a7-3cc8-b01e-416adbbcb81f | -6.1382 | -57.941898 | 2025-08-17 01:18:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c656aca-6723-39fd-8c31-121daefa8a0c | -18.7757 | -45.080101 | 2025-08-17 01:18:00 | METOP-C | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b188c6a6-806b-3c3c-92d7-974905656b44 | -8.9933 | -61.696301 | 2025-08-17 01:18:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7fbdf7-78c7-3e54-90f4-bfc59628a206 | -18.766199 | -45.083099 | 2025-08-17 01:18:00 | METOP-C | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a5fd8335-900c-34d1-8678-bebc57b23701 | -14.9322 | -54.670601 | 2025-08-17 01:18:00 | METOP-C | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6aa5b252-338a-3d59-bb86-db61c19f9dbe | -18.759899 | -45.061001 | 2025-08-17 01:18:00 | METOP-C | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af8f7962-5ae4-3295-8499-110bd58055d9 | -8.9676 | -61.672199 | 2025-08-17 01:18:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3034e56e-5620-35e7-b9a7-1709916079bc | -10.8466 | -45.343399 | 2025-08-17 01:18:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52a14a27-276d-3bb6-8037-705177748d4f | -13.0078 | -56.865101 | 2025-08-17 01:18:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee8c5b2-00be-34ea-859c-4bb8384c54a3 | -10.8386 | -45.314098 | 2025-08-17 01:18:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a4743dc2-9150-3f9e-9bb7-3eea76629aea | -14.9606 | -54.748699 | 2025-08-17 01:18:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9c71236f-b4d7-3224-a30a-dc5e3d4c0e55 | 0.9595 | -60.411098 | 2025-08-17 01:18:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
