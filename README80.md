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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c15dae13-ce4a-39a1-a058-507c4da587ae | -6.40104 | -41.60487 | 2024-10-15 12:44:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 4674131a-b74e-3a0b-a378-d76c687b1362 | -6.44708 | -43.11834 | 2024-10-15 12:44:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9d1f89c5-3a6d-3081-a87f-d584c66238da | -6.49024 | -39.94781 | 2024-10-15 12:44:00 | TERRA_M-T | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 108f2971-48ff-3758-bdb6-45a7992e3dac | -6.9414 | -42.77764 | 2024-10-15 12:44:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 619ae027-775e-3a79-bd23-0cdfe531c66c | -6.94328 | -42.76361 | 2024-10-15 12:44:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 053b7760-f32e-3aa1-ba87-c93cbea230ad | -7.07986 | -43.03049 | 2024-10-15 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| bec177ae-5835-342c-9e0a-64d5327cd35d | -7.08078 | -42.67295 | 2024-10-15 12:44:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 73516570-8a27-3144-a912-a58d1ce7625f | -7.09062 | -43.03194 | 2024-10-15 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| b0b0c0c0-bbb5-319f-97f3-798ee62d945b | -7.17601 | -42.64803 | 2024-10-15 12:44:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| f02e5b24-37d6-3a47-961a-d41d14eb5cbe | -7.32861 | -44.28034 | 2024-10-15 12:44:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 1b1e7f15-e3ff-3563-9b8e-b4616dd86597 | -7.43563 | -44.24467 | 2024-10-15 12:44:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 5da212a3-9d01-3dff-9734-2fda09bf4046 | -7.57209 | -44.96008 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 7576e4b3-a10a-3542-82ea-9356b2a286b9 | -7.69078 | -43.1831 | 2024-10-15 12:44:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| d99ede71-c2b2-3c39-8f68-9449db09214c | -7.69256 | -43.16965 | 2024-10-15 12:44:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| d6ff7dff-e71c-3420-b1f5-6f18c3778d7a | -7.71053 | -43.27992 | 2024-10-15 12:44:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| ab10110f-7d76-392e-bc8a-dd591be6db72 | -7.72045 | -44.8656 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b8a55af1-99b4-35d2-be7d-053203850dee | -7.74639 | -44.5808 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 53b7210b-5222-320e-beca-a0381c78fb18 | -7.7479 | -44.56999 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 2f91912f-2b12-37d3-bf38-21292245c84d | -7.75086 | -44.54881 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 1e1be661-547b-3d72-9eae-4be2428ce959 | -7.75238 | -44.53796 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b198d1a8-c776-33a7-b0e4-38350982d1af | -7.75552 | -43.30525 | 2024-10-15 12:44:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| a305cc98-c242-3dfa-a530-f392c4672d6f | -7.75588 | -44.89176 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 679c7ef6-4af4-319e-b119-f51b7cc0590a | -7.76217 | -44.53917 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 377e1e09-221b-31af-9b5a-42c1aa7eab98 | -7.76526 | -44.53443 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 0713ec03-7550-350b-92e6-c635eaf96cfa | -7.76545 | -44.89307 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 7f2e9ba8-7a7e-3587-b656-0f8dabd72ac0 | -7.76617 | -43.30675 | 2024-10-15 12:44:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 338c1398-c03d-3c33-92d3-e2ae3a7e939b | -7.77504 | -44.53574 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 44429873-e544-39e9-968c-2a93fa59e85f | -7.90274 | -44.49234 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f8c35f12-d5ea-32fd-937c-e570f53e139b | -7.94885 | -44.52039 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| a5346d3c-92d2-3a3a-9ac7-bd5d500fc0c6 | -7.95008 | -44.52662 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| a066a48a-d41f-3cc5-834e-e01440d9a808 | -7.95987 | -44.52808 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 728.9 |
| 17b1b60d-d325-3e77-9f29-a0a3c9b5434d | -7.96139 | -44.51682 | 2024-10-15 12:44:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 231.7 |
| 63df7af7-93b3-3eed-9129-f16eaec63954 | -7.98167 | -45.45818 | 2024-10-15 12:44:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| fe872617-5533-3d00-a689-67ab27a9dafb | -8.06511 | -45.38451 | 2024-10-15 12:44:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 2645a8ef-f37a-379d-8b88-6d6ad2267ba4 | -8.2479 | -44.87186 | 2024-10-15 12:44:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 10fc5fca-d972-3657-8ded-b11661d040bf | -8.28279 | -40.41273 | 2024-10-15 12:44:00 | TERRA_M-T | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 156c4329-449f-3504-9c0c-e91d73eae08e | -8.32631 | -42.79132 | 2024-10-15 12:44:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 6efd5862-b957-3874-acd6-8a234cb61cb7 | -8.32824 | -42.77676 | 2024-10-15 12:44:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| f9b09d51-12bb-314d-a0da-0c9175ca2b49 | -10.02057 | -47.25271 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ab58a4ea-2c6e-3ad2-a88a-caee3fd03a38 | -8.34333 | -42.74909 | 2024-10-15 12:44:00 | TERRA_M-T | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 2ef75910-6cb5-3ee4-9f22-b952f1f61479 | -8.48626 | -41.56975 | 2024-10-15 12:44:00 | TERRA_M-T | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 21ff62ce-80fd-3254-bb7a-a0d0dc21b49f | -8.48859 | -41.5517 | 2024-10-15 12:44:00 | TERRA_M-T | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 921a262b-c465-3a5f-bce1-24cf4043018b | -8.59312 | -40.40631 | 2024-10-15 12:44:00 | TERRA_M-T | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 24.6 |
| ae8c319f-08af-3b0e-bed3-1e69c2077c18 | -8.59682 | -40.4229 | 2024-10-15 12:44:00 | TERRA_M-T | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 31.7 |
| 888eb0e2-e04b-3af8-87f2-12141af11a4c | -8.6339 | -40.81709 | 2024-10-15 12:44:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 516f943d-7586-3518-8fa8-b7c39366f24d | -8.63421 | -40.83319 | 2024-10-15 12:44:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 2977b040-bac5-3b98-8ce7-ac6eb94a5343 | -8.63702 | -40.81187 | 2024-10-15 12:44:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 24.7 |
| d13d039e-8de4-38db-8d02-fea9c68147a3 | -8.72265 | -40.72604 | 2024-10-15 12:44:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 32.2 |
| b6735004-3bad-336e-b536-ee62206936a1 | -8.72703 | -40.71995 | 2024-10-15 12:44:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 9f7c4f94-a382-3717-9ef3-b089e3d0f7a4 | -8.78091 | -40.99567 | 2024-10-15 12:44:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 71.3 |
| d7352d08-f0bf-3e65-85c1-4d7337761f32 | -8.78303 | -40.99026 | 2024-10-15 12:44:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 131.1 |
| 0f52beb2-804f-3408-9ed2-1127d5268bf2 | -8.78345 | -40.97496 | 2024-10-15 12:44:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 835c42d1-42a6-3278-89df-c068d9ab04c5 | -9.41806 | -45.50971 | 2024-10-15 12:44:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1812b67b-a15b-3b6a-a42c-42cb777765b8 | -9.44364 | -44.19895 | 2024-10-15 12:44:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| af939cba-7621-3c00-a4ad-cd41b0bc344a | -9.44531 | -44.18671 | 2024-10-15 12:44:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 522.3 |
| d5b9c7bb-43bb-366b-851b-a8295cc85876 | -9.44696 | -44.17456 | 2024-10-15 12:44:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1ec9146f-29de-34f1-8f52-04cb67ddb87e | -9.45028 | -44.15011 | 2024-10-15 12:44:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1aa28565-263b-37b8-9b78-22028d48eee7 | -9.45555 | -44.18811 | 2024-10-15 12:44:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 149fd150-3676-3d56-817d-8b76b4f389ad | -9.49017 | -42.007 | 2024-10-15 12:44:00 | TERRA_M-T | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 08449fb8-0bfa-3116-b610-91582afd9602 | -9.56518 | -43.49045 | 2024-10-15 12:44:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 6225e4ce-ce2d-3352-9c18-a387b6070410 | -9.57423 | -43.50544 | 2024-10-15 12:44:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 65.2 |
| c628576e-31e5-37aa-8a18-2dcd6c30ef84 | -9.57598 | -43.49195 | 2024-10-15 12:44:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 2a226392-3cb2-35fb-b476-34bdd1001c40 | -9.76683 | -41.98783 | 2024-10-15 12:44:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| e07d324e-00fd-383c-9bad-a190aa0d350a | -10.02949 | -47.25396 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b8c6390e-1ddb-3a0e-b0a7-62376fb8fc29 | -10.03711 | -47.26425 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 580b2a5b-ef49-37e8-80c8-d8e86d606c5b | -10.03208 | -47.23586 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4d42d84b-11fa-3712-a0dc-67f995c41e12 | -10.03078 | -47.24491 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 27db0c9c-7d2d-3163-9270-6d024ae293fe | -10.0384 | -47.25521 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| be9d0cd9-844e-3651-ac2a-8dcefa2a51b9 | -10.04813 | -47.63916 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0a02efa9-155f-3106-80f8-04ec0af59d1f | -10.04992 | -47.37372 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| ca7c68aa-c44f-368c-b9cd-31c5525cf211 | -10.05571 | -47.64938 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 6db2ae4e-9c59-3644-a733-7e919fa68421 | -10.05701 | -47.64042 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| bc392ef8-753a-3a5a-95b8-3c4288c8e6ec | -10.05942 | -47.68648 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 14340174-12fa-3046-ad50-5b4f4b3233af | -10.06459 | -47.65065 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dba53cc8-3b0a-3ae0-ad0b-c40a1def077e | -10.08564 | -47.31447 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| fcd4b748-92f4-3626-a729-3e1dc7c6373d | -10.11289 | -52.04172 | 2024-10-15 12:44:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e5389a02-bbd2-3d81-bad4-b4a428b5ae36 | -10.25441 | -47.29559 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| ecce2cb0-cda5-3455-88db-43a56d4d0589 | -10.2557 | -47.28653 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 3936823e-30b5-3095-9ddf-78fa025c4593 | -10.25698 | -47.27748 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| c755f1b0-dec0-3709-bc19-67962b96a605 | -10.26332 | -47.29685 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 304.9 |
| 5a46378a-c3b5-33a1-a3c1-b7248d3f4397 | -10.26461 | -47.2878 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c1639b21-4a6c-3dae-bc08-7b98a12709f1 | -10.40123 | -48.19632 | 2024-10-15 12:44:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 48a38ba8-eafe-303f-b00e-c285a9d6d268 | -10.01928 | -47.26173 | 2024-10-15 12:44:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| d9c118ed-1786-32a8-ae89-9bc3b127e0fe | -10.40254 | -48.18735 | 2024-10-15 12:44:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 73a998f9-ab32-3963-a16e-0066ce30c940 | -10.45059 | -47.85588 | 2024-10-15 12:44:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| ba464a80-6cf2-3b77-9d9b-eb6708f33c9d | -10.45189 | -47.84692 | 2024-10-15 12:44:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 410075ed-a34a-3bca-b8a2-e189fe22face | -10.65781 | -47.69675 | 2024-10-15 12:44:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4e211102-b367-3b22-854a-1af122b878d1 | -10.82001 | -47.78743 | 2024-10-15 12:44:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 83bd71e4-f8e8-3b05-a42e-55273edb0e8a | -10.82607 | -49.25521 | 2024-10-15 12:44:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1cb1fa5b-cc74-3916-870d-0c63912341b9 | -10.82746 | -49.24586 | 2024-10-15 12:44:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 3da2a79f-5cc8-3cd0-8cb2-c8d74668a3a9 | -11.12319 | -54.01384 | 2024-10-15 12:44:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 565cd240-1a2e-3d6c-aa04-2e1c81d4e36f | -11.93671 | -46.59246 | 2024-10-15 12:44:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3b9cfed0-566c-3af7-a71f-87859c6381a6 | -11.9459 | -46.59371 | 2024-10-15 12:44:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 7936947a-f2c1-33cd-8883-6986809a01e8 | -11.94724 | -46.58405 | 2024-10-15 12:44:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7d0cc50a-2bd1-3b0b-9293-6b5538e0055b | -12.05068 | -46.70336 | 2024-10-15 12:44:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 569923e4-ace4-3ca9-ad96-00496ae884e5 | -12.05984 | -46.70465 | 2024-10-15 12:44:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| daebe63a-58c0-3c9b-87f0-b223fa678561 | -12.19022 | -46.75479 | 2024-10-15 12:44:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8bf9549f-dc9e-3d67-bba5-c773617fee3a | -12.28507 | -46.73468 | 2024-10-15 12:44:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| e6efed21-9ae3-3db8-8cf2-71c0f006b950 | -12.28641 | -46.72501 | 2024-10-15 12:44:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| fc704490-ceed-3e2a-9337-3bc179b92339 | -12.29424 | -46.73596 | 2024-10-15 12:44:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |


[Clique aqui para ver as próximas entradas](README81.md)
