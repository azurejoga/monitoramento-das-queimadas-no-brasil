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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23c287e2-6ae1-3681-83e0-c87098848638 | -14.9161 | -46.8312 | 2025-10-06 12:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d8a20248-a016-3451-81c5-85bda8032648 | -15.6206 | -52.5288 | 2025-10-06 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| be2613c2-de48-364d-8287-0400492ddd42 | -18.2773 | -53.3082 | 2025-10-06 12:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8f6de789-0532-3d6a-926a-cf0a3831798d | -13.343 | -48.0519 | 2025-10-06 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| aa8b6d0a-a3d3-3f87-8f41-b527d9d5f13f | -18.1167 | -53.3977 | 2025-10-06 12:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 98.0 |
| f71221f7-50a9-3d97-affe-ba9dddca1a05 | -8.6144 | -46.2778 | 2025-10-06 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| fdfe6320-ad80-33c8-b80a-7cdf0b952ace | -11.8033 | -45.0856 | 2025-10-06 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 97fdaefc-250f-34e8-8eb7-8f99e25de5e1 | -18.1565 | -53.3915 | 2025-10-06 12:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 56.3 |
| fad23d09-4522-3eeb-ba93-58690ed84051 | -15.3546 | -47.3007 | 2025-10-06 12:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 977548c6-3157-3a39-b092-c661f29f08c3 | -14.2754 | -45.8647 | 2025-10-06 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 7dd4f7b1-5b21-3413-82a0-9b17c06f1323 | -18.1172 | -53.3763 | 2025-10-06 12:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 68689538-a2b7-3357-bce7-4cce58c93f4d | -14.6897 | -48.3797 | 2025-10-06 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 03f60214-8301-3ea8-9a87-54299b90326a | -14.6893 | -48.4021 | 2025-10-06 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| dc4c45ac-898c-31e0-8bc3-9126ca9de7ff | -18.157 | -53.37 | 2025-10-06 12:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.0 |
| d7247851-c4b4-3f34-b03e-f8c07b442db8 | -18.1371 | -53.3732 | 2025-10-06 12:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 241.0 |
| bd645b70-7d72-3fd9-84dd-ea785015a564 | -17.8417 | -57.6254 | 2025-10-06 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 95871f4d-9136-3d11-9db3-5db88bb03540 | -9.9776 | -48.7622 | 2025-10-06 12:30:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| f2fb0831-8d85-3a5c-a802-4eaef5cd1514 | -8.6139 | -46.3227 | 2025-10-06 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c6938797-2702-3dd0-a51a-61064a23ade4 | -12.9812 | -46.8051 | 2025-10-06 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 13c40099-8827-3b2c-8190-ff7f24f55b30 | -10.6184 | -46.3646 | 2025-10-06 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 2958581e-2f04-3de0-a3e4-d2d92eccd43f | -10.9688 | -47.061 | 2025-10-06 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 2c616187-860f-3b2a-a55c-a74b824fe944 | -14.5438 | -46.9633 | 2025-10-06 12:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 1722afe9-2327-3c09-8dd8-1703fdc38024 | -8.6141 | -46.3003 | 2025-10-06 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 6c3ed654-bd07-3719-a5a4-abf09195ba28 | -12.9146 | -47.288 | 2025-10-06 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 51f1f3f1-3ee4-37d2-8ca4-94857d1e9834 | -14.2759 | -45.8416 | 2025-10-06 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 6f2b7806-c277-378f-8de9-eaeced032021 | -12.1458 | -50.9523 | 2025-10-06 12:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| e0686579-d1e5-323b-ba3d-621f23252898 | -14.6985 | -45.1858 | 2025-10-06 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| bb71a125-4af9-37dc-945f-41ef0d696912 | -16.0038 | -50.8365 | 2025-10-06 12:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f2e694d7-cc7c-3b68-9947-b4c9fb7afd5c | -9.6614 | -45.6667 | 2025-10-06 12:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 87d6d138-c8fb-3dcf-a02f-403a0cada4e2 | -18.1366 | -53.3946 | 2025-10-06 12:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 111.3 |
| dc8cd6dd-0c42-3db8-bffd-e9ca5015beab | -13.3904 | -47.576 | 2025-10-06 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 94f45e68-272d-3ae9-91a9-e572ec2b3a83 | -14.3161 | -52.9764 | 2025-10-06 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f985f28b-6f5a-3f1d-ad1b-8c2e1fb8aa4e | -8.1879 | -44.2283 | 2025-10-06 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| be418624-a197-3add-b3fa-e159495fe8db | -8.6141 | -46.3003 | 2025-10-06 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 8b612c2b-9609-3220-99f4-23145cd70089 | -12.9844 | -51.0433 | 2025-10-06 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d18644f3-b211-3a6b-9cb3-b9599d1c6be0 | -12.9812 | -46.8051 | 2025-10-06 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| b64fc07e-a692-37cb-8daa-0ba174f3f76e | -15.3541 | -47.3235 | 2025-10-06 12:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| bda5601f-8e31-35be-858f-48f6372c5080 | -17.8417 | -57.6254 | 2025-10-06 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 75f8a629-eefd-320c-afaf-5cd8f6b4e1af | -14.6893 | -48.4021 | 2025-10-06 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 3c5f7c5d-74f3-3d82-ad90-d44c013c1678 | -9.6614 | -45.6667 | 2025-10-06 12:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 763ace39-d310-3adb-8406-454d23929f1d | -15.3546 | -47.3007 | 2025-10-06 12:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| c555249a-f93c-3504-b5f7-c58cf009c659 | -9.6617 | -45.644 | 2025-10-06 12:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| e1e6c8c5-e746-33f0-939a-eb93309c5790 | -11.8025 | -45.1318 | 2025-10-06 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 37a74716-22a7-38d3-a635-cf19049f37b1 | -9.9776 | -48.7622 | 2025-10-06 12:40:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 787dd3a8-087d-3b5b-8715-d994fba76f68 | -11.8029 | -45.1087 | 2025-10-06 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 817c1f10-e0c2-3d00-a57f-c40bb6099cf1 | -13.3623 | -48.049 | 2025-10-06 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 7a1f1a83-2c8d-3042-bb75-db4444e86456 | -13.3627 | -48.0267 | 2025-10-06 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b4cdee0e-00d7-3d5c-9075-582f8b3cf831 | -8.1687 | -44.2534 | 2025-10-06 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 4869dd93-99fa-330f-9bd7-6b7916892057 | -13.343 | -48.0519 | 2025-10-06 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 9651fab5-78fc-36d8-b19b-b3d1eef42513 | -18.0011 | -57.5238 | 2025-10-06 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| d405d46a-12d8-37f9-8812-c8f34c1473cc | -18.2773 | -53.3082 | 2025-10-06 12:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 226.2 |
| fa662be6-b67e-31af-b4ca-11836a0c83a0 | -8.1684 | -44.2766 | 2025-10-06 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| abee8a0b-74d0-33bd-812d-f334185c6f61 | -10.4277 | -50.4159 | 2025-10-06 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| ac71f3c8-1c5b-328c-ab4e-27226b96007f | -8.8803 | -47.6061 | 2025-10-06 12:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e6c059ea-804f-3233-8f59-0f348d67e18c | -13.2515 | -47.7979 | 2025-10-06 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| b638d6bb-8ba9-38f2-9fd6-7a7f759d81db | -14.2754 | -45.8647 | 2025-10-06 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| bff0040f-7d17-3f81-9de7-9248c7b33b98 | -9.9779 | -48.7405 | 2025-10-06 12:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9de7fdb2-fd19-30a5-bdde-2f0f5a8c3078 | -10.465 | -50.4547 | 2025-10-06 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e3c0fa03-91f8-34df-93c1-2b8c71a8abc5 | -12.1458 | -50.9523 | 2025-10-06 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 8f3b27a1-db18-34b9-ae51-9086b19f76aa | -8.8729 | -46.6985 | 2025-10-06 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0e34b6c2-ac4f-30c6-b44c-ff6440ecef71 | -13.3237 | -48.0547 | 2025-10-06 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1567da10-28dd-35ab-81af-ccd4b394ac57 | -8.6139 | -46.3227 | 2025-10-06 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| fd22152c-50b3-3534-96d3-3cd832321aa4 | -18.2574 | -53.3114 | 2025-10-06 12:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 33b6babe-3b27-352d-a066-7e06c433754b | -14.6897 | -48.3797 | 2025-10-06 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 41bb70b5-91f2-35d6-9e61-5ec4d17bff1c | -10.6184 | -46.3646 | 2025-10-06 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e4209381-4b75-30ef-bc2b-fae5ed13401f | -8.6144 | -46.2778 | 2025-10-06 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 001d234d-1477-357a-8efc-fcd5fec7972e | -8.5376 | -46.3976 | 2025-10-06 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b9c2a1fb-6b99-361a-8022-2ec66b417976 | -8.5032 | -44.6556 | 2025-10-06 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| e3a97c54-4676-387c-821a-e8ddefd66d89 | -14.6893 | -48.4021 | 2025-10-06 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3aadb07e-1730-313f-ad3c-79c6c092eea9 | -12.9812 | -46.8051 | 2025-10-06 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 245.7 |
| dd74548a-8c79-35ed-aa71-222ce60ee520 | -9.9779 | -48.7405 | 2025-10-06 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e582bc87-18a4-3711-a98a-211dd830673a | -18.1172 | -53.3763 | 2025-10-06 12:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 383.4 |
| 3b31b0e5-eac0-3966-b750-95d2f1c9e7d7 | -16.0038 | -50.8365 | 2025-10-06 12:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 50d19f0c-d154-33b8-9837-061a94470500 | -8.8794 | -47.6722 | 2025-10-06 12:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 71dd4726-afcf-360c-90c4-885c40869358 | -8.6327 | -46.3208 | 2025-10-06 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| feae6a07-3b61-31a4-b6f5-18bb5fe8a369 | -14.6897 | -48.3797 | 2025-10-06 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c863f9e9-bb2f-36a8-85ad-87c372f7c8b8 | -11.6849 | -45.2872 | 2025-10-06 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| a431fa0d-e6a1-3e52-8a1c-1f075613301d | -9.9215 | -50.1682 | 2025-10-06 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 169bfda4-afa9-3140-a91e-2243b9b55e42 | -17.8417 | -57.6254 | 2025-10-06 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.5 |
| bd0cb06b-6465-36d2-bdfb-12ccb2692ac6 | -15.6206 | -52.5288 | 2025-10-06 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c60b09b3-1d9c-3b39-a4d2-d6a33dec7184 | -18.1366 | -53.3946 | 2025-10-06 12:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d0861943-075e-31ed-afed-cb16eb0bb3bc | -10.6184 | -46.3646 | 2025-10-06 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4b2ed2d4-b8eb-37bb-ba93-111d5dbbaf78 | -12.5929 | -48.1144 | 2025-10-06 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a9e9cd49-ee92-34b1-adb5-bc8ddd2ab565 | -14.5623 | -47.0056 | 2025-10-06 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| cb29701f-b63e-3244-89dd-e4affdf23a1e | -9.6614 | -45.6667 | 2025-10-06 12:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 900141eb-33a1-3c4e-9632-dcc908be82f3 | -10.465 | -50.4547 | 2025-10-06 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 5826e305-c3be-34b0-b3fc-f69d334003f7 | -19.49 | -44.8839 | 2025-10-06 12:50:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 135.2 |
| edd38c9e-120c-3227-815a-5ef4c9e45a1f | -15.2351 | -49.2914 | 2025-10-06 12:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 6aff1a36-90b5-3f5e-879f-b32c994bb12b | -14.882 | -51.5207 | 2025-10-06 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 687a9da7-2d6e-3139-88a0-81f92904966c | -17.9813 | -57.5262 | 2025-10-06 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |
| c0edd7cb-41e4-3646-8a60-32f0d82083bf | -10.7281 | -46.6433 | 2025-10-06 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 32cbb788-a2bd-35ba-b88d-4c66fd2399f0 | -9.6804 | -48.4014 | 2025-10-06 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| b30abd8b-2e6d-39b5-bd4a-2fea5354d9b3 | -8.1687 | -44.2534 | 2025-10-06 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3a3c4d8e-8b65-340e-a918-cff9ab82c338 | -9.4866 | -45.9813 | 2025-10-06 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7b7522f9-dcd2-33b3-a46a-af950a0f6777 | -14.5628 | -46.9828 | 2025-10-06 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 241.2 |
| 691b73b9-69ed-3630-b0cd-42d881be045f | -13.3044 | -48.0575 | 2025-10-06 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6ae3866c-57c0-3974-aeea-aa30bcd3c452 | -18.2773 | -53.3082 | 2025-10-06 12:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 1ce16f98-ff56-3cba-9b6d-5712f4d5bd55 | -19.5111 | -44.8545 | 2025-10-06 12:50:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 513c5570-bb35-3efd-ac16-79e2e291e769 | -13.3237 | -48.0547 | 2025-10-06 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 49f6642f-1062-3eda-b01f-f971a29385a1 | -8.6141 | -46.3003 | 2025-10-06 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |


[Clique aqui para ver as próximas entradas](README86.md)
