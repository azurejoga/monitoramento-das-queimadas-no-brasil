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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79bc1300-519e-3725-8427-ac432255a763 | -10.05676 | -48.06483 | 2024-10-28 00:50:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d99d596c-d42d-3822-b424-ff3b0949e304 | -2.8548 | -49.238098 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2ae397e-3dd4-3756-9972-c21dd7d0fcd4 | -2.8564 | -49.2449 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01ba24c0-c8a1-392d-93fd-705d53080a28 | -2.8579 | -49.251701 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08931b48-9057-34d2-9505-6c107592462a | -2.8595 | -49.258499 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf2d38a2-b5a9-3784-b80a-880aad63d085 | -2.2719 | -46.755299 | 2024-10-28 00:50:01 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3026134-c54d-352f-9e8f-43af0623a7dc | -2.2738 | -46.7631 | 2024-10-28 00:50:01 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6354c933-3e14-31b4-96f8-7019f5d9299e | -2.2756 | -46.771 | 2024-10-28 00:50:01 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77b77297-2866-3402-953b-37fcbfee4694 | -2.7038 | -48.625702 | 2024-10-28 00:50:01 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49549d0d-c648-371e-93de-9edddeeba522 | -2.8435 | -49.233501 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7991729-95c2-3a74-bb23-d1c01fd2ccd7 | -2.845 | -49.240299 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 852f7bdc-7b5f-392d-9c31-04797ecb284e | -2.8466 | -49.247101 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d337a57a-5db6-3021-8f34-fd7d833aa62d | -2.8481 | -49.253899 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebcaab1a-b1fa-367d-8c5d-683a1330bb39 | -2.5838 | -48.149101 | 2024-10-28 00:50:01 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29c2c85a-22bd-3632-b9e3-0d37c399bf34 | -2.8321 | -49.228901 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 533914fc-ad60-35a5-9eb0-cc3ef2dee76e | -2.8337 | -49.235699 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38aefe8c-48c3-3a1a-b543-bc7f2e116fc5 | -2.8352 | -49.2425 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aafc096-adc6-346a-9d76-e542b14a6fab | -2.8368 | -49.249298 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7b00b2d-6427-3a70-b39b-64905c2ccae8 | -2.8383 | -49.2561 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2b45b38-19bc-3d45-b1e2-dce102e287a7 | -2.6858 | -48.637001 | 2024-10-28 00:50:01 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a19df41-76c6-3749-973b-2d4108252783 | -2.8192 | -49.217499 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ab781ca-406d-309e-8d5c-dd3b59bd40f0 | -2.8207 | -49.2243 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1df80759-990f-3eb9-8fc8-e54ab5670e5b | -2.8223 | -49.231098 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68bc0709-aa11-3f63-bc0b-d749b7aab337 | -2.8239 | -49.2379 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9061359f-c7ac-33d6-af64-68624d42376e | -2.8254 | -49.244701 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6662b4a-eedc-3484-981d-6fd154b48e7e | -2.8285 | -49.258301 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac963f26-08eb-3e78-a4a0-cba8d522ed14 | -2.8535 | -49.367199 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f929c9e-bb4f-319c-90a6-b2217a809ed7 | -3.3448 | -51.520599 | 2024-10-28 00:50:01 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e298edc-dbbf-3730-8e43-8dacaf9cd7e7 | -2.8094 | -49.2197 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff5f4c4-337d-3223-a310-c6bbef34a029 | -2.8109 | -49.226501 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16c64289-db20-30d8-93a8-1d890820ef7f | -2.8125 | -49.233299 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfae1bb7-6e58-3973-bbee-4c133cbdb4c8 | -2.8141 | -49.240101 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f235fca7-ef81-3060-8f83-bbf08a2fa0f5 | -2.8375 | -49.342201 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d6e993-3416-310c-a8f8-78f45ad55899 | -2.839 | -49.348999 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac80ccc2-1c1f-3db0-9886-65d635d71ec0 | -2.8624 | -49.451099 | 2024-10-28 00:50:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 832c8f42-c637-35fe-bace-038316857554 | -2.864 | -49.457901 | 2024-10-28 00:50:01 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b470dd17-5553-337b-a686-cfdd6115b6f3 | -2.6455 | -48.551899 | 2024-10-28 00:50:01 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce37a422-4d74-3517-b641-6b4da6f7a670 | -4.2145 | -55.487301 | 2024-10-28 00:50:01 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33dd835e-680d-3a0b-b33c-ed36dc55c187 | -2.7067 | -49.042301 | 2024-10-28 00:50:02 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09ee8bba-3003-3ff8-876a-b028929c4dd4 | -2.7083 | -49.049099 | 2024-10-28 00:50:02 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70121c27-05e3-3da6-81a2-2f13d79b1837 | -2.7098 | -49.055901 | 2024-10-28 00:50:02 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 406c8661-57fd-3645-805b-fe7d332e872d | -2.6969 | -49.044498 | 2024-10-28 00:50:02 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84062eb6-6f35-39bb-af33-bef72e9c79b3 | -2.6985 | -49.0513 | 2024-10-28 00:50:02 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f672bf5b-75b2-3e4c-906e-e10f6a61b234 | -2.3674 | -47.658501 | 2024-10-28 00:50:03 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abefe86c-886f-3a18-bd27-9dd361c870c1 | -2.3691 | -47.665798 | 2024-10-28 00:50:03 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4e25f0f-85ba-3951-a907-72e93b3a67bb | -2.3707 | -47.673 | 2024-10-28 00:50:03 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d7e090-4cc5-3398-897c-62acdf170705 | -3.26 | -51.555302 | 2024-10-28 00:50:03 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c530cd43-61a9-3258-b6b0-db69187f475f | -3.2617 | -51.562901 | 2024-10-28 00:50:03 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f84c7925-dbd7-30b5-8cc0-ea3003a605e4 | -2.0643 | -46.526501 | 2024-10-28 00:50:03 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fc38de2-903c-37dc-afb5-b16be677b662 | -2.7041 | -49.3004 | 2024-10-28 00:50:03 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d529839-57bb-3e0a-aada-30c12caf6554 | -2.7056 | -49.307201 | 2024-10-28 00:50:03 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7efe374-2d06-3920-8781-97e682020728 | -2.7072 | -49.313999 | 2024-10-28 00:50:03 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abd92d1b-91fd-3d0b-ad5f-61877d18a1cd | -2.7088 | -49.3209 | 2024-10-28 00:50:03 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd63945f-4ae4-3264-a491-77f906b908e8 | -3.3572 | -52.165798 | 2024-10-28 00:50:03 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30add7a6-a132-3732-9932-984efa7143e5 | -2.4484 | -48.501701 | 2024-10-28 00:50:04 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8fa8fa-c253-3025-be4d-1cd7498e9113 | -2.5959 | -49.188801 | 2024-10-28 00:50:05 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80a11b3e-d35a-374f-ad3c-331182fe9089 | -2.5975 | -49.195599 | 2024-10-28 00:50:05 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f23ea0af-5d05-3a04-8b39-aaece7aeb304 | -2.3507 | -48.436199 | 2024-10-28 00:50:06 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4566e9e-248b-3648-a2c6-00febbbaf56c | -3.7199 | -54.462299 | 2024-10-28 00:50:06 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58e86220-889e-3687-a71b-1a99734df3c9 | -2.3393 | -48.431499 | 2024-10-28 00:50:06 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13cb894c-0b2e-37ff-8929-27165cd75a7f | -2.3409 | -48.4384 | 2024-10-28 00:50:06 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 072a50bf-ff08-3c42-bccd-7a87899525b3 | -3.0313 | -51.455399 | 2024-10-28 00:50:06 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19edd238-4e69-38f6-8380-9e6a1a02cfe6 | -3.033 | -51.462898 | 2024-10-28 00:50:06 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47a7c86c-0504-3e7a-8924-c0088d1f341c | -1.5439 | -52.071098 | 2024-10-28 00:50:06 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79407bf4-f68e-35fb-9adc-609808dc8781 | -1.5456 | -52.0788 | 2024-10-28 00:50:06 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dbc5fcc-8c17-3e20-a4c8-99e7edf75244 | -1.5474 | -52.086498 | 2024-10-28 00:50:06 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 599db8d3-4cb7-38ee-a6f0-e816b1976f32 | -1.5491 | -52.094101 | 2024-10-28 00:50:06 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 823eb41e-3534-3f52-a3dd-66b39d2e8bc2 | -1.5509 | -52.101799 | 2024-10-28 00:50:06 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0a6ec64-c394-3570-a290-2a0d255c875c | -1.5526 | -52.109501 | 2024-10-28 00:50:06 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2dce2dc-3b3f-3bd7-88dd-9ebfdfecbf3b | -1.5341 | -52.073299 | 2024-10-28 00:50:06 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebac4bf1-8b83-3366-9955-19fc3bfa11c9 | -1.5358 | -52.081001 | 2024-10-28 00:50:06 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34c0c687-1526-3083-b65d-d649d285d15f | -1.5376 | -52.088699 | 2024-10-28 00:50:06 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdcc25d4-477b-348b-a547-c14b6deeb13f | -2.3603 | -48.925999 | 2024-10-28 00:50:07 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab45cc3-e585-3d04-a1fe-403fdb5ed2c6 | -2.4276 | -49.2192 | 2024-10-28 00:50:07 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87be63d5-bdac-3c72-b3dd-470d4a137680 | -1.7848 | -53.263199 | 2024-10-28 00:50:07 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29e0b764-6a84-38b1-a873-ec06d01e8569 | -1.5976 | -52.486801 | 2024-10-28 00:50:07 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79bc5ffc-1204-3124-9459-bb788fede2ed | -1.5994 | -52.494801 | 2024-10-28 00:50:07 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a14d333-4064-3f12-9a01-98502f933ab2 | -2.873 | -51.303101 | 2024-10-28 00:50:08 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da74f869-306c-3460-bf6a-95d7651249b7 | -2.8747 | -51.310501 | 2024-10-28 00:50:08 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78aa2c40-fc8c-3fdc-b844-169ff05b17ba | -1.6359 | -52.925999 | 2024-10-28 00:50:08 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8650df75-75c0-3099-96e5-1006d06c5c48 | -1.6242 | -52.9198 | 2024-10-28 00:50:08 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7c56f1d-2387-377e-b5c3-d0a9b02b9c56 | -1.6261 | -52.9282 | 2024-10-28 00:50:08 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef8c7736-2a2f-3f24-9ede-8838095c4eff | -2.1883 | -48.806198 | 2024-10-28 00:50:10 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 189b9c34-65e4-35aa-ae09-0824b085ddd2 | -2.1898 | -48.813099 | 2024-10-28 00:50:10 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2c93f02-8f42-3812-afa9-5eab969d07c0 | -2.1946 | -48.833599 | 2024-10-28 00:50:10 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da4d1d9a-b542-3ff4-91d3-ee050fc6743d | -2.8782 | -51.824299 | 2024-10-28 00:50:10 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8e921f8-41b3-30fa-9cda-1ed4c3d5523e | -2.88 | -51.832001 | 2024-10-28 00:50:10 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d14bf9ba-34ab-35e8-b173-626fe6c11a89 | -3.5202 | -54.669399 | 2024-10-28 00:50:10 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5ebc998-1843-31ad-a9a7-0ae55f9a320a | -1.7559 | -53.994801 | 2024-10-28 00:50:10 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa64c2db-f333-36e4-94f5-6e901549379b | -2.1279 | -48.9925 | 2024-10-28 00:50:11 | METOP-C | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56a2f139-0f15-3bbd-88f6-d542a6807163 | -2.1295 | -48.999298 | 2024-10-28 00:50:11 | METOP-C | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee5df6a-fd3b-3e78-afca-6cd54f8c5e42 | -1.9768 | -48.425098 | 2024-10-28 00:50:12 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b687f603-6302-3dd7-8e59-ed2b6ad3f02f | -1.9784 | -48.431999 | 2024-10-28 00:50:12 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf2b9b7e-b590-3d87-a8d7-7875ebdd5b76 | -2.4032 | -50.418301 | 2024-10-28 00:50:12 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ab48fb2-45a7-3a8c-a6a3-d92f1adf0709 | -1.1462 | -51.9995 | 2024-10-28 00:50:12 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 587f6583-49be-3fbc-9b64-b25ab8c51f6b | -1.1479 | -52.007099 | 2024-10-28 00:50:12 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ee790fe3-9be3-3c13-a366-dd4d6808e9d0 | -1.7793 | -47.836498 | 2024-10-28 00:50:13 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 612854e9-e9ae-3273-9f96-245a752fee22 | -3.1632 | -53.902199 | 2024-10-28 00:50:13 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbd3c620-6788-3fa6-a68b-7c181dd9edb1 | -3.1654 | -53.912201 | 2024-10-28 00:50:13 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6865ae61-81cc-3860-baca-ba0ec286794a | -2.8462 | -52.5448 | 2024-10-28 00:50:13 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
