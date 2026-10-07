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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 648f2d9b-7728-39c6-acfc-533bcb9fcaac | -3.53907 | -50.0957 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16e1231a-16ec-3cf8-b3e4-6eb07762634a | -3.2393 | -53.87318 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8c6d858-0d13-3056-8d0c-330ba6e8f3a1 | -3.83335 | -52.14269 | 2026-10-07 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d31b752-094a-3f94-8249-d41c8018ff87 | -5.97256 | -40.91683 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 23731ea6-912b-3b86-a8ab-0055068b45ee | -3.28092 | -54.06627 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7a71e255-d7f5-3854-8c5e-b2b9af993780 | -4.35942 | -47.77909 | 2026-10-07 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 59003c65-a5a8-3f77-bbc7-ba4b39750857 | -8.64425 | -44.88368 | 2026-10-07 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e0f1c1e-82bd-32b2-90d9-51100fa93262 | -3.26608 | -50.4128 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24b5006e-f273-3496-a40e-95f5e97ca40a | -7.86886 | -44.21316 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a1504e89-cf66-3d28-b715-5a88371162a3 | -2.99501 | -54.12188 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ccf0352-341f-344c-b7f5-8e1904d6d286 | -3.01873 | -53.91048 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 564593bb-da52-3a31-bef6-650b2765b547 | -4.15824 | -55.14379 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 46846ed5-7992-3846-92dd-98e9ac3bdd1a | -4.31983 | -43.81875 | 2026-10-07 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 039d0c34-e914-34d5-883e-1e46783fc8d0 | -6.00012 | -53.50766 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a7f190b-6704-3e46-866d-6a4316c460df | -5.72258 | -45.15627 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 633bc84e-29c6-36f0-923c-57e393dccfc1 | -5.27498 | -43.36726 | 2026-10-07 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53567c5e-82ae-3606-ad24-833d54645a26 | -7.24837 | -45.26451 | 2026-10-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d93e09d7-7459-391d-8e4f-fe7670a36110 | -2.99129 | -51.05128 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40c12b0e-ce4d-3da4-a9a1-88a971c45fc7 | -7.83849 | -45.47646 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 79cbfff7-55ae-336d-9faa-03eff6619560 | -3.50411 | -54.64901 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c8ab8a3-6f6d-30c2-ade5-3e920869f537 | -3.12378 | -53.7013 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f60b629e-0f9a-304f-94b0-eb76f8fded03 | -3.01208 | -54.13499 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3f0904b-b3f3-3406-9c96-0656d69f35df | -1.5076 | -54.83236 | 2026-10-07 04:19:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f12d206-1855-3a8f-9209-06f24b05f58b | -3.47046 | -49.93957 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2a7a0e1-4564-3ff7-83e7-dc864d6ee1f1 | -6.08036 | -47.05743 | 2026-10-07 04:19:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51821350-0ba1-3554-a687-878ef94309de | -3.0833 | -54.30576 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a608ddb-01c3-39e0-a403-84579a1ae163 | -3.06336 | -54.17474 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8330b132-1303-3fc6-abfb-4db1d28e5b98 | -3.74256 | -51.22746 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a72d4bb-0cfa-372c-933b-72b31b71cfa7 | -5.49894 | -42.83381 | 2026-10-07 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5e48064b-ddae-300c-874e-4d0ca54602e4 | -3.27406 | -50.42546 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b0254f3-f2f8-3dd1-b559-fe4155e82bfd | -7.83406 | -44.1754 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e7916e6-4467-3468-8ec1-329bcf6c7815 | -2.95225 | -54.14544 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 07f5fcfe-c6c5-39b0-84a4-ab0c0c9e623d | -2.76856 | -54.0826 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 57149e28-735f-3d6e-a32c-30108fef3d89 | -3.61577 | -55.28267 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3c5f9564-7662-3dda-a145-467e49e77a9e | -3.02548 | -53.9149 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| be57c150-5189-311a-ba8b-a76b0e2a8bb2 | -2.96056 | -51.04613 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 910f7242-b924-30bc-828e-675c85350b88 | -6.21086 | -52.83933 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 320df68e-813d-3611-a9e4-b11c88677ed4 | -3.17987 | -50.5682 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 91fe0dde-7ba1-3939-8b20-88d51bbe81fa | -2.77902 | -54.11402 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 99a1d136-d678-3f6b-9b3a-a021a5f26e46 | -3.46666 | -50.08641 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dffbed34-0110-37f2-b79c-995312b36e9b | -3.51687 | -54.65759 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6916ad33-9823-3b03-ba9c-2198ed4dda97 | -3.04095 | -53.92904 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f463346-5a4c-36e1-89a3-92f452e63a94 | -3.28211 | -54.06823 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0d843ebf-49af-3aeb-b188-f48b30918fd0 | -5.28513 | -42.74665 | 2026-10-07 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 43bff620-38c7-3bc2-a033-17933adfdf4f | -2.76565 | -54.11684 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 37126b53-57d3-308b-af9e-297e7130594c | -6.01964 | -42.26368 | 2026-10-07 04:19:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c0e6ab2e-4049-3076-a2dd-84c8dbaa9534 | -8.00946 | -45.46161 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a711c05e-5cc5-3b3b-8e53-331f112ba9d9 | -5.74166 | -43.27548 | 2026-10-07 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c2df6e99-e142-35a1-9d1d-53343d95e5d7 | -6.14926 | -51.75644 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d162df03-9670-307a-bf7e-054f8b99c03b | -3.06128 | -54.22578 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b2ab5b1-ecee-376c-a5cc-e92dd82efdd5 | -3.47921 | -55.43347 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22a2d0a4-9138-3f73-922c-df611b522179 | -5.67881 | -53.49916 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bcea497-878d-3be9-a11c-cdbe3440d8ea | -7.99252 | -45.50072 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2871172-5e09-3354-b542-731ea72b8afb | -5.23386 | -50.91243 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2eb279f4-18ad-3575-ae29-d2b9a343acb5 | -2.93778 | -54.17191 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 51f721aa-7246-372d-a057-fc8c99b7e2f3 | -3.07311 | -54.25197 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c10e844c-0dbc-3ab1-ba75-e8ef001e7fd0 | -3.50431 | -51.68184 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d83c21d6-33ae-3aa9-a843-7c29db7cb4e9 | -6.93941 | -43.06889 | 2026-10-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58584f94-2df8-3d24-97c4-27e5bda265ce | -2.97022 | -54.13228 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4164fd7-671b-3433-9a98-dca916a6829e | -2.76876 | -54.11883 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| db4708c0-dc59-34f5-9ee1-f70f58ba8f32 | -6.43909 | -55.0242 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db691aa0-b666-3435-89a7-e1972050e29c | -3.99334 | -56.25793 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 720d529d-4165-3fbd-8f54-607761b9a544 | -4.1572 | -55.14953 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 93524ae1-c8d4-3a0f-95d4-61b60689b186 | -4.15547 | -55.16493 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3998055e-240a-3533-b803-bb25e16a8aa2 | -3.53612 | -54.65481 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 16b8d0a7-2c87-3d49-890b-a2071f87ae54 | -6.88449 | -42.22401 | 2026-10-07 04:19:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84be6c3e-9080-3a1d-9a80-efec562a7c3d | -3.00753 | -54.12398 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 88646786-4291-3c20-8751-211562489693 | -3.35701 | -50.46932 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bd57271-1b22-3b83-ac29-6e08643181e6 | -3.05778 | -54.2283 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b271187f-4b26-332d-988e-4a326f3f50d0 | -2.75646 | -54.09447 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00f93af7-68f7-32f6-a690-01f4861f8ac9 | -3.22907 | -54.30532 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79ecb27f-fdda-38fb-91b1-2d41da3650f8 | -8.36469 | -44.19267 | 2026-10-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a88165ec-9154-3ad6-8054-112d15f3ef20 | -6.08019 | -43.87976 | 2026-10-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3832017a-a063-34ae-a086-5887e103cb36 | -2.76814 | -54.10179 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| cb0852b9-8729-34e7-b08c-2c3d2f76fbc3 | -3.70987 | -51.14119 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 252dd04e-dfc9-3184-ac73-1887fc2d9469 | -8.20929 | -46.35644 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2736178-6d89-3d2c-bf09-277db4e8831c | -3.94151 | -51.01832 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18c1024b-4c4a-3438-9fe4-bfa795bbaff0 | -3.27739 | -50.42113 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e3b5328-5555-309b-9863-480c1b43c748 | -2.99276 | -51.01112 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed728d87-bbea-3ed1-a4ee-0326deeb67a0 | -2.94164 | -54.16909 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d73bde86-0acb-3350-bc4d-1c647ce647f6 | -4.31701 | -43.00327 | 2026-10-07 04:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4072ed7e-82cb-3383-b48b-d65d035fac3f | -3.49754 | -54.65482 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb4f0f4d-aaae-35c7-8894-a0b4f3f35e50 | -2.77134 | -54.10384 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| cdc9b95a-c1d7-3cfd-a7b3-13619a63cbfb | -3.06676 | -54.25119 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f52713b2-d99d-3b05-8194-ccd3f0adeca4 | -3.49945 | -54.63765 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b187916-e90d-3e49-8d77-bb21ac6c7e6e | -6.65149 | -47.91277 | 2026-10-07 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9b4e7ad-73ca-37f1-856d-4833780d3e1d | -3.48843 | -54.625 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a81a6c93-6cf4-30d0-be4a-7fdcbbf5a1a5 | -2.97569 | -54.13812 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4a120c1-91ff-3eb7-be3f-51a6c492a49b | -8.66166 | -44.86092 | 2026-10-07 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6d9932c-ac2a-386c-b067-ca6a2dd20fb8 | -3.09398 | -54.28144 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 375df1ea-c31a-3a74-afae-93bf23cc8d9a | -6.00591 | -53.50835 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6969f76b-f861-333f-80f9-245db9dd269f | -3.74768 | -51.22834 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4250b60a-90a4-3897-b656-b2ef70d6f856 | -3.80878 | -51.0423 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f10a61e3-dbcd-39e6-bd49-8831698e45e6 | -6.84475 | -41.77016 | 2026-10-07 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1f3b8e70-4c67-3248-a97e-2b6f17086908 | -4.77289 | -50.8158 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6505984-182a-3820-9544-921a3f6a2de6 | -3.27469 | -54.03671 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| f8f8706a-24ea-3dab-a743-9a0a7fc3d595 | -4.15087 | -55.15263 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4aedf69f-07da-3f7f-8906-3f12cc4cfde8 | -3.48094 | -50.08871 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b81ecb7-ab8f-313d-8967-6b75992f0e10 | -4.51851 | -42.89019 | 2026-10-07 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bf12e4c-1f1b-3a55-899a-813265ef1314 | -3.53059 | -54.65473 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README48.md)
