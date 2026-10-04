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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad993492-2427-33c8-b5a8-2614d545789a | -9.48167 | -64.68994 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 513901c2-ffda-332e-bf04-478336f7b8e2 | -8.05487 | -72.43682 | 2026-10-04 06:40:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cdeb87a-4eba-3d2f-84f6-2d125131a3b4 | -8.88341 | -66.88943 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1939dbb5-977d-3aaa-aa6f-a327ba7bdcc8 | -9.05178 | -65.43003 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64bba97d-fa0f-3d86-9206-66514f87c215 | -8.35053 | -62.83279 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9461740-0bf6-35c9-8c5a-ac80991c1168 | -8.57774 | -66.82023 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb8b4c41-4f4a-38cc-a60d-4b81924bb32b | -9.01119 | -65.69271 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1ace3e3-6d56-3437-86d9-d3610f9507e2 | -8.57207 | -66.81937 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d3e4780-e367-3a29-ab95-1c1abf87bed7 | 1.9154 | -55.76028 | 2026-10-04 07:01:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 50370834-ea73-3ca8-88d0-f7da25555ce3 | 1.91247 | -55.74069 | 2026-10-04 07:01:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 5c30d2ba-a19b-35e4-ac85-4e20f1c4eb03 | -1.09995 | -54.11193 | 2026-10-04 07:01:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| d1eb3ab8-5ff2-3bbd-85a5-e9fdf658b9aa | 1.75425 | -55.63364 | 2026-10-04 07:01:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3fc7476d-e39f-3e7a-8699-fbcdc2005538 | 1.76678 | -55.63181 | 2026-10-04 07:01:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a16c93f5-e470-3a23-bbf2-b2e72ac4277c | 1.89979 | -55.74255 | 2026-10-04 07:01:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 1e2e4411-f60c-375f-a16e-8348346e2617 | -1.08942 | -54.11039 | 2026-10-04 07:01:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7eb4fe7b-282a-3493-9c46-04c56fe30a8d | 1.90268 | -55.76208 | 2026-10-04 07:01:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 7d9736c7-e285-34f6-ba3b-55b6fb886a37 | -3.46201 | -50.09602 | 2026-10-04 07:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 78c5ff98-af52-30b7-9085-92dcfc7d60da | -3.16858 | -54.07888 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 787986e7-3454-3f5a-a434-c08710164829 | -3.13031 | -53.72153 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7ee6491b-f781-337a-a812-d15c18cf9084 | -3.18146 | -50.53481 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ed36f23c-9436-3b2e-9442-f94e39d05cb5 | -6.0787 | -53.47472 | 2026-10-04 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b6e02e42-7761-37f6-ba4b-7eef1c042ff9 | -3.07499 | -49.53807 | 2026-10-04 07:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 2c24763e-35f0-3664-bfbe-4af7a83cf710 | -2.59451 | -51.84756 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5449c415-31ad-3de7-9818-6d1bc9d4e81d | -3.12215 | -53.70869 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| f8b96182-5954-3b01-834a-61f5a1ae2726 | -4.81412 | -49.278 | 2026-10-04 07:03:00 | AQUA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3172bfba-bb63-32bc-a205-c892c85a3e49 | -2.24838 | -51.92986 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9457e9de-8dd7-384a-b06a-2a91a6536a50 | -3.06613 | -49.53677 | 2026-10-04 07:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9c8c791d-5353-3baa-828a-dab6e87b5eed | -2.21844 | -53.71087 | 2026-10-04 07:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bce313bd-e044-334d-8ee2-6d2e6e7ad372 | -3.04206 | -54.22747 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9c11d159-3256-3698-a23d-f77e455d4f27 | -4.2686 | -50.27007 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d1606584-d863-3245-aa28-d7f15ed62e88 | -6.06499 | -53.46595 | 2026-10-04 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 97c8a127-8cdb-3194-a809-089226ed8d7a | -3.84336 | -55.83554 | 2026-10-04 07:03:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b25ad0d6-fd6c-3415-9472-f322ff61216e | -4.26352 | -46.37106 | 2026-10-04 07:03:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b35b67fc-083e-3de3-9189-c6b014a51437 | -3.04395 | -54.2152 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5dc38a25-2fe6-3167-91cf-ad1557cf36e3 | -2.58412 | -51.85543 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 1ec12470-63c0-3172-9a4e-d5107b8a4f01 | -2.81142 | -54.1359 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8bc4930f-e0f6-3b02-a323-7310abc32cbf | -4.05818 | -54.30055 | 2026-10-04 07:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f8a082e0-6f7e-3dd5-b245-2f809a4d738c | -4.20756 | -53.45999 | 2026-10-04 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 87a42720-3f37-3f95-aedc-aa499780b524 | -3.00526 | -53.87249 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 752ebd72-7cf4-391a-9aca-b928ba3c753c | -2.6874 | -49.03448 | 2026-10-04 07:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f03e5c1d-e83b-3769-ac9e-9d2c9a6db631 | -3.00759 | -50.46126 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c88a418b-21d7-3640-a84f-cfa0146b7ec6 | -4.82565 | -49.87601 | 2026-10-04 07:03:00 | AQUA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 58bb4695-d4d0-3504-9a8f-ac3876fee68d | -3.69859 | -50.66623 | 2026-10-04 07:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 3b292832-93a9-3deb-ad8e-18d9dfd473cf | -3.83932 | -55.84192 | 2026-10-04 07:03:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7fb27ce9-04fa-36cf-bafc-fea97d3f56a9 | -2.94632 | -54.11897 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 995e6cc1-f56f-3c18-97f1-45710213f6ed | -3.1204 | -53.72003 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| aff9b1aa-c67f-3c20-8b78-64d553c71721 | -4.29626 | -50.26516 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bfea61f6-6329-3e5c-9bb8-1cb8a2794ef7 | -3.13848 | -53.73441 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dfc7c3f1-0584-31bb-b7e0-389e6d7e1e57 | -4.45654 | -50.97712 | 2026-10-04 07:03:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8ad34d93-3eee-34d2-987e-078752589c1d | -2.59311 | -51.8568 | 2026-10-04 07:03:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99dba6db-60a8-3da4-88aa-4241bcf7d007 | -2.81973 | -54.13148 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| c029e4e0-9af0-352c-b4b0-7d5c888cd613 | -2.84636 | -51.28764 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 82cf1fc7-e84a-328c-a863-9aa2e8371715 | -2.90359 | -54.1316 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 37b9cf7a-7207-3313-8e3d-69e3a6df46bd | -4.26992 | -50.26129 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| aaf60f58-a858-3d4b-8555-b62f08c5bd47 | -4.11517 | -49.06939 | 2026-10-04 07:03:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4a9aa8bf-4703-3468-a49c-2e87f76e7732 | -2.80303 | -54.12207 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 13299a4e-9bed-32c9-855b-0a1aecd4f680 | -2.80859 | -54.08559 | 2026-10-04 07:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fcbb7cf9-6fe5-37c6-985c-12c7d604d530 | -3.46333 | -50.08723 | 2026-10-04 07:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 80415cd0-429a-33fa-8d82-20358057ce1c | -4.2787 | -50.26258 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 156.2 |
| fe56772b-2211-3a11-a3e4-762e5e7ffc8f | -4.81676 | -49.87479 | 2026-10-04 07:03:00 | AQUA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3ee77614-0fb7-38d2-b709-2c5ad8bb2ba0 | -2.82352 | -54.12521 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 486bf069-c6ee-314e-8271-d1951a6af19f | -6.06344 | -53.47599 | 2026-10-04 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eb47c087-c86a-316c-8c1c-94f5f138bcc1 | -2.80489 | -54.10989 | 2026-10-04 07:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| ff16eb90-6567-30e3-bdaa-3d5ccb230e40 | -2.81328 | -54.12364 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| c6f278f1-1938-3003-9bbf-725c9d5e3efd | -3.46946 | -50.10607 | 2026-10-04 07:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 29518a6f-4586-3790-8141-7f825bbd006c | -5.9993 | -53.51788 | 2026-10-04 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| e2e71b40-4043-3343-bdf4-9e1ccec54746 | -4.29362 | -50.28271 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 49cf9c19-5422-3437-aa84-e37720ef1056 | -3.70866 | -50.65882 | 2026-10-04 07:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3e0315f5-080d-3485-b305-53d3371d6698 | -2.82536 | -54.11301 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| beafcc50-e6bb-3c4b-8086-041013f2d8a3 | -3.11225 | -53.70721 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2affd6dd-a6a0-3b95-a415-5c1ce9f6ca60 | -6.06932 | -53.47335 | 2026-10-04 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 922f0bee-a477-32ac-bbb7-3b3f5ed8b9b5 | -2.81697 | -54.09927 | 2026-10-04 07:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8f73523b-b6f1-3d35-b04a-a2c1c690dbf9 | -5.9977 | -53.52808 | 2026-10-04 07:03:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3e0d8058-f255-3f99-a93c-a97c817fb797 | -2.69775 | -49.02661 | 2026-10-04 07:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d1f63624-f802-36f8-8e58-a416fa170833 | -4.82701 | -49.86699 | 2026-10-04 07:03:00 | AQUA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a386704f-b999-3bd1-91bd-79d035891b44 | -2.69638 | -49.03579 | 2026-10-04 07:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 347942f8-568e-38ed-85ef-3e6f8bb121a7 | -3.18705 | -54.09409 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 5ee1d1ce-5c4c-38b5-b0b3-68f6b1a0df16 | -4.28748 | -50.26387 | 2026-10-04 07:03:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 187.2 |
| fe8ff121-efcf-39e6-83e7-0b921c9dd5d2 | -2.97051 | -54.09781 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7843b7ac-89f7-38f7-8a56-961de0099722 | -2.69119 | -54.64018 | 2026-10-04 07:03:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 786fdbc9-3a81-3754-bf2e-6a38cde3db58 | -3.17872 | -54.08054 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 6add71f2-6a1d-3d98-8336-5e3302019b51 | -3.07365 | -49.547 | 2026-10-04 07:03:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 16bc9b2e-f41b-3340-89ad-6b1ac3b49ef4 | -2.81512 | -54.11145 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 61d03791-5739-3453-89cc-cf6ea4535533 | -3.12856 | -53.73289 | 2026-10-04 07:03:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 99fec13e-adc8-37d9-8de4-d0ed57009d30 | -2.79465 | -54.10836 | 2026-10-04 07:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| cfa0b13f-2ad8-38f1-b614-64551c04629a | -3.50531 | -54.60614 | 2026-10-04 07:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 2b4a90d0-9a91-3aca-b7d2-472a94befb15 | -2.80674 | -54.09774 | 2026-10-04 07:03:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| e169b7d0-db89-3c91-a346-296f152033f4 | -2.5723 | -51.87257 | 2026-10-04 07:03:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8c1bc475-71c0-31b5-a351-e1ac45e4017c | -2.74957 | -51.55095 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1a805349-00fe-3604-9593-b53aa540d07b | -1.87482 | -50.61135 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d95c0941-d01b-309c-a9e6-ce74425ed932 | -2.98427 | -51.04414 | 2026-10-04 07:03:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3cbb6153-f27e-376c-838a-1dd1aa103bd5 | -3.47078 | -50.09731 | 2026-10-04 07:03:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 33cd3173-c17f-3a50-acb5-f96b50106dfc | -6.2126 | -52.79867 | 2026-10-04 07:03:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ab7952ce-6eac-384e-95d0-d413eac54210 | -3.86735 | -55.81424 | 2026-10-04 07:03:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| a6a33335-0d55-38ef-9274-a23df6a00de1 | -3.89191 | -49.69562 | 2026-10-04 07:03:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ff588e71-1b50-31dc-85c6-7fd4792d1d0b | -4.81813 | -49.86573 | 2026-10-04 07:03:00 | AQUA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 307cbd29-3e23-36ef-9cc7-1f82671566c2 | -2.93039 | -54.15387 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b6ff036d-c807-3ef9-b395-5c8d0611da46 | -4.05627 | -54.31292 | 2026-10-04 07:03:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 423ce2da-a827-304e-ae2c-22cedde4d86e | -1.61736 | -55.01303 | 2026-10-04 07:03:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 6b4184a9-ef31-30b3-8f8a-e43465c3201a | -2.97237 | -54.08574 | 2026-10-04 07:03:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |


[Clique aqui para ver as próximas entradas](README72.md)
