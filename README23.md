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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 996659fb-8cd3-3023-b54c-e1dc572057ca | -8.89963 | -60.57917 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c1c52c7e-d85a-355d-8e61-71727ede50f0 | -8.64931 | -54.71922 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3b2a988-cb78-35d9-aabc-378a0e748fc4 | -6.86695 | -43.87788 | 2026-08-16 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96ddfd1d-7d49-3140-8995-250d68112591 | -8.90385 | -60.58831 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0aa5239e-8251-3257-b0c8-473056d70947 | -6.71293 | -58.94305 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f61e95ac-545d-3097-b684-a69e610fdc68 | -7.01093 | -43.26732 | 2026-08-16 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a44a3697-6a5f-3d29-b390-c548d7388dc1 | -6.8295 | -56.46107 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66c104f2-0066-3c02-a287-705c9d9f2d52 | -7.0127 | -45.90957 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9a083ee-ec60-35d0-941c-d3a9c5f974aa | -6.63753 | -56.39755 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe532da7-0f0b-3f3c-918b-1a46cb7ffef2 | -11.33014 | -46.21493 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae8c378e-d0eb-33d4-b51a-3886acf8de65 | -6.95932 | -45.89844 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a19f0e3a-c221-32bc-b6e2-f590fe6f0330 | -6.61696 | -58.98719 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9c76836-e735-35a0-8334-60b85548b0fd | -6.6999 | -58.97021 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2226916d-fe03-3ce0-8fa6-4ed670114cf3 | -7.53364 | -55.58575 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea8112f4-0dad-3463-a63e-7018fb688749 | -12.23669 | -43.13786 | 2026-08-16 04:40:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2154bfbb-cbb7-389c-adce-779d711ee888 | -10.94224 | -57.11489 | 2026-08-16 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51cf9d47-d880-313e-b5d5-b01cf1ebc13d | -9.9801 | -53.94222 | 2026-08-16 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a166c3e-2b14-3a74-af89-a20c9f5d8be4 | -8.60528 | -54.69436 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb546de5-5355-3db1-b49a-5924e62179dc | -6.8307 | -56.41957 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78803703-0682-3ab3-92d1-90a65dd14674 | -6.3751 | -58.32094 | 2026-08-16 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b93cdc9b-05b2-3c6b-a678-70d5a54f9817 | -6.79021 | -58.78844 | 2026-08-16 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 929628db-0e78-307d-9a22-18b7493d8591 | -6.61816 | -58.98023 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dde3cd37-da1a-30ae-ae5c-119d29072647 | -8.8975 | -60.55463 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 988c252b-1580-3a92-b212-10f862ef525f | -6.70112 | -58.96317 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| badcc59d-de10-32d2-afdc-26ff6b4b8ee7 | -7.42686 | -60.018 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60f66016-580f-3835-9690-8c19cfdda3ea | -11.06559 | -47.25964 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e41fa0d4-aa0b-36b4-bb0f-a00207c593f4 | -8.96285 | -60.52767 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a9189437-2e3b-3740-b725-09c0189133b9 | -7.58944 | -60.89064 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70c3816d-3f64-373f-af62-dcbf3b2efbd0 | -6.51525 | -49.84716 | 2026-08-16 04:40:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3919c9bf-174e-3279-8b2f-c1af72f5f80d | -6.71541 | -58.92933 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fd68a190-9361-3fa7-9505-a8bdf52cf663 | -6.71417 | -58.93621 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 10b49db0-624e-3227-bf94-720927193336 | -11.13897 | -49.04089 | 2026-08-16 04:40:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fe3cb13-fb99-3062-bdfc-7cca112fa6b3 | -10.15616 | -48.09195 | 2026-08-16 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 445b54d8-32ae-3dcf-b0c0-5d59f7cf5949 | -5.83579 | -50.18789 | 2026-08-16 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09d4a7f5-0f80-355f-b1fb-073e8b30e304 | -6.96588 | -59.30022 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1594fef7-efc7-3130-bc63-765534d71c58 | -11.08175 | -50.95693 | 2026-08-16 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1072a125-9048-39a2-897e-1d0f71877810 | -8.90308 | -60.58911 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4d33abf-48bd-3354-99bb-f12a00b925dd | -6.3792 | -58.32815 | 2026-08-16 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b11d6bf-c662-3f02-a8b3-ede76c33e35d | -10.5348 | -44.85109 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc83b3b4-20fa-3665-9571-7711a35be1b5 | -6.97301 | -59.00661 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ca57a314-be0f-31da-8b8a-b30355c7c221 | -7.58428 | -45.03255 | 2026-08-16 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2019713a-8d56-3372-9dd6-230c6976aecb | -6.85693 | -56.43731 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6806d3c-2919-355c-80ed-2631fe78279c | -6.83216 | -56.41919 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb61967a-dfb2-3ba0-a317-685d9a5b6bee | -12.00321 | -46.42052 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66fd5dea-e654-39cb-9b1b-0c66c7a031ba | -6.30751 | -43.62259 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 6c7bdf85-4f06-30ff-8ce3-c33822c5e24b | -10.52593 | -44.85368 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24bf204f-9867-3449-b09a-43dd68cf1ba0 | -11.87565 | -51.95676 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf0c42d9-9773-3a2d-87f9-feb0d502a4c9 | -8.94093 | -45.46421 | 2026-08-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dcb496b-d5ef-3fee-b3a5-481cda866902 | -6.86538 | -42.90555 | 2026-08-16 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 224ecd28-1e28-3251-98f6-71c48307c66d | -10.27783 | -48.28955 | 2026-08-16 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 16b81280-f740-33b6-bc48-7a696c7e49ef | -6.86222 | -56.43368 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbafe989-ca22-3322-9088-dd03832ada84 | -9.4839 | -51.61112 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 157f1e41-9ea6-3e11-9fba-0d4ae5b48bf3 | -12.01275 | -46.43703 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cd2cac32-0586-3de0-b2e1-fa3ab45da9ae | -11.0856 | -47.24978 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0af4814-c2ae-3e2d-87cd-f29570de91aa | -11.87738 | -51.94595 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c1c9b8f-0faa-36d1-aee2-32fb31122b3e | -6.6198 | -59.0456 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 933031ee-6f53-308d-b7ae-88aed6a9e15e | -6.83746 | -56.4348 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cafb1a24-6fdc-307b-a8e1-3eaebd6f73ae | -8.60444 | -54.69941 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e85eb12a-c5d6-3096-a421-3a50a2a679ef | -9.114 | -46.38741 | 2026-08-16 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c1d07e8-0e3d-35cc-9727-662a8b7f1901 | -8.96732 | -60.50374 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 140418f3-00bf-381d-a0f2-4afd1b1ba673 | -8.95061 | -60.52971 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ffbf4c0e-e16c-3cad-978d-053dc68207a7 | -8.65935 | -54.7313 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28e65a1f-124e-3750-bbe5-f5f7132e6133 | -6.78214 | -55.84496 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df5c9f0b-5136-39a7-9016-5ce09faa7e84 | -7.35035 | -59.59333 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8e6f77a-210f-3aea-a9eb-8c911e070aa5 | -8.95146 | -60.58853 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3948c88-ca1d-3d8e-90ca-88d94aec9015 | -6.30809 | -43.61856 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 0c814577-ebfb-3baa-8ac9-2d87d8c8fbb1 | -6.85025 | -56.42218 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 613a4a3f-e0e3-38a0-bd7c-c8e3646ee918 | -6.42867 | -60.07645 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a3aa31e7-010b-3e8b-8a88-1a47696b3fc5 | -10.72024 | -52.11113 | 2026-08-16 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 899a76cc-4f74-33a5-a6b5-184937334272 | -6.82816 | -56.44205 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 305e13ac-76e3-38bc-bb1c-22a2ae79b070 | -9.10215 | -46.39048 | 2026-08-16 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44d032bf-0ab6-36e2-a65c-14ffcf7b1a5d | -6.21642 | -47.73178 | 2026-08-16 04:40:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ac0cc570-ab49-3591-9c32-2dbfc2b2d77a | -7.21991 | -41.53358 | 2026-08-16 04:40:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7684a2f7-49e3-3809-9d21-77da0d536a37 | -7.0046 | -45.91296 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2a67061-d4e7-3c6e-ba10-4b369f1160f0 | -7.27623 | -44.71727 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e111511-fab1-31aa-8602-f98c3428d8c6 | -7.00897 | -41.43134 | 2026-08-16 04:40:00 | NOAA-21 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9e5b3f90-cd0d-3234-8a6b-4602cc0e8bc4 | -8.95364 | -60.51357 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d4f794cf-3971-3f2d-9cbf-9a8fb7c41594 | -12.01659 | -46.4377 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 86dafe44-95e0-34ff-80f5-51dd531dcff6 | -9.48785 | -51.60807 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02cd6dc9-f63f-33e4-aa0d-8f4f9d5c10cf | -12.56195 | -47.84964 | 2026-08-16 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e915fa2b-492a-3579-b626-6d55e8c524f8 | -6.83881 | -56.43438 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 019d5ccb-7bd8-340f-ae9c-43862907cbd6 | -6.88213 | -56.50797 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2e14df8-7a25-315e-8eed-db30a5477a87 | -6.61439 | -59.0446 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 941c98c6-e949-3d85-96ba-d711d8ea2b2a | -6.70986 | -58.95999 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c11d7af1-48d9-3a94-9a42-a4b083d5488b | -9.48316 | -51.63707 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1aa0072e-36d4-3954-baa2-890b7eb0714d | -6.64946 | -56.40945 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d33f21c9-5701-38af-988e-1cd022d8199a | -11.70845 | -49.07412 | 2026-08-16 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b07e64b6-21e8-3c61-88eb-7051bb318f95 | -6.61724 | -59.05988 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e92f6ca-409a-3be6-aae1-7324827e204b | -6.70947 | -58.94703 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e8a982b4-2049-3cb7-b33b-79f7a6b1d6fb | -6.69822 | -58.94804 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 35d38df8-bd6a-3630-b1ce-f300539b848c | -12.00957 | -46.43153 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5acb1859-e1a9-3eff-98d9-b29ba219f70d | -10.2767 | -48.2971 | 2026-08-16 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dc8fc3f-64e3-310f-abfb-2292193209da | -9.27294 | -56.90164 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e61215a-d165-3e5e-b3a1-06a986bc13a4 | -6.85995 | -58.9725 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8a07adf2-e0a5-3d5c-b3c1-9290c4dfed98 | -8.54215 | -54.5891 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2782f22b-efef-3a8b-86d1-80c4771ef6fe | -10.5301 | -44.8543 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eefbfce9-93ec-3c5b-835d-1c9d67a719f6 | -11.19834 | -54.82833 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff0b164a-41b4-35d7-bec3-6cafcd4ab7eb | -8.95936 | -60.51464 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fda70bdd-7dd0-357f-99c2-6721e75c631a | -8.65323 | -54.71992 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00cd9380-173f-33af-80cd-7d44dd38c7b2 | -8.96933 | -60.52471 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |


[Clique aqui para ver as próximas entradas](README24.md)
