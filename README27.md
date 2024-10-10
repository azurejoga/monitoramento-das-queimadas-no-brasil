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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb9cb967-5a34-3260-8274-fb164ce27d81 | -2.8356 | -53.3027 | 2024-10-10 01:07:32 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1c95dc5-2660-3600-9a4d-534ef36cbcf6 | -2.8377 | -53.311699 | 2024-10-10 01:07:32 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef80cd59-10fb-37ed-a04e-7fe9a7ba46c4 | -4.2665 | -59.866402 | 2024-10-10 01:07:33 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92d4b60b-eabf-34ee-aeda-697fb901e256 | -4.2683 | -59.8745 | 2024-10-10 01:07:33 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e04e476-8fe9-3afe-ade7-583fdd53d2aa | -4.2585 | -59.876598 | 2024-10-10 01:07:33 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ccf7990-8f4a-3d2a-8f8a-250c2a134022 | -4.2839 | -59.991501 | 2024-10-10 01:07:33 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34e30ce2-cc37-386d-bcdf-25a59000d90b | -4.2858 | -59.999699 | 2024-10-10 01:07:33 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68041b66-eb70-3310-a777-017506319871 | -4.249 | -59.973099 | 2024-10-10 01:07:34 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35daeaec-001a-3033-b43e-5196cfec97e9 | -4.2509 | -59.9814 | 2024-10-10 01:07:34 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0b53600-c304-3e6f-950f-f6bd0e8de420 | -4.2527 | -59.989601 | 2024-10-10 01:07:34 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00b99a2b-f1a3-36ad-9fab-3a6b64c917ef | -3.0663 | -54.760799 | 2024-10-10 01:07:34 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 482e7666-66c9-30fc-8afe-fd5805d9f08f | -4.208 | -59.9734 | 2024-10-10 01:07:34 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1911ac2c-6e6a-342e-b802-15ad5309576c | -4.2098 | -59.981701 | 2024-10-10 01:07:34 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d01bb28c-12c2-3d62-adb3-72c871e03107 | -2.6749 | -53.320301 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93c2b305-fab8-3d7f-aafd-b15bbd215d6e | -2.677 | -53.3293 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be507457-cd0c-3348-8793-acf203bcf9e6 | -2.679 | -53.3382 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5991c2d-3067-3380-8d55-cfc674bbcd04 | -2.6811 | -53.347198 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32521921-a8a8-34fd-a22c-baba4ebc0215 | -2.6651 | -53.322498 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f26233bd-09ae-3c18-b3db-329f7051ea72 | -2.6672 | -53.331501 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85b2ae09-4925-3d9d-a006-aee0318388a3 | -2.6692 | -53.340401 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b94b8e7-9313-3951-ab40-6954517b8a4e | -2.6713 | -53.3494 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40a44991-58c4-3ace-8654-1b19523386e7 | -4.1561 | -59.924599 | 2024-10-10 01:07:35 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8877b0fd-71c0-3660-a7c6-8fda10716bb5 | -2.6553 | -53.324699 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c966d5c8-3591-3af2-b344-7e364fe8bd3c | -2.6574 | -53.333698 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99e8c72d-8e41-3f6e-a343-a813fcd8404d | -2.6594 | -53.342602 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7a4d8f8-524d-3961-87b9-a31d660cd47f | -2.6615 | -53.351601 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa91252-a911-3b13-99f9-e84369671e8e | -3.8927 | -58.786598 | 2024-10-10 01:07:35 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef6e6655-903d-309e-9a51-30a50565e53e | -2.6476 | -53.335899 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e98802bc-6947-3911-adfc-d986f76a2ea1 | -2.6496 | -53.344799 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bfba651-945c-3581-b755-ecf21e1e6c75 | -2.6517 | -53.353802 | 2024-10-10 01:07:35 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 900b7792-59c2-3c7a-bc69-2b34fb58b58c | -3.9559 | -59.162498 | 2024-10-10 01:07:36 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0137f5e8-7d8e-315f-8cf1-9730a0f6d3fa | -2.8783 | -54.4786 | 2024-10-10 01:07:36 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0906c727-23d7-30ec-9b43-8e5631802ee2 | -3.142 | -57.048199 | 2024-10-10 01:07:41 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 642b959d-5241-3f10-a236-a2abd537275a | -3.6302 | -60.194698 | 2024-10-10 01:07:45 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3dfcc2eb-6dbf-32d4-90f2-581d353b6c36 | -2.1483 | -54.846401 | 2024-10-10 01:07:49 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 154fe0a7-bc82-30c4-a56f-c7bc76397c5d | -2.1367 | -54.8409 | 2024-10-10 01:07:49 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 134d893e-670c-36da-9608-da54960ae87b | -2.1385 | -54.848598 | 2024-10-10 01:07:49 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7601bede-6c68-369c-a54b-7462cfcafd04 | -2.1402 | -54.856201 | 2024-10-10 01:07:49 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52fef849-b973-35fb-b1af-1be083466f92 | -3.0132 | -59.0877 | 2024-10-10 01:07:51 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88d55240-84ed-3995-81ec-49ab9ce9a5a3 | -1.6484 | -53.331799 | 2024-10-10 01:07:52 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50cb4e55-b7cf-3818-9528-4205f13fdcea | -1.9205 | -54.5695 | 2024-10-10 01:07:52 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b57e0a34-4ac6-3a91-adbd-7cb685a60c13 | -1.5278 | -52.939499 | 2024-10-10 01:07:52 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b38d131-000d-3690-81e5-ed8a698377a8 | -1.7396 | -54.227501 | 2024-10-10 01:07:53 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a25f25b4-d0d4-3eb0-b75b-f2f0f127febb | -1.7414 | -54.235802 | 2024-10-10 01:07:53 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59420101-e10a-3d51-bf7d-4a612a919a0e | -1.7298 | -54.229698 | 2024-10-10 01:07:54 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e48432e6-396a-37ca-91a2-d88a17803133 | -1.7316 | -54.237999 | 2024-10-10 01:07:54 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09b4817f-e0a5-35a6-a99d-443bc46d431b | -1.7009 | -54.374001 | 2024-10-10 01:07:55 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3c80951-2ba9-3c7d-81c1-b2e15c1ea930 | -1.7027 | -54.382198 | 2024-10-10 01:07:55 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9fe2b0f-e02e-3f79-8cc4-6b4d2fd9d52c | -1.6911 | -54.376202 | 2024-10-10 01:07:55 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f18cd7b9-53d1-3763-ac71-94c54e04e7a3 | -1.7632 | -54.964802 | 2024-10-10 01:07:56 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bae8e38-edf2-38b1-bf30-191f08b85fe7 | -1.6698 | -55.097698 | 2024-10-10 01:07:58 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f72f38fc-4ff2-301d-878b-e488e6c717ab | -1.6166 | -54.908699 | 2024-10-10 01:07:58 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e87eb31-f272-3c59-b2fe-edd08f563919 | -3.0423 | -61.663399 | 2024-10-10 01:07:59 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e3af0f9-ab61-3ada-a2c3-5f974d043629 | -3.0444 | -61.673302 | 2024-10-10 01:07:59 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4db97e3a-f590-30f1-9274-5889758d9e37 | -3.0325 | -61.665501 | 2024-10-10 01:08:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35fadd82-3ea8-36a5-8f98-b7540dc3789a | -1.1157 | -53.432098 | 2024-10-10 01:08:01 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29565b6c-f289-3332-a277-1b99c8a2af81 | -1.1178 | -53.441299 | 2024-10-10 01:08:01 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a216fb-6c01-3d9e-aa2c-1be57e969da8 | -1.1508 | -53.7668 | 2024-10-10 01:08:01 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f65602de-3d30-36dd-85c9-c632136501ba | -1.1022 | -53.598701 | 2024-10-10 01:08:01 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24cef999-ef83-38ec-8f0a-292c51f8f138 | -1.1043 | -53.6078 | 2024-10-10 01:08:01 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7dc7947-19b5-36f3-8f0d-98e7a82e3210 | -1.2256 | -54.1408 | 2024-10-10 01:08:01 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9a51dfb-4ac5-3b14-83e7-ba0139e40ead | -1.2275 | -54.1493 | 2024-10-10 01:08:01 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae7c6f21-991b-311a-a306-43855aa4e71e | -1.5136 | -55.408001 | 2024-10-10 01:08:01 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af7523cd-3937-312f-85a9-03df637998be | -1.1827 | -54.088001 | 2024-10-10 01:08:02 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e119385c-8a8f-3c44-8a5c-f13f98ced4a0 | -1.1847 | -54.0965 | 2024-10-10 01:08:02 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55df194f-42c3-38cc-9e1a-a8ac3e236470 | -1.2447 | -55.676201 | 2024-10-10 01:08:07 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4197a980-f77f-3bc1-b4e9-d650eefcde2a | -1.2464 | -55.683498 | 2024-10-10 01:08:07 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 878cd97e-7202-3ade-a9ec-4e25da051264 | -1.248 | -55.6908 | 2024-10-10 01:08:07 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e592a290-6a9a-344c-92f5-3eb916df870e | -1.2497 | -55.698101 | 2024-10-10 01:08:07 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 642f8d99-0bb1-34a4-948e-4dd6d3364dcc | -1.2349 | -55.678398 | 2024-10-10 01:08:07 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5b0c74c-3058-3660-be06-896181952dc9 | -1.2382 | -55.693001 | 2024-10-10 01:08:07 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e60128d-478c-3416-9a46-c4232278167f | -0.3744 | -52.027699 | 2024-10-10 01:08:07 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f55cabb2-6530-30f9-ae2e-458baeb485c4 | -0.3646 | -52.0299 | 2024-10-10 01:08:08 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6533792c-7428-3317-a9ee-96110d47d3f2 | -1.5114 | -61.5672 | 2024-10-10 01:08:24 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed859f4-c1c6-3644-a0e9-41ba7698f1d6 | -1.5135 | -61.5765 | 2024-10-10 01:08:24 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fac1015b-390c-36d0-8771-d0b15f3e6a6d | -1.5037 | -61.578701 | 2024-10-10 01:08:24 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d3ed6d3-bf0d-3ce9-88e4-6dfa783d5564 | -1.4841 | -61.583 | 2024-10-10 01:08:24 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f67e1ea-9a09-33cc-b2c8-a0c0b4c0bbae | -1.482 | -61.5737 | 2024-10-10 01:08:24 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 347dfa84-1784-3b64-bad6-5b8609cb7357 | -2.6533 | -53.3506 | 2024-10-10 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| f6783384-9e05-32f2-90ad-f4b1f01117de | -2.6716 | -53.3704 | 2024-10-10 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e130c237-126d-331a-b9fc-6252a373e622 | -2.6716 | -53.3502 | 2024-10-10 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 424.3 |
| c3decedf-bd15-385d-bb12-baf96e8a7f1b | -2.6717 | -53.3299 | 2024-10-10 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 198.6 |
| 1aea2900-5f65-3a83-b4d6-63e22894832c | -2.69 | -53.3497 | 2024-10-10 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 1e0c6202-ef68-369f-a2c0-dba5fe3d2c72 | -2.6901 | -53.3295 | 2024-10-10 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 4a5e5439-7aa1-358d-8645-4d432e584e5d | -3.3341 | -53.232 | 2024-10-10 01:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 716156b6-d1b4-3d8a-b7e0-179249b55091 | -3.3342 | -53.2117 | 2024-10-10 01:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c6d0d938-09b5-31f0-8571-b8c50ebb032f | -3.6746 | -51.1274 | 2024-10-10 01:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 8863c076-4e36-3db5-9c50-7a692f9dae47 | -3.6747 | -51.1066 | 2024-10-10 01:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| d20600ad-8783-3961-b3ab-07514bd889af | -3.6931 | -51.1268 | 2024-10-10 01:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 356ba6cc-b1ec-315d-86a7-b106cf51cfe6 | -3.6932 | -51.106 | 2024-10-10 01:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 7b0bd033-4043-361f-be6e-55aa215c8955 | -3.7247 | -44.9547 | 2024-10-10 01:15:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b20921ba-0af9-3926-a6f2-40f1c4be8125 | -3.7961 | -45.4927 | 2024-10-10 01:15:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 410fc7eb-2df0-3d70-9329-190c7c94f94d | -3.8146 | -45.5143 | 2024-10-10 01:15:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 20a97876-b0db-35ba-9cab-b1cde0167a98 | -3.8147 | -45.4918 | 2024-10-10 01:15:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c9fa5d8c-fef6-3b03-bd65-547f5fa8edc3 | -4.0814 | -51.0292 | 2024-10-10 01:15:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b09286dc-88af-3b78-85c5-12dd5bbe86a6 | -4.0961 | -48.2739 | 2024-10-10 01:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 9aa07c60-98cd-3628-828f-daf070c9f6ed | -4.0962 | -48.2523 | 2024-10-10 01:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| ba6036b5-fad3-35c8-a2c0-81a65fd8ebcb | -4.0998 | -51.0285 | 2024-10-10 01:15:30 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| cc667fef-fd92-3802-be31-fc9945ef5e45 | -4.1146 | -48.2731 | 2024-10-10 01:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 197.8 |
| 44b22fe6-70c0-3f7b-b1f7-0ee9b3b6f18b | -4.1148 | -48.2515 | 2024-10-10 01:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |


[Clique aqui para ver as próximas entradas](README28.md)
