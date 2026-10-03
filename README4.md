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
| 37d3bdeb-9b46-308f-b6b9-6b60b2a9eeaf | -2.9678 | -53.2649 | 2026-10-03 00:30:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 768bde66-2c18-393c-9827-4ec006536572 | -11.7229 | -43.412899 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0e78999-7d41-3acb-8f4b-3c4ce63b6ec5 | 1.7881 | -55.605499 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 315f795c-7372-3640-819f-b8eb5ef4cef1 | -2.5444 | -57.998299 | 2026-10-03 00:30:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cef9e5a6-0a4d-341c-95a0-1bea2dedc4d0 | 3.797 | -60.963402 | 2026-10-03 00:30:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 542c69bd-6b9e-3cac-bc09-be66157db4ed | -6.8554 | -59.233799 | 2026-10-03 00:30:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e41a3342-7239-3050-9a4b-5a7d565e622d | -1.2622 | -54.556499 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 183ac0cc-18c8-3339-8656-52fa583cf22e | -1.0765 | -54.101398 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcea9c30-e852-3c90-a7f6-932aef94c3f8 | -3.2157 | -54.306702 | 2026-10-03 00:30:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd9b923f-e280-33eb-954a-793b4e876630 | -3.697 | -50.972301 | 2026-10-03 00:30:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c553030-8cd1-3820-b2bc-700f5c4c98eb | -11.6935 | -43.496799 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d20e28a0-3d08-358f-99ab-1acd3d9698e6 | -14.3031 | -43.7962 | 2026-10-03 00:30:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d06e41c-5e76-3ebc-a178-4d294e2dadcb | -2.9218 | -54.1026 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8eb113e-a2b3-303e-b172-6d045999dc94 | -2.9776 | -53.262699 | 2026-10-03 00:30:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80a6d008-676d-38ed-9e2a-4c3d81ffecc2 | -11.4222 | -43.367199 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43612f97-b1a9-391a-bb7b-44b89b1f4719 | -5.8491 | -53.465 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1be9eba-9e12-30d1-8de1-33c298545361 | -10.8755 | -57.094101 | 2026-10-03 00:30:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b1689c6-beba-36d2-8d32-92d2444ced16 | 1.9189 | -55.802898 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e39d369-f6de-39b5-81d1-707809c66338 | -2.8843 | -45.395199 | 2026-10-03 00:30:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf17ac43-f508-35c6-98d9-e095a2c5cc60 | -2.9169 | -54.081001 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba11e85c-a43a-3afb-a32b-faef7f375dcb | -4.0508 | -51.0765 | 2026-10-03 00:30:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b172d1ae-2290-324e-9c30-c198e522d26b | 1.9318 | -55.791199 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a352b74a-a864-33fc-9924-0aff7e20d9c8 | -3.2239 | -54.297401 | 2026-10-03 00:30:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd770890-6ff5-387d-a11a-11cdb402e457 | -2.7595 | -58.084999 | 2026-10-03 00:30:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c90fa98d-02d0-397f-8846-099352dd0407 | -13.8934 | -55.132099 | 2026-10-03 00:30:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73c6a307-5d5a-3550-a5be-7e3c7e9581c5 | -2.8804 | -45.421799 | 2026-10-03 00:30:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca5e0d97-406c-380b-8767-9b28b61e3372 | 1.796 | -55.5704 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4ce45e7-e088-3ce0-b911-22e883f16c67 | -15.3009 | -42.772598 | 2026-10-03 00:30:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4dc7b3b0-1e17-323b-93d7-812a3d5b7663 | -6.0633 | -53.4543 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5a4d665-e05e-3009-aef1-4f92990a6ec2 | -10.9974 | -59.1343 | 2026-10-03 00:30:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10d98860-6447-30e1-857d-98b88a5b0d04 | -3.849 | -55.965401 | 2026-10-03 00:30:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e81f880-cdf2-395a-a63f-ace832acef89 | -3.4139 | -52.827 | 2026-10-03 00:30:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30d5e6cd-857a-35e8-b1a4-e70d0bb3ad2f | -4.7804 | -55.708302 | 2026-10-03 00:30:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f50f0a86-daee-3030-9ad1-73ad9b03cc0f | -5.9255 | -43.609699 | 2026-10-03 00:30:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53ed6863-34be-3551-9649-6fb75d08d73a | -11.6839 | -43.499401 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 588aa4fd-99f9-3f04-bdff-82a8a6170d58 | -5.9231 | -43.6408 | 2026-10-03 00:30:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39d514a9-e9b9-369a-b3de-c16841ba0862 | -6.8596 | -59.252998 | 2026-10-03 00:30:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd90abe5-3670-3e61-b1c0-29a14ccc920b | 1.7929 | -55.584499 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1077614b-fc6e-3199-a36d-ec2f94b024eb | -11.629 | -43.564602 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44d0c1fa-cc12-3f5e-8c1c-24eeb1534193 | -6.2147 | -53.2598 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bffe6e05-ea1a-337b-b17f-6b40ea747dff | 3.799 | -60.954601 | 2026-10-03 00:30:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| db59cf12-7fd5-334c-b5f8-31da5008bd8e | -11.6906 | -43.447201 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eff44bb0-3c21-3dbd-8598-7eb6ad87d417 | -11.4286 | -43.3913 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef373fde-782a-3925-bab0-32ff7605a16d | -3.4041 | -52.8293 | 2026-10-03 00:30:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e089a1f9-735e-3d32-8ed8-dc12a6ba729b | -3.2409 | -54.508301 | 2026-10-03 00:30:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd0b38b4-914d-3ac8-a75a-eca6b618394f | -4.7129 | -56.141602 | 2026-10-03 00:30:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ca50e22-da80-33be-9045-a02ec2ffe2bd | -2.8826 | -54.111401 | 2026-10-03 00:30:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff1c55ea-4f9c-31d7-9f94-6f9b1a94ed3b | 1.9303 | -55.7981 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba2b7d4b-4fff-3b87-ba0a-4116f3975d38 | -3.8475 | -55.958599 | 2026-10-03 00:30:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32650115-971f-3d44-8d7e-43e3d06c3b09 | -3.2809 | -53.823799 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d66a890-955d-341d-bec6-2034e5572dde | -3.1186 | -53.744801 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9eae217-96f1-368f-8516-64be28b53a1e | -2.9496 | -54.088799 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce76cd0-d540-33e5-885f-16a4b9faf1b0 | 1.7945 | -55.5774 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc9d8c9-3f76-3b2f-b987-ef7acbfe0bda | 1.8043 | -55.579601 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad9e5788-bb5d-33c6-b9ac-c76df3deff77 | -6.0061 | -53.520199 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b26b017-dfd5-346e-b192-4221fb5f843b | -3.5853 | -54.526798 | 2026-10-03 00:30:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d123e21-1879-36e4-99a7-9b1aab61f724 | -3.0145 | -53.876099 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3af2c013-2706-3d8e-be9b-70636c6bf92c | -2.1486 | -59.216499 | 2026-10-03 00:30:00 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd89f09e-7f30-3948-92b1-13b255acf3fb | -3.6401 | -55.496399 | 2026-10-03 00:30:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9c25409-e506-3d51-a68d-ad5ff62bbd39 | -2.1502 | -53.656898 | 2026-10-03 00:30:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddebd827-7f99-3497-ab21-3d1530020278 | -6.1282 | -47.334499 | 2026-10-03 00:30:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f39a91e0-8a00-32bb-8f7d-50fbf26835c3 | -2.9202 | -54.095402 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee17c12b-9cd1-3bb5-97fc-ab978910bd70 | 1.9043 | -55.821499 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ddaee0f-cae0-31a4-946d-9790865900a6 | -13.5295 | -44.077499 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8f5d3cd-3628-3bf0-98cd-b6ec109f4114 | -3.2255 | -54.304501 | 2026-10-03 00:30:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e73b40c7-0fdb-3a00-83e8-a925e0a242c1 | -3.4023 | -52.821301 | 2026-10-03 00:30:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 207db8ef-b6d0-3d80-b254-bbbb840a53e2 | 3.6332 | -60.7346 | 2026-10-03 00:30:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 15544f9c-d478-3911-a71c-4adb07fbe142 | -2.961 | -54.0938 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02364722-46ac-3d37-a27e-2386fedd776b | 1.9138 | -55.7798 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4777aca8-1f94-3fc0-99ac-9287ddf26c12 | -12.8593 | -44.675301 | 2026-10-03 00:30:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9b169a2-03ab-3024-9214-c68e3a994ab0 | 1.7976 | -55.5634 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72a33a15-8526-364a-aecc-a83efd284924 | -2.9185 | -54.0882 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9adcff3-3f0f-3764-90f2-b3add9021158 | -2.8858 | -54.125801 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a275ef7c-7540-3067-93b3-ae19e8d9c031 | 1.809 | -55.558601 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c0e6cb7-ec3e-39d4-bc27-668e31c45c6a | -3.1768 | -54.090698 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58ef63b2-f417-33ea-8ed5-a4d207ba4cbb | -11.6324 | -43.5387 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa8a91bf-da75-3d6d-a623-5f50975148c3 | -1.2792 | -55.4048 | 2026-10-03 00:30:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3984ca2d-cd6c-3059-a7a0-cdc57143cba5 | -3.0162 | -53.8834 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3685769-373c-31ba-abd0-fab966290906 | -2.8688 | -45.3731 | 2026-10-03 00:30:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 948b662d-605c-3037-b52c-7ff0030d2b26 | -3.2793 | -53.816502 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 151c2da2-b244-37c8-bfe3-0ce058ea072c | -1.4451 | -54.635502 | 2026-10-03 00:30:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6801c719-e1c4-37db-a2bf-3fadd015748a | -11.7065 | -43.468102 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b6b27ad-3bd0-3024-977f-c4ae6d648320 | -6.1244 | -47.318699 | 2026-10-03 00:30:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f09ba35-6537-36b7-8d0c-98526603c0a3 | 1.9075 | -55.807598 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d2f98e2-29c9-30e7-9e11-96154fe6a195 | -6.51 | -55.380798 | 2026-10-03 00:30:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca8798d-ca54-38ac-9d02-96685802739a | -5.2589 | -55.9119 | 2026-10-03 00:30:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e8f1da0-6631-3260-ae81-3981ec259a5f | -3.1284 | -53.742599 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ebe3c9a-8b8c-3404-b449-f12fd42fffc2 | -9.6975 | -57.436001 | 2026-10-03 00:30:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6895116a-4921-3493-ad31-cf9db152a80f | -12.8545 | -44.656601 | 2026-10-03 00:30:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f75a875-e05d-3c9d-90a1-382d02bfb50d | -5.3715 | -56.046501 | 2026-10-03 00:30:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9301fcc7-2f93-31a1-a1b1-1d629cf43cc3 | -2.8924 | -54.1092 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 318e988c-cfc7-3ff1-a9af-5bcff15d5131 | -5.6022 | -44.358898 | 2026-10-03 00:30:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e35840d-816b-3a75-9d90-0b0556ea62a0 | -6.9207 | -49.6064 | 2026-10-03 00:30:00 | METOP-B | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35443cc1-5136-3b1a-8f1d-e2960c46f1b1 | -6.0078 | -53.527401 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0afb5cff-6aaf-3054-82c5-5b5e64d34d29 | -4.7887 | -55.699299 | 2026-10-03 00:30:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdaacba8-ff13-3f4b-9b68-648783d07444 | -4.4261 | -55.736801 | 2026-10-03 00:30:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b4d4489-3827-3a8a-b68d-ba92febf525f | -3.1169 | -53.7374 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae2cef51-de9e-3d98-8de4-af63dcc774ed | -2.8907 | -54.102001 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aad11c9c-0711-3207-8aa7-d4fe863d8da6 | -6.9259 | -49.628101 | 2026-10-03 00:30:00 | METOP-B | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fd6ce6c-5e52-3a7b-9a40-327e53fdf558 | -2.8956 | -54.078201 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
