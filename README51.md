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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db328c50-4887-3c70-adb3-6ce34057e23b | -6.98587 | -42.58599 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 30bed333-7afc-3f5b-a4be-ddc482abe7eb | -2.98688 | -50.51545 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3d75927-048c-3969-85ad-01d40bbd7cac | -5.57586 | -42.29937 | 2026-09-23 04:25:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d9cb344f-854c-34fe-b4e4-f5e7976fd0fa | -6.34297 | -43.36585 | 2026-09-23 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2fb51b6d-7cbc-313c-966f-a8a679e2ce72 | -7.31676 | -42.26347 | 2026-09-23 04:25:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e2088afd-56f8-35d4-94d8-0967f287d126 | -3.22867 | -53.94834 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ded0ee0e-5c9b-30c3-a9d5-40c8b2b37094 | -5.11716 | -48.8031 | 2026-09-23 04:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ee4dcec-f5c7-3dfa-a868-88fba2ae8edc | -6.85451 | -45.56461 | 2026-09-23 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5328cb98-43a1-3fa4-81ff-4ec1b27a89a8 | -1.48319 | -49.30291 | 2026-09-23 04:25:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 223ee65d-f418-3021-812d-ff364e046db9 | -3.23322 | -53.95184 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca9261e2-1e07-3e56-b97c-83816bad7694 | -5.41586 | -49.26778 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f2091923-4db5-3f63-9c99-ebfffd3ddff1 | -6.88926 | -43.75319 | 2026-09-23 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e074d66-e150-3026-8552-629cbabf95da | -6.61788 | -43.72795 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ece62e1-d31a-36fc-86f9-159049a4acb3 | -5.03097 | -42.478 | 2026-09-23 04:25:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a3687d8f-6482-363a-aa18-9a7fcc2ac0fd | -6.14531 | -43.83767 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4f34dff-84f5-3212-8f08-83af64973365 | -1.05082 | -47.35282 | 2026-09-23 04:25:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb09ace6-f0cb-35ff-8461-0267f292f1c8 | -2.82903 | -50.47529 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6413bdc8-e519-3faf-89d8-be3d9c65f9a9 | -5.60893 | -45.9444 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72843248-8d81-3279-9626-431ee8692a8c | -5.84381 | -47.86872 | 2026-09-23 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8093d849-96bd-32b4-846d-bf8ecf3be90c | -3.37929 | -50.40562 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bad52338-e8e9-3d61-b148-d34f07508c90 | -2.7416 | -51.37033 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f65d0239-93e2-39e9-9868-37bb03b55e96 | -5.28452 | -47.25443 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84d34ef2-b2dc-3b09-b0c2-9438a1a0c84f | -6.47565 | -48.46474 | 2026-09-23 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ff3b60c-4381-3183-87df-8a1661592756 | -6.83875 | -45.51163 | 2026-09-23 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 77339fed-0765-3b71-a519-d35491dc8eb4 | -5.62219 | -45.24401 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4f694278-af6c-378b-b3d4-4b40e3c606e8 | -3.00926 | -54.18974 | 2026-09-23 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c5b9d36-89c7-3b21-9832-acf499be9958 | -6.48282 | -42.7849 | 2026-09-23 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3868b353-4315-3584-86a0-49a156930c3d | -3.91168 | -55.83295 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8b907bc-aecb-32b4-8625-7d7936d1c056 | -3.80658 | -52.36344 | 2026-09-23 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6caedef-64e2-34a2-b591-92ac2eed9e67 | -6.1412 | -43.84116 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f12a90e3-ae60-3ebe-9628-9d3adbef0188 | -1.21643 | -54.54911 | 2026-09-23 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eca86ccb-ea65-3a77-9cf6-fb2d9be01021 | -6.43923 | -48.45089 | 2026-09-23 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d921ac5-fb6c-3996-979b-9a6e5c7411f7 | -3.93855 | -49.99488 | 2026-09-23 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 406114f0-3e45-36da-ae59-fe11778ee052 | -2.97408 | -50.39924 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c319544a-399f-3118-8ead-c85151ab7f02 | -6.62315 | -43.74102 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7289c19c-0bc1-31fd-98f2-e691366109c6 | -4.91574 | -45.65487 | 2026-09-23 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d7b61e1-7dfc-3668-a8e2-5bf8b8e7a306 | -6.93837 | -42.88369 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4c0ee96-d80c-30af-85ce-562756c3bc97 | -1.21695 | -54.54585 | 2026-09-23 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da93719a-4f6c-3745-b3bf-402c31b55d9d | -3.15052 | -48.06688 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61b72e79-bedb-38f1-af17-496773f8fb39 | -6.17104 | -44.13002 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f150c535-3d48-3a4f-bade-a82ff5b3b5a9 | -5.86832 | -46.26756 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84e1619d-808d-329f-b2e3-d0c27ffc9b87 | -6.581 | -44.66589 | 2026-09-23 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dbb7fd4-09c1-36a7-88f2-350ff29188d1 | -2.97488 | -50.39422 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0a23446e-7854-38a3-9d56-253962bca8e7 | -6.98384 | -42.5999 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 39c3effc-01b2-3eb5-abfb-24da21d79016 | -4.00438 | -52.09256 | 2026-09-23 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6979c7fd-1914-32b6-a7bf-226ae3735d0a | -5.40388 | -45.84124 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84c9b863-7261-35c0-95df-bd5ad5081cd3 | -6.13652 | -43.8485 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e7f69dd-a376-3c24-bbfd-e36563f839d8 | -2.97802 | -50.39989 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e32d90d3-a6bd-366e-8192-81a87b220d4a | -5.80578 | -52.09056 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65512e3c-bde8-345c-84b3-f692bd663c6d | -3.03364 | -54.40901 | 2026-09-23 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4987bf9-3480-3c77-9519-e3c80fd55fc3 | -5.18383 | -49.33409 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 117fbd93-5920-3f35-bf14-ec89b2b6fcc0 | -6.18509 | -45.32048 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77da7a63-de48-3ca7-98a2-7724b3e70486 | -3.90605 | -55.83214 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 01458beb-6ee2-3f5f-be5a-75a00534af22 | -3.22677 | -46.9496 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b9c25d66-871c-3487-85df-2cf1bd60ddac | -1.38479 | -49.04556 | 2026-09-23 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d18685c-235c-3422-b1d3-677b7302634e | -5.76402 | -45.11819 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ed0ea55-7b87-3bcc-835b-814358bbbc09 | -5.56967 | -52.02223 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91267056-9f38-34ee-8991-f030ae8126dc | -2.32394 | -49.20626 | 2026-09-23 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0625ef43-73cf-3b6e-b772-8ecdd4989066 | -4.45487 | -55.07038 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 961b5433-09dd-36c0-bc10-0fbff0900009 | -4.46104 | -47.92533 | 2026-09-23 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3390f762-190b-3a72-9d04-d061c585cf1b | -6.57879 | -44.15129 | 2026-09-23 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0d23a06f-77a9-3708-a3b5-bcb08482c20d | -5.81356 | -47.76435 | 2026-09-23 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e67f766-ae2a-38d1-804b-57bfd578246d | -3.80587 | -52.36773 | 2026-09-23 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b987d8b7-fa57-35f2-9293-c5eed01e6d77 | -6.72502 | -44.15127 | 2026-09-23 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b8c80739-6dac-3d24-a582-b940345b6145 | -5.77945 | -43.78534 | 2026-09-23 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d1d1576-fa8f-306d-b962-ab2ad9ac2da6 | -6.6084 | -43.74291 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 321202bf-3ddd-30e0-9218-842bd7880e94 | -3.39104 | -50.82635 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97cab621-95c8-34ec-90c3-3904a9aaacd7 | -5.00019 | -49.47374 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcc1873f-2d09-3203-b8e3-21ffeb5312d0 | -5.80741 | -49.15729 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2da190a8-71af-33fc-9af3-153ab6d1a3b8 | -5.52656 | -47.7007 | 2026-09-23 04:25:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a911f971-8521-3855-82ea-6d6711b9947d | -6.43394 | -43.72273 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a76e9ff4-71d5-308b-b76e-676929559765 | -5.85057 | -52.02935 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abc33f20-d634-3525-9bcc-bcdc71b29360 | -5.76845 | -45.11164 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 478a11ef-8f1f-35c8-9b88-763eb3c4bac2 | -5.35512 | -45.7382 | 2026-09-23 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b7be2fd-86fc-3d41-bc8c-99fb82670006 | -2.92523 | -48.74161 | 2026-09-23 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4418550-2392-343c-afd7-aadd2986baee | -5.19708 | -50.08951 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0df57903-5010-3c45-a32b-0b061c14a61f | -5.12194 | -48.79582 | 2026-09-23 04:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 57d34e66-5adf-36a3-9bec-1b2fe385d309 | -1.38036 | -49.0494 | 2026-09-23 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02d31fb3-399b-35ea-8f83-2759d540edb3 | -5.78005 | -43.78145 | 2026-09-23 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2642a6ba-0a60-37b5-a502-b68704ed7f05 | -7.05067 | -43.71452 | 2026-09-23 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfa717fd-a88b-34ce-996c-4580055531dd | -5.76122 | -45.11414 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 676cdb30-5fba-33e7-b2ae-ab710f791982 | -2.7821 | -51.36072 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb606c5d-3305-3b84-bd8a-02ffd89967e1 | -6.58317 | -45.89151 | 2026-09-23 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e28f12f-dd18-3f3b-ae6d-c3d5ae58c70b | -5.13778 | -50.05214 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d370fb3-b583-3604-bbf5-232b5c943a97 | -2.97042 | -51.45711 | 2026-09-23 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fabc6b80-215d-3ee5-b6f8-cc4302143349 | -5.00382 | -49.47431 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 436f98da-eb10-3070-ad70-e0850a3c2e91 | -6.61487 | -43.74794 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a6d7b7d2-a42c-3204-92da-74bf15c92a08 | -2.9539 | -54.08281 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5b884f0-c8b8-31b6-a613-b075ccb57986 | -5.57004 | -42.72932 | 2026-09-23 04:25:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| afe09c5f-424b-34bb-b5a7-2b96a19487d6 | -5.86552 | -46.11188 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cf51319-9ffd-3432-92cf-01ae2b0e27ed | -7.13331 | -43.08425 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f81ac74-5bb7-318c-b90e-558c01240700 | -3.22981 | -46.94658 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83be0534-de13-3997-9373-0181295b47b8 | -5.24513 | -40.59559 | 2026-09-23 04:25:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14663888-6968-3475-ad9d-a3e4e8ade9e6 | -2.62111 | -59.38007 | 2026-09-23 04:25:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9c2537a6-1c30-3b5d-b77e-43bac5536148 | -6.20423 | -43.8508 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07112212-4e0a-39e9-bc9d-0fd440ec2776 | -5.60509 | -45.94734 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33bf24bf-64d1-356e-9036-eaea7026d4fa | -5.85481 | -52.0298 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61c08644-7513-33ce-9ed0-1129a6f8f149 | -3.14992 | -48.07072 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24dea1c3-fe84-3f9c-a340-c56acfda7d0f | -2.79033 | -49.52676 | 2026-09-23 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbdf4e3f-39f4-3e05-99bc-45a19522b2e2 | -6.1334 | -45.01813 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README52.md)
