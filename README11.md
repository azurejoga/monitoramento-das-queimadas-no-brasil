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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92bc260a-8383-3ffa-9da8-9b76b50c756e | -3.78728 | -47.11145 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e88a7d9-5ba6-3b79-9144-493a44bd53a0 | -4.56068 | -43.29842 | 2024-12-22 04:50:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 42551f54-683b-39ef-99e1-2d2fe991dbc7 | -3.91836 | -46.93378 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be07af7e-73e8-3b91-9ee5-1663a4848786 | -2.61381 | -47.46409 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c55da52-1011-3a6e-b509-8c26e6ec34d8 | -2.56618 | -45.95779 | 2024-12-22 04:50:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a2f4075-ff6d-3ade-971c-e44b3f9fb084 | -2.22454 | -53.79617 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81972e3b-14a1-3702-b7a1-e4e93e46b4ce | 0.98572 | -59.53185 | 2024-12-22 04:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a3173002-1b08-36da-8b88-face7e6c3da7 | -2.49617 | -45.03159 | 2024-12-22 04:50:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 276f937f-6acd-3be8-a0c0-161a5b21c47a | -1.46228 | -52.50679 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e54761b9-9ea8-34ea-b574-ee132e74f50f | -2.49581 | -45.03312 | 2024-12-22 04:50:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9246866-3e8c-34ce-9d84-b209eb952949 | -3.36966 | -50.74691 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7895abd0-f418-342c-8caf-caac17d79600 | -2.66637 | -54.87047 | 2024-12-22 04:50:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c252850d-4118-33f9-93df-645780a7e7b7 | -4.56293 | -43.29932 | 2024-12-22 04:50:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 21794918-2e43-348d-bab1-1c4b27b5433f | -1.26036 | -53.51929 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd05fcc4-985c-354f-8afa-0f16b10bfa91 | -3.499 | -42.33394 | 2024-12-22 04:50:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a8ba8a4-b4ec-3f09-9453-4132682164ad | -1.37664 | -53.7054 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78127439-08d8-3fe5-a9df-c1de8f74beea | -3.36778 | -49.1694 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3633b674-43ec-38ea-9539-08351ca18b8c | -2.11455 | -54.20937 | 2024-12-22 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c98424c-e17b-3071-96b9-2e549583afe1 | -3.75179 | -47.18245 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a32e4b4-a311-3d05-8797-cc0bc780c4cd | -2.79807 | -46.74876 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5fe5b83-b71d-315a-89c8-685421e691b5 | -3.40596 | -44.11621 | 2024-12-22 04:50:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c6f8736-aabb-3ca5-83b3-8751c2914b5f | -3.92192 | -47.01501 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d2ade4b-daab-32a2-ab24-df77c7b1654f | -1.45893 | -52.50627 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c809e5f5-4478-3704-9add-598efa48304c | -1.17566 | -52.54838 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7536c4b-8afe-37b2-987a-e68900f40268 | -4.60773 | -45.45492 | 2024-12-22 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2805bd54-4196-3fbb-8c8d-6db6916e4287 | -3.76177 | -47.19796 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afc47118-42b0-34a1-9210-4e0551c9613e | -2.56572 | -49.46553 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31f92a36-dcb6-38a2-ba13-d8ab43f15d0b | -3.90663 | -47.00975 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e1f1058-5970-3753-8ae0-a5a30dbb1692 | -2.23706 | -46.27227 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67c74cf1-edcf-3e0e-bbef-d7d445fd8345 | -3.91574 | -46.89623 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b90c92b-748f-33fc-bc5d-8c01b865b40f | -2.5818 | -47.54296 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaa60514-1218-3849-a962-e73bcbc79874 | -1.18964 | -52.54694 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92865d86-2554-33ac-a3e6-017887478817 | -2.73824 | -46.87209 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a07add63-b40b-3d8d-9d9e-8d6b4ff1108d | -4.01562 | -47.05082 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9302c2d6-a1aa-348c-a24f-25b1ec1e69b5 | -1.56257 | -55.16111 | 2024-12-22 04:50:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38bda9d4-4e87-3167-ac29-d6a56f27c8fe | -3.78342 | -47.11135 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc753e5e-2de9-37df-95b2-65e9ab12b5b9 | -1.22073 | -53.6815 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab6da533-71f7-3b59-b3c1-f840beb315ea | -3.95079 | -46.41298 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| fa90230e-a8ca-3d77-b0ab-cad64ade33b6 | -2.04287 | -52.10938 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 95f6377c-665f-3ce8-9614-0fa427760474 | -0.78456 | -48.77762 | 2024-12-22 04:50:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 372e6314-be2f-380d-b2e8-560f9f6fb569 | -1.88919 | -52.07842 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e5308b6-60a1-3d4d-9490-9a375cb5f4f5 | 1.06874 | -59.40682 | 2024-12-22 04:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb31b35b-8f1b-3e5c-973b-c0dd441015f8 | -2.56633 | -49.46168 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6eca757d-9cee-3f79-a504-1f899c109668 | -1.37094 | -53.69668 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2385942d-3b3b-36a0-9f39-2cbd8e90d659 | -2.56214 | -49.46791 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf5d9fdc-b52d-345c-af37-33308a2b94e2 | -3.74776 | -47.18183 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a99cabfd-96b7-3c3f-b4f1-bf0a119d2832 | -3.18656 | -50.39859 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59c5e0e9-926c-369e-869b-9269b7a90e28 | -1.50654 | -52.63972 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccf6ce58-d33f-3970-aaeb-e9fe8e446985 | -2.50579 | -48.06285 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ac921a7a-7aa9-37e7-b8c7-4c0dd93fe5f2 | -2.56682 | -49.46072 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de71fcf1-6f82-3b5f-9031-07f64d47084b | -4.05515 | -47.09313 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1923ac23-0340-3e6b-8e2c-a52a72e0948d | -4.73252 | -46.542 | 2024-12-22 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a38c4d6-72c9-38b7-ae20-3f0d0930d545 | -1.15277 | -46.7521 | 2024-12-22 04:50:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e885cc4f-6259-3d4d-bac8-7d8e9c3212aa | -2.84734 | -54.70151 | 2024-12-22 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96f4cb2a-3a5f-378b-8dab-c12d39b73834 | -3.92751 | -46.90181 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3db8bf8-0a42-3b33-9e83-ee260e43f046 | -2.68632 | -54.84725 | 2024-12-22 04:50:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3dc39a22-5eca-3ba8-ae11-ff72c310b1e4 | -3.91596 | -46.35434 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 375fa570-e418-3329-a114-1271df286a92 | -2.57501 | -49.45407 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26e810be-d4a4-3e9a-811b-a3f5a5686042 | -3.90308 | -47.00568 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3ca0956-e8c9-3386-a5d1-72401e023f45 | -2.57382 | -49.46178 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3f28abd-d908-3292-8cc5-be400af483f9 | -1.40214 | -48.21537 | 2024-12-22 04:50:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d0d6e10-2b03-3682-9fa3-5b122e15fe82 | -3.76231 | -47.19445 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da1453f9-b5d0-3b3f-9e7c-7f9c91546303 | -3.0993 | -54.54843 | 2024-12-22 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aca75186-cb6e-3313-9d2e-f0ed727ca71b | -1.30067 | -47.75106 | 2024-12-22 04:50:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a8a618f-a5ea-3d18-bf8f-e651abe60cdb | -2.56854 | -49.47283 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad3895da-148c-3351-b5ac-ca686de2829c | -2.57792 | -49.45846 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eb5824d-e80b-37aa-84d5-c37a3e1b4988 | -1.62261 | -45.83863 | 2024-12-22 04:50:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4750d5e-01af-321c-a062-ee77c99e935a | -1.93946 | -45.63611 | 2024-12-22 04:50:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b112eb5-3a69-3112-9bca-5bea92e94112 | -3.17423 | -46.253 | 2024-12-22 04:50:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5952c119-1eba-36f0-9661-8e2bb036c757 | -3.80334 | -46.84619 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da10b8d1-521e-310f-a48c-f290a345f926 | -2.4455 | -51.78706 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cbea729-2049-3db4-851c-d23e5e4978bf | -3.94657 | -46.41211 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa645988-05cb-32ed-b09b-22f09b7d70d3 | -2.50758 | -51.825 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49eeb697-b9ec-3659-ba16-2e8777fb8d2f | -4.09211 | -46.81908 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb31ed1c-8e21-3c50-b55d-c0685fe51a16 | -4.82048 | -44.41131 | 2024-12-22 04:50:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a0b0185d-7191-36ee-a8bb-25bb7f0d5f56 | -2.97365 | -48.07906 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ddae7db-2281-3522-b51f-658bafa7c44a | -1.72 | -52.57188 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2074b262-9ba9-3f36-9c3e-d158ded320c2 | -3.07998 | -46.56124 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d8d6b0a-6438-3ca6-824d-e56c15e296ca | -3.9189 | -46.93029 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ad6222e-9eb3-3537-994e-43d145989930 | -2.55459 | -46.87913 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43456cb6-4cb7-30b0-9466-687b06558809 | -3.36968 | -49.16681 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 470323a4-f5cf-3670-94bf-1dd6eadf70ac | -2.39226 | -47.0799 | 2024-12-22 04:50:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86725de3-6d33-38da-a352-424d7740b1b1 | -3.92637 | -46.90916 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a2bffe7-c82f-3a3b-9aea-8ed306905d9a | -1.25575 | -53.52623 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f9381af-21b2-32ec-85eb-79eeec9ed9de | -2.64699 | -46.10335 | 2024-12-22 04:50:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3155376a-0909-3caf-84c1-647d30fbfcc7 | -1.29023 | -53.12924 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9eb37bfd-8402-381f-9128-58769a33910b | -2.04232 | -52.11284 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bb6817da-07dd-3566-914e-9134632f2122 | -3.65352 | -50.7137 | 2024-12-22 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11926177-6a14-329b-959a-a344eb459205 | -4.01893 | -46.61979 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e128608-3cf9-3afd-920e-dcc15d123a42 | -3.91536 | -46.35839 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0207f58d-3b4b-366f-830f-aafd4c16f364 | -4.54047 | -45.8827 | 2024-12-22 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb138b77-842d-3e77-8d45-eacbc4d389a4 | -3.25415 | -52.88031 | 2024-12-22 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27308235-34bc-34df-a9c2-f7153ae967b6 | -3.90938 | -46.99195 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a8ad500-bb83-3b4c-bc7e-3070ae1aa72b | -2.56346 | -49.08767 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bdc01ebc-ccd0-340e-baa5-9254d7f3be37 | -3.06653 | -47.76934 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dbacb47f-c1a5-35a3-8f62-7641f3f2d59f | -1.36401 | -53.69562 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c19200a-b14c-31ea-b563-4d674eb60b4e | -1.02404 | -50.87082 | 2024-12-22 04:50:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 131e990b-7eca-35f0-9354-78583df59a81 | -2.5645 | -49.47325 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b90e181-4280-340e-a487-0bd8f021a0ef | -1.72769 | -45.8861 | 2024-12-22 04:50:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe30d674-4e7f-3b3b-b60a-b47454ed2c94 | -2.45005 | -49.02627 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README12.md)
