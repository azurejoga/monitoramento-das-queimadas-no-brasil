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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdbcb073-683a-3da3-b083-6717f709678c | -2.1492 | -50.906502 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df0aec30-3529-3ea6-924f-9396c71e2fa2 | -1.7524 | -54.508202 | 2024-11-24 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce9bf017-70b5-37e7-a25a-9899e2d55140 | -3.1019 | -45.780102 | 2024-11-24 00:25:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8642e3-0a71-30bd-8e8c-9ee14cf099ec | -2.2484 | -46.826599 | 2024-11-24 00:25:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39c37f2c-8048-3cd4-9051-4693932cda75 | -0.5716 | -51.720901 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3648e312-e364-3141-beed-da123cb71ac1 | -4.3802 | -49.741299 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac456be3-3c9b-3a0e-a83d-0d44794e0df2 | -4.2659 | -48.681599 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d44f0f7b-fefc-35f6-84b5-67da82ee084c | -4.3068 | -43.195702 | 2024-11-24 00:25:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9acd2c8-a0f9-3715-911a-5ceebbae7cf8 | -2.2203 | -49.206699 | 2024-11-24 00:25:00 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2a5f5b8-03a6-3910-b17e-e56f46fef82c | -3.5623 | -51.103298 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 731e0796-84eb-335a-a2a3-eeb806b55b10 | -4.6307 | -48.837299 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62dee258-92cf-32ba-ba06-54c7eed1657b | -3.0535 | -45.0746 | 2024-11-24 00:25:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38b97881-1790-3c05-b7df-24c38452f757 | -4.4887 | -48.1157 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d75c1a3-2258-3914-894d-e69aca8fdfb6 | -3.0913 | -54.536999 | 2024-11-24 00:25:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf6aab16-b1dd-3874-a20d-c4c8bed381f5 | -3.4891 | -49.901001 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d408b10-6acd-3fa8-a17e-6ead37223ccc | -5.1064 | -43.137199 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 104c5048-1d32-34d4-847a-d4aa5a5d1c59 | -3.9372 | -48.137901 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95c62091-aa8d-3f18-9337-2a086759c94c | -3.5916 | -49.3479 | 2024-11-24 00:25:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e71cdb43-5af2-3f3f-b51f-de83d5f23d51 | -5.1064 | -49.121201 | 2024-11-24 00:25:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 072cb277-be05-3e69-b693-d2d0ad0ea565 | -2.6248 | -46.216702 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 703adf14-fedd-304e-9837-61f70e4990d8 | -2.5885 | -46.057499 | 2024-11-24 00:25:00 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bdaa3a35-a118-386f-9369-a93c760948b0 | -2.6805 | -45.648899 | 2024-11-24 00:25:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46544f5c-fff6-3f68-a4b6-d20b77f03bfe | -1.6058 | -54.402901 | 2024-11-24 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a2af7be-3b9d-3f9b-a1d9-aadd4b8090ee | -3.5985 | -47.506901 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85203cb4-761f-3306-81e9-b59bf5a3f183 | -1.7762 | -53.604301 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a49ecc5-6199-31b6-8047-2490cb1772c4 | -2.7984 | -46.797901 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a74f9225-6d7b-3a3a-87cc-7f5c50994d34 | -4.5397 | -42.9156 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86135cf4-8832-3d75-ab80-8280706af4c6 | -1.3501 | -46.908401 | 2024-11-24 00:25:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa82e85d-c362-3759-895c-4c3ba1cbe828 | -3.2948 | -49.907101 | 2024-11-24 00:25:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70817a98-2914-3156-966c-2ccdc9903ec6 | -3.1585 | -45.532101 | 2024-11-24 00:25:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ecd2625-5c7b-31a6-bbc1-7703bbd1261c | -3.9387 | -48.144699 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 878affd5-ec7b-3b6a-8cbb-1db1b1c1a657 | -2.3191 | -51.2966 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f070e3-3e18-31e7-8255-4348a1eb20ad | -1.2434 | -51.732601 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81059e94-2cec-377e-850f-475e80b30fc4 | -3.4733 | -47.682098 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8485690-4711-31eb-87b0-ac6bb05d117a | -5.9473 | -48.049 | 2024-11-24 00:25:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9498f0a-d099-3a20-ac48-c2bc34d0c011 | -3.2683 | -53.806999 | 2024-11-24 00:25:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9503090b-a0f4-3c83-8704-e9c91e505f33 | -0.981 | -51.710201 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ad4188bb-d3bd-3425-958c-cc35b24d4996 | -0.923 | -51.635502 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 165bf44b-5088-36b3-8512-7bfb6afbb2c3 | -4.6587 | -46.052399 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bcc7dd4d-a5ac-36f7-8321-1ea68a230984 | -1.4781 | -52.502499 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ba47c40-4d2a-3617-9a90-cb2a3c89c8c8 | -5.0966 | -43.1395 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26d152e2-0a18-3ebe-b73e-56f6c1e9dd1c | -2.8098 | -54.005798 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6ab6889-6af5-3fa3-8fd4-059ef593daa0 | -4.0041 | -45.670101 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f8016f9-ad42-3176-a4cd-1240638ac3a0 | -4.3131 | -48.068401 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e949cbb-805a-3532-9510-8f228e5a785a | -2.8591 | -53.950699 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 379cac91-3cce-3613-bfb6-83e3449b7de7 | -2.6194 | -46.193001 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c939bf07-11b6-3a79-96e2-5f12ff2ae4c8 | -4.2164 | -50.391102 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c388f18c-9c0d-371a-8262-0ff04a6c048e | -1.1961 | -51.750999 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 847f0c68-0191-3925-b161-ef23cc9a35ab | -2.582 | -51.874199 | 2024-11-24 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 870620b9-c048-3b6b-9a2f-74c25c7dd1c9 | -0.2858 | -51.595299 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ed8495f8-ad0b-376a-9078-4ded73f796de | -1.2584 | -51.753399 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 219fdfed-2154-397e-a8a1-947829976428 | -1.2854 | -54.529999 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1a368d1-cbd8-3526-911b-9b716b449fb2 | -2.6712 | -46.239498 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b640868f-985d-3599-b129-542b6e76567f | -3.9104 | -50.588501 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0d3ed43-b743-37ec-979e-c3b662ea5131 | -2.5946 | -45.5886 | 2024-11-24 00:25:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb963c66-b610-3049-9c77-7069e021394e | -0.7503 | -51.737202 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 23404d72-1b73-3c4e-879a-f366fbf45760 | -1.1123 | -53.3927 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1633950-89c2-30a5-86e5-c468279ed9ff | -2.4004 | -49.045399 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 681bff03-0aeb-3df8-abb6-748db96f717c | -2.7077 | -46.264301 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cb56700-e8f4-30a6-a3c2-8592eb425c41 | -2.4405 | -49.086498 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0195a69d-a7e6-327c-bee8-597d36fc0f9b | -4.0814 | -46.142601 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11613ea6-1020-35fa-bd00-5479bd40cb83 | 0.4191 | -50.8447 | 2024-11-24 00:25:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5735b651-3a55-3864-9f62-5cd39fa50718 | -2.0782 | -50.314999 | 2024-11-24 00:25:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eadd1bb7-df83-360c-a341-a60f75c8a680 | -2.701 | -46.099602 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b76cfcd-8113-34be-aa56-75c923301863 | -3.5698 | -41.936798 | 2024-11-24 00:25:00 | METOP-B | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f081341a-a095-3a59-8531-4a255245a011 | -2.6729 | -46.247299 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 013df479-f1de-3853-8d6a-2a3b6c1b74e1 | -2.6843 | -46.1618 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d3a135f-d7ef-3f38-ba4c-88e7132be7f2 | -4.2438 | -48.629299 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a43a02b6-bcfe-3dc7-99b0-fd3266d7b411 | -1.2676 | -47.863499 | 2024-11-24 00:25:00 | METOP-B | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a56f3548-4740-3873-9467-4deb85fefe81 | -1.9502 | -49.516899 | 2024-11-24 00:25:00 | METOP-B | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1ea2341-4db5-331c-845a-851f7d134923 | -2.8687 | -45.841202 | 2024-11-24 00:25:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50ad84c6-d341-30eb-aa0b-2be4a1861674 | -2.6992 | -46.091599 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a9fd8ef1-681a-3a6e-8e4a-ae5cf485826c | 0.0141 | -51.178902 | 2024-11-24 00:25:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 11f96c44-32a0-3063-b687-29d7c72ecb39 | -2.6691 | -46.140202 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5640ff11-f575-3380-96dd-d14b67c7923c | -1.7312 | -52.7141 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f1dc16d-a750-3123-b26d-92adadfadfa0 | -1.2758 | -47.854198 | 2024-11-24 00:25:00 | METOP-B | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d036bf5-633d-37bc-8e31-3a19ae6052d8 | -1.2336 | -51.734798 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6c069ff-fa27-33d9-ac3e-750c3478fb9d | -0.9362 | -51.648399 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0666ad93-6b74-399f-b1a1-db980bf51484 | -3.2378 | -47.461498 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ece869a-e8c5-3603-b0c9-950b84b698ea | -4.3703 | -49.7435 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6b52cc0-c543-32a0-9a70-c0480f125fbc | -3.3947 | -50.307201 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7357db9-9e72-397d-b694-21eab0f900be | -4.4006 | -49.648602 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d357843-0a42-3ebb-938e-a99c8f4ca11f | -1.1417 | -53.3862 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4912f483-2216-3a26-9249-26a8afe7cb04 | -3.4408 | -50.007301 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91501d4b-c419-3619-acc3-a64d61e5c59a | -2.5681 | -46.555901 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f57dd4a-443f-35a8-aafa-a2b2b3a35421 | -1.7292 | -52.705502 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70f30c4c-3fed-3022-b628-25bc5e7f2475 | -2.958 | -45.152199 | 2024-11-24 00:25:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 328fa74b-1e6f-335b-9c4c-8574ce1efd05 | -1.5257 | -51.614201 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ae390a5-b524-38ce-b924-05cd46e93615 | -2.2501 | -46.834099 | 2024-11-24 00:25:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4daa357-2679-34e1-96bd-54ee26a2bdfd | -2.5749 | -45.637402 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d73b471d-3f92-30fd-86cd-cfe80c660f7a | -1.7331 | -52.722801 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc5f4d68-a69d-35d2-afce-2d9816484ea9 | -0.8772 | -52.758301 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cda100de-5651-3d1e-906a-5848b752f89a | -4.5273 | -46.4245 | 2024-11-24 00:25:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e7c94e1b-8171-316d-a923-3254c5eadae6 | -5.1942 | -49.145199 | 2024-11-24 00:25:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90dfa8b1-2324-3018-85e1-25a645eb4dcb | -3.9425 | -45.985802 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c66df74-4916-3dc0-8245-572dad4299ce | -1.9615 | -49.521599 | 2024-11-24 00:25:00 | METOP-B | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f23ef2ce-172e-3aef-b802-49225d2b38e5 | -1.5159 | -51.616402 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89da1cf6-9867-3199-8c66-760699733ae4 | -3.1763 | -45.295399 | 2024-11-24 00:25:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b48fe49-b576-3ef4-a6f6-e0e9c6ea3c70 | -2.5903 | -46.065601 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2696e713-580a-3c68-b0c2-ecebf8ac28c2 | -1.7316 | -52.027302 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
