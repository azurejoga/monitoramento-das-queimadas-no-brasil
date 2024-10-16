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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88d9ce53-a886-39f2-b2a3-0699c8a76e1a | -4.98518 | -46.4945 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 043806ac-3928-3e1d-944b-012a8e41577d | -4.87713 | -47.10125 | 2024-10-16 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3fdab96-9cee-3862-bff6-ab2cb4ce2d66 | -4.86944 | -47.10713 | 2024-10-16 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d15844f5-bfb1-3251-9b47-ce282cc016ab | -4.8689 | -47.11057 | 2024-10-16 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b863ff38-fcd4-3abc-b2f4-8ae908a04e80 | -4.82212 | -46.60587 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a61cf961-a52f-36ae-a8b0-6519001ba7eb | -4.74232 | -46.61515 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5f6a482-659c-38f4-9522-fce9a0f6f042 | -4.74008 | -46.60766 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7c1fbd7-348d-3da6-96f9-a4eab60c6b01 | -4.73968 | -46.65403 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81fd19d5-bc77-3fbd-a50e-327a5866c184 | -4.73954 | -46.61115 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73b29322-5e1b-374f-b501-fbf78eaacb30 | -4.739 | -46.61464 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c189c6e0-ba32-338d-99e0-32e7f6fe5b1b | -4.73622 | -46.61063 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c9db26c-a797-34d1-9a8a-12f0b6303032 | -4.73268 | -46.5455 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bc05c68c-ab65-37b5-b91d-78d18f6eccc2 | -4.7299 | -46.54147 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 93df735f-fcb9-3d53-8a62-ff5cde99ce26 | -4.72935 | -46.54499 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a69b69d9-8716-37ab-a790-3b68d210a6f8 | -4.72881 | -46.5485 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57478fab-acc0-3da3-b9cf-fd6f3f88f0b0 | -4.72695 | -46.54076 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bd82f7d-cc31-39ea-b075-589fc81748a1 | -4.7264 | -46.54427 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbebbd49-5aa5-3f94-a101-57429d6e4230 | -4.52702 | -46.81997 | 2024-10-16 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bce9bd3-807c-3dec-8462-fdce477fa6c4 | -4.47486 | -47.73647 | 2024-10-16 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4f5d1a6-dd12-3785-8ea9-73e876bf8ed2 | -4.47156 | -47.73595 | 2024-10-16 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ea721cf-a717-3027-9594-d6a184deda76 | -4.46825 | -47.73544 | 2024-10-16 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92ef921a-9f10-3de7-8a93-0148f3f89018 | -4.43169 | -47.53572 | 2024-10-16 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 308713ef-3220-363b-aa3d-f34f4c7a09bc | -4.35731 | -47.27353 | 2024-10-16 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b430381-1341-32fc-bf75-e68b3484fc2c | -4.3389 | -46.69797 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2524e181-dfe8-3e67-9ccb-17b40c0dafd1 | -4.33835 | -46.70145 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e5888243-beab-3625-8e07-cc95448009e8 | -4.33504 | -46.70094 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ccf67b8-c8f7-3544-a2fe-ef63290ad962 | -4.33014 | -46.7322 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50604670-0db2-3ddf-9c1d-aef315e865da | -4.18623 | -46.84832 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15d397f1-e93d-3539-b50c-466f771058d4 | -4.18383 | -46.62444 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f249b482-4086-3929-b1d8-05e9804bf335 | -4.18258 | -46.74142 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f5000d4-e07c-3aeb-a384-d6b5d63cb044 | -4.15267 | -46.86787 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a38911ab-ec23-3b4b-8c3a-c71381983443 | -4.14382 | -46.85941 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5dac18e-cc9b-3f2a-82f1-20f6283e387e | -4.06736 | -47.12967 | 2024-10-16 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98e6595c-3c1d-3f99-83df-1c2d4f2d388f | -6.12777 | -47.00836 | 2024-10-16 04:29:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36c78578-0cc3-3ab8-a6a4-441c54d31e59 | -5.70901 | -46.62041 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb3b5520-90e8-3784-bfba-810e7827642a | -5.51547 | -46.90596 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afc15b8f-afe5-3618-93b3-7961dcfc2682 | -5.51492 | -46.90944 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d0261c8-7190-3079-bdf0-3edd3c6db667 | -5.51269 | -46.90195 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b6239bc-ad80-3e79-848e-95665f530340 | -5.51215 | -46.90544 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 762992cf-bbd6-3628-ae50-6800d0b04ba4 | -5.5116 | -46.90893 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 022e9450-2dd3-38b6-8a56-5d2fd298ef87 | -5.25289 | -46.86901 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55b22524-ebc9-372e-9a7a-5a9bea98dcc9 | -5.1076 | -46.84259 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d854d84a-97c6-3682-bf17-c3620f3e4fe0 | -1.60271 | -48.13075 | 2024-10-16 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89594ef6-d33e-35fa-b0c9-a2f446a2dc6b | -1.56196 | -48.01881 | 2024-10-16 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b39ab419-56aa-3617-954a-26abd4d46a86 | -1.50266 | -47.21284 | 2024-10-16 04:29:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1a4f319-02f6-3a43-a76a-4df220f32dce | -1.4908 | -47.33112 | 2024-10-16 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3585c464-5268-3538-a7cb-cd22ceff876b | -1.48749 | -47.3306 | 2024-10-16 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60114829-5dce-31f5-ae7d-3362e34f6491 | -1.48418 | -47.33008 | 2024-10-16 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 912a7321-365d-30d8-8cea-7fd6a40cffdb | -1.43792 | -47.40844 | 2024-10-16 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 956b9546-9fd0-3f7a-b4dd-c2aecd4f7a64 | -1.43737 | -47.4119 | 2024-10-16 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2f03b26e-c058-3efa-8e0f-13ad818a31e3 | -1.4346 | -47.40792 | 2024-10-16 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f446882f-26a3-3166-adc9-eda98cec69dc | -1.43406 | -47.41138 | 2024-10-16 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ee32068c-806d-3c2e-885f-011c81fa72fa | -1.31866 | -47.49644 | 2024-10-16 04:29:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b358ab8d-88c3-337f-906d-d194f2d99285 | -3.21715 | -48.92098 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 122e6cbd-176a-3e44-9fa3-ac83826f7cda | -3.21657 | -48.92465 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 84c98f11-0cc1-3116-9b53-70aef7c0a475 | -3.21375 | -48.92046 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 292e5131-2ad2-3e89-bdaf-9b2318b69c12 | -3.21317 | -48.92412 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 63dd97c4-53b2-320c-a479-5fb9f49a9e83 | -3.16763 | -48.37433 | 2024-10-16 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da46d20c-5941-35ba-a685-b9899b53eb93 | -3.16428 | -48.3738 | 2024-10-16 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f7024aa-fcbe-3216-9a90-a2b63315f5ec | -3.06365 | -47.48602 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 880643d2-c884-32be-93a7-838fa3d5c589 | -3.46616 | -47.66993 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 695ecf9d-ea7a-374e-976a-431e21155e8f | -3.46562 | -47.67337 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94dd1195-518c-3ada-9ee9-882ba31fc6ef | -3.06695 | -47.48653 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cb4844f-bf9d-300a-a616-09c4aeb8b0e7 | -2.38415 | -47.59175 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b900c654-a645-3a9c-8bc5-44fcc5a8f6b2 | -2.96497 | -48.0035 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d5afa68-f7a9-34b5-b0f2-62138c371035 | -2.96442 | -48.007 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fae82924-2141-3720-9cd0-60e4b9c8de03 | -2.96164 | -48.00298 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 19e38761-62db-3857-846a-7a5f40d947b2 | -2.96109 | -48.00648 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 15830a83-86c7-3e6d-b390-ddbd3e75638a | -2.95776 | -48.00595 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5517fa35-a979-3f08-8157-c0c65b47a6f9 | -2.93611 | -47.99181 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad49c6d5-f9e4-3860-82e2-12528f42caa3 | -2.93278 | -47.99129 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1097a48e-52da-3b67-9145-6248e02e1ad7 | -2.79789 | -48.66936 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 883cf78e-8c67-327a-8c14-55c2d32e7588 | -2.78649 | -48.69733 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0c50dfb-350e-369c-822c-f4aaa6284cba | -2.7793 | -48.6553 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3514aab-2f07-3a78-a66e-e1c545e85f8a | -2.7388 | -47.54108 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3220225-6154-323e-a5d9-e3dfef53175d | -2.70073 | -48.70649 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a771df71-63b3-3e9e-892d-259374ed15ed | -2.66538 | -48.54877 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20f76631-53e3-3a12-a11d-74790a692f73 | -2.57017 | -48.15762 | 2024-10-16 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14024353-e072-3d61-b8f7-b9ca752231ae | -2.50748 | -48.5539 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c4a9655-8714-3e99-a181-6d74dc97abdc | -2.5041 | -48.55338 | 2024-10-16 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79b63625-b051-30e3-ad14-febeccff07bd | -2.46172 | -48.35158 | 2024-10-16 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 91eb56fb-018e-3f25-b657-8f25000d8aec | -2.45892 | -48.34748 | 2024-10-16 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15e04dd2-9102-3781-81cb-af1b4a220aa7 | -2.45836 | -48.35105 | 2024-10-16 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a515664c-2bea-3622-a586-42716ca3b408 | -2.45815 | -47.81364 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 523bd839-aed4-3da6-a706-7b945d945cec | -2.45764 | -47.83857 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d9c44e3-4be5-3163-baf0-06262484656d | -2.44107 | -48.77478 | 2024-10-16 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 692754fc-628a-3316-a49a-ded17b8edf01 | -2.41838 | -48.4513 | 2024-10-16 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebe8baec-0fd5-32a9-b7ee-049fba22b36b | -2.40971 | -47.64583 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63ef8c66-be8b-357e-8183-021d452c29b1 | -2.38361 | -47.59521 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09acb898-80b6-3f1f-8c38-e6d205555a55 | -2.38138 | -47.58777 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d4596c1-a4cf-3667-a862-8f16db9723fa | -2.38084 | -47.59123 | 2024-10-16 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5365031-da89-3e24-90e2-5ae23198a32f | -2.35565 | -47.98755 | 2024-10-16 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7055dee0-a3ca-3bb2-945c-65b87557ad04 | -2.32386 | -48.58171 | 2024-10-16 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 520aa321-0dda-3632-ba63-41b00f7a0789 | -2.23502 | -48.0188 | 2024-10-16 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2a10c23-178f-305d-b8da-4e7e54d7edfc | -2.16095 | -48.81505 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78e0e226-1d23-3038-b979-ae41b1cf965a | -2.15986 | -48.4484 | 2024-10-16 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7e09d6a-059d-3fa3-97d7-6c37958f119e | -4.82008 | -49.14026 | 2024-10-16 04:29:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77609824-a188-3741-a109-2f50966a853b | -4.8195 | -49.1439 | 2024-10-16 04:29:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b562a08-1bfc-3ef6-b247-fafc8780d18e | -4.81611 | -49.14336 | 2024-10-16 04:29:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3cce9af-5b07-327a-89de-0ed7314b46a5 | -4.81568 | -49.38784 | 2024-10-16 04:29:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README45.md)
