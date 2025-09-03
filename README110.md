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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ab18f2c-3d52-3257-9484-7e533fd00b34 | -6.2038 | -43.3475 | 2025-09-03 11:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 89ea748f-a30e-3600-a315-79e6c8da777c | -5.908 | -57.7311 | 2025-09-03 11:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 8c31225e-674a-302b-8672-a98579de4779 | -11.5779 | -52.115 | 2025-09-03 11:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 1dee048d-1406-353e-bee5-f455de1a34ca | -11.5969 | -52.113 | 2025-09-03 11:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| f95e91fa-78ee-3b64-861e-098577173a58 | -6.3689 | -45.6483 | 2025-09-03 11:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 374d0f2c-b89a-39c9-b517-ce04d2c6ff71 | -6.3687 | -45.6709 | 2025-09-03 11:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| a95fa307-a970-3acc-a354-e24d0c065227 | -7.7226 | -48.7355 | 2025-09-03 11:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 117.4 |
| e682d234-2ab5-3538-9d07-95b6df6569f9 | -11.5779 | -52.115 | 2025-09-03 11:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| e0696d8f-5a13-3860-9b4f-e82e05b668c5 | -6.3502 | -45.6498 | 2025-09-03 11:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 213.1 |
| b51c7ddf-392f-3c04-ad81-19219f35df95 | -5.7677 | -43.8698 | 2025-09-03 11:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| b17dc5a6-0981-3345-8bfc-cd73845f0002 | -6.2038 | -43.3475 | 2025-09-03 11:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 18ea7b7b-e406-39a5-bf93-912ab48000cc | -6.35 | -45.6723 | 2025-09-03 11:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 7557d2cb-8cf3-3064-abd9-c299c1ed15b6 | -7.7224 | -48.7572 | 2025-09-03 11:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 438.7 |
| 725d3ffa-3aca-3b61-a5c0-06ce7593e6f9 | -11.5776 | -52.136 | 2025-09-03 11:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 427ba029-b3b2-37e4-a009-c32dbe1480f0 | -8.0608 | -45.3636 | 2025-09-03 11:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c0244417-577c-3977-94d4-fbddf4531b93 | -11.5966 | -52.134 | 2025-09-03 11:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 1282a8ed-3a80-3d47-ac1e-301a5f8c4b9f | -7.7036 | -48.7587 | 2025-09-03 11:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 277.4 |
| 6d6ad29d-246e-30af-a24a-bf76d9445fc8 | -5.8111 | -43.2156 | 2025-09-03 11:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9853ff31-12d8-3715-9953-fa6b959845fd | -6.3502 | -45.6498 | 2025-09-03 11:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 3716e806-2877-3c25-9203-324aca47af12 | -11.6346 | -52.13 | 2025-09-03 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 606e5706-95ab-3677-a2a0-4c6573b27a2e | -5.7677 | -43.8698 | 2025-09-03 11:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 54ccd176-55e6-35f6-8cd0-aed9537dd292 | -11.5776 | -52.136 | 2025-09-03 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| b28dca32-0a23-3cf9-a5fc-424c97fde584 | -9.7427 | -49.414 | 2025-09-03 11:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| afc141a4-9798-307d-ba72-2a7a6cf43e45 | -11.5779 | -52.115 | 2025-09-03 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 1bc4ce50-0507-3df5-af98-56cc4dc505e9 | -11.5966 | -52.134 | 2025-09-03 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 9b599113-b65b-3460-add5-961a75c25933 | -6.2038 | -43.3475 | 2025-09-03 11:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 221.4 |
| b14c1690-ce75-3afe-a999-4591c417d625 | -9.6232 | -47.0416 | 2025-09-03 11:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| c482ca78-6006-3d26-a3b3-9384fb84c288 | -5.8109 | -43.239 | 2025-09-03 11:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 338f6c11-46c5-3cb1-8b2f-30eee78f4bd7 | -11.1224 | -44.6521 | 2025-09-03 11:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 5778b49f-09db-3017-b40d-ce446fb39711 | -10.4853 | -50.346 | 2025-09-03 11:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| b38bc42e-189a-35e2-9e8a-37abae5cc07d | -6.35 | -45.6723 | 2025-09-03 11:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e98bc3d6-7a9d-344a-980f-361b699ba273 | -11.5969 | -52.113 | 2025-09-03 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 77d37731-3cb3-37b7-9707-3f2f0578d6c5 | -6.7784 | -45.8855 | 2025-09-03 11:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 02ca1adb-6bb9-32de-97fc-36e57de88c0a | -7.7066 | -50.3188 | 2025-09-03 11:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 8e7b53b6-190e-3bf6-b02e-93321a8b8eac | -11.1224 | -44.6521 | 2025-09-03 11:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 2aa53edc-7df1-38f7-a775-261e1c939fcc | -10.4853 | -50.346 | 2025-09-03 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 10433706-08f3-3d65-bdce-c92193f006eb | -6.7782 | -45.908 | 2025-09-03 11:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| e8b41179-f300-3290-9111-c81d0ebab1c7 | -5.8111 | -43.2156 | 2025-09-03 11:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 10c001aa-e2d0-387a-a5d7-5120489a5c86 | -6.2036 | -43.3709 | 2025-09-03 11:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 2b52ecf4-171d-3138-8b53-507f1f6f4e84 | -6.6982 | -48.4035 | 2025-09-03 11:30:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 102.7 |
| fa5a98a6-9b71-331b-80bf-7ebb55eac95f | -6.2038 | -43.3475 | 2025-09-03 11:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 188.0 |
| b6d6c792-3091-31cc-8315-696970e1646c | -9.7427 | -49.414 | 2025-09-03 11:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 41116fe9-ae5d-3254-aae9-e05b54ee8f1d | -6.3502 | -45.6498 | 2025-09-03 11:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 9f36561e-467f-3e05-abfa-dd5e26e0cb08 | -9.7615 | -49.4121 | 2025-09-03 11:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| c9857474-43f6-3050-9732-6cc1c921e4b5 | -5.7677 | -43.8698 | 2025-09-03 11:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 0c4c2676-9be2-3519-b366-f2d22379c215 | -6.7595 | -45.9095 | 2025-09-03 11:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 7feefd0a-153e-310a-8475-2f7aa28b3def | -5.8109 | -43.239 | 2025-09-03 11:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b942fe90-2e9b-39ec-b219-72e0d32e760a | -7.7068 | -50.2977 | 2025-09-03 11:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| a0b1a7a6-705b-32ca-98f6-888f4ec59811 | -6.07965 | -37.46414 | 2025-09-03 11:34:00 | TERRA_M-M | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 11.5 |
| f82c0167-ffac-32c7-a13a-6ce58d33883d | -11.1248 | -44.64382 | 2025-09-03 11:36:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 7eb1600a-263f-391b-b2fb-d9a8c4e0dd65 | -11.95993 | -45.76794 | 2025-09-03 11:36:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 501e982d-ade6-31c7-be71-298b9c5d7f76 | -6.76369 | -45.91615 | 2025-09-03 11:36:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 02e0fc74-154f-34e3-93b8-de9c794de01c | -11.12952 | -44.65062 | 2025-09-03 11:36:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 0333db8d-8418-3327-9116-3e2f647fda38 | -7.95614 | -37.1823 | 2025-09-03 11:36:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b868766e-a739-3fdd-ac5e-8ad032f051c7 | -7.70171 | -43.88072 | 2025-09-03 11:36:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| ca5c6fba-3691-371e-b9cb-84a9887c97c5 | -11.11552 | -44.64837 | 2025-09-03 11:36:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b29daee8-456b-3f65-934f-8e2e9046d237 | -5.81206 | -43.24516 | 2025-09-03 11:36:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 63c0215d-b11f-3301-9d4a-779d76d934de | -11.13374 | -44.62634 | 2025-09-03 11:36:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 5d6072a2-1cd5-36aa-9922-92d06b5be575 | -11.38224 | -43.56158 | 2025-09-03 11:36:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| fbffedb6-450e-35d6-a869-08facba6fd0e | -6.35918 | -45.66309 | 2025-09-03 11:36:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 880154b6-dd93-3b64-a504-d7570e709db1 | -7.48559 | -44.82648 | 2025-09-03 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1480d08b-fc29-30d4-8b2f-d2a34a418803 | -6.2202 | -43.38809 | 2025-09-03 11:36:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 549e083d-3b00-3703-a067-0b6ab389978a | -9.67982 | -47.03218 | 2025-09-03 11:36:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 1cd22979-52af-3813-b1fa-d869caf3a0bf | -7.59815 | -46.22508 | 2025-09-03 11:36:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 0139c665-a688-323c-8eda-cb8bb79c5a0e | -8.46813 | -45.06528 | 2025-09-03 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 277b3911-6c30-3ced-8800-d938de3e570a | -6.19623 | -43.36052 | 2025-09-03 11:36:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 207.0 |
| 3e44b237-de9a-37ac-91df-232e84aa3bd2 | -6.07523 | -44.68023 | 2025-09-03 11:36:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| be5566df-d875-3913-9766-1176690f80a5 | -6.2 | -43.33729 | 2025-09-03 11:36:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 191.9 |
| cd3074cd-30d9-3018-bbdd-c114cc4ea26e | -6.29583 | -43.57836 | 2025-09-03 11:36:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| bfd47a65-ff72-3740-a1db-cb25f293bd00 | -7.60217 | -46.23153 | 2025-09-03 11:36:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 0b4223dc-c50c-353b-a9d4-cfa32afd662d | -6.07088 | -44.68694 | 2025-09-03 11:36:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7834362b-6ee4-3e72-b27b-8358d28f9e7b | -6.34912 | -38.8647 | 2025-09-03 11:36:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 00aaa7f7-1b81-31d7-9bb9-08d117995e8f | -10.14445 | -46.25767 | 2025-09-03 11:36:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 73344e52-043c-36b0-8353-96b39736ba33 | -8.89023 | -45.84383 | 2025-09-03 11:36:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 7fe20a48-0da9-3a0a-8908-102a592b73ab | -6.25379 | -42.59806 | 2025-09-03 11:36:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| a59c325d-196d-3bea-8a6e-1b4367b7f158 | -6.11868 | -45.91547 | 2025-09-03 11:36:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| f268b210-87ed-3101-8240-a3cb564e2bbf | -6.35457 | -45.63219 | 2025-09-03 11:36:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 9cad3fa8-cc60-3b6c-bd9f-e600a2d8c66d | -6.79253 | -44.48397 | 2025-09-03 11:36:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| b654f215-54aa-38fd-8e81-22e4734136ee | -7.70156 | -43.8484 | 2025-09-03 11:36:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 04b4452b-442c-3c5a-9b44-7d38f8046d07 | -6.50414 | -43.07598 | 2025-09-03 11:36:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0a52f3d9-4043-3b9d-bd60-2372f83c14ab | -7.69776 | -43.87276 | 2025-09-03 11:36:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| d880b12e-5de7-3d2e-8eb1-5a8af43271f0 | -7.70575 | -43.85606 | 2025-09-03 11:36:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 1b925e81-c83a-3fff-882f-ea759466959b | -5.77248 | -43.87724 | 2025-09-03 11:36:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 367.3 |
| f5d7d79f-0112-364b-89bf-25ebb4705b0c | -8.47075 | -45.05947 | 2025-09-03 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 234bba52-1262-3ee3-aa5e-a984a2490de5 | -6.20435 | -43.35566 | 2025-09-03 11:36:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 350.6 |
| 08febba6-1f84-32e5-afbe-6c256872ec88 | -7.00757 | -43.23346 | 2025-09-03 11:36:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.9 |
| 576081a0-2211-3505-bafd-56c7a8f58583 | -6.12262 | -45.92189 | 2025-09-03 11:36:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 0315f96e-a410-34a1-9f57-6d166ae7348f | -8.89587 | -45.81014 | 2025-09-03 11:36:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d2e443eb-d774-34b1-8962-eb26bf71f420 | -6.45968 | -45.4025 | 2025-09-03 11:36:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| d5a42d02-529b-3bfb-8ecb-1dbdf996d18f | -8.06858 | -45.37446 | 2025-09-03 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| c74a0e2c-bc6e-376a-b66f-78be6a948717 | -8.88862 | -45.81488 | 2025-09-03 11:36:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 671a5106-96b1-3c94-8e8e-104b06b444f5 | -5.77387 | -43.88334 | 2025-09-03 11:36:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 226.4 |
| eb54f7b8-c7b2-3464-b31a-7fe9be904754 | -6.20797 | -43.33215 | 2025-09-03 11:36:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| ae3cbfe8-453b-342a-ad04-3092aa1c8d1d | -8.43548 | -45.08401 | 2025-09-03 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 977867ed-fa10-3a02-8a4e-eaad8690f444 | -5.81566 | -43.2221 | 2025-09-03 11:36:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 227.8 |
| a2563c47-a6d1-3e18-914e-416ca22e967f | -6.34851 | -45.66796 | 2025-09-03 11:36:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 6a5613a6-5508-30e1-9bf2-fd328e66ac46 | -5.77808 | -43.85705 | 2025-09-03 11:36:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 3d3e7c02-7c7c-3a84-ac27-b6cd7682ddd4 | -5.75932 | -43.88116 | 2025-09-03 11:36:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 229.5 |
| 98f5ab65-66eb-3230-a3b1-6f0aeff89be4 | -8.88271 | -45.84852 | 2025-09-03 11:36:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| fcb48220-6447-3694-9820-ba6b9edb9139 | -6.75935 | -45.90796 | 2025-09-03 11:36:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |


[Clique aqui para ver as próximas entradas](README111.md)
