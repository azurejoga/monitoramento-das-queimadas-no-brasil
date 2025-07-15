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
| 2f0185f3-a0f6-3d15-ad2c-1d76511010a4 | -11.4584 | -45.1126 | 2025-07-15 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 86d28c84-a676-3af3-b0fd-6aae42682fa1 | -11.478 | -45.0868 | 2025-07-15 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c3d1950b-443e-32cc-a28b-d5c784a8acd6 | -5.5241 | -43.8878 | 2025-07-15 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| cee50d73-5044-3959-8f5a-05869b3c522b | -11.478 | -45.0868 | 2025-07-15 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 07115b0b-7a75-3143-8ae0-3a05366a8047 | -11.4393 | -45.1154 | 2025-07-15 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 31f84a72-9ef7-34b6-96fd-7d36daef0ca8 | -11.4397 | -45.0923 | 2025-07-15 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 9e62dc19-ef9d-3cc8-a4a1-f72451e8f129 | -11.4588 | -45.0895 | 2025-07-15 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 235.3 |
| 8d2b2c84-46a2-3701-80d3-534c039116c8 | -11.4592 | -45.0664 | 2025-07-15 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 762bbe59-961a-3d0e-b5de-72d2d6ff6fdb | -5.5429 | -43.8864 | 2025-07-15 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 8107da4b-9ec2-32e4-bb45-fcbe6ac44f03 | -11.4584 | -45.1126 | 2025-07-15 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 6a5189e2-0e2f-3d1b-a622-70818e4fa64b | -10.5776 | -49.1316 | 2025-07-15 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d100d168-1a6d-3dd3-a475-77b26fdb40dc | -10.5586 | -49.1337 | 2025-07-15 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 12627b21-7505-3cd8-9f0d-b570dcfd2b87 | -11.478 | -45.0868 | 2025-07-15 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 54dcc80e-ce7a-394d-8479-6eb2c7fdf99d | -5.5429 | -43.8864 | 2025-07-15 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 853983f8-9701-3404-8662-91fadf9fc929 | -11.4588 | -45.0895 | 2025-07-15 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 213.7 |
| a6d3786e-512e-3941-83c6-621539ebfd69 | -11.4592 | -45.0664 | 2025-07-15 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 97434cdb-a18f-3223-9d91-127f013f7676 | -11.4584 | -45.1126 | 2025-07-15 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| ea2835c7-78a5-3712-a60a-9f7d016eb5e1 | -11.4397 | -45.0923 | 2025-07-15 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 77a43456-4ce6-3615-b528-0c91db954146 | -10.5776 | -49.1316 | 2025-07-15 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| a15df80c-def0-3030-8ba2-a07fff143ebc | -11.4393 | -45.1154 | 2025-07-15 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 7dbcc2d6-6aaf-35b0-8694-fdc28b730fcc | -10.5586 | -49.1337 | 2025-07-15 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 048bd006-2e51-3ae6-8904-bf0d352a51a4 | -11.4588 | -45.0895 | 2025-07-15 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 225.9 |
| 809c4df4-c04f-325e-81bc-d535469f9279 | -10.5586 | -49.1337 | 2025-07-15 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e58fa241-90c2-3d7b-8e77-ebf99bc12215 | -11.4397 | -45.0923 | 2025-07-15 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 8c6544fa-0d16-3956-a291-a813d74efc3f | -11.478 | -45.0868 | 2025-07-15 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 264fc97a-842f-3521-9c4d-ccf932e4a46d | -11.4584 | -45.1126 | 2025-07-15 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 89c91b63-adf0-33ee-9a91-7ea9440af0d9 | -11.4393 | -45.1154 | 2025-07-15 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 8edb1006-bf1c-3c1e-bec4-ea338a20d670 | -11.4592 | -45.0664 | 2025-07-15 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c1758a91-e787-3272-bef6-75b1c91da369 | -10.5776 | -49.1316 | 2025-07-15 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| a461a073-06a3-39ca-bdce-a5a386d4cafe | -10.5586 | -49.1337 | 2025-07-15 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 099e21e1-a0a0-393f-ac54-66712d6cc570 | -10.5776 | -49.1316 | 2025-07-15 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| baa96373-185d-3b65-b92d-29b8829fee51 | -11.4397 | -45.0923 | 2025-07-15 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 21417f32-350d-318c-89fa-ec25cb45bb5b | -11.4393 | -45.1154 | 2025-07-15 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2c08340a-8e6a-3346-a7ec-129f3482fe48 | -11.4588 | -45.0895 | 2025-07-15 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 238.9 |
| e4acfb0b-800f-30d6-9c20-a1710dee3081 | -11.4584 | -45.1126 | 2025-07-15 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b8d5f9c1-fb65-3c8e-9f32-eb537dd9370c | -11.478 | -45.0868 | 2025-07-15 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8f074eff-486c-3842-ba03-01535591994d | -7.40136 | -72.60223 | 2025-07-15 02:24:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 20526d35-ff29-30fd-9399-cd933348b514 | -7.39984 | -72.59183 | 2025-07-15 02:24:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b9b477d8-ddcd-325e-a6ba-56179408766d | -11.4588 | -45.0895 | 2025-07-15 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 276.7 |
| b4fd163e-380b-3558-9d1a-35de97a22a7e | -10.5776 | -49.1316 | 2025-07-15 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 6ad20261-f4ca-3991-bd71-5611c052667d | -11.4397 | -45.0923 | 2025-07-15 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9be87062-878f-3fd5-9072-fc71a85521b0 | -11.4584 | -45.1126 | 2025-07-15 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 02c3c288-6fa5-3149-9971-5473f5068784 | -10.5586 | -49.1337 | 2025-07-15 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 0a9ef1c8-953b-3749-98ad-1cb2d400e8f5 | -11.4592 | -45.0664 | 2025-07-15 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 58fdf617-792d-3467-a2db-0e9e78637102 | -11.4393 | -45.1154 | 2025-07-15 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 384d76fb-58fc-3561-9662-3e6ce664266b | -11.478 | -45.0868 | 2025-07-15 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 8fdd2614-6501-3dde-a62e-2e5b9a426f54 | -11.478 | -45.0868 | 2025-07-15 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 562bb228-ec21-38d8-addf-9dfe1dcb4a0e | -11.4393 | -45.1154 | 2025-07-15 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| eeac6a57-1725-3a65-9be8-8be60de78184 | -10.5586 | -49.1337 | 2025-07-15 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a06af68b-de5c-3d05-98d0-288009f2299f | -11.4588 | -45.0895 | 2025-07-15 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 248.8 |
| 9debfc51-2ea3-3114-8d71-aab2739bc821 | -11.4397 | -45.0923 | 2025-07-15 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| b69a5f5c-a5cc-3d0e-89f8-731325c78862 | -11.4584 | -45.1126 | 2025-07-15 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 4b86c078-2f77-3243-b29c-ef0e6299fb83 | -11.4584 | -45.1126 | 2025-07-15 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| b75741d6-1a6e-3303-93b9-25145615e869 | -11.4588 | -45.0895 | 2025-07-15 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 260.9 |
| b2e55b39-301f-3267-8aac-f96276582005 | -11.4592 | -45.0664 | 2025-07-15 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| e9f10d2e-c93e-314e-8641-6c2639d3d10d | -11.4393 | -45.1154 | 2025-07-15 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 80807644-dcda-3ac7-a740-ad4fcf280912 | -10.5776 | -49.1316 | 2025-07-15 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| df79540c-c04a-3d55-809e-658ddc369a75 | -11.478 | -45.0868 | 2025-07-15 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 659b0c07-6e13-3421-8fd6-8a5ecd2869b6 | -10.5586 | -49.1337 | 2025-07-15 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 55754eb3-eafd-38ae-8611-85f196745ccb | -11.4397 | -45.0923 | 2025-07-15 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 04fac12b-f345-3c79-9b46-e71867f1df37 | -11.4592 | -45.0664 | 2025-07-15 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b5566be8-c718-3e36-a090-9f069233e5db | -11.4584 | -45.1126 | 2025-07-15 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 07d03f60-4d90-32e6-b3c5-4fb3321cb3a6 | -10.5586 | -49.1337 | 2025-07-15 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 15383616-7698-31a2-9cef-73c8bd680d42 | -10.5776 | -49.1316 | 2025-07-15 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 1878cafe-fe84-3a66-b2c8-7add12516c45 | -23.121 | -50.0011 | 2025-07-15 03:00:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 55458cbc-8533-3a92-9b49-077a5a6b2841 | -11.4389 | -45.1385 | 2025-07-15 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 10e1a8cb-9d6e-3622-b754-20cd9ed05aef | -11.4393 | -45.1154 | 2025-07-15 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1e920881-67e1-3122-bd9c-29d3e94e0c84 | -11.4397 | -45.0923 | 2025-07-15 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 2258f74b-a397-35db-9812-5bbe011b7001 | -11.4588 | -45.0895 | 2025-07-15 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 256.2 |
| 02f2b16c-cf7b-3774-b9ae-3d17db42d73f | -10.5776 | -49.1316 | 2025-07-15 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 376bac02-ef06-3869-90c8-cbc6b1ef26d7 | -11.4393 | -45.1154 | 2025-07-15 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| cc76a608-b46e-3ce6-bf86-7e9b45a37da8 | -11.478 | -45.0868 | 2025-07-15 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 0ce53e90-5276-3805-9edd-ee44a13cc8a6 | -11.4397 | -45.0923 | 2025-07-15 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d6287e9f-bc38-3e45-8de6-dd0d6e379adf | -11.4588 | -45.0895 | 2025-07-15 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 251.1 |
| 84f71e06-9cae-356e-aa74-6b2fa87831a0 | -10.5586 | -49.1337 | 2025-07-15 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| fae62614-e8a8-35d7-adb0-7ca986fa4d76 | -11.4584 | -45.1126 | 2025-07-15 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| b55211e5-b196-3a45-9a8d-24d2ecf48c5f | -11.4389 | -45.1385 | 2025-07-15 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 34b82cd7-e9d8-3a58-b7f6-9d1b435482d2 | -11.4397 | -45.0923 | 2025-07-15 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 34bb1b1c-9180-3b57-9532-c805d2c51c00 | -11.4584 | -45.1126 | 2025-07-15 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| a16543cf-c2e8-3ada-bb0a-34370673fbd5 | -11.4393 | -45.1154 | 2025-07-15 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 56200467-50b5-3795-ab07-c5aa69ce6a43 | -10.5776 | -49.1316 | 2025-07-15 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| ee78109f-9ca8-37d4-888e-45367ddc7c30 | -11.4588 | -45.0895 | 2025-07-15 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 284.4 |
| 3a143a4e-d123-3700-a3f9-c205e21f2c36 | -11.4592 | -45.0664 | 2025-07-15 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 54e0261a-94bb-352a-8ffe-4c7c05e7d821 | -11.4588 | -45.0895 | 2025-07-15 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 250.1 |
| 075392a3-7fdd-3c3a-88e1-d5e788f5d57c | -10.5776 | -49.1316 | 2025-07-15 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d8ae07e5-eafe-307c-af27-75381bdb71aa | -11.4584 | -45.1126 | 2025-07-15 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 1de949b4-14ea-3abe-bc4c-3fc48d106cd4 | -11.4397 | -45.0923 | 2025-07-15 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| dbc754cb-4373-3e69-8a0a-6caf0672f21d | -11.4389 | -45.1385 | 2025-07-15 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 1e3a5ccb-3289-3ff0-8bf4-ecabfcf7514f | -11.4393 | -45.1154 | 2025-07-15 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8ad44513-13c7-37f8-8fdf-f1d97d90fb04 | -11.4592 | -45.0664 | 2025-07-15 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| edf400cb-ca54-3ed3-9a65-c073366aba34 | -11.4389 | -45.1385 | 2025-07-15 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| c6422a54-12bb-33e8-8875-3a06682b42e5 | -11.4397 | -45.0923 | 2025-07-15 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 930f914a-f547-3b5a-b3e7-688d8a42102f | -11.4584 | -45.1126 | 2025-07-15 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 9a9827ed-6374-32d3-ab59-7124e7639f14 | -10.5776 | -49.1316 | 2025-07-15 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 10ee0b86-acfd-3a6d-b27e-5e189695e2c2 | -11.4588 | -45.0895 | 2025-07-15 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 34fe455e-23f8-317b-9de3-9b221e5043a3 | -11.4393 | -45.1154 | 2025-07-15 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| eaf3ea7b-8feb-3b31-a14b-202492ea7fb3 | -7.20152 | -43.10996 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b0108ab5-85e7-3efe-a52e-ad81072d76ce | -6.71311 | -44.32787 | 2025-07-15 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9344b1c-ece8-3fc3-a10e-4eeda1b7a032 | -5.98332 | -43.76425 | 2025-07-15 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e1d087a-6652-38cf-b8e3-579a8e6e8937 | -5.69566 | -44.2445 | 2025-07-15 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README5.md)
