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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76bb1a3f-7651-3cc9-868a-dc5022c16bf5 | -17.58504 | -57.55499 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2454ef04-7907-3e41-8ca3-9756ae6b435c | -17.59071 | -57.49023 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2e6848ad-9941-3aa3-b8f9-a1e8dcae3f2f | -17.62503 | -57.54899 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c39bdf75-8b42-3619-a8c6-50a3ca07681b | -15.62416 | -57.51628 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3054b777-4bb0-31f0-920d-f5cec294be53 | -17.57709 | -57.52619 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fd19886c-aaf8-3320-ba27-2527fb678682 | -17.6907 | -57.48943 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 77ba5c69-746b-3469-95f2-b33ebb9f545f | -17.23566 | -57.46776 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| cf996631-fe9f-33b2-9193-ef73195a27f4 | -17.22806 | -57.19809 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6e85fa6c-6194-3e41-9b7e-f70fa8249d9a | -17.59706 | -57.47063 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| cba8f2ac-688d-35b3-9b02-aeb6463fa4e2 | -17.59067 | -57.40887 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 01f4216e-fdff-32de-9083-4c10efd79569 | -17.58704 | -57.48259 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 893bb374-e109-3838-a413-49b276942e88 | -17.75085 | -57.52691 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 415c1a68-a442-3584-8025-6a7b733a8763 | -15.90804 | -59.27624 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11c2a882-0180-3571-890b-6347e5040efb | -17.04854 | -57.43615 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 87d50026-816b-3306-b758-5e7798b5749c | -17.58224 | -57.56383 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 516f43b7-f096-32e8-a489-ea9290e9ff6e | -17.58275 | -57.57098 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 81cf6c2b-2052-35ea-8b14-042bd2174f1b | -17.57662 | -57.45626 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0c0d6448-e80c-36a7-9214-3f2310a48f49 | -17.65116 | -57.44195 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 63ee000d-9085-3920-9fd9-430d1672484f | -17.67319 | -57.53606 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7c495062-4bb1-355c-ba4e-78e893550d76 | -17.58327 | -57.54242 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bc1fa0cd-0f3c-308d-b20a-b0dcff88bba4 | -17.72584 | -57.50239 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b792dc70-790d-3f1f-b6ea-24387b31656c | -17.58297 | -57.48606 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 74711fdd-c48d-3ff4-9cfa-f0336f02c11e | -17.69278 | -57.53424 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6446d083-39cd-3b3b-9210-1d5114836246 | -16.07158 | -59.70652 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29fb08e4-9eca-3ba7-b52b-c8458745452d | -17.26348 | -57.47211 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 6e6a5425-d408-391f-9b5f-b8258031cc7c | -17.57302 | -57.52965 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 768f773c-3177-31ee-90d6-18f6f8c8bde2 | -16.95502 | -57.63963 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c4d904ce-91aa-3338-8d17-900c5e3114c2 | -16.94869 | -57.63462 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 0816e2d4-b913-36db-be71-625ab22cefdf | -17.59085 | -57.56408 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| f16bc048-48ef-31a5-afa1-5599fa39461a | -15.31232 | -56.521 | 2024-11-15 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39c91d63-67e5-3b9d-a730-bdf8667d03ad | -17.61045 | -57.47685 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 807f43db-a60d-3aa7-a632-0e95cbe78bae | -17.69419 | -57.48997 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7514f68f-44de-374c-84a6-90b9492d4426 | -17.23683 | -57.45976 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.1 |
| fe9e17de-7f3d-3e99-bee0-2a33c076ffb8 | -16.02043 | -59.38298 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b9da1f1-9e77-3a4c-8c29-b2a3912ddae4 | -17.70786 | -57.52839 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1eb3c111-35c2-32c4-a58c-c187c48ce000 | -17.58106 | -57.57182 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| b303c8de-4c95-36d7-9a95-1864c9a34b3d | -17.59112 | -57.47911 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| b55fcd05-4794-3682-8860-fed5b1ade400 | -17.69922 | -57.56398 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 63f9770a-aa15-3193-a5bb-79164f1b3120 | -17.28731 | -57.51595 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4b21fd3f-8de1-3194-b8c5-61fbba2ce63b | -17.84214 | -57.39494 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 81c94167-a6f9-34d8-a9a7-d36d333a99af | -15.31172 | -56.52514 | 2024-11-15 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90cc84a4-f4ed-3214-94db-52eff0f95eb4 | -17.64011 | -57.54316 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| 34a0742d-e205-3d10-abdf-947290ae11bc | -17.58333 | -57.56699 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| dcf29edb-2f50-3c72-9dd1-1565a98d86a8 | -17.58069 | -57.45278 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bed2e40d-a5cb-3633-8fba-f6268e2eed0c | -15.23044 | -60.22806 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ad1ae79-3aa4-367f-9711-cd186f0d4608 | -17.24378 | -57.46085 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| e1eff70e-2476-3761-be50-25573855b5b1 | -15.47702 | -60.04763 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95683e39-54a4-3f5f-a6b7-3771fbdde07f | -18.64087 | -57.3322 | 2024-11-15 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7a6ed612-bb78-3470-be34-9b19fc9a9677 | -17.23797 | -57.47629 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0bc2b7f4-bd54-378f-bbe5-1a5c03c94b81 | -17.58532 | -57.46998 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8edc01e0-295e-3a01-b05c-ff2ab2b0f8f2 | -16.94066 | -57.64137 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 38b9bf3a-c3ee-33f0-abb4-ec8d10835d23 | -17.71135 | -57.52894 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3aac0733-3511-3be4-848b-7c2eaf495d29 | -17.56548 | -57.53257 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 2d3b2e7a-389f-394d-b8a0-6b0018443b5f | -17.63083 | -57.55809 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 408ee44e-9347-3c3e-af6b-bf1969a95b3b | -16.02095 | -59.40138 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a13e0035-00f2-3249-adc3-c5c437324321 | -17.61344 | -57.55536 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 699eeeb4-863b-36e5-8836-a683c0e48fac | -17.71486 | -57.55415 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5331b6b6-e2cb-3270-91b7-6cb2bd54a4ea | -16.94468 | -57.638 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| af1cfe1e-75c7-3864-93f8-b6a9671baf55 | -17.80235 | -57.31894 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8b7077b6-77b7-395b-a344-24d7642131f5 | -17.26813 | -57.4762 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2d60c62e-4d6a-3409-bb20-f6fbf551e710 | -15.62816 | -57.51297 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58a1b306-9cc3-3fee-9f84-25363745f8a2 | -15.31587 | -56.52154 | 2024-11-15 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0ed8708d-78e7-31e4-87a5-4c37cf23fe68 | -17.60347 | -57.47575 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 133737b8-abf1-3d70-8a77-3e8322084bb2 | -17.58763 | -57.47857 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 3244adba-591a-3aee-9522-5818b619a164 | -17.56083 | -57.54003 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 289a0efa-254a-3564-945c-c89e986184d2 | -17.58368 | -57.40778 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e9bd5319-0895-3085-9988-168dcbe40307 | -17.58795 | -57.55954 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 24ddb307-a113-3741-a91d-982992ca159c | -17.58305 | -57.43663 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0131fa5d-1348-32e2-8b2a-f6f263e33f86 | -16.01712 | -59.38242 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0a74a24-b50e-3db7-9285-7c463d463aea | -17.57705 | -57.55075 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 195d55ce-3289-3b91-8878-ec7103bf435e | -17.29511 | -57.3117 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 48916a91-7161-3793-80fc-fb643f8915a2 | -17.62735 | -57.55754 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 22293200-070a-3072-b192-721b74da8f12 | -17.5865 | -57.46194 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8ba70b46-bb32-34bf-a077-aa44ddb91e34 | -17.57353 | -57.57472 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f70a6e4c-c2ce-3a67-9452-9c3f6bbdcba6 | -15.29632 | -56.53121 | 2024-11-15 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e055a2be-c16c-3e72-bcec-5c8c3430cc7f | -17.2629 | -57.47611 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 5f22a5dc-71c4-3761-b0dc-6e1be9185bb1 | -15.41266 | -58.61753 | 2024-11-15 05:12:00 | NOAA-20 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53cacc88-c4dc-366b-bf21-7ecac05ae220 | -17.18109 | -57.29594 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 02d3d9bb-b63b-392c-ac38-d294c506ad80 | -17.58048 | -57.5758 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 9c7f7652-1e9d-36da-8642-cb971039cacf | -17.24843 | -57.4534 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 5cc30e45-53a7-3bcb-ace1-d473ec7cfd12 | -17.57985 | -57.56644 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 4a2b7f0a-3c77-390a-9c95-45cf1f9e0f45 | -17.592 | -57.55608 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3e4cddee-b182-3a0b-a0ec-8f7a78cf171e | -17.58426 | -57.40374 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 731ac8f1-3711-3940-9d32-9e174ede9084 | -16.95157 | -57.63908 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 3a8b6b26-a15e-33f1-9533-0e8fcb64a4ec | -17.25364 | -57.46649 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 6dee9b62-e666-3353-9b89-ab151595ef9b | -17.25653 | -57.47102 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 11778a10-71ef-352a-8978-866d86b061a5 | -17.66216 | -57.53843 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 28ef1888-1a53-396a-bef1-149b004ba43b | -17.59107 | -57.50376 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4c388743-d070-3a09-9842-d8c8b7d0ae84 | -15.8948 | -59.27404 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bc35841-154d-3b00-b6b3-5c33498d630b | -17.58356 | -57.48204 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 046b5c50-ce9e-30be-940d-a8b18d87ad69 | -16.95445 | -57.64355 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1d76233d-49fe-34e8-ade8-f6feef89c9d6 | -17.62677 | -57.56155 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 75d0a438-646f-3d90-ae12-a5f6464664e1 | -17.58618 | -57.54698 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2fa81296-cac8-3e09-82ea-bf640351af2c | -17.64242 | -57.45298 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bc820896-932e-3d37-a032-8d5f9eaf4204 | -17.70732 | -57.55706 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 84d414dc-618a-392e-8738-883679007e8a | -17.69821 | -57.5112 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 75ea8f90-7d27-3520-93a0-793b9dcd3c90 | -15.42446 | -60.27245 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62c06abd-79d6-33eb-b3ff-3c593cbf3b9a | -17.58099 | -57.55843 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 69615751-fbf2-3678-b214-48b1f5324c86 | -17.23624 | -57.46376 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.1 |
| f8fa1e5c-67ca-317c-9016-cd10cbd94806 | -17.57123 | -57.56618 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |


[Clique aqui para ver as próximas entradas](README32.md)
