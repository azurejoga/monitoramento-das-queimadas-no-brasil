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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 281821f3-9377-35fb-a476-9ef71f0c83d4 | -7.51492 | -44.36268 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bdd188a-6890-3cbf-9d95-c3f99ef857f9 | -10.02943 | -45.30005 | 2025-09-15 04:49:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af99ce78-67f7-3e10-91c2-d3dd9a317216 | -4.41988 | -47.96793 | 2025-09-15 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1333d2a9-c9c0-3216-b9e4-2fabe9bcb6c6 | -8.4243 | -47.22232 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1370b465-6db2-3a0b-95dc-0c6307da22ee | -10.18593 | -46.1577 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0f997de-77c0-304c-a401-b21c122711f6 | -7.88077 | -43.58812 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 490b7080-30a7-32cb-b45c-f2a46577b14c | -8.09741 | -50.16088 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bec26efb-80bb-3844-a53e-68a4a5040575 | -8.62397 | -53.11542 | 2025-09-15 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12519ea8-1a7d-3948-8add-fe3dd83d8a9f | -8.60279 | -46.3517 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8604c9bc-4ce9-3b5c-8f8f-b025aeb96a89 | -5.76472 | -52.36926 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 422ae6ad-3390-30ef-9343-c209d80a50cc | -6.17836 | -41.18948 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e45d2c93-0c1b-3800-a1a4-d74b38994d3e | -10.78022 | -45.97982 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a4756ea-d0b4-3f77-b4e8-fb4bde5922ca | -6.32767 | -43.33761 | 2025-09-15 04:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15577924-118a-380d-9ec9-1b7750507b3a | -7.88193 | -43.56543 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 878c4461-c884-3ccd-bbba-b17b297c4b94 | -6.17943 | -41.18205 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3f6b1f20-decc-3815-a20a-c584253a6fcd | -6.55615 | -43.99168 | 2025-09-15 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de558060-4dae-3b4f-87f1-51368baba621 | -8.9637 | -45.77724 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40f71633-f82f-31ff-bcdf-dbfba3158124 | -8.95914 | -45.78606 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 283d8bc1-1314-321a-a7f7-6f32606f9dd2 | -7.98646 | -44.84304 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b015b07-fed8-3e08-b984-13335db784b9 | -7.391 | -49.98943 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26d42ce7-d098-3a65-93b9-8dbb7621bc93 | -10.89653 | -45.55585 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d0216f5-4a60-3b5b-a4fb-c38dbc306f7f | -9.55704 | -48.04216 | 2025-09-15 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5f215f1-e174-3b16-bc01-ae9309ba5ef8 | -6.9142 | -46.15913 | 2025-09-15 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5b66c46-b3e4-3ccd-a757-3ac82d1a62b2 | -4.28358 | -56.33431 | 2025-09-15 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68e99fe0-036b-33fc-9694-8b2536541721 | -10.43114 | -44.84676 | 2025-09-15 04:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dc723b7-e371-30a3-9b15-59e8da821574 | -9.91827 | -50.29005 | 2025-09-15 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e65a6091-738d-3b63-ac24-7f8ec872f84f | -5.84661 | -44.16406 | 2025-09-15 04:49:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 48f46617-6add-31bc-bcc0-d229dace7817 | -8.96206 | -45.78911 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4675196f-2447-3d7c-9f2f-b341f2017c11 | -6.40256 | -46.9407 | 2025-09-15 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4557da6-212a-3dd8-a9e4-3598a80a569c | -9.23656 | -45.67391 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22b78b0f-af21-323a-8d17-bff86c645163 | -8.59665 | -46.36549 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b52c4b9-54cd-33c8-9e7f-2ac629b7f62a | -10.65563 | -46.23561 | 2025-09-15 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a5c2ca1-2f43-3fdc-b29c-c11e71450eb7 | -3.74912 | -51.80824 | 2025-09-15 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c2d4f64-d409-3f55-968d-11870f998135 | -10.86836 | -45.46239 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be60e9e0-a6d7-342e-9025-cf3f86895d71 | -9.00928 | -47.04237 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c91d6a03-7392-3d7d-a728-89ece2c5c26a | -7.84771 | -46.11033 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 346b129e-a062-3121-b48f-d0cf58c5dcd9 | -4.85747 | -45.73253 | 2025-09-15 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d383a29c-b5e9-3a61-aaab-b8d697be069c | -7.85012 | -43.85466 | 2025-09-15 04:49:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7dbe906-a683-300d-b886-a75af60b83c5 | -6.97592 | -44.5406 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 906ea545-739b-330e-bb58-0a0069095e43 | -5.47284 | -44.69194 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c5d066a-6972-36a1-86f9-664b613d14d2 | -8.13527 | -43.65353 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66aee7a5-53e8-3fa9-9471-407414874860 | -10.17051 | -45.32082 | 2025-09-15 04:49:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e9c7848-f906-32dc-9377-38e4eec41082 | -8.4166 | -47.22112 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0de73cbb-e766-3a19-80f7-8900d8243ecc | -6.42486 | -42.60571 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1deabd34-a905-31b4-9e1d-749ac143a8e5 | -9.00912 | -48.02448 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3c1e5d4-31ef-3e44-a4b9-e17e717972cd | -10.89321 | -45.44765 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 556e2d2c-99cb-3769-a303-759ac840770f | -5.11669 | -46.12793 | 2025-09-15 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e39a23db-4eb3-34f7-a24d-4b7455f8a8d9 | -4.1109 | -51.09089 | 2025-09-15 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2561b992-8dad-39b6-855b-8cc6c47f685a | -7.64116 | -49.72379 | 2025-09-15 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d732f2d-a023-3bf0-9e0c-82336c14c600 | -7.88756 | -63.70285 | 2025-09-15 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a177c72-b4d2-3a3a-b66e-ca2010c37521 | -5.16283 | -48.14699 | 2025-09-15 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 641f50d5-5f07-305c-ae1d-047f4aa5f004 | -7.88116 | -43.57082 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| d1e46376-b7ae-3437-abf3-66994e9b2756 | -6.43051 | -42.63994 | 2025-09-15 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e1f9bf69-511a-30e3-8d4c-6b6285640205 | -5.64854 | -42.6005 | 2025-09-15 04:49:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 175aef54-7b6a-38fd-bffe-a1f2d16cc285 | -8.92189 | -54.44701 | 2025-09-15 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7a79e33-41b8-37ea-8286-59ecd2cfb200 | -5.85119 | -44.16449 | 2025-09-15 04:49:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b03acfc2-9df5-355e-95b6-ffc4095533c8 | -8.08664 | -44.50055 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13f3ac2c-041b-3573-8f1b-4394f7780be3 | -8.9277 | -54.44664 | 2025-09-15 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7519e2b8-dc53-35bc-bbc6-4e009714be84 | -4.86569 | -49.33147 | 2025-09-15 04:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a12670cc-b322-3142-b19f-857caf86d202 | -6.99814 | -44.55885 | 2025-09-15 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 516c3576-5f62-3c1c-9d8a-b5ac4b421d00 | -7.70747 | -50.35284 | 2025-09-15 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 753624eb-9b86-3cb1-afb5-9e8b749f2161 | -10.18952 | -46.16086 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c601d5f9-c397-3aeb-83ca-78d31f1e14f9 | -8.14688 | -43.67721 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4600cde4-c429-3c31-b529-99d536ce349f | -10.14267 | -46.15847 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08e17beb-7d0c-3827-814b-bf5843bfeae3 | -8.96909 | -45.76973 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b710d6d-e67b-3854-8599-86cbc578c0ca | -7.87962 | -43.58155 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 0c228a62-ea46-398b-8b9e-140a55ecf577 | -5.67799 | -43.49275 | 2025-09-15 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13b70dba-79b8-3861-a4c6-a457f36d43ee | -6.62772 | -51.00423 | 2025-09-15 04:49:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06af66bf-0e8b-3a94-bbf0-002e17e74dab | -5.22433 | -43.69983 | 2025-09-15 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eff168f-2950-342d-8d5a-a66dee6f628a | -7.38425 | -49.98837 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29be067c-5f9c-30cf-bcfd-5bb1ebe3df3c | -8.07484 | -44.51818 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5120cae5-8ee8-3eea-a279-3049c7becb70 | -5.95588 | -42.79533 | 2025-09-15 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b1afe234-5068-3364-ab27-611b4faff58b | -8.3486 | -44.72375 | 2025-09-15 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 030ac725-8bd0-31d6-8ab8-e500e4cae7ef | -5.14699 | -46.00885 | 2025-09-15 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f101a96-2ac4-347f-914a-2df61b6b3262 | -10.7759 | -45.97922 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9409ab5-252e-3a3b-bfc0-4eed79ed206b | -5.73905 | -43.20535 | 2025-09-15 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29fa64c8-0601-31fc-bc59-3529075c0399 | -6.40708 | -46.93663 | 2025-09-15 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72902e3d-0740-3cca-a839-5d221c82b307 | -5.39049 | -42.83202 | 2025-09-15 04:49:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cc0ddd12-c4a6-3a6d-86be-f0158ea6b078 | -7.69265 | -48.86426 | 2025-09-15 04:49:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52db9785-323e-35e0-970e-891933a767d4 | -7.8549 | -46.11865 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aabe1b6b-0727-3a23-8163-9e31453ac9cb | -8.97364 | -45.83074 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a62889e7-d83e-38e0-876d-1fcda2afc661 | -6.20495 | -55.63397 | 2025-09-15 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3c18ae0-931b-37f8-9e12-465b63cb9516 | -10.72827 | -44.77077 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a760987-fbb3-35c4-8e7a-443b600385a3 | -8.44086 | -55.62965 | 2025-09-15 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f906bf9-f2e9-3ee1-93cc-3feadcd49523 | -8.10078 | -50.1614 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aac9a007-29d0-3fce-8377-a402c5456d66 | -6.66323 | -45.55561 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcad7f92-e916-3621-9415-c61f2e8593b1 | -9.12018 | -46.94479 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9aa6ea81-751c-3b72-b043-3ece7d4d3beb | -9.08611 | -44.81376 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e1e14b2-b519-3a4a-920c-e551737a95ba | -7.85936 | -43.58402 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 878face2-1ae4-3065-ac4d-786019cabf9c | -8.09224 | -50.16407 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11bbb2be-63ce-30e8-821e-1e702e13a82d | -7.98146 | -45.65398 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4774e8e7-f2b7-3306-a54c-fd96dea05bc4 | -6.91967 | -46.17793 | 2025-09-15 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 725b4dc7-dd91-37b2-bd26-ec258a1094cc | -7.36664 | -44.35316 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0f1250f-3f65-35c6-a37c-9a2cb2cafad1 | -7.89274 | -43.57336 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 880c1619-0952-3a1e-b40e-8edaaa3058ce | -5.94911 | -42.8071 | 2025-09-15 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 771b31b5-077c-35a6-8f09-6c4421975ffc | -10.79321 | -45.98138 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2d59494-c0a9-3579-80ed-539e32ffdcfd | -8.12893 | -43.66349 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bcc0597-e989-3d24-b77a-eb832b46d1cf | -5.9744 | -45.85436 | 2025-09-15 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3aad4e66-cec3-3ae3-87e2-b81f5f5116c9 | -5.97651 | -45.84002 | 2025-09-15 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d055ea1d-90cc-3117-90ea-e9b85fab8cfd | -9.73397 | -46.04318 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README42.md)
