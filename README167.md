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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21159578-956f-3498-8f1c-d05197714062 | -10.3721 | -50.3363 | 2025-10-05 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 195.8 |
| d6227eb1-125a-3593-925c-e74a0cf78dc1 | -3.9135 | -41.5447 | 2025-10-05 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 140.5 |
| fd33829b-b23d-3c99-ba35-883874be1acf | -9.2439 | -51.8133 | 2025-10-05 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| c2f2bc4f-ea9c-3f2c-84dc-a0d1ded64eb9 | -10.195 | -45.4882 | 2025-10-05 14:30:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| e467f4e9-c166-33fa-aad1-01854ad0304d | -8.1891 | -44.1357 | 2025-10-05 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 177.9 |
| bec9756a-8b0e-326f-ba6d-47a6b0b95b5a | -15.6019 | -52.4888 | 2025-10-05 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 0afaa493-b76b-3400-9127-b6dd19d46b14 | -6.7048 | -42.1712 | 2025-10-05 14:30:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| ad9df0c8-5512-3d74-8581-256d89dcfb75 | -6.9873 | -47.4665 | 2025-10-05 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b00a8880-9a7f-37fa-92a1-9ba97b2071f7 | -17.8617 | -57.6024 | 2025-10-05 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.3 |
| 6f058021-bd31-370f-8d60-e30decf267ac | -15.2211 | -56.8006 | 2025-10-05 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 813ffc3f-bbe3-310e-91a0-2ba638c797bf | -11.8225 | -45.0827 | 2025-10-05 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 299.7 |
| ec8eff7d-6e67-3cff-90b0-61106c9f880d | -7.0367 | -42.8036 | 2025-10-05 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 139.5 |
| 49846416-47da-38c0-b188-81629107d706 | -8.6138 | -54.976 | 2025-10-05 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 1504aa35-bcf5-3298-a5e8-ef65490502d2 | -17.9404 | -57.6134 | 2025-10-05 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 5668088a-7153-3c01-9362-80e45283210f | -5.8764 | -44.2764 | 2025-10-05 14:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b841a661-2524-390a-bf66-355da798ba4e | -5.7917 | -43.2872 | 2025-10-05 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| f5a27abb-4880-3dd3-859a-3a773cbad483 | -6.2064 | -45.0278 | 2025-10-05 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 5763c603-5017-3162-af34-b20134c537e6 | -10.4051 | -45.416 | 2025-10-05 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 756.7 |
| f09e4698-4a67-37b9-a40b-2e838f11697a | -12.4105 | -51.0917 | 2025-10-05 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 1dd493ee-eaeb-39ff-814a-8886573b10dc | -11.6558 | -46.9941 | 2025-10-05 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a46c6e2c-23ee-3c12-a82c-36d63da8c883 | -18.1773 | -53.3454 | 2025-10-05 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 56.7 |
| c1b32f3d-88d8-3f08-9b04-5fd9fd17e89f | -6.6976 | -42.8354 | 2025-10-05 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 9bb74b49-6b5f-3caa-a1ae-7cf9f5748113 | -6.7051 | -42.1473 | 2025-10-05 14:30:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 4ef4521f-6410-3b5a-9c19-830c50933cb9 | -10.2212 | -50.3303 | 2025-10-05 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 80598f76-2531-3cfe-9e99-5883da00cada | -1.3558 | -49.2732 | 2025-10-05 14:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| db649919-5b83-3b13-9808-13cd8090ca8f | -5.9584 | -43.5072 | 2025-10-05 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 2e7eea8e-e034-3b3c-84bd-bfef8db9df3f | -11.8635 | -44.938 | 2025-10-05 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 705d5582-e5a9-3762-a222-83a69ca3d760 | -1.2085 | -49.0838 | 2025-10-05 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a1b685c0-54f7-3727-bf4c-0d1eda22a18f | -11.1165 | -49.8707 | 2025-10-05 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 75fdbd7a-f334-31c3-b964-fcc69ec402f0 | -18.1972 | -53.3423 | 2025-10-05 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 3d75c070-8a99-3b13-8137-18fbc576b506 | -5.9226 | -43.3236 | 2025-10-05 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 3c67ebd1-ab18-3d21-8c3f-6e99389c2b38 | -8.5407 | -47.6831 | 2025-10-05 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f4663093-fb1c-37b2-9130-6651fc5c9356 | -7.7938 | -42.5607 | 2025-10-05 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 137.3 |
| e1348db9-fdd3-3021-97b2-9a8fe5b0b8d4 | -5.9269 | -42.8783 | 2025-10-05 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| ff3ca875-5f0e-330c-8fc6-011ef9308600 | -7.7308 | -46.2513 | 2025-10-05 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| dbf0095b-e99e-3d3d-b09b-a92ea35f7d5b | -7.6993 | -42.5708 | 2025-10-05 14:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 865a585b-7f95-3a96-b33b-813587a282d6 | -6.7052 | -43.8859 | 2025-10-05 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b1b5a614-41d4-3c48-ac8f-4c2ad4010715 | -9.2973 | -46.0026 | 2025-10-05 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| df67a2ac-8754-3e62-8f65-6d2fac18b40f | -6.3889 | -43.6115 | 2025-10-05 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f1fa440c-c18f-3ea4-8b73-a85ed506ef77 | -16.077 | -51.0859 | 2025-10-05 14:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 7f27d45b-ba0f-3373-843d-2c0c36a1070f | -6.4076 | -43.6099 | 2025-10-05 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 0e6babf8-2d89-39cc-a72f-fcf4180b89a0 | -5.7882 | -45.7809 | 2025-10-05 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| fd46f0e8-36df-342a-802c-82eb17b3c3a3 | -10.1501 | -45.9482 | 2025-10-05 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 5c398983-ae1e-3c1b-a497-cd59f2cab395 | -6.4161 | -44.6466 | 2025-10-05 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 895cb2dc-927c-311e-96f9-d0a73956568d | -17.9605 | -57.5904 | 2025-10-05 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.6 |
| 869afe4b-c084-3c08-b987-8580cec75eec | -12.3911 | -51.1153 | 2025-10-05 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| e19059bc-e6c7-31ce-a68e-8ce6d636a4d8 | -12.5297 | -54.7326 | 2025-10-05 14:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| a3b43cd7-fe4c-3dd7-85ef-f6911965ff3c | -5.5671 | -43.2576 | 2025-10-05 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 79931682-262e-3273-af4e-ba17dab8b779 | -8.5405 | -47.7051 | 2025-10-05 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 391e7667-f989-30db-8a3d-b4f5c235e2ed | -12.3154 | -55.1416 | 2025-10-05 14:30:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 4036c581-33d3-36f7-a258-a08792b1efc4 | -7.712 | -46.2531 | 2025-10-05 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 276.4 |
| 6c28e872-d8d3-3500-bfc8-9217b719ea11 | -12.5487 | -54.7307 | 2025-10-05 14:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 1e89eefa-3fcb-3345-ba28-fe6146d9dd2f | -13.7304 | -47.9494 | 2025-10-05 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| ab972b46-0ea1-3861-8b5b-0f4d7a0bbd1e | -3.9134 | -41.5687 | 2025-10-05 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 129.5 |
| 9f77cffb-9bab-3fe0-ae41-0cf533aa0aec | -18.1968 | -53.3638 | 2025-10-05 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 239.2 |
| e3df2e0b-0357-37dc-b6d3-825938b8468e | -12.5294 | -54.7531 | 2025-10-05 14:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| bfe24ee6-ce83-372c-993e-39f47f3ad43b | -12.5485 | -54.7512 | 2025-10-05 14:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 65575608-53e0-372d-a71c-e8f9cb1ad2e6 | -8.8712 | -46.8324 | 2025-10-05 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 9c5fbb0e-e150-3b17-8ea9-2975ec298ac7 | -7.0369 | -42.78 | 2025-10-05 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 184.6 |
| 8557f9b6-e882-3023-b7bd-b77f11b7e0aa | -6.154 | -44.6217 | 2025-10-05 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 0fcb8016-f8ef-3880-bf38-326070552115 | -5.7762 | -42.9372 | 2025-10-05 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 128.5 |
| 47dba5ca-8f6a-3e0f-b335-b3d519001326 | -18.1963 | -53.3853 | 2025-10-05 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 1b047e5b-51f2-3fd2-898f-f5cfe6096143 | -11.8038 | -45.0624 | 2025-10-05 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 237.9 |
| 338fedf3-4864-3b54-8f44-b235e364ede1 | -13.7476 | -51.2883 | 2025-10-05 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 200.7 |
| f5bbb128-a4e2-37d5-a4c4-342adb6ed9c8 | -8.1699 | -44.1608 | 2025-10-05 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 8093085d-65a9-3e9c-ac9e-466897118209 | -6.6416 | -42.7934 | 2025-10-05 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 4691a87e-851c-30b2-b11f-0129a9e777e3 | -6.3982 | -42.6972 | 2025-10-05 14:30:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 32864845-1b17-360b-9bd9-f9761add9cdf | -9.1114 | -44.4029 | 2025-10-05 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b71aff7d-6dc4-31f1-bb96-8d9c80c9779c | -5.8891 | -42.9048 | 2025-10-05 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 07bba248-9c9f-3ec2-9f8f-be8da3b0dc41 | -12.3157 | -55.1212 | 2025-10-05 14:30:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 24324006-c9f4-3194-a442-33180d3c153e | -8.1702 | -44.1377 | 2025-10-05 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| f190266c-e5d4-3220-bdff-451ca65422d3 | -8.8803 | -47.6061 | 2025-10-05 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 0da6a1ec-c167-3294-8baa-90c533b959d9 | -16.0212 | -50.9425 | 2025-10-05 14:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 21b42c75-7966-3b07-a477-486899a210c6 | -13.6909 | -51.2315 | 2025-10-05 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 4149b25f-2d43-3721-844c-28be45988b3b | -5.5348 | -42.6736 | 2025-10-05 14:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 1ebfab13-ab9f-3b62-858b-a8797cb86702 | -6.2251 | -45.0264 | 2025-10-05 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1fc4030e-1cbf-374b-ae8a-3d846022b4d2 | -13.7284 | -51.2908 | 2025-10-05 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 209.5 |
| 4ddd8a6e-1cf6-3bde-abca-1d57896acb64 | -8.6139 | -54.9558 | 2025-10-05 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f631991e-bf9a-30f5-922c-2058ae244830 | -6.7167 | -42.8101 | 2025-10-05 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 1300d7af-be4a-3699-9416-a9785277ee1b | -8.8991 | -47.6042 | 2025-10-05 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 9909739e-3029-301f-860f-e19810f4efe9 | -6.1353 | -44.6232 | 2025-10-05 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 35491315-1ba8-32e9-99a6-7855ea3ef402 | -11.1573 | -47.1712 | 2025-10-05 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 436eb5fe-103e-3788-9b7b-be127cb45775 | -11.5301 | -47.6798 | 2025-10-05 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 485f27cd-b2e6-30aa-8434-3c03483a1dd1 | -11.1192 | -47.176 | 2025-10-05 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 78e92491-8651-3887-bd54-a72bf201be53 | -21.6888 | -50.0559 | 2025-10-05 14:30:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.4 |
| bb0af2b4-ad00-38e4-8221-6e61d3608ac3 | -8.4683 | -45.9106 | 2025-10-05 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| cfc96467-0034-39c5-8fee-c73aaf83817c | -6.2181 | -45.7722 | 2025-10-05 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 2545379e-e139-32ad-abae-176200cbe8c7 | -17.8808 | -57.6412 | 2025-10-05 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 600def10-d4e1-3e64-b3dd-541366c99b13 | -7.6622 | -47.367 | 2025-10-05 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ba666f84-ce6a-3a6f-b5ef-8d6d34246204 | -12.2876 | -49.2101 | 2025-10-05 14:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| beaa0e41-affd-3a93-a8ef-d9ff1c229dc4 | -14.3353 | -47.6755 | 2025-10-05 14:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d0aaa03a-ba5e-3fc1-8126-34f4d59c8371 | -16.0016 | -50.9456 | 2025-10-05 14:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 5d2693d5-3249-3fb3-8e48-2c012d87fd38 | -8.6324 | -54.9747 | 2025-10-05 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| ef0625d1-7e4c-36d1-ae33-1b02277b0c88 | -17.9006 | -57.6388 | 2025-10-05 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 7cbb71ef-95e7-3b9f-b816-882fad61d4b1 | -11.8033 | -45.0856 | 2025-10-05 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 201.8 |
| 1abaa755-10cd-35c7-af5a-c9f2eb7e473d | -5.4775 | -42.7956 | 2025-10-05 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 176.3 |
| 6a0fe24b-3a05-31f9-9e9c-1f722b6b22b3 | -3.8946 | -41.5698 | 2025-10-05 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 10a2711d-fa7e-30e9-b344-d7137197607c | -12.6286 | -50.5734 | 2025-10-05 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ad99cba9-1f28-39db-a53c-a9a5f205878f | -6.2596 | -45.341 | 2025-10-05 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7163e3c4-2299-35b4-b5d3-e6280be46feb | -11.1168 | -49.8492 | 2025-10-05 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |


[Clique aqui para ver as próximas entradas](README168.md)
