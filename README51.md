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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a7b35cb-d607-35b3-8c13-695b02f8ed5c | -7.58078 | -43.44246 | 2026-09-19 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ea4bb49-bcdf-3231-89ab-92f4e220ebf0 | -3.82137 | -50.74705 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 263023fb-4487-3636-a186-6cce9709a56a | -5.86541 | -52.04349 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b288974-023f-313a-9df6-69fdbd2b033d | -3.72546 | -54.64697 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68f5ec2d-393a-3c9a-aeef-195e071bfb15 | -4.48785 | -55.49409 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4f123a1d-dd83-3fc5-988f-3ca826f5a17e | -5.86746 | -52.0442 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe3f9e19-f2a1-3a8f-837c-1a69ca1d8730 | -3.56012 | -50.05772 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78239ff8-f060-36fd-9612-7d2692c58014 | -6.66329 | -50.9296 | 2026-09-19 04:38:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b40d336-0a89-365c-bd24-fe53d31df324 | -8.68101 | -45.42834 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a6782f3-d873-3254-b983-20049b58face | -4.5614 | -42.97312 | 2026-09-19 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c3e3398-5db8-326c-b236-4c424b872fc5 | -6.09193 | -44.30667 | 2026-09-19 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee5ea39a-6455-3687-8699-57b005589a5b | -8.47391 | -44.53365 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba90d7f7-2f55-336f-a309-892dde039f42 | -4.44574 | -55.53957 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a69d230c-6733-3b42-b7cb-2b67772a6efe | -5.88915 | -52.08475 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31f9a26b-9056-3fab-9d8b-66c2e655773d | -8.77724 | -45.86271 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e833cd58-a237-36de-afd3-18f0f43e393b | -8.37026 | -47.2205 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0014a8de-5cc2-30d6-9e47-73a0770ce85d | -7.82714 | -44.97352 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0f789e1-d0a6-3189-b2e9-a6ac2152f1f3 | -7.60403 | -45.42442 | 2026-09-19 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31173e3f-7f40-3687-9dff-bbe11398ea63 | -2.32802 | -47.20143 | 2026-09-19 04:38:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4fd6cf2-810d-31ee-86b9-984c0ae0f4f6 | -7.64799 | -46.0998 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2866cb25-20f8-3bff-9b51-2b5b03620a3f | -6.90949 | -41.70712 | 2026-09-19 04:38:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9f723f7-3cb3-363a-bb1b-8d5a02668f81 | -8.12374 | -44.83244 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b4523d5-11e0-3b2d-941f-8f9c54e8b47e | -3.43132 | -50.66866 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1035778b-9647-3997-af2c-40b3c6419404 | -7.86389 | -46.44904 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 996fc7c0-f8f2-3b38-a5bd-f6fa7623e130 | -8.4397 | -45.83518 | 2026-09-19 04:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84d05852-39f2-3afa-98a8-c0c733396e7a | -6.00239 | -51.80173 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b21cb3cf-f981-3d52-9ba7-6d598be5d012 | -8.23162 | -45.60537 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10dffa15-db3c-39d9-8c99-e286843e3c4c | -7.22465 | -49.63688 | 2026-09-19 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76a330d9-1b0f-3b48-bf49-bc4150a61787 | -7.65022 | -46.10731 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4180f625-73cc-3114-b39e-587e0dc0a84c | -5.83886 | -52.03106 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00f685e0-a2e0-35f2-a57c-19acdfa24180 | -8.66359 | -45.44841 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d775fe6-d440-35b2-ab8e-30c7f6348b80 | -5.86454 | -52.03528 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 682158af-db3d-3b98-8828-e3b97668bfcf | -5.74449 | -57.58749 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aac067b4-f959-3271-ba50-73abdd573dea | -7.58502 | -46.30444 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48976516-5e3a-397b-8cc9-86ed99e52953 | -3.82129 | -50.74695 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9846c3c4-3c26-3fed-8ff8-908fd42f4d67 | -7.64411 | -46.10276 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92903d0e-af2b-3cb4-8ab6-348aa8a53418 | -2.90232 | -54.1877 | 2026-09-19 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d21c0b69-628f-309f-a87a-d1917cb57799 | -7.58331 | -43.44456 | 2026-09-19 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ad33ebe-e13e-3dc7-9bf5-b112353817ac | -4.98441 | -45.05751 | 2026-09-19 04:38:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae65e56a-a586-3610-95cb-a523ca78f5bd | -4.49063 | -54.98175 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a49a656d-0b28-3c9c-9386-7a49f8c8dbaf | -6.96341 | -42.5638 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5643a678-a969-3dba-9206-0dc14d189a6f | -7.75986 | -46.76091 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c3e385c3-9997-30bb-ae6b-a3216cfd27d7 | -7.19363 | -44.10163 | 2026-09-19 04:38:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4160b6d3-660c-3797-b62d-29bdf7ca6b05 | -2.83312 | -50.46664 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6db81daa-bf8f-3a55-ba50-d16dc960fad8 | -6.26567 | -41.66511 | 2026-09-19 04:38:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f1c55b3f-dea4-373c-982a-75c098e88acd | -7.58203 | -43.45282 | 2026-09-19 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8147a6e7-79b2-3f2b-8754-4866476b7c68 | -5.75585 | -57.45235 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 716013a6-b58f-35ae-bf3c-65153c39746c | -7.63968 | -46.10921 | 2026-09-19 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ab8cffc4-f5c1-3677-a647-566dfe618928 | -8.0848 | -45.49143 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| beee8fdd-0110-3395-9860-024cc45a35c9 | -4.5759 | -42.95041 | 2026-09-19 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0de2f0b-15d6-3b94-9088-c8e65cfae26c | -4.50778 | -54.97791 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 100852d0-5f7c-370b-a2cd-b57f3361734e | -3.4946 | -49.50866 | 2026-09-19 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c049796b-c013-331d-bc1d-b7006ec17bb2 | -2.83024 | -50.45892 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4eab73ae-65b9-3372-9172-6c65d154fe2a | -7.78223 | -44.88025 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dee7839-929b-3660-9224-e09bde132366 | -7.88279 | -46.43041 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb1c3a44-b572-3fa0-a0ec-6b7284555445 | -7.77653 | -44.89437 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72ecd2fe-da58-3c94-a211-2f3b79714495 | -8.75916 | -44.22327 | 2026-09-19 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e1042593-117d-304f-adb9-5d7c1bdcbeac | -5.66023 | -45.51132 | 2026-09-19 04:38:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a29d68e-b283-3579-9379-06d4069209b1 | -8.24508 | -45.60749 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c19e9fa-dacc-3001-80d7-212b06bbee17 | -5.86201 | -51.94505 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fc8247d-551d-368d-99cd-db8f4b815d5b | -5.74258 | -57.58578 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fb3cfe9-6a5d-33a4-bd1d-612221af94c1 | -5.85407 | -51.94028 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba016fb2-1787-3a3d-b5e3-975e634c922a | -2.73417 | -49.4644 | 2026-09-19 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5e09378-0c44-3b87-b4a5-8948e7b59d25 | -6.02139 | -51.76882 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 32964667-71c7-3650-9cdc-6d0f6d3878d6 | -3.00987 | -51.39072 | 2026-09-19 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 434418f2-b6be-319b-a151-8b63cdb45ed0 | -5.88609 | -52.05124 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39d447ac-8b16-3302-aa6e-3981c17bb7e1 | -5.76278 | -57.44905 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa167420-0c46-3785-bae3-ba05d298b6ad | -2.94044 | -50.49487 | 2026-09-19 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a01a3da0-d8a8-3e74-9c81-f3b99ec271cc | -7.29351 | -44.52551 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2af653b3-72ae-3bd1-8230-f8763e855405 | -1.19974 | -54.21882 | 2026-09-19 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c44641d5-467d-3a29-b261-f787d7344313 | -5.63062 | -40.86751 | 2026-09-19 04:38:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 88ac0e95-4324-362f-916c-9150fc85840c | -5.99883 | -51.79716 | 2026-09-19 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03de9226-4795-3fec-aa02-2ce596dac2e4 | -4.50363 | -54.96989 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68c65013-33c0-3b5b-9d9b-814545f900f6 | -5.8601 | -47.27767 | 2026-09-19 04:38:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42ae27db-10d2-3136-8113-a6ed046dd225 | -3.84787 | -50.01186 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4a043c5e-f1cb-3860-8a4e-830e3b57f026 | -8.86816 | -45.9275 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f183c26-a614-30c0-9ba7-673008ec9af4 | -7.09646 | -46.44431 | 2026-09-19 04:38:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18fc3c11-d64e-32fe-a745-377694674130 | -5.55986 | -48.44864 | 2026-09-19 04:38:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 595becbe-4d0c-358c-8aae-d0708ddda749 | -3.21096 | -53.94839 | 2026-09-19 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f2a3910-e676-3977-9c24-8791c0f0799b | -5.75671 | -57.44755 | 2026-09-19 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1032481-36ee-3f00-9111-86da1eb23eee | -8.23946 | -45.59929 | 2026-09-19 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b6bdaa2-3b5f-3427-a8a4-c880e9db6c75 | -8.35628 | -47.5754 | 2026-09-19 04:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bdca52b-3e01-3f3c-96e6-e3855f7feed5 | -3.28402 | -44.68505 | 2026-09-19 04:38:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1243316e-e7bb-37a0-bd59-0f1031a8a99d | -7.58315 | -43.45145 | 2026-09-19 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79ad1f2a-b350-39c3-b13d-037917bbb12b | -4.50616 | -54.96993 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d870e933-9659-3603-a38e-624376985d20 | -4.27064 | -46.53371 | 2026-09-19 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f384a65-ed16-3657-b67f-1998f05d9a75 | -2.58393 | -48.4404 | 2026-09-19 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f2c360d-9072-3664-b269-d98727dfa268 | -3.51802 | -50.79613 | 2026-09-19 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2bb37ace-6ace-307f-bd72-5441558ef26c | -8.93342 | -44.40258 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8885309-1b66-3fb5-ac4f-e6c93f1e3aa6 | -8.47908 | -44.83666 | 2026-09-19 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1358e6d0-0789-31d9-8dc4-8f5a73cd8a59 | -7.00022 | -42.16983 | 2026-09-19 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb08755d-70fe-3708-a013-fc5202bbb271 | -8.47858 | -47.00453 | 2026-09-19 04:38:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 241c8557-c103-37e6-bbf6-565cbd51ac1c | -6.26492 | -41.67012 | 2026-09-19 04:38:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2690fd1e-3742-35e2-bfc7-731a5ba7fbf2 | -3.89226 | -49.06646 | 2026-09-19 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 605931fe-4e55-36e2-82f7-1a40eabac145 | -4.38268 | -55.25465 | 2026-09-19 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46632651-9ea4-3937-b43e-3db1171f2fe7 | -8.67148 | -45.44224 | 2026-09-19 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6eadf97-6be0-379f-bb1e-bcc01c4fc6e2 | -3.03949 | -51.37088 | 2026-09-19 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70813911-1be6-3db9-9547-035c3db1ec32 | -7.19303 | -50.8274 | 2026-09-19 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90f26ae2-21a3-381d-8030-2251bb8de05d | -3.04218 | -46.92772 | 2026-09-19 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a947ec88-7a63-36e0-86f8-313e4afdfd1b | -3.73133 | -54.64451 | 2026-09-19 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README52.md)
