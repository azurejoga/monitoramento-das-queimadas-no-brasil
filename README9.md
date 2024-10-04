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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05679d54-334c-3540-bd24-6eb002ed5159 | -18.856701 | -42.915798 | 2024-10-04 00:40:53 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd021394-c011-36bc-959b-07986c2ca0e9 | -18.8416 | -42.895401 | 2024-10-04 00:40:53 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f7bcec5-5182-3d68-a093-a117a197acaf | -18.843399 | -42.903099 | 2024-10-04 00:40:53 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ca79f77-9e9d-32a6-9636-bec4f8a4aec9 | -18.8452 | -42.910702 | 2024-10-04 00:40:53 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 02e54d20-83b0-37eb-b39c-b566c8ae036d | -18.847 | -42.918301 | 2024-10-04 00:40:53 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 058bec12-00e9-32bc-ad0f-3fc5b2e7b052 | -18.833599 | -42.905602 | 2024-10-04 00:40:53 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 728dfcc7-616e-310e-9170-4b7567a1ed45 | -18.8256 | -42.9156 | 2024-10-04 00:40:54 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 139081e9-e1da-314a-bb38-773112ae6ef6 | -18.8274 | -42.923199 | 2024-10-04 00:40:54 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a8a004c-4a8f-3457-80d3-6278b5a41294 | -18.8202 | -42.981602 | 2024-10-04 00:40:54 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 21f311ed-4ef0-3135-869e-1f67dd202c0f | -18.878799 | -43.459599 | 2024-10-04 00:40:55 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c81023b-960c-3936-b31b-5accd64a5f27 | -18.861799 | -43.565601 | 2024-10-04 00:40:55 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b353f50c-22d2-3354-a60d-e08f83e50b0c | -18.863501 | -43.573002 | 2024-10-04 00:40:55 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 984f17ce-cf73-310e-ae70-4ac6c8348b0c | -19.992701 | -48.6852 | 2024-10-04 00:40:55 | METOP-C | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba3c2ce-ac6f-3941-907f-1bb7d0aedf7a | -20.006399 | -48.702599 | 2024-10-04 00:40:55 | METOP-C | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 091d1c7c-9e4f-37a9-815d-d1b12481966d | -19.982901 | -48.687302 | 2024-10-04 00:40:55 | METOP-C | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dbc61f0e-b682-36bf-9daf-166d07c654a6 | -19.986799 | -48.706902 | 2024-10-04 00:40:55 | METOP-C | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8668b331-6ab8-3027-b25c-4784a3b21c96 | -19.996599 | -48.7048 | 2024-10-04 00:40:55 | METOP-C | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e3c47c96-d276-33d2-9b92-62b7a168a284 | -19.9849 | -48.697102 | 2024-10-04 00:40:55 | METOP-C | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8d1976e1-4b5a-37c7-b4f5-b5d6b3995194 | -20.004499 | -48.692902 | 2024-10-04 00:40:55 | METOP-C | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a96a2f77-bc34-3858-a55e-5c733cced0bd | -19.994699 | -48.695 | 2024-10-04 00:40:55 | METOP-C | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ab18af50-bf09-389d-bda1-ae77cd76049f | -18.851999 | -43.5681 | 2024-10-04 00:40:56 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dcc336a7-1639-308a-a3b6-380c6d282930 | -18.853701 | -43.575401 | 2024-10-04 00:40:56 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63fa6e2c-d36e-3c98-a012-cffd22fdae52 | -18.8554 | -43.582802 | 2024-10-04 00:40:56 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 73654d3b-80a4-38d8-837b-d68acd9746fd | -18.857 | -43.590199 | 2024-10-04 00:40:56 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4df5ebe0-01a2-3a76-82f5-dcff06f2aadd | -18.8587 | -43.597599 | 2024-10-04 00:40:56 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5838fae6-f5c9-3057-a44e-c7eff1fcd7ab | -18.843901 | -43.5779 | 2024-10-04 00:40:56 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c782bd0e-728b-3300-a649-8ca8a51812cc | -18.8456 | -43.5853 | 2024-10-04 00:40:56 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 219cce81-f8d4-3f18-882a-02087fad4006 | -18.8473 | -43.592602 | 2024-10-04 00:40:56 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2403c7e6-8aab-329e-9e46-e7ad576ad91f | -18.849001 | -43.599998 | 2024-10-04 00:40:56 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97ee2e1a-ea92-3301-a341-cbc13f8c5019 | -18.2941 | -42.1493 | 2024-10-04 00:40:59 | METOP-C | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71736d25-d2c3-3338-8898-83e364dba04f | -18.5786 | -43.953602 | 2024-10-04 00:41:01 | METOP-C | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb53c75-e326-319e-ac48-e058942dac75 | -18.580299 | -43.960899 | 2024-10-04 00:41:01 | METOP-C | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 265e3065-e9e3-319f-92ec-75cdf77e956e | -17.849501 | -41.417801 | 2024-10-04 00:41:04 | METOP-C | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03bad8be-da19-397f-80a5-5bb16c9b3f29 | -17.8517 | -41.426701 | 2024-10-04 00:41:04 | METOP-C | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fafd0301-d8ca-3a87-b1ab-c6f56ab3f077 | -18.078899 | -42.5956 | 2024-10-04 00:41:04 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7504eb4-d3d0-3c02-8f73-3509e77dd1ec | -18.0807 | -42.6035 | 2024-10-04 00:41:04 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09ae6697-6af2-301c-acc6-bc9292bcb9ed | -19.016701 | -46.902 | 2024-10-04 00:41:05 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d153a1ef-f421-3047-949d-3194bd8cdf72 | -18.067301 | -42.590199 | 2024-10-04 00:41:05 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a62e247d-9350-3bb0-a920-e37f74ae4b2c | -18.069099 | -42.598099 | 2024-10-04 00:41:05 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac632ee3-3c55-3d13-b9b9-105ad1cfdbb3 | -18.039801 | -42.605598 | 2024-10-04 00:41:05 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9690c4f2-c384-333a-859e-24ba8174da87 | -18.0417 | -42.6134 | 2024-10-04 00:41:05 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 984a94b8-5580-3f36-96a9-96881bbb6de1 | -18.0436 | -42.6213 | 2024-10-04 00:41:05 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31329d5d-96d2-3a53-8004-0b14ceb7b623 | -18.395 | -44.465199 | 2024-10-04 00:41:06 | METOP-C | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 26dc8dc1-a8e3-3154-bad0-7f716ab6080c | -17.908001 | -42.179298 | 2024-10-04 00:41:06 | METOP-C | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7e1b6b8b-8951-3784-a1fe-68918d89089f | -17.91 | -42.187401 | 2024-10-04 00:41:06 | METOP-C | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34649741-6232-39ca-a823-674751995e5b | -18.7976 | -46.641102 | 2024-10-04 00:41:07 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 277e989d-75ff-363a-94f9-58d70b2f9402 | -18.7862 | -46.635601 | 2024-10-04 00:41:08 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 262b00f7-ac92-36d5-96e7-23df9fe78f18 | -18.7878 | -46.643299 | 2024-10-04 00:41:08 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dd7b54bc-4cd8-30c7-9f07-a810399d9080 | -17.9123 | -43.432899 | 2024-10-04 00:41:10 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b1859543-a099-3537-beae-da921ec9c845 | -17.914 | -43.4403 | 2024-10-04 00:41:10 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fe25ec1e-b1fe-3527-90db-e176cc1421dd | -17.9158 | -43.4478 | 2024-10-04 00:41:10 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f032a483-d9b7-31a8-9097-8f2d9eb6975d | -17.618799 | -42.007702 | 2024-10-04 00:41:10 | METOP-C | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39af224d-b58c-322f-a408-0100da066567 | -17.6208 | -42.016102 | 2024-10-04 00:41:10 | METOP-C | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a23b11ec-02fa-361a-8780-7b13fcd46feb | -17.7381 | -43.797298 | 2024-10-04 00:41:14 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 72b7657f-4411-3c7e-bca5-a43297f083dd | -17.739799 | -43.804699 | 2024-10-04 00:41:14 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| da9b40b7-777b-3721-81e1-f1721850e6c6 | -17.7283 | -43.799702 | 2024-10-04 00:41:15 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d574cf25-0bd3-3a4c-bb8f-75379c8a58ed | -17.3818 | -42.621498 | 2024-10-04 00:41:16 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f57251eb-0e24-35fb-a420-97af1b1540df | -17.3111 | -42.3666 | 2024-10-04 00:41:16 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c0264fa9-07d6-3a40-9abd-94c292e5b0fd | -17.370199 | -42.6161 | 2024-10-04 00:41:16 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a8bfcb07-53c8-3569-a789-b98a8f34a518 | -17.372101 | -42.624001 | 2024-10-04 00:41:16 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3fe1cf9c-6dd0-3d3b-a32c-7dc6bb7f82f0 | -17.374001 | -42.632 | 2024-10-04 00:41:16 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 54b6d96b-72f3-39a8-8388-1efda1abfdd7 | -17.360399 | -42.618599 | 2024-10-04 00:41:16 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f7e72efe-046c-346f-bb7f-daa8ccb1d713 | -17.362301 | -42.626499 | 2024-10-04 00:41:16 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a0700b81-953f-3fa3-8fee-e3d0fb64ec86 | -17.347 | -42.605099 | 2024-10-04 00:41:16 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 162b86f3-db8b-3d61-9fbf-b5c5c9a7b6e1 | -17.3489 | -42.612999 | 2024-10-04 00:41:16 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| aadd3a6a-c30c-3893-82bd-48c3a4a35fad | -17.3372 | -42.607601 | 2024-10-04 00:41:16 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a348ddf6-7bd7-3c02-8a43-9d637f125466 | -17.4086 | -44.937801 | 2024-10-04 00:41:24 | METOP-C | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 86dc3496-a358-3b05-8dce-b891c4bbba9c | -17.533899 | -46.730301 | 2024-10-04 00:41:28 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 94d0939b-3f9e-3c65-a820-e30e8fb153ef | -17.5242 | -46.732498 | 2024-10-04 00:41:28 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 62d2d906-8141-3578-b727-4c9480b79d43 | -17.525801 | -46.740101 | 2024-10-04 00:41:28 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f3e535ff-b505-3ead-8c8d-29a4c0aa783e | -17.527399 | -46.747601 | 2024-10-04 00:41:28 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cd48ac58-2b23-3f4c-b308-ebd411ba0b2c | -17.101601 | -44.580898 | 2024-10-04 00:41:28 | METOP-C | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f0c815cc-441c-3d07-a838-0de86eda46aa | -17.103201 | -44.5881 | 2024-10-04 00:41:28 | METOP-C | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6763d82e-efb0-33ef-9dbb-06d069bb595e | -17.6073 | -46.977402 | 2024-10-04 00:41:28 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 710f1cb5-3beb-3018-a17c-40a16fac82b5 | -16.469999 | -43.805099 | 2024-10-04 00:41:35 | METOP-C | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4fab6a5c-f18a-3629-9f8c-b985feaef6b2 | -16.471701 | -43.8125 | 2024-10-04 00:41:35 | METOP-C | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c0bf3dc9-a5f9-3b55-8253-fe25a331040a | -16.4734 | -43.819901 | 2024-10-04 00:41:35 | METOP-C | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0540cb53-884a-33a7-856f-ceb2baf3edb1 | -16.928699 | -47.115398 | 2024-10-04 00:41:39 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 116a8eeb-7f81-3249-ae97-b9738962b377 | -16.930401 | -47.1231 | 2024-10-04 00:41:39 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a2f9dd3f-38bf-3a16-8cd7-d2ee169f0c77 | -16.931999 | -47.130699 | 2024-10-04 00:41:39 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a0a94f39-6e58-3ded-999e-eeed7945555d | -16.933599 | -47.138401 | 2024-10-04 00:41:39 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c5a68f9-50fa-3c4a-ae3e-31fdfbf032f0 | -16.920601 | -47.125301 | 2024-10-04 00:41:40 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd0052d-59f9-3c82-89d6-1b4accb2ec33 | -16.9223 | -47.1329 | 2024-10-04 00:41:40 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 82fd9776-0e28-3565-bf3f-fedd695e4ac5 | -16.923901 | -47.140598 | 2024-10-04 00:41:40 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d782f51-5a58-3df8-b9c3-12901e0aa2bc | -16.093399 | -44.276501 | 2024-10-04 00:41:43 | METOP-C | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f7ac4d2c-0719-387b-9033-4f73455009f4 | -16.0951 | -44.283699 | 2024-10-04 00:41:43 | METOP-C | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac8431af-dfcc-3e23-8f7d-746f2936d9dc | -15.7658 | -43.5746 | 2024-10-04 00:41:45 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e30cd239-f121-3b34-9de7-52149dcdca8a | -15.7676 | -43.582199 | 2024-10-04 00:41:45 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 000f40b7-d125-33b7-9c2d-f7d95cf67574 | -16.6947 | -48.6315 | 2024-10-04 00:41:48 | METOP-C | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 215c32d0-a714-3595-9939-d85339299f34 | -16.696501 | -48.640301 | 2024-10-04 00:41:48 | METOP-C | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 292c7820-c9c5-3e86-a063-bc5d3862e0fe | -15.622 | -47.197102 | 2024-10-04 00:42:01 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2f5b0a73-3ca3-39b5-998f-d66071eebe81 | -15.6123 | -47.199299 | 2024-10-04 00:42:01 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3902d047-5b2e-388d-9ff1-f00f396260e4 | -15.6139 | -47.206799 | 2024-10-04 00:42:01 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5770f370-e86b-3c9d-97a3-b9c53276884a | -16.1052 | -50.446602 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 95b81c37-4e47-3315-8f70-bac56b4ba648 | -16.1073 | -50.457401 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fa9a27b1-1132-3cb5-a800-e7509ae72212 | -16.093201 | -50.438 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 042b7f0c-bbde-3318-b239-7d3310a3732a | -16.0954 | -50.4487 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea3ddaf0-1c2a-3026-8e8f-e12014fac091 | -16.0975 | -50.459499 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 198d6f97-c68a-3243-ad28-1ad6c1b2c000 | -16.083401 | -50.439999 | 2024-10-04 00:42:04 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 42d65904-8561-36ba-b145-98cac290cd8f | -14.3252 | -42.338902 | 2024-10-04 00:42:04 | METOP-C | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README10.md)
