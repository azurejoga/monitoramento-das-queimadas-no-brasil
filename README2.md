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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdc6d621-f04d-34d2-8a1f-07d50de9c4fc | -10.81665 | -50.18806 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 62070935-7ff2-30c1-9a9d-cf19f0787c61 | -10.82689 | -50.19612 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d2a132e6-14ac-3048-9344-148e3953e840 | -9.09005 | -45.72078 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| cfa16640-b605-3588-95dd-7ee78308b7ad | -7.05527 | -46.23244 | 2026-09-18 00:01:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e40d667e-2091-310d-8257-83e6a30f6e38 | -6.01887 | -51.76717 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 88b5a889-c234-38fa-8c23-d156fd04bd55 | -6.18814 | -47.52606 | 2026-09-18 00:01:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c57975b5-6624-3ba4-94b6-b3da26d5c30e | -4.36199 | -47.78742 | 2026-09-18 00:01:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2475d973-86b4-3380-8dc9-6c3c0512ad4a | -9.39166 | -46.85231 | 2026-09-18 00:01:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ff99cbc3-4f9c-3416-9dce-ed7d5ff23154 | -11.13975 | -49.03952 | 2026-09-18 00:01:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cf5f1e64-1695-3bb4-be28-a2a225831d26 | -11.3146 | -47.25687 | 2026-09-18 00:01:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 59c19cdc-b925-370a-9750-ce41c6b84d54 | -4.41246 | -42.32468 | 2026-09-18 00:01:00 | TERRA_M-M | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 826497ac-ce9b-3de7-baed-6baad37be122 | -6.32066 | -55.26859 | 2026-09-18 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| fec532ac-9eb0-3ebb-9bef-09aeaae2f56a | -11.06376 | -48.29395 | 2026-09-18 00:01:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 37f1969d-956a-3584-8557-1108a4fd0c8b | -11.52753 | -46.88129 | 2026-09-18 00:01:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b9be8d2f-ef4a-3990-8168-300f0f39ac1b | -6.32276 | -55.28503 | 2026-09-18 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 23991112-cb4d-3483-af97-16f87a617915 | -11.31045 | -46.77112 | 2026-09-18 00:01:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4febb747-eebf-380d-8093-d7870579875c | -9.54353 | -45.45782 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| eded8d72-5196-380c-9729-6776cb6eec3f | -10.66297 | -50.27874 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9ad4bfb2-2b63-3422-be3e-e9a08a7a02ba | -10.32959 | -45.30508 | 2026-09-18 00:01:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 8f1fbc67-381e-381c-9d7b-750b44828ccb | -6.02536 | -51.33248 | 2026-09-18 00:01:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f7ecb9a6-e6ba-3dbb-991b-019e67762aa1 | -7.80585 | -44.90186 | 2026-09-18 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 73601e39-0d20-30b9-be17-9f973ec0818d | -10.65187 | -50.47207 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5c0727ed-8375-336a-b814-665182f964f3 | -4.77728 | -55.71543 | 2026-09-18 00:01:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7e8beaf9-e0c6-369c-998b-12dee5e9ad06 | -11.3179 | -46.77438 | 2026-09-18 00:01:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6864c9c5-9bcb-3f63-83e3-f5f3c6173182 | -10.8089 | -50.19864 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 69e6bdac-b512-3b93-9156-ae5a67f061ab | -4.41185 | -44.39272 | 2026-09-18 00:01:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1029fe32-ceb8-3015-a062-2ffd4c15ceb3 | -5.74251 | -57.58761 | 2026-09-18 00:01:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| da0ff070-1852-3f12-924b-1ede3ca5c7e3 | -8.9273 | -50.92879 | 2026-09-18 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7d1b691b-da93-3d73-bdbf-19c50add700d | -9.56069 | -45.44855 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6405773b-b4c8-3ad2-bfa9-b7af56614bb9 | -5.90609 | -53.56218 | 2026-09-18 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2bff8653-846a-3cb5-a5b1-444475253735 | -11.92042 | -49.76509 | 2026-09-18 00:01:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fc8de829-c279-342d-bf0f-382142a49fc8 | -6.41146 | -43.47425 | 2026-09-18 00:01:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 9fab4e49-6c08-3a10-85f1-c6b59849b131 | -4.43212 | -46.29926 | 2026-09-18 00:01:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5619d276-0d76-3764-b63c-6a9291684a90 | -4.36049 | -47.77702 | 2026-09-18 00:01:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a0ca5345-1193-3d50-8050-726e98651bc9 | -10.65438 | -50.49106 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| d0e66931-10b0-3f78-85b3-203bc0146fa3 | -5.75664 | -57.58576 | 2026-09-18 00:01:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| dac7b704-f8bc-3e36-922f-7474209f20c2 | -6.02528 | -51.81551 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 80b7babd-f23b-357a-a187-c3317b9f85ca | -9.71725 | -54.8087 | 2026-09-18 00:01:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 37f6f627-b376-387d-bafa-ba78829d2cc9 | -10.67102 | -49.04633 | 2026-09-18 00:01:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0c8f604f-9b11-3f94-8786-24ffd0eb3b9a | -8.78074 | -46.89309 | 2026-09-18 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ceac86c3-3e71-397d-8e57-5c529da94eb7 | -11.01404 | -54.15501 | 2026-09-18 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fdd79b74-d791-320d-bc99-daeeab435542 | -4.87875 | -56.07021 | 2026-09-18 00:01:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 3b3d0c3a-517a-3a87-b0f9-8c16f026d2de | -9.84255 | -49.18413 | 2026-09-18 00:01:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a36ee3a0-2d39-3548-9b13-ca08032a08dc | -5.89977 | -53.51369 | 2026-09-18 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 9d153297-cef6-3e0d-9d62-dbff287fa113 | -8.95273 | -51.47155 | 2026-09-18 00:01:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 71bbe7a5-5e6c-3925-8385-ff3207f554d7 | -10.61654 | -46.56673 | 2026-09-18 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 1e28a8e7-e34b-37a4-aa85-532a47c8e962 | -10.81789 | -50.19738 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ac251cf9-cee1-3837-bee3-c385010d879b | -9.91646 | -48.38791 | 2026-09-18 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 135a25cf-a32f-3da8-a479-6b175ea8ac41 | -6.46845 | -47.99926 | 2026-09-18 00:01:00 | TERRA_M-M | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 80431459-af09-30ec-9e5d-ce10b90967b0 | -10.51981 | -46.73384 | 2026-09-18 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| de4b3288-078a-3175-97db-9857a1f79272 | -10.49437 | -46.29097 | 2026-09-18 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| baa6306b-e041-33aa-baaf-9b8d7a52ce47 | -7.9349 | -44.84724 | 2026-09-18 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a7f09357-6237-3c82-8473-6040a17b5bf0 | -6.61582 | -44.19969 | 2026-09-18 00:01:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 0f2f6d87-70ea-31de-9079-ac4c512bc817 | -9.95535 | -45.68486 | 2026-09-18 00:01:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f7e23865-99b3-3849-a13f-9277265834f4 | -9.9076 | -48.38921 | 2026-09-18 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4dd095f6-b916-3c70-a5b9-202945647661 | -11.13094 | -49.04079 | 2026-09-18 00:01:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 19fc24b1-d5ad-3fbd-ab0b-2b710f8b2138 | -7.02176 | -44.66677 | 2026-09-18 00:01:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 22f3de54-bf92-3fd2-8694-e0b59ff23fb7 | -7.67027 | -46.09583 | 2026-09-18 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 5404de67-25bb-30af-a515-8f152dc92aee | -5.76218 | -45.09858 | 2026-09-18 00:01:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 132ffda1-7f30-3ddb-a707-ed19fcde2e9d | -9.95717 | -46.60389 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 73dac671-ba72-39d5-bfc9-df5ba5646f99 | -9.9429 | -45.32648 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9ccec70e-43df-3adc-896e-2a562d70d271 | -7.35073 | -44.63822 | 2026-09-18 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 2c4579a2-61fd-3492-a50b-34141f451b1f | -6.02399 | -51.80581 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a19fc045-bd00-3653-b00a-b57631f77852 | -11.06125 | -48.27582 | 2026-09-18 00:01:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 753fb2a5-2c64-3585-8e5b-c11a130bf927 | -8.84324 | -45.92325 | 2026-09-18 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b0cbcec5-9e07-32b8-b5e3-18efae20d1bc | -5.90135 | -53.52581 | 2026-09-18 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c3208a54-6d3d-30d3-a32f-d1dfc5d45abc | -5.18062 | -56.18079 | 2026-09-18 00:01:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| a714f6b5-6614-3bdb-b51a-d2950c1e27ec | -7.46213 | -46.83998 | 2026-09-18 00:01:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 779bc930-87ed-3401-a294-998fb77508bf | -6.61036 | -44.20683 | 2026-09-18 00:01:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d439dc8b-dd00-311a-9b02-00919503dc09 | -9.72395 | -54.81449 | 2026-09-18 00:01:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6d0791d1-f71a-3121-aa49-2e5429165596 | -8.46093 | -44.51811 | 2026-09-18 00:01:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c6549fb1-7409-3c10-b239-05e2e76560e4 | -7.0166 | -43.64988 | 2026-09-18 00:01:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 12cbbd13-2e85-3c09-807f-606816bb5024 | -4.01016 | -49.94829 | 2026-09-18 00:01:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 662305d6-08f5-3242-aa34-e03f630bea2c | -11.52609 | -46.87141 | 2026-09-18 00:01:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7b70fb55-04ee-3004-86a7-7e3a4a0b575f | -5.14144 | -47.60455 | 2026-09-18 00:01:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8923520b-40bc-3ef4-86a2-58cc69c5be50 | -7.00969 | -43.88008 | 2026-09-18 00:01:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| c12fc693-d2b3-31c7-a038-c620c920b1a5 | -5.88649 | -52.08597 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8bcd208f-1b7d-382b-b699-ffb7280e69a5 | -10.02083 | -45.50971 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 554a9d4c-d205-349c-b286-164ac1d1ca47 | -5.50067 | -45.51886 | 2026-09-18 00:01:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 28621a11-fa06-3dfc-a181-4b9aaf95af6c | -5.73261 | -51.75243 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 581d80b2-eff9-3334-baee-899860926170 | -7.62989 | -46.16899 | 2026-09-18 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9f31125f-382d-3d76-964c-6731765b0e4f | -9.94662 | -45.35123 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f30af467-5d5c-3a15-b518-2140c285fa61 | -8.78223 | -46.90338 | 2026-09-18 00:01:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ec0da471-d56b-3e5f-8507-09db35f914ab | -4.56784 | -42.92714 | 2026-09-18 00:01:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1ae7bf93-659d-35d0-86a2-600a7bec4746 | -9.70731 | -54.82774 | 2026-09-18 00:01:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4b06b562-e489-3adb-b0e2-15373d38530a | -6.63983 | -51.17694 | 2026-09-18 00:01:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 63b6164f-c654-3d5a-8e36-be0fdb32fb14 | -6.63857 | -51.16769 | 2026-09-18 00:01:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 3ada3167-5781-330b-867e-440711b8611c | -9.5542 | -45.47499 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a41247f0-1609-306d-b6b4-ed95fbdcf421 | -8.53409 | -44.54461 | 2026-09-18 00:01:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 22125691-90b4-3c19-bd72-ca9fb37f9c1e | -5.74331 | -52.25092 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 6a22aea6-57b0-3029-a014-1497404b72eb | -10.99433 | -48.3133 | 2026-09-18 00:01:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7aae208b-0154-3cb2-910e-eacbcdfcd108 | -11.66831 | -54.45755 | 2026-09-18 00:01:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a54f8c21-1013-38b1-b40b-5d31b90a1080 | -4.40574 | -44.3819 | 2026-09-18 00:01:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 82c2319b-380e-3391-8905-08793d8d1f1d | -9.5574 | -45.48074 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3ef5467b-b869-32be-a714-5e4f7fd0080e | -9.95506 | -45.3372 | 2026-09-18 00:01:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 01324707-3bff-359b-b297-5efbd7722756 | -9.91797 | -46.53523 | 2026-09-18 00:01:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3308b7f2-1e98-378a-855d-2607bdd2444d | -7.00133 | -43.63324 | 2026-09-18 00:01:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 632997cd-fc2f-3411-9681-c26a964415ad | -10.6347 | -50.27316 | 2026-09-18 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 7be5af89-e97b-3fa1-8fe5-2f5855ca9024 | -5.58084 | -48.10957 | 2026-09-18 00:01:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1f38ef82-f1e1-3884-82b4-4fcdf714a367 | -10.11325 | -45.64286 | 2026-09-18 00:01:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |


[Clique aqui para ver as próximas entradas](README3.md)
