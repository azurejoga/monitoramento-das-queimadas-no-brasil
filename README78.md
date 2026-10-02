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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85c6cb8f-b294-36d7-8e1b-bd6638354a20 | -6.00486 | -53.54189 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4993cea-ead1-3e74-bff2-4b8d43e747c3 | -10.60001 | -50.08109 | 2026-10-02 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92488a3f-3acf-3c89-9dca-4b4bd408434c | -7.73327 | -54.80192 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5852c07d-9ffe-3607-82c8-a2812bb57ac3 | -7.4901 | -54.99534 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8fef19df-b380-3b11-8d3f-bee4242c8460 | -7.74311 | -54.79499 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 464d58cd-3f77-32b7-8d55-03ccfd8a0ad4 | -10.24826 | -49.67138 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b8b1f27-b3a4-3bf4-9942-0e5633b8b089 | -7.04744 | -55.6386 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ac6e7f3-cec6-38af-9260-e1934d64d556 | -7.05813 | -55.62221 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38f708ec-f35d-3c99-908b-af0da7d8601d | -7.05149 | -55.63922 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fffb74b5-df07-3702-89e9-310a3c699caa | -7.54815 | -55.03499 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1893e96-eea4-30a5-8a6e-57a0176d8884 | -6.08073 | -53.30109 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 945f58b2-ffbc-38ad-ae18-b09a4c585e56 | -6.31707 | -54.78428 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df0188ef-a3f9-32c8-9256-c0a2f7c9ae3a | -8.16805 | -54.79656 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f6c391f-6bff-30e1-a776-a528c4803d26 | -7.51144 | -47.33532 | 2026-10-02 05:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46538789-3a9e-39d8-8721-a42892412f24 | -7.28203 | -55.59027 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03cff474-03fe-3a53-bcf9-60e353bcbbf6 | -6.26174 | -55.43763 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6387b761-b07b-32ac-a42c-36de9e9e1cc8 | -7.34032 | -55.22294 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b31e2d6-8f69-3563-a725-1fd888c76bd3 | -9.88151 | -65.14168 | 2026-10-02 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8af0613-4684-3d33-af0d-d34309dd8f62 | -8.07971 | -54.88887 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2ae2605-ef4c-32a8-bbce-680b72341fc5 | -7.12696 | -55.71866 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a784fc59-2a4a-3d86-9e72-99f9a9061d4d | -7.46098 | -54.98675 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02aa5088-3bf2-353f-a2a7-f53bb4e571c7 | -7.24176 | -55.60995 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c9fa124-ae43-3216-89f2-a2c8b7f141a8 | -7.54983 | -55.02335 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c31ea098-3848-3db0-a501-d162d2a174b3 | -6.13485 | -53.29005 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e977c320-6f95-3f51-aa76-bab0dfd74e46 | -8.54083 | -54.56728 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea3b14bc-a770-369e-b9dd-df15c216dedb | -7.74683 | -54.79973 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ffaf319-e278-3fdf-9fd6-625a563157a1 | -8.15833 | -54.833 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c3774e4-e1fb-392c-b94c-5285459c2b88 | -7.74742 | -54.79565 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de9bf8f2-2947-36bb-96e2-8eeed25f1b30 | -7.72285 | -54.81296 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a0d86d5-0473-3acc-bc4f-ce71e957e72f | -8.25779 | -54.73081 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da0447e3-826b-3dc7-9c18-a89768f32d9a | -8.1637 | -54.79593 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c83fccaf-3794-39a6-b076-0a8bd8d62282 | -10.75196 | -54.0867 | 2026-10-02 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1b1b93a9-c1fc-3c92-a9f6-4dd2f62355a8 | -6.20399 | -53.25811 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de516071-f654-3dc2-92f7-2bb4520724d1 | -7.71854 | -54.81229 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48f83a8d-6f55-305a-9966-a9ca127e6994 | -10.41079 | -53.76879 | 2026-10-02 05:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43c1259b-af13-3a5d-a630-599facdcd62e | -7.56853 | -55.13267 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2369a7b-1637-300a-b70f-e9fd8db1faff | -8.21415 | -55.09613 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b62ea70-04a7-334e-8ce5-3543a0949eb5 | -7.54176 | -56.12823 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80c72047-7069-3c1a-bf99-facc532822c4 | -7.39849 | -55.2117 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b465f79c-2d5a-3d46-8f1f-2a3debd359d2 | -6.3896 | -56.41519 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8420ebe5-b9ad-365f-818e-98c15fbf3078 | -8.2301 | -55.28316 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96555b54-3582-3008-9986-1012593741ff | -10.25395 | -49.67713 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ad3d578-c5c9-354c-a0d4-b7037022a96c | -7.54927 | -55.02723 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9300d9e-158f-3ee5-99e4-c8106c7f8094 | -5.97323 | -55.37342 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10e43d3d-a5e4-3ca5-8d00-364170c73faf | -7.71794 | -54.8164 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 138dda6c-74a4-365a-a524-b9f49a3ad2bf | -10.81993 | -51.09503 | 2026-10-02 05:36:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b703ce58-4596-3638-b410-130902f2debe | -7.82391 | -55.11985 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18b7bcd7-01fe-3a05-8c8c-00c5935a8180 | -7.39906 | -55.20773 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 1b6650c0-404b-300f-a444-ed3bb25e9a02 | -7.28503 | -55.59814 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86e7c58c-6240-3305-8400-59b5ba955e3c | -6.24568 | -53.13619 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25531c98-d398-3209-af9e-a3411a511334 | -7.05097 | -55.6427 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb677463-4957-308f-abeb-16f00a8aded3 | -7.28149 | -55.59391 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f577408-aa1e-367f-9fad-c0d569fcbb90 | -8.1619 | -54.80833 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 545e3400-7032-30b2-a2cd-06fa94ec043b | -7.5442 | -56.13887 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04f2c9cb-bb9e-3685-aa7b-c668f9fc0d03 | -6.43783 | -55.8034 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a197c0cc-ed38-3a03-b398-82da590f6129 | -7.83238 | -55.1211 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e212650-7c15-3b90-81ad-5ed59520d506 | -9.88527 | -65.14235 | 2026-10-02 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86e01b7d-b276-3a25-a28d-95584a55be06 | -6.40628 | -56.40819 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e2a872f-060d-3b54-b24a-9fbf4478e6be | -6.19127 | -53.1789 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fdca7af-32e3-3abd-82c4-89f2613426ec | -10.26217 | -49.66277 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4b9d81f1-6e15-31c0-9315-e137ae0a5caa | -5.99962 | -53.54556 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7ad0fb2-2265-3d94-b8b9-01945dccf602 | -6.1516 | -52.80513 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06253346-6047-3032-b268-94efe7924cec | -10.25135 | -49.67234 | 2026-10-02 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66a5781f-3e5f-3601-9231-810eebd377f8 | -7.04443 | -55.63097 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9e27973-30af-34da-a125-2463d63f4a14 | -8.30809 | -54.72442 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b368fea-8448-3896-bbe2-9c60cfa84e77 | -7.83496 | -55.13335 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b12a8ef1-03e4-3b95-a71f-b73d1b48cb32 | -7.8454 | -56.61168 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25b0db47-712f-304b-9036-2b38c59b6256 | -7.74563 | -54.80792 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23006dc4-6d36-3a07-bd8b-1a25d2e74ac1 | -7.72685 | -54.75488 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3951c26-4324-3e6a-93ed-587be0f770c6 | -8.5449 | -54.56129 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f569fdd0-ce03-303e-87f0-5b27e88774ef | -7.04796 | -55.63511 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe7a90dd-9fee-3aac-bb52-e34efccfe880 | -8.4173 | -54.70766 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2789323-dd7d-35d2-8ee3-5913c75ef9ef | -6.24021 | -53.14056 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 485a4215-7aa3-3f77-a171-63a4fd2bece5 | -8.16685 | -54.8048 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa717064-48c5-3af9-bbb8-42a7bdcace3a | -6.29863 | -58.1467 | 2026-10-02 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85d8c867-0b83-3d8a-b8cb-8af74adb0842 | -8.5443 | -54.56569 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e61cf5e8-478c-366f-adcd-e8d6beac1eb5 | -6.24419 | -53.14642 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 863e8f93-08ed-325c-ab06-09700b82f511 | -7.74994 | -54.80854 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 173abcec-32ad-3207-8d76-bd5430764cd7 | -6.23147 | -53.13407 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd9ca18d-e76e-32ac-b056-6fe9814759f4 | -7.46601 | -55.01189 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a70baf1-1a20-3e07-a656-3275e2357d0c | -6.2387 | -53.15096 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0f3e5f11-ebb2-3da1-b39c-bdd3664a3afa | -6.8252 | -58.86093 | 2026-10-02 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a34c59cf-4312-3c74-8150-8e9cfbdba16d | -8.30274 | -54.72888 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3c5e285-43d2-3e6d-8a8b-83773cf7ad49 | -7.39377 | -55.21484 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8f8bd8c6-29f3-3c71-b494-25a493fd4573 | -7.27689 | -55.59694 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2b5eca3-7b29-39a7-8023-c222c63deaa0 | -5.76936 | -57.46811 | 2026-10-02 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d27d83e-69b0-3eab-b3b5-1bd5197cbad8 | -7.27337 | -55.5926 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 709cd7a2-f2f8-3cfe-ba6f-6de0faa6c094 | -7.41928 | -55.5886 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 719c475d-9996-3736-93e3-bb443efc84ea | -7.72715 | -54.81369 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13ed761e-27a9-3e0d-ba0d-c001514f0527 | -6.10589 | -53.09156 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3d36c3b-20d3-33e7-863f-2d5aebfe06fa | -8.17675 | -54.79779 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5dc2a3a-7b56-3a8c-aadf-4d13accaad29 | -7.41982 | -55.58498 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 80fe6571-85eb-35f4-a71d-36cc981d74d3 | -8.20272 | -54.70969 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d0eaaee-9259-30cb-88d6-6d231a4cd51b | -8.26524 | -55.68821 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f67fe848-1601-3b38-b892-6f7be79bd88f | -8.54935 | -54.56193 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6e68e11-595b-308c-b3e4-a87c3b54fade | -7.6985 | -54.76758 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f371c7c9-a50a-39fc-8997-c231d2d46d49 | -6.24168 | -53.13043 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d8321ea-d6d0-3c46-802b-12978d828fee | -8.22971 | -55.28678 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f74240d4-52d6-3cd2-9da0-6a8ca756a3f1 | -6.85645 | -59.04179 | 2026-10-02 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b18c9519-aa99-3afc-88f1-172e5915bb44 | -7.04848 | -55.6316 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README79.md)
