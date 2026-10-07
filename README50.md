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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec140086-67fe-384f-9aa2-ae27bb2ff636 | -5.24353 | -47.93949 | 2026-10-07 04:19:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f77e93d7-2913-3739-a8ec-8175147459df | -6.92519 | -43.67327 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abd913ec-d285-3b7b-9351-01004255f095 | -4.24652 | -50.73494 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b9956a1-6220-350f-a0e1-09e6c78d0d42 | -3.04631 | -53.93487 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04477d89-be11-3cf3-80f0-299e6e72842d | -2.1515 | -51.97743 | 2026-10-07 04:19:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bf748f4-0b56-3f7b-83b7-d3387c05a28a | -5.23511 | -48.39555 | 2026-10-07 04:19:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb248749-ba9c-346c-863d-b736292a6eb1 | -3.98231 | -56.22974 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65623f8a-e79a-364d-af42-54cb2fc6a092 | -8.38779 | -46.28398 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f700bdf5-af7c-3f37-b2c7-4d3e7ca580a1 | -3.27851 | -53.86547 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fbe750d-a425-31a2-89ca-6b1959963d99 | -3.08594 | -54.29042 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 53575eb4-5e46-39a6-8e90-8b5785bd37de | -7.83351 | -44.17887 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5f51a518-8186-3f7e-904c-45dec88d3303 | -2.96151 | -54.14585 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e70444c9-f093-313d-ac98-582f7df35398 | -6.59949 | -37.89322 | 2026-10-07 04:19:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e2d25ae4-2ef3-3c9d-a8a9-ac15d25e1fb0 | -2.97441 | -54.12926 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb0a54cc-d45d-3342-9981-55d9251f7bef | -3.16403 | -50.43962 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8736922-5bd0-3428-bc81-63f7fd7978a5 | -3.85636 | -55.98462 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 25a43036-9bb7-3051-95ac-eb8bb19e4b30 | -3.86099 | -55.99868 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0d5c889b-9127-39b5-94d3-0fce96bda7b5 | -7.87273 | -44.21022 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 93d39b7c-639f-314d-a3d5-33d2f139e371 | -2.98737 | -54.05463 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe647e55-87e9-32f6-b424-79fd40e3b94f | -6.73308 | -45.80664 | 2026-10-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36583386-8eb9-3f52-b754-ff8c9b72ab9e | -5.23875 | -50.91326 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49dd240f-af1b-3931-b234-0dd8dddc074e | -3.68364 | -55.95915 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffeb5488-f683-3838-b86d-c1857efeb042 | -5.8351 | -42.42451 | 2026-10-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f7761915-39d9-38f9-b6a4-91072313ab2f | -3.02407 | -53.91634 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 77861d59-9eed-366f-a671-9849df285c2f | -3.08414 | -53.7135 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ecca196-b302-3bf6-9f26-9470e6dbfaac | -5.01403 | -50.94555 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c138906-45e6-3411-98ed-5f414b475710 | -3.23849 | -53.87785 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e055601-fc20-3e3c-a499-7def59e99884 | -2.96356 | -40.39782 | 2026-10-07 04:19:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 38847dab-6c1e-3c18-9980-b0284317d152 | -4.93672 | -45.66949 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7078f89-153b-34d0-8d5a-9c4b5e72e98d | -8.20773 | -46.34407 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04a66cc7-2876-3a23-aff7-e05ff5e34f96 | -3.85293 | -56.00397 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 83525aa4-9662-3455-a266-d153d44fcd7b | -3.09312 | -54.28644 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 565c7651-8440-3abe-b422-b840c1bb6fa5 | -3.17894 | -50.57378 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7bd66c34-e320-3595-a561-4fbbd3f2f06d | -3.02859 | -53.92701 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2914dd9-d649-323f-ba17-ceb95c28bf0a | -3.08681 | -54.28536 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e9ef7aa9-ad49-3c03-8ea1-3709e8b4638b | -6.35386 | -42.53832 | 2026-10-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6a39b51-352c-3166-8ed5-adec90e59c75 | -3.27491 | -50.14668 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 065b2353-6755-3bf6-b173-0d68007cade0 | -5.74215 | -41.65332 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 09e2a8fe-d1be-357f-a673-08f3964fe008 | -3.50957 | -41.94278 | 2026-10-07 04:19:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 163b917d-f738-3b5a-a7be-480e9c9a0572 | -5.97028 | -41.35955 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 854efe14-eab4-3bb1-8e8d-47e2b0379d4c | -4.44262 | -48.34227 | 2026-10-07 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31b7cb02-de10-3100-a99c-7d3838fe440c | -3.10061 | -53.76429 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb6ac0d5-28d2-3662-9c02-05485f083125 | -3.67102 | -55.94992 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49c5c2d6-756b-3eb4-a2b8-bdeba8489622 | -5.24072 | -50.91491 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3fd1b8c-862f-3ed7-9044-5691c3dd441a | -3.03189 | -53.90784 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 99d22b8f-9cdf-32b6-9e90-0b34d668d514 | -4.11823 | -50.82594 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1242a200-09b4-335a-93cc-dd6dd65fb458 | -3.09633 | -53.71553 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a598754e-a300-3302-a95f-51d0ae0c3fdc | -3.26973 | -54.06591 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 601eb086-5bbd-39b5-9b43-f8cec04a5094 | -3.13917 | -51.03072 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edd6ce55-74a9-3ccf-bb3f-bc77a4789595 | -3.27796 | -54.01743 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f177ef43-d8aa-38a9-a4b5-4d2c3a502509 | -4.25071 | -46.38118 | 2026-10-07 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cde6c7b0-97b4-3dbd-b736-439f8e674667 | -5.57419 | -48.99127 | 2026-10-07 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50c6633c-4ae8-34ba-8c00-0485a54e4bd8 | -6.44444 | -55.03042 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b79a9c0-5cf3-3b21-a685-301487697e62 | -5.74102 | -41.66054 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8493bc7-a418-3b3c-820e-96e6048b169d | -3.84996 | -55.98158 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| eb10a630-f4ae-3f8d-98f3-531f4bd943c0 | -3.49824 | -51.69352 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20e03dd5-b977-3da5-9ca3-970c01721b99 | -5.75159 | -46.68108 | 2026-10-07 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e0c7871-98d3-32ce-b4d2-5da445a203ff | -4.7598 | -55.66257 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64ecff11-faae-38e4-8e78-7f57332a7e99 | -4.55494 | -49.35234 | 2026-10-07 04:19:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9369e859-e5f9-383a-a253-3399baf068ae | -5.97483 | -40.92506 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0fb240a3-dd75-35e9-a4fc-43c51cc04131 | -4.29553 | -43.01048 | 2026-10-07 04:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7287776-6c44-3446-bef4-b8f5c42295aa | -3.27317 | -50.43097 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70f81da7-7ace-3f60-9c93-c1e2c58df628 | -3.47059 | -50.09212 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 18c95f2d-48e1-34e9-8ab9-fc320404ba80 | -3.5382 | -50.10082 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 033269ec-603e-32af-90fa-73e971e2c188 | -1.20997 | -49.04264 | 2026-10-07 04:19:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a9ff200-6a73-357b-9be3-3f0b8c77cab3 | -5.89154 | -45.54442 | 2026-10-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dfe994c3-0bcd-3f16-a272-512171a0f36d | -6.92353 | -43.66236 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e2ffc30f-8573-30c1-894d-4400f86430af | -1.59158 | -46.21334 | 2026-10-07 04:19:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff731f3d-f63d-3cdd-b892-9e29f49ad990 | -4.32373 | -43.81577 | 2026-10-07 04:19:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96d5f9f0-4f3b-357f-8333-1b1ec1be6663 | -2.95446 | -54.14946 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 041a59e9-9400-34ac-a65d-d1c6ce0c9389 | -3.32317 | -54.19186 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcecc12a-9804-3a99-abd5-d9224606e8f5 | -3.57663 | -54.31916 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7bf48d2-5ffb-3765-ab77-ba5e7d4f6131 | -3.0193 | -53.91383 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 50a8b72d-52c0-330b-9c6b-ebfa44ef7ae9 | -5.01268 | -50.94402 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7003a4d-8833-3fbb-bb37-782e1f767f97 | -3.5059 | -54.63852 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f2ef9fd-cd9a-3af9-9d10-1ae34abc7e7c | -6.60006 | -37.88935 | 2026-10-07 04:19:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04af2a84-4570-3f43-90dd-ce26640220e9 | -3.23966 | -53.87394 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 761d3dc5-7a94-3291-89c8-bdeface3f897 | -2.99757 | -54.10706 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 003b2cf7-7902-30c9-b6a7-c49be69288e7 | -3.09942 | -54.28756 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 902bdc6f-88d0-3ea1-8124-a3c4dbfd4477 | -3.04746 | -53.89108 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b50a217d-9f5f-3abd-b196-271c3f5e9e3f | -3.03887 | -53.90419 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b57029d2-e463-3c90-aa0b-b9d491cf5e34 | -2.59449 | -47.35553 | 2026-10-07 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b722888a-c899-37d6-b1b0-b31c20190d81 | -3.51232 | -54.63952 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a3e11d95-fd47-32e1-8ed4-e9c839608bd9 | -2.6093 | -45.11845 | 2026-10-07 04:19:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94a3d7ff-9206-3b1a-a2d3-e1ac524bfd18 | -5.02094 | -45.52923 | 2026-10-07 04:19:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e075f0b-7911-3122-abe1-9ad60daf6427 | -4.13918 | -46.83372 | 2026-10-07 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7114be4-4560-3c6c-889c-631e1d28dc63 | -7.42236 | -46.71117 | 2026-10-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 351b4200-2be0-3935-be68-f27f7b48b7b0 | -8.6193 | -43.98072 | 2026-10-07 04:19:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30a12729-6a56-3867-9314-93f779686cdb | -4.35618 | -47.78248 | 2026-10-07 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e6bb494-707e-35bf-86e3-13c6157dfbf4 | -3.75002 | -47.14957 | 2026-10-07 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a700e484-9990-33fc-8381-555bec19c993 | -3.04711 | -54.27178 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dea868d-0d8d-3f84-afc2-f92a32083d62 | -4.03003 | -46.98174 | 2026-10-07 04:19:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c72fde50-2797-3a9f-a76b-d0d48e272d9b | -7.99227 | -45.50082 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4ca436b-9857-3ac2-9403-17d9ea0bc7c4 | -3.57387 | -50.35832 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e88d9ef9-89b9-3e8c-ba6e-4f23cd9634ec | -2.98894 | -54.05836 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec1cde34-f58b-35dd-90db-932c4ee42edc | -2.77192 | -54.11795 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 18f573be-da49-3cd8-bf21-a63b99394f92 | -7.8639 | -49.60749 | 2026-10-07 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0f1a36b-0bfa-336a-a392-688a758db2dc | -3.16978 | -50.43518 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec1c385c-6803-3631-931e-43c33dc3a9ca | -2.93693 | -54.17694 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 83d5da4b-509e-3301-98a8-142f0e61191b | -3.09855 | -54.29261 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |


[Clique aqui para ver as próximas entradas](README51.md)
