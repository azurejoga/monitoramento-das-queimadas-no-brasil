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

## Dados Diários - Página 258

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61d9b4da-78a3-3292-9cf8-6a5ca64c1a38 | -3.2136 | -42.9764 | 2026-10-07 19:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| dba610f2-3ce4-3e33-8ec6-74ebea645371 | -5.3695 | -44.4734 | 2026-10-07 19:20:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 74900ddc-0357-3737-8efa-917ca926fd2b | -3.8786 | -44.1265 | 2026-10-07 19:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 9efc547e-10da-330c-af73-1d66df2c06aa | -3.1697 | -58.6437 | 2026-10-07 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 6359dc69-0322-3e71-b2c7-a397f7ca58e2 | -3.2949 | -53.8798 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ab896859-2f6b-3474-9b19-575ab3228b01 | -6.1615 | -52.6676 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 3cd0add9-bf1a-3bab-9ce8-394e2e8b5731 | -6.1298 | -51.9281 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| d6656a99-fc0f-30b4-8baf-9187b499bba0 | -1.4771 | -53.6134 | 2026-10-07 19:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 95b5c557-82a5-33a9-9dd4-404cd1af3f1a | -5.8773 | -53.6202 | 2026-10-07 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ec603fa2-2f53-37dd-bab7-58da8326f207 | -6.8952 | -43.6833 | 2026-10-07 19:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 274.3 |
| 4d51f6cd-69c7-31ae-83fc-440252aecf95 | 1.3346 | -50.8503 | 2026-10-07 19:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e45d2367-bde3-39df-8cb5-5ba2e78e615a | -8.629 | -67.0667 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 8359661d-c9b1-3b41-8841-63eee9823bd0 | -5.2275 | -48.3897 | 2026-10-07 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2809ea64-80e8-30b3-83f4-a77d2c5828f0 | -10.7863 | -46.5686 | 2026-10-07 19:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 955bc6b7-f7ab-32cd-994e-5dcdeb0d45fe | -3.5875 | -54.3138 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 30eb2877-a106-32f3-80e8-b926e3b816f2 | -5.4835 | -44.2592 | 2026-10-07 19:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 250.7 |
| 58c681d2-ddc1-305e-ae05-e30b1231780c | -5.8205 | -53.8255 | 2026-10-07 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 099a6359-bbe6-3707-a604-1cf332248c16 | -3.8152 | -45.4019 | 2026-10-07 19:20:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 084dfa3b-a72c-3802-8d22-489989ffa17c | -11.6374 | -43.664 | 2026-10-07 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 5df64238-9c64-30c7-9ccf-d5a379586701 | 1.6937 | -55.6461 | 2026-10-07 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 74a23df0-7496-3d0d-bf86-04c791ada07a | -10.9953 | -45.4068 | 2026-10-07 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 293fc998-e6da-31a5-8eb2-def54544ba8e | -3.7481 | -51.2079 | 2026-10-07 19:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 5fbc00a7-78b5-3165-8c11-96503f8e84a7 | -6.6784 | -52.9664 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| fb0ab965-08a4-357a-9eec-12990d2eda1a | -4.3044 | -50.7909 | 2026-10-07 19:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 597da59d-2552-3588-ac5b-8b6632052acd | 1.3346 | -50.8711 | 2026-10-07 19:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7be0df51-949f-3cb5-9056-fb348497b693 | -3.3637 | -50.4701 | 2026-10-07 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 224.0 |
| 53c0e0a2-ebdb-3c13-97f0-4c728ee9711a | -9.9601 | -45.9712 | 2026-10-07 19:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 150.3 |
| b0bc6c93-4949-3848-9583-3a3e8d945e65 | -9.9596 | -43.5045 | 2026-10-07 19:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 85885556-d9eb-3c12-b4b4-5e7fd84fc169 | -4.3045 | -50.77 | 2026-10-07 19:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| c74d8bae-53e9-3f9a-9f56-7e3d0bab5f79 | -3.195 | -42.9772 | 2026-10-07 19:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 7d628ef5-366f-3516-8dae-47653a8ea587 | -3.8037 | -47.4839 | 2026-10-07 19:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| f9b904b2-ed04-3044-83e8-aa92b37bc17c | -3.5876 | -54.2937 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d3cb07f1-d1a5-38b4-b1ca-ef569e192eba | 1.7121 | -55.6063 | 2026-10-07 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| c5154637-b63f-3be6-ae4a-c80bfa61e302 | -5.4771 | -42.8427 | 2026-10-07 19:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 142.3 |
| 20b905a6-112f-3d62-9f41-da47c4c38b77 | -3.4763 | -50.0673 | 2026-10-07 19:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 90afb642-0962-38ba-b868-f391758ccb76 | -3.6786 | -54.5115 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 3fb84b10-fcc8-332f-825f-8adb8857c82a | -5.6748 | -53.4879 | 2026-10-07 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| ea5d0d8a-09ee-3be3-b48a-a166eaeb2cb6 | -8.9082 | -49.986 | 2026-10-07 19:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 04e5c5aa-4903-32fa-8721-4d3126eafd85 | -1.8011 | -57.0967 | 2026-10-07 19:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 482e0d09-3366-343b-a998-3af920896646 | -9.0591 | -65.9396 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 149.6 |
| c3346957-02f6-3a72-9b04-4236684d8cde | -8.5366 | -67.069 | 2026-10-07 19:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 7482de2b-92ed-3a79-a1e6-0d08db4a2d07 | -2.6859 | -49.0325 | 2026-10-07 19:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e186dd97-f08f-31fa-98bc-a2515f65f1cb | -7.6583 | -72.3144 | 2026-10-07 19:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 8c623697-3580-3cdf-8a9d-53c863151db0 | -6.1617 | -52.6471 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| cdf1161a-0c5d-3dd1-9c28-4c205a913b60 | -11.6369 | -43.6876 | 2026-10-07 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 32adf588-104a-3710-802b-d91dde2700cb | -3.1101 | -54.1661 | 2026-10-07 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 612.3 |
| cb57ad75-b09b-340a-9c7e-6061077ee59d | -13.4141 | -42.5728 | 2026-10-07 19:20:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 87.9 |
| ba06a309-320b-319b-ba4f-ef8111f51bd2 | -5.2473 | -50.9149 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 98342a4b-0012-3ddf-b33f-cf6e315166e1 | -5.9647 | -40.9383 | 2026-10-07 19:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 184.0 |
| 35bbe1c4-5339-3c3a-b57b-a4a9b6772f80 | -10.9938 | -45.4985 | 2026-10-07 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 68a63701-e0a9-390e-9ac8-d253a542263c | -3.476 | -54.6172 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 0c9caf2d-aa09-35d2-8337-3af6c7010938 | -10.472 | -47.2556 | 2026-10-07 19:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 2d714ba9-dd13-34da-8ca4-23b7b61eb90e | -3.1973 | -50.5382 | 2026-10-07 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 4ec5534a-cf14-36ff-9a84-f6cac65040f5 | -5.9835 | -40.9367 | 2026-10-07 19:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 566c9cc7-7c5e-3989-984c-b3c33ba048ad | -5.9644 | -40.9627 | 2026-10-07 19:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 180.2 |
| c57605ac-5931-30db-b58a-4a5d4e30165c | -9.9787 | -43.502 | 2026-10-07 19:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 601540a7-dd06-3ec6-8ed6-76a0d61234fa | -3.3133 | -53.8793 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 93cf96fa-ba0e-3da5-8ce9-ffe80760e56b | -8.9958 | -45.9454 | 2026-10-07 19:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| eb37fb6c-e25e-32ac-af7a-0edd7bb03dd7 | -5.9649 | -40.914 | 2026-10-07 19:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| a4c7774d-5f83-361b-aabf-aeb0c4f23dd4 | -3.2137 | -42.953 | 2026-10-07 19:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 205.6 |
| e2f2de3d-7a17-33db-80eb-ddf529afb322 | -3.4944 | -54.6167 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 83963f8b-8c49-3d4c-9145-65d138c80cba | -10.4727 | -47.211 | 2026-10-07 19:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| a6645f7a-25dc-339f-b6bc-d6e450f603a4 | -6.6224 | -53.0105 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 1aaf925b-4f09-3b1e-9799-8861c650bfe1 | -6.02 | -51.7272 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 57c3ff89-f3d6-3296-b017-a8bbbcbc9fab | -3.4947 | -50.0877 | 2026-10-07 19:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 96cc3ba5-6a3e-3ec9-a478-36583e9fb9c5 | -5.8204 | -53.8457 | 2026-10-07 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| a8e05186-665c-3296-8fb4-5ebd854940cb | -3.295 | -53.8597 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| fcd53a1f-25a9-3d87-bc8e-765e536c64b2 | -4.2558 | -46.3855 | 2026-10-07 19:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 3856354c-7477-35ac-a17d-6908862a72e6 | -3.6612 | -54.2715 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 12feb91b-ef6d-3270-b922-f6e33ca91e8e | -3.73 | -55.486 | 2026-10-07 19:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 352de89c-531a-346c-bc82-98ee0cd560b4 | -6.895 | -43.7066 | 2026-10-07 19:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 931ec87d-1b56-30d6-9473-4528a666e30e | -6.2485 | -53.4592 | 2026-10-07 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5ba6f705-1898-34c5-a4fa-caf099a97053 | -3.5907 | -53.5081 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| cc78b8aa-93ec-39b5-9038-2d71ffbb97d3 | -3.3135 | -53.839 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| fe8b2557-88db-336d-b98c-20c81ae74055 | -7.3935 | -46.2144 | 2026-10-07 19:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 4c4190c0-fb6a-376b-9648-45831cfcfe26 | -6.8764 | -43.685 | 2026-10-07 19:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| b2719d88-6994-3ba6-872d-31d1785b9c70 | -3.8973 | -44.1255 | 2026-10-07 19:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| f3af98bf-f297-3226-8d5a-3ee7e337de01 | -1.562 | -47.7465 | 2026-10-07 19:20:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 245.0 |
| 64233b3a-79bb-3a43-b6a7-762447b16511 | -8.2181 | -46.362 | 2026-10-07 19:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| f167f43a-e88c-34b0-b599-647eef32ceec | -6.6037 | -53.0321 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| e65a91ae-2cdf-3b5f-8f6f-ad15570fa95d | -9.0592 | -65.9209 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 186.2 |
| 5067d8f2-dd5e-3d30-85d5-b7443048b443 | -6.6223 | -53.031 | 2026-10-07 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| de6ad6c7-5ea6-35b3-b082-0573b1b7c500 | -3.6931 | -40.8572 | 2026-10-07 19:20:00 | GOES-19 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 160.9 |
| 8344cf50-053c-3a12-be5b-62182ef22d68 | -4.777 | -55.7104 | 2026-10-07 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| f90ccce0-8624-33aa-8d19-eb29e7f60017 | -4.1574 | -44.2726 | 2026-10-07 19:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| efe067fb-e68c-35fd-854e-1c0f0152e0a3 | -6.1502 | -39.4158 | 2026-10-07 19:20:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 4634fa84-7320-3ca6-8a52-3daeaf3159df | -9.507 | -70.4439 | 2026-10-07 19:20:00 | GOES-19 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 954104b1-0cdc-3947-a2c9-c1d74c487615 | 1.6937 | -55.6263 | 2026-10-07 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9080befa-045c-3f60-b777-6489477c3a11 | -3.3452 | -50.4707 | 2026-10-07 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 6ab6f7dc-1c9f-3fb0-89bc-9f5d64e67b52 | -11.6181 | -43.6669 | 2026-10-07 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 99cafd9d-ef0d-33d8-862d-ba157dcde744 | -7.8789 | -72.3492 | 2026-10-07 19:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 478b20de-1368-3856-85a3-e3070c8eb64b | -5.9772 | -43.5057 | 2026-10-07 19:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 4878259c-20d5-3ad8-b013-f52c47fa438e | -9.8821 | -44.8402 | 2026-10-07 19:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 25cc80a5-2f50-3526-b68f-eae10440006a | -3.5684 | -54.4946 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| e40534f9-fa15-3ad0-9a5a-e9490ab304a7 | -3.7166 | -54.2096 | 2026-10-07 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 12fd1b68-600b-3b5e-8c9e-73456fe4a9f1 | -5.7378 | -45.1307 | 2026-10-07 19:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b3e8b0c0-6d86-3e07-a6e3-8b847d07f278 | -6.8292 | -39.5472 | 2026-10-07 19:20:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 024593ca-abe7-3d38-8a8d-55ee57e02965 | -3.2199 | -54.3038 | 2026-10-07 19:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 947b8e4c-96fe-3c44-989e-2de787745331 | -9.0407 | -65.9215 | 2026-10-07 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 691a4155-d0ab-3be9-8279-9d4b1ba169ad | -3.5865 | -54.5742 | 2026-10-07 19:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |


[Clique aqui para ver as próximas entradas](README259.md)
