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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f7934d3-aa58-3885-a582-3a7ae08409f8 | -14.48236 | -58.6336 | 2025-07-12 02:02:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 003ea737-aad0-3582-8c81-40e510b259a2 | -14.49239 | -58.63873 | 2025-07-12 02:02:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 241806a2-d3bc-34cc-8270-004211806438 | -9.96691 | -64.95071 | 2025-07-12 02:02:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 8cd76c74-0f5a-38ce-81f6-873a245980c6 | -16.2708 | -59.546902 | 2025-07-12 02:03:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49638416-6c2d-32d6-8848-67c2354f1ecc | -16.274799 | -59.562199 | 2025-07-12 02:03:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f55f2e7-6e26-32f5-b975-e7a1cb290dc0 | -14.4524 | -58.635201 | 2025-07-12 02:03:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ad8db5a-bfa8-39c5-8619-2f6e17a3d44b | -14.4575 | -58.653999 | 2025-07-12 02:03:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f88daaae-3dcd-3694-b5e9-d1150ea3831d | -9.9329 | -64.9562 | 2025-07-12 02:03:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d4bb4cc-d234-3fd5-a4aa-f7bae749ec55 | -9.935 | -64.964996 | 2025-07-12 02:03:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a007ed57-9179-3e21-93e3-325a8072a735 | -10.8986 | -49.204 | 2025-07-12 02:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 3d7469eb-cbf7-30da-b3f1-1c003534d1de | -5.8412 | -48.3964 | 2025-07-12 02:10:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 054254cd-791d-3146-b578-6538fd178459 | -5.8412 | -48.3964 | 2025-07-12 02:20:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| a334abc0-9f7f-3d19-af0f-943e9e7dba05 | -11.7245 | -47.4543 | 2025-07-12 02:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| a8248dd5-ebe4-3bdf-b8c5-6c9cc9849118 | -10.8986 | -49.204 | 2025-07-12 02:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 54e43bc5-a821-317d-a9ac-b651fd7e9973 | -10.8432 | -49.1018 | 2025-07-12 02:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| c16b85be-f8a2-3de8-a2d0-d5e5250f458d | -10.8986 | -49.204 | 2025-07-12 02:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8e95f889-47f9-3d71-8059-5f26fa9f0ea4 | -10.8432 | -49.1018 | 2025-07-12 02:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| d141f52d-a820-39db-a0e0-279d872ae43a | -5.8412 | -48.3964 | 2025-07-12 02:30:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e0f7e3dc-4347-341e-b818-9987ddf267f4 | -10.8432 | -49.1018 | 2025-07-12 02:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| d90e9923-665a-3e32-9ea4-c4785bf43ed8 | -10.8986 | -49.204 | 2025-07-12 02:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e7ed9903-3d70-38fa-895d-b24371cc51f7 | -10.8986 | -49.204 | 2025-07-12 02:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 3b732cef-836c-3063-b8eb-80d83451c2ce | -5.8412 | -48.3964 | 2025-07-12 02:50:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 935570f1-aa00-3615-b62e-11faffce5132 | -11.7241 | -47.4766 | 2025-07-12 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 313f4956-7c3f-358e-81b1-db99d94ccb0c | -11.7245 | -47.4543 | 2025-07-12 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| fe1ca6b5-ae1e-34be-8e34-96d82b1abfbf | -10.8432 | -49.1018 | 2025-07-12 02:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e2616982-c771-329b-bad1-91d7a8e7e532 | -5.8412 | -48.3964 | 2025-07-12 03:00:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3f10e768-8882-38a1-898a-a095eb033802 | -10.8986 | -49.204 | 2025-07-12 03:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 2a72df73-3be4-34b6-8555-528344e6a869 | -11.7245 | -47.4543 | 2025-07-12 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 50d5e439-491a-3df5-a198-ea0801573cb8 | -10.8432 | -49.1018 | 2025-07-12 03:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 6f4e01b6-d38a-3922-9c78-69e7f53267c6 | -10.8986 | -49.204 | 2025-07-12 03:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| f96c0e2b-90ea-3567-af83-83f640b374ca | -11.7245 | -47.4543 | 2025-07-12 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 522746dd-8abc-36a6-b14b-d633ecba6717 | -5.8412 | -48.3964 | 2025-07-12 03:10:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a78d9611-bc9d-36c2-9113-f9f8f7263dbc | -10.8986 | -49.204 | 2025-07-12 03:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 9b712244-9cba-3b57-bb71-3d75e59130a3 | -5.8412 | -48.3964 | 2025-07-12 03:20:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0626293b-1383-3770-becc-ddce958c295c | -6.7194 | -44.3231 | 2025-07-12 03:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 20ee6ddb-2a0f-32ff-869b-d182e094ef63 | -4.5156 | -38.5511 | 2025-07-12 03:23:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1dfc08ea-23d1-3bf5-b6d6-a104133aa266 | -4.51612 | -38.54805 | 2025-07-12 03:23:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ea6913d-104c-3764-a470-aaf7a8e5ad41 | -12.41333 | -45.35257 | 2025-07-12 03:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2a06e8d-b41a-3c45-b131-880c0aef8c05 | -11.46645 | -45.11217 | 2025-07-12 03:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59027bb4-324f-3307-a520-0ee9d4c04900 | -11.45964 | -45.11039 | 2025-07-12 03:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f408e133-bf58-3301-ac12-cc70ab882694 | -12.41448 | -43.49509 | 2025-07-12 03:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dea86337-e34d-305c-aaae-2fa092da08f2 | -6.85109 | -42.77353 | 2025-07-12 03:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a25c0268-ea69-3b2b-ba96-766b9f34283b | -12.42165 | -43.49155 | 2025-07-12 03:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e6e5d72-2d97-3bca-b316-725d5ab44316 | -11.89578 | -44.89558 | 2025-07-12 03:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3aa8deb-68f7-3b4b-8cc2-b4de0cc88032 | -6.18715 | -42.14579 | 2025-07-12 03:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e64b8e31-8c7c-3370-be7c-4ee20061687b | -11.46487 | -45.11396 | 2025-07-12 03:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d82520c1-19a6-3be9-8138-2d7944d05b4e | -11.89479 | -44.90032 | 2025-07-12 03:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb038d4a-44d2-3b7c-9ec0-5310bb24e806 | -6.27728 | -43.4187 | 2025-07-12 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b3af044b-925e-3055-8f25-bc9b7a6f8bee | -12.41653 | -43.48525 | 2025-07-12 03:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 020653e9-b329-3f2e-bb4f-244314a8a143 | -12.41673 | -43.49417 | 2025-07-12 03:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bbe1476b-308c-3513-b8be-77c35656a5b2 | -12.41551 | -43.49016 | 2025-07-12 03:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 374fe42b-5265-3559-b48c-d3ca9c521b1b | -6.27045 | -43.41763 | 2025-07-12 03:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9a4b90c3-2af7-35de-ac23-922e8d7ba89d | -6.18623 | -42.15083 | 2025-07-12 03:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4da0ce25-96a3-39a6-a5c7-13a3dad25990 | -12.42014 | -45.35431 | 2025-07-12 03:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f72942ac-9eae-3cb9-aae9-c486cf5f53db | -12.41772 | -43.48925 | 2025-07-12 03:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2019ceb-0bc5-3a59-bb33-5537fbb481ee | -12.41195 | -45.35907 | 2025-07-12 03:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bcc77a22-cb98-3411-92c1-f5dafb59bdcd | -6.18408 | -42.14831 | 2025-07-12 03:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8e6f452d-8856-3ee4-937d-01a16d323566 | -12.99152 | -44.87595 | 2025-07-12 03:28:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62fde441-314e-34fe-a99c-35a27bab4fd5 | -18.32347 | -47.63926 | 2025-07-12 03:28:00 | NPP-375D | TRÊS RANCHOS | GOIÁS | Brasil | 5221304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0b5890ad-9913-3550-bc05-9e86e7fb8547 | -12.99926 | -44.87198 | 2025-07-12 03:28:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f98f96c5-72e5-3c6b-9be0-9d17ee05c139 | -5.8412 | -48.3964 | 2025-07-12 03:30:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 98a94880-cb20-30a5-b273-f48fca0fd7e7 | -10.8986 | -49.204 | 2025-07-12 03:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| be07183d-b924-3172-af96-75221fa89bb0 | -5.8598 | -48.3953 | 2025-07-12 03:30:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b8b60b7c-9f42-3ce4-9419-6da3508dbdc8 | -10.8986 | -49.204 | 2025-07-12 03:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 6296a2f5-76c9-3087-991f-e38e723938e7 | -5.8412 | -48.3964 | 2025-07-12 03:40:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 5cde7f55-6d14-38cc-aecd-cab5c96e351b | -8.47261 | -49.61649 | 2025-07-12 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8ffd3eb1-cdd9-310e-b1d6-3c6d9bd8e13c | -7.68383 | -44.37534 | 2025-07-12 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fa74222-2cef-3869-884d-3597e1a7c309 | -6.85395 | -42.77281 | 2025-07-12 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 483c503b-15fa-3f82-972d-463b97e7cb42 | -5.83896 | -48.3871 | 2025-07-12 03:47:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d2b6899e-6d7f-3533-84cc-40ac899be4b9 | -9.51657 | -47.56765 | 2025-07-12 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdab86b3-3a22-3b94-9186-a1f5eef9dd66 | -6.71155 | -44.33056 | 2025-07-12 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78551788-c3ab-3d12-ab93-61a577a81bc3 | -6.71625 | -44.33138 | 2025-07-12 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 116f3d4b-fde9-3453-aa64-82f5a1da5b2b | -7.08092 | -49.60666 | 2025-07-12 03:47:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88ff2b11-468a-3959-b027-631fb70ddac4 | -8.37446 | -44.03648 | 2025-07-12 03:47:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8252a378-0b33-3640-97a2-82cb73e2662d | -7.47697 | -47.51625 | 2025-07-12 03:47:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78086e2f-ef21-3aaf-a006-62e29bdb42b2 | -6.6244 | -43.361 | 2025-07-12 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 42364b74-90aa-3d99-b210-fcca19e4cc53 | -8.46514 | -49.62065 | 2025-07-12 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f665e927-59a6-3df1-97ec-fb2417b63ea2 | -6.86662 | -42.77486 | 2025-07-12 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bf1ba7f0-fbf2-3503-8a93-b520a33e02f4 | -8.47157 | -49.62183 | 2025-07-12 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7cfbc98e-60bf-3469-ac4c-d69ed77b35c4 | -6.63514 | -43.21795 | 2025-07-12 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e110e87e-5949-31b5-bc7a-0cd0ed4840e4 | -8.68188 | -47.98952 | 2025-07-12 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71f04378-ed92-3237-b516-a11e315d751f | -7.23192 | -43.10559 | 2025-07-12 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f09f635f-740d-3167-a550-40842ec58c58 | -7.18573 | -42.98948 | 2025-07-12 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a715f5a-81dd-3e63-91ed-0068af8b6409 | -6.70998 | -44.32891 | 2025-07-12 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 636921f4-46c2-3019-8b2a-21878dd72469 | -9.50473 | -47.56934 | 2025-07-12 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf0527b2-4e4f-3d47-b8bf-ca088c8c11be | -5.83803 | -48.39229 | 2025-07-12 03:47:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| ac9d4152-1da4-35f6-8749-37e560dc352b | -8.47071 | -49.62339 | 2025-07-12 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5c77333a-f581-3e92-b30b-d180e43851e1 | -8.92104 | -47.34978 | 2025-07-12 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9622023a-7572-3745-987d-feb2d927d38d | -5.84956 | -48.39969 | 2025-07-12 03:47:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3dafa97-3a42-32bc-85b2-a511d3ba703d | -5.84333 | -48.39856 | 2025-07-12 03:47:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 99af453b-1534-3fc0-a765-02f5ce83cbba | -9.50543 | -47.56562 | 2025-07-12 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 231fa617-e61e-328b-8e34-a65fc900cec0 | -8.22918 | -47.55903 | 2025-07-12 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79d4f140-829e-35d7-84f5-0758d5eb2da7 | -9.511 | -47.56663 | 2025-07-12 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d830f946-0dc5-3746-be1c-48fa8b75b083 | -7.08185 | -49.61018 | 2025-07-12 03:47:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4979f793-536d-3644-9e88-a3a48ab36129 | -8.68769 | -47.99051 | 2025-07-12 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec2d2d24-9e8c-3285-a4b7-2014a11a3fef | -6.71469 | -44.32973 | 2025-07-12 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 553ab1bf-3352-3d3c-913a-b11d53facfab | -4.09415 | -40.98333 | 2025-07-12 03:47:00 | NOAA-20 | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4e6f2b7e-1fe0-3ee7-802a-3a0985628437 | -8.92173 | -47.34607 | 2025-07-12 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5191a8cf-ccda-33c2-9e8e-a0cc09d4cbcf | -7.18356 | -42.97666 | 2025-07-12 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b869c59d-0dab-39ae-9d94-4db4afe7c1ff | -8.47171 | -49.61801 | 2025-07-12 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README6.md)
