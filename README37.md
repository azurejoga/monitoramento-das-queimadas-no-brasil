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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0417fb7-618d-36c3-acdc-8233e0a771c0 | -5.00893 | -56.09713 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a043d075-8d26-3adb-b042-05f617139991 | -4.68204 | -46.41755 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a48ba07d-ec77-35a6-9c91-19003a8075df | -6.92024 | -43.73269 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bc89906-3bf2-3647-bc8f-8a2f29b01520 | -6.54917 | -45.80006 | 2026-09-21 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91c8d513-7e64-3c55-bd6d-30ed533383cb | -8.79204 | -48.74834 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 77bda6bc-86f2-3373-89e7-3fae7348621f | -3.65952 | -54.26713 | 2026-09-21 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a009bf00-f120-32ce-bc42-6df52de6fe34 | -6.8355 | -46.04575 | 2026-09-21 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7d69c88-5035-3782-af05-388a650c642e | -7.42581 | -42.11567 | 2026-09-21 04:19:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3fd4d65-26f9-36c7-bb05-45206415356d | -7.02847 | -42.07683 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8ee8fc5d-a9d8-39c6-bd73-dacc632dfda1 | -9.45319 | -45.41213 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0c7250d-ce28-3a45-8cf3-365496fc9769 | -7.38101 | -46.03802 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5d85646-ddb7-3086-90e7-8f58f7c8468e | -8.76659 | -45.85382 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b87f8aea-9275-3414-a70f-b88302ee79b0 | -5.21133 | -56.1125 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df95326a-a26a-342b-ba42-541c9b19f320 | -9.44726 | -45.38498 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f2c02552-e479-3a14-9a6a-bf4d9eae89b8 | -5.81795 | -53.51297 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4791d8af-39fd-31ce-b202-efe857069fdc | -6.87475 | -43.07572 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9050d1b1-aa71-35ef-bd2a-621ada377be4 | -6.69146 | -43.01127 | 2026-09-21 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8272eb66-2b3a-3d6a-a4ba-18a6ee649251 | -7.33003 | -55.6174 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea2634ea-408b-3732-8763-bad693d4c121 | -6.97918 | -42.17187 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e43aedf-eec6-3625-bcd7-700fe295f355 | -5.8737 | -53.6356 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a735707f-8623-3ea7-938c-d17e17d8b37a | -7.23838 | -55.61203 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4add4933-6d24-33c1-b826-28ebd707076d | -9.45439 | -45.40481 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6593672a-cb9f-362a-8cdd-60ca20ff1c9f | -6.35731 | -43.36251 | 2026-09-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7947d16-532f-306c-b01e-6e6505267067 | -6.1908 | -55.4488 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4379d8f-8e8c-3813-9663-5fc85d4f8310 | -4.11575 | -46.39723 | 2026-09-21 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09bcca61-7e18-3047-a753-30d26fdbd407 | -7.15262 | -39.33995 | 2026-09-21 04:19:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 95bed17f-0e85-3cfb-820f-c1b1b3b85ea7 | -7.58725 | -57.66754 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06161f4e-af70-317c-9712-fc613628235f | -9.44528 | -45.4182 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca3e12d5-4d78-3edb-a8ff-ca27a667b999 | -7.41671 | -44.76971 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 709167e7-cc11-32ca-9553-8f282f8f1748 | -8.30784 | -45.99838 | 2026-09-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9969761-8b63-32a2-8ac8-8bfa3c91ef7c | -3.01234 | -54.18725 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1dca233-2cee-34df-b5fc-1efea7888eb2 | -7.48469 | -45.47528 | 2026-09-21 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ee173e0-f4e6-374e-a7f7-6644a276876f | -7.4122 | -44.77631 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 09e993f3-d3a8-3a08-80be-54d885ec7662 | -7.41719 | -44.78808 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb1362d8-0660-3eed-946c-fc283460efde | -9.46627 | -45.39555 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c311b97-a247-3f6b-ab1f-7f782ed5a5bb | -4.59259 | -45.16064 | 2026-09-21 04:19:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de211a01-b61d-3c90-8fa7-5b59769b4647 | -9.43769 | -45.41353 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ec0a41b-3cf0-32f0-ab2e-2f89e38d94e0 | -3.00532 | -54.16973 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25cce8b1-7c12-3946-bfd2-598428126e69 | -8.77027 | -48.74348 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f0732fe-4c90-31e8-aaef-da2d3e19e736 | -6.82837 | -55.54336 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bfde0e1d-c2a9-3283-ba76-6af849500295 | -9.44864 | -45.41879 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4f0a6a2-1933-3c2d-b31e-bf692b57e7b5 | -7.55251 | -45.42526 | 2026-09-21 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98981ef6-b0ad-339b-be0b-f71d2f006c9d | -5.8972 | -52.09372 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97dfef65-627f-38f7-914a-99b3a3fc5819 | -7.24386 | -55.6181 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6591d13c-7b3d-383f-b089-b46807fd54fa | -9.46964 | -45.3961 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a44e996-c61a-3625-8d5e-cae274c8da1c | -9.46172 | -45.40225 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cad5022a-c563-370d-8328-528e2ccfab03 | -7.2473 | -55.59349 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87bf1105-82fc-35aa-8c1c-bd7126867b46 | -7.55298 | -44.94214 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb26e3f9-bc8a-3e7a-a4df-aa0569a92d9a | -7.28081 | -44.53982 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd72286-e38d-369f-bc42-651bf1affed5 | -5.8353 | -53.54893 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 027a614e-09f2-39e2-b56d-8d02153f8745 | -8.77693 | -48.74091 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d53bc3a-632f-31f1-81f1-5fae0d8c4c78 | -3.34755 | -42.76168 | 2026-09-21 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc8fa248-917e-39f9-98b3-0450289e1f59 | -4.34605 | -55.65963 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6e5d6c6-4e4c-3615-918f-4e436d2ff1f6 | -7.41278 | -44.77274 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5d080635-1d97-38a8-bb56-8f34f022bf3c | -6.19731 | -55.44963 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71764d0f-3c50-354d-9b44-e652d3ccf8c1 | -5.21024 | -56.11863 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 39d5f6c0-6f19-3df4-9312-88cf743b57da | -7.4262 | -44.77488 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 192655b1-cf91-3d8d-96c9-6862971e3734 | -6.7658 | -55.63187 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25474b25-f8ba-3673-8fed-0c7f5836e8f5 | -7.31751 | -46.77326 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 350a5070-7538-3093-9940-da044bc455a1 | -9.54727 | -46.57126 | 2026-09-21 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d3bd306-e3ac-3f35-a6a1-5be762b47080 | -2.99903 | -54.16877 | 2026-09-21 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc92583d-1014-324e-b68a-af55d109c228 | -6.9904 | -42.2101 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 64000b13-389e-33a3-a16b-68c3b534bef1 | -7.43349 | -44.7724 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0cbd9081-1c2a-3936-9ae7-3b3e9f1a394c | -5.85169 | -53.5234 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1a790b4-6ff6-389c-8fce-768aef8092c2 | -6.98207 | -45.81976 | 2026-09-21 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e58ba868-a415-3b55-8a7b-baef823310a3 | -8.30947 | -46.87093 | 2026-09-21 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf48b8f7-4b76-300b-abaf-447c9f4d6c3e | -3.38138 | -50.44101 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc1b6a33-6cfb-388d-81bc-28bee4c13136 | -6.03715 | -53.27883 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12b7cf8a-f238-30cd-88b8-47985dc105a9 | -6.91417 | -43.72817 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2a0c1ad-2c6e-3d1c-b26f-a4e4e50bd2a2 | -8.77934 | -48.73829 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 844bb5b7-2ff9-380a-bcd6-1f3229aa32e6 | -6.83595 | -46.04521 | 2026-09-21 04:19:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aed99649-ac37-3f5f-b6dd-efb06bb376e2 | -9.46905 | -45.39972 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62a3a11b-0edc-3264-8a7a-f7f6e632e430 | -9.3701 | -47.77721 | 2026-09-21 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a401efe-4f91-37f8-a830-13f64c4ca6d9 | -6.97281 | -42.58069 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c328f8c1-3008-399a-831b-e5b65b3ad5cb | -6.03399 | -53.28033 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a37407b-913a-3a74-a644-8c3513b66daa | -7.42112 | -44.78505 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c0a4c366-14d5-3294-8264-9973ebcbc1cc | -3.09769 | -53.17102 | 2026-09-21 04:19:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 58ec2a37-b82e-3f9b-bf85-b233c1ee9946 | -8.83405 | -50.48591 | 2026-09-21 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79599d1a-c89f-355f-8827-dacb26ad6a59 | -6.35676 | -43.36597 | 2026-09-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28e1c25e-00db-3ad7-ad40-c46a6749380b | -9.11018 | -44.70144 | 2026-09-21 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad2d8596-9ee4-3e88-8a60-f4a62c7e8f85 | -9.45022 | -45.43026 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5f44df4-90e9-3fb9-beef-191e5528675c | -7.76894 | -44.82259 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21e94ef0-9e65-34b1-bcd8-080c72faf804 | -2.82719 | -46.71212 | 2026-09-21 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c765ddf-5c0c-3835-9700-28399a936f0d | -2.67909 | -49.02109 | 2026-09-21 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af8b183f-2822-3fca-9901-aa6a9c369513 | -7.71129 | -49.38797 | 2026-09-21 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed74fc36-811d-322b-9354-38af332a8d4f | -8.77854 | -44.28767 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e2dae93-ff7b-3957-a76f-a0e656aeac5d | -8.7782 | -48.74508 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16b83e38-e2af-322c-bbcb-2930bfb51497 | -5.2047 | -56.07836 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05076b77-83bc-3fa7-81d2-8a2b0ecba7a1 | -5.80541 | -52.09402 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10d272c1-ea6f-35a0-a400-b91ca2371b56 | -6.82992 | -55.53933 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 05b3e94d-82ae-3eef-a8cf-92addef65e47 | -8.77687 | -44.29815 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9000ce49-f175-3840-9085-b32a4fd7bc90 | -9.57851 | -45.48087 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af2a3ccd-7639-368f-8bd5-4761142ba390 | -6.30058 | -41.75939 | 2026-09-21 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 68b449e0-cecc-387c-bf1c-d70da8a622e7 | -6.77132 | -55.63745 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9e30288-3a4e-3679-83c4-5d370565c825 | -7.68235 | -46.07437 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bbf99c4d-7bd1-3b8f-813c-5663841aaf86 | -9.54822 | -45.40177 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 743912ef-5d86-35e4-a176-2cc9190c2370 | -7.31378 | -46.7508 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 107a8e52-ee01-3e60-80c3-10bfa3ad4d9e | -8.96468 | -49.14898 | 2026-09-21 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 899cbc40-21bb-3548-9152-c3b993440833 | -6.72635 | -55.08426 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5df5335b-085a-3267-afb3-adc770e6ed0e | -3.33916 | -42.77085 | 2026-09-21 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README38.md)
