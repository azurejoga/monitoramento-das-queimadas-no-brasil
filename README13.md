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
| 05b626db-7f10-349a-8434-f2806322553c | -1.83693 | -54.48911 | 2026-08-17 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b089f7e-0b49-3fde-b859-22887fd8d29b | -2.80324 | -48.59158 | 2026-08-17 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dfac4cf6-b4b3-3f42-8f69-06943458e80d | -7.45679 | -46.14919 | 2026-08-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09540bf9-e139-3e54-ad55-270d7aded77c | -6.99594 | -41.43593 | 2026-08-17 04:19:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2fe3c337-1978-3d4e-9f4a-e68fc50d2415 | -7.1827 | -44.18222 | 2026-08-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d594d8da-a0eb-38ab-91e3-36e25d99e981 | -6.82216 | -45.33997 | 2026-08-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14733248-88e6-3d2d-8cf5-80f5264d2f4a | -5.84521 | -44.91222 | 2026-08-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9e8fcf4-5cb1-3c9f-9211-53cecfc64037 | -6.11044 | -57.71679 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9c9458db-d714-3910-9ef4-345c49f4c877 | -2.95888 | -49.26547 | 2026-08-17 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd68248c-83c7-3ea1-a81f-d84a0b48086c | -6.74145 | -44.68258 | 2026-08-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4d00825-4a81-3734-a3e5-fb18eeffcf42 | -7.2186 | -41.5472 | 2026-08-17 04:19:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 595930e8-a5a8-3e30-880b-acc2b6dc6fc1 | -5.69703 | -36.25554 | 2026-08-17 04:19:00 | NOAA-21 | LAJES | RIO GRANDE DO NORTE | Brasil | 2406700 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 324397ae-9549-34df-914c-d59effadd18c | -6.11284 | -57.74197 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 603b3773-4d9d-3265-bf02-31c7dc2d2c64 | -2.76949 | -48.5761 | 2026-08-17 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1af209ba-f4e4-3f97-9169-755a39052947 | -6.70879 | -45.36845 | 2026-08-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c0a9aee-d236-32d1-89bb-64e1e5375e69 | -2.95829 | -49.26909 | 2026-08-17 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb833ecb-d2c0-3ba6-bd1f-74462a73613d | -4.94802 | -48.40235 | 2026-08-17 04:19:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b35e62b8-ea75-3eb2-8e5e-95083b3a968c | -6.53271 | -43.11868 | 2026-08-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b2a81096-cc59-3216-b2aa-dfc63f02e9ea | -6.87251 | -41.96027 | 2026-08-17 04:19:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d7419b09-bfd3-388c-8d95-ee312c328777 | -6.02234 | -57.81503 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d79d5e8c-e637-33d6-8a51-4739a29559f8 | -3.26396 | -49.5217 | 2026-08-17 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fea1979-bb35-3f01-b205-9150ed79a8b0 | -2.66484 | -48.52609 | 2026-08-17 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aeefa26-dd37-3935-b30c-802d7a83a783 | -7.5951 | -45.02967 | 2026-08-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13942e13-1325-3a40-90d7-bbb96c05e586 | -3.66216 | -41.12568 | 2026-08-17 04:19:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f3ac75d6-b27e-3c88-a6e9-cb6b05702795 | -7.57638 | -48.43747 | 2026-08-17 04:19:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b001e0f8-e6f5-386f-a367-3ddf0af880ed | -4.0991 | -49.06045 | 2026-08-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4db45543-464f-3d3a-b49a-1b161008b8e6 | -7.61228 | -45.72323 | 2026-08-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14396496-6dba-32a8-a9eb-987041d26f23 | -6.12283 | -57.72537 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5486ba6e-a5c0-3de9-a989-36f9237dc23f | -7.46106 | -45.08313 | 2026-08-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10b5ca2a-22a2-3241-9825-ff8bcd7f650b | -6.12066 | -57.73734 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b2743757-2efb-3546-8a61-5fc13b2d6f8b | -7.80932 | -47.83442 | 2026-08-17 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07878116-164f-30f4-8da3-a0cd45d26646 | -6.52592 | -43.11764 | 2026-08-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80b2c199-8daf-34de-99ae-d5e86c1c1a50 | -7.17851 | -43.72566 | 2026-08-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbcc8d48-845c-363b-a54d-7219c7d829de | -6.23874 | -47.76227 | 2026-08-17 04:19:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25d3abbe-4884-3ae5-b264-84a2e3450971 | -7.76854 | -44.57051 | 2026-08-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bff0fbcc-10e2-3b26-9904-149416af60e4 | -6.53381 | -43.11138 | 2026-08-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b8c96ad3-c88a-36d2-951f-e7a4ca6fe49d | -3.96331 | -43.10559 | 2026-08-17 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dcf1e84-19f2-3e87-bd95-13486a1ecc71 | -7.1208 | -41.44962 | 2026-08-17 04:19:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dd903a0c-9e89-3c58-89b3-ef1cf20220c6 | -2.87798 | -48.85611 | 2026-08-17 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1b2e65a5-4e97-3310-ac44-098ee931afd1 | -6.10042 | -57.73347 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 657091ea-1ae1-36ad-83f2-ae6022632893 | -7.64976 | -42.75599 | 2026-08-17 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 578a7924-69c7-3f1f-9984-0420dcd4296e | -7.01565 | -43.78815 | 2026-08-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fe71e74-e08f-3a8b-8df4-a4956992b8be | -6.71264 | -45.36551 | 2026-08-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b740e62-32d5-3963-b62c-2b3862322088 | -4.12465 | -56.32868 | 2026-08-17 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9f7fac0-110d-33b6-acb2-23d865239f84 | -7.20398 | -41.5449 | 2026-08-17 04:19:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e35a8682-4fde-3470-b958-411e9493ab22 | -7.02498 | -45.90973 | 2026-08-17 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cef06b0-2537-3372-b97a-3f45b570e42b | -5.25034 | -42.85405 | 2026-08-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 131bf3d8-73d4-348a-94c8-caf9d54709b0 | -6.73261 | -44.67411 | 2026-08-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c36c5d9-4280-3e07-9cb0-befa7cae1897 | -6.74091 | -44.68603 | 2026-08-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77ced92c-2060-3b3b-a545-470d99506089 | -6.74199 | -44.67912 | 2026-08-17 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e698095-3823-3986-8bbe-9ff924963335 | -6.12173 | -57.73148 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 14c7cc9e-9b93-3225-81e6-f897eb2f38b8 | -6.47947 | -47.01964 | 2026-08-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5438bff6-60cc-324a-8091-5210e9e7fe46 | -6.77744 | -46.33812 | 2026-08-17 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68f06581-fbf1-3b4f-b40b-99e2532654e7 | -7.01176 | -43.79118 | 2026-08-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 460e87fd-2765-3245-a6e6-f3606e295f9b | -4.35854 | -46.16445 | 2026-08-17 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efd86bff-b48e-3a02-a88c-9c721e8432af | -6.30791 | -43.61826 | 2026-08-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edd29a05-0afe-3553-9145-94346752f3dd | -6.11394 | -57.73591 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 69d2b28e-0740-35e5-af1e-da5f300c2130 | -5.45072 | -48.91583 | 2026-08-17 04:19:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d276a4f-c14b-3133-9cdf-d0bb55d7e2b9 | -6.02813 | -43.02362 | 2026-08-17 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 636b156b-18b3-3d31-a979-7a872e6abc8c | -7.01231 | -43.78763 | 2026-08-17 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af11d805-9c8d-3288-9e09-4b691a3c9cfb | -7.02109 | -45.91273 | 2026-08-17 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59f84368-b13b-38c6-b4d3-0a120ea4b5e0 | -6.39015 | -45.68615 | 2026-08-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1dcb46c-7311-3962-a105-f212fcb9a319 | -7.47165 | -45.1238 | 2026-08-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0803d5ef-f5a7-3a8f-973f-cca8c2cca735 | -6.23941 | -47.7582 | 2026-08-17 04:19:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a1bd45a-be24-38e7-bcc9-b5927b20bd9a | -7.64687 | -42.75163 | 2026-08-17 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e251b3e-5869-33e6-9802-f4eddeedcc42 | -6.02793 | -57.81505 | 2026-08-17 04:19:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 55071df9-af20-3d5a-ac69-2e0b81c4f292 | -2.7703 | -48.5711 | 2026-08-17 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 66812f11-4810-3e0e-82cf-7a576541c053 | -5.44687 | -48.9152 | 2026-08-17 04:19:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9edc34ec-f3bd-3396-9040-c30736b76097 | -6.38351 | -51.74324 | 2026-08-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 747f49ad-20e4-3618-b0d4-0af256c8368f | -7.82094 | -44.09777 | 2026-08-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dcc2bd5-40ef-300a-ad4b-a5ce7baee1af | -15.9189 | -55.531 | 2026-08-17 04:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 75c0a9d2-343a-3cce-b825-dfab544e4e65 | -10.5085 | -50.0228 | 2026-08-17 04:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 0b6ffd5b-43a6-3fe1-a9a3-ebba2b15d804 | -8.9038 | -60.5962 | 2026-08-17 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 3222b795-cc67-35bf-9292-65645f5df949 | -6.6384 | -58.9636 | 2026-08-17 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 28725b2a-3b0e-38c3-9212-6a499cfb76f8 | -6.6199 | -58.9643 | 2026-08-17 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 0d2d7ef9-952c-399f-ae72-d16dc60020bd | -6.6568 | -58.9628 | 2026-08-17 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 21557084-eb8f-3e9b-b640-a153fd99cbf9 | -6.7123 | -58.9412 | 2026-08-17 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 4cc089a9-479f-3595-a5fa-23d6d3c181c5 | -7.3824 | -55.4924 | 2026-08-17 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 435ff95c-8911-3caf-b282-602e584954ce | -15.8994 | -55.5334 | 2026-08-17 04:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 0b3d5b3e-9412-371b-a351-27230436910d | -11.48087 | -46.57756 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1d38eb32-b137-37de-8b42-d9a101e03631 | -10.46868 | -50.37193 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 805b517a-3438-3ebc-9762-12d6a2fc3a03 | -15.166 | -48.64686 | 2026-08-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a9121fe-52c8-3d37-b275-ca0a1964b914 | -11.71856 | -54.60316 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96d5caed-cced-3f5b-9c8a-e5f83ddf7375 | -11.48143 | -46.57399 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8c11df79-0b4a-3265-9026-42f2affbfef9 | -7.37867 | -55.48389 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ba47e889-5204-360a-9465-75a6d8cc1a7d | -14.88919 | -46.63592 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f381770e-1078-35dc-b37f-310f5bd6fee6 | -13.65255 | -46.23752 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bcd9d58-d30a-3c0c-a159-a40733218b0b | -12.66463 | -48.5117 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5a7cd165-d20a-3f82-b961-5919f7d2e294 | -14.87376 | -46.64789 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 02c35f0f-1f4c-369d-ac05-a85e5d44493b | -11.71405 | -54.59924 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e48cc9ad-08d3-3f34-9360-5f01f459f731 | -12.24882 | -47.01004 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20f1788c-7be2-3d50-808a-ad1ccc1f5b0c | -11.72753 | -54.61121 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 509e7643-92ef-3cc6-b94b-dfdb0f74b145 | -7.78323 | -48.27828 | 2026-08-17 04:21:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f469544c-f4c4-3334-83fc-4ea6a0c936c1 | -12.03921 | -46.48818 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8196dae6-5956-3c97-9b6c-b86d963acfb0 | -14.31436 | -53.04873 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b206ff6-902c-354c-bf13-bafb4ba14963 | -11.21592 | -54.0253 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c2c3c60-89d6-3266-8554-3d7a0d099ca5 | -12.37352 | -46.43802 | 2026-08-17 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7dcb128-7986-37f3-bfe6-93b781395ce2 | -15.72816 | -45.97456 | 2026-08-17 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df981ed9-b076-3a87-a4ee-329ef74fdf1b | -12.22643 | -47.04305 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98e1386b-f596-3188-a0dc-27795b6301f0 | -8.02162 | -55.15117 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README14.md)
