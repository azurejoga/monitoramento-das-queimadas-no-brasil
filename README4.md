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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b19f031-1711-30ef-8576-a0d3870a2f1b | -1.7355 | -54.937099 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87f7696d-5f78-37ee-9942-ca134cea5323 | -12.843 | -44.376801 | 2026-09-19 00:19:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a69fe08d-5f87-3ccc-bfcd-47df5197056a | -6.6325 | -47.769199 | 2026-09-19 00:19:00 | METOP-B | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8572e4a-b505-3235-bd35-2b7b112eef05 | -5.2499 | -49.402699 | 2026-09-19 00:19:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 472ecb4e-1b12-3c2e-9358-ae027fb6c220 | -7.3608 | -50.330502 | 2026-09-19 00:19:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6c84f32-8776-3838-b1ef-616a52b9af26 | -1.8402 | -54.853298 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37698f2d-25f2-3b8a-9406-709544383daa | -4.5316 | -54.9212 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc212117-9248-3281-bd30-280abab3266a | -14.6889 | -46.645699 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6058fc82-ccab-35d4-92fb-59fb784cc370 | -6.3047 | -47.558701 | 2026-09-19 00:19:00 | METOP-B | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9a8f8a3-3172-3a62-ac1a-c250af8dadae | -11.9849 | -52.445999 | 2026-09-19 00:19:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d710aea-c012-3bfb-a20d-6631ec91aa26 | -21.459499 | -48.674599 | 2026-09-19 00:19:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1e9a45c4-f1ec-3f5e-805d-b74d4badb2b9 | -14.7881 | -48.573502 | 2026-09-19 00:19:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9902fba4-da5b-360a-8c59-83afc8a742fa | -16.067301 | -52.2425 | 2026-09-19 00:19:00 | METOP-B | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7c9a3f63-ada3-37ac-a0e6-dde3b5a6b9c6 | -11.2772 | -54.1166 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 130f71ee-2dc8-3c30-afc4-cacdc9e3bace | -2.9581 | -52.138699 | 2026-09-19 00:19:00 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb0369f-b56a-3ef5-ba88-26eaf0f9a96f | -5.8654 | -52.051201 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ad39a62-8f03-3dba-b302-64e103ec51a3 | -7.6421 | -46.116199 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc296eab-c0e9-3c2f-836a-0a3a94235b04 | -4.0648 | -56.245098 | 2026-09-19 00:19:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5678aad4-634a-3c73-b347-591f197e93a2 | -3.4546 | -50.606602 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b76746ce-4b01-370c-a52c-bcada2430488 | -6.3245 | -55.267502 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63054172-3695-3b5d-b6ef-97897fd726dc | -10.7959 | -50.885601 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c7e7f41-06a0-30f6-8f27-c4438f7641ed | -4.7119 | -55.687302 | 2026-09-19 00:19:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d0425f4-16b2-3ad8-912e-c51aa4801345 | -13.8748 | -48.5966 | 2026-09-19 00:19:00 | METOP-B | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7aaf499e-49ce-3b31-9f91-a3812109eeb2 | -7.6518 | -46.113899 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abe3f1aa-a679-3dcf-9d96-02ec66eb0427 | -13.6079 | -46.925098 | 2026-09-19 00:19:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b582d5c2-7d7c-3ce4-a216-3caf987babe5 | -11.4154 | -51.446098 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c39f4a8-324c-3282-bbba-f94d8f81c038 | -10.607 | -46.0882 | 2026-09-19 00:19:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3eb808ab-7f4c-3cda-96e9-620aae38d177 | -10.3292 | -53.5723 | 2026-09-19 00:19:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecec43ef-a3a7-3ba4-92a0-5d764ec7d8fb | -11.4268 | -51.450901 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e86e2b9f-1f05-3453-9af2-fde0c0eb1f9d | -11.1008 | -49.4575 | 2026-09-19 00:19:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c68841f-d5eb-3daa-931d-4cd291a32695 | -4.3776 | -55.246399 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4a3291c-c27f-39f9-8d96-7495fbbe356b | -10.8073 | -50.890301 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ecf949a-e7b7-3abe-af4f-a6c34d5ea7a5 | -3.3309 | -59.789902 | 2026-09-19 00:19:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2821575-b675-3ba0-a2e6-d690fbc78c8b | -5.8586 | -51.930199 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ca20bf8-61cb-3ef6-862b-f48aa2984b2a | -9.936 | -53.9846 | 2026-09-19 00:19:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc17356a-4546-3e36-b18f-922cd4f7bcef | -1.2222 | -55.720798 | 2026-09-19 00:19:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5be7444c-dd9d-3a85-938a-e6cf4cab1fd4 | -6.9401 | -55.0308 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5c19b9f-8a68-3580-8b1d-89fde213e002 | -16.803699 | -46.975899 | 2026-09-19 00:19:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 01ac7c88-f0fc-3693-94a2-03a45261b0d9 | -14.6812 | -46.657001 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 32093c16-8f2d-398d-9d4a-889378c355f9 | -11.2506 | -54.0877 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac16308-7372-3e10-8330-df34b533e983 | -7.1937 | -47.875301 | 2026-09-19 00:19:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6440163f-2592-3767-bfe6-1bb87b05aeaa | -11.325 | -43.350201 | 2026-09-19 00:19:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 45833bab-f86a-3eed-ba7c-6d41cabf694c | -4.4224 | -55.494301 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4947d412-cc63-34e7-b20b-5588427b10c2 | -1.5939 | -55.5429 | 2026-09-19 00:19:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccd82e0a-ed71-36e6-b072-8dc3a09e2a27 | -2.8218 | -50.453499 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df793dcf-168f-3ebd-a9d0-24e091ca2861 | -21.031401 | -48.223099 | 2026-09-19 00:19:00 | METOP-B | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cb86da95-dcb1-3718-b428-6eb17a8c36da | -10.8664 | -56.200001 | 2026-09-19 00:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a15ee0f4-ce90-36f0-bd72-523e65a28b15 | -13.6022 | -48.310101 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 756c730a-2e3f-3c7f-909f-76b16302159f | -12.1269 | -46.998402 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d5fd901-949f-3198-a27d-10d5d5eea4a8 | -11.417 | -51.453098 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0742047c-8b7b-38b7-ad16-a505db6d9dd8 | -13.3814 | -48.026402 | 2026-09-19 00:19:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a8646ac2-d42d-3929-b719-cdd859ab91b1 | -5.7412 | -57.576199 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be07e8b8-f291-3c51-a5e4-e60cc43d3c0a | -13.6084 | -48.292301 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0f3c8601-68f3-39e5-8c8c-663f81dd0bba | -12.1345 | -46.987 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6237c50-38be-3c2c-b8e3-9b56e95da17c | -10.1797 | -48.5089 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 564b08a2-b836-3da9-b831-2b25a3198a98 | -3.555 | -50.2799 | 2026-09-19 00:19:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb895438-2658-33d5-98e8-d7aec830c3e7 | -6.0021 | -51.789799 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9809d719-dc88-3f3b-a935-5d45cbe957b1 | -4.4492 | -55.522202 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6d5500c-0ed0-300e-8b49-746a67e174c1 | -1.3052 | -55.815201 | 2026-09-19 00:19:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cab278e-7141-3c3e-9130-0eee0158554d | -16.3083 | -53.8596 | 2026-09-19 00:19:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 47a540ab-4914-3842-a571-7a61dae3d3ab | -2.2822 | -47.880901 | 2026-09-19 00:19:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cdc2b89-c784-394d-a00d-567cb0be68b3 | -14.6596 | -46.653099 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0993ab-e800-3146-8a24-9123315c6207 | -9.0318 | -48.7206 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5a5f9810-beb4-354f-9f29-8a75429e5d20 | -5.3299 | -48.990898 | 2026-09-19 00:19:00 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba01a6ba-bb21-3e5c-a972-e641f972b951 | 1.2625 | -50.9706 | 2026-09-19 00:19:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5835c51d-0e77-3d2a-9b42-70845547e672 | -11.0782 | -50.674599 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dfe469b0-5f2b-37d1-a818-b3939751540e | -11.7652 | -47.433498 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3eeb6c5-d172-39de-afa3-f9a8ded1f6e0 | -11.3022 | -46.7892 | 2026-09-19 00:19:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a88f3544-6b02-3a27-b9ac-51a9d30354d2 | -12.9991 | -46.973099 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8de3cc54-fa95-312d-82f8-c0bbffd11c0e | -9.7792 | -45.062 | 2026-09-19 00:19:00 | METOP-B | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 33fe94a9-caa5-3c8b-af51-c343794acbcf | -5.2913 | -43.414501 | 2026-09-19 00:19:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0aad39d3-b64b-3ac3-b14c-1d6032d4e58a | -15.6774 | -52.729 | 2026-09-19 00:19:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c7b939cc-08a6-3563-9f5d-895cc2315932 | -3.7303 | -54.650398 | 2026-09-19 00:19:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c00a7ee-0bb9-3563-be5e-1729372a847a | -9.2292 | -48.196201 | 2026-09-19 00:19:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 704bc5ca-b9c7-3ca5-9a55-3c52718fdaf6 | -10.9343 | -53.951302 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc9660c9-9c97-3e8c-b2df-e179a5ee3f00 | -18.4044 | -49.156898 | 2026-09-19 00:19:00 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec0e9dcc-ed88-3319-9e5e-5ff54820d132 | -15.3631 | -49.014599 | 2026-09-19 00:19:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2828469c-6ca6-34be-9389-727a28ff0b5e | -8.7707 | -48.662701 | 2026-09-19 00:19:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 05740405-ad4a-3abb-ab5d-a0efa01481f5 | -11.331 | -47.344501 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89a1daa4-bfa3-335e-bd55-ccfbcebdf0ae | -11.1071 | -49.440601 | 2026-09-19 00:19:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1995e0a9-20d5-33d9-88be-56779c7889aa | -6.9419 | -55.039001 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe871740-9008-3238-a68f-cca1b1d2d3c7 | -6.5715 | -44.160099 | 2026-09-19 00:19:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a0994eb-8419-3bae-8379-50d9ca47ec19 | -6.0134 | -51.794399 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f0a21e6-d4d6-3ce7-ac8b-658efc5c2f13 | -10.359 | -48.880901 | 2026-09-19 00:19:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f195868-a6f3-33f3-9883-8a03b69a9bd8 | -9.3518 | -50.108002 | 2026-09-19 00:19:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 811fee27-ba90-3fb4-883c-2af4e27a0031 | -12.1584 | -47.000198 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb26f70e-10ce-3142-9d19-796b22c9b168 | -12.5886 | -49.106998 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb489df1-4772-33a9-933b-2676a1b72c51 | -5.885 | -52.046799 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8d27b01-a42d-3b18-84c9-6aa2356fc730 | -12.1409 | -47.014099 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 473e025d-720f-3ec6-b5b3-1fe9f7a748cc | -3.1455 | -53.9258 | 2026-09-19 00:19:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df87b7da-1154-38e4-857f-c050c38950af | -11.0675 | -49.7631 | 2026-09-19 00:19:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9668713c-cfba-3843-8c19-cbfc6a21d9fa | -12.2818 | -49.164101 | 2026-09-19 00:19:00 | METOP-B | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6f99c55-82f6-3cad-a89a-807f6e3490b1 | -6.1399 | -51.715401 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5963af4-ce51-3933-bf4c-2d07aaf1d462 | -5.2273 | -49.304699 | 2026-09-19 00:19:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 608be3ac-02fa-3611-8b30-8c404f7d2a7f | -15.8168 | -53.104801 | 2026-09-19 00:19:00 | METOP-B | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d28c3357-51fa-3ac7-b8b5-6b9cf3ed60f3 | -11.0836 | -48.2682 | 2026-09-19 00:19:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b74c88a7-4de0-3382-9deb-861267d00dc1 | -4.3793 | -55.2542 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ffba221-6e51-3f9e-aa35-810f5969cc89 | -7.572 | -57.675301 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec933f1f-d09d-3714-90b9-a8cd1a327f20 | -3.3577 | -50.453499 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1415dd0-72b1-310c-ae4a-a71c76be3dc8 | -10.9104 | -48.411098 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
