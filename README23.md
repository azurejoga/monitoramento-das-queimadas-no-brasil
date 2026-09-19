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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10c27b84-99a0-3690-b2fa-47fcaaee0b7d | 1.2608 | -50.976 | 2026-09-19 01:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5f3e5125-b579-3e65-bff8-718cc5006008 | -4.5772 | -42.9746 | 2026-09-19 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 98215cb8-d0c5-30f4-b4e8-0432aa990d6b | -2.8285 | -50.4653 | 2026-09-19 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| e70f3f24-9226-345f-88b9-87e30c46b305 | -10.6928 | -60.7322 | 2026-09-19 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 0bde428b-f4a5-327f-98b5-90e504b1ee18 | -10.7115 | -60.7312 | 2026-09-19 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| bd1a0965-f868-3afa-b5cf-b9c2a0d6c816 | -12.5952 | -49.1046 | 2026-09-19 01:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 640a3149-0e42-3f3e-b7e7-a800a2b9186c | -3.331 | -59.8292 | 2026-09-19 01:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| c98cea09-0f9c-3c40-8be3-fe39e46ffdf9 | -9.0546 | -48.7252 | 2026-09-19 01:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 53837d29-e494-3f62-a9db-51f2065a0d40 | -18.4098 | -49.176 | 2026-09-19 01:00:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 89.1 |
| 2fd76601-b112-315e-bd6b-44396d09c00e | -4.5585 | -42.9758 | 2026-09-19 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 6f7f5b26-06e9-328b-8a00-a962b282546f | -7.6574 | -46.1013 | 2026-09-19 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 781e9771-5d44-3a6e-b8be-b7014ee5d133 | -3.2313 | -46.9596 | 2026-09-19 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 680d5077-38d2-3ce5-9458-5d6bd86769ca | -14.8512 | -47.1382 | 2026-09-19 01:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 82ef04cd-a963-3ec0-8479-8351632be37d | -14.8708 | -47.1349 | 2026-09-19 01:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| fc538830-b0c3-380f-b83d-3228665f2c79 | -5.5249 | -43.7953 | 2026-09-19 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 8df331bb-6ae0-3d7f-936a-ba1e1dcde937 | -5.5064 | -43.7735 | 2026-09-19 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 42d3ddb2-29b0-3728-9254-f24c8daa8a11 | -18.4104 | -49.1534 | 2026-09-19 01:00:00 | GOES-19 | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.3 |
| 538223ca-31ee-39b5-8d88-5704b10f2a26 | -4.5961 | -42.95 | 2026-09-19 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| ce749282-ab72-3b93-8fd7-f69bbbd1a2e4 | -14.1347 | -45.171 | 2026-09-19 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| ba86d6da-e583-3355-bcff-5a2602469eba | -10.867 | -56.1975 | 2026-09-19 01:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 51d0395d-5aaa-3f56-bb9c-902633a12f6c | -3.3638 | -50.4492 | 2026-09-19 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 66f452c3-1e68-3221-8d34-51ad4ead16bb | -3.3311 | -59.8101 | 2026-09-19 01:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 2a9bad3a-ffd3-30ff-bef6-d490ee41c03d | -10.9301 | -53.9618 | 2026-09-19 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2a81c0e2-8fe8-3531-a48e-9632d67b8ade | -7.6386 | -46.103 | 2026-09-19 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| a840f54b-4608-32e0-862c-2dc24021480a | -4.5774 | -42.9512 | 2026-09-19 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| a9e35b53-5f22-3400-aad5-66b8a1e31f29 | -5.5062 | -43.7966 | 2026-09-19 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 9eb13c87-bcaf-37c5-91cd-bcbc53adeabe | -7.6386 | -46.103 | 2026-09-19 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3750c99a-d21e-333b-a459-45511acc0612 | -2.8101 | -50.4658 | 2026-09-19 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 19410dea-5d93-34b8-a8d5-03a6e0dca1af | -2.8284 | -50.4863 | 2026-09-19 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 9d23ce9d-1e63-3b26-9914-59ead6002c41 | -7.7631 | -46.7167 | 2026-09-19 01:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| ea61bfc5-5e85-3f4e-9516-a6da201ad332 | -3.2313 | -46.9596 | 2026-09-19 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8d7afc3f-631c-3e39-ac3e-1f49bf66985c | -4.5585 | -42.9758 | 2026-09-19 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 828dc5d1-d93e-34fe-85b6-66b17087b206 | -5.5251 | -43.7721 | 2026-09-19 01:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| cdc0c97f-95a5-34fd-949b-2058c5ad698e | -7.6574 | -46.1013 | 2026-09-19 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 66e64679-2d63-3c57-8e05-fb65951eb4df | -5.5249 | -43.7953 | 2026-09-19 01:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 170de7d4-56cf-3cfc-9434-c4aae3f83e56 | -6.9871 | -42.1917 | 2026-09-19 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| b3f1aa7d-3e8a-33b5-b9d2-b61c979a9561 | -8.4983 | -57.6271 | 2026-09-19 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b2d4d322-9a5c-3c0e-89be-c0dee247795b | -10.8941 | -50.8782 | 2026-09-19 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 0f42dcbb-6486-3e5a-b506-08b8d597c181 | -11.0611 | -49.7693 | 2026-09-19 01:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ab12d97d-a963-3c04-ae0b-6d221b5c6a81 | -10.9301 | -53.9618 | 2026-09-19 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| aeef3936-e312-3159-8209-e59dfd20245a | -4.5772 | -42.9746 | 2026-09-19 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a176fef8-aed2-3627-80ba-6f050d86f578 | -10.7115 | -60.7312 | 2026-09-19 01:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| e9b01189-cbf9-35f8-bb4d-30942b317405 | -6.9874 | -42.1678 | 2026-09-19 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| ba0a43dc-389d-328f-8f10-795ccc793e27 | -10.6036 | -46.0955 | 2026-09-19 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 8ebd9397-2ff5-3b18-83d0-8bfbb7adb827 | -8.4296 | -54.7262 | 2026-09-19 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| eb5f4e99-da79-3d2f-b6ca-04e106567eae | -10.6226 | -46.0931 | 2026-09-19 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| c75423e2-6a51-3e61-8ba9-161e374fe506 | -8.452 | -45.7092 | 2026-09-19 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 6292131f-f701-3f03-9cfa-71a56fbccd61 | -3.3638 | -50.4492 | 2026-09-19 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 708e91ac-7c2a-3fdc-b5d8-69189af859e6 | -3.3494 | -59.8097 | 2026-09-19 01:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 8768eded-6d24-3ade-8b70-ddc78c9b735e | -10.6928 | -60.7322 | 2026-09-19 01:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 72c1d28d-f56f-34a1-be12-2c5ee14a55d0 | -6.001 | -51.7903 | 2026-09-19 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 523923ee-baea-328c-8a30-c8ae4112bc4e | -7.7629 | -46.7389 | 2026-09-19 01:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| aae7c1f6-a780-3a73-a539-497b59f95ec9 | -10.867 | -56.1975 | 2026-09-19 01:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 3c2aa971-f6b8-3463-b9b3-3d7916b4fd32 | -3.331 | -59.8292 | 2026-09-19 01:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 820a84d6-9bef-3929-b596-80cd4bc60b9b | -16.8149 | -46.9841 | 2026-09-19 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| d083443a-c259-35da-95a6-790828c0d2a1 | -16.7951 | -46.9879 | 2026-09-19 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2d8c3501-e0a5-3fd0-8312-225c802c6e78 | -3.3311 | -59.8101 | 2026-09-19 01:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f1dd2a87-ebef-3974-a8cf-c0c3d68a044a | -2.8286 | -50.4444 | 2026-09-19 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 96968cac-06bc-3886-a807-4f72ae0a851a | -2.8285 | -50.4653 | 2026-09-19 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 7798e68b-4992-3604-b949-a83db240c8c9 | -3.331 | -59.8292 | 2026-09-19 01:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 15581694-f223-373f-97bc-60c3b298ec6c | -10.6226 | -46.0931 | 2026-09-19 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6c3db71f-e0d9-3666-bc1c-0f8a6b491d8a | -3.2313 | -46.9596 | 2026-09-19 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 472bb933-6a2a-3954-aed6-3b8d7a1ddfb0 | -16.7951 | -46.9879 | 2026-09-19 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 082c5e86-74fc-336c-a3fb-91ab1f65ba1d | -2.8285 | -50.4653 | 2026-09-19 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 742f0720-b1b4-3fa6-987e-ed318f729c4a | -10.6928 | -60.7322 | 2026-09-19 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 183.2 |
| 945d9e6b-59dd-32a3-9fad-fad7ae0ffdb2 | -2.8101 | -50.4658 | 2026-09-19 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0ee164d1-31f0-3e0d-926a-b8af8ac5bd7b | -10.7115 | -60.7312 | 2026-09-19 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 240.4 |
| 294d8773-88ea-34a1-b3be-2a6f73a80e75 | -10.9301 | -53.9618 | 2026-09-19 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e70ebaf7-b928-38f0-b3cc-c0bd16c776f7 | -10.6926 | -60.7516 | 2026-09-19 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| bd5b1126-26a7-3a27-b1f0-b0229df91683 | -8.4983 | -57.6271 | 2026-09-19 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 9112c4eb-db44-348c-9730-72d2d2e45ec9 | -6.0009 | -51.8111 | 2026-09-19 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 56e78a45-13ea-3839-a59b-2c8b6618e252 | -6.001 | -51.7903 | 2026-09-19 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 81fa95f8-24dd-34ab-9cb5-e6fe45f43f5b | -3.3311 | -59.8101 | 2026-09-19 01:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f52a78f0-ff7f-3a84-8740-e1c92f8789fa | -10.867 | -56.1975 | 2026-09-19 01:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| bdf857b6-a844-3b72-ad81-9baca36cb587 | -4.5774 | -42.9512 | 2026-09-19 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 5efacb2c-b5b8-38d8-9251-710ea55f90d6 | -10.7114 | -60.7505 | 2026-09-19 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| cc346b33-1e10-3058-b238-40abbcc9e176 | -5.5249 | -43.7953 | 2026-09-19 01:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7adf6110-bec0-3fe1-8abb-dfb7469c29c3 | -3.2314 | -46.9376 | 2026-09-19 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 971e33b7-d99f-3285-a8f7-3785208af458 | -6.9871 | -42.1917 | 2026-09-19 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 178.6 |
| dd615415-d168-3fbe-9d15-c50d6c3f3d0c | -10.6036 | -46.0955 | 2026-09-19 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f0cbe94c-5700-3153-ae3d-5ffdfbb1f107 | -4.5585 | -42.9758 | 2026-09-19 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 511bbb17-0adb-366f-933b-98e12bdcabfa | -10.7303 | -60.7301 | 2026-09-19 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 1e102e79-1f8b-3556-83c9-a170b1800428 | -6.9874 | -42.1678 | 2026-09-19 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 40d2b501-c7fa-3113-935c-dd87143a6455 | -7.6386 | -46.103 | 2026-09-19 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 1e866d6d-ca0e-31d3-ac18-73cc90508979 | -10.6226 | -46.0931 | 2026-09-19 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ad828ed0-a095-3bfe-9829-4fbfe6691600 | -7.7629 | -46.7389 | 2026-09-19 01:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| be127722-6d41-37e6-81b9-29471e6edbd4 | -2.8285 | -50.4653 | 2026-09-19 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| b8e3bce9-65c8-38a3-ba69-2e5be816d0d2 | -3.3311 | -59.8101 | 2026-09-19 01:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| afa73ae3-48e6-3ad4-9bf5-e327386fa695 | -10.7115 | -60.7312 | 2026-09-19 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 148.1 |
| f9e4a87e-ec8b-3074-9cbe-6e9c136246ba | -2.847 | -50.4648 | 2026-09-19 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4f6b47f3-d9b7-3733-a28e-382f06413dd5 | -6.9874 | -42.1678 | 2026-09-19 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| ad8d4419-6a58-31df-b0bb-ca306c31e621 | -2.8101 | -50.4658 | 2026-09-19 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ada631f0-a444-3575-8c8a-358ce4e03c2f | -3.2313 | -46.9596 | 2026-09-19 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| cf263162-e736-3b71-9be9-11d5f000c1c6 | -6.001 | -51.7903 | 2026-09-19 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8b3cffc6-49ac-3c4c-a162-a2bddbdc7b1e | -7.6386 | -46.103 | 2026-09-19 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ff605772-e360-3417-8819-23732a27aba6 | -3.2314 | -46.9376 | 2026-09-19 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 75d7f30a-b1a2-3da8-aa3f-596832bd63a0 | -10.6928 | -60.7322 | 2026-09-19 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 88370070-fbb6-3493-b8fe-8d714172c191 | -3.331 | -59.8292 | 2026-09-19 01:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 657f8d2f-be4b-336c-99a0-04ddfb8602b7 | -10.867 | -56.1975 | 2026-09-19 01:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2d051116-2a02-3352-97d9-b36a901e6875 | -6.9871 | -42.1917 | 2026-09-19 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 138.3 |


[Clique aqui para ver as próximas entradas](README24.md)
