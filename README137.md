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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e8c1e4e-b5b1-3aa9-9851-ae280df92e78 | -11.5818 | -50.5047 | 2024-09-27 13:16:12 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 99696a36-6103-305d-b81f-570a78f0afc3 | -11.8422 | -49.635 | 2024-09-27 13:16:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| fc5a8112-069a-3006-8fea-bf7ed5d4f51f | -12.3625 | -50.4987 | 2024-09-27 13:16:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 73b04435-44ef-33ec-9684-6f89ff66b8ca | -12.3242 | -50.5033 | 2024-09-27 13:16:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 2d873b7f-ff95-3b4d-a43e-cb2d2b3d6a0c | -12.3434 | -50.501 | 2024-09-27 13:16:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 768c42ac-b346-3c69-96d8-419190e8b6c1 | -12.7505 | -51.3279 | 2024-09-27 13:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 139.0 |
| ce7852f7-4e9c-3f30-8815-adfb9e5d5960 | -12.7501 | -51.3493 | 2024-09-27 13:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a0dbc9c3-9c2e-3608-972e-db49a66a0557 | -12.7508 | -51.3066 | 2024-09-27 13:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 20ab00e5-eb86-3448-99d4-f8e8659f0f8b | -13.1607 | -45.4752 | 2024-09-27 13:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 4c06a476-4887-3d42-82f0-b35e8491ea3b | -13.1801 | -45.472 | 2024-09-27 13:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 360.8 |
| 0aa53585-c37f-3b0c-8bd1-5c4684ad1d4d | -13.1612 | -45.452 | 2024-09-27 13:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 2b3011cd-fcb9-32b6-a348-bd3b8851e253 | -13.1614 | -48.5215 | 2024-09-27 13:16:21 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 436a614a-b870-3506-b43e-25adf637be36 | -13.2105 | -51.2714 | 2024-09-27 13:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 315c1dd2-f315-37f7-ba2d-70b7bfca7292 | -13.2482 | -51.3094 | 2024-09-27 13:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| b3694fe5-0450-32e0-8aab-fd7689dae25b | -13.3376 | -46.2957 | 2024-09-27 13:16:21 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 0746ec1c-a2eb-3971-a528-bc14a6d6343f | -13.235 | -45.6245 | 2024-09-27 13:16:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 9f85da11-81f5-3adf-847f-c6ebf9706530 | -13.2675 | -51.307 | 2024-09-27 13:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| fd27ed6f-6e7c-3792-adaa-d9cb4b719abf | -14.7119 | -45.463 | 2024-09-27 13:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e7fc875c-be38-37ac-9dc2-0b7145f7219b | -14.7114 | -45.4863 | 2024-09-27 13:16:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 3bbde0b8-8af1-315d-9e44-816d60c39635 | -14.8734 | -48.9062 | 2024-09-27 13:16:30 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 3f8b7b5e-17c1-3f9d-95a3-ed1d9c2234d3 | -14.9026 | -51.4534 | 2024-09-27 13:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 387529fa-8e63-3de1-97e6-abc859c9751e | -14.9014 | -51.518 | 2024-09-27 13:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 7aebfe1b-58bc-32ba-b84a-1286fc95bd3d | -15.3904 | -47.4533 | 2024-09-27 13:16:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 019a270d-198a-32d8-b657-ac81f890e68e | -16.857 | -47.7082 | 2024-09-27 13:16:40 | GOES-16 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f0cdd75f-274b-3070-baed-b78ae5f69a38 | -18.0547 | -44.3888 | 2024-09-27 13:16:46 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 11183ed0-f7b5-3fd2-8227-8e2775514a83 | -5.5888 | -42.9282 | 2024-09-27 13:25:38 | GOES-16 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| b448d41f-1ae8-34a2-b720-8aa6bab30b06 | -5.57 | -42.9297 | 2024-09-27 13:25:38 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 81a01330-417c-3530-86e4-1eb637d7b836 | -7.257 | -44.9623 | 2024-09-27 13:25:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 1dce6306-103a-3fe3-a97c-28cf856f502d | -7.3609 | -44.0804 | 2024-09-27 13:25:48 | GOES-16 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5c28d499-f1b7-316f-ad94-cd647338e8aa | -7.3606 | -44.1035 | 2024-09-27 13:25:48 | GOES-16 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| f53da8b3-2d7c-3084-879a-d2187bffbc2d | -8.0886 | -49.5224 | 2024-09-27 13:25:52 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 47cf8cbe-0251-313a-bd17-79c4b0a44384 | -8.0541 | -42.8876 | 2024-09-27 13:25:52 | GOES-16 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| e6712fb2-8071-378f-ae4a-6111941c031a | -8.073 | -42.8855 | 2024-09-27 13:25:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 217.9 |
| ebe9e5e7-ea2b-3453-a0c6-0b54f67a5af8 | -8.3215 | -56.4929 | 2024-09-27 13:25:54 | GOES-16 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 220f4ec4-b55c-3277-8460-1816432d56e1 | -8.5922 | -51.4491 | 2024-09-27 13:25:55 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 3d39722a-52f2-39e1-8852-9189d11b00f6 | -9.0251 | -45.1707 | 2024-09-27 13:25:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| a2de9f12-c80c-370d-b95b-10e2de843fa7 | -9.0444 | -45.1457 | 2024-09-27 13:25:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 770e71c8-55b1-3004-8510-b95477b14896 | -9.5829 | -50.137 | 2024-09-27 13:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| f875f4cc-511f-3d07-a41c-34d3467bd364 | -9.5641 | -50.1388 | 2024-09-27 13:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| df0660eb-80c5-3413-adad-cce85e73751b | -10.0134 | -53.4875 | 2024-09-27 13:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c9fcf4d9-acdd-3f4a-b305-c30bb827480e | -10.0136 | -53.467 | 2024-09-27 13:26:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 162.4 |
| c6a6780f-a63c-3710-abf6-e65411a5c6f6 | -10.1501 | -49.9956 | 2024-09-27 13:26:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 37961ec5-de9e-3689-ac40-7ec825377d4c | -10.2824 | -43.5551 | 2024-09-27 13:26:04 | GOES-16 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f522e8d9-3608-31b0-a75b-7f4f53b40a9d | -10.1312 | -49.9976 | 2024-09-27 13:26:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 0f8f72fd-5253-3794-a316-24c30ef836da | -10.3672 | -53.7858 | 2024-09-27 13:26:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 18cb29e9-513e-3c13-9280-77117258d3b9 | -10.4675 | -50.2624 | 2024-09-27 13:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8fe5f3b0-2d94-3bb0-8cf9-23392045dd3c | -10.6434 | -45.9772 | 2024-09-27 13:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 317.0 |
| f06a45a3-932f-3734-907b-27c50798fb99 | -10.624 | -46.0023 | 2024-09-27 13:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 58abe886-3ea7-3627-aba5-d5ce7a1faeda | -10.6438 | -45.9544 | 2024-09-27 13:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 224.3 |
| 8d578882-947d-3ba9-a90c-aeb4ddb7e59b | -10.6844 | -51.0059 | 2024-09-27 13:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 558c055e-7f68-3a56-bde8-92c2c66ade2d | -10.6639 | -45.8838 | 2024-09-27 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 472.7 |
| add588ad-7cef-3570-82a3-5fbb0dd5f212 | -10.6076 | -51.0984 | 2024-09-27 13:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a8c1a7f9-e4bf-3648-80bb-082d0c040749 | -10.6643 | -45.861 | 2024-09-27 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 75e7e3bb-d5b0-3277-a708-110afff3a9e0 | -10.6846 | -50.9847 | 2024-09-27 13:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 0d7ea614-fcb6-3fee-a3c1-8646d0f15d5a | -10.6636 | -45.9065 | 2024-09-27 13:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 432.3 |
| e19c6a2a-0ee3-3531-8398-461252620d19 | -10.942 | -50.1478 | 2024-09-27 13:26:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2dd04628-2a6d-3d16-bdfb-54409b520c9d | -10.865 | -46.4009 | 2024-09-27 13:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 55a74d78-a9a5-39b8-8288-4fda79859c79 | -10.9148 | -45.669 | 2024-09-27 13:26:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 7dece490-1919-3b17-9792-547232a0daaf | -10.9152 | -45.6461 | 2024-09-27 13:26:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 0e066d1b-e78a-3287-b60f-5b144904b57a | -11.0976 | -46.1446 | 2024-09-27 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 2d3aac7e-aed8-3d85-9e40-b4813c94db94 | -11.1647 | -45.5439 | 2024-09-27 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 44c9a34a-43b8-3357-af5e-05825d316180 | -11.0577 | -51.3694 | 2024-09-27 13:26:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4652d8ab-5fac-320d-985d-ba42d7286840 | -11.1459 | -45.5236 | 2024-09-27 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 00ce9909-6fc7-3a6d-86fe-8d645c455814 | -11.0972 | -46.1673 | 2024-09-27 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 2f42d5dd-26c9-36b3-a598-286e629d4b0a | -11.1456 | -45.5465 | 2024-09-27 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| fdb7742c-c803-3c36-9791-273f715ecc1a | -11.2025 | -45.5616 | 2024-09-27 13:26:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 3a5ade0c-f5a4-3e6f-95a4-c75ea40854ec | -11.1219 | -50.8328 | 2024-09-27 13:26:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 3d14a881-8775-382f-a2f9-07b0ca24022c | -11.2534 | -47.1142 | 2024-09-27 13:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 792435bb-0564-39a2-9481-e78e81a963bf | -11.2531 | -47.1366 | 2024-09-27 13:26:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 208.8 |
| fce9d658-c36b-3958-9359-a52b2cbcadd5 | -11.1754 | -49.7348 | 2024-09-27 13:26:10 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| eca7a10c-6c33-32d6-9e2a-8425594e656b | -11.1564 | -49.737 | 2024-09-27 13:26:10 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 20b65db9-89d7-3525-bc7b-6b039c398276 | -11.1567 | -49.7154 | 2024-09-27 13:26:10 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| a61a1401-e7db-3783-8df8-739b906f0b57 | -11.6409 | -44.5303 | 2024-09-27 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 6bc28468-b492-3a28-8dad-a57e6803ff14 | -11.6605 | -44.5041 | 2024-09-27 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| e1ceef93-a688-3043-87f0-36965d1d975c | -11.8422 | -49.635 | 2024-09-27 13:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| fa888a2d-d07e-3c55-8dd7-1f4603139667 | -12.1859 | -50.8195 | 2024-09-27 13:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 422a124e-a8a6-3f4d-9d8d-752d3bc45a58 | -12.1856 | -50.8409 | 2024-09-27 13:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| b531e4b8-657a-302a-a3df-f7a932dccf64 | -12.3625 | -50.4987 | 2024-09-27 13:26:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| adede0f1-88d4-3305-8750-017e03978879 | -12.4786 | -50.3986 | 2024-09-27 13:26:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 644ffdef-7243-3399-ace3-cbe162d036b3 | -12.4782 | -50.4201 | 2024-09-27 13:26:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c8d561bf-07e2-36b0-a089-846d04f3d4a8 | -12.7505 | -51.3279 | 2024-09-27 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 5ab331c1-6555-36fc-9565-2a23e0e8992e | -13.1801 | -45.472 | 2024-09-27 13:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 3e412967-19df-3be9-a109-2a5d70337cb5 | -13.2675 | -51.307 | 2024-09-27 13:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| cb641902-dd1a-359b-a344-188d410edaa6 | -13.235 | -45.6245 | 2024-09-27 13:26:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 4e357faa-e9d7-336f-bdc6-f5fbbaf853e5 | -13.2105 | -51.2714 | 2024-09-27 13:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 518e95be-945d-3b5b-b984-9657914cf784 | -14.9026 | -51.4534 | 2024-09-27 13:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| c662f01b-74ce-3539-a250-97a8671abc9f | -14.8734 | -48.9062 | 2024-09-27 13:26:30 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| dbc81fde-e2b1-3bbd-9356-bfe5b03c1652 | -14.9014 | -51.518 | 2024-09-27 13:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 5dda0f36-ae55-3680-8385-fea970c89d01 | -15.3904 | -47.4533 | 2024-09-27 13:26:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| ea72a870-107a-39fc-af63-2bbfd3b046ad | -18.0547 | -44.3888 | 2024-09-27 13:26:46 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 76298e04-33e1-311b-9c77-d6feee22e481 | -19.3773 | -42.5809 | 2024-09-27 13:26:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.5 |
| d9e24a5f-656c-3042-b7a0-6b51e1b35c91 | -20.0286 | -45.2064 | 2024-09-27 13:26:57 | GOES-16 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 106.2 |


