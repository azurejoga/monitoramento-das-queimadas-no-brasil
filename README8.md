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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9ff37d1-8e8e-3173-be0c-1286db48f7db | -6.56954 | -43.92348 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30f44eef-1262-3e48-be92-f8894281af44 | -6.6381 | -44.65395 | 2025-10-13 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e8c1e73-ae87-3f33-b66d-7258e4ff4adb | -4.48258 | -44.93253 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3e6cd2df-914b-386b-84e9-e65597d6cc0d | -6.40559 | -42.53459 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| db7d1ee2-c606-3c1d-8ec7-90df049eeaa8 | -6.21107 | -42.67899 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e5d754c-c9e6-3766-9149-358a453d8580 | -6.44674 | -44.24223 | 2025-10-13 03:53:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb94150e-1f2f-3ac7-a246-9231390ed4a2 | -7.04986 | -41.52334 | 2025-10-13 03:53:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 21dc732e-a2bc-338a-9490-d1928f4f68c6 | -5.25102 | -45.59695 | 2025-10-13 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39e6d0e4-c6c5-3a40-9e4a-69a7bd0d80e3 | -4.48097 | -44.94201 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a32b99e5-3e77-3064-a130-85cddddfb930 | -6.48469 | -42.06063 | 2025-10-13 03:53:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8967b80d-769a-3382-989d-5851cb2f1a12 | -7.15557 | -42.18438 | 2025-10-13 03:53:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d31770f-3717-3c83-ac17-53488dfbcc62 | -4.4732 | -44.93356 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 95af8b10-14d7-3fbc-8ab5-0e310e50940c | -7.35486 | -43.85188 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73425e24-5903-364c-b5fd-cc18a8580f7f | -4.83819 | -41.47825 | 2025-10-13 03:53:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e5ac6f4f-675e-3514-83e3-bf57bf5421f4 | -5.89626 | -44.73564 | 2025-10-13 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02e713a8-5aab-37c7-933c-8b5167f20da3 | -5.64552 | -42.78598 | 2025-10-13 03:53:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 00284449-1077-3302-a828-22ee6029dd9c | -4.47717 | -44.93652 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 09c9ff34-b5d5-32e0-847f-972416423841 | -3.13123 | -50.20551 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e19c830f-9676-3ce2-a1d0-6f82b224b3a5 | -5.94103 | -43.93904 | 2025-10-13 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbd088cd-780b-34fb-b85e-13734bb81e52 | -3.60733 | -42.74515 | 2025-10-13 03:53:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 881045c2-11a7-3892-8e14-448b930dcfc6 | -4.47242 | -44.93834 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9fe545f2-56ca-380b-b719-bb2791410282 | -5.62457 | -42.57582 | 2025-10-13 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ec5bd7e3-3e98-3e0f-b1ca-482d1eff8ffb | -5.93243 | -40.8926 | 2025-10-13 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 44d251bb-086f-3de8-9956-0356432aa2e9 | -6.24175 | -43.00549 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 15a61ce0-ff5c-3831-9c13-1c39e17a3876 | -5.58205 | -41.10564 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| abd9fe1b-531a-34df-9a1f-6948b51057e3 | -4.46796 | -44.93509 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9c5887c-d322-30c1-a555-601fe15c19ea | -4.91179 | -41.53453 | 2025-10-13 03:53:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 13a7b118-5894-31fa-a4ec-738952ad17ae | -4.47014 | -44.95004 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb4edd17-ef14-3b51-8697-8f4d44ed8df8 | -5.83621 | -42.31105 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b4a8b27e-9254-375d-9443-4e9ecb22c615 | -6.19952 | -42.67706 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 37a468af-513f-3475-94ac-6ca37840688d | -7.50343 | -42.14713 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 04c7a888-f6d5-3f52-bf9b-0d2e10649671 | -7.51598 | -42.16261 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4b56291c-fb27-3ab6-b37a-11a253f3cbe6 | -6.28107 | -43.01174 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0abae566-86b3-3cda-a36b-c02fc38d25c4 | -4.46878 | -44.93029 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0abb6d57-916f-3cf2-8ac8-2b060b112086 | -6.40936 | -42.5354 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| abb95d58-8d07-381d-a187-5acc26ee6efd | -5.92146 | -45.42662 | 2025-10-13 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3c8266e-b4a9-3948-ad46-f2fa31e3f2e4 | -6.21507 | -42.4882 | 2025-10-13 03:53:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 504a2672-40f2-346b-a6a3-96fb97bad050 | -5.57477 | -45.27873 | 2025-10-13 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 135efa38-9e65-3eaf-b53d-0fc682add134 | -4.46635 | -44.94448 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78fce437-93ac-3771-9e17-758ab743ea17 | -2.24847 | -47.87197 | 2025-10-13 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0c6354f0-e8ee-3631-ac92-60e6df23c9ef | -7.43301 | -42.97081 | 2025-10-13 03:53:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1070dae9-6914-33bc-958e-be60d95396f1 | -7.35117 | -44.09204 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bac7ff75-f91d-3583-b893-89c9512997b2 | -7.26957 | -42.95426 | 2025-10-13 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c2aee944-44a3-3d36-8aa9-6f74c1877ab5 | -5.1041 | -43.20573 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9b52a9f0-42dc-3e9e-b2b2-744d00d6b1d8 | -6.42301 | -42.54742 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 484c2d14-e144-3718-99f0-14a84f4ef8c6 | -4.48557 | -44.94274 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4448e686-c57b-3b61-b0a0-4276b57ce248 | -7.14556 | -41.7171 | 2025-10-13 03:53:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9dddae05-bcdb-3b86-8a98-7969249dcbe6 | -4.48477 | -44.94748 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aef7b732-9cb9-33f7-bad6-aae5293be688 | -5.73849 | -40.76711 | 2025-10-13 03:53:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd99c95d-73c3-3aac-a6ac-a9a7dccc4982 | -7.37914 | -44.0779 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d28175d-e516-3555-959c-b201419c61ed | -2.24887 | -47.8691 | 2025-10-13 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2a2fa931-685f-3e2c-aaa0-f000f4f6b530 | -5.1047 | -43.20216 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| df98992b-fac2-3fee-85b6-ccc934a8a7c3 | -5.62524 | -42.69083 | 2025-10-13 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e1f38945-6f2c-305e-9e27-8ff87fd3d750 | -4.46705 | -44.9423 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93b08902-4dd4-3cc8-a59c-1736d10fc3ae | -7.27647 | -42.96045 | 2025-10-13 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 065ff9e8-d7f1-3c0e-9dd5-b9022342736b | -5.07037 | -40.46982 | 2025-10-13 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 80ac22e0-4fd0-3f5b-bf17-8825e1c55517 | -6.42219 | -42.5523 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b8a37e06-7333-3875-8f86-483574dd9688 | -7.51669 | -42.15822 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e250640d-da1e-3307-a19d-5e6e310ecbe3 | -5.81719 | -44.03304 | 2025-10-13 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5b6cfe8-3b1c-3e0c-b3ac-5ada4fcb1bbe | -6.76892 | -39.07367 | 2025-10-13 03:53:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a3d56ca-07e2-3bfa-9211-10572eaee7ac | -5.35269 | -43.42144 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df6e7f88-4d7d-3861-b64c-712c2e82345d | -7.68993 | -41.47229 | 2025-10-13 03:53:00 | NOAA-21 | VERA MENDES | PIAUÍ | Brasil | 2211506 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e2c8d916-9d58-30ee-a2b2-168b10c2ca89 | -4.28571 | -48.5731 | 2025-10-13 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4bf0599e-8b2f-3c6e-a6a5-09e4e0900af3 | -6.17567 | -42.54253 | 2025-10-13 03:53:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2a128414-81be-3a9e-a0a3-66e07809ab94 | -6.57962 | -45.97681 | 2025-10-13 03:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 227be68b-956f-3861-a02d-dc44a192a438 | -6.27817 | -42.98034 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4add4586-094e-3bc1-bc59-c292e6ce1a1f | -5.21977 | -50.94836 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b5cc49f-44fe-3036-901d-9a451d7a6844 | -4.86386 | -45.73288 | 2025-10-13 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfc34050-5117-382b-9646-1c4527f35122 | -4.86734 | -45.73537 | 2025-10-13 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2b3ce05-1578-3298-b7dd-4b3cd603412f | -2.26424 | -47.84929 | 2025-10-13 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48f1636a-6982-35fb-9740-17618e084f6c | -6.73711 | -42.08083 | 2025-10-13 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 628fc91f-d0ab-38f6-9312-db23ca5aded0 | -6.23696 | -43.00999 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7aea08ee-9375-3875-861f-b6866fc243f9 | -6.58264 | -43.92162 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 529e2743-dccb-3ca3-a83a-42ad539c076d | -4.70401 | -46.01317 | 2025-10-13 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61e76fc6-0467-36ea-9f43-223e243e1336 | -6.67438 | -46.02777 | 2025-10-13 03:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fc9b380-8455-3e53-8518-11548c57be60 | -6.57847 | -43.92102 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5631a001-045f-391c-bc5a-84e2d04d4542 | -6.23609 | -43.01516 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 47720408-2c39-3703-8f91-729a28f67b20 | -6.74701 | -42.15959 | 2025-10-13 03:53:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ce442260-5a31-3873-b2a3-e3e6dff355a7 | -7.21349 | -35.78026 | 2025-10-13 03:53:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31d17bc9-f593-3f5f-8dc0-7feed51758cd | -5.8332 | -42.30569 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1ff1bba6-bef1-333f-8fc4-70bdc2b5ab16 | -5.06689 | -40.46926 | 2025-10-13 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 75e20859-127b-3b22-9a4c-97a382eafad2 | -5.74548 | -40.7682 | 2025-10-13 03:53:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9664e120-cedb-3967-8f43-65239857233d | -6.58534 | -44.62236 | 2025-10-13 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d32e9e1-8c01-3fae-9254-ce9c92d81532 | -4.39828 | -43.47436 | 2025-10-13 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4047bcf3-aedd-3fb5-976b-f6d9039ae65c | -4.48009 | -44.94934 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 75a3d73d-c19d-3f38-bbc4-bfea3c05ca90 | -5.9095 | -43.49091 | 2025-10-13 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d71b9aa9-6a05-315c-828c-b6f4f864e6c7 | -7.6989 | -42.3755 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3c457882-9708-3ff6-9cab-0167d75a9e9d | -3.61135 | -42.74582 | 2025-10-13 03:53:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 585e5fc9-c102-3136-8f2e-c9b11d461b8c | -4.91248 | -41.53017 | 2025-10-13 03:53:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 63073542-ee93-3dc3-a6b8-24915337c9d5 | -6.76501 | -44.65175 | 2025-10-13 03:53:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3ceed0f-3393-352a-9059-02f70e91c5a8 | -7.21289 | -35.78424 | 2025-10-13 03:53:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 893a15c1-cbcc-3c57-9cc6-862621915b55 | -3.72656 | -44.40665 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db0f2063-c902-3325-b492-77926a5d0b7f | -6.21026 | -42.68391 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5ec86cd6-40f8-316f-9989-f10e56cd0b52 | -3.22606 | -50.05056 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f97dd89-f2f9-3bed-8941-ff8d959e1efb | -5.62913 | -42.69146 | 2025-10-13 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 490db157-f1fc-32a7-9c98-41f8de19ad5f | -5.31402 | -43.4265 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84e1363d-3f3c-30db-bc73-b8dfa100b2db | -5.57557 | -45.27395 | 2025-10-13 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0c82da7-8cea-31e9-8458-8f1089ef8dc1 | -4.4747 | -44.95339 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 611ef78c-1f2e-3f35-a51d-3888ff70612b | -5.63383 | -42.68718 | 2025-10-13 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| aa1922f8-72cd-32c2-842f-d2be84a53c3c | -5.53449 | -46.49377 | 2025-10-13 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README9.md)
