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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1a2bd03-7e04-3f6a-a586-1ffeb75c2539 | -2.81139 | -49.22679 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 731605a6-663a-31f0-a30e-81e59c0ac041 | -2.8109 | -49.22979 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8421a70b-8d2d-3efe-a8ab-5b0698c4936e | -2.81042 | -49.23282 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6c856dd-13a3-3c3f-b719-eb1497cecd4f | -2.80993 | -49.23586 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d2d7091-8e77-3c1b-bbea-83ef086a569d | -2.80944 | -49.23889 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ffd3f2f-6b4c-39ec-90ce-a1e01199f916 | -2.80888 | -49.22793 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 177841d1-13a1-3385-bcc9-64af18056ea2 | -2.80837 | -49.23094 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 94e38ffc-84e2-33ed-927a-13a676a7d4d0 | -2.80786 | -49.23397 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d7d8dc59-7f55-3b81-a05f-9d91dd75406e | -2.80735 | -49.23699 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f47e8975-8cc9-35be-a6fd-7cbd39db3432 | -2.80579 | -49.22895 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d56e18ad-59a2-327a-a7ba-ce6b180d2406 | -2.80531 | -49.23198 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bc40a12-610e-344a-be14-4fb3911314b5 | -2.80482 | -49.235 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c488ae9a-4da7-3710-bfe7-6a5c716dc83a | -2.80433 | -49.23803 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ec06280-40d4-30f2-a171-7ef0b73e53c3 | -2.70587 | -49.05212 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e081afd-c15f-393c-bd45-31d22810acae | -2.70081 | -49.05129 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ecc74cd-ff99-3f79-bf96-fd8290ed1837 | -2.70034 | -49.0542 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ccb7748-bbcb-3c2b-aae3-ab86cf0b17f3 | -2.69986 | -49.05716 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b022548a-49c2-3ab2-9e19-1d89d7187c0b | -2.59278 | -49.19897 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d0de8d7-ae20-3215-b515-7dfd7f14e5ee | -2.59007 | -49.19843 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce8ce82e-3aee-344a-bb3c-9275a171fdaf | -2.58959 | -49.20148 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d674df95-bbf3-3ab9-9536-6bde8b79768d | -2.58664 | -49.23538 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9591ed64-c26b-38ea-8ffe-25d25ea530b7 | -2.58495 | -49.19761 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 741c9c63-f149-39a3-8130-eab11c5706aa | -2.58447 | -49.20064 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a894c46d-edaa-3892-bafb-dd6e3a9f1d43 | -2.58421 | -49.2349 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e139f340-33ea-33b0-9fe8-719d7f2c1d72 | -2.58372 | -49.23793 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aedfd5c2-65ca-3bb0-b3c2-561710dfc1f2 | -2.57859 | -49.23707 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 313a869a-1853-36b0-95d1-1a07d343b224 | -2.54451 | -49.18785 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 745268ff-0d5f-3d73-98f2-e2e814daf45c | -2.48315 | -49.24013 | 2024-10-28 04:04:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe214b0d-da58-3fcc-b24c-5e7c9a355ba5 | -2.4682 | -49.06023 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2ca7590-44ad-3c06-b823-57f254350ce5 | -2.46771 | -49.0632 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 059892e6-9bff-3d21-b692-0d4532a8635d | -2.4233 | -48.95996 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 404c6336-5ee7-3f19-8ead-a6319e97ee52 | -2.42236 | -48.96587 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d925491-bff5-3ec8-a156-a20d7c7026f0 | -2.42162 | -48.96443 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39dae34d-1dac-3c43-a3e6-3650c6470cb2 | -2.42113 | -48.96738 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81482244-fbb1-3ea9-afc4-805fed400ed3 | -2.93172 | -49.55065 | 2024-10-28 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7ce7e79c-a26d-3380-b81f-d134d34b8f4c | -2.9312 | -49.55383 | 2024-10-28 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2f01666a-fa86-3351-81c0-31dc195f95df | -2.88597 | -49.50416 | 2024-10-28 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52c28bd1-3c0d-3b14-9218-2da9548edba5 | -2.88544 | -49.50731 | 2024-10-28 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33831af8-b669-36f7-83c9-9921c66c57e0 | -2.88077 | -49.5033 | 2024-10-28 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6efc8597-22b8-3ef4-83c5-c450577c9976 | -2.87838 | -49.25196 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| fd0a74c5-f394-39fe-a939-66b2883d59e1 | -2.87788 | -49.25501 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| d93b6ba0-0f09-3d3a-8297-a27bb2bc6489 | -2.87739 | -49.25804 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 5d9e6c15-8c3c-3ef9-b754-aa60c06a0aad | -2.87689 | -49.26108 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4941073e-393f-394f-b044-84cc91c9e80a | -2.8764 | -49.26411 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1af8c60-8ea4-3774-9315-39c764124e76 | -2.87327 | -49.25112 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5905d8a3-6f0a-32d2-8d2b-6a8b17d4fd95 | -2.87277 | -49.25417 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| c1003474-0e41-3b10-945c-b50ed1e85cca | -2.87228 | -49.25719 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 7773263f-4874-3ff3-a6d2-77e688ecb2f5 | -2.87178 | -49.26022 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| daa9c680-f3cb-39d7-a4bc-e842ab89b288 | -2.87128 | -49.26323 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07d9b8ef-0548-34ab-8acb-7f5dd4020c17 | -2.86766 | -49.25331 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c42e9486-fcf8-389c-b4bd-68ae1c180c8e | -2.86716 | -49.25634 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c2eff1f-931e-3f51-bc56-505878ddb22b | -2.86667 | -49.25935 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 204ef523-a8aa-3d93-a5a0-09f9cd2fdd15 | -2.86617 | -49.26236 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcb395ba-fe22-3e11-88d5-63bf4ac4875b | -2.86255 | -49.25248 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d65acd5-2734-3aec-ab51-99fbbee616d2 | -2.86205 | -49.25549 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bdf67a4-b4e2-356f-a29a-3010af520fe6 | -2.86156 | -49.25849 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e7fce10-eaff-3257-ade9-7fa3e964d86a | -2.86106 | -49.26149 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5631eab7-639b-3b6d-b2d5-eb7f432f3ae5 | -2.85742 | -49.25168 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8b370a9-19aa-3ac9-9b36-d2648125a979 | -2.85693 | -49.25469 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20aabaeb-0578-3970-a483-36dda00245d3 | -2.85644 | -49.25768 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d89c51c-9abe-3243-a264-613813121fe7 | -2.85594 | -49.26065 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5809c7ec-2957-3618-9c87-36601d47efc8 | -2.85231 | -49.25084 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bea4c64-9bca-39da-bb24-2f1ab61af24a | -2.85181 | -49.25385 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1dbd9c94-6ac6-362f-9c0a-db909e73cb59 | -2.85132 | -49.25682 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 011cc713-adb0-377b-b1a1-2c3ddd197427 | -2.85083 | -49.25979 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb8409b2-079d-37ea-a7d7-44c4d48e6293 | -2.84671 | -49.25293 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20a24197-f635-3d4e-bea9-08d28fd32b88 | -2.84622 | -49.25592 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f9cdb20-0ee7-3b52-bd72-78fdd1b2af6f | -2.84572 | -49.25893 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 370f160e-d5d4-33ea-9a04-73aa36f4af19 | -2.84161 | -49.25204 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26ebaf5a-b307-3bdc-a07c-cbfc48e91379 | -2.84111 | -49.25505 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08200a98-a117-390c-a6d0-96797b0f969f | -2.84061 | -49.25805 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1434b980-60f5-38e7-92d4-41c31d4af6bf | -2.84011 | -49.26106 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2fb73bc-dd02-375e-a243-c03327de251f | -2.83649 | -49.25117 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 984f3f09-2a60-35f0-96e9-51be753f5cbd | -2.83549 | -49.2572 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d397499c-bd59-3502-9778-99ac9693919b | -2.83499 | -49.26022 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a28498b7-59f2-35ab-9a47-2dece82de750 | -2.83088 | -49.25335 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c7c046a-92ad-31da-88e3-ac67d9cba49e | -2.83037 | -49.25637 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8180788a-e244-3f46-85e1-6333c537c9a6 | -2.70779 | -49.31272 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2dad24b4-722b-3e89-9f1a-32a3a5652f81 | -2.70727 | -49.3158 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 04c24da4-58d3-3eba-9f09-e07eb1b605e9 | -2.70675 | -49.31889 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02cc7f07-68e0-303c-a8cb-85f1f7a5e202 | -2.70624 | -49.32198 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2882cfe-eb67-31a0-90a7-da5fb040a23c | -2.70572 | -49.32508 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df43ada6-b8f6-3ead-8254-7d1b9b690cbf | -2.70213 | -49.31491 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fb70fc2c-7959-317a-a8f7-f0e4b2f0073d | -2.70161 | -49.318 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d465c2e6-58d0-3da9-a645-c9a5b017c007 | -2.7011 | -49.32108 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b452ece6-407e-3642-8439-047cc5934739 | -2.69595 | -49.32021 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8bd0fd7-af42-31a2-a528-dde5a9a7e8cb | -2.69132 | -49.31629 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c667230-f8a2-3078-a68d-269bfc09cc20 | -2.62925 | -49.26447 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1443bf4e-355d-3f34-af8c-7160ced09e3d | -2.62875 | -49.2675 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09081194-cdd1-3dbc-8300-09ebdd40de3f | -2.62462 | -49.26056 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d47ce80d-d3c0-3aec-b264-919af685e7e9 | -2.5574 | -49.83156 | 2024-10-28 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 259be569-a186-3239-8c0c-681db87e767e | -2.55261 | -49.8273 | 2024-10-28 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14780993-32b2-3659-b2e4-c0457b8db802 | -2.53915 | -49.84232 | 2024-10-28 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afd1bc41-441e-39d1-b7b8-6564e78e195d | -2.47232 | -49.7939 | 2024-10-28 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 709e1712-0a10-39c8-8f36-9c30aeeb7f3e | -2.46755 | -49.78952 | 2024-10-28 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5325f036-a7de-3441-94f5-2f7693a5efee | -2.46699 | -49.79294 | 2024-10-28 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62cad662-f930-3a1d-b4cc-156ff5b475a3 | -2.46221 | -49.78863 | 2024-10-28 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7780a9c-165e-3970-b11e-52273771503d | -2.46166 | -49.79203 | 2024-10-28 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17e20e8b-a748-3c93-b2ce-f4477a0046e2 | -2.4611 | -49.79543 | 2024-10-28 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6971af35-d642-3f2e-bf90-b254815664fe | -2.35093 | -49.54714 | 2024-10-28 04:04:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |


[Clique aqui para ver as próximas entradas](README34.md)
