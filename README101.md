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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f52166a-9008-3049-ab65-771340e58087 | -2.87162 | -50.75543 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7fc70cb6-414f-372f-a29a-5492a9780619 | -2.86998 | -50.74071 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c1503e8-b840-3db7-a396-d360d4c5517b | -2.86926 | -50.74541 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ed3dace-523f-341f-a032-596d21ce2f70 | -2.86543 | -50.74483 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae0f631f-3d8c-3671-a021-1da92e860144 | -2.86471 | -50.74953 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a6b4b87-b2c1-3c85-bd8b-dc02bb6a5201 | -2.86325 | -50.75894 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37e7b274-36f2-3ed4-8a09-c4fc5967c311 | -2.86089 | -50.74895 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| faf64d8b-2a93-37f2-895c-23c645314783 | -2.86016 | -50.75365 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 81d9238f-dd3b-3816-afa0-7ae4df9bbe1a | -2.85852 | -50.73893 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f2b3c6b-0d45-3fe8-87ef-f03fc3d40fc2 | -2.85779 | -50.74365 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3144a8a6-80c0-3055-96da-42880cb96658 | -2.85634 | -50.75306 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f9029c2b-8f1f-38f9-a39c-83c4c7fe8f6e | -2.85562 | -50.75775 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65c7012e-1d7d-3f6f-9779-48dedff6d4ae | -2.85015 | -50.74245 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfd17a60-bac5-3760-af56-4c88b2b5a9e0 | -2.88366 | -50.72828 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a79c8c63-04f4-35c6-9667-7625aaf2cb3d | -2.88292 | -50.73301 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d24ee9b5-610c-334a-ac41-10d2cb2b9212 | -2.88276 | -50.70878 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 907b0d26-d765-304f-8bda-e0ef66a7c8de | -2.88203 | -50.71353 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c466819e-4a10-38d8-8271-097441db3c0e | -2.88129 | -50.71825 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 123d80d6-0616-312b-9c33-5c6cb1320043 | -2.88056 | -50.72297 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb1ac8fe-c659-366a-9000-8aa3d374e79a | -2.87893 | -50.70819 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e1ff868c-5aa0-3327-8eee-fb50922a7bf0 | -2.87836 | -50.73715 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8548254e-acb2-3520-8047-dc54c0f9910d | -2.87747 | -50.71766 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9230772f-8457-3bde-8290-a03d6801ac62 | -2.876 | -50.72709 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f1db9b78-33ab-3045-8188-65c6b50736b3 | -2.87527 | -50.73182 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 10900c80-b348-3fde-98bf-c09f23c983e7 | -2.8751 | -50.7076 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6c3b004-e461-3477-8a2a-c9540b02bd12 | -2.87454 | -50.73656 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dfbf2891-598e-3d49-9243-c8492517af57 | -2.87437 | -50.71234 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 00b046c7-456f-314c-8944-ffdae9376ec1 | -2.87364 | -50.71707 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 39466887-6a54-3611-abb5-959b9cc38208 | -2.87291 | -50.72179 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 4905544b-e4ec-321b-b424-1fc7f83d1bbb | -2.87218 | -50.72651 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| e741bbdb-2592-3466-b57a-ae2b759f8622 | -2.87145 | -50.73124 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| a54a1938-265e-3d91-9b7c-700886512ac9 | -2.87054 | -50.71175 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 32271870-e59c-37cf-8203-ecfdaebc0427 | -2.86981 | -50.71648 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 84e49b7f-6c23-3ae5-8b74-1c30a63356eb | -2.86908 | -50.7212 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| aa94e9bc-4424-3c33-95db-6b15875702ea | -2.86835 | -50.72592 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 6230c14a-f97c-3325-8f17-90c9fd81eca6 | -2.86762 | -50.73064 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d8ee7def-5904-316b-940f-cd7d5907ed2c | -2.86671 | -50.71115 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a822bdce-cb80-3449-924d-6585119b1067 | -2.86598 | -50.71589 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a0fb7f5f-6564-36ae-b7cd-d29b065dfb3a | -2.8638 | -50.73005 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d6f76ddf-0f93-3650-bdd6-56f7cf1561ae | -2.86307 | -50.73479 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5f192610-6d1a-3b2a-aa0e-47d0eff1aba3 | -2.86215 | -50.71529 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a127c0fa-5ea5-3d1f-92bf-d0d23e1efb7f | -2.8607 | -50.72475 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 241.6 |
| 549bdd33-bbbb-3955-a12a-f3bbc42c1706 | -2.85997 | -50.72946 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3625703b-5045-37bc-be04-c7d6a5b79cec | -2.85832 | -50.7147 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29820936-c29b-3fdc-9b77-ef403944d77f | -2.8576 | -50.71943 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f3f752fb-b481-3711-9508-8c3bcc33ff06 | -2.85687 | -50.72415 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d70acfa6-20fa-33ed-b398-64e54a2dbf1f | -2.85615 | -50.72886 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 3cca7af2-99dc-3442-9e24-50ec257103e9 | -2.85304 | -50.72356 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 0d21c118-94e9-3b07-a6e0-ae45d60ce9fe | -2.85067 | -50.71352 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32700d06-b2d0-3c4b-88c5-cac4274cc049 | -2.84994 | -50.71825 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1ffc0463-1978-333e-a60c-aa2e1c20017a | -3.30015 | -50.66446 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46b7fb21-990b-3b12-9801-b68185207354 | -3.29941 | -50.6693 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 393c05bc-85f9-3f2d-a3a4-c9411dac87b7 | -3.2678 | -50.66924 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60a3b8d2-eb3f-34b3-b7e1-33bd61aed518 | -3.26394 | -50.66866 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6b957e9-bc09-3cbc-8189-d1c19d486390 | -2.90604 | -50.67597 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4743cbb2-f512-3896-bd70-dbe211924fb8 | -2.90401 | -50.67316 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6aaf4c3e-d349-3bd1-807e-aa7f08cb6116 | -2.90327 | -50.67793 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 830b81d8-c40b-3870-81a3-d4557d895b65 | -2.90291 | -50.67059 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50f926b1-a54e-3b64-b7ae-fcbe06f612c0 | -2.9022 | -50.67537 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1579c4f-b3bd-3cbf-bfc5-7cd2ea948aaa | -2.90017 | -50.67257 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ce14e30-c111-33d8-bde2-d1cab533a422 | -2.89943 | -50.67734 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9461145a-9d2e-3a43-95db-e3ed7ec7ebd9 | -2.89836 | -50.67477 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7101343-39e8-35ba-b120-ce1c99914d3d | -2.88065 | -51.66727 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa99c5d8-0c3f-3231-bddd-b4c320f5df33 | -2.87763 | -50.74187 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5987a596-bc9a-3740-8590-76d0148b04a2 | -2.8769 | -50.7466 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cb523fe-e9fa-3169-bead-350fb1420e5d | -2.87617 | -50.75131 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1a1dc322-3e87-387c-b090-fd7470158a66 | -2.87381 | -50.74129 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd961f73-e167-3d1f-b9ff-f5f5dccd4613 | -2.87235 | -50.75072 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4fe26dae-5aef-3f06-b8cb-2486008c9552 | -2.86853 | -50.75013 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d20c15e-7b54-3b10-931b-40a39435efe6 | -2.8678 | -50.75483 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea4b670c-a608-3f1d-91ba-d5c2918df075 | -2.86707 | -50.75953 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 371fd302-f8d1-3dde-b1f0-6f1a1e06ee0e | -2.86616 | -50.74011 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 494d1900-d763-3dbc-99e7-3d59521b8429 | -2.86398 | -50.75424 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f57c694-aeaf-3e50-a226-a89b50eddf1c | -2.86234 | -50.73952 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b0a7646-7647-36f0-a46d-fe2a8970a230 | -2.86161 | -50.74424 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf1b2df1-7264-3f37-b436-3d06a98c9387 | -2.85952 | -51.65968 | 2024-10-01 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d16d8a27-dc07-30ff-9691-b1d91f09dd06 | -2.85944 | -50.75835 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c9450dc-ebbb-3ee6-b311-1ab737c75d6b | -2.85706 | -50.74836 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f2d51325-165c-3e2e-bc7a-5959c1a2863b | -2.85469 | -50.73832 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8069c2f-5c88-3186-85bd-70126cd827bd | -2.85397 | -50.74305 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b2dc9b9-b1d7-3ddb-a25b-79190ed8800d | -2.85324 | -50.74777 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0691fd36-1676-38a1-a758-f083da74a8ab | -2.8518 | -50.75717 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46eb2a6e-916e-375a-a328-a0b54889edd9 | -2.84942 | -50.74717 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 674e81e8-8bf6-342e-a3b2-3fc1df0c42ee | -2.91284 | -50.73535 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f7a994e-36eb-3ee1-961d-7fef974a31e7 | -2.91186 | -50.7158 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fd75326-3713-3996-830c-f6a98868c0ec | -2.90902 | -50.73475 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9583a888-de34-3e4a-bf73-9df17fc187c6 | -2.90874 | -50.71045 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e9659361-aebf-323f-9e4e-75139495da3f | -2.90803 | -50.7152 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4aa80534-e6d0-31a3-8ee6-5f9c868dc21a | -2.90732 | -50.71995 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35079c57-657e-3750-851e-8181175a49f1 | -2.90661 | -50.72469 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d5e74fe-39c5-3a51-a6bc-798b219223d7 | -2.9059 | -50.72943 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ed11012-75af-3e48-bae0-bf2d4a2e58a7 | -2.90575 | -50.71231 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97c55cc7-82c9-3da0-8aff-2b045e1e317e | -2.90519 | -50.73416 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f19dc66-e374-3b4b-85a1-f029f9a40936 | -2.90501 | -50.71706 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0465f9df-fae0-3960-8831-7c6f12aab3cd | -2.90491 | -50.70986 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8da4bef2-7b42-3f2a-90c6-c171c493693b | -2.90427 | -50.7218 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0267ba6b-b0c5-30d4-8628-9ed191549674 | -2.9042 | -50.7146 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 701ad16a-83a6-3c43-96f5-41083ed9a538 | -2.90349 | -50.71935 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 14e00769-76b3-3c14-a54e-e3c8c7a9c03e | -2.90278 | -50.72409 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5345b842-bdce-3f82-97a5-0d7dae0f71d2 | -2.90266 | -50.707 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README102.md)
