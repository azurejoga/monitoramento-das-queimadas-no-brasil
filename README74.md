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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83eabca7-d4df-3ef5-8eaa-5cee6b601007 | -4.18953 | -48.62177 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 970f21f0-7064-3501-b5a3-09f133911202 | -4.18899 | -48.62521 | 2024-09-27 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15b5f19c-7565-37af-974e-1b647202126b | -4.12388 | -47.9735 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 154db769-8bbb-3bb7-94e7-54a696808561 | -4.12056 | -47.97298 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d4ba316-a3be-3ac8-9f6b-c880283a448f | -4.0871 | -48.2736 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a00e24a0-da69-3c5a-8b1a-939394d58d20 | -4.08325 | -48.27653 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2b905d9-6866-37f8-a47c-fca1927af68b | -4.06509 | -47.93574 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8ac4d7a-55f9-3b24-bd8a-c0f842c24693 | -4.05179 | -47.93369 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 665445e8-10af-3648-b9c4-180747088545 | -4.05125 | -47.93719 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac6d567f-8a33-3e25-bad6-62fbc22f1e1e | -4.05071 | -47.94069 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1352bddb-5b90-3107-bd51-cdb03d394cae | -4.04793 | -47.93668 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05f0563d-cc91-33b8-882f-36ca34c3ffd6 | -4.04739 | -47.94018 | 2024-09-27 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5465ac49-2c61-35a4-af70-4e915a2d6020 | -3.97814 | -47.883 | 2024-09-27 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82c29dff-cf4a-36d3-ae2a-b030594508fe | -5.87665 | -48.09721 | 2024-09-27 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b7b9405e-b50e-3ab0-b939-0abcbd6d8f23 | -5.8761 | -48.10077 | 2024-09-27 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1b13fe78-6d60-3abc-9c21-53094da5e3be | -5.87331 | -48.09668 | 2024-09-27 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bb7df5bc-3015-39b7-b1be-963072a88d18 | -5.87276 | -48.10025 | 2024-09-27 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b6cced8b-6ae0-3c9a-8e58-bb6775c25770 | -5.87222 | -48.10381 | 2024-09-27 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4ec1af8-0769-39b8-94f7-86cc7f42c4ea | -5.86942 | -48.09971 | 2024-09-27 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e2fce08-e5b0-3522-8a5e-840698eee92f | -5.86888 | -48.10328 | 2024-09-27 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44b2fe2a-98ef-31f0-bb2d-abdebc1753ec | -5.68724 | -49.31594 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 92c97211-2893-3c5a-ba5d-b3470d463f57 | -5.62718 | -49.155 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b68d148c-d761-3ea0-bf10-347ba3dc7031 | -5.62664 | -49.15845 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d72dc0c0-f5ca-3f7b-a0ec-c3422f259949 | -5.62388 | -49.15449 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 844f04ce-11a9-3866-8e5a-ffeb325eb910 | -5.62335 | -49.15793 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 303cc9e9-c691-3c4d-9fad-d7b12103c8cb | -5.60888 | -49.09928 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd9a9ad3-c13e-3b2b-951e-32645b27ae54 | -5.55795 | -49.01018 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01b6973f-fcb8-33c8-8285-91f032f49892 | -5.55741 | -49.01362 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f06e6f9-dc79-35a4-8293-ba5698e22baf | -5.55465 | -49.00966 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b1bb036-a6a5-3b52-ae5f-90d3d1d54002 | -5.55411 | -49.01311 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fa15110-0a84-36b1-948f-b24f51513ecf | -5.41118 | -49.07893 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 959c07bd-938e-3f03-91a6-309e3a0be643 | -5.40788 | -49.07841 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58e1a2eb-30bf-3dfe-ad7d-4fbb72499ba4 | -5.35302 | -49.12195 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc0607fb-5c68-300f-961e-73f7d6ae1950 | -5.28925 | -48.83361 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb128092-1b2b-3a47-917e-a7bf1f6c07d1 | -5.28871 | -48.83705 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5610251-4fda-3426-ad60-4cff80eb0f00 | -5.26137 | -48.88217 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0da79291-4c88-343d-843b-df79490bbb4a | -5.25861 | -48.87821 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e7d91be-c383-3741-b458-2e4b66261d37 | -5.25753 | -48.8851 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e444fd98-72ba-3469-a11c-b332a9be88cb | -5.25638 | -48.87082 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 226ee06a-fcc5-3bc2-85a5-ad7e0d6a26a3 | -5.25477 | -48.88114 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74149c63-b761-3fca-9b5b-bddd00970d2a | -5.25423 | -48.88459 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89e41cb0-2432-3b36-9485-39ad6e966cd9 | -5.25416 | -48.86342 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 564783da-ebae-3e32-bec3-328038df7ef4 | -5.25369 | -48.88803 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cd2b749-8360-3a6f-bb25-eaf43cb7d4d0 | -5.25315 | -48.89147 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9461106e-c51e-3cff-a335-5efc39a7db7f | -5.28817 | -48.84049 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ad56323-ce99-3da5-b2c8-9ffc71c0ab40 | -5.28595 | -48.83309 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 786e4381-5f22-3736-aa93-3402d2367734 | -5.28541 | -48.83654 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebe263af-f8a7-3c47-b240-d45ebe903e27 | -5.25807 | -48.88166 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87a09ef4-8c8b-3cef-af71-2a414b3d7be3 | -5.25746 | -48.86393 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c498f7cd-5f4a-38fd-88b8-e7a63d42142b | -5.25699 | -48.88854 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 921ab62c-c8a9-33dd-91f7-688ede189663 | -5.25147 | -48.88063 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b82e9aee-fc6e-38b9-a17d-73defffc853f | -5.25093 | -48.88408 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 519b7ac6-121e-3eda-9cf4-aadb8b6274f8 | -5.25039 | -48.88752 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31d759f6-3fcf-32d5-b4a7-6cf60b01224d | -5.24763 | -48.88356 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fbc180d-2c89-378d-b407-34df44649942 | -5.24709 | -48.887 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44bc6186-ab1b-32fc-a89d-a612bf53f630 | -5.2421 | -48.87565 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82061ba1-ba8e-3bb6-843a-343163a37761 | -5.2223 | -48.87257 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fe34bbe-8a33-34c7-b506-77c1066e18c7 | -5.22177 | -48.87601 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d87219e3-2332-345c-a2bf-bc795aecba88 | -5.22123 | -48.87945 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f5871d6-b97c-3839-92e2-e45718558c8d | -5.21954 | -48.86861 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8a6a98e-fd53-3b32-9562-babe2b836b72 | -5.21739 | -48.88238 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9977f187-fa4a-3cf2-8116-2b1c6944f17e | -5.21678 | -48.86465 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 978f9c41-c8f3-3cfd-9f79-86152e65194d | -5.21409 | -48.88187 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c088e84-167a-32db-97ba-67e74cc1275c | -5.21402 | -48.8607 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a991e652-8fcb-31a8-a3dc-ae052e330d78 | -5.20695 | -48.88428 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f391e978-847a-3d87-b466-a1dfa439d1a0 | -5.17769 | -48.87257 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f46d8155-1026-306a-bd98-c8cfae98029d | -5.13984 | -48.8984 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 762e8cad-f415-33df-93a2-a29a745962f1 | -5.12665 | -48.89635 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b67ca8e7-1fb5-3f9d-a273-e80e60cfd1db | -5.12395 | -48.91355 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91739f2e-c432-3ba7-9b3b-52f1fd09263c | -5.12234 | -48.92386 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48cabcbb-9fd5-3f3f-9a07-4ad8277c40f8 | -5.12066 | -48.91303 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 888b8e9b-21e4-3d71-9a0a-e89b25039f75 | -5.1185 | -48.92679 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ad3732f-7fb1-32bc-8fe0-630b1ef3e8ca | -5.11123 | -48.8869 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffbe2b11-09e6-3824-bed2-d6995ca5e3ea | -5.109 | -48.87951 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5dd64381-ed7a-345e-880b-3b43f2606872 | -5.10846 | -48.88295 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00dbb150-bb90-3265-9862-d778873bd988 | -5.10516 | -48.88244 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af23e599-e431-394c-881d-cd515db609e2 | -5.10348 | -48.8716 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d031e34-a741-37e3-b148-ce4c6d40ee97 | -5.1024 | -48.87848 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50f712ed-e333-3c60-a996-6f48676f8ce6 | -5.09964 | -48.87453 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aaca66c-2ede-3d07-a70a-ab7cbf8fa3e3 | -5.0991 | -48.87797 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 698a785e-48a5-38b8-adf6-34a417256eda | -5.09634 | -48.87402 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 669fccf4-d1cf-3ca5-9be5-0b47b47cd29f | -5.09465 | -48.86318 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 372ce440-9b40-3da2-b204-87cabb455d51 | -5.09358 | -48.87006 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5e616c8-4e25-37e6-b7f4-e40a53eafd8f | -5.33263 | -48.62125 | 2024-09-27 04:38:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f84806c8-a624-32f5-a6a2-a5c7bc352847 | -5.32933 | -48.62074 | 2024-09-27 04:38:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0632060-2940-3f78-8ff0-2f7b6f61dc3a | -5.2416 | -48.5291 | 2024-09-27 04:38:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecb52a8e-f505-3b08-987c-32e2ce064c1d | -5.24106 | -48.53256 | 2024-09-27 04:38:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df4ecaca-94e9-3681-a783-be92bf5203f4 | -5.23937 | -48.52166 | 2024-09-27 04:38:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0fcfc0bf-6e5d-317c-a2f1-b7ae01d32239 | -5.23883 | -48.52512 | 2024-09-27 04:38:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d590a498-4b70-3299-b83c-f92493dcd799 | -5.23829 | -48.52859 | 2024-09-27 04:38:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d20321b-7a3f-3790-9a0e-3ef9dd53b688 | -5.23552 | -48.52461 | 2024-09-27 04:38:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e3307e1-0bfd-30c6-ad70-7ba1f43cd101 | -5.19635 | -48.51498 | 2024-09-27 04:38:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e97704a-46e2-3c22-8884-4b5e6e136b77 | -5.16056 | -48.2634 | 2024-09-27 04:38:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26ff20e8-4e40-3297-9a66-b28feadcf34b | -5.2264 | -49.12685 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d122b62-360d-36c5-9a2a-2412cbbcde44 | -5.22586 | -49.13028 | 2024-09-27 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 642da800-3686-3a1e-80df-87b0574434d3 | -5.21465 | -49.24476 | 2024-09-27 04:38:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc9eac60-ed7e-360e-8aa4-4e2d15fcf8ab | -5.21135 | -49.24425 | 2024-09-27 04:38:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc7c1715-ac19-37ef-890c-8f22deebb63e | -5.20831 | -48.96203 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0a30314-2a07-383f-81a3-6385b4706b12 | -5.20723 | -48.96891 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da4a7c95-0b1e-39b5-a31f-23f4d2c9d5b8 | -5.20555 | -48.95807 | 2024-09-27 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README75.md)
