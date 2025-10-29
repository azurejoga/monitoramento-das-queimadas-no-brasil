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
| 3b0452e6-d1cf-3af7-87f5-66c21e4fc732 | -4.65573 | -42.51322 | 2025-10-29 03:53:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4e3c7d57-98dc-33a2-9c22-365cebc2fe81 | -6.10878 | -42.46911 | 2025-10-29 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 3da7d547-07d7-375b-bb2b-7dc48149adaf | -6.23431 | -42.53617 | 2025-10-29 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 009abee5-ea39-386c-bc70-154a910966bd | -7.92955 | -46.01288 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 615f3361-f3db-34a1-bb6d-5f257e4dd9be | -6.45969 | -43.55936 | 2025-10-29 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa119f39-b287-33a1-80e9-a8e467b47a70 | -6.11089 | -41.72179 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bc6f01d3-76c6-30d9-a4f9-05b513185a56 | -3.78618 | -45.59122 | 2025-10-29 03:53:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5eba2c39-0eef-3e61-bac7-d774901fd022 | -7.79705 | -46.46037 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d27a9728-5e52-3174-9989-e127df65b09e | -7.03793 | -39.47862 | 2025-10-29 03:53:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 31ea99ec-67d3-3001-8e67-5c45e601f09a | -5.60955 | -47.1116 | 2025-10-29 03:53:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd8efd99-4519-309a-8d59-590aa7a81a06 | -7.78924 | -46.4761 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d8f9b464-64fe-3094-aab7-919645af8f9b | -5.19988 | -46.14974 | 2025-10-29 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d35bd90f-cfeb-3022-b22a-9d9bc574a4de | -6.22109 | -41.8289 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 56e8a566-a88e-3a47-bb5a-ada2d5dd872f | -7.33676 | -42.46958 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 073e8590-6f8a-3939-9244-068da6efad41 | -7.9282 | -45.50204 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 050af457-cf8f-351b-9f6d-914dd66da93b | -5.33341 | -41.21645 | 2025-10-29 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 32a05648-bf48-38ce-a3cb-cf34213e022f | -7.7824 | -46.45803 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5f452246-e869-3a22-a1f8-2ed0e5790f6b | -7.80384 | -46.47881 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 888d6b75-1cc1-382e-b0f4-8064065da84d | -6.18011 | -41.68752 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 34a33aa2-21c0-312f-9880-ba01a35a20a1 | -4.85018 | -40.06894 | 2025-10-29 03:53:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1bc48659-7080-3c07-88c5-12bf89c6ec8a | -6.15375 | -41.57392 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 19f2f54c-fe79-3e5b-9077-eec0240dcc14 | -7.28152 | -44.0987 | 2025-10-29 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f38c47d-537f-316d-8e89-38e6b3888903 | -6.50031 | -42.23761 | 2025-10-29 03:53:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d210adaf-69f9-3e8f-90ab-9c61e7f6107a | -6.36717 | -44.18829 | 2025-10-29 03:53:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1265e3d0-5f58-3126-a208-0e25ee8bec30 | -6.17939 | -41.69187 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 429bdd9b-99ad-3c5e-bddf-eb3318b934aa | -7.44592 | -46.60722 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aada2247-578a-3daa-af8c-e02aa379b0a1 | -7.60265 | -43.57433 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 652fdfc9-805b-3403-adcc-c9ac76d9441d | -6.47543 | -43.39068 | 2025-10-29 03:53:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67671453-04ca-359d-ab47-06902c986bcc | -7.37061 | -42.4541 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 91b94ccd-c65e-383a-b7f3-ddcd1858d887 | -6.88799 | -45.04292 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 383eb8e1-a1d1-383f-b8f1-3852ff422205 | -7.61256 | -43.5953 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 166cc05e-1065-3665-a9fa-b657e11b061e | -5.65333 | -46.45035 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cf1c782-431c-3e50-81f8-2934541ed5b0 | -6.24649 | -42.5586 | 2025-10-29 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 05869b0f-81c7-3505-923c-6d18f65524fe | -3.84114 | -42.55121 | 2025-10-29 03:53:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ffe5645-dda8-39c0-8685-b38fab017566 | -4.01068 | -43.28404 | 2025-10-29 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9791b8aa-d5e6-37e6-a76d-9aa43af7a6b3 | -6.54164 | -42.87531 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9caacbb4-7514-3950-83a0-570e7741eb16 | -7.35981 | -47.63554 | 2025-10-29 03:53:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58561538-7e28-3d17-a015-9e9c778e7e1c | -5.96413 | -46.32224 | 2025-10-29 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32eead5c-b5ba-375e-8344-8a3d65ecf4ed | -5.06255 | -42.75785 | 2025-10-29 03:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c2b982e-f0e1-3903-a25c-5e823501795e | -5.05481 | -40.46387 | 2025-10-29 03:53:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d09cae19-d1ad-3096-af31-7220a07d8984 | -4.35664 | -43.63601 | 2025-10-29 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb39519f-5545-36f9-95fd-b8ecd53c9827 | -8.76183 | -40.61126 | 2025-10-29 03:53:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ed486a26-db82-301c-8ae1-c60980dd0ba8 | -4.66737 | -46.40355 | 2025-10-29 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 439afa78-16b7-369e-8418-6eb12d5224d2 | -8.53165 | -40.64326 | 2025-10-29 03:53:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 14097e30-b162-3509-a8e2-cd10ecb5a672 | -2.41949 | -49.30347 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 71eb453c-b9a5-3967-a846-100fdc7d0b2b | -7.41842 | -41.8757 | 2025-10-29 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 65d60cdf-d70c-3a2d-a62e-ca011ab73d3f | -7.44089 | -45.1174 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcd48b2b-b9c6-33e9-95e5-eeb56a90c67e | -6.54276 | -43.56144 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be107c81-9b25-3149-a0f8-64906ae67898 | -7.07677 | -44.93975 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b86a9112-a648-3368-a202-029775a35436 | -3.99644 | -43.65785 | 2025-10-29 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e8eeb7e-9d8e-3e84-b9ca-52f014c7032e | -6.13869 | -41.7132 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 21dcf5e6-f57c-34ab-874d-e77d85f26f83 | -7.41117 | -47.17285 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ac98d87-a598-3f84-9010-ceb4553e9c2d | -7.77043 | -42.17769 | 2025-10-29 03:53:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0c73f816-f1e8-344e-849c-b0061c405bb3 | -8.03096 | -47.39717 | 2025-10-29 03:53:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c357dd66-06c2-3c21-b07d-041f5977e4f2 | -7.31063 | -46.31585 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8158f31f-acc0-3d33-a87f-0f5a80a2253c | -7.65665 | -38.51048 | 2025-10-29 03:53:00 | NOAA-21 | SANTA INÊS | PARAÍBA | Brasil | 2513356 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d4631a5-e7bd-3142-b1ca-37e588d9d725 | -2.63666 | -47.9609 | 2025-10-29 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af287d79-7b4b-34c3-a290-77c2585639ee | -4.67795 | -43.24018 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2576ba96-eba0-39c1-9268-724975f8396b | -6.54122 | -46.76511 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1098627a-af46-3899-9024-93a23b92a0bc | -8.76523 | -40.61181 | 2025-10-29 03:53:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 97a346ac-ae05-3089-ad07-d19f447aee1e | -6.08856 | -42.14138 | 2025-10-29 03:53:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6a058212-28ef-3319-96b7-c6a7b3092306 | -5.63877 | -41.53252 | 2025-10-29 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cb136bd3-5413-3c23-9109-3d317f03aa64 | -7.96482 | -46.73643 | 2025-10-29 03:53:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 42449ed7-68d1-36f5-a849-8e9ee925e893 | -6.11316 | -41.731 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4a404bb6-ab21-3114-84dc-2f2bfe3dc372 | -7.69786 | -46.90179 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c3640d06-de72-334a-a372-dd6a4a61b7ad | -6.24156 | -42.57551 | 2025-10-29 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5151a6e2-b120-3c54-9464-327510958cc2 | -8.17863 | -45.71574 | 2025-10-29 03:53:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f9d48a3-c165-30b0-8682-da2bc2286fa0 | -5.0882 | -44.81005 | 2025-10-29 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4882bf6b-b416-3ba3-9615-e0e4a298e384 | -7.80094 | -46.46675 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c630eaa2-83f8-39b3-8514-317b38faebbd | -6.29539 | -44.69629 | 2025-10-29 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60052b63-8abc-3a47-b03f-6253fb00a4be | -7.34458 | -43.91355 | 2025-10-29 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59d69fe9-4c6f-32ad-8507-d9fb25451676 | -7.79314 | -46.45411 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b42e564-cd69-30f8-a281-c20d9bbb3dea | -5.61016 | -47.10809 | 2025-10-29 03:53:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae9d6e78-6fe1-3453-a9c2-80fd15d59ed8 | -3.86871 | -43.35684 | 2025-10-29 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f4d4c436-b2b4-30ee-a734-48674be6003d | -6.60382 | -44.63662 | 2025-10-29 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e9434cb4-f44e-300e-a8c2-294ed6f754fd | -3.78524 | -45.59673 | 2025-10-29 03:53:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 78380af8-1e8e-36a9-bc5d-44df113e2dcc | -8.54441 | -45.70116 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c26832a0-4e9e-3cda-a162-457e84ea465b | -7.85501 | -44.23302 | 2025-10-29 03:53:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd8fae08-022d-3d05-938d-dd5972b88299 | -8.00529 | -46.20269 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3783208b-49db-3e18-b309-c7d7d4934b01 | -6.48821 | -42.24069 | 2025-10-29 03:53:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 107218b1-3a5f-3499-8a5f-abcc9b0ba668 | -8.61709 | -44.80606 | 2025-10-29 03:53:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 06294c09-7583-349f-9c35-c575555d1a28 | -5.65966 | -47.8277 | 2025-10-29 03:53:00 | NOAA-21 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9de42e5-fe6d-3f58-b7cd-0bec3c9f4211 | -7.49737 | -47.04528 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5a349c4-7f8f-34f5-a303-b5a577a0e510 | -6.27954 | -42.87596 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1761d1eb-b94e-3b5a-99ee-0b5c6b13d1b2 | -7.14798 | -45.80722 | 2025-10-29 03:53:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f3b7e40-865c-3e25-aa14-8be184b683a6 | -8.3328 | -46.16049 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bdfa0b25-4aab-3c73-8a97-db9776b98579 | -2.43027 | -49.30658 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 44e0bc5f-b378-326f-88a4-34ea14662de5 | -7.2802 | -44.10661 | 2025-10-29 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ba1691a-a052-3c36-bf24-32d35722fd54 | -5.56343 | -42.16893 | 2025-10-29 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6fe1cda9-43b6-31c5-ad1d-535efa08c4ec | -7.07629 | -46.10353 | 2025-10-29 03:53:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d607b1c-3e44-3b45-a9ec-e4c7af120042 | -4.51499 | -45.99889 | 2025-10-29 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3a81121-eec4-3bd6-bf8a-73a449b6bfe9 | -8.21604 | -43.80829 | 2025-10-29 03:53:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8df497b1-0e23-3af6-ae03-1bafbd38b202 | -7.79606 | -46.46598 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e316172a-d0a4-321c-8728-ac6460b1dba8 | -4.72668 | -46.81441 | 2025-10-29 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04e562b6-a730-369f-a48f-3b6a2052278f | -5.90313 | -37.8222 | 2025-10-29 03:53:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c47a9a62-1165-341b-9bb3-4017b10b10dc | -3.46159 | -43.34951 | 2025-10-29 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2a9e979-7ec3-3de0-8425-2f38148b6624 | -3.74215 | -44.01268 | 2025-10-29 03:53:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0571b632-126e-34ae-b5f5-65a4828ddcdf | -4.74533 | -46.4563 | 2025-10-29 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4242770-b2ef-3317-8a45-f5e381ef9e0b | -8.54156 | -45.69031 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbf2884d-a4bf-3cb3-88c6-faf647565fe9 | -7.19388 | -46.74864 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README10.md)
