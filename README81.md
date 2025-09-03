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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f77adb4-1fec-3191-ac04-42e77f0f9328 | -7.92536 | -46.54728 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e485bf6-7c5b-3819-bd06-13483b2b12b3 | -7.90989 | -46.4803 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ba5df78-8e48-3dcd-8008-a047aac0a4e3 | -7.69321 | -48.74903 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 21aa8c5d-8efe-38b6-ba58-9578d1dc2064 | -5.90365 | -57.74266 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 481ff5e4-90f8-391a-9d9b-05a06481b121 | -5.9203 | -57.72386 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 20bd0163-035f-32a8-b01f-06ec02e3b6eb | -8.05761 | -45.36414 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3822bc2f-5bbf-34c0-b60c-7a96483ca464 | -7.7037 | -48.75059 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6252917d-ab6b-3799-b169-f3211b066ccc | -6.47693 | -45.41103 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05d436e9-8c01-3dbc-9519-a7c87c15c65b | -6.17405 | -43.31322 | 2025-09-03 05:12:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 05288bd9-c582-3760-92cc-1f4c3ce38838 | -8.21005 | -44.81237 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 51afd081-c8d1-3f1b-8226-0fb79a26e77d | -6.84936 | -52.79588 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e7883dd-ed86-372a-8468-c1a13858c401 | -5.89643 | -57.74511 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 4071c10b-b989-37ac-aec3-1c4029740802 | -6.79467 | -52.81641 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0551a2e-e198-3c68-ae40-8829668ec553 | -3.21326 | -61.19582 | 2025-09-03 05:12:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35ce5a0a-11f2-3c50-a6a4-5d045a12adf7 | -7.91641 | -46.42982 | 2025-09-03 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f4f5a11-4237-31c2-a113-1db89b83eae8 | -8.05828 | -45.3588 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85eab3f9-c9d0-3153-9cf7-efbd952a4c84 | -6.15052 | -56.1303 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e335710-410c-3453-9b23-5a12a8b81d56 | -6.81113 | -52.81392 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e2da948-25f3-356f-b2e3-d56c75417800 | -6.52832 | -56.19581 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b161ca0-dbb5-38d7-b5d4-48b9594e9bed | -6.89827 | -45.56834 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6223182-fcaf-3da1-8861-68b1a5b95171 | -7.8998 | -46.46049 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b1d0546-42fa-3dcb-b936-50b0b2fbaf2c | -6.43169 | -55.62239 | 2025-09-03 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dc413ac-e469-3437-9e36-5bf6c2b71f50 | -6.23453 | -55.63422 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23a454dd-7263-3ee2-bdd0-9966fed2441d | -6.85402 | -52.79156 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7d1b180-8309-306c-9f55-0b20a605d32f | -7.93225 | -46.54777 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3cb29388-eb75-3fb4-a4e2-05583358e8b5 | -7.48875 | -44.81704 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 38af8a50-bf97-3a40-a5b9-7e233aec20b4 | -6.19424 | -43.34432 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63f351c9-66e1-3fb6-ab22-b368d0624623 | -6.81507 | -52.81448 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55cc26ad-abc5-3474-b813-25feb9e256f9 | -6.33664 | -58.18512 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0f81629-b46a-30e3-9944-23fad9fe8a79 | -6.82282 | -52.81224 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb703392-7386-3a90-87d7-508b6d6d2bd3 | -6.97344 | -44.35455 | 2025-09-03 05:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a69ff200-967a-317f-aafa-1e599d74b164 | -6.81816 | -52.81664 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90474488-6d71-34eb-8231-f51a2597a608 | -5.86533 | -57.76877 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d8e47fd7-c56a-35b7-8dd4-efe818350c63 | -5.9214 | -57.71689 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 48840951-41cd-38d6-95a4-a24609786e23 | -5.8942 | -57.73762 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 599f860d-31e9-3d67-a646-cfaff5aa0443 | -6.80103 | -52.82758 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc25018a-000d-3450-b102-2c02d34d9566 | -6.3514 | -45.66564 | 2025-09-03 05:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ede00f8-39b6-3046-b7ee-536951e9743b | -6.83814 | -52.84502 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a6306a3-b6c0-3415-84c6-54a28e1bd634 | -2.93402 | -49.46059 | 2025-09-03 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88b7d6af-bb69-37c9-b6d8-50893c31e9cb | -5.87088 | -57.77684 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e72620f0-96ea-34e3-b854-54292c74354c | -7.93954 | -46.53942 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 998b800c-4230-38b3-9f3a-4a7d1aa44db4 | -5.81165 | -43.22214 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a075c2e1-1c36-3425-b939-79718c098e63 | -6.03616 | -46.01923 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69c34e1c-96cc-3446-803c-053c3737722b | -6.81028 | -52.81552 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fc33036-6e19-3726-b8a1-c4893baf2e72 | -7.53057 | -47.44601 | 2025-09-03 05:12:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10a36695-dbbd-3156-a3ad-bb579d4eb959 | -7.70671 | -48.72912 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4a07193d-3f95-3b20-b790-99bc14ed99ab | -5.81781 | -43.23093 | 2025-09-03 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f8c78087-c620-3a82-ba9e-c5e7843ceb48 | -4.52683 | -54.97128 | 2025-09-03 05:12:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 945899ec-946d-3636-8601-3cd2a2f363b3 | -6.70223 | -48.40481 | 2025-09-03 05:12:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5db6247d-401e-31fe-8d09-dff9e354ab8e | -3.20124 | -49.1072 | 2025-09-03 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18b108f6-f216-37b4-b97d-d77c664b5598 | -5.91586 | -57.73032 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3b37d193-4e6a-3c0e-989d-9c422adc4c40 | -7.9071 | -46.45258 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b60a462-669a-3e29-94ba-e7b687235027 | -4.36586 | -54.74399 | 2025-09-03 05:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6a0b50c-e6b7-3a7b-86b2-fe80a1930c18 | -6.70268 | -48.40171 | 2025-09-03 05:12:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e307981d-c4ce-38bd-bfb8-6c2a384a81ae | -6.45939 | -49.52819 | 2025-09-03 05:12:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d53579ce-b989-38a2-a8d4-6cb4d4b74489 | -6.20052 | -43.35265 | 2025-09-03 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da3b8785-d77f-3561-aa8f-e7044fa0f2c3 | -7.80214 | -45.45964 | 2025-09-03 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 121369db-9666-3301-96fb-9e708eff42ac | -6.33555 | -58.17049 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89ba3cb1-3f8e-3113-85a0-89640c4c1aaa | -7.49021 | -44.80547 | 2025-09-03 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3a8b8896-09b9-38f8-99e6-b22a9a3a0edc | -5.91087 | -57.74025 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2fbbf2ce-14aa-3b76-afc4-04e229cbfcb8 | -5.90697 | -57.72177 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0038292d-5ad9-387f-8f35-7bb2b813e22d | -5.86699 | -57.75831 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a7b8c885-dfce-3e61-86d2-fe4e70b866d5 | -2.90389 | -48.29384 | 2025-09-03 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa5b039d-976a-3f5c-8501-1617b5b9731a | -7.85724 | -46.73128 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e69538d-dc15-3f21-99d7-2e9543fb5ebb | -6.82269 | -45.68607 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8a26e3e-feba-3d19-952b-dbfee831e57b | -6.77181 | -52.80793 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 770362af-992e-397d-a0f2-2a4e26c2697f | -6.86218 | -52.81816 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c742e90c-0945-3d88-b64e-1cde28b6e2c5 | -6.82371 | -52.81062 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d13949b5-203d-3223-aff6-2c677f154270 | -2.20035 | -47.99267 | 2025-09-03 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb0e92cb-07c6-3564-8a45-b89d5391187c | -7.72192 | -48.72742 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5b2a7c18-bc98-366c-a28a-de557c8254f8 | -7.92257 | -46.4305 | 2025-09-03 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b026e88-710b-3507-82a3-90a1dd0af63c | -5.87199 | -57.76986 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e4459b04-7ed3-3846-91fd-5869730230d3 | -5.86255 | -57.76474 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2d631369-43ba-3b81-9d8e-7f9a0631990b | -6.41036 | -43.76118 | 2025-09-03 05:12:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e79873e6-6dda-3d04-b62d-bfd186eaa952 | -7.93344 | -46.53859 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6fb0168c-5d9e-3c9a-b865-6262895276e4 | -6.0374 | -46.01036 | 2025-09-03 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0366e6a7-03d2-363e-865d-604cbc6414dc | -6.7901 | -44.09701 | 2025-09-03 05:12:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| adcd55cc-c5bf-3a64-b575-dcf1a44c4804 | -6.85521 | -45.54925 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efef24b5-622f-3996-ada4-cc919b14a5c4 | -6.87123 | -45.56796 | 2025-09-03 05:12:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 894b8662-0048-3631-8e9d-bea99996b637 | -6.05481 | -58.00311 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c96765ec-9cd6-3d28-af20-80ab6ab4f77e | -4.13074 | -56.18023 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f789bea-81a9-3265-97a2-5c49448a429f | -6.78359 | -52.80983 | 2025-09-03 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2208815b-5b74-3492-b7af-9791690f8251 | -6.26033 | -57.7774 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15a245e4-e9fa-3214-b905-a72acda6cce4 | -6.46395 | -55.88784 | 2025-09-03 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aadb062c-e87a-3022-b462-72934219e12a | -7.70413 | -48.74755 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e54fda3-263a-32a6-b1a5-32eeab778773 | -7.90785 | -46.44746 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 17c9e7d6-96a6-313a-9402-d28fb01d922a | -7.72237 | -48.72407 | 2025-09-03 05:12:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7a07d441-2548-3326-853c-f6649ca43458 | -4.1554 | -46.79277 | 2025-09-03 05:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ed5348e8-b5eb-35a3-bb72-096c08e3af7c | -8.01781 | -44.10901 | 2025-09-03 05:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c79929d-444b-3c01-8049-beb5ba38b982 | -7.93166 | -46.55235 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1e9985f0-6861-3d10-8c74-54f88ac0cf01 | -5.90643 | -57.74668 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 08f5139b-ae22-3d67-b6d6-302b80f2ad44 | -2.93938 | -49.4566 | 2025-09-03 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 293f709b-7c28-32ff-8232-d91b9aba45b2 | -6.27319 | -44.51651 | 2025-09-03 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3486aaed-43ed-3147-9924-11bcb690711e | -2.89928 | -48.29017 | 2025-09-03 05:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48686d53-9e80-32e9-ba84-59ce02d53b8a | -5.86144 | -57.77171 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2d303cae-9a7c-36fc-bed2-c678ebf3373c | -5.86588 | -57.76529 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ca46fb6a-2c3d-329a-89fc-6835eef71175 | -6.33833 | -58.17455 | 2025-09-03 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5284378a-d4a1-331f-ac3e-b8152722d54c | -8.07041 | -45.37726 | 2025-09-03 05:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e690cc73-a9f1-35dc-ba4b-759bc81b115b | -7.94074 | -46.53026 | 2025-09-03 05:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3f6b004-9d6e-3ee4-801a-585392d8578d | -3.5247 | -59.01432 | 2025-09-03 05:12:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README82.md)
