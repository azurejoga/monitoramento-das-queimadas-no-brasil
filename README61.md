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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62b8737b-6aa4-3724-acb2-1fdb0ff65f40 | -11.23298 | -54.00752 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a6dfb82c-2854-35a6-a245-3a22ac633ba7 | -11.71783 | -54.5437 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf25ab29-862e-335f-8df3-5f8e0d4b1404 | -10.78761 | -54.00242 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2ecaf50-3eb1-3afd-b2bf-17b7df83274a | -8.99041 | -65.44514 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7310ff15-a1ef-3c92-8c9d-70c6549f3df6 | -11.77539 | -47.6616 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12b967f8-de6c-3d4f-b0b1-52590476bf6a | -10.79409 | -53.99777 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b8ebecd-7ba8-395b-a6b9-e7b1ac1c75dc | -10.26613 | -64.50322 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f6b1a94d-c0fe-32a0-8700-32518daf1e8c | -9.88018 | -60.26404 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 366c6c41-7e02-3558-85a8-dfab301e5353 | -9.86479 | -60.26593 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd665591-7d46-307e-a5a8-a55d5fdabe01 | -15.30902 | -52.75021 | 2026-08-28 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf10630b-d6a4-3791-85fd-c6a074588be8 | -14.87865 | -52.59626 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 499a010c-aa27-31bd-ba45-7104b86a15bb | -14.43278 | -53.38483 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 334806e6-840a-3c1d-adf6-08b1b71c31f1 | -10.78823 | -53.99828 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f505aec-a9da-3f52-8588-524e447ca6c1 | -14.18661 | -52.83263 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71abaef5-536f-301c-b440-3619c41e1519 | -13.60436 | -45.78373 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c08fd006-29a5-3b1a-b98d-6c2541290f99 | -14.58202 | -53.17731 | 2026-08-28 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90e7d490-70ef-3dd8-a4db-6a0d354981d1 | -14.99302 | -52.60807 | 2026-08-28 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf3d8340-62e5-355e-8455-2f71c219df56 | -8.63247 | -66.53886 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b5922ce-1b03-3444-9166-d8ee8e59f65c | -12.43517 | -43.41367 | 2026-08-28 05:12:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 6f306004-5850-3d05-898e-941df145f29a | -11.23303 | -53.99621 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1e60293-219f-3962-9572-efc29bc194b9 | -11.16512 | -51.21904 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c9ee9ce-1d16-3bd6-86f1-b53efb4fd42f | -11.19698 | -51.23447 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25c49b30-e8a5-32d4-8fce-6b174ed79935 | -13.42341 | -51.86974 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89253c06-18f0-3158-849a-909817758e31 | -11.20199 | -55.09584 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f8eabd1-5715-3e6e-a538-b6d4f7b8efb8 | -8.9858 | -65.441 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa821e60-59e3-3c3a-848c-e59e8207bc8c | -12.28226 | -50.58709 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72993e13-88a6-3e05-bc69-fcd3f43f1e3c | -11.27488 | -54.02243 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24860bbd-bad6-3a00-a1ba-348e929bcd52 | -11.6393 | -46.73746 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68a695ab-7ac0-33d6-9797-c8e603c45d52 | -10.84581 | -50.51751 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd6e5bee-86e4-3a02-ab7d-3dfe6a51bc19 | -11.81618 | -47.20961 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dedd8117-1a4e-31e9-a5d0-dd84d1441752 | -12.28495 | -50.60145 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1e2b8935-a1ba-36c6-870b-9239f06bd630 | -11.20123 | -51.23508 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d43aa4e-5dc4-3b0d-8325-b5623df0f7db | -11.27611 | -54.01408 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 277de77c-4e62-3a89-a008-511ac1031bfb | -11.2324 | -54.00038 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| decb162d-40bd-3d72-adce-44d8f6341003 | -9.84903 | -65.02265 | 2026-08-28 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e2e0f4a-c6e0-3367-9c12-4d850aaebf32 | -14.15075 | -52.82725 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6796ba82-f9b8-3ac9-aa42-129eba936541 | -9.88311 | -60.26906 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23bb7edb-93f6-3bdd-8fee-fb7057234550 | -11.79721 | -47.67564 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d448179-ee0f-359d-8fab-e9c07785e5f0 | -11.82645 | -47.21869 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 56a71049-e6fe-32f2-8a28-8123d2caf192 | -14.18336 | -52.82674 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f7157b4-f1d9-336c-99ec-e4c1e6def614 | -10.79288 | -54.00606 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb44d314-426c-37f2-a942-7346014cb54d | -13.83441 | -54.04486 | 2026-08-28 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e3251dc-267b-37c5-a69f-3e605e516f28 | -12.28166 | -50.59167 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c36c3e25-8125-38a8-bda7-0b2a5c6f8dc8 | -11.20231 | -51.22707 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 7222a077-7b21-3bbf-80bc-7ff1f241663a | -11.28864 | -54.02879 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 81f86ef9-bb37-3f70-86d3-02862930ea22 | -15.51139 | -55.95147 | 2026-08-28 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 765742cf-787e-3f3a-b5d2-bafbb4409771 | -13.42394 | -51.86582 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0404bce6-121c-3b95-b992-a5512bde7cd0 | -11.23719 | -54.00386 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1adb5e58-9bf3-3593-bc1b-193a32f75e47 | -14.92346 | -52.59837 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8f421d3-0f60-3428-b2d6-802b17b23b71 | -12.26093 | -50.57479 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 148ae622-b09d-3685-a86d-c629f26b1f23 | -14.94036 | -52.59671 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cf435832-1a70-3e22-a55f-e6d56af9366d | -15.60229 | -46.58101 | 2026-08-28 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9fce8083-04b5-3f8e-aac8-2062b65336d9 | -10.76147 | -53.9815 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad65e97b-4360-35a5-8579-1b241261bc07 | -12.778 | -46.44923 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6debc0b-6db9-37ac-a915-7760d22ba780 | -11.2348 | -53.995 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f6c1d88-6206-3170-8c12-1c6ae5b45209 | -11.82085 | -47.21783 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a57f4411-7f2b-31a2-961f-a7717697f8a1 | -10.98952 | -51.09004 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f79087f-272b-31b4-9f3a-d658f9d7aa6c | -14.98838 | -52.6072 | 2026-08-28 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1757b03-4fce-3196-84fd-86b63dabf150 | -14.88224 | -52.60043 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 11797af0-2688-38bd-a6d9-f3921e5ded78 | -11.73485 | -54.5504 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09a3cbe9-1e53-34f1-9900-42de8441698b | -11.7508 | -54.51588 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d514a3c8-d504-3ffa-9abe-97e522f8762a | -10.79476 | -54.00351 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26f1b3f2-32ab-32b4-a326-5cd794e0f45f | -14.16344 | -52.82368 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a9c9f4f-16aa-346b-843b-c0ef54d25a51 | -10.84138 | -50.51689 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85a1d202-ce51-3b82-922b-eb7350df36fe | -11.2138 | -54.00186 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1009629-9155-3cb9-98fb-776424d323fc | -11.33493 | -48.37986 | 2026-08-28 05:12:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed5b53f7-c352-3b8d-a9cc-fd2b4d3d7fce | -11.74667 | -54.51935 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d10f272e-c234-3b27-aab9-bab7ffd8e841 | -12.78113 | -46.44839 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c6d7285-67a1-30bc-b2ec-68db577dbfb2 | -12.25423 | -50.5757 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 549e4dda-76ed-364e-8a51-f9564c06b95c | -9.84426 | -60.27589 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0c20237-ea13-3548-9425-e9f472472d5c | -12.25642 | -50.57417 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57eacbe6-ffec-3d14-9371-ed26060e8c2f | -8.87532 | -66.90673 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 04e91d9f-83e0-3637-9a1d-86ba4db4a97e | -12.78401 | -46.4497 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 044b9def-e919-3d31-af40-cdb9d932e34f | -11.63833 | -46.74527 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1b7f410-4e8d-349a-a436-1f6e75a60320 | -9.05044 | -65.44475 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77e2d2a7-1d70-38fe-8182-6f7f9d036aea | -11.81103 | -47.20508 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0bd644a9-166d-3d57-8595-8696a7946382 | -10.75642 | -54.03976 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2994d9cb-71df-330d-947d-d9d768d51e21 | -13.74738 | -52.01895 | 2026-08-28 05:12:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 554b1436-08ff-3df7-a824-6a38af2c22e1 | -13.43259 | -54.01535 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9551303-16b1-3989-8785-2ce0028c87aa | -8.59444 | -70.21298 | 2026-08-28 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 335c7ec2-e244-3f53-8337-9c452311870c | -15.79646 | -56.45716 | 2026-08-28 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6aa3947-a487-396c-93d8-0c6415a5f0f6 | -11.01461 | -49.6552 | 2026-08-28 05:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8857f62f-03d1-387b-9ae7-f896a5bc5800 | -8.99616 | -65.44296 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c02ebd5e-56be-327c-8abf-26c17d46df55 | -14.16742 | -52.82431 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a9815c8-4c26-38c7-a458-8f0ccd087115 | -11.71842 | -54.5397 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 950f296e-a7a9-3a95-813d-4a496a4052ad | -11.76832 | -47.63966 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb3cca66-e008-3d98-ad51-cbfe0b612db1 | -10.56875 | -57.48765 | 2026-08-28 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67a477ea-d300-3cc2-8a89-702379594c2b | -12.29006 | -50.5975 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b8c5aed-ceb3-367b-b43a-63c4f9625873 | -11.27786 | -54.02717 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d3f5753-cbf5-3802-ad8d-48fee96aae72 | -12.20856 | -50.57405 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcff3184-b95b-3e17-881a-734695ed281a | -14.51201 | -59.82311 | 2026-08-28 05:12:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aff240f-c66a-34ed-828d-b0b7ae9de5b6 | -12.68987 | -48.43417 | 2026-08-28 05:12:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 312fe049-3132-30bb-a8f0-4caabfba25ba | -11.72665 | -54.53275 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1eec5406-ea08-30d9-a11c-6449564c0315 | -10.39323 | -61.24243 | 2026-08-28 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9eaa2b9d-b474-3505-a346-3068da3f5ef1 | -13.41146 | -51.41977 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 574dc1c0-fe78-3faa-b08a-3a8c05034048 | -8.99212 | -65.43565 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b7813ff-4d42-3755-839a-0375d7820d9f | -14.32329 | -51.70812 | 2026-08-28 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8e7564d-fd15-3e7e-be98-33bf4cdd8d80 | -12.9143 | -59.88267 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de0b4783-d635-3e8f-90ef-a4ae9b8dc1fa | -8.9975 | -65.44128 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7afe4039-5001-3889-adff-aa34ab75e459 | -12.78454 | -46.44536 | 2026-08-28 05:12:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README62.md)
