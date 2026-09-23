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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d125dca-3b4f-3832-8928-832e7f01c8f3 | -11.8867 | -45.7852 | 2026-09-23 00:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 9902841f-4205-3fc2-9d80-2372f1624991 | -8.935 | -61.495 | 2026-09-23 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 450d3f57-c9b5-3128-8f23-f8e1a71360c3 | -8.8463 | -50.4804 | 2026-09-23 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 18a7f3ce-07ec-363b-ad42-6f59c616ed10 | -9.9436 | -48.4827 | 2026-09-23 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 0904ee46-1a0f-31f3-be13-59b1b4a1a95e | -6.789 | -48.6779 | 2026-09-23 00:00:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 33b803db-6b3a-3568-84d1-1f7dbfa978bc | -5.3451 | -45.1803 | 2026-09-23 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 3fd0fe75-8eeb-3c64-af5f-3059db02b6a6 | -15.6574 | -43.527 | 2026-09-23 00:00:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 33a9e205-ca98-3c0d-81d4-10d2b8a00fb0 | -12.478 | -47.0145 | 2026-09-23 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 77e9136e-cc02-3556-b2db-0bbdbd18abb5 | -6.1109 | -57.684 | 2026-09-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| fe400734-3234-34ca-b19a-7256cd84dc11 | -9.9516 | -53.9844 | 2026-09-23 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c83b7a6b-e956-362f-bfdf-3c4f02bad56f | -6.6332 | -59.9073 | 2026-09-23 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 660327e8-8732-3bf8-8f15-b0466998bc26 | -3.2314 | -46.9376 | 2026-09-23 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 3d13049a-7265-31a7-82e6-0cf9d51636bd | -5.3453 | -45.1576 | 2026-09-23 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 99e28840-ab2e-3da9-b12d-2b2df7cf8ba9 | -3.2128 | -46.9602 | 2026-09-23 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7089ad16-89e4-3409-b192-2a5abd774d5f | -5.6246 | -45.2518 | 2026-09-23 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 84a4bc1b-55bf-3bb6-a5ed-6de3316279f0 | -8.4538 | -48.6944 | 2026-09-23 00:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 7db5c5e4-133f-3bfc-8f6b-1faba2a47ee4 | -6.3293 | -43.9411 | 2026-09-23 00:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 9fb85edc-254d-32a7-ac50-b3a1e8bad23f | -3.6947 | -60.5645 | 2026-09-23 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 0989dd53-725d-3838-96c2-59642ba4e899 | -6.9216 | -46.5441 | 2026-09-23 00:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 174.8 |
| df35b817-d930-396b-8610-664c9dd3c9a5 | -9.0839 | -61.4308 | 2026-09-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 849f5a2f-34c2-3887-8fb4-5feb1f364d48 | -15.6376 | -43.5312 | 2026-09-23 00:00:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 76.1 |
| c6d43327-cb5e-3adb-bc3f-caa06a063543 | -6.6816 | -55.0502 | 2026-09-23 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 50b45b73-be4f-3536-9624-97002729d0ae | -4.0925 | -62.0874 | 2026-09-23 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 0f220dab-d3ac-365e-a45b-ef54ef428856 | -14.6307 | -45.617 | 2026-09-23 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 44432b07-653f-3afc-ac15-461bc6e51fff | -8.5982 | -54.6341 | 2026-09-23 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 17fb7d49-24a0-39e5-bef7-4b32690103c6 | -3.6764 | -60.5649 | 2026-09-23 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| cca35ccf-33b6-3195-b058-71b8a2ef7a25 | -8.4985 | -57.6075 | 2026-09-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a6baedd5-1683-3fce-b107-7f576a3019c7 | -6.7464 | -59.4223 | 2026-09-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 18687b71-ad17-390d-b3a1-6517aa07c5c3 | -3.4598 | -59.5591 | 2026-09-23 00:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a4c2c255-7e0c-37dc-8f32-99aab37521c5 | -9.9625 | -48.4806 | 2026-09-23 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 2a0adb5c-d36d-3688-8d52-6d1321e5c413 | -6.6129 | -43.7317 | 2026-09-23 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 17438900-6cd0-32a2-b33e-7a3934d27f08 | -8.4726 | -48.6927 | 2026-09-23 00:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 1a261f09-cf95-3df4-b14f-98d21185fca3 | -14.7475 | -45.6191 | 2026-09-23 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 8f101ba6-624f-300c-8853-3d0fda68f004 | -6.1111 | -57.6645 | 2026-09-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 4e312ef1-5030-3c58-92c4-dd82f87e81f2 | -14.7279 | -45.6226 | 2026-09-23 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 30c14b6f-77ff-311e-b90b-17f0cd560a5c | -5.7565 | -45.1293 | 2026-09-23 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| eadf4315-84f6-3ea4-8560-898f2acb0534 | -5.7754 | -45.1053 | 2026-09-23 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 77a9e02a-3fc9-3cec-8ac6-8127dc925133 | -10.5087 | -44.8748 | 2026-09-23 00:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 108241b2-525d-3fdb-98ea-40e841e9f8d1 | -13.0109 | -50.5898 | 2026-09-23 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 1162f547-6086-3a00-bf85-5453fa253c77 | -8.8275 | -50.482 | 2026-09-23 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9a8efe24-eb46-3ddd-9bc4-8cd29ef1f47e | -3.6763 | -60.5839 | 2026-09-23 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 1b640624-26a3-315c-bb48-2b2e72718ad0 | -14.6302 | -45.6403 | 2026-09-23 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 8580c83f-ad59-3207-adad-63fa6b76013e | -3.2129 | -46.9383 | 2026-09-23 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| d2a72409-5ad5-30c8-be53-ae1b1ebe06e8 | -10.6094 | -53.9902 | 2026-09-23 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 3c8f64d9-0d0d-3197-bc40-3971c54bc18a | -14.9599 | -47.5274 | 2026-09-23 00:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f0652532-987b-3d6d-9cf8-ffea0236f26b | -8.2062 | -54.7207 | 2026-09-23 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 05b60118-b690-3741-b316-de45be986b82 | -6.9214 | -46.5663 | 2026-09-23 00:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 209.2 |
| cf3a69c6-48e6-3ecf-936b-c496075fd2b4 | -6.9018 | -55.3387 | 2026-09-23 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| b20ccf81-bea8-3d59-8b72-807441d5b95a | -8.9165 | -61.4767 | 2026-09-23 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 46fa6d46-377a-3c16-868d-d3b1603c9a40 | -6.467 | -59.9902 | 2026-09-23 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 82a0bec3-da53-3af8-98ca-775292aabbbe | -6.7279 | -59.4423 | 2026-09-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 6938420c-0bd5-39ee-9796-6ee07cfe9674 | -3.2313 | -46.9596 | 2026-09-23 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| eba67fde-a1dd-37a9-908a-b2d3d3f8489f | -6.7213 | -44.1387 | 2026-09-23 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 05a6cc11-68e9-39a8-9617-cbef428af6bc | -6.9403 | -46.5426 | 2026-09-23 00:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 1f276400-3c37-37aa-a716-c8af2f18bca7 | -6.7211 | -44.1618 | 2026-09-23 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e362f952-3939-3b77-a39f-3cc3c1a1a0b9 | -6.9401 | -46.5648 | 2026-09-23 00:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 056bfa95-151c-3299-a9a6-f46f8c2f4470 | -6.6331 | -59.9265 | 2026-09-23 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| d11fbaa9-c524-3655-add5-e2ed019afbf6 | -8.1876 | -54.7219 | 2026-09-23 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 15fc6d59-39c9-3d38-bd69-572e1921b7c5 | -12.4788 | -46.9694 | 2026-09-23 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 0b382876-5c03-3c2a-8983-3f919256c692 | -14.7289 | -45.576 | 2026-09-23 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| abaebf78-b7ba-3d8a-a7f5-3ae148213849 | -9.0838 | -61.4499 | 2026-09-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f43d9e35-931f-3dba-9558-13f962e2862f | -6.3295 | -43.9179 | 2026-09-23 00:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| fcdf7e62-d6e0-305b-96ac-764f762dee2d | -6.6315 | -43.7533 | 2026-09-23 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 2d38eb01-d1ba-3f4c-9902-b29ced2e96a6 | -9.1025 | -61.4299 | 2026-09-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 79f8be97-4e09-3e04-acfb-5a2be5911e3e | -14.6297 | -45.6635 | 2026-09-23 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e7224e02-c67b-312d-95e6-5d726457b3f4 | -7.8811 | -61.1779 | 2026-09-23 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 5d32aebf-bfca-362e-a71b-06b3a24cdd58 | -14.748 | -45.5958 | 2026-09-23 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 474d9453-3a25-340e-be61-a5c6653bb5cc | -3.4781 | -59.5588 | 2026-09-23 00:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| a00bd815-ca05-3423-91b3-f97f04aa04ba | -3.4597 | -59.5783 | 2026-09-23 00:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f54b9e9a-a9e7-3b4d-8bd1-b2fb12b26cb3 | -5.7752 | -45.128 | 2026-09-23 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6b2efb80-9528-37cf-9556-cd52c58b27ae | -4.0925 | -62.1062 | 2026-09-23 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 2f2b9096-ab8b-3a91-ae42-386d90853a03 | -5.3639 | -45.1564 | 2026-09-23 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 22c3d59c-ca5d-3f62-90a1-fcc4ae66ab8d | -8.9351 | -61.4759 | 2026-09-23 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 0e6601c2-21b4-3486-a7b0-d2adf1d09842 | -13.0106 | -50.6114 | 2026-09-23 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 4d3f8ef1-413a-344f-a57d-4d3159c710ce | -4.4488 | -55.0662 | 2026-09-23 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 83c07118-bf2f-3dc1-ad76-421b61cdcb3d | -3.478 | -59.5779 | 2026-09-23 00:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| c278be3e-2cc8-3298-b4ed-163a2e1a5efc | -6.6146 | -59.9272 | 2026-09-23 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b19e4fce-2372-327d-8891-bea02f18e41c | -10.6097 | -53.9697 | 2026-09-23 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 44c433f4-4a6c-397f-a1e9-2b7a7a7ae28f | -4.1108 | -62.087 | 2026-09-23 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b405ebf8-aa0e-3f96-918e-be9dcfebb437 | -14.7089 | -45.6029 | 2026-09-23 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| f2510a66-4c6f-33ed-a83a-120f2874168f | -6.728 | -59.423 | 2026-09-23 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 91ab5bda-eccb-3246-8f8d-6f2b193d23b4 | -10.6283 | -53.9885 | 2026-09-23 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 7b93e322-6a92-3417-ae28-c697c06a638a | -6.0925 | -57.6847 | 2026-09-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 386b4213-2657-3612-9275-bcaefa59ebc8 | -12.4212 | -46.9777 | 2026-09-23 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1b69e159-b13d-3828-b42f-7be6e0ef9f99 | -6.6776 | -58.5554 | 2026-09-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d1b9242a-ae1b-3a15-bd6f-d7b92d67fc57 | -6.1289 | -57.7613 | 2026-09-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 6aa22d05-baba-3d0e-93c2-f89d66f09329 | -11.8675 | -45.788 | 2026-09-23 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 8dd42124-2b6b-3af3-9413-42f2d21c68e9 | -3.6946 | -60.5835 | 2026-09-23 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f100e03e-1b39-3f53-b3d4-11f41705bb83 | -8.9164 | -61.4958 | 2026-09-23 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 100.8 |
| bffa41a2-be10-310b-8d3e-58e07af23d36 | -10.5091 | -44.8517 | 2026-09-23 00:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| c51cb767-8b2b-3008-b5cc-32bde281151d | -5.7567 | -45.1067 | 2026-09-23 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 203.5 |
| e6d1001d-ac2c-3eed-971b-d392656a1c37 | -14.7284 | -45.5993 | 2026-09-23 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 201.9 |
| d499567b-9ed2-3dad-8a74-b71fd5aa928c | -7.0349 | -44.6625 | 2026-09-23 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 31b31a66-9bbd-3aff-b500-f63b8d0c57cd | -14.6497 | -45.6367 | 2026-09-23 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 0250a7d2-1d00-3ec5-aa31-cf924c2929e6 | -6.6127 | -43.7549 | 2026-09-23 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 82586674-7d24-346f-ba81-197ccfc26aa6 | -6.6148 | -59.908 | 2026-09-23 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| d140fc34-0d5f-3496-9f92-a784542d1e79 | -3.8648 | -58.8211 | 2026-09-23 00:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e9fcd9db-628e-3de1-893a-f4bcf70360d9 | -6.6775 | -58.5748 | 2026-09-23 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 709eeeac-b7b8-3803-902b-d20e7b4e73ab | -12.4216 | -46.9551 | 2026-09-23 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 8b74d82b-a072-339d-9ded-9e9df78766de | -6.0926 | -57.6652 | 2026-09-23 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |


[Clique aqui para ver as próximas entradas](README2.md)
