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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 628d0893-b9a0-3c4e-99a1-8380d95aa117 | -11.6967 | -54.6081 | 2026-08-17 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0abbff43-e8f3-3df5-9807-e4a8937edf4a | -14.4929 | -45.6879 | 2026-08-17 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 0b89ce1d-805c-3cd7-bbe9-a202a030afff | -6.6937 | -58.9613 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e0c47d54-dc40-3dd9-b76c-17176cde9841 | -6.1106 | -57.7425 | 2026-08-17 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 5d080821-d9b6-3862-ba57-69ec85968b3f | -7.3824 | -55.4924 | 2026-08-17 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| e80b3288-edd9-36ac-9f43-6de09a459ee2 | -8.9601 | -60.5165 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fdbff803-1b79-3122-b312-2e8ba9eecaea | -11.7154 | -54.6268 | 2026-08-17 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| fd73f3e0-e411-307e-af3e-a8d788411c40 | -7.4259 | -60.01 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 10444be0-8b34-3361-af89-3d6a7adabd82 | -8.96 | -60.5358 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7b979bd9-022c-3084-9b43-f59d43de8be5 | -6.6938 | -58.942 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| a2136850-c6fc-35c3-b568-00602dec93e6 | -14.4934 | -45.6647 | 2026-08-17 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 780c52f3-43f7-3035-a262-2d6b51c2ed4f | -8.9788 | -60.4964 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 7544f577-239f-379f-9ee7-8be20f19f8eb | -8.5977 | -54.6948 | 2026-08-17 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e4b63c4f-fd6e-3bb9-b046-ca47582b69d3 | -8.9787 | -60.5156 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 6154bd01-b669-3ca9-b559-7a060bcddca6 | -8.9039 | -60.5769 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 8f408319-2d94-31f2-bf0c-07607e7fe49f | -11.1299 | -46.5019 | 2026-08-17 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 6fbe2e14-4962-3a36-8ed6-1a0dbc58abce | -7.3639 | -55.4935 | 2026-08-17 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 9e54d9ca-1324-3f4e-8343-55f91b8acc88 | -10.4655 | -50.412 | 2026-08-17 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 1a5fa5ec-3a08-3c18-ab95-865257d756a8 | -6.7123 | -58.9412 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 003df008-dd3b-30a4-ad85-011979201017 | -14.3722 | -51.932 | 2026-08-17 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| bc0fbf4a-ac7b-3c2e-9658-06818f345840 | -6.1291 | -57.7418 | 2026-08-17 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| acdd47c5-32bc-3125-b32d-7813815b3057 | -6.6568 | -58.9628 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f6df5041-aa4e-3f0b-866a-733fb0ec6091 | -6.6014 | -58.9844 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 30ce48e8-28ef-3e72-ae25-325d10faa9cc | -6.6015 | -58.9651 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| de14a17f-735f-3fa6-8db0-8681cfe7445f | -6.1107 | -57.723 | 2026-08-17 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 6ce0a8bd-d1ad-34ef-b325-7a073a9c7f8e | -6.1292 | -57.7223 | 2026-08-17 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d10ddfc3-6554-3da3-a73f-90217aa6b4c5 | -11.2314 | -54.0164 | 2026-08-17 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 229696ab-b17f-3bcb-bb0f-f86a2b6cc44e | -6.6384 | -58.9636 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 333b7a24-4953-3542-aabe-584ccd966a73 | -8.9038 | -60.5962 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| adf8b3e4-899c-3403-988b-e012ba4dd1d7 | -8.9415 | -60.5174 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8bea9b2d-f370-3a8b-9b20-4a917143a644 | -6.4048 | -54.9441 | 2026-08-17 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 0e61cfd9-28e1-3f0e-97b4-6fe82d23fbca | -10.4658 | -50.3907 | 2026-08-17 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a32d1598-3003-3975-b657-35997754cb85 | -11.1296 | -46.5244 | 2026-08-17 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 0edb25df-a751-32f6-a1e4-6c3c71f73838 | -8.579 | -54.696 | 2026-08-17 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| edff13c3-828a-31dd-b98d-588d34ed5a3f | -8.7224 | -62.9103 | 2026-08-17 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 0dd426ad-346d-31d7-8c1b-792bc66dc918 | -6.7124 | -58.9219 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| a640246f-cfdd-3502-9683-d0e00416a3dd | -8.8852 | -60.5971 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 045901e0-aa7e-37c8-939a-5f160f736fc6 | -6.6198 | -58.9836 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 26e643b6-b434-363b-b8f1-7fbc06f48222 | -8.8855 | -60.5586 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8c4a2837-bb84-358c-b84c-70e5abed2928 | -11.7157 | -54.6063 | 2026-08-17 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 72e3f23d-0096-325e-9a9c-6ae91c3a977f | -14.4734 | -45.6914 | 2026-08-17 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 8a4313c8-5ce9-3d62-9f11-ded0c815ac49 | -14.4739 | -45.6682 | 2026-08-17 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 6b025022-eaf8-3fd6-9785-db8f32e18bf8 | -6.6199 | -58.9643 | 2026-08-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| cf0dde2e-360a-3eaa-ad23-47f765790385 | -8.9041 | -60.5577 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 2b8e333d-faab-3462-9d48-6cc1b23c3416 | -8.9597 | -60.5742 | 2026-08-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 57ef1d10-f4a5-3555-b618-28e5d92bf66a | -11.2314 | -54.0164 | 2026-08-17 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c1af4e37-1ed8-38ef-9479-9258d6a3f2c0 | -8.9415 | -60.5174 | 2026-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0e25bcb5-2466-3e63-9cfa-96392a7af98d | -8.7224 | -62.9103 | 2026-08-17 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 9f25074f-c59e-361a-9d35-07d4e6de8794 | -6.4048 | -54.9441 | 2026-08-17 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b1b5dbf2-b244-39b9-b520-6107877ff511 | -7.3824 | -55.4924 | 2026-08-17 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| dd56e9ae-248c-3474-be0c-931a88c1d355 | -6.6568 | -58.9628 | 2026-08-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d18fac79-87b8-3e01-ae65-4f4df35ae67c | -6.1291 | -57.7418 | 2026-08-17 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 0efdfe58-3412-3478-8061-07e334c0a792 | -8.9038 | -60.5962 | 2026-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| b0b0936f-ceab-3c30-8274-de0c8fa016e5 | -8.579 | -54.696 | 2026-08-17 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 29d5e494-588a-3d0f-abef-76319a3031da | -8.9787 | -60.5156 | 2026-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 6981bd1f-dc81-3673-8105-9637ac6e0f73 | -11.8083 | -44.8072 | 2026-08-17 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 95a85a52-d0c6-3bca-a5d6-978337eb1ffc | -11.7157 | -54.6063 | 2026-08-17 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| c81d099c-baa0-3f2d-b703-fe06629a97b7 | -14.4739 | -45.6682 | 2026-08-17 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 2afa175f-2689-37a2-bb70-245e2e11ee21 | -8.0351 | -55.1539 | 2026-08-17 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f309eb55-1cd2-390a-99cb-5c8244ca4b33 | -8.9601 | -60.5165 | 2026-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d27ff606-fbbb-3872-978d-cb9f243a795c | -6.1107 | -57.723 | 2026-08-17 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 5f17f164-32e1-39da-88a9-5d05dc07f315 | -6.6014 | -58.9844 | 2026-08-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 181b48f8-0179-394d-b24f-133519dd54be | -15.9189 | -55.531 | 2026-08-17 00:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 64956b06-0b40-3f86-9e35-f608b3a4e50d | -6.7123 | -58.9412 | 2026-08-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 3c181efa-a8ce-3c66-87df-7fbd96cdd3ef | -6.1292 | -57.7223 | 2026-08-17 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a93ddc04-20f6-3862-a12e-ae35ffe60d81 | -8.9597 | -60.5742 | 2026-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6af051b1-bfa7-3763-97c4-a94538431e77 | -10.4658 | -50.3907 | 2026-08-17 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| df156a9d-cc16-3cb9-a836-8929cc8ff558 | -11.1487 | -46.5219 | 2026-08-17 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 953d16d2-f7ca-3de0-b0e2-d97f8c252b3c | -6.0922 | -57.7433 | 2026-08-17 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 882be12e-4d03-35e0-8554-a97d9dcb5649 | -10.4655 | -50.412 | 2026-08-17 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a2a97eeb-da60-3c41-854b-1e3897e4169c | -6.6199 | -58.9643 | 2026-08-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 90da3794-5c88-384e-8a07-91125519a556 | -6.6938 | -58.942 | 2026-08-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| ff91ed56-6db1-3da6-975c-eeed5a3eeb1e | -14.4734 | -45.6914 | 2026-08-17 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c9d31869-0ea2-326b-9eaf-d64aff7f7576 | -11.6967 | -54.6081 | 2026-08-17 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 9e0171f0-6cc5-34ed-967f-8b061d744725 | -8.9039 | -60.5769 | 2026-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d27a9383-4fdb-37a5-af7a-e6fd3ef65598 | -11.149 | -46.4994 | 2026-08-17 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e3fd1791-52ab-359b-8fed-f61435e856f7 | -8.9041 | -60.5577 | 2026-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 85d8b1a7-bb24-35fd-affd-2f0818c2d4fd | -6.1106 | -57.7425 | 2026-08-17 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 85870cbd-87be-3ba9-af33-21341a2e4205 | -7.3639 | -55.4935 | 2026-08-17 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 86ddc5c0-9346-30c2-91c6-21d39d16c689 | -11.1299 | -46.5019 | 2026-08-17 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 01e70851-0e60-3bab-9a8d-2f3267031a2b | -11.1296 | -46.5244 | 2026-08-17 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 6219f7ef-c08e-356e-aa60-41fd16101475 | -14.4929 | -45.6879 | 2026-08-17 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 45403312-f174-38b6-9fd0-226e0c1b1d66 | -8.5977 | -54.6948 | 2026-08-17 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7e39d5fc-c93b-3d6d-8169-742c66c78b7f | -8.9788 | -60.4964 | 2026-08-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 834b70ed-3e82-379d-85fa-ebe06d050257 | -6.6015 | -58.9651 | 2026-08-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| d7718d7f-7978-3ac5-bbde-640e90173fb8 | -14.4934 | -45.6647 | 2026-08-17 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 4e7992a9-f8fa-3a3c-b4f3-f881d237b950 | -6.6384 | -58.9636 | 2026-08-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 58214444-4a76-3813-9077-c230087bea5a | -6.6198 | -58.9836 | 2026-08-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 4e84deae-d279-3fe9-81d2-3a767bf76ce6 | -6.7123 | -58.9412 | 2026-08-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 94624ce8-c8cf-31f0-ba29-0465cd66624e | -6.1292 | -57.7223 | 2026-08-17 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 3c955576-a107-3fbe-9999-a634c5e1b5a2 | -6.6014 | -58.9844 | 2026-08-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 3b8d2785-c15a-362f-9245-8dac4a50db10 | -8.9787 | -60.5156 | 2026-08-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| ad0be9bf-d846-3478-8880-32952ca9ac08 | -6.6938 | -58.942 | 2026-08-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| e83f769e-fb14-338d-b8c6-887385bd3d5c | -8.9601 | -60.5165 | 2026-08-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e3266c2b-6f95-3022-8d5e-1bbbd3c50a7f | -8.9038 | -60.5962 | 2026-08-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| abcc7e20-0f00-3a8c-ad0e-157c5fc99249 | -7.3824 | -55.4924 | 2026-08-17 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| e5835c04-fead-3a71-b880-73315a5b6961 | -10.4655 | -50.412 | 2026-08-17 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 65bc88ec-b66b-31c0-96c1-db9d0e469d63 | -6.6568 | -58.9628 | 2026-08-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b37069f3-51aa-379e-bb51-d6aa63048594 | -6.1106 | -57.7425 | 2026-08-17 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 233994e8-d713-3223-86ca-c8736a65011d | -11.8083 | -44.8072 | 2026-08-17 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |


[Clique aqui para ver as próximas entradas](README2.md)
