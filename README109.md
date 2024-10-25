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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c77ba66d-1ea2-38e6-b2a3-f3742d423725 | -8.98279 | -70.63191 | 2024-10-25 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 022a9694-cde5-3b4f-9fc3-7a7e182d53ab | -8.98219 | -70.63556 | 2024-10-25 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7b11e70-4324-3b09-9ac1-a77c57b89374 | -8.20604 | -70.97453 | 2024-10-25 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f37bd308-99bf-33e8-b7d6-0800fb3cf40b | -8.20261 | -70.97396 | 2024-10-25 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8549999e-1769-3ba3-a945-4373a065de27 | -1.6062 | -53.3087 | 2024-10-25 05:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2f4a5eb5-9404-3aff-817d-5f2a445995e6 | -11.02969 | -68.42337 | 2024-10-25 05:57:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df6b65a9-64c1-34e8-8401-c79e442674ee | -10.99718 | -68.5461 | 2024-10-25 05:57:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e12a66a-6a62-363d-b7b9-cb05d77df31f | -10.99385 | -68.54556 | 2024-10-25 05:57:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62a02b59-a24d-3f4b-9c29-d79d164f28b1 | -17.85365 | -57.55919 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1e87115c-496e-36f8-bea4-17b717d4bc6e | -17.85316 | -57.5651 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7f3c352f-fdb3-3bec-8bb0-7e77eddf17e4 | -17.2099 | -56.66905 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c4b44dde-0df8-3af8-b6da-8780b84ac125 | -17.86787 | -57.55443 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| aa621d11-8a07-30dd-b9ba-e79f6fa60c10 | -17.86736 | -57.56056 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6cce80f6-e747-3354-b4a7-6ab477525128 | -17.86718 | -57.55322 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| cb6d31bd-8dd0-3868-a337-d9f0a7e65f6a | -17.86667 | -57.55893 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ce2dc639-e306-3feb-95ff-6dcec447bc8c | -17.86605 | -57.56574 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5d2333f8-4c5c-3f12-822b-7cdbef7ae5d6 | -17.86101 | -57.55379 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c634abb1-cbdf-362e-9cc7-00e17f058f2a | -17.86052 | -57.55967 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6505f150-7c98-3a5a-8d57-0c8a3b1ceaf5 | -17.85999 | -57.5661 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 14316d78-4ac5-3c1e-93a9-0b549ca7861d | -17.85981 | -57.55824 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 11b96050-fa93-3523-a3b6-04390ccfdf9d | -17.85926 | -57.56442 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2cf04e5c-27a4-3c2a-a3f5-cbb5017235dd | -17.85864 | -57.5713 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 97531c0d-3fa7-38e1-92c7-cfa5edd52ded | -17.85293 | -57.55789 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| e45bcff9-cd0e-3c2a-bb2a-20a2123ba0f4 | -17.85243 | -57.56356 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a7830e97-1a46-3787-8b6c-bee12132ba38 | -17.85185 | -57.57003 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e48ec8c2-986d-340b-87f1-8d6c7cfc0f45 | -17.84679 | -57.55852 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 77c9900e-81cc-3c66-ad3c-b9937d63d1d8 | -17.84632 | -57.56422 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f4a58b9f-d73e-319f-8da9-332a208e8f13 | -17.84558 | -57.56276 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 84a05c64-9669-34c1-aaad-63b17fa7bf13 | -17.84503 | -57.56907 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5d6ca072-3906-325f-8e5f-b9a855de5dab | -17.83818 | -57.56828 | 2024-10-25 05:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| eb7e15c4-e5a9-3f38-8a0e-5aa9d08b29e0 | -17.2638 | -57.51288 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b82b7c98-b54a-350e-acb5-1bc2cd053848 | -17.26276 | -57.51135 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9cdb1e4b-69b2-3cb2-a7b5-c5ee30525e6e | -17.25754 | -57.50566 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b70d7d2f-197e-3e1b-951b-1a212b541aaf | -17.25698 | -57.5121 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| cf636c0d-96b4-36e5-95fb-32a77c4a25f1 | -17.25653 | -57.50418 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 74339495-507b-34de-8cca-99c91eb4339c | -17.25641 | -57.51852 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| be3f7df4-d4be-36f4-8163-8c72382269cf | -17.25594 | -57.51061 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 30b16096-a969-3b1b-98d6-ea3b7e45a7c5 | -17.25533 | -57.51703 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| b4889697-8a3e-3e0f-98ca-ab5fb76c5140 | -17.25126 | -57.49844 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e4b65a18-d6fa-3b56-88e3-32fda3fbece5 | -17.25071 | -57.50489 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b29e75fe-e716-3b79-9275-526667948d3f | -17.24971 | -57.50344 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 992dad8d-372a-32fb-8e7d-ae1c5e4c897c | -17.24911 | -57.50986 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| c29a3ef2-f965-3f77-a31a-d0a296a63819 | -17.2405 | -57.52835 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eed54ee7-71c5-3e11-ac4e-5c8a66b6e25d | -17.23484 | -57.52904 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 1dd560d6-7a48-3cfa-8b79-8ef6193179a4 | -17.23368 | -57.5276 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 46e76ccf-a0af-359c-a452-5a02b4ff7f41 | -17.23353 | -57.22305 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| d678b6a4-da04-3948-9f2b-3e5555ce3a80 | -17.23293 | -57.22976 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| a45b4254-5f0c-3c65-b450-f852d3fbc6d8 | -17.23233 | -57.23647 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 44a2c4b9-e9a1-3ff0-a5a3-424ca35d4093 | -17.2254 | -57.23571 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 08c27301-0102-31e4-9a16-3802edae9f1d | -17.22504 | -57.48241 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 462c6382-1b3f-3425-a50c-543ce6f20bd4 | -17.22481 | -57.24243 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| bcf65ecc-19c1-31f7-8c54-ca75e6e67923 | -17.22449 | -57.48887 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 179454c4-1b28-335a-a12d-4c9abfce53ec | -17.22394 | -57.49531 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 80f33c46-5924-3420-980d-636b680718d1 | -17.22357 | -57.48755 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1947c026-29a6-3b8e-8134-d915cf70b0b5 | -17.22299 | -57.49398 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fbf84ab5-8c03-3a8a-a721-a7cddcd4a0fb | -17.21733 | -57.48033 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| c2f4353d-e140-3a2c-bde5-f599a659a7b4 | -17.21729 | -57.24833 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c9f82cf4-85d7-3376-a777-c0d1c0e2dc80 | -17.21674 | -57.48679 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| cba38dfe-da92-3e45-8603-856219307ad7 | -17.19302 | -57.28599 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 666c9198-c8f7-3dde-ba5a-fa79045de6be | -17.18553 | -57.29184 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1d07eb05-cd53-35cc-a3c1-59fbdea2e7c7 | -16.80378 | -57.63659 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9f63c811-e606-335f-9289-c17e075d8876 | -16.8032 | -57.64278 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e037b8ba-f5d2-3850-8d53-4fc36dade778 | -17.08414 | -57.4093 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 98dd9972-92ca-371a-a9ad-bd94e4ee9032 | -17.08356 | -57.4158 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| ec550a92-ca46-38f5-8c2c-aae22b2e8f17 | -17.06074 | -57.43935 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ea7a592d-3b48-3bdc-a410-d077e3f45eb0 | -17.05959 | -57.4408 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2c11a722-4be7-360d-97a0-243f6c4dd340 | -17.05838 | -57.45367 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4517f7fb-a201-3631-b6f1-064c55c36180 | -17.05733 | -57.478 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| adca7794-b018-340c-89eb-b721e60a3cee | -17.05595 | -57.47937 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d1fb5ba2-c0b1-3d3f-b98d-9e9a67ee6522 | -17.0539 | -57.43859 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b6f4d6a2-db00-36df-acb6-2ab00117a242 | -17.05333 | -57.44502 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7018f9ab-87a3-333c-8559-503f4f2967e6 | -17.05277 | -57.45147 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 648281cd-3233-308b-a8ab-984dc18cd556 | -17.05275 | -57.44007 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 96331643-3353-3380-859f-6fc97a372db0 | -17.05215 | -57.44649 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5cb3b4cb-e95e-3a3f-aedf-f79f8145194e | -17.05154 | -57.45293 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7c1a9e52-d5a8-31b2-9ec0-4630f5c924c3 | -17.04913 | -57.4786 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 20b33c19-252d-351d-92d4-717a56def8dd | -17.04762 | -57.43131 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2e2fa793-cb7d-36cc-a07b-acebf1758c81 | -17.04706 | -57.43779 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| bde3e3d3-fe2b-3570-b92c-ea5d3fe61fb6 | -17.04649 | -57.44425 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4de3cf0b-72c2-36fe-8770-e37f2fd3f818 | -17.04593 | -57.4507 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| dec87b57-6f63-3a63-a4a6-4c467abd7b1d | -17.04592 | -57.43928 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| dd943f7e-0a92-37f2-9b21-3650eaf9d6a7 | -17.04531 | -57.44575 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 836c9f44-cd8b-3412-965a-9122f9818b99 | -17.04471 | -57.45219 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 34b202d9-50b7-306a-a279-55f14a3b7a67 | -17.03966 | -57.44344 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ad998a6c-8e65-3d33-aa57-e14806f2cc47 | -17.03854 | -57.45634 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| a6233126-67cc-3a46-87c4-e2e54e77f9fa | -17.03848 | -57.44497 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 711f4d55-dfbf-3669-a3e0-8acf7107d0ae | -17.03798 | -57.46278 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ffaf4d57-0919-39ac-93bd-606bd6aff5f2 | -17.03728 | -57.45785 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4c109c33-d4bc-3e73-a8ac-64859cfb1abe | -17.03668 | -57.46429 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 254b01e2-fe1e-374d-b189-a81fe0c45489 | -17.03059 | -57.46844 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 15103dcc-5e3b-3d2f-973c-3f0e6e498c4e | -16.99883 | -57.34875 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| d0d38f8e-a6c3-3b60-9ec7-941c4782c91d | -16.99824 | -57.35528 | 2024-10-25 05:57:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| e4a78431-ae3c-3596-95b9-b7103b57b327 | -17.0405 | -57.49706 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 503f7c77-8113-3537-979e-686bdae6b663 | -17.03976 | -57.52126 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 58f8b66a-8de0-3444-85b1-0ec99fae0682 | -17.0393 | -57.50985 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9220a079-0ec1-392c-ad02-1d4be1de8deb | -17.0392 | -57.52765 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| ef7b55c8-f470-3d15-b175-bd96e53b589c | -17.03811 | -57.52255 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 73a68b87-6bd3-3fc3-828e-f9be5359e22a | -17.03751 | -57.52893 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d63a8fcd-efe1-3cbc-bfa6-1dfafc8b8b7a | -17.03462 | -57.50134 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b093d3d9-3f99-3254-a410-f896c1dc0946 | -17.03407 | -57.50775 | 2024-10-25 05:57:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |


[Clique aqui para ver as próximas entradas](README110.md)
