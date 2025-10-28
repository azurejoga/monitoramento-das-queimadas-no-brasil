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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 884a5d22-bc63-31fe-ad45-19e94aa80456 | -2.8037 | -49.14662 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 750ebe4a-c228-3cd7-ac39-f17973c3e948 | -3.11282 | -51.29093 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74ba445c-ec5c-397a-8b98-a8d379325d83 | -5.04166 | -45.13352 | 2025-10-28 04:42:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccbd617b-f8fe-3e4c-adce-2ea0d3e71f78 | -3.59896 | -48.99568 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02b368b1-1223-3219-9fdf-8fd7b1712e21 | -8.15016 | -47.00548 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb5ccf5a-5bcc-3ea6-9d16-de3e3ea5154e | -3.12831 | -50.15287 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20fa7607-0867-37fb-a73f-4d60af05dd34 | -7.13264 | -47.06558 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fd0c00a-78f4-3203-b0b0-7c09cd075303 | -5.79024 | -35.60731 | 2025-10-28 04:42:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b5bab829-6ca8-3825-95f2-c27f242bb74c | -5.10779 | -48.48316 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1ede65f-06fc-3779-90e8-7adf3be59ce2 | -7.97597 | -46.28348 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a178c1f0-a5db-302a-a55d-f6dd4ef43dcb | -7.94754 | -45.49514 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91f73226-a89d-36f1-a351-b4bcd8c57006 | -3.4455 | -50.22092 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c7820b0-9031-356f-96b7-14c7f9cee8ea | -5.63018 | -47.61686 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9b20619-9740-382e-9231-8ceb9fc26cc2 | -7.45197 | -49.40798 | 2025-10-28 04:42:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c1c65432-7c76-3c88-af66-0d264e48c363 | -6.18492 | -44.86588 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8461ae46-f03c-303c-aea5-f0865d1522f5 | -7.97215 | -46.75322 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a8dc4e79-8a4e-3d76-8ee7-8323d4a1cbf3 | -7.29609 | -45.07132 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1d506a76-c56c-3116-a8cf-dfd860f0c4b4 | -4.87067 | -48.5282 | 2025-10-28 04:42:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 189d55b9-9f01-30d0-a9df-3d2907bc0ec3 | -3.58152 | -43.63123 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 035a80d2-f19d-3528-9be6-4b880442d0cf | -7.9447 | -45.51439 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7eb9587-bc8a-3524-8cf8-5bd654a45111 | -6.91891 | -43.48773 | 2025-10-28 04:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15a5440d-63ba-359e-9ab2-6856d502fa8d | -7.97904 | -46.70734 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4128c2b9-6a73-3f68-8c88-ab026f4405c0 | -2.64463 | -48.50623 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ea9cd0e-dc75-38c9-afb6-c445fa992a9c | -3.44392 | -41.84549 | 2025-10-28 04:42:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e42bde06-59f0-34c6-8036-4e4b7cfef3eb | -5.70471 | -43.53158 | 2025-10-28 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9ffea3b-df92-3b37-b4a2-a5f06ed0b7c6 | -3.53465 | -53.31553 | 2025-10-28 04:42:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1a8f932-5293-3817-b547-e402ef03bee7 | -5.6381 | -46.43103 | 2025-10-28 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d77664e7-a4e3-3846-b28f-efaad3e31cb2 | -7.46117 | -47.15644 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 457f912a-6213-34f1-83fe-8de82483dcf4 | -7.89097 | -45.69274 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c61bd1b2-8931-3782-9569-e4640aa2f129 | -5.01834 | -41.03959 | 2025-10-28 04:42:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e2c8b6ab-21bb-3f74-b483-ca3b0e7c16ff | -6.58402 | -42.69488 | 2025-10-28 04:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ff02fc4e-6c02-3a91-8c0a-3f9743bffe8e | -4.32773 | -48.08918 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83a7df71-5da7-35c6-9646-24a79ec1f7f4 | -7.95101 | -45.52522 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c75a37f6-d767-3b0c-98ac-74fb60ba0bec | -6.5588 | -41.59397 | 2025-10-28 04:42:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01780875-913d-3698-be1b-0fa94cbf824a | -5.62798 | -46.30394 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| de1e6d8a-f00e-32d3-ae38-659eec0c37c1 | -5.04484 | -49.6103 | 2025-10-28 04:42:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d26918be-e3c6-3121-8a8e-d95d79f8ae08 | -5.48231 | -43.08881 | 2025-10-28 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45730e97-6296-3a02-992a-05a9960bb78e | -5.6117 | -47.09846 | 2025-10-28 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfea23d4-576f-36c7-89b7-9b008e54fa37 | -3.79621 | -43.32299 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9db8c18d-7389-3ddb-a460-2ff45a30ae54 | -3.9386 | -51.33668 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b9db109-d1f3-39f0-9dc6-a1b4fff67ef2 | -7.27075 | -44.9699 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47962b04-3902-3a34-8545-428b597f819f | -7.86419 | -46.40078 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32dac0f2-adeb-3110-82f0-388d35c47c2d | -7.2609 | -45.00922 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f000a50d-09be-36ed-97f3-56b53b38537b | -2.95208 | -49.34464 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60f51be8-c6af-3b98-852d-1660b4cfb0cb | -7.94818 | -45.54438 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 947ab003-3db9-313e-9acd-1bbc535a6f47 | -6.98015 | -47.33831 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1055c63d-dad5-307c-95e5-8c6ae69971cf | -3.28404 | -52.60941 | 2025-10-28 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2cfdeb3-e6a1-35fd-a63d-78fceffb0b91 | -3.88154 | -47.99825 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb094ede-9f35-3a0b-ad58-59ab05d34479 | -7.36436 | -47.79319 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a47a531f-6d4c-39ad-a3a1-1ff993d5d9b3 | -6.87195 | -43.58783 | 2025-10-28 04:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fef99951-b72e-36ae-bb85-1b710bddc9cc | -7.03141 | -47.61785 | 2025-10-28 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 262b3129-6f17-39cb-aecd-d0b4b34ccd87 | -7.47295 | -47.1502 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da509639-0688-3645-ab45-a6d3ab70bae3 | -7.94613 | -45.50473 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99487537-91c5-353d-8733-ea3da706afb6 | -6.74102 | -48.17221 | 2025-10-28 04:42:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7809f29-2fe2-340c-a0a3-cc6a102a69bd | -1.80566 | -55.68801 | 2025-10-28 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba27d95b-3cac-3c57-82e6-7794a89044c7 | -6.82671 | -41.20717 | 2025-10-28 04:42:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| afea1509-2a15-33e0-a918-14ae4c855104 | -6.68454 | -42.04572 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dcb8a082-2c82-35ad-8279-67dd4226a3fb | -4.17635 | -47.65215 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed9e715c-4bca-33f0-8d58-886002bf0921 | -3.11087 | -51.21139 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8433ae29-4058-3995-a84d-5558d8f36c52 | -7.06833 | -47.36779 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad9b698b-874a-3d17-af3d-1c7c64a7f24a | -4.20447 | -48.35671 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aef594f9-30db-374f-8371-382c2fd1f3ec | -7.95316 | -45.51073 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d92d3fc-7b42-3d5e-ae4d-936ca049a5b0 | -7.8648 | -46.39657 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feec38ba-6781-3e9c-b533-cee7dec7f96b | -6.97726 | -47.33386 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8db7407-6dad-3b76-9a1c-0204c684d95e | -5.30725 | -47.87572 | 2025-10-28 04:42:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a994c012-a737-3913-aefb-4e2548c0d02b | -8.15078 | -47.00134 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54407b4b-7572-3c72-8c38-7564f259617b | -7.96239 | -47.24478 | 2025-10-28 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 913ad271-870a-35e8-8a27-d4d1f4230166 | -4.6343 | -48.69799 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42bf5462-b4b6-3a3d-93fc-9fa9a765848c | -6.1483 | -46.69712 | 2025-10-28 04:42:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f42c3466-7565-3d19-93d4-c0c03b011f9a | -7.02939 | -47.6184 | 2025-10-28 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e2050ed-68bf-39c0-baf9-3ce79c830584 | -7.81464 | -46.43942 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b787cbdd-ffa8-31d7-bcb2-6ccad91d298b | -7.31281 | -47.20731 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ed06dc9-23e6-381c-bd24-1c13033a57b5 | -4.17803 | -48.19888 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76a6b418-993d-399d-b5fc-ccef05b3eaef | -7.97716 | -46.71986 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7255f6a-343e-3ea1-b0b9-c80d8f5f3586 | -8.17943 | -45.71376 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c86541a4-a563-3f78-8188-664b8462c018 | -2.76087 | -45.39804 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8e10757-aa3d-3369-a0dd-ad7524600ea8 | -5.65167 | -51.10294 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 285bf8cf-5118-33de-9d06-a01371156d95 | -7.95916 | -45.49691 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7583cb44-99d3-3dcf-9f73-c63cc24eef20 | -8.02714 | -45.17364 | 2025-10-28 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e79d341-2099-32d2-a151-f8bb8b098503 | -7.84248 | -46.40414 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fc90ac3-591d-3330-96ae-2285e39c28ac | -3.77268 | -48.92746 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 459c5505-b966-3dc7-ad17-5134dc45acf9 | -4.88024 | -47.54808 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c2c76be-7315-39cf-b9dc-a863bb9822ac | -5.20067 | -46.15196 | 2025-10-28 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2f68484-2538-3b2d-afef-ec8609f04d89 | -2.94531 | -51.05472 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a29db3ea-d12d-3c28-86ef-9b9eaff0bc87 | -7.21082 | -46.71562 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5a5190b-f596-3683-8e87-25fc2aa9a43e | -3.1114 | -51.21079 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c9b3d31-009e-3bab-acc7-810ebdfddc75 | -3.10624 | -50.18255 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e640c320-b75b-34f1-a5ee-fb1def7c62e8 | -4.87394 | -47.54397 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0430507c-6821-33b6-a029-c53ede1e7883 | -4.64914 | -48.647 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5110c85-1d29-31ec-9a08-92fb96008a83 | -4.97086 | -56.27843 | 2025-10-28 04:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b60709cd-9a13-35f9-85bb-5174bb8b5b39 | -3.05124 | -53.01769 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6675ab0b-8ce9-3386-a92a-ba1971ff1756 | -4.46441 | -43.23542 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 682a093a-8cdf-3fb4-bab8-e859dcd96248 | -5.65953 | -41.1494 | 2025-10-28 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 184d127d-9561-3adf-b1bf-71e5af0e4688 | -1.3345 | -53.60347 | 2025-10-28 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe7820d3-dd12-329c-a016-dbdcdf7adc67 | -7.49039 | -47.03504 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ad64364-ffab-359a-805e-2c5672aeca1b | -4.7407 | -48.01935 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b19a517-6fa5-3498-9cd9-cdfae0179c4e | -5.61054 | -47.10606 | 2025-10-28 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f7516be-e95a-34d3-ad98-39378bb77938 | -1.69857 | -53.69493 | 2025-10-28 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cda343a-7cde-3a62-907c-6e2cc503d913 | -8.19611 | -44.43935 | 2025-10-28 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c067edcc-e699-3535-b3bf-e325949e1fb9 | -6.58944 | -48.58763 | 2025-10-28 04:42:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README54.md)
