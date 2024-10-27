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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7c09507-40f0-34bd-9336-536a89009f9d | -7.255 | -41.2173 | 2024-10-27 00:13:12 | METOP-B | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a830de5e-225c-30e4-93c5-dfbd81d35df3 | -7.2566 | -41.224602 | 2024-10-27 00:13:12 | METOP-B | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a6b72429-9f44-3d8e-8c60-b98f3f308378 | -7.2435 | -41.2122 | 2024-10-27 00:13:12 | METOP-B | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 66cac3a9-028b-399c-98da-d28fef4ee305 | -7.2452 | -41.219601 | 2024-10-27 00:13:12 | METOP-B | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8e0049b3-47a2-3217-9b52-3d630b36e2de | -7.2468 | -41.226898 | 2024-10-27 00:13:12 | METOP-B | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 551e8581-fb54-300e-8f40-22cc37b444eb | -7.9221 | -44.882801 | 2024-10-27 00:13:15 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cef6b290-7dcb-340c-84fa-0f9f7d77c0d0 | -7.9237 | -44.890301 | 2024-10-27 00:13:15 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1e3609-2fd7-3670-92ab-3920fd80f343 | -6.9578 | -41.3158 | 2024-10-27 00:13:17 | METOP-B | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c5b03b91-63f2-3de4-bb0f-429f749d2c74 | -6.9954 | -41.299599 | 2024-10-27 00:13:17 | METOP-B | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 74cdcd02-aca5-3b6c-bf0a-09e0cd5dd590 | -6.997 | -41.3069 | 2024-10-27 00:13:17 | METOP-B | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b0c8832e-e073-3ec4-a8ae-f6c815896bf5 | -7.8734 | -45.364101 | 2024-10-27 00:13:17 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b281483-0ee0-30da-a75b-0c07aaaca9d0 | -7.8751 | -45.371799 | 2024-10-27 00:13:17 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 675cdbea-f60a-3f56-9118-9ceb9dbb9661 | -6.9562 | -41.308498 | 2024-10-27 00:13:17 | METOP-B | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| de18fc3c-3411-3c9c-9212-56a3c8f0328c | -6.9162 | -41.178902 | 2024-10-27 00:13:18 | METOP-B | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4d83bcfa-da26-352b-818a-f80282eaa9c2 | -6.9464 | -41.310799 | 2024-10-27 00:13:18 | METOP-B | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2e48e2d4-5e78-3b3b-8f4c-b3dd845e2c1e | -6.948 | -41.3181 | 2024-10-27 00:13:18 | METOP-B | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b52badad-f883-3de7-994b-f6f47a837b55 | -6.9497 | -41.325401 | 2024-10-27 00:13:18 | METOP-B | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f4aa4f4c-b6a5-36e3-af87-8c5f241eb6f3 | -6.9514 | -41.332699 | 2024-10-27 00:13:18 | METOP-B | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b8b71910-25dd-34c2-a5e1-1427375b6a5f | -6.3961 | -39.684101 | 2024-10-27 00:13:20 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cbdc43f5-72b1-3569-b71f-1558756d5435 | -6.4148 | -39.542702 | 2024-10-27 00:13:20 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bc5893df-3d2e-3479-b055-2aba787d2715 | -6.3928 | -39.492298 | 2024-10-27 00:13:20 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ea26a817-07b1-3f01-aff8-b2bed5e7337e | -6.6825 | -40.879002 | 2024-10-27 00:13:20 | METOP-B | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8c3d03ea-bd97-3efa-96d0-2e2f34d665f4 | -6.6842 | -40.8866 | 2024-10-27 00:13:20 | METOP-B | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 085c95b9-fe7b-31c5-9f2c-8495d22caff1 | -6.6859 | -40.8941 | 2024-10-27 00:13:20 | METOP-B | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2e488e5b-3c0b-38ba-a71a-3267c3f5eb00 | -6.3981 | -39.692699 | 2024-10-27 00:13:20 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bf9c26f1-7245-3079-bb3b-44a2cb94cb0f | -6.6744 | -40.888802 | 2024-10-27 00:13:20 | METOP-B | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2db8e9d2-45db-3954-a3fd-60caed5b64ce | -6.6761 | -40.896301 | 2024-10-27 00:13:20 | METOP-B | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d71f0a5c-cb6a-3f66-a9ab-c48964179618 | -7.7097 | -45.6968 | 2024-10-27 00:13:21 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 673ad846-3ced-3cc2-ac73-b0a611a06620 | -6.3567 | -39.6478 | 2024-10-27 00:13:21 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4ffecf97-1b93-3e52-b37d-f129ef997f62 | -6.3587 | -39.656399 | 2024-10-27 00:13:21 | METOP-B | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 87c28454-0119-3867-9849-abfcead2e586 | -6.543 | -40.4972 | 2024-10-27 00:13:21 | METOP-B | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0e8dbc02-0f67-3d0c-ad0b-3ac93313b747 | -6.5448 | -40.5051 | 2024-10-27 00:13:21 | METOP-B | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 752d1a30-0ebd-3e41-8417-01ff4fa9ffef | -6.8695 | -41.923199 | 2024-10-27 00:13:21 | METOP-B | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b239467f-68f2-3167-afe3-c6c0b1c30037 | -6.6793 | -41.225201 | 2024-10-27 00:13:22 | METOP-B | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db884014-13c4-31d5-90f1-a0f1078a825b | -5.9273 | -38.120899 | 2024-10-27 00:13:22 | METOP-B | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 4278bc48-fafd-3ce5-9acd-c063ada4ac01 | -7.2615 | -43.941399 | 2024-10-27 00:13:22 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 88b38eea-ac37-328e-b620-7347efefdac8 | -7.263 | -43.948399 | 2024-10-27 00:13:22 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| da047ec0-7f11-3a13-b237-e242f47202e8 | -7.4223 | -44.713902 | 2024-10-27 00:13:22 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 59b7bdfe-2665-32e3-b88e-8288c3400f7f | -7.4108 | -44.708599 | 2024-10-27 00:13:22 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 16612071-ddb1-39a1-8ba9-f6dde3917122 | -7.4125 | -44.716 | 2024-10-27 00:13:22 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4cf98e31-6aae-3f75-ac63-527799809c29 | -7.4027 | -44.718201 | 2024-10-27 00:13:23 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7ec491b0-9fe7-3cc3-a5a7-cca190c3d9ec | -7.4043 | -44.725498 | 2024-10-27 00:13:23 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d7ee1abc-5969-3065-bbfe-fed32d005502 | -7.2135 | -44.003502 | 2024-10-27 00:13:23 | METOP-B | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c8c61415-17f8-3f77-ae4c-9a4552eda309 | -7.2151 | -44.010502 | 2024-10-27 00:13:23 | METOP-B | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c8dc05e3-df99-39be-99fb-6a42d5a9127a | -6.2004 | -39.729401 | 2024-10-27 00:13:24 | METOP-B | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fc6e6b67-8efd-315a-ad28-64eaae64751f | -6.1425 | -39.568802 | 2024-10-27 00:13:24 | METOP-B | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 567aafe0-971a-33a4-8c07-8edcb7898eba | -5.6793 | -38.0303 | 2024-10-27 00:13:26 | METOP-B | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 44970736-14ba-3f10-9f9f-10181c86fa91 | -5.6819 | -38.041199 | 2024-10-27 00:13:26 | METOP-B | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| bac7a75d-ce22-318a-94ce-db39537a76ea | -6.6011 | -42.0578 | 2024-10-27 00:13:26 | METOP-B | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a284f0ea-d9d1-3b9e-8f08-ecb2c8b2d308 | -7.3887 | -45.825298 | 2024-10-27 00:13:27 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa0e10c3-1fed-3134-a13d-352f517a3e19 | -6.52 | -41.928101 | 2024-10-27 00:13:27 | METOP-B | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1655da17-c8ee-3a91-a45e-fae9192140d0 | -5.872 | -39.204102 | 2024-10-27 00:13:27 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ea9689a1-9469-351c-a077-2aff5e25ca73 | -5.8742 | -39.213299 | 2024-10-27 00:13:27 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 46117263-7f66-329c-b722-8f2bfb03b316 | -5.8601 | -39.197102 | 2024-10-27 00:13:27 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a11f2067-1320-3c73-bb6e-69d734b99569 | -5.8622 | -39.206402 | 2024-10-27 00:13:27 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 66d384c6-2759-3648-915b-f53623d594a2 | -5.8644 | -39.215599 | 2024-10-27 00:13:27 | METOP-B | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0b30ef4b-8a4e-35e3-a555-938806d6cd6b | -6.847 | -43.560398 | 2024-10-27 00:13:27 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cfccf23e-b5ee-38c5-be89-62cac371b6ca | -6.8486 | -43.567299 | 2024-10-27 00:13:27 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 444d6a51-4376-3e19-9d03-ae7bdde1f99d | -6.5011 | -42.344601 | 2024-10-27 00:13:29 | METOP-B | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79ee4ae5-05c2-3789-a818-7dda8f43c77d | -6.5027 | -42.351501 | 2024-10-27 00:13:29 | METOP-B | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 248515b6-c0ef-32d5-8c8e-f9490601f80c | -6.6648 | -43.528702 | 2024-10-27 00:13:30 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9658311-4766-352d-b934-4e62a81e290b | -6.6664 | -43.535599 | 2024-10-27 00:13:30 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7618f6aa-fd46-37f5-9b33-0d629c2a0e04 | -6.2866 | -41.899101 | 2024-10-27 00:13:30 | METOP-B | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40bb982c-aa49-38cb-b8f7-298fee0f88e7 | -7.2547 | -46.058399 | 2024-10-27 00:13:30 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3046b9f-176d-367c-84c1-442a33cd208a | -7.2565 | -46.0667 | 2024-10-27 00:13:30 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 684f4639-8aef-30dd-b1c9-c150fd08f37c | -7.2378 | -46.027802 | 2024-10-27 00:13:30 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99fddf75-c15f-360d-a51a-5cbbd2b2757a | -7.2396 | -46.035999 | 2024-10-27 00:13:30 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5c31c2e-8659-3137-88f0-a6f3f0d72357 | -7.2414 | -46.044201 | 2024-10-27 00:13:30 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86ec3313-4fd4-3c9b-ae88-cb2c15f7cc8c | -7.228 | -46.0299 | 2024-10-27 00:13:30 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d21857b-cbaa-3598-9704-d7c7550ff19e | -7.2298 | -46.038101 | 2024-10-27 00:13:30 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbc9753d-494d-37c8-ae28-045d4ec9d31b | -7.2316 | -46.046299 | 2024-10-27 00:13:30 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f00c9c5-2beb-3692-b138-cf381661f83f | -6.627 | -43.681702 | 2024-10-27 00:13:31 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7dbd406-fcaf-3a3d-971d-0c395549f86e | -6.6286 | -43.688599 | 2024-10-27 00:13:31 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d0d1a9b-05e3-3d5d-9b08-0faacc30dee5 | -6.7405 | -44.0056 | 2024-10-27 00:13:31 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6d9f057-b980-3392-bfe5-7db49fe9f644 | -6.821 | -44.460499 | 2024-10-27 00:13:31 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a55aef2c-1344-327a-b16f-125e6b9cc929 | -6.917 | -44.893799 | 2024-10-27 00:13:31 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2aa3bbc3-5a9d-37ce-a066-613d06b80135 | -6.9186 | -44.9011 | 2024-10-27 00:13:31 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed102359-0006-331c-81ba-dc224692256c | -6.8097 | -44.455601 | 2024-10-27 00:13:31 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 345bfff2-8494-35fb-9514-7da90ea9a675 | -6.8112 | -44.4627 | 2024-10-27 00:13:31 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78bd41c1-630d-36de-bdb9-430a43c0c987 | -6.8128 | -44.469799 | 2024-10-27 00:13:31 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26fb44d9-d2f4-3655-862e-47f0197d3e1a | -6.8733 | -44.742901 | 2024-10-27 00:13:31 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8d0a50d-f07f-3976-9d3b-32db5b706904 | -6.8749 | -44.750099 | 2024-10-27 00:13:31 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f405910c-6ec3-31cf-b21f-49e454a830ee | -6.9743 | -45.200199 | 2024-10-27 00:13:31 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b5814b3-670c-3845-9eda-8cf1ed7cf692 | -6.9759 | -45.207699 | 2024-10-27 00:13:31 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7ee1765-2cb4-3ce0-99b5-415539abe89f | -7.0518 | -45.600101 | 2024-10-27 00:13:31 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79c75ebf-5b32-3e16-8532-40d016568b8c | -7.073 | -45.743599 | 2024-10-27 00:13:32 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b67e61b1-6491-32d6-ad3c-0a0a8f462af8 | -6.8729 | -44.880501 | 2024-10-27 00:13:32 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3259f458-3aff-3b9a-be52-9ff6244cba03 | -6.3723 | -42.960201 | 2024-10-27 00:13:33 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 665fa2e0-283f-33bc-b7e6-5e26d1f71ab8 | -6.7234 | -44.6698 | 2024-10-27 00:13:33 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 015a9ed0-c42f-3e39-93db-d4b27cedf629 | -6.725 | -44.676998 | 2024-10-27 00:13:33 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d54a46cd-7ec2-366f-a5fe-53ae49b9bc24 | -6.7152 | -44.6791 | 2024-10-27 00:13:34 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c377eb69-bb40-36a0-a4b1-5efd971c283f | -7.1022 | -46.441898 | 2024-10-27 00:13:34 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f518342b-7c54-327c-a85d-8e4b18fc0ea3 | -6.8764 | -45.8778 | 2024-10-27 00:13:35 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75e60bca-08f3-3deb-827c-e85c2e4c799b | -6.8781 | -45.885799 | 2024-10-27 00:13:35 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf60f9ea-4370-34d1-87d4-cc56836c7610 | -6.8631 | -45.863998 | 2024-10-27 00:13:35 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c7d003c-4721-3ec3-9975-d4455af6cb8f | -6.8648 | -45.871899 | 2024-10-27 00:13:35 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c182741-ded6-39bc-aa41-5b33aee8b1c0 | -6.8666 | -45.879902 | 2024-10-27 00:13:35 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a17b37c-fbd5-3f7a-b81d-9b2854f33401 | -5.9626 | -42.105999 | 2024-10-27 00:13:36 | METOP-B | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9daa1bc8-93e4-3820-8177-95896409972f | -5.9642 | -42.113098 | 2024-10-27 00:13:36 | METOP-B | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d5a378e7-8a71-34a2-8c87-c25e339a7f0d | -5.9657 | -42.120098 | 2024-10-27 00:13:36 | METOP-B | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README6.md)
