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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0661072a-05ca-3f94-98c5-dfbd774d1794 | -17.04823 | -56.69521 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a7d1848a-8895-35a6-9d84-c0fb5669eb44 | -17.03988 | -56.68299 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 7fcfe0f8-20dc-3e74-a7a3-445f8876e929 | -17.03924 | -56.68848 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| fb2a631b-be91-33da-9941-0efe3f6fef45 | -17.0386 | -56.69394 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 072e6e12-fd58-3cb3-bc23-6fd6f5e95e31 | -17.03796 | -56.69941 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 86da6874-42a9-3fda-8543-e7b167c166a0 | -17.03443 | -56.68784 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| b4b0e79f-1423-34a9-8c3a-971a548231ce | -17.02961 | -56.68721 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.5 |
| de9d89d3-8886-32f0-8a16-a35ce2210ad0 | -17.02898 | -56.69267 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 2c9a30f4-890c-3ef6-a203-1da6755f190b | -17.0248 | -56.68657 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.5 |
| ab8eb0da-5658-3184-bef7-2a70d3ef41c8 | -17.01454 | -56.69075 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 328b9ff4-be66-3a0d-917d-06f9ef89aaa1 | -16.96939 | -56.1475 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 78746d8b-9141-38f4-a963-b43994b258b1 | -16.96441 | -56.14681 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b917c93e-4a22-382c-a808-50b02f25696c | -16.93325 | -55.84067 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1e55999a-2e1e-323b-9565-0fe4b66b11f1 | -16.92887 | -55.83384 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 689459de-c4bb-3f5c-960b-41d5e168910f | -16.92851 | -55.83694 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 65205a62-add0-30af-a3a1-2ce99722b293 | -16.92817 | -55.84001 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4439b7a7-1881-3fe9-a823-7bb496fb9586 | -16.92483 | -55.82387 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4a05b86d-e23d-3614-aac5-e21aefc22281 | -16.92448 | -55.82698 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 90729c8d-9501-3a78-94ff-6723ca399b07 | -16.92413 | -55.83008 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 93474d71-bda0-3db5-80cb-cf1000ccffee | -16.92378 | -55.83316 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 17507109-79c4-3ee0-8b3f-e78c149010f6 | -16.92343 | -55.83624 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 55d629ac-a544-3455-b280-480a1d39ee1b | -16.91974 | -55.8232 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dcecf0da-9224-3396-bc39-da81a810be79 | -16.91939 | -55.82631 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 751bb57e-e788-30d6-ab35-4085d2acc662 | -16.91904 | -55.82941 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1d318911-43e9-31db-b57c-169b8aa39c57 | -16.9143 | -55.82559 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d0fcdbd3-3ead-3dfd-855e-9cd780c8a270 | -16.68894 | -55.49587 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d768d8bc-3211-3591-87a5-529d54f6143b | -16.68417 | -55.49157 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b0c62524-7b5b-3513-b72c-a8a14ffc6943 | -16.68376 | -55.49512 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5e48d6ed-cdae-3ff8-9bfd-aa88f7a697b6 | -16.67899 | -55.49076 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1f5e7fae-8249-3c16-b003-6c65aff664e6 | -16.67754 | -55.54897 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7b4f1768-bc71-34e3-8186-f60efa99ebfc | -16.67272 | -55.5453 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| da9ba179-174e-30af-b3bb-d1ea4a97ad90 | -16.67236 | -55.54842 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 09f3d3f6-9a25-3272-98a0-000b2095d486 | -16.672 | -55.55153 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c93e888d-f333-3fd7-ad7e-5e2870903c1f | -16.66752 | -55.54489 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 01f38319-ba29-33c9-8f85-7916d863f663 | -16.66717 | -55.54795 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bfbb067d-ee30-3af2-929c-c7aa397ddb80 | -16.66682 | -55.551 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 01b968c0-84b0-3392-9467-ff7c75d227a7 | -16.663 | -55.53859 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 562f80ec-1690-346c-9149-b91f978e0633 | -16.66266 | -55.54154 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f40f08af-1808-38c3-aa08-5c7f1dd9d1a3 | -16.66232 | -55.54453 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f396cdec-83f5-3cda-a3bd-cccd3a24a7c3 | -17.15256 | -56.14851 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 774b5a92-f9f2-3507-ad14-f95cf41e3a13 | -17.15233 | -56.14852 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f65e1612-ba7e-3a9b-976d-ba950f8252af | -17.15125 | -56.16039 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 093223ce-2eb4-3909-a3f0-d60d53ff0600 | -17.15094 | -56.16037 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5a4d9373-5aa8-3558-8fae-174307941a8f | -17.1506 | -56.16632 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f1b058f7-742c-330a-ab9f-01643ed5c85f | -17.15024 | -56.16629 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 811d0196-eee5-3035-85d1-0630c3168e18 | -17.08454 | -56.67781 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 27428aa2-973e-3555-8118-30709946fa04 | -17.08373 | -56.67828 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6a48480f-6655-3324-a652-73c42afb996b | -17.07841 | -56.6881 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e58d1c62-39ab-3431-a1ad-391985637801 | -17.07425 | -56.68201 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a4fd4da4-4ea5-34dc-b6d7-540b3bca47e2 | -17.06943 | -56.68137 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 9a7fdcc1-0209-3239-8f02-aa7e021a039d | -17.06048 | -56.06206 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 857eae2a-64f2-3e8f-b9cd-43a0c6449b71 | -17.06027 | -56.06405 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 976e054d-32d7-3900-ae96-376dd6ad16fe | -17.05956 | -56.07003 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0a5cb9ba-8099-351a-b765-17d61a138986 | -17.04887 | -56.68975 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 9e989562-1a5d-3688-8d1c-6c2ece0ac334 | -17.0447 | -56.68364 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a387fe08-17f0-3f4d-9cb8-07394c84d586 | -17.04406 | -56.68911 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a8bbdf53-03fa-329d-b931-e383183dd918 | -17.04342 | -56.69458 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0137d468-cbce-3d8f-bd47-df678c3f2cd5 | -17.03506 | -56.68237 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 237cf14b-b1a0-32cc-9a83-cb24dab08e7e | -17.03379 | -56.69331 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b8d0df03-3273-308c-a0df-005ca50c74e5 | -17.03315 | -56.69877 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9450cac7-b149-3f10-983c-1b83f7f83f4c | -17.02834 | -56.69814 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| cf939dd5-7874-3b14-94d5-0c33ef48f2c0 | -17.02416 | -56.69203 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| d1085f64-c9e1-3748-90d9-f63f049ca3f2 | -17.02353 | -56.6975 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 5163ce48-0487-3a33-a461-a953d3ad9565 | -17.01998 | -56.68592 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.5 |
| 8f0d86d4-2948-3684-81d5-7245bab1f987 | -17.01935 | -56.69139 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| c5990beb-3274-3475-a8d2-6aa31782fccf | -17.01517 | -56.68529 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.5 |
| 3cceac9f-8453-3a18-a819-300e0b0005dc | -16.98368 | -56.15536 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 64a0d64d-5b7c-3ee2-afbd-581bcf2582d3 | -16.97869 | -56.58396 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8df04f50-65c8-38fb-8385-7f5d4d2b5a7b | -16.97803 | -56.58949 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 230f8e9f-fc3f-3e2e-9092-40fa16bb3e54 | -16.92782 | -55.84308 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6ae3f705-0d96-363f-be00-2062c58f862c | -16.92308 | -55.83931 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 55eafe83-51ba-37ac-874f-31d55f39b6bc | -16.89962 | -55.86444 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| dd1d2bb3-e3ba-3db6-81b8-14ac346024d8 | -16.81906 | -55.90431 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| daf7098f-aa37-3343-ad6d-051ef14eeb45 | -16.81505 | -55.89449 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d690b9d5-faa4-3932-83be-381a9af9861e | -16.8147 | -55.89753 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1268d281-a78d-35d7-8863-3c87447fc09d | -16.81435 | -55.90058 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cff86fd9-1c16-321f-81b9-5abc0b3abe5e | -16.68589 | -55.91161 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e28fc95a-366e-3920-851a-bd1388615460 | -16.68555 | -55.91464 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4ec6133a-f779-37e5-bf9e-abb3db3511bf | -16.68119 | -55.9079 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f3627d3c-597d-359b-8922-fecfb08e9d44 | -16.67076 | -55.90958 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6e635403-a33d-3bf6-bfd2-eca875441941 | -16.66605 | -55.90591 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 54887a91-c5af-390f-8cbc-ed748a7360d1 | -16.66571 | -55.90894 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 41f829fb-d144-3d51-aef0-10d1de0dd4a7 | -16.62538 | -55.90892 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 83c31a97-b505-3ea4-8d0f-e60287fe4151 | -16.62034 | -55.90825 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| acdc4a98-151f-389a-b4e0-cc45937e3b53 | -10.37878 | -55.63615 | 2024-10-05 05:31:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3456d735-14e5-347c-a5b9-4ff70091c0b1 | -11.90716 | -56.9386 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4939cf13-cdbd-33f0-9ec3-3cd3b01996bb | -11.90682 | -56.94057 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4bb9031-5a34-3cfa-b44c-462e47c7229a | -11.90656 | -56.943 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9347672c-4691-3f08-b383-cc8336c5a696 | -11.90625 | -56.94498 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0207248-54cf-3035-bc98-78ba052c6409 | -11.90596 | -56.94741 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d584f38f-c490-3f2b-bff8-f1f67572abf9 | -11.90568 | -56.9494 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1c2c93a-aae0-3572-8386-53a836de0885 | -11.90535 | -56.95181 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7177cf1e-e258-31d5-a6af-a12fd1c62283 | -11.90511 | -56.95382 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d85749b-b5e6-310a-874f-667f837e51c9 | -11.90475 | -56.95621 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35b183ca-3699-39ea-8fc8-d8ac41869048 | -11.90276 | -56.93795 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 582ebe4c-a1a6-349f-8d70-42372393b54e | -11.90242 | -56.93992 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d60cc3d-ad77-3a60-bea9-baba6d25a023 | -11.90216 | -56.94238 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 913531de-b4d5-3aca-ad7d-853fae6b3025 | -11.89957 | -56.92849 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab5029c7-24ef-31f9-a4be-45fec5df8f8f | -11.89896 | -56.93291 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 086c0211-7a1f-3ca8-8fa7-b33cce23fb21 | -11.89836 | -56.93735 | 2024-10-05 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README139.md)
