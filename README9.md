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
| 24b4634f-1d13-3d2d-bd91-bffdceace303 | -11.06303 | -52.46968 | 2026-06-21 05:29:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95a3fd71-1b99-3d7f-81aa-98b06a2f27b9 | -9.18464 | -58.05795 | 2026-06-21 05:29:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 098d28a0-c40b-389b-9f5a-bd75a882ea4e | -11.06253 | -52.47389 | 2026-06-21 05:29:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51f37d86-6d17-3156-8a9e-459388272bdc | -8.46708 | -51.5349 | 2026-06-21 05:29:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a0a4c97-6a88-3027-9aad-bf77a6efb0f2 | -10.83525 | -49.11989 | 2026-06-21 05:29:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a285b0a-f945-3f7b-8bcd-c1dd41a909bd | -11.06836 | -52.47459 | 2026-06-21 05:29:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b69c31d8-f924-377a-bca0-4fb23545b847 | -8.68066 | -63.62037 | 2026-06-21 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adcf196d-1082-37de-bf2c-6ea9edfb2241 | -11.06353 | -52.46547 | 2026-06-21 05:29:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 525d7799-d7dd-367e-bdb8-cade1c904daf | -9.53174 | -57.37558 | 2026-06-21 05:29:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdbf21b3-ba51-3d78-8b71-816c0dcb5102 | -9.18854 | -58.05854 | 2026-06-21 05:29:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e435912d-5e17-336e-b24c-51d388a23130 | -10.51898 | -51.94061 | 2026-06-21 05:29:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d8e075e-ca9f-3ddf-ba39-9d7b04a9de62 | -8.35546 | -50.50535 | 2026-06-21 05:29:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6c761393-9c2d-3ba5-a589-0336acb652d4 | -10.16137 | -51.65205 | 2026-06-21 05:29:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55e10b35-8fab-3091-a890-a8db6a2a5c66 | -8.34974 | -50.49936 | 2026-06-21 05:29:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4651efc0-c1bd-3d5c-be38-34d2b1cc2feb | -11.1168 | -54.1294 | 2026-06-21 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 3e861763-bd29-3fee-ba9c-d177687e37e4 | -11.1165 | -54.1499 | 2026-06-21 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 38752121-1313-3197-8c19-aae2c476735c | -11.0976 | -54.1516 | 2026-06-21 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.8 |
| f0073740-9dab-3f9f-8085-d642f2b88975 | -11.0979 | -54.1311 | 2026-06-21 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 7b183e85-65e7-3a8f-aa1e-41787c400b00 | -11.09258 | -54.14828 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bfec9023-39cd-32bf-8f11-5a05f0c42b3e | -11.09741 | -54.15205 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 475b3ad1-8d56-3111-b2da-b8b62871eb3a | -11.1143 | -54.14452 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7ea10299-7121-387e-93ff-c2506cca1228 | -14.08959 | -52.19466 | 2026-06-21 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03bd8d3c-b788-3189-9cb6-99acf723722a | -11.10989 | -54.13746 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 12ca4457-db5f-3d02-abb4-f5c12ce844ac | -11.10866 | -54.14706 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b8101fe6-5a28-31f1-8a67-045c623830a4 | -11.10425 | -54.14004 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 0d3cce26-f185-330a-a9e2-dc209f697e8a | -11.10223 | -54.1559 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07f0dce7-0e50-388c-a061-ce9429a21b73 | -10.68577 | -60.75037 | 2026-06-21 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 50036d22-3fd3-394b-92ed-e8df6c291ace | -11.73134 | -62.2988 | 2026-06-21 05:31:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ad19b06-ca32-30d5-afed-1c2819126e95 | -11.10507 | -54.13358 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 995aaab3-fa8d-3fe2-a017-b12446832bda | -15.81187 | -58.64999 | 2026-06-21 05:31:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5eebc904-6ade-3b87-806c-dda9909f75f1 | -11.09781 | -54.14893 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d8bab657-573a-3216-9993-6ec58c7dd1a6 | -12.42552 | -54.18084 | 2026-06-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f9250fb-e1ae-3a92-a192-aef0ee77f631 | -11.10343 | -54.14643 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 2bf8fb26-c1e4-3764-83b8-4c119c09725c | -10.93238 | -56.84669 | 2026-06-21 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ae0dd68-bcb6-3289-9ada-f32a04a40234 | -10.68921 | -60.75091 | 2026-06-21 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 205240f6-ffa7-3fa2-b4b2-3dab397bf32b | -11.10826 | -54.15023 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 42cf952a-a765-3244-ae48-c21e8370d8d2 | -11.09861 | -54.14257 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 93f96078-4fd4-3b23-bda9-fa04b4cd59c7 | -11.11029 | -54.13427 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6b201e48-de61-393e-864e-7b2cc1411efc | -11.09943 | -54.13609 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| fe7c3d57-db51-3d02-b870-25b893624464 | -10.92805 | -56.84608 | 2026-06-21 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d3f8146-1911-37a6-9602-12bded8d76ed | -14.09578 | -52.19514 | 2026-06-21 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9a09aef-5ffb-313c-a0dc-5db8066a92ee | -11.09902 | -54.13932 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 6ddfa734-5379-330e-9485-a64d312b0114 | -11.10466 | -54.13681 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| ed84799f-470f-3695-8ec6-c2ab94e41841 | -11.64783 | -52.87143 | 2026-06-21 05:31:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac4afdc4-b414-3c92-9f29-5319ea52cefb | -12.41841 | -54.18602 | 2026-06-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 113b7b71-5afe-313c-9f32-d6e65442b3a6 | -11.0934 | -54.14184 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2ea5e55c-36e6-39b0-b238-2e467f51df3b | -10.6852 | -60.75422 | 2026-06-21 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 1c788b4b-6e5d-3f08-9e1c-85ae920a42f2 | -11.27682 | -58.31207 | 2026-06-21 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edce2fa3-78b6-3149-addd-bc749ef771c1 | -11.11471 | -54.14133 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| e5f4dc41-dbe7-306a-8326-45f77994c7cf | -11.62338 | -55.18642 | 2026-06-21 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b016dd8-c4de-3b5c-887f-445b5731b7e3 | -12.42413 | -54.18325 | 2026-06-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b28878ed-1d7c-34a7-9991-d5f8a2d3bc22 | -12.42372 | -54.18668 | 2026-06-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5ff78ed-1130-3af3-a640-f8226ab004ea | -11.10744 | -54.15663 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fb3c6da6-04a5-353a-8993-f1de7c5b771f | -10.68464 | -60.75806 | 2026-06-21 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b4ac6bfc-d134-3d83-81f0-ba07bbbc2610 | -10.27405 | -60.54821 | 2026-06-21 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f2bdf55c-f54f-32ba-ba01-50924316d14d | -11.10303 | -54.14957 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9565ba70-c24c-36dc-bdc4-04589a7105e9 | -12.42509 | -54.18425 | 2026-06-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d514ab59-39c9-3d42-a01f-4f4082854e9e | -11.09298 | -54.1451 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f3248682-17c1-31c6-851f-121a004c6e1d | -11.66597 | -56.76435 | 2026-06-21 05:31:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0461f4a-eeec-3b9c-adf6-be36be7a36fb | -11.10907 | -54.14387 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d52889a6-0833-3949-bbeb-b771e48f417a | -10.93183 | -56.85078 | 2026-06-21 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39d27352-061e-34e3-b50e-d94e957e05a5 | -11.10948 | -54.14066 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 7870b438-415b-3a2d-bcd1-62a128b574b2 | -12.42679 | -58.41858 | 2026-06-21 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e3aa85c-2a7f-36e2-a880-f1fbe816864d | -12.42453 | -54.17982 | 2026-06-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65150135-d18e-33c7-9761-e82a0e2c83d6 | -12.41935 | -54.18702 | 2026-06-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 362041bf-2c41-3567-9f3c-f5dde1566369 | -10.69323 | -60.7476 | 2026-06-21 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 882233a1-441c-36fc-9922-0bd155cc059a | -10.68978 | -60.74707 | 2026-06-21 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 587767ed-db9a-38dc-81de-9ca8acee3919 | -11.10264 | -54.1527 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8e391e3b-1ecb-30b7-90c1-115ada96b7c9 | -11.11389 | -54.14772 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c1f47e14-e4e2-34f9-87d5-1b76e443bf63 | -10.9275 | -56.85019 | 2026-06-21 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3bf6442-2441-3727-9b78-9d4361a9518f | -11.10786 | -54.1534 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 64fe5247-3d7a-3c58-874f-10c6bdf3e5ba | -11.09381 | -54.13858 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a5ae8a6f-035a-3264-8da6-a9fcd0c6b543 | -11.09821 | -54.14579 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 64959187-3971-32e0-8141-ba1531891359 | -11.10384 | -54.14324 | 2026-06-21 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| c1c3d312-1edf-30b5-a42e-ac0f43137f95 | -11.1165 | -54.1499 | 2026-06-21 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 5e107f54-cf4a-3ee0-ace7-54342275cfb8 | -11.1168 | -54.1294 | 2026-06-21 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 5daba593-86ca-3965-b086-8679893f0b94 | -11.0979 | -54.1311 | 2026-06-21 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.1 |
| e867ed98-4747-36dd-90ca-c7a50276a499 | -11.0976 | -54.1516 | 2026-06-21 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 37dee8c9-83ba-38ed-818a-2b264398f4ae | -11.1165 | -54.1499 | 2026-06-21 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| ab826fda-d0f4-36e8-b41e-b796a372b7e2 | -11.1168 | -54.1294 | 2026-06-21 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 95e587cd-78ef-3295-8669-9011420d9b76 | -11.0976 | -54.1516 | 2026-06-21 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 174.9 |
| 6885a43d-19c8-3a97-93a7-eacedca0ee6e | -11.0979 | -54.1311 | 2026-06-21 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.4 |
| c1f37fc1-34c1-3df4-b5af-276207507cb3 | -11.1168 | -54.1294 | 2026-06-21 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| bd6a9328-5837-3ef8-b9b4-59f3890761d9 | -11.1165 | -54.1499 | 2026-06-21 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 5096d02e-30c4-3499-a8ab-2a3a29916468 | -11.0979 | -54.1311 | 2026-06-21 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 730240f1-81f8-34e8-a93c-5f7b8341627d | -11.0976 | -54.1516 | 2026-06-21 06:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 49053436-3c45-3c11-9567-1ceb81a2eb5c | -6.99889 | -42.88313 | 2026-06-21 06:03:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 11c89dfe-45d9-3bbb-8a7e-b92058b32748 | -11.88694 | -43.82695 | 2026-06-21 06:03:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cc0da18a-de2f-3cf9-b0d1-0ae96e1609ce | -6.50008 | -42.21363 | 2026-06-21 06:03:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 5c41a4f2-9940-31b4-b194-9012c2000c31 | -3.84854 | -54.22961 | 2026-06-21 06:03:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdc6da43-2824-327c-b7de-a921c7d8e37d | -3.84961 | -54.22245 | 2026-06-21 06:03:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 700122f3-2748-3f03-b327-e8c8bc713513 | -16.06008 | -42.08827 | 2026-06-21 06:05:00 | AQUA_M-M | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| f5714fa4-91da-303b-b177-13a5cf9a0cb5 | -12.5119 | -48.29995 | 2026-06-21 06:05:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| decf1d5a-778d-3ae2-acc4-52c26c90d0ea | -10.6887 | -60.75472 | 2026-06-21 06:05:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a8182280-129a-3859-8afc-228814dd7a7b | -9.18128 | -58.05963 | 2026-06-21 06:05:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46639856-9ffd-30d1-8b13-2a75cfafd3c2 | -10.68344 | -60.75397 | 2026-06-21 06:05:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5f412d13-55f8-3f01-a355-dc94b524ceee | -10.68428 | -60.74743 | 2026-06-21 06:05:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d536703-f68d-3fcd-85d5-bf4100e8fe9f | -10.27475 | -60.54597 | 2026-06-21 06:05:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a79bba3e-a5ad-31c3-9e07-53050e8f6dbe | -9.18794 | -58.05901 | 2026-06-21 06:05:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec10727f-f387-3e6f-98bf-adc40b916e1e | -9.18742 | -58.06053 | 2026-06-21 06:05:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README10.md)
