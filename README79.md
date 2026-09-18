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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be1c6731-d73a-3ea1-b042-85685bfc0260 | -7.67426 | -46.10409 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d490cbb4-14c6-32f6-ab1e-54896852f460 | -4.35617 | -47.78036 | 2026-09-18 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a22a87f2-ceeb-30b6-9783-b1841db17ff2 | -3.44001 | -58.21068 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0bce12a-f226-3410-af8d-d80221422baf | -6.43259 | -47.25135 | 2026-09-18 05:16:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ed119ea-f23c-3890-b8d7-c4a70f2bb09a | -3.3791 | -50.45191 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f63c56e-34d2-3463-8676-0521de4adc3f | -2.81337 | -50.47715 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f4d6fb2f-e230-3201-8715-b01ef884f47c | -2.75089 | -57.62922 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a74fd5ba-80de-357d-ad03-428db9aab3d6 | -3.21111 | -53.95007 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0484127-30e0-38d8-b178-8b9e37014f14 | -7.79385 | -44.90749 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 78df7c0d-5d8d-3056-9aa5-a92c33ea3bb2 | -4.37725 | -55.03104 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eb61b32-fe96-3be6-830b-f9b25575f777 | -2.49469 | -49.41493 | 2026-09-18 05:16:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f36b16a0-1514-34e1-b14a-43d9f0bf49e2 | -1.78945 | -47.83467 | 2026-09-18 05:16:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75d6f968-ad9b-394f-bcf2-f7829f3453e9 | -5.33388 | -45.1436 | 2026-09-18 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08a17cc4-4728-38ca-99ea-7ac1e5d92ac9 | -2.91207 | -54.1753 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5115ef8-e070-3055-a6f7-58de44c2234c | -7.65578 | -45.83597 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef861918-07d1-332e-bd11-3b1407c7c13c | -2.8274 | -50.47337 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c03773d6-fd89-33f9-8133-97d9a2d3ce43 | -4.55365 | -54.92967 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7354b001-0c1d-34bc-b5b5-f1d7dc3c510f | -3.3709 | -50.452 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87c3217c-bf79-3f99-8b2b-8a1e289bfe36 | -4.88459 | -56.06008 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9c1fb51-f906-36c1-85a1-36b58ce47bf6 | -5.89467 | -51.65438 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c61cd9c3-cb5a-3993-bc61-5decb81a6c03 | -2.2983 | -48.58478 | 2026-09-18 05:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a3ab33d-93a2-35ef-9cab-e6def81c630a | -6.45457 | -58.16 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7f381fe-544f-3c03-893b-7654e688dc44 | -3.33047 | -57.84995 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38edcbff-1ede-3173-9083-fd2d19169b7b | -3.46785 | -54.71077 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d9e2712-be1e-3d3a-bda3-a4ddc5c12cbb | -6.66257 | -50.90234 | 2026-09-18 05:16:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c1def16-2050-38d1-9f72-55f525087299 | -7.80063 | -44.90852 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09bb907c-e6c4-32ab-b058-33fe2d0f5a07 | -2.81737 | -50.48042 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9bd55aba-cfc8-377c-87a8-54d77e3a7790 | -3.59882 | -59.06349 | 2026-09-18 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a302ed-6885-331b-8b21-cc9585eaaa43 | -1.38091 | -49.36882 | 2026-09-18 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62af8a64-5775-3f5c-ba06-60d772071784 | -2.6125 | -54.7541 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 690d10f0-2a89-3ac6-bff4-5a499625fb67 | -2.36695 | -55.24547 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e28a99f9-7120-39bf-88f9-0140fb78ccfa | -2.8272 | -50.47499 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ed45905b-de7c-359c-8d8f-83001c8a039a | -3.33213 | -57.86099 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7dce878-46bd-3d1d-a279-33c008d42ad4 | -4.3801 | -55.03533 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddad8ae1-dd5a-32ab-a5d7-7d824efbce28 | -4.49584 | -54.85474 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbba76cc-d3b0-3ba0-be43-afb64f2d3168 | -4.49122 | -55.4897 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9581c43-3e1b-33a7-ad77-357064c2e3ad | -4.44095 | -55.52276 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6af92dfd-4e6a-3f8f-adce-2f7d08bbf4fd | -7.80374 | -44.89855 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64764ec3-691c-37b0-9465-9c5f4d71f3f1 | -4.5334 | -54.96922 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecf7ef07-f776-3b1a-888c-da0c06820c30 | -6.45808 | -46.01551 | 2026-09-18 05:16:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 604f6dcb-6392-3b77-ba90-f107d565d848 | -6.10426 | -57.62819 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dd61f4e-e542-3aa9-a03f-90379c2bb9aa | -5.7583 | -45.09741 | 2026-09-18 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| db72b6e9-ec9e-3cd1-bd74-99edb48bbf27 | -1.70561 | -54.88639 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69ac4371-5385-3935-b11d-ff9bd434c4a5 | -2.8136 | -50.47554 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 553111a7-4b32-3c9e-94a8-0a6e7a86bfe6 | -6.14182 | -57.69082 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1df73e38-b369-307d-ab2b-933a608e9605 | -5.14267 | -47.60118 | 2026-09-18 05:16:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0750fc6-b213-36d4-a8f0-0345833a2e47 | -4.43294 | -55.0773 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 950bd5c5-9d3a-325a-9c13-77879106e6f2 | -3.81475 | -58.89766 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfd47405-8ccb-33bd-bfaf-56737de0762a | -2.8986 | -54.16918 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c023c36c-d673-3122-94e8-55decddebca8 | -4.51136 | -54.98182 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f2e0977-e459-35e4-87a2-57e7c614d6fd | -2.81711 | -50.48203 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 77f2c631-43ea-3646-a09e-d2e500e0a56a | -2.96675 | -52.13369 | 2026-09-18 05:16:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee568954-5fd0-3f6c-a39d-63e849a75658 | -1.19712 | -54.2168 | 2026-09-18 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd534186-dd44-37e3-81dd-5ee5de073127 | -3.7307 | -60.59803 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fda8b2b2-73c9-35a5-9406-f4609c99785e | -1.70184 | -54.88239 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1765119c-71a4-3f35-a775-24c7f7352cfd | -3.54448 | -53.99453 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8beb637-1067-306a-a2ea-12311e7c4237 | -2.69761 | -57.59936 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3162b704-93e4-3261-ac9f-ff716b252e8b | -0.53895 | -49.14137 | 2026-09-18 05:16:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d26a3db4-d583-379d-8620-7f4a1adf2de8 | -3.37401 | -50.45564 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 719cee31-5790-3c07-b9e8-38aa58fe65df | -2.7026 | -57.61088 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1aad30b0-4304-3b70-966b-c595190a179a | -2.63283 | -51.70803 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4694fd95-24dc-3d9c-afa6-332547b93dde | -2.60907 | -54.75357 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25ab03a2-7354-3974-bd39-1d570b899766 | -3.20489 | -57.84781 | 2026-09-18 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09a586ff-982d-305a-a98b-1abcfc549aed | -3.37158 | -50.44761 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4727bfa-3bbd-3068-bb65-68009903355e | -6.11981 | -44.03342 | 2026-09-18 05:16:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| aa68cc43-9302-3643-99d2-b50dd1105eca | -4.42853 | -55.51334 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee6b5b44-30ea-3bb5-9d8a-62b46e0b338f | -4.51674 | -56.08678 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75f7f79c-e4b8-300a-b085-5eb6d756aa22 | -4.5682 | -54.90437 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 201cb9ad-1403-34c5-8e05-9e7d23497886 | -4.51195 | -54.97804 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f380b49-1006-3baa-91a3-1289cc14be9f | -4.427 | -55.51705 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aede31c1-3db2-3dc2-bee4-e0a521363bd4 | -4.71226 | -55.75277 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 330f7462-afaf-3844-a414-e23c7bf7f8ae | -4.51086 | -54.96247 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c85c473-635b-348f-88ab-865f8dcd030f | -3.43891 | -58.1959 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68e79f4f-b96a-3824-8e99-f31b69adf5fe | -4.47684 | -54.97652 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b45b70a-782c-3215-b496-fb0445dbf7be | -3.25836 | -57.49174 | 2026-09-18 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aabca5aa-4604-34c0-bcd2-d7353914ce22 | -3.49727 | -51.25133 | 2026-09-18 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b19196f5-3262-3f0e-9f56-93382dd3eeb9 | -3.37 | -57.70922 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92b485e4-f846-3726-b456-ac7aa1f0e48e | -3.81876 | -58.89451 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c3369d0-6d36-331a-b821-dfa92c017bcb | -3.47836 | -54.70338 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bf5150b-c48f-30ea-aaf0-0661afbccb42 | -2.81485 | -50.4671 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 3dcbc6d4-688a-36f1-8419-ca82cc81d767 | -2.36191 | -55.23368 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ee7e301-558c-3e08-a809-7566c49e734b | -3.36784 | -50.44252 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e5d14cef-a635-3e23-a5d5-1c943ed4857b | -3.92307 | -55.75931 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83105960-7fd7-3e69-bbe5-a686a87720f0 | -2.89682 | -54.17784 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4b6e621-d586-3704-b92b-291df550c594 | -2.82655 | -50.47916 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7272111b-dba8-3329-a4e4-10be954465a0 | -1.49513 | -54.97598 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9ad94c1-bc0f-365e-9165-742d6bf1a306 | -7.68125 | -46.09987 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45e2dde4-d9cc-36bd-8998-bb322fca1f51 | -2.63227 | -51.71154 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbe4208f-3aa9-3f3f-98ca-890edd00dc4f | -1.70899 | -54.88692 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be5dc75b-1a71-3803-a1b1-88f5df77edf7 | -4.437 | -55.52588 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7248af7-5ebb-33b8-9794-e26dbabc604a | -4.79593 | -56.12241 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a14b200d-60fa-3623-80a1-b71d9f5211f6 | -4.5145 | -56.07924 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 983ce040-c596-33b0-b0eb-ce35fe4ff4f7 | -4.51255 | -54.97424 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48dec360-22d0-309f-8e88-cf104e1ca12f | -2.81403 | -50.47297 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 1a98770b-d01a-300b-84dc-8360bff316e7 | -5.8646 | -52.03609 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d7db92ad-bf4d-384b-b631-56482461515c | -3.69827 | -60.6107 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ade20926-85ed-3882-8c9a-5f349e16663d | -3.54076 | -56.88987 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b21580fd-26af-304c-8b45-bcc36bd784b2 | -7.22552 | -44.21466 | 2026-09-18 05:16:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66dfb5da-c32c-3116-901c-350bfa05a4d6 | -4.87956 | -56.07016 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9244ad3-5c82-39d6-aed3-a9d98a156ce4 | -3.92084 | -55.75166 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README80.md)
