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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a02e865e-5504-3126-b983-d748d18029d7 | -2.97384 | -54.10223 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d249d87-6f87-3a24-b99c-4bd9f9924e58 | -7.50344 | -54.98123 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b261cc9e-687f-330a-9b4a-f61138fb7360 | -3.21823 | -53.4115 | 2026-10-05 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fe6504f-e175-3ecd-9098-5f39bda6b8a3 | -5.98198 | -55.38243 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04887bd5-e789-3dc0-a4fa-5544cef21aee | -3.06519 | -54.16621 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| da822f8b-21c5-3411-a629-8c2ffb25de40 | -2.58339 | -51.87179 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20f9dacc-effd-3d70-9cb8-fd9eb51a57a7 | -3.07552 | -54.16789 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 5da5381a-c3c7-379f-b976-cb0c141f806e | -6.89379 | -43.68582 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d1a9ca81-a847-35b8-90d5-ea26dfa13a79 | -3.20121 | -53.951 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0a1fed3-8be5-36e5-a756-7f33ab881161 | -3.07374 | -54.17912 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 00b35454-2d23-3d73-8627-aa2895d2b6fc | -3.1182 | -53.72373 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b51a7e29-3da3-3d20-a0d4-3d0ecfd40f61 | -2.93779 | -54.08496 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e846adc-3df7-3179-9d10-c60808c06320 | -2.9902 | -54.04351 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f07bea9-ccf9-340a-aaa6-ce1a99c2a4eb | -5.23134 | -48.40376 | 2026-10-05 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e494973f-4a21-36a9-9089-b2eb87515256 | -8.66814 | -54.5657 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e3ec5009-57e7-3142-a543-9682ddbc4831 | -6.05838 | -53.48243 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b533568-3ea9-3006-9c30-08b4bf699b25 | -3.84559 | -55.84161 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a6c91f2-98f5-34f6-b0b3-6f2158f4b600 | -2.90646 | -54.12611 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8920c178-95d0-336f-aa25-215448cc487f | -2.80791 | -54.08435 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 255149e8-203e-3eaf-970b-8786e3c7fd8c | -4.03937 | -48.99398 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce6f94e4-6711-38f8-8886-5ec828c4681c | -3.87642 | -55.81527 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b13178c-270d-3ea1-aac4-ae394743469d | -2.84755 | -53.99107 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ab67882-8807-3386-98b4-c247ce754090 | -3.46093 | -54.59823 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 40ad0ac6-8050-3bb6-a21d-abfa5eed56b3 | -4.14522 | -53.94753 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3acc87d1-4c26-33b3-895d-b62a08b3373f | -2.98416 | -54.10387 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 9bb1f6bf-6580-3b11-bd1a-02c0ba9569cf | -2.94944 | -54.14458 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 20a86dbe-b763-308b-baab-94d402c3096b | -6.26335 | -52.85681 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1eee5c1b-8c57-3bd5-8693-7b9abd07598a | -3.90758 | -49.71401 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebca49f7-17ef-32db-8ce4-408a9237dbfc | -4.4663 | -54.96342 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77d72484-8384-3ce3-99ee-05534fc48329 | -5.99937 | -53.51214 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f2107ba-b98c-3d0b-aa81-b7d0bee25603 | -6.21885 | -52.68743 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 042bcfdf-3894-3e44-bf33-4dcb9f6f23ec | -3.30894 | -53.8471 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e6f6fcf-71b9-31b3-a269-17ed6c26d4b2 | -2.88768 | -54.09319 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04109aa3-3f41-3156-8b8c-a896aa2a26e7 | -3.84297 | -50.31696 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1191f27c-7f08-3bbb-823e-ad289741adb4 | -2.78988 | -54.10846 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8fc587a-6f68-379f-92ba-c94bd8852282 | -6.87911 | -43.67318 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 10080436-008a-3e65-a1e7-f27c7c19f032 | -3.71344 | -50.65221 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ede87ad8-e945-34c4-ad60-0bd2c92c0e2b | -3.21411 | -53.87002 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0da43fe6-a5ea-3fb9-bbd3-9a537e7d679d | -6.21567 | -52.79314 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f691716-ac0e-3965-8d4a-ab0391f55ad8 | -3.12374 | -53.75448 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ea2ff5c-d6c3-35e3-bf24-b78993291f6a | -2.88722 | -54.09229 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c4be9e9-47e3-3984-ac54-4d8dedab4209 | -2.48346 | -56.10899 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e591a71d-6049-3043-a63a-206c19ccb96b | -2.99949 | -54.17901 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0848503d-bd15-3147-bf3c-d9c8c50cee76 | -3.27997 | -50.01908 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0486fd3d-15e3-3ba8-83b7-c3a8175a1fec | -6.00935 | -53.51371 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 32c3877f-ceba-3da8-9ceb-ea36f408eb2c | -2.58284 | -51.87522 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16dc60f9-d4dc-3990-a479-5e8b495af1e7 | -3.11074 | -53.74868 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30d80992-aa8e-371a-91ce-a855e8e487ed | -3.5201 | -54.63148 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9f6d632e-c850-3f7a-971e-63508f686a27 | -2.93807 | -54.12732 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cddd6baf-e0f0-3d1f-9315-3847ee88901b | -2.98131 | -54.09958 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 411b75ed-2513-34b8-9821-6f5c02f7bb7f | -2.44772 | -50.25464 | 2026-10-05 04:57:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a4e4559-976d-3d61-8a7f-134a1e2eb053 | -3.71339 | -54.21272 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f9e622a-34e7-3af3-b538-2865923b3d26 | -6.17392 | -52.92812 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8ff59b3-50e3-3e01-be96-f1d37aaa97d6 | -3.46157 | -54.59434 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| a729a9b7-c740-33cf-9ace-a02a42f6b955 | -2.22796 | -51.88591 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e65fcc2d-4113-3dba-a224-fab19282aad8 | -3.28083 | -54.17696 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9b81d86a-736e-3c64-9b3b-557f0be6efe3 | -3.00376 | -54.21833 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb0d5855-d5da-30c5-99d2-1ddcdb53479b | -2.949 | -54.12524 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca0fa5bf-d54c-3698-8cd8-e31c5bd34967 | -3.12044 | -53.73155 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ce3dced-27c9-3942-a4c9-0acb3d18cfb7 | -1.55255 | -54.79982 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e42f34d-afcc-3d31-b88a-46a726b37df6 | -2.80712 | -54.11118 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a85ce3ef-b801-3d66-8fa6-3643e583b722 | -6.89472 | -43.67912 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1723771-0271-3f59-8d40-742c0d71c8ca | -3.91574 | -49.70754 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d461ff19-c789-3309-af3a-dce563d33744 | -3.10638 | -53.71068 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5ea5f6b2-4d89-35d0-94e7-d22b378429d5 | -1.74138 | -55.2354 | 2026-10-05 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2d1b4da-6ac6-3b94-a013-634aea8a5d7d | -3.05439 | -54.23405 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9ae2fe5-e712-3155-88e0-cc3d12e5b794 | -5.99202 | -53.64398 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dd40ff7-a423-33a1-8d72-f2f4d402bb75 | -2.68902 | -54.64153 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e93e4714-1cc0-3aa0-bd92-c6b026c94ffb | -2.47049 | -48.03725 | 2026-10-05 04:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23af7eae-9525-3ac5-84f7-c58f84dfd361 | -7.71871 | -45.45779 | 2026-10-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa232afc-ee80-3e86-ade8-afc85ac33a40 | -3.05485 | -54.16455 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f87537ad-805e-32e0-b192-091ed6c080e5 | -3.04298 | -54.21674 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee8f302c-ff9d-3351-9fb0-8a99bc15ebcd | -6.42793 | -43.72444 | 2026-10-05 04:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9db0e3b-847b-37d2-bc23-71e33b27753f | -3.22774 | -53.87215 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a86747d2-ad11-3acf-a57c-85c4f4c390c1 | -4.45803 | -54.97005 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fee4e9a-5bdc-3a7e-80fb-eeaf4d886589 | -3.10463 | -53.72158 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f86cf4a8-492c-357d-bf99-d2da7a7cf82a | -6.24846 | -52.84383 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce2dc190-ae97-3c17-9d10-141933262f26 | -3.92773 | -56.17012 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5af7cf79-20e4-3c0d-8287-905adde485c1 | -6.2135 | -52.82821 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce1914f4-3f5e-3f35-bd9e-4f2f67f3a58e | -3.11258 | -53.71538 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d37f5a1c-68ab-3190-a6ed-b2abf9e2424f | -7.19281 | -44.31164 | 2026-10-05 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36830b7f-e179-31d3-8295-fc6a80429c46 | -3.12838 | -53.72535 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d4a844b-9e89-33ae-9f4b-f5da0868b21c | -2.5737 | -56.14963 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f7037b0-8f61-3281-b99a-78417398b3a1 | -3.09997 | -53.75072 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2a453c41-a356-3f38-a99a-4dc3754d71e6 | -5.96473 | -55.3553 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5f8d3a8-d13d-38bf-a9b1-2b220344570d | -3.84858 | -55.8466 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8be577c-967f-3ac9-927e-2120f602f050 | -6.12713 | -53.05182 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 206585d2-d3c7-385a-8826-def939237445 | -3.10008 | -53.72832 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 36aee095-92d3-3809-b8ab-519ca89813e6 | -3.12168 | -53.70192 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1f23a70-68b9-3bd5-ae60-c030505e1094 | -3.51722 | -54.62705 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 538d5016-895f-3a5a-b00c-ae908764ce81 | -3.01771 | -53.89207 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd6f467a-7c5a-3799-88f7-3a415a849fcd | -8.52845 | -54.58728 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75934e66-c8f1-3de8-8ec2-c0a386cbbcff | -3.46918 | -54.59163 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 9e95a3d8-a79c-3016-9108-8ba1060f0ff6 | -3.07778 | -54.17591 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| f0a2422c-7c11-3aab-9753-aca457bf0a2b | -2.94388 | -54.20164 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce897083-0c17-3afc-80ea-ece1fc0cf542 | -2.90423 | -54.11805 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98977f9c-36f1-301c-ad40-f58c9b733d5d | -2.22014 | -53.70456 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7df9815-ff46-3c33-b293-f26ad8bf6c65 | -2.80367 | -54.11063 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb976a39-01cd-3181-be01-71d2b913ac6d | -1.20157 | -55.86107 | 2026-10-05 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9844eb52-7a04-3df8-a369-4fe2bcc304e8 | -6.00602 | -53.51316 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README39.md)
