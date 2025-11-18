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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bc4c16d-9aed-391e-9a65-c6b83fcb8f13 | -5.83597 | -47.83736 | 2025-11-18 04:21:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9ee19bd-24de-3fd6-b259-765f85398d4e | -5.45838 | -40.97635 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7b200a62-6ea0-39f7-8a15-62bb2dc1f131 | -4.18561 | -44.2373 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0525ea76-1f60-35d4-95c5-7219da93356a | -10.96447 | -48.70512 | 2025-11-18 04:21:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfc990cc-3d57-322f-98cb-24a79180bbc4 | -4.6153 | -47.25663 | 2025-11-18 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e50f7e33-e447-3062-b97a-c48e9534fd53 | -9.97216 | -44.77697 | 2025-11-18 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cc6d91c2-1e04-3ddf-b5c4-0773e60968a0 | -3.47344 | -50.2426 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d2117761-65bb-341d-8380-db03713abdf9 | -8.47006 | -47.98162 | 2025-11-18 04:21:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 921ce097-9ead-32c1-9a15-42251236a186 | -4.64382 | -45.65146 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cb980e0-ae05-35a4-8b73-ecb99dbd8c64 | -3.77855 | -47.74873 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92b9aa49-7239-37a2-bf8e-57fc6f80d5e9 | -7.67723 | -45.33725 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d045584-c97a-3867-96c6-410e4b94f60a | -7.86412 | -46.86998 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a796fc60-4af0-3d58-b31c-13752247bb08 | -6.66994 | -42.03452 | 2025-11-18 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 0637dabc-b41b-3bf1-b00c-7c8afbab14e5 | -11.20387 | -43.17661 | 2025-11-18 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 52d4e1ac-c1db-3acd-9034-3c697b498fb5 | -3.15015 | -51.49025 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 402d7f4e-62e8-3d41-bf54-9073b73d4437 | -7.2498 | -39.3882 | 2025-11-18 04:21:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2dbe1dfc-e79b-382d-9304-7492a3ac5378 | -8.57594 | -46.48804 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cca49911-a814-3d4b-92da-e4a403880bcc | -6.41277 | -47.19778 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55cf9573-492c-3d9e-bb06-3df2f7c59291 | -11.43109 | -43.13271 | 2025-11-18 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a580762b-35bb-3bfe-a35e-2bdb15728b4f | -3.52458 | -50.34298 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f0682e3-68d4-38dd-b2d5-d07c40f280d0 | -10.78846 | -47.64222 | 2025-11-18 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d853d5a-e097-3f88-8371-7c27f0ff3937 | -7.22679 | -48.46753 | 2025-11-18 04:21:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 159b0fe4-7942-3041-8dec-f62b084b417b | -9.40691 | -48.44627 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1f0f7545-cca0-3651-9e96-f939d23c0101 | -3.41212 | -50.1213 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9760db43-150e-3a5d-9f20-b35fe851e62d | -8.22217 | -48.30045 | 2025-11-18 04:21:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d594bf6-cd4c-3c01-9436-08887db873b9 | -11.49197 | -40.45904 | 2025-11-18 04:21:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ecd5fb3a-8bbe-378c-b2ec-291d0995f6f5 | -5.47869 | -44.69298 | 2025-11-18 04:21:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 08454a96-f914-3c0f-845d-e2c1f9ba89ba | -6.55124 | -46.90565 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3621b4ef-9e85-3581-bd18-c09d3740c956 | -6.40196 | -42.32343 | 2025-11-18 04:21:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c972cbb7-be14-351f-8b23-1dc69969b551 | -3.1771 | -50.65225 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 484c673a-099a-341b-b897-53abf684ed1b | -3.81266 | -47.49437 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7897961a-3661-3ebf-b1df-59863319fdb6 | -3.48195 | -52.35625 | 2025-11-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4207a5c3-9112-3288-a065-e59d8d3ea1fe | -6.06393 | -41.65907 | 2025-11-18 04:21:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e23be8a1-94d1-3c4f-9ada-dce49d345202 | -6.21016 | -46.88408 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1428df0d-be54-3862-9da9-56c3d131d77d | -5.59031 | -44.89097 | 2025-11-18 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bd7c2bc-3a24-36d4-ae14-84f900fa64cf | -7.29651 | -39.26772 | 2025-11-18 04:21:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af5bfa4a-45dd-38a3-b5f2-73a1b939d085 | -11.43168 | -43.12873 | 2025-11-18 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 42dcc599-d60e-332f-883a-ecce741c6838 | -8.03689 | -48.93428 | 2025-11-18 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35935ec0-071a-387a-9d87-71c8e8d5fc1f | -4.19497 | -44.24227 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06adff61-b3a9-34fd-bed5-8f97c1af2398 | -3.08413 | -51.26007 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 231acfad-306a-3e11-bbcc-e627418b5549 | -4.03855 | -50.48681 | 2025-11-18 04:21:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c37b049b-6550-336f-a860-09aeb7156420 | -4.05142 | -47.50344 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5248b006-2f29-388a-8128-0bda306336ae | -3.40098 | -50.18859 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91ed0e30-30a4-3a2a-bfa2-427773edd4f4 | -7.62536 | -42.58139 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 45c7929b-c3db-3544-902e-fa20a01d8abb | -6.09054 | -51.26911 | 2025-11-18 04:21:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e29eac4a-c4ac-3cf5-aeb4-ece24fe5b851 | -10.73286 | -44.80344 | 2025-11-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db149b2d-6f0d-33c6-8b0a-61d0134428a2 | -3.33092 | -50.28404 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d9ce4ac-84cc-3d8f-a9a8-6ca282d10c70 | -6.64417 | -43.60827 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c0ca239-d3a2-3504-9ee1-168eb021aef6 | -6.99464 | -46.1825 | 2025-11-18 04:21:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5c37fa3-afeb-30fd-b953-9846cf539cb3 | -3.16459 | -50.16719 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37221a76-7d8f-32b2-b304-54850d2f2e48 | -7.61556 | -42.57594 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f24db2fb-07cc-3332-b503-7b35faeac4ab | -11.10066 | -45.43465 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4a0b58a-e549-3ec1-80d6-a7f1b8021c3c | -10.79877 | -47.64383 | 2025-11-18 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbda0046-421b-3904-b05e-2af94d26844a | -9.91605 | -47.8638 | 2025-11-18 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc82c36d-2101-344a-897c-f3d4440d640f | -6.24944 | -45.67236 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be2f3125-d8a7-37d2-b6bb-e4e5188d84c9 | -3.94693 | -50.30217 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdf14e4e-a3be-3687-91bb-507c060560cc | -8.54785 | -46.04773 | 2025-11-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c12c0d10-ab76-31b5-b898-9d73002fa3db | -10.67643 | -44.26147 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab0ec22c-732a-3a5e-93c1-36d0b7ccbfde | -5.7511 | -45.10157 | 2025-11-18 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1720beed-3c1f-3f60-ba70-39a4fd79e608 | -10.97926 | -45.14546 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c408c47-c02d-32b2-9d32-ae968ba32b48 | -7.2923 | -48.31652 | 2025-11-18 04:21:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75e663c2-bb99-3562-b977-338d4e14bf5a | -6.32561 | -46.12829 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc7ee5e4-af53-3f81-9aca-0721d8a0039b | -6.15713 | -46.10136 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3086f51-adbd-3188-ba46-dbd4668f4a37 | -5.0748 | -49.83871 | 2025-11-18 04:21:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daa7d180-04e3-36e9-855c-cca52b200644 | -6.85365 | -46.11203 | 2025-11-18 04:21:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 578df416-ceb6-37e1-9255-13985dd6ec83 | -6.41214 | -47.20169 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb796481-3a94-335a-bc31-3c0ccb35f5c0 | -3.46141 | -50.1204 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4600341-9859-3395-8900-fb87ef018cb8 | -9.3925 | -48.44394 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aad6b7dc-d35c-3102-824e-87da50375c94 | -3.23048 | -50.50678 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 918dbc19-ac30-3942-a02d-32a3ea51ee86 | -3.16527 | -50.16584 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd076b1f-1b9e-306b-9566-12e791db90ab | -4.42098 | -45.91032 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 412dce90-dae5-31db-8dfb-f05df885a602 | -7.3424 | -44.43277 | 2025-11-18 04:21:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2536f6e-8dca-3029-b1a0-01442b4d4bf4 | -3.23115 | -51.18151 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b2aff6d-fcb8-3351-8832-bfa26226a8fc | -6.70807 | -40.79173 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f558fdd7-7bac-3957-b921-cf7f343587cf | -6.44505 | -45.74722 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 028bdbd9-d4e4-3a2a-9150-7ccdbbe85c34 | -10.5144 | -43.9649 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 488e6055-cba4-364b-a158-7d740b99c7de | -4.39754 | -46.57924 | 2025-11-18 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 047a807d-cee3-3073-a4c4-0862bc084e02 | -7.66183 | -40.15191 | 2025-11-18 04:21:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0b6c17ab-b90b-3e97-a7be-bd0d6f1b530f | -9.10128 | -47.78221 | 2025-11-18 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 794e51b0-d003-33c1-9739-d7e7b682b85f | -3.5161 | -50.28435 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f60b333f-29af-3606-acd4-47b05b1870e4 | -10.6204 | -42.32026 | 2025-11-18 04:21:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| febe5093-4e6f-3279-9f9d-c990b8cc9efa | -4.97349 | -41.85228 | 2025-11-18 04:21:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 43f26840-b7eb-3873-8cf1-230352d9a093 | -12.1254 | -39.7459 | 2025-11-18 04:21:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 667600f6-f9ff-3c85-b67e-d7b578930e04 | -9.53565 | -48.34717 | 2025-11-18 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d50b4d0c-fe75-3dc2-99fd-0f77c3adcab9 | -5.25324 | -50.68119 | 2025-11-18 04:21:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 836773ba-0a3c-366b-b350-dec7d279447a | -8.2104 | -45.03907 | 2025-11-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdb53117-d99f-3e1e-86e6-4d65d7e90b5a | -4.31116 | -46.70569 | 2025-11-18 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e20174e4-9322-3617-a16f-29dd2f80148b | -10.87397 | -44.88023 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b873b05c-6cc5-34dc-8cd0-177ffd91d356 | -3.23122 | -50.50236 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1ffe7f8-d780-3cac-ac6d-a34c9ff01c92 | -10.51269 | -43.95338 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b116fb95-639c-3da8-8ed9-ceba8f6d0230 | -2.34037 | -55.80202 | 2025-11-18 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6a36e8d-da63-359f-a66e-fe3fd259e946 | -4.42803 | -44.01511 | 2025-11-18 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1431495d-358e-3176-ba6a-aa8f658b0755 | -3.46855 | -50.24302 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87508ccd-881f-39a1-95f5-b185ebda1334 | -3.06688 | -51.36732 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39a496f5-6edc-37bc-9592-113b454ab8a3 | -7.68072 | -47.52502 | 2025-11-18 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f86a7824-ef3e-3de1-ad15-cc063f35ff5c | -6.99406 | -46.1861 | 2025-11-18 04:21:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03307749-cd48-3b76-9c93-c734ed621985 | -9.88445 | -44.17896 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| de0d179f-d01f-3224-8d5a-6fb56b6a753d | -8.30029 | -43.9338 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5afc196-13f8-3e31-8df3-09a16070a34b | -6.45616 | -42.31649 | 2025-11-18 04:21:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a3b99dfa-f4a3-3519-b66f-000948224984 | -4.9706 | -41.84787 | 2025-11-18 04:21:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README32.md)
