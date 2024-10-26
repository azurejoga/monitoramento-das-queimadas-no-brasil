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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a4883ee-d90f-3aa0-83b8-0c84e15750d8 | -3.15023 | -50.4518 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6767357f-a066-3cb5-81e2-91e55a67facf | -3.14949 | -50.45626 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b573b62-7737-3122-b1d8-326de0949c1c | -3.14876 | -50.46073 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 247063a6-60c3-346e-8b31-68b058c3b4a8 | -3.14573 | -50.45106 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70e7cfa5-3b86-3658-9563-5f8e7a427a34 | -3.14499 | -50.45551 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b615d05-834e-3441-8a8f-82831ea29812 | -3.072 | -50.49651 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f91f9f4-f210-3831-9a8e-2538aa06e1c9 | -3.07127 | -50.50104 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86cfcf5d-dbb7-32af-adde-161ad3b214b7 | -3.07053 | -50.50557 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c8cbd45-e063-36a8-a144-7d590815f2a2 | -3.01851 | -50.48309 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 36505a64-24b0-32f3-92dd-4522c89d35e6 | -3.01776 | -50.48761 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ff76884c-bfee-3a31-ac54-83d8c7c8c434 | -3.01399 | -50.48236 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| acda3834-3097-3424-89d9-ab3c68e82fce | -3.01324 | -50.48687 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0c296120-7672-388f-b944-69e9ea567cb3 | -3.00947 | -50.48162 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9c641c2e-8e86-3b7f-9b1c-c0b078ee7fb7 | -3.00872 | -50.48613 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2a3bfdbe-894a-3402-bc12-0842822197cd | -3.00796 | -50.49067 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 23550f97-e431-3850-8316-e536a430df7f | -3.00495 | -50.4809 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 808d652d-0a3a-3833-9b65-5cadf40cd6d4 | -3.0042 | -50.48539 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e33891f6-104d-31dc-8757-fcd1486ad83e | -3.00381 | -50.48343 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d75738b9-9f69-339e-87f1-5e64eb27bd64 | -3.00345 | -50.48991 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 09cf978e-5049-39d5-a2da-b3bad038a629 | -3.0031 | -50.48793 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 6eb6c335-3dd7-32f3-a1fb-4c4a874ee8c8 | -2.99968 | -50.48466 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 1e385ead-e9f4-3741-8e0a-057c022832c3 | -2.99929 | -50.4827 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 65504427-f4eb-3ff4-9ea9-44c20663191f | -2.99892 | -50.48917 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| b6d50700-4c32-36a3-a076-4d4ffc049205 | -2.99857 | -50.4872 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 6c4a31b0-51e1-348e-98ec-68d135f035c2 | -2.99785 | -50.49173 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 5dd8b106-8a0e-349b-9bc8-06b781eb60cc | -2.99515 | -50.48395 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| a7111070-e6ff-30a1-ac09-7be76dbc6020 | -2.99476 | -50.48199 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e24f9d5c-834f-360f-8af6-2c55bfb8ba1c | -2.9944 | -50.48845 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 7b96b7b3-52c1-32b5-83df-29a0ba97b43b | -2.99405 | -50.48649 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e4812266-a5b0-3694-bd39-c0bd7e85e3bf | -2.99333 | -50.491 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9d66f9bb-08f3-34e2-ad84-f3abcd89b4d0 | -2.99136 | -50.47884 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 155ea68b-b08b-3734-9469-f98122722110 | -2.99061 | -50.48332 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5b84e6f7-9d58-31ee-adb0-2762c86dee2d | -2.99022 | -50.48139 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1e5053f6-797a-381c-9757-a2cad200c34d | -2.98951 | -50.48581 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a2293005-a314-3bcf-969c-8afc7bf42102 | -2.96031 | -50.52292 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c72c6b2-4cfe-362f-b843-3556136a0c46 | -2.95577 | -50.52218 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 698beeac-93c3-3a22-a06b-8954a91a38f5 | -2.95503 | -50.52674 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 890e323c-67c8-354a-b7b4-5d963d7c9294 | -2.88028 | -50.46541 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b5e2561-9f88-3430-bf2e-ac8eca155f9a | -3.15522 | -49.18111 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9854537d-6d77-3e36-8d0f-601770cd37e2 | -2.98752 | -50.2975 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52992912-2438-31ea-921a-42e99eaa307c | -2.98375 | -50.29248 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b669048b-4970-3492-962d-cc430d3b3276 | -2.96882 | -50.41295 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12e5c2fe-7a19-3226-be50-8c67f025e464 | -2.9681 | -50.4174 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91cde49e-3932-3f7a-956c-91387c18bc84 | -2.96737 | -50.42186 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff11dc49-1cd1-3271-bce7-20797aeb9240 | -2.96664 | -50.42635 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8fd4a8f-d072-3d6e-9b42-b3d2133fd575 | -2.96359 | -50.41666 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d33d6df-6622-3ae9-94cc-1465091079b2 | -2.96287 | -50.42114 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 979df391-976c-399a-b397-803dcee7fd67 | -2.96214 | -50.42562 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d62ceb9-f03a-3f50-b71f-8eae80faf211 | -2.96141 | -50.43011 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0048e7f3-7853-383c-aa29-98bd05cea34b | -2.95836 | -50.42041 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58778d2a-7229-3838-a647-8d821ad743a5 | -2.95763 | -50.42489 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 56db7da5-6c2d-391c-b772-16b040650bd8 | -2.9569 | -50.42938 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 34d35063-536d-38d9-8de9-9d950a2355c7 | -2.95385 | -50.41968 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cd66d5c-ca33-30f6-84ee-9ee4d3e72f18 | -2.95312 | -50.42417 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b4d02798-e64b-3fc7-a43a-7d503b957e9b | -2.95239 | -50.42865 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2f808c31-09b4-3760-9fd5-b2e62b0cf86a | -2.87214 | -49.46243 | 2024-10-26 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7707dc65-8cb9-3eb8-84dd-0afd6599a0f6 | -2.86561 | -49.44935 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aea154cb-fc12-396a-9f14-ca00d4ebe69d | -2.86497 | -49.45323 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b006fa35-251f-380c-b186-11cfbda93d14 | -2.86075 | -49.45255 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09a79a3c-eb86-381f-83c6-2e4cbd7735af | -2.83033 | -49.53689 | 2024-10-26 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dca7d44f-11fd-3840-9ced-6124fbbd677b | -2.82961 | -49.53581 | 2024-10-26 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38816999-1e17-3dc3-b708-ab6f009082bc | -2.82772 | -49.25545 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f13103b4-10ef-3519-9450-0b8c6a2ee68e | -2.82711 | -49.25922 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e422796-a4c8-3354-8965-330964fbe897 | -2.82416 | -49.251 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4c887cdf-b4cb-3221-9c2c-d8299e5e5fca | -2.82355 | -49.25478 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c684acdc-70fc-394d-87dc-06d4d4330572 | -2.82294 | -49.25854 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fdaa5f5-f47a-340d-be28-b03df28891df | -2.82233 | -49.26232 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df8c5bef-6cce-3939-8904-acaef756415a | -2.81999 | -49.25032 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7ba7c434-5a91-3c06-ac93-650f7f11142b | -2.81938 | -49.2541 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 519a7b29-7044-37a2-ba5f-7b352e0c92ea | -2.81877 | -49.25788 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8338c8a6-775c-3564-8500-2e85146aee0e | -2.81816 | -49.26166 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| facbf2e5-a588-3415-abb5-890afafdc2d6 | -2.81582 | -49.24965 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4db4ccf6-bc1f-310a-8416-f632f1ad8800 | -2.81521 | -49.25342 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58ae6810-d386-3218-9f9f-02d538958201 | -2.8146 | -49.25721 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cf81581-4cb5-3d60-a181-acdc29e49af9 | -2.81398 | -49.26101 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b34220f-de75-354d-867d-bb642c4332c2 | -2.81166 | -49.24897 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8369e30-d05a-33ac-8c5c-743dbd90729f | -2.779 | -49.31772 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f895104a-11c7-392d-b6a7-797d1a1d810e | -2.74569 | -49.30962 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47bca217-63a5-380e-82d3-74930a222e97 | -2.74508 | -49.31347 | 2024-10-26 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93470276-4e4f-3dc8-a19a-4fffe1c75833 | -3.54833 | -50.29971 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5e311d3-c1e5-33e0-8687-1b8d32dae2f1 | -3.54765 | -50.30396 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6efeffea-92f2-3a2a-8482-558870d0efe1 | -3.51037 | -50.47793 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 114f5683-8637-3cc1-acd9-ca6dc188258e | -3.48201 | -50.48243 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 969b5852-dd08-3c3f-a276-706c71c647fe | -3.46959 | -49.26419 | 2024-10-26 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb7d338d-3c9a-3e3b-8190-8fc63c8c89c4 | -3.46899 | -49.26789 | 2024-10-26 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef01a381-2227-3954-b157-f92d135ee0cb | -3.46486 | -49.26723 | 2024-10-26 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a6029e4-0f36-3725-be29-50af0d932a42 | -3.44568 | -50.15783 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b41f281e-fd78-3c15-845f-f8849ac381f8 | -3.445 | -50.16201 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeb9374b-65ab-32a4-97e2-32528cbddb0a | -3.44128 | -50.15717 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eaf535d-8257-3e53-8356-dc9dbc091943 | -3.43047 | -50.25152 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b734f6a9-c505-393c-9dd7-b62f1218902b | -3.41819 | -50.38352 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e1e9a22-3517-39f9-b8e7-cca5fb2b5a70 | -3.38883 | -49.70729 | 2024-10-26 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f683a69-4ac6-3634-b1d6-696633bf2a98 | -3.38457 | -49.70657 | 2024-10-26 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b24a772-3fd6-30ae-a6fa-4cb71e201c4e | -3.38099 | -50.22151 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64efe287-505c-3fdd-82a7-d88cc72cd5b1 | -3.37657 | -50.22081 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da2d1119-1d08-3fed-9458-247c47083ea6 | -3.37516 | -50.39445 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c101334c-2477-300b-a749-2a3911222696 | -3.30293 | -50.01393 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91805a97-da30-30e4-96c6-0884eddd3022 | -3.28502 | -49.55082 | 2024-10-26 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6481652-39ec-30c7-b0b6-ebd8f4b6f660 | -3.2808 | -49.55013 | 2024-10-26 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17d1ca3f-3bd6-3809-87b8-0a487c478f6e | -3.26023 | -50.60667 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README44.md)
