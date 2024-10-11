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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ffbafbd-aca4-36a4-9e0e-9e84909d96f2 | -4.10614 | -48.25028 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 2138ae95-1752-33a4-bae3-dfe584075138 | -4.10586 | -48.26682 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12d7b4f2-654d-3fc2-9942-f53d4ba8f1b6 | -4.10556 | -48.25421 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| e55abfae-75c1-3d14-91fe-806ef091974e | -4.10532 | -48.27061 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a2d81b1-c104-3bfe-997f-62a5fd71de7a | -4.105 | -48.25799 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 685926ab-20d0-30ed-925d-8e3ede05e37c | -4.10478 | -48.27446 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06ea1eab-6c36-3308-a847-bcd346b6a911 | -4.10444 | -48.26173 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 92c2bd6d-5320-3155-bfd1-685133fa0e63 | -4.10388 | -48.26552 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0717db99-38a5-3275-bfe2-219c65950f9e | -4.10332 | -48.26933 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed40921c-f364-3cdc-8c4a-624699c61a43 | -4.10286 | -48.24667 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 38a3e63d-8654-3649-9105-be5c0a08ca7c | -4.10274 | -48.2732 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a474bb10-6cf2-3ee8-b710-682c500971be | -4.1023 | -48.25066 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| feac201e-43f6-3b0e-9855-ee56c31fa43d | -4.10174 | -48.25465 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 794dc7bc-575d-38a0-b5af-5aa9fe1f0ff6 | -4.1012 | -48.25845 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2bac94c-7841-32b8-a8f2-fff6ace8d655 | -4.10105 | -48.24523 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ba696910-04fc-3e21-9307-6f25b9b634d4 | -4.10045 | -48.24927 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 50bc2e23-d14c-344f-bded-2ffdac2d6324 | -4.09985 | -48.25333 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ac464b75-5252-308b-843b-9a19c3df9c51 | -4.09957 | -48.27005 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b65f0787-5944-361f-b28a-0b5361760c70 | -4.09927 | -48.25721 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 049f2172-bf9f-3937-80e4-b6b608c51b7a | -4.09719 | -48.24544 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c6fd53dc-ccab-3b08-8ed6-9143203872e6 | -4.09661 | -48.24958 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 80cadc0c-3ca9-3d08-8ca3-396a590e2221 | -4.09538 | -48.24403 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b8805f9-cbf9-3749-b924-2f7c88fcd03e | -4.09477 | -48.24818 | 2024-10-11 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ab5333d7-f62f-3c57-85c7-6d92657ea2c1 | -5.71108 | -49.31355 | 2024-10-11 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ede1788d-393c-3d46-916c-fc59f5586afb | -5.24724 | -48.04197 | 2024-10-11 05:16:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 76696933-d5b3-3c5c-a761-51825612ff50 | -5.24665 | -48.04622 | 2024-10-11 05:16:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3009e5bb-d87b-3d2d-a325-e4ce2341e29a | -5.24166 | -48.45793 | 2024-10-11 05:16:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fe2472c-518d-3bb5-81b8-2800de01201d | -5.17275 | -48.27839 | 2024-10-11 05:16:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 682e5687-34eb-3936-8779-462dc1401c3e | -5.1722 | -48.28246 | 2024-10-11 05:16:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5d960585-991a-3491-a2cb-b5c155e2acb1 | -5.17175 | -48.2815 | 2024-10-11 05:16:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 897f522d-e2b4-3133-99c3-3fff706ba320 | -5.17116 | -48.28557 | 2024-10-11 05:16:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5aecd192-b144-3407-88a5-a49e9c245d9a | -5.16639 | -48.28166 | 2024-10-11 05:16:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5cf7520-67a6-3671-91af-8e3280f2a716 | -2.94904 | -50.30443 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e0d49d5-a51c-3674-859a-14f5227cc5b8 | -0.81968 | -48.67091 | 2024-10-11 05:16:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 803e3ca7-9eb0-3185-87b7-efeefa682450 | -0.81917 | -48.6698 | 2024-10-11 05:16:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bebe614e-25af-3f50-9bf0-9d329169a213 | -0.81916 | -48.67419 | 2024-10-11 05:16:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30b1c21d-8f7b-3b5f-8ac3-524202c404bf | -0.81867 | -48.67308 | 2024-10-11 05:16:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d043592a-670b-35c0-b2a9-93d1c716e396 | -3.65379 | -49.62702 | 2024-10-11 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ec25e60-0fad-3165-98ee-a6b29e093085 | -3.43132 | -50.15935 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c474890f-7893-37dc-9aaf-d7c3fcb623f0 | -3.4309 | -50.16219 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33150960-1767-3d08-965f-93917a8c77be | -3.42592 | -50.16145 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57f56499-702f-3584-a26f-402cab31a9d2 | -3.42549 | -50.16438 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24d23ab7-9f18-303d-b533-1c143b8d970b | -3.40627 | -50.32961 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3c15c30-7a46-384e-945c-5c37634f2a43 | -3.31588 | -50.17683 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| be85dbd8-bfa4-3e82-bdf0-aefb3502ab5a | -3.31092 | -50.17607 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 90cffd75-a359-3f33-8952-a45372b2a578 | -3.27205 | -50.16425 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5316b640-62c7-37ac-a0a5-8651d69dc07c | -3.27114 | -50.16363 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e990b9d0-9cdb-317d-abab-51ba3af0deb1 | -3.26708 | -50.16347 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1523cfb-6254-344a-a17e-cd6fff48eb55 | -3.17022 | -50.43523 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 492e5bfb-7ab0-397e-9961-80cd42f01798 | -3.16535 | -50.43448 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f9f82f0d-5e0b-3428-848a-181f7d4ba629 | -3.16453 | -50.44009 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6618dbae-9ea1-3d34-8489-436c309e9181 | -3.15966 | -50.43938 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| da02c049-e350-3931-8160-46424e156ca9 | -3.1548 | -50.43868 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 33f577d0-b4ae-3769-9e5c-ec77cc6454ba | -3.15397 | -50.44429 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| a5dad8c4-781d-30d8-96a3-6664c9ab58fd | -3.14992 | -50.43801 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d647e514-703d-3c13-b3c5-b0f67500c107 | -3.14912 | -50.4435 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 3923e778-8d1c-3c37-8ae7-0c016538a67c | -3.14654 | -50.43703 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ece706b-34b1-3be6-a598-b51461f2ddbd | -3.14571 | -50.44245 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5e9dd13a-3727-3b36-9198-253abfcb45cf | -3.14427 | -50.44274 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 48fb355f-40cf-3aa5-a245-6d925ae2cb26 | -3.14061 | -50.24623 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7575777b-dda5-37fa-a948-da40385a4073 | -3.13851 | -50.42452 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c45b406b-329a-33a8-8dee-c5da4770c419 | -3.13693 | -50.42483 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f8976b9-7117-32f4-8df2-8687c9bc55e1 | -3.13363 | -50.42392 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce83a35f-a9f0-3169-b20f-24210515ef63 | -3.13205 | -50.42418 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a43074a8-15b0-3978-aeb9-bd18ddf5e220 | -3.0931 | -50.22696 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 73fff5f1-d05a-382f-b418-d3467ef94e37 | -3.06895 | -50.49087 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8b678bf-aefe-3bd9-a320-25530503b31d | -2.9463 | -50.30368 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 528c7ff8-ab82-30f3-b168-56fb8e3d8c69 | -2.91824 | -50.48586 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a492dcd-f718-333e-8490-7989ce46cb42 | -2.9175 | -50.48622 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed97aa18-9a2b-383c-b701-bb60f27d00da | -2.90299 | -50.39121 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4d37ea7-7645-3846-a9ee-683e3841f209 | -2.90218 | -50.3966 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dfa47bd5-cb9c-3d90-a926-fec524fe01c7 | -2.89732 | -50.39586 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c55bc31-56cf-379d-9aef-8164198532ae | -2.89247 | -50.39511 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac8bdef4-185a-3b4a-a046-33002a788345 | -2.89166 | -50.40044 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29f4e76d-a462-3081-b1e9-eca0773868ad | -2.84851 | -49.87119 | 2024-10-11 05:16:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e279ae9-a47f-3d7c-baf7-46c7efd0b28a | -2.84392 | -49.86747 | 2024-10-11 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a3d986c-d63e-3711-91f3-58b081131e7a | -2.84348 | -49.8704 | 2024-10-11 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae45b407-076d-3ebd-9c83-f1e8f3f3f0c1 | -2.83431 | -49.52782 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ead6adf5-4745-3984-82dc-0687d46b9445 | -2.83177 | -49.52525 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 05d09959-d1a4-3531-8c2b-6ee34bbe3461 | -2.83132 | -49.52839 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 15fba7e7-6a9b-36bd-8826-8de96afadd70 | -2.82917 | -49.52697 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c40df949-7596-3003-a76b-47594232fb70 | -2.74324 | -49.53858 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8279cdf4-12eb-351e-be37-17a2d0b452e4 | -2.74279 | -49.54163 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a3b3833-8a33-335b-8172-3b0af9d6c3b4 | -2.7381 | -49.53779 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 23ab79d9-a826-357b-becf-31664284b093 | -2.73765 | -49.54084 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cf842e82-e6fb-3026-af7e-e64776d0408a | -2.73536 | -49.54055 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf8fc79d-f859-3845-9b51-f055ddf2b283 | -2.72604 | -49.54842 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8491bda-bef6-3ad1-b443-a1048b5b4154 | -2.72415 | -49.54509 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77ca1d7c-1cb4-335d-830d-48901f2954cd | -2.72368 | -49.54813 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35a40639-8a02-35ba-87af-6fe87460b591 | -2.72135 | -49.54459 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31847f43-2806-30c8-965d-58a9852fca14 | -2.71386 | -49.43942 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9f3d6d4-b3b7-3d24-a853-3c7969143ae1 | -2.70869 | -49.43862 | 2024-10-11 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2e250231-1546-3aaa-a391-3e6356dc207a | -2.61508 | -49.78535 | 2024-10-11 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef277c22-e00f-3548-975e-d79c2c55ca10 | -2.61464 | -49.78828 | 2024-10-11 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0b01e90-a1a7-34b4-8ea5-ba86e72db961 | -2.59779 | -49.79771 | 2024-10-11 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9252a1b3-989d-3ee8-bceb-41fae0dbcd29 | -2.53832 | -49.71622 | 2024-10-11 05:16:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21cc2af6-0b65-31cd-9ac7-57eab580dcc7 | -2.53788 | -49.71918 | 2024-10-11 05:16:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cac68b76-a15a-3d09-a63f-5c0dcdbc3e40 | -2.47416 | -50.24331 | 2024-10-11 05:16:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12677d87-a390-31a8-a4b9-1b1a2501a5e7 | -2.47334 | -50.24873 | 2024-10-11 05:16:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d55a3ffc-5551-3121-ad07-5d6c36e02b62 | -2.46684 | -50.25875 | 2024-10-11 05:16:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README77.md)
