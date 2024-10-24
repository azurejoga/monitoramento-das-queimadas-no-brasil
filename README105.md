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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d8b25f1-7044-3b0b-80ad-1f873629467c | -17.76379 | -57.58783 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 961846e1-8d59-3004-8804-2fc7069f14f4 | -17.75952 | -57.48777 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| beb03825-84fc-32f2-bb9a-c73d3e840cf5 | -17.75486 | -57.49112 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 73abdc91-0e9d-37dd-a50f-077a40909597 | -17.75293 | -57.36969 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b801e776-1329-383f-a0ce-06b6fb0da96d | -17.75244 | -57.36778 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3f1fd256-95c8-3fa0-aa3d-9a9bfcf40161 | -17.75139 | -57.58609 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9be05671-56c8-3991-b521-10ff746fc54a | -17.75071 | -57.49053 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6c3544ad-a7c3-300c-bed6-cd040cfef8f1 | -17.74773 | -57.37121 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f6335982-042b-3dea-8a4f-0d6e61fd89f0 | -17.74726 | -57.58551 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 04d2834e-7d60-3a87-b5c2-490645ea5828 | -17.74678 | -57.47603 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 456335c9-4723-3471-b30b-c507b36197c6 | -17.74655 | -57.48996 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f5cc0203-cb78-3b86-abf6-c0e58e5055ad | -17.74507 | -57.56937 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7c1083f9-3be0-3951-bd22-6812ba66b98d | -17.74459 | -57.57327 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c5bfbc4f-8f93-38e2-913c-dcbfb7709a58 | -17.74239 | -57.48938 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| fc6b2aee-9dd8-34a1-8c5e-5ec587285295 | -17.7421 | -57.47939 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8f6b4d20-3fbd-39ab-aaa8-4ee2c59cb5f6 | -17.74045 | -57.57267 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8156d427-613e-3941-8331-3574807b7d67 | -17.73969 | -57.47699 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dc599164-3c0c-3e1f-a1d4-0de9c8948ccd | -17.73327 | -57.48217 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c2c28078-de42-3617-baf9-6aa081475d7b | -17.70781 | -57.48264 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| e57054a5-d300-3682-b0b9-3cb700b5eabb | -17.70634 | -57.36142 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0f7701b4-eb0f-3c1e-9047-3ccdd11a31f8 | -17.7 | -57.47755 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0100d33f-500c-3320-943f-41ed01843805 | -17.68386 | -57.47131 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2fd03258-82db-31ea-80d7-0599e7ea5e89 | -17.6792 | -57.47466 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 273d80ca-73d8-3083-b5a7-0575bb5c9bfc | -17.66821 | -57.46112 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 53b64675-05d1-3089-9e8b-9793c3e14f55 | -17.66603 | -57.44476 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| dcfb3aad-fd17-384d-a537-f5ed78032646 | -18.11437 | -57.33057 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| eb73e192-c911-36c1-b535-5f7d862097e3 | -16.20573 | -59.16426 | 2024-10-24 05:23:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2b4818e4-8d34-3053-9cad-df5b1f8e891c | -15.49435 | -58.07225 | 2024-10-24 05:23:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8e46bb4-b9a6-36a8-8d23-0a11a3449b0e | -15.16328 | -59.71604 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3f62fb5-3a67-3524-ba7c-3b8e5822514e | -15.16267 | -59.72015 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0e01f61-0608-3da5-b6af-3bfe8c9d3ac7 | -14.92236 | -59.88119 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce1f870c-0ee1-3f03-ac77-adeeb3493974 | -14.87438 | -59.86559 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fad6dcf-c891-39a1-a256-5aab97ab961b | -14.87028 | -59.86909 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bd95798-93aa-353a-ab0e-273dc47f845e | -14.86677 | -59.86855 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3e341b2-b241-3832-b5cb-4e7685b449e9 | -14.70953 | -60.00972 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6170c2b0-fe45-3ea8-9fae-ca9e3b601f40 | -14.56243 | -59.9968 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bec39c2-ba19-3fd3-a223-d8aebede0821 | -14.56184 | -60.00075 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 710508ec-e589-3c27-9360-41d3969beb94 | -14.55953 | -59.99231 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d39e1169-b51c-310a-b955-99f8aef729e5 | -14.54326 | -59.95749 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6713839f-b1fc-3dec-93a4-d2f5418f74a5 | -14.53978 | -59.95693 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d1d22fd-90cf-37a4-a2c5-0e2a31f80e29 | -15.80364 | -59.55241 | 2024-10-24 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc9cce41-2e22-3081-83d2-a50a65b1c639 | -15.67096 | -59.74891 | 2024-10-24 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eea37ade-e63d-3f2d-96ea-e8f71caa5b2e | -15.67036 | -59.75308 | 2024-10-24 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 267ef9f8-8237-37cb-9429-b2001353e919 | -15.66976 | -59.75723 | 2024-10-24 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b70660a-657f-344b-bcdd-d8bb6cfcb723 | -15.66916 | -59.76138 | 2024-10-24 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b95a8614-5b7c-3b51-a78c-84b85d5ab9ff | -15.28827 | -60.40299 | 2024-10-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23713fcf-2abe-38b4-98d5-9bc739b71c70 | -6.76368 | -59.11895 | 2024-10-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 480da1ce-d124-3644-9ab3-995abe5946fa | -6.76312 | -59.12256 | 2024-10-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ff32dcc-7974-323a-a822-25a1dbc9caff | -6.7603 | -59.11843 | 2024-10-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 33fbf949-cb5c-31c4-9458-0973711c90dd | -6.75975 | -59.12205 | 2024-10-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 251fcb1d-37cd-39e7-a2bd-6b68fa8317b3 | -6.75919 | -59.12566 | 2024-10-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2220b087-098c-3c6f-9f86-1fd359a20ab5 | -6.75693 | -59.11792 | 2024-10-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2c01b9f-edb7-3304-a7cd-8fdd1ca26fca | -6.75637 | -59.12154 | 2024-10-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c16dad18-2a16-3a25-944f-f8b9d6a74823 | -6.75355 | -59.11741 | 2024-10-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e770a1d0-100a-336f-80f3-e7037eff55a9 | -6.75299 | -59.12102 | 2024-10-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1321bb55-c09c-32fe-b704-c2208bf9a1f9 | -7.4851 | -63.5579 | 2024-10-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76103a5d-1c31-3cf3-a044-af94beb2a733 | -7.3035 | -64.71976 | 2024-10-24 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f88683f9-c337-3793-97ae-196f2581b4dc | -8.20471 | -64.09484 | 2024-10-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 656aaaa8-a619-3d0f-b748-0255e9813a11 | -8.20402 | -64.09901 | 2024-10-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e99a1493-6a52-3a64-9e20-cc48e9e46e87 | -14.26692 | -51.13361 | 2024-10-24 05:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c35eef8c-7805-33aa-9a92-8853d532ac49 | -14.26191 | -51.12348 | 2024-10-24 05:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b1605216-3e72-31fc-8987-6d20d40d663a | -14.26142 | -51.12804 | 2024-10-24 05:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cdde227a-7991-3fa4-867e-50e9d927ef11 | -14.26092 | -51.13258 | 2024-10-24 05:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 971fbfa7-a286-3a5d-aa19-61ea63035a2f | -14.72303 | -52.78959 | 2024-10-24 05:25:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12dfbdcc-80e9-3dd3-b313-fa65610e9761 | -14.45509 | -52.88657 | 2024-10-24 05:25:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2135860c-bd80-329d-a685-09a2afb76fcc | -14.45345 | -52.88314 | 2024-10-24 05:25:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08b41037-c1a9-36c6-9d14-9fd1e7ca2967 | -14.45303 | -52.88659 | 2024-10-24 05:25:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbe1d88b-2b28-3df7-9bd1-563d9bc752dd | -14.45009 | -52.8823 | 2024-10-24 05:25:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d484ed25-170c-3b04-b9f5-4a2bd5943cc7 | -13.75878 | -54.06711 | 2024-10-24 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4cd9ba3-ec61-3bef-b2ee-470230817815 | -13.75754 | -54.0652 | 2024-10-24 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb1c1489-10dc-383f-a7fa-17b79eb5e3fa | -13.75331 | -54.05884 | 2024-10-24 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9d88b316-bb17-35e8-83b9-d4da5cbd4494 | -13.75259 | -54.06452 | 2024-10-24 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e959e620-4941-3bae-b8a2-d8e19e33f0d6 | -13.74836 | -54.05821 | 2024-10-24 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 04a57512-44c6-3d42-bb4e-d623f1aaebfa | -20.38773 | -54.86181 | 2024-10-24 05:25:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5e5374b-b458-3995-ab2d-5a60cd261d48 | -23.83003 | -55.2931 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| faacd533-3c35-3b59-8a7f-96b03a9f15db | -23.82969 | -55.29654 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 0260a413-5db0-3a25-a8e3-77dbb5bbc6b6 | -23.82936 | -55.29999 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| 22b01667-05c3-36d8-b89c-2d743c47a4e5 | -23.82514 | -55.28923 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| bddb85dc-ca1f-35c7-889e-73b5232cf9fe | -23.82481 | -55.29268 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 48700c15-ad17-39ed-9a1e-0bf37af6275e | -23.82448 | -55.29613 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 992c87aa-457c-3983-a839-422d1374a6e3 | -23.82026 | -55.28534 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3ffa9b15-01c4-3634-939e-4132fce0cff6 | -23.79365 | -55.28887 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 8513eb56-4721-3abf-bc1a-c7a77a10cab3 | -23.79333 | -55.29228 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 32e18142-934f-3634-bf41-0ff01012aeb8 | -23.79035 | -55.26808 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 728dd3aa-4d13-357f-82df-67fe86a430c1 | -23.79004 | -55.27144 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| afd0a84d-e466-3cc6-a9e7-a96da9139673 | -23.78972 | -55.27479 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bc71c6d2-d9a4-360e-a1dd-4147bca2f91a | -23.78941 | -55.27813 | 2024-10-24 05:25:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1ff6fb64-e36b-36db-9683-dfea131b86a6 | -23.26597 | -55.20543 | 2024-10-24 05:25:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5bc711c3-c9e8-3766-b469-10bc562ac154 | -23.26565 | -55.20879 | 2024-10-24 05:25:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c3af3469-3fa6-3e38-96f7-8b5aecc879d1 | -19.65511 | -56.85655 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 42cbbb9d-4cfc-3cc5-8018-65eba55b7b56 | -19.6551 | -56.79258 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 86bbcb48-4363-39c1-ba19-b1410735782f | -19.65453 | -56.79723 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1c4d279f-3233-3e6c-bd91-6552a413b9e6 | -19.65396 | -56.80186 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b35c3f86-bb73-3e6d-bd1a-7755e2d0fc82 | -19.65368 | -56.79041 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ea298259-377d-3e0d-8b3c-90679f8769dd | -19.6534 | -56.80651 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9cfac04b-f74c-36f8-a371-5397068e3e71 | -19.65315 | -56.79507 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9518e924-7f9f-30b3-abad-79e47573491a | -19.65274 | -56.84875 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 37d3c424-10f3-3523-a0c7-637792cf522d | -19.65262 | -56.79972 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| aeca0562-f2f5-3e67-ae31-c027c1c639c9 | -19.65226 | -56.84209 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cf610313-0425-3880-bb36-01a55842ec6a | -19.65217 | -56.85336 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |


[Clique aqui para ver as próximas entradas](README106.md)
