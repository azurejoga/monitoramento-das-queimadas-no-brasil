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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd3d6437-f2b2-3d40-865e-2df97038e606 | -9.16211 | -46.9882 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6650255d-c56e-3da1-94cf-83b033d3ad0b | -9.15873 | -46.98769 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 282a8618-5008-3482-8602-de7ef2f6f4a3 | -8.92817 | -47.05289 | 2024-10-16 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df9d5b1b-555a-3263-9482-0edfc1793209 | -8.92762 | -47.0565 | 2024-10-16 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90788c4c-ad0f-358d-9452-4e79f6ff7d25 | -8.92426 | -47.05598 | 2024-10-16 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee2ce001-a6da-3b41-85a3-88664043ad35 | -8.9055 | -46.83101 | 2024-10-16 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8111d928-5624-3fef-adce-6313ff258eb6 | -8.87677 | -46.83783 | 2024-10-16 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d536b5d3-ed85-3b26-ab2e-9fdd92f60aec | -8.87621 | -46.84148 | 2024-10-16 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da17ec0f-90fb-39e0-9830-a77791cf409a | -8.84317 | -46.92185 | 2024-10-16 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd110d13-d24c-35ae-a336-c1dd8385deec | -8.67816 | -47.08781 | 2024-10-16 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1a6024c-a0eb-34eb-bd5e-eed58dacfb3d | -8.67761 | -47.09138 | 2024-10-16 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 758cc9e6-4f93-3119-b4d3-48aa0c3f25df | -9.97596 | -47.34605 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32f88155-1118-37ff-a10e-b0302f06421f | -9.96435 | -47.39948 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ead6a1d-8241-3e6f-910b-5a45eb30ba8d | -9.9638 | -47.40307 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92e19b85-4e3c-350d-bcf7-72a351cdb2ff | -9.96209 | -47.39178 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16bdec57-e1bc-3b79-adb2-44a8b922ab78 | -9.96155 | -47.39537 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13275498-b359-3188-b872-780226efdd00 | -9.96094 | -47.3769 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 032a2a98-92fa-3d28-bc2f-2642c8194dac | -9.95929 | -47.38767 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8fdf64a9-8ecd-3e77-8893-c03a075515ca | -9.95874 | -47.39126 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7691125-cfd1-34cf-99f5-a14fb67a1089 | -9.95758 | -47.37637 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 890c9266-66dd-39e3-bf1d-a46822509e4f | -9.95703 | -47.37996 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 973e5aec-3967-3f36-9d45-27fdf6685d47 | -9.93957 | -47.33675 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c06efe00-7530-35c6-b2f4-e960e8975263 | -10.02849 | -47.27286 | 2024-10-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c66951b2-ad4c-302f-8120-792a6a9845db | -10.26325 | -47.30487 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| caf3737a-9a1b-392f-bd87-172348b1e0de | -10.2627 | -47.3085 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47ee2310-c730-3127-949b-c07c4ad75827 | -10.25933 | -47.30797 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe18f7b1-c787-36c4-aa5d-1f97b3fcbaf5 | -10.25812 | -47.30402 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eee0e0c-8942-3b41-8885-7aa9ab326ef5 | -10.25756 | -47.30765 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7b4d38d-3137-321a-a246-493c857aa072 | -10.25531 | -47.29987 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8795a059-2a37-34b0-bc87-5fc29131d34f | -10.25476 | -47.3035 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b5feab0-8e3d-38fe-a1fb-ef8187b729a2 | -10.2542 | -47.30713 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 230cbcbf-846f-332d-b88a-bf2051deb124 | -10.25307 | -47.29208 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20c70049-2506-38ac-9f64-b0e92738495b | -10.25251 | -47.29572 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 94a037c3-d246-364c-a429-04aaa93e9594 | -10.25195 | -47.29935 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 445e1427-2bc6-35e9-9e47-ed06b37f11a6 | -10.25139 | -47.30297 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 700c60a6-1388-3cad-93d9-62d15533874a | -10.25083 | -47.3066 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 294c9a22-2260-38f6-8cad-523348d2ab87 | -10.25026 | -47.28792 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e234f122-f65a-39b2-921b-3e47c8cdc039 | -10.25017 | -47.19854 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d531165c-cbf3-312a-91ca-625d1bd3af99 | -10.2497 | -47.29156 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c14041c4-6239-3f54-9efb-67db97616516 | -10.24961 | -47.20218 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3d9f790-9b2e-3e76-9fe6-60c208f0fcfd | -10.24914 | -47.29519 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8ccfa2a7-bc14-3fbd-a8a6-c4b7ec31ebcc | -10.24858 | -47.29882 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fd7c1278-3d39-3e42-b5b1-8ad462fa7812 | -10.24802 | -47.30244 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a5d6a2b1-a021-3a31-a589-93a4e625ccdd | -10.24747 | -47.30607 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 91526d58-9bcf-3d48-b54f-afd3d9949a3d | -10.24745 | -47.28376 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 734da4b9-dcc0-3556-8587-d29ca855bf1d | -10.24689 | -47.2874 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfdc6c4c-35ce-3278-a206-98002a9f8bf0 | -10.24633 | -47.29103 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ca4aecc-1046-30db-885c-38ec212334c7 | -10.24577 | -47.29467 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9028e03d-1c38-31a7-89b0-4c3e9430ede5 | -10.24521 | -47.29829 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06b34c10-e80b-37d1-92e7-fcd0e6c6e392 | -10.2452 | -47.27596 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a3aade6-964e-3f18-9a7c-7b58bb69ea7f | -10.24466 | -47.30191 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc7b9d5a-2417-30e7-814b-1c7b2c4bde09 | -10.24464 | -47.2796 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d209175-3449-3553-af2d-f5a26425ce10 | -10.24408 | -47.28323 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd17a08c-d6ae-3506-8270-745f5c6cbfaf | -10.24295 | -47.26816 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78be1b3a-bcd0-3f43-8c3f-93dc0b845561 | -10.24239 | -47.2718 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ca5c861-a200-379e-894b-77837924b606 | -10.24185 | -47.29776 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e791f06-acf7-329e-ac37-088926ebcfcb | -10.24183 | -47.27544 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 326dc665-a1a6-3766-adaa-98a34db84901 | -10.24127 | -47.27908 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd7a7d70-a6b7-3a0e-ac51-54e8e47dd8af | -10.23217 | -47.20327 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4cdab90-fb2b-3a7a-93ec-19cadf561b21 | -10.22768 | -47.21004 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16f13f24-3d33-3371-bccd-e2311f1f04c9 | -10.22712 | -47.21368 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d030131-dfe3-3570-8212-6e13fff6326b | -10.22601 | -47.22095 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03aa5553-0abb-3910-beaa-2094a63cfc95 | -10.2243 | -47.20951 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 836342b8-caaf-3d99-8779-248424ef2c07 | -10.22375 | -47.21315 | 2024-10-16 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e80a254e-4504-39cc-9c18-b37015e30d5c | -12.15804 | -47.52298 | 2024-10-16 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9cb90b5-f345-39b2-a754-899405b7a4c8 | -12.05117 | -46.69889 | 2024-10-16 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8bb9670-7a25-3eb3-9431-d8533ab998cb | -12.05059 | -46.7028 | 2024-10-16 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f26ee8b-efe0-3e47-9eed-98cb20d019a7 | -12.04769 | -46.69836 | 2024-10-16 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b52cc072-2e97-3b97-809a-b2f2fc658e4e | -12.0471 | -46.70226 | 2024-10-16 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 70f49ce5-cdf6-3533-a76c-e49a01003436 | -12.0442 | -46.69781 | 2024-10-16 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1aad7794-f555-3746-a1d6-50ebc46fab00 | -12.04362 | -46.70171 | 2024-10-16 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fd446dc-07a8-3b24-ac99-fa312b214bc6 | -11.79974 | -47.39625 | 2024-10-16 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3858ae23-f374-3ee8-b84d-7fb09e3fa456 | -11.79918 | -47.39995 | 2024-10-16 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8bc87033-37c9-3cf1-ad44-c912d185c095 | -11.79862 | -47.40365 | 2024-10-16 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4c1c13d-ebac-3fc6-8fcc-f40a79dd686b | -11.79579 | -47.39942 | 2024-10-16 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6196d07a-d8ee-3318-9864-fe7589fc56db | -11.6389 | -47.58219 | 2024-10-16 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 131435e6-4ab2-3e00-8912-81f69b919efd | -11.63552 | -47.58167 | 2024-10-16 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09a64ace-edc7-3b85-91ac-dbb2629964c8 | -11.63497 | -47.58533 | 2024-10-16 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de246ba0-94c9-3278-ab73-2f0485ff0029 | -11.6195 | -47.22141 | 2024-10-16 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 376c373d-e254-392e-8d13-36b416050904 | -11.61894 | -47.22514 | 2024-10-16 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e757347-e70c-3077-b5bc-74bd3fe9da99 | -11.61609 | -47.2209 | 2024-10-16 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f3e172d5-8d11-34a6-8c54-6e9cdf206010 | -11.61554 | -47.22462 | 2024-10-16 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 206e08b5-045e-327d-8e69-be5898ff5453 | -11.59414 | -46.76018 | 2024-10-16 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38dc3356-0d12-39e4-8318-134e6d5ef8fa | -11.58779 | -46.75529 | 2024-10-16 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 126940e8-9fc4-38b9-85bf-5d1ceb99880b | -11.31638 | -47.58567 | 2024-10-16 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a867a1fe-16b9-3c2d-824a-da5b2b1ae723 | -12.52744 | -47.83493 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51fd18e6-29d7-3b70-a3a8-06b5ea728f63 | -13.38015 | -46.95085 | 2024-10-16 04:32:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10153bb4-2105-3d83-b90c-a276c0d9231f | -12.69813 | -47.63171 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cdee098-a27b-37b6-be88-f0206644f5f1 | -12.51316 | -47.42066 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2994eb8b-a5fd-3cd3-9ce5-bec604d05128 | -12.50976 | -47.42013 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c6684da-0587-3f94-a399-3b06dd75a8cb | -12.50919 | -47.42385 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2934f3db-cef5-3b17-b01a-46447430789b | -12.48809 | -47.28582 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| caaacc9b-44cc-3a77-9e53-f1a44c25d7dc | -12.48752 | -47.2896 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f4a59ea3-0d29-355b-b54a-e8bebe4fd4b4 | -12.48467 | -47.28529 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c910ec73-0df4-3ba0-827e-2d147bad10d7 | -12.4841 | -47.28907 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 12dcc0c4-236e-3a57-8ce1-675831917b47 | -12.48068 | -47.28854 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 53bb38de-3053-30b4-8f34-b6e1f33db524 | -12.27684 | -47.646 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 157c1228-924f-3a64-8f6d-6a3372e68360 | -12.27346 | -47.64549 | 2024-10-16 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f5e97e7-b38d-3b18-9e36-a32e8473fef6 | -6.90522 | -47.31507 | 2024-10-16 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f1c37ba-0cfd-3222-9d89-030fd9cebe72 | -7.91138 | -47.83261 | 2024-10-16 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README51.md)
