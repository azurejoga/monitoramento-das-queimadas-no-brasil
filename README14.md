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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc270e2c-a37c-3313-88ce-586beb8439cb | -11.0237 | -52.501801 | 2024-10-04 00:43:34 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 469a6cf4-a421-3e88-be1f-5b9a01b5fed0 | -11.8882 | -56.9328 | 2024-10-04 00:43:34 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c63f152c-7ea8-3955-a2e1-0ded4ebb4231 | -11.8129 | -56.592999 | 2024-10-04 00:43:35 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd4a1ac-41f4-3693-81df-6d3bea9ee616 | -11.7987 | -56.571201 | 2024-10-04 00:43:35 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ceffa167-606a-39df-b0a7-12a562d01717 | -11.8033 | -56.594799 | 2024-10-04 00:43:35 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21acdaf5-5f8c-3f7f-aae6-8b45ad1b7c96 | -9.9019 | -47.698101 | 2024-10-04 00:43:35 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2594363-7f3d-336f-bbd9-aa2d64cfff00 | -10.9011 | -52.402 | 2024-10-04 00:43:36 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd4ca394-8bb7-32ef-b94c-4423574eb001 | -10.9036 | -52.413898 | 2024-10-04 00:43:36 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 414bf67f-84c2-314b-a8f0-90f26f5c2ade | -10.906 | -52.4259 | 2024-10-04 00:43:36 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be976e0f-aac7-3596-8293-cc8c9b96dee9 | -10.8963 | -52.428001 | 2024-10-04 00:43:36 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4567983d-1fc0-3942-b793-17e4c2ae0a63 | -10.1129 | -48.829399 | 2024-10-04 00:43:36 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8b2c581-de62-39d9-ad12-5cab7f629149 | -10.5468 | -50.9664 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac28999c-e07f-382c-9090-789b1d42b2ae | -10.5489 | -50.976002 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 47fcf867-bcf6-3eee-b937-a877e54ed8f4 | -10.535 | -50.9589 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| afd773cb-af93-3ee9-b0e7-2ca8cef5125c | -10.537 | -50.968498 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa688bfa-f51b-3270-a8a4-e8aff1a7704a | -10.5391 | -50.9781 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 220c6b5f-aab2-367d-b727-8a189c6a0aba | -10.4532 | -50.720402 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf0bea15-8148-30ff-950f-f59ba5af89ae | -10.4552 | -50.729698 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b846dc9-a825-3ee4-9822-acd59e6f0ae2 | -10.4572 | -50.738998 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77d71e5e-b301-357c-ad3d-37d7b3ecb24b | -10.4434 | -50.7225 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf57a966-b4e2-3e0e-b00b-d0b3fe539aff | -10.4454 | -50.7318 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50d0874c-09dc-3b20-89eb-9a99046c6bca | -10.4474 | -50.7411 | 2024-10-04 00:43:37 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df26bdd4-0ad3-3d86-9d2f-2d1ea3f2bdc6 | -10.4336 | -50.724602 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b0698ee-7060-36b8-9a3f-c3e7b6d89783 | -10.4356 | -50.733898 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8e7279b-a721-3277-9477-918cc3061dbd | -10.4376 | -50.743198 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a5960efc-9b5e-37ec-a7ee-445fd1c9f6b2 | -10.4396 | -50.752499 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb1daa20-9635-3011-8780-250563711160 | -10.4338 | -50.773201 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5000dc01-db9e-3617-a84f-a6907fb6fd25 | -10.4358 | -50.782501 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| baa0634c-e7e4-35eb-b994-a86cafdd1992 | -10.426 | -50.784599 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51c19da1-cbcf-3114-84d8-ed091241c3d0 | -10.428 | -50.7939 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21ae79aa-0828-3137-aa80-a870f6b58703 | -10.4163 | -50.786701 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5b86081-f764-3d1f-b977-47f12c4d5320 | -10.4183 | -50.796001 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a766609b-1547-372f-a41c-7a894b806ccd | -10.4203 | -50.805401 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a39ebcab-85ff-3fcc-9699-53b334004717 | -10.4223 | -50.8148 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea6a371f-c6d3-3e55-894b-322beb3198ec | -10.4105 | -50.807499 | 2024-10-04 00:43:38 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 920da79c-3f61-32c1-805f-56b94e6ec5ab | -9.3355 | -46.563999 | 2024-10-04 00:43:40 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba5186d-7e24-3506-bde8-4088b613b6c4 | -9.3371 | -46.570999 | 2024-10-04 00:43:40 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7957cd00-476b-37ee-9198-6751ed254899 | -9.3257 | -46.5662 | 2024-10-04 00:43:41 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1131d36e-48c3-345b-b7b7-40fb02019f2c | -9.9776 | -49.4743 | 2024-10-04 00:43:41 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b988a18-46ce-36bc-8a92-ea6693d7f40a | -9.9793 | -49.4823 | 2024-10-04 00:43:41 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cee3169-4515-3aa7-b140-cf7dff06ab7b | -9.7011 | -48.826199 | 2024-10-04 00:43:43 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71ac42f9-113b-36bb-a3e8-07c500ee8799 | -8.3153 | -42.831402 | 2024-10-04 00:43:43 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0a1fc0f2-d29f-354d-9aa9-0e6da320601d | -8.3032 | -42.8242 | 2024-10-04 00:43:43 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f00038d-41df-3871-9076-bf8eef9aa98c | -8.6813 | -45.250301 | 2024-10-04 00:43:46 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1bc69d3-856e-3396-a35e-9ada4bd44937 | -8.683 | -45.257702 | 2024-10-04 00:43:46 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e47b00cc-1d54-3a90-9be9-1a47582c0adb | -8.6715 | -45.252499 | 2024-10-04 00:43:46 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 88bb67d6-4842-39f0-923c-ea55bb007db7 | -8.6732 | -45.259899 | 2024-10-04 00:43:46 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 198fe56d-8c71-37d8-a06b-dee6eb4768b5 | -9.7624 | -50.085701 | 2024-10-04 00:43:46 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05e955e8-a6a4-360d-b93d-44bf82f6f937 | -9.3133 | -48.194302 | 2024-10-04 00:43:47 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36b5e098-351a-3dbf-a987-8d4708f716e6 | -9.3149 | -48.201401 | 2024-10-04 00:43:47 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee0b1313-2b1b-30c0-b12b-215379667cfe | -9.3035 | -48.196499 | 2024-10-04 00:43:47 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53465eb0-41ef-3110-a849-5eb5db855fb6 | -9.3051 | -48.203602 | 2024-10-04 00:43:47 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa82fffa-5abb-3272-b71f-5faef9d42764 | -10.2355 | -52.729301 | 2024-10-04 00:43:48 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a2b0608-9de3-3e4b-8ed4-70b1813b17b1 | -10.2257 | -52.7313 | 2024-10-04 00:43:48 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9dfeb06-d96f-3ae8-b9be-2d0cbefa65e8 | -9.6234 | -50.107101 | 2024-10-04 00:43:49 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6d3b03b-7cb9-3741-9714-b581cec4506a | -9.5886 | -50.088402 | 2024-10-04 00:43:49 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfc44fbf-9712-3319-9d3f-154baed19f6f | -9.5837 | -50.159901 | 2024-10-04 00:43:49 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc72d093-2be4-3d15-8318-fa1b15f64364 | -9.5855 | -50.168301 | 2024-10-04 00:43:49 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73cb35bf-282d-37b6-ab7e-236ff82421b8 | -9.3059 | -48.944901 | 2024-10-04 00:43:50 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b33aae1-f73f-3171-851e-a19ca158dfe5 | -9.3076 | -48.9524 | 2024-10-04 00:43:50 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75e2c899-e1ce-328a-b04c-bd34d7dd093f | -9.5776 | -50.178902 | 2024-10-04 00:43:50 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6c973ef-4940-37c9-b64a-a2eb76ef43e8 | -9.5654 | -50.216999 | 2024-10-04 00:43:50 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 445493fe-4012-351d-91a6-34cf1fb20d88 | -9.5672 | -50.225498 | 2024-10-04 00:43:50 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecc712ef-519a-3055-9d05-8fdd0dafb9f9 | -9.5556 | -50.219101 | 2024-10-04 00:43:50 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc98ffcf-3d2e-3c30-a4c8-05daf0c3eb85 | -9.5574 | -50.2276 | 2024-10-04 00:43:50 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98e388aa-3847-351f-a35f-9bed46f2874c | -8.7517 | -46.8064 | 2024-10-04 00:43:51 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d89b3542-62fa-38d9-8216-dd280ab23ccb | -7.6301 | -42.428299 | 2024-10-04 00:43:52 | METOP-C | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86fc2da7-a8e6-3b05-a8ae-d73ff4a0ddf9 | -8.5938 | -46.521999 | 2024-10-04 00:43:52 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e351c159-778a-38a4-8d6a-a76e831a40d2 | -8.5825 | -46.517399 | 2024-10-04 00:43:52 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8f69ccd-00ab-3ead-8219-c0d30252834c | -9.136 | -48.9669 | 2024-10-04 00:43:52 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb635a7c-5148-3dfb-9171-c4a409076ef7 | -8.6231 | -46.515301 | 2024-10-04 00:43:52 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42d108fb-c17d-3656-a3a8-48636cfc18ca | -8.5907 | -46.508099 | 2024-10-04 00:43:52 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12285cfd-9156-3103-843c-bddd13a10f52 | -8.5923 | -46.515099 | 2024-10-04 00:43:52 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e78236c-6910-3eb6-a423-96650c9a04c0 | -7.7501 | -43.057098 | 2024-10-04 00:43:53 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2eb471b9-c677-3007-a2e5-16b15cfba945 | -7.6905 | -42.980801 | 2024-10-04 00:43:53 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7df28933-e390-3c90-a543-f07af1d80633 | -7.6928 | -42.990398 | 2024-10-04 00:43:53 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b157effc-6ffe-35ae-918e-b1cc190e8ecf | -8.1167 | -44.778 | 2024-10-04 00:43:53 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4e79a1de-9c3b-3f48-b3ca-c8799cd8e5ab | -8.1185 | -44.785702 | 2024-10-04 00:43:53 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3d233c79-2e79-37a8-8a54-b408421fd60d | -8.1204 | -44.793499 | 2024-10-04 00:43:53 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37c83bc8-9751-3513-a78f-bebcd68a985e | -8.1106 | -44.795799 | 2024-10-04 00:43:54 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c089a5be-121a-3905-ac1b-106f3579527f | -7.6808 | -42.9832 | 2024-10-04 00:43:54 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f8ce917-215c-345f-b395-726d3cf3f79a | -7.6831 | -42.992802 | 2024-10-04 00:43:54 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1af30a94-405b-3e69-832e-0fce8842e1a7 | -8.1069 | -44.7803 | 2024-10-04 00:43:54 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a3e0d3f-71ed-3714-bad1-ac31f6c849fb | -8.1087 | -44.787998 | 2024-10-04 00:43:54 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1871012f-4e07-3352-a949-04981443926c | -9.5877 | -51.456799 | 2024-10-04 00:43:54 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 488c51ff-cec2-33ac-864b-42954d6f017c | -8.4072 | -46.293499 | 2024-10-04 00:43:54 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 030bce19-9890-36d4-864b-4a94a6774619 | -8.4088 | -46.300499 | 2024-10-04 00:43:54 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dde2e7f-2a84-3efc-a605-203e882b7db7 | -8.399 | -46.3027 | 2024-10-04 00:43:55 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4056926a-f4c1-3d72-8f2a-60c897aef214 | -8.4006 | -46.3097 | 2024-10-04 00:43:55 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c58cbd9c-172a-3a4a-922b-e004b3c32841 | -8.4213 | -46.444401 | 2024-10-04 00:43:55 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f9889ac-f541-3324-a6c2-f27bb8bdc7cb | -9.3624 | -50.7453 | 2024-10-04 00:43:55 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 793ae5e4-fa43-3253-9885-ad27493c1ba8 | -9.3643 | -50.7542 | 2024-10-04 00:43:55 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d1abddf-0ef5-3f69-b64b-b8b092dcb372 | -8.5321 | -47.153702 | 2024-10-04 00:43:56 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc7bc7ae-8d4b-3f4d-8f8f-7c32a831f372 | -8.5336 | -47.160599 | 2024-10-04 00:43:56 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a20390b2-745a-3e2c-a056-0c394af257f3 | -9.3193 | -50.7827 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97010e4e-17b1-33a0-b495-d22ec57dd2fe | -9.3076 | -50.775902 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf1acf32-07d7-32e2-a130-96cf3fd72732 | -9.3095 | -50.784901 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0e4808a-5c23-363d-9389-2b2f873c574c | -9.3115 | -50.7939 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddd5db6c-2413-396a-a526-c704b3185b4e | -9.3135 | -50.803001 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0cff789-8550-336a-baa7-ba907555bcff | -9.3154 | -50.812 | 2024-10-04 00:43:56 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
