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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b18a22f-a30c-3236-8507-f76a7832a050 | -8.49019 | -44.75167 | 2026-09-11 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 74dd13f1-873a-341d-8dcd-2c25c22edc3b | -6.08261 | -57.3422 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1444e5d3-9b66-30fe-9051-e045568d1805 | -9.70081 | -43.45697 | 2026-09-11 04:51:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5bb8a2ab-5f3d-3b8e-b657-e3cc9f3b7258 | -3.36865 | -50.74398 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86b4e4d9-b245-3a72-8773-bf60e37c4b96 | -4.82288 | -42.88533 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f9687440-1f3f-3f27-b155-afb591686553 | -6.08306 | -57.3399 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3997375c-d555-38a6-be25-cb9c2b55f743 | -9.1573 | -49.98153 | 2026-09-11 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b68f568-af87-367f-88cd-c52ec51494c0 | -9.44861 | -51.18293 | 2026-09-11 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2777832c-01a1-3c5a-97f1-3b4578c19777 | -4.5384 | -54.96146 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0df6566b-5b01-3148-af32-4eb432246825 | -5.97569 | -57.77317 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d56c32f-23f7-3e0b-884f-215694f6efbe | -9.05856 | -45.78163 | 2026-09-11 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7720b2b6-0d35-3a69-a9c0-28ecf4d5d030 | -6.10726 | -57.65835 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69ad2888-ea5b-331a-b27e-8299c06b9500 | -6.79572 | -44.81381 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9ffbb860-0a21-3577-ba65-b14ee2764f68 | -2.87415 | -49.10082 | 2026-09-11 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ab812ee-05d8-3be6-8a0b-e118bb890e95 | -2.94472 | -50.49253 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5749e051-649c-38e2-98dc-993c993cc63e | -10.28489 | -45.30512 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a987a99d-f632-3668-9ad4-3d687bfcdb42 | -4.52787 | -54.95981 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d83aca4b-be0f-3cf0-9932-04bf4529be9d | -2.93789 | -50.46944 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94919de1-6b7a-38f8-9cad-5b04daeabee3 | -6.63107 | -55.30002 | 2026-09-11 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5190cb9-d7f0-355e-b702-3c29a24809b8 | -5.25989 | -50.97326 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f1829c1-3784-3abd-b024-c282f331f7b4 | -2.72291 | -57.61917 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99879a93-e4e4-3f6d-856c-a5fab45d1d8f | -5.97858 | -57.78078 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78fc13da-4b0f-3744-9186-1313f56a9c1b | -6.34135 | -57.8641 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fad8ad69-ae2a-3ca2-b714-86a9df04dbff | -4.29678 | -49.10437 | 2026-09-11 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 52e8e51c-be74-336c-9a0d-ef8a71a4e0f2 | -9.39435 | -49.39117 | 2026-09-11 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fc62515-389b-39f5-bf3c-e6f6ef1dbbae | -2.61137 | -47.74757 | 2026-09-11 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bf94932-5802-3230-9ebd-a08a93e052a2 | -3.13324 | -60.66327 | 2026-09-11 04:51:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca406929-fee0-374d-92df-9d74f8ca770b | -4.30103 | -49.10075 | 2026-09-11 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 67616ae9-bf98-346f-9b8f-7eb5e8ea45ca | -10.60733 | -45.22546 | 2026-09-11 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87714937-ebe6-312f-a99a-c2caa4776b3f | -2.4791 | -49.41065 | 2026-09-11 04:51:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ed54d77-c676-3d51-87d9-6746b971cb71 | -7.00784 | -43.87025 | 2026-09-11 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d13b0ec-2fb0-3082-b76e-29c29909ef18 | -9.17335 | -49.94866 | 2026-09-11 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c6438c6-d590-397d-83d4-df6327902040 | -2.73614 | -57.6173 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3be1764a-ca7f-31dd-aad8-5e8b725d7544 | -6.1014 | -47.38215 | 2026-09-11 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4782ffbc-52db-3f35-82e3-f82674de76a9 | -10.60226 | -45.22464 | 2026-09-11 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cccbd96-3325-319b-a8ab-eff808d1fab5 | -6.24517 | -51.68683 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b4468900-7965-366f-8ab1-d6a83f507aa1 | -6.24129 | -51.68985 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 482ef697-1c19-33df-9bc6-37361a8b1279 | -7.84705 | -56.58459 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4808fc0-7c80-303f-8844-8c6654b3bd63 | -5.7734 | -45.07612 | 2026-09-11 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0f0bb755-b8f0-3526-aa0b-005712e79cb3 | -2.94582 | -50.48537 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a54a7f70-670a-3eda-8a41-4dd74ba12eed | -4.56002 | -47.76119 | 2026-09-11 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09570604-51ae-3833-ba66-38db25dd6f1a | -10.60772 | -45.22249 | 2026-09-11 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fa44d74-df37-39eb-8812-749fe47e2c0e | -3.37826 | -50.40326 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05aae61d-b98d-3635-a855-2b3eb0290ddd | -4.53427 | -54.96481 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eeef171d-a074-3ff2-bd6b-3e90ab5f8ad7 | -6.11121 | -57.63429 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1dec52f8-dc7f-33cb-93ac-5a683b81163b | -6.19495 | -55.26048 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23ab2dc0-a0ce-37e3-b8d5-9ce3f2185e49 | -6.56791 | -58.98136 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59ae07fa-1d5b-3199-a02d-1c260072016e | -9.60731 | -46.77975 | 2026-09-11 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 737a04ff-955e-37c7-8658-50b809e4fe7d | -2.86237 | -49.53737 | 2026-09-11 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 09952dbf-6259-367b-bd27-41b10e97de9c | -7.34978 | -44.19201 | 2026-09-11 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e87f5141-130e-3567-8628-6bf7cd6841d1 | -3.24793 | -47.25034 | 2026-09-11 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd6a3e1a-517f-3b2b-9b76-54b6ec871acc | -5.97394 | -57.78382 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 832ac57c-5050-322e-8d1f-4f270bec253b | -3.09969 | -48.68076 | 2026-09-11 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06307cc2-b225-33c0-9617-fc187c184193 | -4.08418 | -56.30026 | 2026-09-11 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70def275-1bdd-36bb-a4da-191999edb386 | -8.48672 | -44.73888 | 2026-09-11 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b54c306a-1e6e-361e-9a25-bfdeee1d6971 | -4.3004 | -49.10493 | 2026-09-11 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4de47345-33ca-311e-a7b6-283bf7195424 | -3.51707 | -43.25869 | 2026-09-11 04:51:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d7472ce-4d90-3e5a-92bc-bb77a718e010 | -2.93845 | -50.46585 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9130cdfa-a59a-370f-a9f3-b13c47a0cf06 | -4.35709 | -47.56479 | 2026-09-11 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4755bb2e-9954-3503-a0ce-84adf65a0fec | -10.05771 | -46.27819 | 2026-09-11 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8cc9203-b61f-3e72-b746-9a95454f0803 | -9.15666 | -49.98584 | 2026-09-11 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17858fc9-f075-3a1e-8471-0c472582ebcd | -2.5243 | -48.13814 | 2026-09-11 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5e4fdf3-cef4-3678-9fb0-3a9e6b25e247 | -3.07599 | -51.33889 | 2026-09-11 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f8fa384-293f-37c3-906c-7c3e882a79fe | -10.41939 | -45.12898 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcd22b2f-2ee9-3945-ad20-30b8d47cb8ad | -4.53489 | -54.96092 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b86db4b5-51b5-3863-8f44-ac9480b50b66 | -2.94809 | -50.49305 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f42a7880-2959-34ca-86f9-97e946d806d0 | -2.85888 | -49.53684 | 2026-09-11 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e3b6ef51-6e09-37e5-b320-8c3c067b18b5 | -3.07413 | -50.33446 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f24abea-c7d5-31e5-8c27-691985b0ef8e | -6.08224 | -57.34497 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 001f983b-cc29-331d-8648-8925b9d5ec31 | -6.2001 | -55.27325 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b3ec427-037c-3e61-81d4-fffda0ee5d3a | -6.82393 | -58.98885 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8af965eb-d8c2-3293-bdba-f1a35c3e8600 | -6.1966 | -55.27269 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 471b7a49-6c66-381d-aebe-421d070ee910 | -6.20414 | -55.27723 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e2b08db-ba09-358c-8e3f-a3e50cc77c6c | -10.2208 | -45.21071 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2185cb09-afd3-32db-a9aa-9ab8773fe55f | -3.36529 | -50.74345 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fe13c4d-1dd1-3933-a012-7fd7e5ad07c6 | -2.71933 | -57.61465 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1da63cf5-8fb6-3be8-8ef6-ff0706d6bd00 | -9.90594 | -45.90745 | 2026-09-11 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb437d1a-cedc-3ec6-905f-c4ba05faf4c1 | -8.7104 | -49.6166 | 2026-09-11 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bc5574f7-45ae-3bed-bea9-d682f91eba70 | -2.73911 | -57.62568 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c233757d-f73a-394e-82d7-429a6b62b39c | -6.50391 | -58.38969 | 2026-09-11 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b8e972a-d324-36bf-802f-92b90f6a0979 | -6.79079 | -44.8129 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 97b7d983-32b1-3d14-8645-3629900cce1c | -5.67031 | -44.94157 | 2026-09-11 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 739d6eca-ed08-3d32-a380-dcca73281b77 | -2.72525 | -57.63143 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ee0678b-ab92-3e3b-be8c-b0b35047650a | -2.8583 | -49.54071 | 2026-09-11 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 03986df3-bc22-31bf-ab49-31d4d24c6615 | -2.72774 | -57.61597 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94b30be8-4f9e-3d7a-9db9-d605fe9043ff | -9.3121 | -44.37374 | 2026-09-11 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e00126b-280e-3ac1-b60f-b2e1f7a73504 | -4.28108 | -46.53071 | 2026-09-11 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e1648749-cdff-3cd3-bfa3-5c4271510b3d | -9.17701 | -49.9492 | 2026-09-11 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40b4466c-e02c-3b3d-98d1-ec039513a04d | -2.68827 | -57.51543 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b412bf5-288f-3db8-9775-864a2d41734d | -4.83243 | -55.76463 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4da8125-10d1-3b26-adff-051bbe610cb1 | -6.18784 | -57.754 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16ee6815-c48a-3953-8d67-cd88b64a1d8e | -3.37036 | -50.75519 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d077276f-926c-3a0c-9296-9d86a41cc103 | -8.03204 | -43.84997 | 2026-09-11 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5592fe48-49ed-311e-a2f0-f295348319e1 | -2.86178 | -49.54124 | 2026-09-11 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b7705028-f4de-36cc-b486-3ee73d37aac6 | -2.9339 | -50.46188 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b422f32f-ff1c-3bd9-bf90-041dd3a160bc | -10.27381 | -45.27091 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9f2f210-f749-3953-83a4-35f283879fd6 | -4.56394 | -47.76178 | 2026-09-11 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ceaae57-bb18-34a6-af47-75e0e6e5a4ca | -5.05246 | -49.7061 | 2026-09-11 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13d901d7-cb8f-3064-bb5c-4fd6c4c98e1b | -2.92171 | -54.11488 | 2026-09-11 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1541d6ae-7129-3a76-abf3-bb61bb164d67 | -5.33228 | -49.16475 | 2026-09-11 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
