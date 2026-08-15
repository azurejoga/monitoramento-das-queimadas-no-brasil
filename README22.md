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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44940766-5b8e-3c16-91be-db848ef29b9d | -4.64114 | -55.70633 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b1e0f32-7b69-3293-9967-7349da8701ce | -9.11317 | -46.40117 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ee6cff81-4899-3ab7-8aca-9af1ac114eea | -8.02033 | -55.12586 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49f11dba-6c40-3334-93b8-85dfc47cc65d | -2.5335 | -57.88379 | 2026-08-15 04:57:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a582e13d-2fac-3fc2-9dc7-0fe057ae4ec7 | -6.78407 | -55.84864 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd4e391e-297e-33f3-96b5-562071c2d9a5 | -3.25286 | -61.19287 | 2026-08-15 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1b7b165-3108-362a-900f-01a3b2d7bed3 | -1.51124 | -52.59547 | 2026-08-15 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1600d55-2e8c-3618-a7bd-414442c181f6 | -6.61423 | -58.99812 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0f210b9e-e90c-3ed2-a52b-fdd78e524613 | -9.11867 | -46.39881 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 88bbdb21-2f81-39e2-ae7d-b4efaff06fbd | -6.79196 | -55.84248 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab373fd8-6ec2-3ed3-bccb-c7b5ed2c29aa | -6.84384 | -56.42342 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acfb7bae-f957-38fd-b45a-3c7ad9b2f6f4 | -8.02917 | -55.13439 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79bf7011-4dd0-375e-9312-7ec7d4be3562 | -3.71851 | -55.96991 | 2026-08-15 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fbbbca5-b9a3-312c-8781-7919c3f596b0 | -6.61016 | -58.99965 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6aae4742-0b46-32ea-9a68-388ed48d513c | -6.95706 | -59.28733 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd7bfd10-01cf-37c0-8034-3c94ebca544a | -6.6097 | -56.32921 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6f28632-5b22-3c63-be49-24feadfdc489 | -8.07502 | -49.7137 | 2026-08-15 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eeea2f2-e10e-3390-8e0b-10eddd00e83c | -6.61539 | -56.33722 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66762ee1-ff1d-3053-b4f8-7193647c6e58 | -6.64323 | -56.07285 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10cc395f-9a30-3b4b-88c2-b61a8abf6954 | -7.45759 | -55.30778 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf52d62c-3540-399e-b418-ce027b656b22 | -8.5185 | -46.53434 | 2026-08-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a5f2415-4bbe-3a65-9d8a-be688995ba6b | -6.62454 | -59.05699 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 559e2dd0-bb60-318a-a4ce-2eac62d3638a | -5.33868 | -43.17784 | 2026-08-15 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 452d609d-df4e-36a1-9fd6-b3d9170515d9 | -7.06309 | -56.65563 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 053f2747-1616-3f82-b0c8-1190e5987e3d | -9.11399 | -46.39498 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4327ef7-7d7e-30ba-9dcc-9da4c2ac30f9 | -7.69531 | -55.15968 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f9cb944-c6ae-38ed-828c-1fc214e1d364 | -4.23213 | -49.92348 | 2026-08-15 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6b90e8e-7b1a-342b-9948-aa38ab86bf1b | -6.78744 | -55.84917 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b9b3a2f-7a98-39ff-b9b7-ae2f818c97ea | -8.49394 | -44.7397 | 2026-08-15 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a33cee89-3aa7-3531-85e4-01d62732113c | -3.75001 | -59.32877 | 2026-08-15 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 955a3686-0a97-3a71-806c-f96c0d9b4382 | -4.10985 | -42.50227 | 2026-08-15 04:57:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ae995efb-9324-3921-92f0-275f5160103b | -2.79166 | -49.58269 | 2026-08-15 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24f3557a-d130-3023-844e-3d4372acd93b | -2.79303 | -49.5224 | 2026-08-15 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 060a0349-2d12-3572-b0ed-1c48a3ef0a73 | -2.6255 | -47.99731 | 2026-08-15 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 272e09af-e58d-334e-9c46-5be484bac4e3 | -6.69791 | -58.95516 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73e529fd-e98d-3ac1-bbdf-9bab06d94d2f | -3.59495 | -58.61662 | 2026-08-15 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf7596ae-3c54-3728-bbbc-7faabf4a0179 | -6.85817 | -56.42188 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4107c4d2-71d2-362b-899a-0488d9e381e9 | -6.54624 | -55.17698 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58c3d70e-dcf4-38bc-a239-56692c3d41d2 | -6.96729 | -59.29967 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 973a51c4-6726-37b3-b8df-0ae7b08e8026 | -2.72446 | -53.97568 | 2026-08-15 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 301f2802-92ea-3a8a-b7a1-63fc430ade6d | -3.93149 | -52.24901 | 2026-08-15 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82312609-b5ec-3197-ab3c-0f4d487ba32a | -7.70029 | -55.17118 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c4f6a09-33a8-30ca-b916-0aea77d280bf | -6.54346 | -55.17297 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29d37c57-b212-3bd4-a895-7c00355e4be0 | -6.86052 | -58.97129 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96da19ac-bf2b-321a-9c0a-6201aea253d5 | -7.01655 | -41.4353 | 2026-08-15 04:57:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c2cb070d-7556-32c5-8f57-27f06913b0fa | -6.96104 | -59.28798 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8333fae1-4359-3538-9b24-01a7d4982816 | -6.11641 | -44.03418 | 2026-08-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3bbf15eb-814e-335e-bb2e-505543fc1ecc | -9.11389 | -49.26374 | 2026-08-15 04:57:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1baf819-202e-33e4-9630-1bf6e4ac7460 | -7.41923 | -60.00462 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e5954ae-e23e-3501-989b-727c5159b3ed | -6.72224 | -58.93111 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2d1450d-7e75-3dc6-8a3d-75f72a285cbf | -3.16883 | -48.06879 | 2026-08-15 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c0de659-27cf-33b0-a743-e5d6cdec58f7 | -6.95932 | -59.29834 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53c5aa9a-0f18-3437-8eb2-25f133091d63 | -3.66864 | -48.92817 | 2026-08-15 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 258a318f-edc9-3fb6-8fda-208f69cd4392 | -8.44974 | -45.11518 | 2026-08-15 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d687b20-81f1-3f96-8077-e17fa753df83 | -6.62145 | -59.05124 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dae49881-5011-37bd-8d1f-fb8908c5d680 | -6.59351 | -56.36483 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59559c94-022b-349a-916e-416307485233 | -9.12845 | -46.40329 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be1e6b63-4b91-3088-b62c-e7d7c54ec794 | -8.36549 | -46.38081 | 2026-08-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 456ac443-50ff-33ec-914a-6650f218a842 | -3.50519 | -57.01923 | 2026-08-15 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dafee300-4139-37cc-afd4-684589cdfb2e | -6.61838 | -59.04546 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6cd6131b-ae13-3edc-8799-c4b53e123a86 | -6.78687 | -55.85279 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c136ee8-944b-3bd0-901e-84c8fcc69118 | -6.96388 | -59.29552 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 952497cc-a38d-3718-9601-1ad8a329c838 | -6.72139 | -58.9361 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b681ec5a-ef4f-3272-8a1e-1b72fe2af849 | -6.60736 | -56.34399 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64e650ac-2dcd-34d0-8dea-c784c336562a | -7.45814 | -55.3043 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6a2a1dfd-e3a5-3cf5-9fb6-40dead07f65f | -6.9525 | -59.29013 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3cf7382-487b-384f-ad57-9149198ac37c | -6.96218 | -59.28108 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd4169ad-94a2-33e3-8fc0-d3a09a283a69 | -1.48046 | -60.29824 | 2026-08-15 04:57:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f6c0767-ab56-3d61-aaa6-647a9a1f6a2c | -6.59467 | -51.67529 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9207c808-621a-3f48-b2c0-9e713fbeefe8 | -6.8483 | -56.43947 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99d71473-046e-3a82-aa39-9aeb6cecff8d | -6.9582 | -59.28042 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2549e54a-d2a2-3368-abbd-eea0c1cd026c | -6.61409 | -59.00029 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9a6e8253-8122-36c9-bfaa-e3f5bf5bdfbd | -8.80366 | -47.92907 | 2026-08-15 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f797a53e-78e1-3d9d-97d7-5d14bef27133 | -6.71595 | -58.94305 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e6764c8-a7a8-316a-abf0-586b2d0a0280 | -6.62292 | -58.99446 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30632ede-6ec7-3998-9ed2-0cebdd37a015 | -6.79647 | -55.83579 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8279a75-4981-3cc6-8fad-3187e8e4749f | -6.85775 | -56.40264 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdf3004a-ea35-3936-8af2-970aa8cfa1cf | -6.36724 | -51.74453 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0189a82-a344-361f-a636-c8df47ccc313 | -6.70263 | -58.95086 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a26b999-6b77-33a6-8724-98752c2dd798 | -7.41774 | -60.0012 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a0db70b-69bc-304c-b75e-fb1c1c621f72 | -4.31251 | -59.46958 | 2026-08-15 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 267dda79-fbc2-3230-95ed-9bfb84ffe3ca | -6.64915 | -56.41175 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ae3ad6f-e726-3007-ae75-fa549ea48932 | -7.45427 | -55.30724 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdb8277e-7526-3b6d-a3c7-80b4f4d456a7 | -6.34217 | -44.07262 | 2026-08-15 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be3f7e0c-564f-30f7-a250-cc7e5558b9ba | -2.9495 | -50.31712 | 2026-08-15 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 91f32805-2076-39e3-96f7-e78b3fe4723c | -5.13761 | -50.85076 | 2026-08-15 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8383758f-1fa8-3308-b02e-0ce8250f6990 | -6.61137 | -56.34037 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a97321a-3ed8-3a3f-b329-734aa6f028d7 | -8.03248 | -55.13492 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bb83b4bc-77da-357a-b5f4-b6a298494b1a | -3.23934 | -43.22301 | 2026-08-15 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 535e513f-007d-3ae0-82c1-5548d638a867 | -1.48511 | -60.29894 | 2026-08-15 04:57:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f841aaa1-28b2-322e-b407-d392c76fa350 | -3.94789 | -59.62968 | 2026-08-15 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f349e11d-43be-3556-87d9-e8c41b3ba921 | -6.58781 | -56.35639 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc705d7f-0d84-3385-b848-537ca60168b4 | -6.72148 | -58.93372 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ba48590-046b-348c-baee-f6d3b6e8bbf7 | -9.16687 | -45.83113 | 2026-08-15 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33200a04-be4e-3857-9ba0-2ce5d9cf4295 | -6.96273 | -59.30248 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6c628b5d-62d8-3ead-9b69-1db445579879 | -1.96802 | -48.37 | 2026-08-15 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82494ed3-ce80-3503-8ea9-86bf6cdcb5d1 | -8.75601 | -49.41914 | 2026-08-15 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8af60770-96f5-30bd-bf61-614226e84ccd | -6.79963 | -55.84784 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27e9dfc3-1815-3d0c-9a08-beeab809b371 | -6.31592 | -47.33421 | 2026-08-15 04:57:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 892d270e-c5a2-3fa5-991f-0c2c57392445 | -6.11761 | -44.02542 | 2026-08-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README23.md)
