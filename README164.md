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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a56a3cc1-116b-3f1a-af8b-f02fc252ea71 | -10.4235 | -50.7355 | 2024-10-05 13:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f97194db-b26c-3679-b354-fb77e81665dd | -10.3131 | -50.5128 | 2024-10-05 13:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 18f4235f-bc9c-3c42-a0bf-6ad02a3812a1 | -10.4424 | -50.7336 | 2024-10-05 13:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 3decf2d7-5472-3465-b142-7ee830970b7f | -10.7542 | -46.1894 | 2024-10-05 13:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d1b4020d-2b8c-398c-b578-1ab9bab8a6e0 | -10.9671 | -54.0199 | 2024-10-05 13:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 6c2f6cd3-dbb2-3ef5-bc6d-7865fb1eb1f3 | -11.1983 | -46.9871 | 2024-10-05 13:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 223.5 |
| 46e51297-265e-3ca1-a0c7-7143af49398f | -11.3368 | -45.5202 | 2024-10-05 13:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| c9456318-65a3-32aa-afde-cf44971886c6 | -11.3662 | -47.2113 | 2024-10-05 13:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 40b8d280-8a86-36d9-85c7-a9020583192a | -11.8914 | -50.147 | 2024-10-05 13:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| c71ccc0c-e41d-3cc3-a2f1-52690ed7d3fe | -12.6723 | -54.0395 | 2024-10-05 13:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 3b95ef62-07c4-3fa5-b2dd-9ad60a24148a | -12.7815 | -50.5758 | 2024-10-05 13:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| fafbe0df-570b-3cc8-9555-fb4be461f935 | -12.7774 | -47.4425 | 2024-10-05 13:06:18 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| ad92a69a-8716-3d2b-9cb0-af757fdc828d | -12.6532 | -54.0415 | 2024-10-05 13:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 4ccdbfca-77a3-3dde-b47e-540f86017ba4 | -12.7623 | -50.5782 | 2024-10-05 13:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ba7be443-fef1-35cc-b3cd-05ec310aa86b | -12.8198 | -50.571 | 2024-10-05 13:06:19 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 292214b9-3a46-3d7a-8a37-ed3762b95fad | -13.0368 | -51.357 | 2024-10-05 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3be7eea0-8f71-3497-a29d-c554a4a2fa33 | -13.0598 | -51.1195 | 2024-10-05 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 4245252f-2280-31ba-a873-bf71540fb440 | -13.1056 | -46.3321 | 2024-10-05 13:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c5e2323c-efd8-3bfc-b1e1-04b220d5b82a | -14.0572 | -45.1614 | 2024-10-05 13:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 0c41aaa4-30de-3aa7-b3ac-72b57b8a5a13 | -14.0504 | -45.4877 | 2024-10-05 13:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 363.4 |
| 2c01e449-74ff-36cf-aa4d-8b4620f4c87c | -14.0577 | -45.138 | 2024-10-05 13:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| ef8882e1-ebad-3bca-93f1-dc658b76e749 | -16.679 | -55.5402 | 2024-10-05 13:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| ac701937-97bb-3b26-9a6d-3fb9a4a86cd4 | -16.6923 | -55.9117 | 2024-10-05 13:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 04de3f4f-031e-351d-8ecf-d71b391e0ba8 | -17.0319 | -56.6749 | 2024-10-05 13:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 3da347c9-5233-3126-a0fe-47b35ebb371d | -16.9711 | -56.8058 | 2024-10-05 13:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 62098a06-02f0-3b7e-89e9-30b0ac3542f8 | -16.9748 | -56.5789 | 2024-10-05 13:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| a9e30ea2-66d1-3315-b518-801a90f74dba | -17.012 | -56.698 | 2024-10-05 13:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| f29ce24b-ae54-3454-8aff-385b55ea2b9a | -16.9744 | -56.5996 | 2024-10-05 13:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| e4b952f8-3f15-3444-8dfd-9682aaef778e | -17.1284 | -56.7661 | 2024-10-05 13:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| cc098f69-0edf-37f5-9d5f-12f1d830db56 | -17.1185 | -57.3834 | 2024-10-05 13:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.1 |
| a83caed3-10ae-3ce4-a6ae-c79fa6cf6a23 | -18.6984 | -57.2708 | 2024-10-05 13:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 146.1 |
| cb23c275-0774-3e29-a430-17c73e69199b | -18.6785 | -57.2734 | 2024-10-05 13:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 196.1 |
| 43ce3e47-0d91-3361-8c70-d23ceeba0cd7 | -7.0232 | -59.4111 | 2024-10-05 13:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c2d3d3f1-aeba-3c35-a037-3f8d27126939 | -6.9515 | -59.0473 | 2024-10-05 13:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 3840cbaf-b3e4-36cd-9849-2ce6edbe80c4 | -6.9698 | -59.0852 | 2024-10-05 13:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| a52e4e20-ed4e-31a0-8e27-346adf539b26 | -6.9514 | -59.0666 | 2024-10-05 13:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 253.3 |
| 48d005c1-3098-30c7-a40d-8bfb04435c70 | -7.0233 | -59.3918 | 2024-10-05 13:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| da061639-1161-3628-b76b-4b778d019f14 | -7.7498 | -43.0618 | 2024-10-05 13:15:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 94fa2973-4135-3483-b2cd-b04740ee8484 | -8.7772 | -49.955 | 2024-10-05 13:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 9b6a5ba1-2dc4-3db9-81f2-0bdb4c062e7a | -8.8528 | -48.3097 | 2024-10-05 13:15:56 | GOES-16 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 7a6f2128-aa2c-3e8c-b566-d0171908c190 | -8.8525 | -48.3315 | 2024-10-05 13:15:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 77199da2-934a-3cd8-8a1c-feb5375fe93e | -8.8714 | -48.3297 | 2024-10-05 13:15:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 34df931c-f1b0-3ec4-800c-01a193999a3e | -9.3269 | -51.1142 | 2024-10-05 13:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1fb69d00-23be-336f-8449-54e484a40a71 | -9.3457 | -51.1125 | 2024-10-05 13:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0f78772b-f1d5-3eda-ab8d-989a85aeca1a | -9.3647 | -51.0898 | 2024-10-05 13:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c21b8843-d0e6-36ec-b85d-81b44d9e685f | -9.7883 | -46.0593 | 2024-10-05 13:16:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 7bb09651-8bd5-3453-8948-f7c9008dc6a6 | -9.8858 | -47.1901 | 2024-10-05 13:16:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| afb2ad22-bb81-3c29-b374-51401ddb3a6a | -10.2479 | -52.7242 | 2024-10-05 13:16:04 | GOES-16 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| e6eca7c2-1bb1-3a53-a2d9-283e531aee4e | -10.2908 | -45.4305 | 2024-10-05 13:16:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 8635bb84-011d-3e31-9f39-213c49796dcb | -10.2476 | -52.7449 | 2024-10-05 13:16:04 | GOES-16 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 09a83cd9-42c1-36c9-9b20-5423f71fb54f | -10.3131 | -50.5128 | 2024-10-05 13:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ad7994e1-0eac-3ff1-bd38-06d0f166706f | -10.2942 | -50.5147 | 2024-10-05 13:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1667965f-fcf7-3a69-9115-276a83575806 | -10.7542 | -46.1894 | 2024-10-05 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f28bb327-d0ee-3277-9602-ae1fe15c1146 | -11.1983 | -46.9871 | 2024-10-05 13:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 2f268c17-c037-3519-922a-a80fd9499468 | -11.3853 | -47.2088 | 2024-10-05 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7666911f-998a-378b-9dae-de473c85fd82 | -11.3662 | -47.2113 | 2024-10-05 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a48ee7b5-84f5-347d-b817-c4a4865d41ac | -11.4238 | -47.1815 | 2024-10-05 13:16:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3f5f6e06-408e-3104-8d80-e46ade50b6e6 | -11.4234 | -47.2038 | 2024-10-05 13:16:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| decd38fe-8603-3832-ba5f-6f4db1651ee6 | -12.6723 | -54.0395 | 2024-10-05 13:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 47114097-619c-3ed5-b846-2df600a373c8 | -12.7623 | -50.5782 | 2024-10-05 13:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 19d4aa8a-4db2-368e-b605-e0e1b7a4d393 | -12.7815 | -50.5758 | 2024-10-05 13:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| d9e15fd4-2c96-3021-bb65-3ed05c168e94 | -12.6532 | -54.0415 | 2024-10-05 13:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| f87a6b9e-9800-3269-8d32-4e983995f63a | -12.7774 | -47.4425 | 2024-10-05 13:16:18 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 659c6fdb-673f-3e43-ae5a-8982273e5f22 | -12.8198 | -50.571 | 2024-10-05 13:16:19 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 4f25a301-d7f3-3556-8d98-c68a0620fbcf | -13.0598 | -51.1195 | 2024-10-05 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 8fa6d7b8-1d34-3647-9005-447d10959ea3 | -13.0594 | -51.1409 | 2024-10-05 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| db0a7abd-9dd2-3ab5-aef3-71291d169d93 | -13.1543 | -51.1931 | 2024-10-05 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| b64a54c4-a5ba-3b73-a6ec-1c0ce24cd3ad | -12.9831 | -51.129 | 2024-10-05 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 39a06034-0c22-38cb-a01a-d6e38e2eb07c | -13.1056 | -46.3321 | 2024-10-05 13:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d798fdc3-c67a-3a1f-a616-b9a5b4ce0b18 | -12.9776 | -51.4706 | 2024-10-05 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 3c866f82-29b4-31da-8677-cebf44950c6b | -12.9827 | -51.1504 | 2024-10-05 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| f6ecb044-8f74-32df-ad5a-af2b758de5c4 | -14.0504 | -45.4877 | 2024-10-05 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 366.5 |
| fec5d73b-f0f2-3b6a-ac80-74adbdff6b87 | -14.0577 | -45.138 | 2024-10-05 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| bfd6291e-9775-3654-bdd3-9c14e02d14d2 | -14.0572 | -45.1614 | 2024-10-05 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 0096fc31-bfad-3f13-af6f-a51f89455002 | -14.5646 | -48.8217 | 2024-10-05 13:16:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ecc29ad4-9b37-301d-b090-8de398960ce8 | -16.679 | -55.5402 | 2024-10-05 13:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| deb8bab3-85c8-3567-884e-404815c27401 | -17.0908 | -56.6678 | 2024-10-05 13:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 00726d78-4bec-3b93-9239-3f32504ec621 | -16.9748 | -56.5789 | 2024-10-05 13:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| cd22e2c2-ac0b-3eb2-a96f-57117ec37920 | -17.0123 | -56.6773 | 2024-10-05 13:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 94761841-bd60-334b-b460-62dd0f23efc0 | -16.9744 | -56.5996 | 2024-10-05 13:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| f02efe4f-48d6-3976-95d3-07ebc1edd1cc | -17.012 | -56.698 | 2024-10-05 13:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 5438e1d8-1dc5-37ca-88b0-6d9fdde605dc | -17.0319 | -56.6749 | 2024-10-05 13:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 07479039-46c3-35ec-8120-4e6a42dab089 | -17.1288 | -56.7455 | 2024-10-05 13:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 169b8e93-bdc1-3cb5-9610-80910c911503 | -17.1284 | -56.7661 | 2024-10-05 13:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| c9b3e7df-e60e-3c71-babe-b43a9a9084a0 | -18.6785 | -57.2734 | 2024-10-05 13:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 216.9 |
| 6715a596-c3fd-348b-b619-2aea3fdbe59a | -6.9514 | -59.0666 | 2024-10-05 13:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 253.0 |
| ce65e400-8cbe-3663-8066-d6c45ca02bbd | -7.0233 | -59.3918 | 2024-10-05 13:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| f487c257-4bf4-3798-9373-17072cc8b575 | -7.0232 | -59.4111 | 2024-10-05 13:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| d10c269e-a27f-30b2-b740-2f4e115fa7bb | -6.9515 | -59.0473 | 2024-10-05 13:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 7708df85-fcac-3fc4-9fba-e49a11a60fd4 | -6.9698 | -59.0852 | 2024-10-05 13:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| d2daf4fd-b4fb-3f4f-b105-c0601e5555ca | -7.5028 | -44.8254 | 2024-10-05 13:25:49 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| cfa9f2a0-eb92-3a8a-892a-fef8f9333965 | -7.6262 | -45.5413 | 2024-10-05 13:25:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f698d5cb-cee3-394c-9c4f-cb1c8a03af71 | -7.7498 | -43.0618 | 2024-10-05 13:25:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| e15d63b4-e774-3c28-9b5c-4220f247f737 | -8.1183 | -43.7718 | 2024-10-05 13:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 128.6 |
| 47875c2d-94ab-30a1-87b3-393654c1b3a9 | -8.6377 | -40.4266 | 2024-10-05 13:25:55 | GOES-16 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 82.8 |
| c55ba11a-97c1-3ac5-a115-da3be8976728 | -8.8525 | -48.3315 | 2024-10-05 13:25:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 01d32b3b-b64a-358c-897f-2e1cf2900acf | -8.8714 | -48.3297 | 2024-10-05 13:25:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 73454cdb-46e4-3f4d-ac0a-5686050c4174 | -8.7772 | -49.955 | 2024-10-05 13:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 7c533be0-1a9d-3c2b-a7df-1395b1375dd7 | -8.7584 | -49.9566 | 2024-10-05 13:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 0ff97f14-a908-33b8-87b3-94244a9b5386 | -9.3269 | -51.1142 | 2024-10-05 13:25:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |


[Clique aqui para ver as próximas entradas](README165.md)
