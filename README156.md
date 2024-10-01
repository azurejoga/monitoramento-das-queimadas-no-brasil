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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eff2fec4-3344-3709-8549-8ec141db7886 | -12.82037 | -62.88562 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29765937-8e48-385b-910d-263a3cc13f8a | -12.81581 | -62.88499 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54e18402-bb62-34c8-9b5d-3aaadd5e1591 | -12.80669 | -62.88375 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21213372-f0ea-35d5-b838-5bcc36233e0b | -12.78541 | -62.90486 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7690ee16-b442-3b4b-ae7a-b9f1398937bf | -12.78146 | -62.89952 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 692d3288-1346-3fb1-a73a-7bbd36900193 | -12.78085 | -62.90424 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 639b777e-3bad-3f1c-977f-2fc5b6a55790 | -12.7769 | -62.89891 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76c52c7a-6524-3cc1-9881-7987ed50d419 | -12.7763 | -62.90362 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d63b54a-f541-39bb-b023-83179cb62713 | -12.77235 | -62.89829 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14101d37-64c4-3f1d-b17f-8547a344973d | -12.77174 | -62.903 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 533827dc-48e4-3084-8e74-c657b1f6857d | -12.75808 | -62.90113 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ff26667-1384-3666-930b-b27b1a46c978 | -12.75749 | -62.90584 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9467c9e5-1e0b-396e-8ac1-79a67d022055 | -12.75709 | -62.90355 | 2024-10-01 05:53:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf004544-8c30-38b7-a6f7-ddc03f7be34e | -12.33453 | -63.71947 | 2024-10-01 05:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c48a54f7-46c6-3723-9f98-550541b935ce | -12.33024 | -63.71888 | 2024-10-01 05:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6f8a44d-aeb7-3e2f-8a77-80a30d7ea78c | -12.13573 | -64.317 | 2024-10-01 05:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75512c5e-ba5c-3934-a5c7-a306f6b08c4f | -12.1352 | -64.32073 | 2024-10-01 05:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d238aa3-3875-369c-9e0e-6648dd15edf6 | -12.13476 | -64.31617 | 2024-10-01 05:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de88ec69-6ece-3c50-a9a8-0bbc640fd8c4 | -12.13426 | -64.31991 | 2024-10-01 05:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 841d3e66-0b40-3bd7-abc8-bebbf6c37a62 | -11.69438 | -64.05795 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2125fc88-fb7f-3382-8eec-5500cd60481c | -11.58949 | -63.78681 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d11d246a-7983-39ab-a86d-a1b660ee61e2 | -11.58474 | -63.79017 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc2f24fe-6ad5-3cad-9af1-c554868e02e7 | -11.58421 | -63.79412 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 562c4d27-de07-3401-ac98-6c2fec45a1f9 | -11.57947 | -63.79741 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 31154e3b-946e-3c00-92db-7e02196fe865 | -11.57474 | -63.80071 | 2024-10-01 05:53:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25021dff-4340-31e4-839e-2d3f18cacaf1 | -5.26548 | -55.92572 | 2024-10-01 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 379f0c8f-097d-3684-9be3-d43dee186fdf | -2.90807 | -61.8332 | 2024-10-01 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7dcc57a-198a-3fcd-bd37-62867537f31f | -2.88839 | -61.87827 | 2024-10-01 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a08c1a8-1e76-35a5-9268-1ccfa5c3638a | -2.88724 | -61.88604 | 2024-10-01 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 267cadc2-c51d-3fe3-b35b-c9b9baa6c7bf | -2.88666 | -61.88991 | 2024-10-01 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9292505-98c7-3f02-8391-d0b29289d325 | -2.88419 | -61.87757 | 2024-10-01 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3a43f73-2e5a-316d-9ac9-d6c0cf0308fd | -2.88379 | -61.8779 | 2024-10-01 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a522e57e-0e0b-3336-a5ef-4e02a74929d8 | -2.88361 | -61.88147 | 2024-10-01 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8931b2fa-02fb-36e5-8f9c-25346022f4ca | -2.88318 | -61.88177 | 2024-10-01 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4cd5bbd-b3ef-3ce5-b553-2dbf13bf6c1a | -19.11916 | -57.46577 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| b2efbac5-67cf-35b5-b427-21873a946d5d | -17.21096 | -57.37874 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 79afc46c-f5c1-37f7-aa65-44bff2f35a1d | -17.21027 | -57.37879 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d0757e1e-9e8f-36cd-a84a-913581df2bf3 | -17.20411 | -57.37801 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8717882a-8a96-36f5-bc4b-225fc359d34a | -17.20353 | -57.38448 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9f40c334-4218-33ab-8075-4e1eafbc1ed9 | -17.20342 | -57.3781 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2e7e8abc-4ac7-326b-922f-9a667ebbc775 | -17.2028 | -57.38456 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 93f24751-2c61-3486-830b-ce0decd6fea3 | -17.19595 | -57.38386 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 982afb52-05d6-31ca-82a8-673cffd8bfca | -16.89506 | -57.69998 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8eec0a89-8cbb-3e6a-a208-50f806ad55cd | -16.88779 | -57.70536 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8088e834-4050-3de8-b025-cda328a8f665 | -16.87437 | -57.70397 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ab6d7432-605d-3824-8871-563a6296f8d7 | -16.8714 | -57.69867 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 42795ce5-9afe-3e5d-abee-5bcd2bf7d5e9 | -16.8708 | -57.70476 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5856940c-a5f9-36a3-b730-ba60b249b11e | -16.86823 | -57.69719 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 148a9b3f-e950-3153-8613-2f894263f1ca | -16.86469 | -57.69801 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c110a56d-0079-350e-866f-12f8eaf0167a | -16.7618 | -57.7852 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8a8e82b3-f0d7-3361-9841-54e677e05360 | -16.76124 | -57.79118 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d8d3afba-1de5-3a12-af4e-4f008e556864 | -16.76068 | -57.79716 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 10f80bb4-eddc-3d3a-b9ba-a8a305aaa96a | -16.75956 | -57.80916 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aa4b06c2-cdc9-3e6d-8907-4e7b92fd9d8f | -19.15953 | -57.48032 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| feb08263-e1ef-3535-8c60-01254c643b94 | -19.1526 | -57.47944 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f262bf77-7723-3118-9cf3-6bb57916384a | -19.13239 | -57.47509 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| afff9e2a-5062-3a4e-b3a1-f143b24548ff | -19.12611 | -57.46638 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| b35c9d58-d1e0-3c3b-b088-21824950fa8a | -19.12547 | -57.47414 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.3 |
| 63e64209-3e43-3121-abfd-50761d209518 | -18.71316 | -57.32716 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b55366f4-7676-3b6b-bb50-a09bebbc6876 | -18.70675 | -57.31968 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 1476ec0e-f72b-303d-a8a6-f682d6ee2e38 | -18.70618 | -57.32652 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| a355e03f-1194-3dfe-9fda-6c0de53b11f3 | -18.70561 | -57.33334 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 893c5205-0f63-32c1-a1ab-f2c06f50a52c | -18.69977 | -57.31905 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| ce9640ae-1ae4-330f-9f36-22ce4a1c7ebb | -18.6992 | -57.32587 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| d0a2b166-e940-385e-83c8-98c4825e8282 | -18.69864 | -57.33268 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| f4ee27a9-a7aa-3c4f-afb7-2ab1612071d7 | -18.69222 | -57.32523 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 455dcebc-1c3d-37d9-820f-26d8ef208ef8 | -18.69166 | -57.33203 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9b338154-9718-3cd1-a250-8fcdc9f578c5 | -18.68468 | -57.33138 | 2024-10-01 05:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1688427d-a873-311b-8a85-f83d382ee439 | -17.04542 | -58.39653 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3d2b8959-0b32-3eba-b46a-a894b9981cc6 | -17.04488 | -58.40206 | 2024-10-01 05:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bb599cab-6c3c-322e-83d0-131e5efc4858 | -9.31941 | -66.54391 | 2024-10-01 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29143e91-f65b-3524-8a95-818620c6103e | -9.05837 | -67.82012 | 2024-10-01 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74500cb1-dd78-3cd1-b71e-5047f39f30ee | -9.0488 | -67.79305 | 2024-10-01 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47bcd21e-f1ff-3a0a-82ca-5b44b6b98c7b | -8.79264 | -69.02728 | 2024-10-01 05:55:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3797c05-04db-3dc5-ba7a-4c8baa477bd7 | -8.69519 | -66.66264 | 2024-10-01 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54f41ad1-9b00-3749-93d8-758f774926e1 | -7.92754 | -61.55742 | 2024-10-01 05:55:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 090b1317-0269-3b8f-931a-dc07caa5c047 | -11.6555 | -64.9991 | 2024-10-01 05:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 58f692c5-b36b-3bac-91f6-1d6c853bfbb6 | -13.04 | -51.23 | 2024-10-01 06:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98fd596e-5f22-328b-a577-3b7c9fdd4112 | -12.98 | -51.32 | 2024-10-01 06:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e697c074-a91a-378d-9e0c-e0daddf22353 | -12.98 | -51.26 | 2024-10-01 06:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 198ffec9-4aaa-3221-89f5-adc68513a4bc | -13.01 | -51.27 | 2024-10-01 06:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0211d72f-b223-380e-ad4e-b9b3a91a2c4f | -13.01 | -51.21 | 2024-10-01 06:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4dbece5a-627e-325d-be73-e032c827da61 | -13.04 | -51.17 | 2024-10-01 06:04:10 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 09dc1f22-ed1f-3dd5-92bd-dffb4fc6a88c | -2.85 | -50.72 | 2024-10-01 06:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9622e4c0-925b-360a-aefc-058399745bdb | -2.88 | -50.78 | 2024-10-01 06:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64a23169-278f-375e-9c9e-4bdc251b575b | -2.88 | -50.73 | 2024-10-01 06:05:11 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 936c76bd-3974-3cc1-a6da-bc5fc6c17f76 | -11.5695 | -63.8084 | 2024-10-01 06:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 776cb387-bed6-3219-99de-c290d3f81a11 | -11.5694 | -63.8274 | 2024-10-01 06:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| ce7dbdec-1cc6-300e-9868-f828b438bc55 | -11.6743 | -64.9983 | 2024-10-01 06:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| c9bc5953-9207-3415-8983-309f6df96f83 | -11.6555 | -64.9991 | 2024-10-01 06:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 31472a1c-cfac-3b65-bd20-5dc85f74991b | -11.5695 | -63.8084 | 2024-10-01 06:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 07994c7f-5ced-3112-91f8-f67585cbaff6 | -11.6555 | -64.9991 | 2024-10-01 06:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| e0b6810d-02f6-33ee-921f-6b35e77fec1b | -11.6743 | -64.9983 | 2024-10-01 06:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| dfed9f41-5f74-3a54-bb42-041ae7429c3a | -16.8787 | -57.6971 | 2024-10-01 06:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.3 |
| 3de66a47-0fe4-3320-a3c1-ba077933f577 | -16.898 | -57.7153 | 2024-10-01 06:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.1 |
| 60e3ed9d-952c-3dfc-aaf6-eb18ff8d87b1 | -16.8983 | -57.6949 | 2024-10-01 06:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.2 |
| ac2f3b37-7f88-35e0-806e-a248957fc4a8 | -17.0895 | -56.7503 | 2024-10-01 06:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 8852714b-bfd5-3d26-8655-9410aacc3e73 | -17.1095 | -56.7273 | 2024-10-01 06:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| b43ee108-8e1b-30d1-a539-1a32d674ae28 | -18.6973 | -57.333 | 2024-10-01 06:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.8 |
| f2cc698c-3d81-33f7-9139-61fa17c829a4 | -18.6977 | -57.3123 | 2024-10-01 06:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.1 |


[Clique aqui para ver as próximas entradas](README157.md)
