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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e5832e4-7e98-385d-8248-256862bac6fb | -7.89496 | -44.60251 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c68f3e5-c4df-3255-8e93-3f8c52b6fc03 | -7.89442 | -44.60598 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1dd23f51-7dfd-3486-8c11-2be107a17c40 | -7.89387 | -44.60945 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 538fb052-279d-3bee-a571-b19b8d9de2e1 | -7.89333 | -44.61292 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 388d3d40-bedf-3690-8df5-1c1534b9f58a | -7.89279 | -44.61639 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13c62142-4235-358f-a7e5-fa5904caac84 | -7.89166 | -44.60199 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b1570ce-08da-34e0-b5a6-ebc7a50df148 | -7.89057 | -44.60894 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48bc1850-7e9b-3e4f-bf20-6340405ff420 | -7.89003 | -44.6124 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c84dd88f-e595-36c6-98f3-7cff6d394a43 | -7.88949 | -44.61587 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0eaf458-e5d8-3dee-8994-e8b6c49144cc | -7.88836 | -44.60148 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 322b2297-a376-3315-b884-a776a421175f | -7.88781 | -44.60495 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0917a235-4982-37ca-93bd-ae8d646d1357 | -7.88727 | -44.60842 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5993495b-edb7-3a05-818f-9316af04cc81 | -7.88673 | -44.61189 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d44dc50c-f1e4-3942-bd8b-ba2d0e812370 | -7.88619 | -44.61535 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b649c001-0b42-32a2-82dd-4e03811f144c | -7.88451 | -44.60443 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c4bc948a-5ab6-38e7-bab7-ad25c41971e5 | -7.88343 | -44.61137 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f254d416-7a80-3817-9b73-398fae324fdc | -7.8818 | -44.62177 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 386d876a-4f4d-3678-8f5e-f7970f96626a | -7.88126 | -44.62523 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3e4c854-60d2-3862-a0b5-2a23b9d2852d | -7.88121 | -44.60392 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b94ab35d-d1f6-32f1-a842-dcfbce010c09 | -7.87958 | -44.61432 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0b675d0-6efd-3f36-8d13-ae1524b74bb0 | -7.87904 | -44.61778 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6f7c74a-3d87-35e8-a868-28e13cdab9f3 | -7.8785 | -44.62125 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e1ac473-b76b-35ad-86f9-40c881f98aaf | -7.87796 | -44.62471 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71f08f8a-e62f-356d-9889-21516863a47c | -7.87791 | -44.6034 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9ceb243c-ae81-3220-98a2-cfdfb5a8b13b | -7.8752 | -44.62073 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e44a169-c9b9-371e-bb5d-8fdda5fda0b6 | -7.87352 | -44.60982 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bc83b7f-62ea-37bd-a978-1e03ba907779 | -7.8713 | -44.60236 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7721a90f-98ae-35b3-87f0-8e5560e58853 | -7.87076 | -44.60583 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2eeead35-c3b5-33ba-91ae-694a3b339d88 | -7.87022 | -44.6093 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59a5b3ac-cdac-33c3-a2e6-4d10f42347ec | -7.86968 | -44.61276 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7b8653c-22ec-39a7-9d13-dc3f0211ed24 | -7.86914 | -44.61623 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f36e58d2-4c28-31c2-bb83-4e16897c23aa | -7.868 | -44.60184 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f321bf98-f8f0-32da-9dd8-428ef72916d4 | -7.86746 | -44.60531 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d70ba53-e494-3554-b222-043740499501 | -7.86692 | -44.60878 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d2748ec-4810-37cd-a278-e9a757961926 | -7.86638 | -44.61225 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 806ad1b5-e47a-3545-810f-e45090342970 | -7.86584 | -44.61571 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 915b839a-82be-32d7-b0c3-74f083d4c88c | -7.80718 | -44.90412 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3e6c2faa-1882-38e8-9181-f644c4c89ea7 | -7.80275 | -44.67321 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70c10f4b-d380-3762-a2ca-c94dda9ea151 | -7.80221 | -44.67667 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63495862-32d8-311c-b4c1-1b03ba24fadf | -7.80167 | -44.68013 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1590028e-44d6-343b-96bd-e79850254cc1 | -7.79945 | -44.67269 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b2f5806-0075-3f39-bade-f541747a9319 | -7.79891 | -44.67615 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e67bdc0d-8a99-3870-a011-6ec4c6a8eade | -7.79837 | -44.67961 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| baabfa6d-706f-3b94-b602-908cbd95b379 | -7.79615 | -44.67217 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f72c4c2a-37ed-3867-be30-802d8bf8adef | -7.79561 | -44.67563 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7962d3b3-ed37-3d3b-b6f7-37e2ba171919 | -7.79507 | -44.67909 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 56b3088f-06e8-3a98-8f33-2b43f55fc065 | -7.79285 | -44.67165 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c9f398c0-b72a-3aa2-8a5a-4bdf036e8caa | -7.79231 | -44.67511 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 28b7e2a4-18b6-38fe-a859-c7ffde3f021e | -7.79177 | -44.67857 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c773e512-726e-3b33-9d25-99764c74ff6b | -7.78955 | -44.67113 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2a69c0ae-f82e-3531-b920-c9b7ffa166f2 | -7.78901 | -44.67459 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2a0823f8-1a87-30bd-b7b6-edf6a399bb27 | -7.78847 | -44.67805 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| bc3cb16f-d19d-3292-9f84-8698dabe9d09 | -7.78793 | -44.68151 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| da63a879-0802-3550-a3ed-97ba661c427e | -7.78739 | -44.68497 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29918ee5-fe80-3a6b-8c85-0b078499f0c0 | -7.78685 | -44.68843 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1432e76d-2777-36b1-93e1-941b8b8e3a5e | -7.78571 | -44.67407 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12d762ea-0a8a-36dd-827f-9873598d6ec3 | -7.78517 | -44.67754 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 51c65a98-827b-35b2-ba7b-52f80b5b57e8 | -7.78463 | -44.68099 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c43aa5a5-43cb-39c3-9763-2a40ee3f592d | -7.78409 | -44.68446 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3406b1df-60ab-3cc3-970f-6b199f02f097 | -7.78187 | -44.67701 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| caaeafef-30d4-3cf3-8b9e-f14288d6cf61 | -7.78133 | -44.68047 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cae335b0-a80b-36d9-9bf8-e577737f05a6 | -7.77836 | -44.67301 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 18db9014-e7c1-3e56-a513-3ad968581230 | -7.77782 | -44.67647 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| a14cbb26-9805-3dc2-bf0b-083d46efe653 | -7.77728 | -44.67993 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 7ece34b2-ce7e-3434-8856-e885c9e31727 | -7.77673 | -44.6834 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22df6196-f749-3834-b52c-8bab12b6164e | -7.77506 | -44.67249 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a5a00d2c-4522-3a3c-8864-cdfd84f99333 | -7.77452 | -44.67595 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 3c043679-f8c1-3966-aea6-0c3f5a7c4127 | -7.77343 | -44.68288 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6922048-5b43-3fe6-85d7-4e6d24b5e488 | -7.77289 | -44.68634 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5f74c97-bcef-3120-8bce-5d53831b2589 | -7.77122 | -44.67543 | 2024-09-28 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| de35d10e-fe18-39a1-b225-5abe77bc9a54 | -7.75058 | -45.19981 | 2024-09-28 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e9412b2-3238-35f6-82a8-a8c1dddec01a | -7.42853 | -45.1696 | 2024-09-28 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72372ca8-0616-3180-bda2-f3712daf9ac0 | -7.42523 | -45.16908 | 2024-09-28 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93f110ce-d0cc-381e-af1d-11a518145969 | -7.35019 | -44.78199 | 2024-09-28 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beb25473-536c-36e3-a545-6dc218909672 | -7.34635 | -44.78492 | 2024-09-28 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 059e01ee-9a71-37c2-9dbd-698a2e4f1c34 | -7.34197 | -44.79131 | 2024-09-28 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e781f64-4f1f-311c-868b-bb7bb3bd6ec5 | -7.34143 | -44.79477 | 2024-09-28 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c51fd3a-faf6-36e5-977b-2aa581df629a | -7.3257 | -44.73927 | 2024-09-28 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f176c06-d7b6-33a2-a101-346cd205e0dc | -7.28059 | -44.96213 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae58897c-eb8b-384d-ab8f-99c178f5174e | -7.27783 | -44.95816 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9af425a-9617-3959-aadc-368583892601 | -7.27729 | -44.96161 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32bb88f7-0d8b-3a14-ba49-e60bd51b5105 | -7.27724 | -44.94037 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1df58d40-0421-3644-bcfe-a807c164ed17 | -7.27675 | -44.96506 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb277835-3c82-3686-9f56-e9fead72d3bc | -7.27566 | -44.97197 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ae22ba7-d6ce-314b-a083-b67501e6805c | -7.27449 | -44.93641 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d456ce7d-b5a4-38fb-992f-78049281224b | -7.27399 | -44.96109 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc0b1674-6203-3e8b-82cd-a57adb7b17f4 | -7.27345 | -44.96454 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be84087f-e7ec-33f6-9cd9-da74cb6bf8ca | -7.27119 | -44.93589 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7732a303-72c7-3412-86e8-a5e07f1042d8 | -7.26576 | -44.97041 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4589e6f3-ca37-32ad-922b-0a03614c4512 | -7.24208 | -44.949 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee91f2ab-91e9-3f44-97a3-6b72118aacbd | -7.23878 | -44.94848 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afa444bf-7e53-37f1-bc6d-2d0a9f96960a | -7.2344 | -44.95486 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a007e75c-8fef-3178-a4ee-f51350f95843 | -7.23386 | -44.95832 | 2024-09-28 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 459aeaca-00ae-3458-8132-cba66cb1807a | -7.21434 | -45.10386 | 2024-09-28 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd0bed70-4a66-3df1-b0bf-6fee351062a9 | -7.21213 | -45.09642 | 2024-09-28 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efe00cc7-04d2-3d1b-b2da-8dfb8f5c03b5 | -7.21158 | -45.09988 | 2024-09-28 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ebbb91b-1237-3619-90cc-00afe2bde438 | -8.81787 | -44.94485 | 2024-09-28 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2f56709-2bb4-3a27-a275-cf397b4651e6 | -8.71411 | -44.78262 | 2024-09-28 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7db3fb3f-22d6-32f3-bfd1-16c254ed1a00 | -8.71357 | -44.78609 | 2024-09-28 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2d012b7-e845-3e1e-b20b-bc8d6ea4a0cf | -8.40667 | -44.6377 | 2024-09-28 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README41.md)
