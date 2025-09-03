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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bb0185c-be6e-3054-8749-62320a038121 | -6.33804 | -58.32679 | 2025-09-03 05:12:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 769639a4-2981-3785-876f-265ad6d68dd3 | -6.05925 | -58.01823 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11eac04e-97b3-3f68-8294-e9a10dc86470 | -6.82296 | -52.81555 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c55f634-19a7-3d49-8966-65eb88861485 | -3.07963 | -56.64677 | 2025-09-03 05:12:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d335ac79-1ff3-3ffc-a823-7f409ef515b9 | -6.03552 | -46.02385 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89d871c3-a7a0-3b66-8986-4a7799ab7647 | -4.15029 | -46.78802 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90e7bb9e-497a-3cd3-92b2-04cca54acde8 | -6.79542 | -52.81144 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b010314-ab28-3212-b63c-56882efece1f | -2.13721 | -48.00942 | 2025-09-03 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bf0be1a-eb41-3d6d-8352-1c05fb320281 | -7.92598 | -46.54272 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d27ec1d-150b-375a-b5eb-204e22424fd5 | -4.89826 | -43.21564 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc68c85b-aeaa-3390-93c0-64f909683d38 | -6.7804 | -52.80425 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12e30d3f-4e94-330d-b6c0-9cb773444c0c | -7.89919 | -46.46506 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 326c6195-2239-3484-bf33-e4cdc0db22c7 | -6.3372 | -58.1816 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccfc47ed-c253-3ab8-a03f-cbd57ad708f9 | -6.80178 | -52.82257 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa84792b-de41-3ade-aca1-5cdec157591d | -6.94907 | -43.27585 | 2025-09-03 05:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99159200-1c76-3b35-8c44-9b36a5d53c27 | -6.43338 | -55.61138 | 2025-09-03 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fac00772-2bea-3978-bb53-3d8cf99289d0 | -5.92363 | -57.72438 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 850dd86e-8b52-39b4-ae40-71ff997032d3 | -6.80564 | -52.81983 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a592eb0-e46f-3a55-979d-9a25af3d7cea | -5.69801 | -45.94355 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08946312-01dc-3e75-b02e-ba39a5a04b94 | -5.8138 | -43.22039 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7202675c-e44f-3d58-8297-a5b6b4fcfe3e | -5.90807 | -57.71481 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a369cd9c-b832-3791-821b-924e938d1cfd | -7.80293 | -45.45364 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36f3aed5-d31c-3771-9260-0a8155a2d5ae | -6.70356 | -48.39561 | 2025-09-03 05:12:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 141b8fb6-6fb9-39dc-ae1c-184e87d0b057 | -6.70146 | -48.39674 | 2025-09-03 05:12:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8481664-0adc-3da7-801e-bd3529d09d9c | -7.93106 | -46.45996 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6dc3ede-7379-3bdf-8ac1-b1a6b5714687 | -6.8364 | -52.82943 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab97d8e5-580f-3a23-abaa-006a45252b06 | -7.48351 | -44.80423 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f88035f8-cdbb-3566-bfe2-d9774ffe1693 | -6.7068 | -48.39719 | 2025-09-03 05:12:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4756a80a-cf95-3df0-a57d-7e3827596f62 | -6.81901 | -52.81502 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ef78fd0-108f-3972-b5e4-10bc6dad3fa1 | -2.94155 | -54.8 | 2025-09-03 05:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26cffaba-b1a8-345c-8c4a-c0389c5ca029 | -7.71978 | -48.74347 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6459b6cd-9a2d-39f0-ad57-c86b580f6949 | -5.86644 | -57.7618 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a563734b-4aa6-3411-a55c-ba0d82910d1e | -6.87231 | -45.56794 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b25d5f3-4eb8-3c96-b0f2-b4194aa66858 | -5.862 | -57.76823 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9f84cf73-20f6-3e8c-b8cc-2ae46902b86c | -6.78286 | -52.81473 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f787ae15-1258-3fe0-872c-53640ae2052c | -5.10986 | -56.9629 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59a2b3f6-a7f7-3444-bd7e-5ead1ecb18ed | -3.81083 | -52.27211 | 2025-09-03 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 28821f26-c5d6-3457-a853-3dae352db933 | -7.48757 | -44.80531 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6259f55e-cd46-3426-a72c-6b56cc773b6f | -7.90834 | -46.44338 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4280418a-e8fd-337c-8c0c-e2a066c2e8d1 | -4.8935 | -43.21326 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ee5f4ef-dc7e-3c23-a71f-30f82e00d7da | -6.43053 | -55.60719 | 2025-09-03 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d90f2489-c28a-37fa-bf0c-da4e1bfa665f | -8.051 | -45.36361 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0dabbec8-0133-3e69-8875-a606d9dbbf2b | -6.13874 | -56.11752 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99384808-3a71-320a-b64a-433aed8b047e | -6.53919 | -44.5633 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb6c3f2c-5a67-325f-8664-4bcb0a6ebc5a | -3.22991 | -47.12348 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6892f0c-6d48-3ba8-bd4a-2baabf758e35 | -3.4845 | -48.44102 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 57de6a0b-8206-3d42-9a32-63eee5d46790 | -3.21897 | -47.12162 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 958335f0-94fd-3645-8c09-2644b0aca130 | -4.48554 | -48.11675 | 2025-09-03 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4b11d39-95d8-34db-b984-f3700f66103b | -5.90588 | -57.75017 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58f0b62f-c65a-3aec-821b-5cdd42b38bc7 | -6.42712 | -55.60666 | 2025-09-03 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 942e70e7-19b0-30d0-8b81-96d6b94cf736 | -5.91142 | -57.73676 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a3a55e2f-2baa-34dd-8bbc-c1de3526a200 | -6.3322 | -58.16996 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cd28e58-8a4e-3477-967e-9b0e7b5bd827 | -6.8543 | -45.54896 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc095a1f-dd21-3c22-a4a4-5c190eb26ecf | -6.70638 | -48.40025 | 2025-09-03 05:12:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 70dcc243-55a8-3f4c-ba13-f907eebbcb16 | -4.48032 | -48.11594 | 2025-09-03 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1700ce57-ae0f-39d1-ba3e-bd0180659613 | -6.40826 | -43.75717 | 2025-09-03 05:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fde0abf8-5837-3a1d-a2ec-3c4fe8cabe79 | -6.79691 | -52.80153 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45436e68-bd83-3e29-a0af-104a0d29e55a | -8.06489 | -45.35938 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d19d0001-1a12-37fe-a0fd-37c449803b06 | -6.80635 | -52.81491 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0058601-da53-38b6-9d27-89642bd0c28d | -6.17303 | -43.32085 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 90788c21-1124-3b94-ad76-ac91ac07ad2c | -6.23113 | -55.63369 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc5fcd15-e6bb-33ee-89cc-b7d1f415ff4b | -6.2611 | -57.8962 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de0e68c6-c60a-3544-9719-1fdd247e969a | -4.58061 | -48.01737 | 2025-09-03 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 225aa3bf-c1f8-30be-b52f-db481276c64e | -8.0193 | -44.11718 | 2025-09-03 05:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be3a0cde-4c89-335e-8c33-d8c20b3bdeb0 | -7.69489 | -48.73696 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 85ff0ad2-821c-32c5-90c3-4e1975eb84fe | -7.53004 | -47.44994 | 2025-09-03 05:12:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a3bc3a9-cc1f-374b-9230-9ae9bb4e385d | -7.89946 | -46.46442 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5fa0ee5-7f24-3a33-930d-ae1487af0600 | -6.33442 | -58.17754 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ef21ad8-5738-3093-b181-cdba079c1aa3 | -7.47988 | -44.83308 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 361eeae4-cce6-3b7b-947b-4467da50ad6b | -6.86267 | -52.78758 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18ab6289-7a13-323c-bd28-4d6b6dbe5a87 | -7.49203 | -44.82333 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b6e67812-7c5e-3ce9-849c-43a67e7ca98c | -5.91419 | -57.71933 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53a756a7-1710-3c09-affe-2ea4be879ebe | -5.11319 | -56.96342 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e69f30e-5537-32e6-93b0-40e3f151c5ee | -7.92869 | -46.43093 | 2025-09-03 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a46bbc85-faae-3c75-8c60-cb35bad7b45f | -6.8072 | -52.81332 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 060b6976-a229-3b71-ae06-bc9fbdaf4151 | -5.88755 | -57.75798 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ff5132d-703a-3b40-a5eb-e508710e4b71 | -6.47073 | -55.88889 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a31a0918-9904-3176-bcfd-c042ae9cc37f | -6.79317 | -52.82639 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c725f316-e49e-3858-bd18-b30b6d8da698 | -6.8396 | -52.835 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 197f842d-1bfd-3967-8f36-18714a6f2fb3 | -7.72298 | -48.72795 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d57a1cdd-f0a6-336c-8690-a04d965f705a | -3.92592 | -56.06301 | 2025-09-03 05:12:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5901b39-27ca-37fe-aa07-c28afcee1564 | -4.39393 | -49.34743 | 2025-09-03 05:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f7a9da1-f484-3652-9931-557e7bb3bfc3 | -4.89252 | -43.22038 | 2025-09-03 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 35357276-cb3f-3667-9e03-c9e2a62a7080 | -4.0229 | -49.7677 | 2025-09-03 05:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c0ebb30-7ab7-32f3-a9a8-654b60df1362 | -6.64892 | -45.9025 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acd8c1cb-74e7-3590-8e62-073fd993e516 | -5.56165 | -43.75724 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82ea8ea7-fa8a-3358-b713-3e9c9e6bc2aa | -6.94787 | -43.28423 | 2025-09-03 05:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a1dfc0cc-324f-38c9-bb27-e9467a6da151 | -6.52948 | -56.21057 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30c9fcdc-2ee8-3d23-96c9-f1dc078ae5eb | -6.53786 | -56.20093 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f8dc38e-5107-31d9-b518-ca2dd5b3e7ec | -6.83175 | -52.83378 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6400dc71-c7e3-31b3-861e-d7a14f54b257 | -7.4961 | -45.33557 | 2025-09-03 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8e1ba54-9df6-3620-8da2-2238dadec3e0 | -6.33164 | -58.17348 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48d34d01-786a-337d-8f50-9785c9807d06 | -6.80884 | -52.82555 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 165ac62b-e275-3a79-95ef-334d4ee4d11d | -3.22444 | -47.12257 | 2025-09-03 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3527c2b-c4ac-37c1-9dbd-08b3a43b9800 | -7.47913 | -44.83901 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9b057c8b-474a-3b65-bffa-504e3d540b50 | -6.79073 | -52.81588 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c2b172b-288f-37b0-9af3-70ea187d6234 | -4.47509 | -48.11518 | 2025-09-03 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b638459-d3eb-37df-bbc7-554396a1e6d0 | -7.90771 | -46.44809 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef22b0bd-c2b6-3f2c-8e66-6928633a70a3 | -6.83029 | -52.84375 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c395c317-3c72-3b19-96e5-0cccd052f10e | -7.93404 | -46.53401 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README83.md)
