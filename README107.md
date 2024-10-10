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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2004e34-82f8-3291-8971-8d110586fef8 | -4.14101 | -51.09685 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b6a8eae-ac2d-3446-9665-89473cb08dd7 | -4.14046 | -51.1003 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1f3d0a0-c5db-3d9f-9c19-9450af27d1a6 | -4.13991 | -51.10375 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17f2ebb3-f2bd-3071-a4f8-5275d75e8da6 | -4.13714 | -51.09979 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d8fba0b-413b-307e-b2be-f2bb7e2a2a28 | -4.13491 | -51.071 | 2024-10-10 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62a6a8b0-5215-3039-aed1-774a2df627dd | -4.13004 | -51.18759 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35b6e7a7-5db6-3ce2-b4a4-0b1f1901e169 | -4.12672 | -51.18707 | 2024-10-10 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1d1b360-f68e-3b9e-bbbb-4aab81f41a83 | -8.88542 | -53.05804 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21539d5e-13a1-3408-95ad-2e42e391a347 | -6.39592 | -52.72554 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32999db3-095c-3481-be2f-41781d14273a | -6.39311 | -52.72133 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08161393-1be3-34d4-bd56-b984ddb804a1 | -6.39252 | -52.72499 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c0b79bed-9858-3f45-bdbe-cc2ee8953bad | -6.38913 | -52.72444 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d153a73d-c146-3894-b8cd-4a3feb9f7b8a | -6.38854 | -52.7281 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a7caa429-5c3e-38dc-8b61-f76d080dfaf7 | -6.13721 | -52.69669 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 896f9124-05d4-3ec5-9ff9-b2f2f83a5c71 | -6.13662 | -52.70041 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2f7a40c-7d9f-3eff-81af-f594d37d00c5 | -6.13603 | -52.70412 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44657f42-b395-3ab5-a393-091491d3b343 | -6.13439 | -52.69248 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62d3e9da-401c-3f6d-835c-2aa60bcee614 | -6.1338 | -52.69617 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 385703dc-fb1f-33ce-bfb0-49db5d559382 | -6.13321 | -52.69987 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f416360-9747-319b-9b3d-f5ccb02d2c56 | -6.1304 | -52.69565 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d415b05c-5bf2-3033-920b-0fed511898f5 | -6.12981 | -52.69935 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f2ead7d-e7b8-3de8-9ab1-9a7cfdeee025 | -6.12758 | -52.69144 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85d5f40c-c415-3495-9fbb-ed6c8031286b | -6.12699 | -52.69512 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc2837aa-3e4b-3492-9065-a3fd30dff3ff | -5.96335 | -52.40042 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80c45991-689d-31d4-855f-7e5efd161bc8 | -5.91308 | -52.56369 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4670cef6-a998-329c-bb90-a480abb38b36 | -5.9125 | -52.56735 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 797692e7-00f1-30ed-826b-91502ac59767 | -6.45618 | -51.71183 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfa4fcce-4835-3343-9f66-a5692f4b12ed | -6.45563 | -51.71532 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33c8f6ab-2f30-37e6-9cd0-875b86a66443 | -6.44513 | -51.65288 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf558e7c-3ccb-3994-8ecd-138d51ce9503 | -6.40753 | -51.71874 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7a50d82-83a8-3394-baf1-0ad7fed42cf7 | -6.40532 | -51.73273 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e9fcd75-e3ee-32d6-917f-60aebac90761 | -6.40531 | -51.7112 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41cffff9-a496-32af-98e8-32d162af29ec | -6.40476 | -51.7147 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 657b2cb9-b3a5-3afa-9b64-327a18d1691a | -6.40421 | -51.71821 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 14ef2b42-3fd6-3c38-9b7a-5dbd630c4260 | -6.34776 | -51.70932 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66b7d16c-29ff-3902-ba60-c18fd9fee8ea | -6.20686 | -51.50478 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 266cadbc-b4a8-35be-aa45-3cadcf53c02b | -6.20631 | -51.50825 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea5cf45c-c726-3f91-83e8-24a923132f84 | -6.203 | -51.50773 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a37a8924-5ee2-369d-a521-b3b60cd64724 | -6.20245 | -51.5112 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72cb1592-0232-3d67-9fe2-4ceb84983c4b | -6.19804 | -51.51762 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f11b2c10-c518-3cda-bbcd-386114d61194 | -6.1185 | -51.69776 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91c49e62-c25e-3aaf-82ac-8c8f32f89172 | -6.11518 | -51.69723 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04c2df54-b55b-3b63-a0bd-8e1b12ecd4b9 | -6.05396 | -51.52687 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad325abc-33be-3826-99d4-b1f72656a70d | -6.04448 | -51.37238 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae1422e8-b111-38dd-8d87-2319262813e3 | -6.03954 | -51.2082 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c132c0a6-c858-3e1f-9e85-e0402a795ab1 | -6.01943 | -51.35741 | 2024-10-10 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e33927b-e17e-3df5-b919-047ded03d1cd | -5.97472 | -51.78979 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de4a493c-f7e0-315e-a6e6-8c277bfed1ea | -5.94072 | -51.59762 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c7f00df-ea11-304e-bfac-c6a858d00892 | -5.94017 | -51.6011 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63a2efdb-6222-3a93-a161-30a9c1d8d155 | -5.927 | -51.27594 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df19a16d-195e-31e4-b605-f8255ff0ff73 | -5.91466 | -51.44044 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a3a43d2-6c66-344a-9f78-11522204d275 | -5.83408 | -51.62794 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aac23d17-e753-390f-9507-43676624dc79 | -5.81524 | -51.53214 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8c3e2a5-f845-3d3f-b9d3-a401aebc7aca | -5.76157 | -51.44138 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ada2542-8744-3b56-a2ab-de82f91fde1f | -5.76102 | -51.44485 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe50a593-01a4-3afb-84b5-3f807c89def8 | -5.76048 | -51.44832 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf5f0fb1-378f-3782-9996-d077b71d66ae | -5.75993 | -51.45179 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ffdbfbb-4692-31a0-b780-a13c4f51d04f | -5.75938 | -51.45525 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdb54af1-fed3-33f5-a8ac-16eb6c209516 | -5.75883 | -51.45873 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a13a003-c560-3d95-afe9-2526294361b2 | -5.75771 | -51.44433 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbf0786a-e625-3799-9c73-075a8668e34e | -5.75716 | -51.4478 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1e6859e-492d-3b3d-a39b-f6e48897a540 | -5.75661 | -51.45126 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed38c776-5c5b-377a-9c6c-f668eb4c8f92 | -5.75606 | -51.45473 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bda91c73-2155-38d0-a6f8-79215b046aa4 | -5.7533 | -51.45074 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6b78101-c7a4-3756-b123-210389ba7062 | -5.75275 | -51.45421 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02785259-3721-3f4f-ac55-6b0cd8efa6c4 | -5.63546 | -51.20844 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1259b0ec-743e-39d1-b889-8f32e9019ef6 | -5.63491 | -51.21189 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4cb4497-2355-3595-b5fa-ce465656eeae | -5.59924 | -51.69446 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 194b3de2-9153-3c0a-9375-15c87a6e12af | -5.56047 | -51.61666 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 385b5c8d-36b9-362f-a3dd-cee5fb82ea2a | -5.55991 | -51.62015 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a78a5a39-c3c3-3f23-96dc-2713a6126b80 | -5.55686 | -51.6194 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ea14a15-a60f-3eea-8eec-c52f588cae14 | -5.52951 | -51.34044 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa1fcb50-0e3d-35a7-afbe-7ed1129b9ce6 | -5.46028 | -51.177 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e9ac008-41bb-3ef7-9175-ef1ce0232bef | -5.45243 | -51.09789 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28de6a55-2ef9-330d-b5b4-8158222a465a | -5.33582 | -51.57763 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a1a0f72-44c7-30be-b633-e48ae35c0cf7 | -5.07475 | -51.95547 | 2024-10-10 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d48717c8-74a3-3961-92ff-83b135a4f0d6 | -5.07418 | -51.95904 | 2024-10-10 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b73f30d3-6e95-356a-b2cf-6fd7ed363bc9 | -5.0714 | -51.95496 | 2024-10-10 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55147bda-5af6-3d39-a95a-c4a939c7f157 | -5.06925 | -51.95441 | 2024-10-10 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 316a73b6-725e-3096-a554-581d7ac70e5d | -6.972 | -51.6083 | 2024-10-10 04:44:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7bca28b-7af2-37bc-b25a-cb1f350fc5e8 | -6.95927 | -51.58138 | 2024-10-10 04:44:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1ee4c25-1bf0-3ca8-a914-501be4c3bfd7 | -6.85963 | -51.50176 | 2024-10-10 04:44:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcb64b30-2516-335c-9863-99276f004521 | -6.53964 | -52.59498 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c43e4b48-6810-3dcb-baaa-06a94c021f3b | -6.53287 | -52.5939 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d91723c-cd62-3cf7-810c-e4722f826cdd | -6.53229 | -52.59752 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fee5541e-300c-3283-85df-42b72482f01d | -6.52949 | -52.59336 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f567d3e-a6ce-3336-834e-24f3328e2572 | -6.47061 | -52.60653 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f8e6fbd-f66b-3769-9287-09e8dbdc58d4 | -7.91389 | -52.35428 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 450d42c0-69b2-396b-aec6-202351281299 | -9.33993 | -52.55152 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 562fde83-b3bb-3a26-b6d9-d17a4fb9c028 | -9.33442 | -52.54327 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b09b53a5-992d-354a-9b47-663afa24b262 | -9.33327 | -52.55042 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dde1ecc-2ff3-3285-8479-a927bb2daf25 | -9.06671 | -52.96112 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 287efc39-3712-3155-81e9-be46bfcf1d70 | -9.04522 | -52.98723 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b17cb20d-b176-3cb6-8b97-c6c0d0c879ad | -9.04244 | -52.9831 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba13ef17-06d9-3009-b5c1-20988c7d5d05 | -9.03966 | -52.97895 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0ec0133-e83a-3d2e-b2e3-c6151c1476d8 | -8.98719 | -52.80059 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9241b36-981c-355b-8b5d-f7cfb8dfa7ac | -8.98442 | -52.79642 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbda3dfa-b2c8-3b68-924e-264b548906cd | -8.98326 | -52.80364 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2253a214-22bb-327e-8ad2-577a2112562d | -8.98221 | -52.78878 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 007e951d-4041-38ba-aa47-085f45e288ff | -8.97656 | -52.80253 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README108.md)
