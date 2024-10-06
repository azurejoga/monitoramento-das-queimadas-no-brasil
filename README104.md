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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78a69b9d-5f13-3d67-bfc3-c74779ebcc61 | -10.43527 | -50.69889 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 760.8 |
| 2e4d421a-e726-356e-9711-6963bb077c1d | -10.43457 | -50.70415 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 760.8 |
| 678a4cd6-3eea-3769-b043-25782ccddaf6 | -10.43387 | -50.70942 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 11d1efd5-3881-3245-8980-13df83d2b5f5 | -10.43367 | -50.78332 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35b5f84d-434c-35f4-985e-97029b00254b | -10.43317 | -50.71466 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| a17c742e-5b25-3458-9ace-e5ed7bc7da3f | -10.43257 | -50.68269 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 912ba1df-299a-3a24-be4c-99fa664628dd | -10.43248 | -50.71987 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0f130b54-2a78-384b-839a-29298e975cf5 | -10.43188 | -50.68788 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8bd22dad-cc56-3a95-b059-ed0941714c9b | -10.43178 | -50.72507 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2bdfc09c-b6af-3b75-9a45-3fe54134fef7 | -10.43119 | -50.69302 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ea127aa-93b1-3c61-9516-9c20f14d4295 | -10.43109 | -50.73029 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| edadf996-a861-3de8-a974-4cb5a9c4f950 | -10.4305 | -50.69821 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 227b512a-cc13-3d13-8fcb-69845b06997d | -10.42911 | -50.70872 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 433.6 |
| 46951a98-bf09-3f78-9a64-891aacb66684 | -10.42841 | -50.71397 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 433.6 |
| 9f473ffd-996a-396a-844e-35cb0d066185 | -10.42772 | -50.71917 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f623a790-99ae-3869-90f5-5a6dde837036 | -10.42709 | -50.68729 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ed72e82-76b4-3284-b8d3-fe51db339ce5 | -10.42702 | -50.72438 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6178a7c5-e4ee-34ca-ba75-0b2df94fc743 | -10.42641 | -50.69241 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8688c3f3-250f-3e04-a572-a52c69b0c907 | -10.42633 | -50.72958 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 654816b1-86e1-39ab-8c04-d69d57d3bc5c | -10.42573 | -50.69756 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 222.1 |
| d9942890-f717-327f-b72e-7905f6582d23 | -10.42504 | -50.70277 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 13366639-71ef-35bc-a87f-0bde635bde1b | -10.4235 | -50.78712 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae56cebf-74af-369a-9c35-14a77578aa66 | -10.42296 | -50.71844 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| fc93c8c9-1f88-3c43-9b05-8e5b0589a450 | -10.42227 | -50.72365 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 21d27ec0-b820-390e-8049-548490164dae | -10.42163 | -50.69181 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 73406a46-37f6-30ed-9a88-199881fbb13f | -10.42158 | -50.72885 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e6a744b3-1324-30fe-9684-0ac066174f6e | -10.42095 | -50.69692 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 729f425d-08b6-3af6-97f8-66e475a7bdb1 | -10.42027 | -50.70209 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15c87611-e51a-3c87-be7a-73eace774dfd | -10.41958 | -50.7073 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8040e88-f7ad-3d91-a00b-d971a0c93299 | -10.41889 | -50.71252 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d25d2b1-2bd6-3867-8eaa-0b2b0dd133be | -10.4182 | -50.71772 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 4e813332-7723-3bfd-9849-1e794fe221f4 | -10.41751 | -50.72293 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 1333e923-8e20-3de7-aa51-6b0bd29e7430 | -10.41618 | -50.69624 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 839c3ce5-888f-351c-9b44-7191b622c2c1 | -10.4155 | -50.70144 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98a51458-3718-3850-8c15-5f7d886b22f8 | -10.41481 | -50.70663 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92130b70-6c72-3008-a025-49e8c6cf7bca | -10.41413 | -50.71183 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3da94453-1536-3060-b3cc-8516c887b2de | -10.40936 | -50.7112 | 2024-10-06 05:12:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26c450c1-2571-3de3-b490-e06a1927895a | -9.74901 | -50.64643 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c8283d0-3363-3f6e-afac-e7fc7f3fc71b | -9.74833 | -50.65156 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 011803d8-4426-3975-b632-6d095885348d | -9.74359 | -50.65091 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 253f1e85-e9e2-3ba2-8831-911069bd5bc8 | -9.74261 | -50.64954 | 2024-10-06 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 73edd218-1dd9-3b91-9631-cbde5b87d5fe | -9.64572 | -51.78714 | 2024-10-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5ba2cd3-d1ff-36db-9d8c-d19fa41f9e85 | -9.64195 | -51.78216 | 2024-10-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3455b4d9-c93f-34b5-990e-b546d96c12e8 | -9.63817 | -51.77718 | 2024-10-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7e7f6ca-ac13-35cd-b072-84bde917949b | -9.63758 | -51.78143 | 2024-10-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bff6482f-14f2-33f3-834b-473d13692d64 | -11.24387 | -51.19259 | 2024-10-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 520f1ebb-f535-3fea-8a61-dc07544b3bab | -11.23927 | -51.26238 | 2024-10-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 987fea46-a688-335c-8f28-671deb84c26f | -11.23921 | -51.19189 | 2024-10-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3587959-21a8-38e8-acc5-313b0466772a | -13.25104 | -51.26847 | 2024-10-06 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9532f050-1f4c-32fd-9174-a8fecfcaec24 | -13.25037 | -51.27376 | 2024-10-06 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50523be5-23ba-34c9-86bd-31ab4e2de731 | -9.09125 | -53.29978 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb54bd50-5aab-3faa-8b17-306a33a8ef5d | -9.08058 | -53.262 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 37d0e77a-c6e1-3bde-a585-8196806990d3 | -9.07665 | -53.26143 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10a6d450-8a0f-3b65-b4a1-f65e3598fc50 | -8.96023 | -52.78834 | 2024-10-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db71d7bd-7976-3896-b54d-358abd632126 | -8.66097 | -53.08404 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ca80e6d-ee0f-3184-9fc3-ab3126b71fee | -8.55057 | -51.77596 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba18efaf-986a-3b24-8d4f-c25a7a26789d | -8.54566 | -51.77966 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ccb3501-bf82-31c4-a28e-bfbcccf96f66 | -8.32804 | -51.72949 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29650985-cfec-3ff0-bb8e-cdfc058fd616 | -8.95617 | -52.78784 | 2024-10-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8c21cd46-63f9-3689-8eec-553a6009b5d8 | -8.63614 | -53.17414 | 2024-10-06 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b976b67-9b97-34ba-915c-5579fce6301a | -8.54999 | -51.78006 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8b6eb54-f63d-32a7-9b1b-fa7b81252cfc | -8.33235 | -51.73011 | 2024-10-06 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 114589bf-28d0-3156-81b3-09caf634c816 | -9.75624 | -53.15997 | 2024-10-06 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f15488f-f5c0-3fef-b0a4-0a0aeab83a4c | -9.7328 | -53.18165 | 2024-10-06 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a517306-2eea-33ef-9aa8-a5799ada04ee | -9.73231 | -53.18515 | 2024-10-06 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61d8a08d-325b-38fd-b59b-0570b04969da | -9.7288 | -53.18109 | 2024-10-06 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c23b9c4-03fe-3c92-87a8-8d18a43d0dfa | -10.92784 | -52.40552 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4561ed8-5407-3d7f-8ec5-c0c1dbc84d3f | -10.9127 | -52.45323 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27f390c5-cb08-3877-a412-099a641447ed | -10.909 | -52.44846 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 773ee7f7-1480-3f2e-8de5-438a79c52448 | -10.90549 | -52.37709 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b17c86f3-0f0a-3053-bbb0-25068e65fc66 | -10.90494 | -52.38123 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7833c859-3489-345e-8ca5-0bb59b99ff08 | -10.90438 | -52.38536 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b61bd1fe-b3a0-3062-a9e3-20415fcb839b | -10.90384 | -52.38946 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05367e47-2a87-3960-83b6-953d6c6b569e | -10.90282 | -52.37348 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e1a67cb2-a0ab-38a6-af67-b51415ec0095 | -10.90224 | -52.37763 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 995b6fd7-1967-3bec-9dc4-867be4d934ae | -10.90165 | -52.38177 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 128f6cfe-2570-3cd5-aaab-e04e31f84d6c | -10.9012 | -52.37648 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 55954a36-24c8-3b92-8d82-c62e9683c359 | -10.90108 | -52.38587 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6da7b51-036d-3110-8c05-1491b03a06f2 | -10.90065 | -52.38063 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ab382a0-fc4b-35b4-8b6b-aee8459c09fc | -10.90011 | -52.38473 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7072e69-cf2f-3725-9e4a-c6ac8486d27c | -10.89795 | -52.37703 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 546b7b09-e342-3949-b373-950b8ce85b1e | -10.89738 | -52.38116 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54a4c7aa-37d9-3ed5-a718-a2aa6b6c0df9 | -10.89734 | -52.4382 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2b5d411-db56-3a70-830f-44b3cff9ea36 | -10.89692 | -52.37586 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f8dad556-016e-35fb-b3fc-79afb2045273 | -10.8968 | -52.38523 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b911f361-4135-390c-93b9-3adc11ab21ea | -10.89637 | -52.38001 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9b6e772e-916e-35c2-9282-f759477ba125 | -10.89583 | -52.38409 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63517420-e4ab-3fab-8b14-f23fddbe8c36 | -10.89253 | -52.38459 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64c37f3f-86ce-37aa-94c1-c764082ac18a | -10.89155 | -52.38343 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6ff6cb0-4557-3bbe-8505-38d489f45c78 | -10.88883 | -52.37983 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1351624-f5dd-374a-b93e-a1e7c78645b6 | -10.88826 | -52.38394 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ca77e25-7ef2-3d73-9243-9489518da1b9 | -10.88455 | -52.37923 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68a4cdd6-754d-3a6f-a507-7f771e4fae8f | -10.8834 | -52.38749 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5290c626-6840-34a9-9a25-5be485ec6889 | -10.88282 | -52.39161 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0af3c240-5c28-3918-88ea-3a07d6753b06 | -10.88225 | -52.39571 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af565fb9-7fdc-3062-869b-d99f6c6f405e | -10.88168 | -52.39977 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfffd41e-6c7f-32a3-bb77-9a787b4dedb2 | -10.87686 | -52.40314 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1dcf7da1-305d-3813-bc78-a42588266a0d | -10.76807 | -52.4715 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bfdbc1af-14c3-3c97-80f8-f542c76a51c3 | -10.76382 | -52.47095 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 92dfca23-4af3-3d41-8ec3-22b47aa9cefa | -10.76326 | -52.47498 | 2024-10-06 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README105.md)
