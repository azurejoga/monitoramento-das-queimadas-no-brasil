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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05d88d90-9b47-3714-943b-a8ec773d6e85 | -21.04442 | -49.59404 | 2026-01-10 04:31:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| cd2e4bf7-3bc5-3f30-8fe5-1cb2c2ad9a90 | -22.09731 | -50.23394 | 2026-01-10 04:31:00 | NOAA-21 | POMPÉIA | SÃO PAULO | Brasil | 3540002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 637d9c51-d0c4-39c8-9085-b1bce736ea2a | -22.13278 | -48.10581 | 2026-01-10 04:31:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0957bead-5e96-3db1-a23c-7760cf81c3a6 | -20.96924 | -48.84299 | 2026-01-10 04:31:00 | NOAA-21 | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0d64a865-bfd3-3b90-be02-ca79c42add6d | -22.82637 | -49.29475 | 2026-01-10 04:31:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c5d33e1-2279-37eb-a67f-1ac238d3c904 | -20.54709 | -57.95249 | 2026-01-10 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8fb8cf2a-502f-37af-bab6-e98fe591d9a4 | -20.26754 | -46.41954 | 2026-01-10 04:31:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4980e47-64d3-3d10-bcf1-86a43c79ee58 | -20.63834 | -49.71193 | 2026-01-10 04:31:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16bd8ee1-14ba-3135-9b02-c2bc365c2f85 | -21.04168 | -49.58977 | 2026-01-10 04:31:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b9d08366-2c3c-3b1d-bc2d-cba3f44990d2 | -20.22035 | -46.48161 | 2026-01-10 04:31:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fef11e0-ed17-3327-b8a0-2ef3efa940c6 | -20.22394 | -46.48211 | 2026-01-10 04:31:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed220356-29df-3d05-a86d-ef506a6d9632 | -19.79329 | -57.38319 | 2026-01-10 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| ffef6f77-29cc-37b6-8917-790d69c862f8 | -19.79435 | -57.37792 | 2026-01-10 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 02995efb-319d-392f-82b4-16d587636852 | -22.13462 | -46.9388 | 2026-01-10 04:31:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b1a0382-22c7-30d1-b0cc-d9f220c24660 | -12.3754 | -58.0521 | 2026-01-10 04:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| ea7dadd3-e042-3980-a41c-48852ab96a29 | -12.3946 | -58.0307 | 2026-01-10 04:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 2503a85a-745b-33a4-8c6d-afdfc3432d42 | -12.3756 | -58.0322 | 2026-01-10 04:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| ea7d2af7-71bd-3301-bddf-9613cba5f78d | -7.4943 | -45.576 | 2026-01-10 04:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 7f5cbe70-931b-313a-a33a-532ac586d275 | -12.4133 | -58.049 | 2026-01-10 04:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b4d20f0f-a3b9-3f9e-bc18-0bc4132c584a | -12.4135 | -58.0292 | 2026-01-10 04:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 951515d2-423d-38a6-8000-bba65e27e976 | -12.3943 | -58.0506 | 2026-01-10 04:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| e2daeb3f-7c6f-301d-af26-5fb03cf026ab | -12.3946 | -58.0307 | 2026-01-10 04:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 64468cca-c4ea-306f-b7eb-6eae1d523438 | -12.3756 | -58.0322 | 2026-01-10 04:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| b19f29b3-5fbe-341e-90a9-90dcee74def4 | -12.3943 | -58.0506 | 2026-01-10 04:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 48e57df4-662a-3945-b2e2-800cf5075578 | -12.4135 | -58.0292 | 2026-01-10 04:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 53a0c801-ce3f-3009-ba0d-ff3fee18bbdd | -12.4133 | -58.049 | 2026-01-10 04:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 98f2207a-785d-39b0-b7cd-c538f9da12d6 | 2.10584 | -55.76134 | 2026-01-10 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9850fed8-4600-3944-8c41-92df5031851e | 2.11041 | -55.76426 | 2026-01-10 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4d03bf5-da2d-3dd2-a9e4-587904fd4616 | 2.11443 | -55.7636 | 2026-01-10 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 542ddd2e-c93f-36a0-8b60-0f5404c248fb | 2.10638 | -55.76485 | 2026-01-10 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb76c8e1-7118-3d31-8090-7f3813e63ace | -5.49413 | -42.16959 | 2026-01-10 04:55:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8f8d9f5b-1ae9-331f-aff6-5f0c9ab69a09 | -1.08292 | -46.7747 | 2026-01-10 04:55:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db5209c5-1827-3239-867e-ef3f888249be | -2.19769 | -46.38969 | 2026-01-10 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be671a17-04bc-3695-8b0d-6f6e928e9f27 | -6.15767 | -46.96348 | 2026-01-10 04:55:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fd97978-df17-32ec-a4b7-9194513adc2e | -1.7054 | -45.81087 | 2026-01-10 04:55:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec1d6557-bab4-3171-9781-7c1bdaab7a09 | -1.7097 | -45.81148 | 2026-01-10 04:55:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d176236-2c4a-35e9-8585-a427d15c5749 | -1.37699 | -53.83804 | 2026-01-10 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55f58bac-e66d-3b67-89ed-4395611ad4ef | -1.10469 | -46.61282 | 2026-01-10 04:55:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a64f900-473d-3091-9ff1-b2bd497bb116 | -1.71031 | -45.8075 | 2026-01-10 04:55:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acf6fc26-550a-31db-ba09-c13d3d801d32 | -1.13903 | -47.12271 | 2026-01-10 04:55:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a27c30c-d4e5-32b8-9cf5-8da21056c1ca | -0.877 | -51.99715 | 2026-01-10 04:55:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| decce90c-f882-33a8-ac42-df7609dcd23b | -1.71873 | -54.6293 | 2026-01-10 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 540c41b3-0ff5-39f5-bea1-37b5e75d5b68 | -2.78869 | -43.34746 | 2026-01-10 04:55:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa750169-d4fc-3b70-85c4-8aeb5677fff8 | -0.73667 | -50.6569 | 2026-01-10 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22f1de29-de8a-3271-bc7f-318f200de6c8 | -0.11724 | -51.45305 | 2026-01-10 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fd47da7-8636-3c9b-8843-c72239640e4c | -1.10413 | -46.61629 | 2026-01-10 04:55:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c2ae502-8d8f-3de2-8b57-c57e34c64fb8 | -2.7873 | -43.34705 | 2026-01-10 04:55:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cff3e9fe-54a7-3114-af3f-dc53a78db009 | -4.33969 | -44.12929 | 2026-01-10 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c0e8d13-8362-35d8-9ca5-f1594118f583 | -1.70111 | -45.8102 | 2026-01-10 04:55:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1231a473-e5a2-3ae5-8f26-ee7fd266a856 | -2.24585 | -46.41526 | 2026-01-10 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea076fcc-750e-3e8a-9d60-52fa5c6dd492 | -1.0849 | -46.77116 | 2026-01-10 04:55:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d54ec280-9973-3a1d-ade4-56086606f3d2 | -1.68636 | -53.19247 | 2026-01-10 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d30b0b3-148d-305a-8327-753b5b561ddb | -0.87755 | -51.99368 | 2026-01-10 04:55:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b84dc904-0e85-357a-91d6-3ecbbd5770e3 | -4.34052 | -44.12369 | 2026-01-10 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b192d784-0c56-3c35-a6a5-83330ffdc729 | -2.57954 | -54.72771 | 2026-01-10 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8b0e2e9-84e5-3402-8a0c-06a735c65e35 | -0.14337 | -60.73845 | 2026-01-10 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac886183-735a-3bba-bcd4-809db39338d6 | -1.15868 | -50.6833 | 2026-01-10 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d0dd127-7b66-3130-8f3b-52e18ae257b4 | -0.80761 | -51.90119 | 2026-01-10 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15790a1c-005d-368b-ab28-10ecbf3b302b | -1.58537 | -53.9551 | 2026-01-10 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc3ae6c6-9fbc-31aa-81a5-2f4cfc442fa9 | -1.37606 | -53.83463 | 2026-01-10 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbaae193-b477-3947-8266-1121641ac699 | -2.46776 | -48.05979 | 2026-01-10 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 686b58ad-450f-324c-9e8b-8ae0582fa998 | -0.09027 | -51.27942 | 2026-01-10 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 78c57cdc-ace1-35e3-a39f-55f0b15ec22f | -1.68975 | -53.19301 | 2026-01-10 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d3c83ba-65f1-3de7-bbec-60cfaf5d6c88 | -1.70479 | -45.81484 | 2026-01-10 04:55:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21e84326-ce54-3854-b60a-968c873d50ef | -0.14885 | -60.73923 | 2026-01-10 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bec9fdde-d9ac-3b25-b403-eb7625b880a3 | -3.64393 | -42.0207 | 2026-01-10 04:55:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3b5d5693-41b6-3f0a-9208-5dec23d7121e | -3.64801 | -42.0228 | 2026-01-10 04:55:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81b79257-417e-3851-a05c-5004bb508baf | -0.08694 | -51.2789 | 2026-01-10 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d6f9b992-20f3-3206-aa3d-d4bcab4e60e6 | -0.14829 | -60.74281 | 2026-01-10 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7daebe59-defe-38d2-9a63-7c806ee926f3 | -0.12056 | -51.45357 | 2026-01-10 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d110b9db-074a-38c6-a931-83fbd118f295 | -0.81093 | -51.90171 | 2026-01-10 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aebca1b-2a92-3cd4-8689-1b42af55442a | -3.7891 | -54.40865 | 2026-01-10 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f99a9f0-24fc-3498-97f1-daf311fdb84e | -3.79257 | -54.40924 | 2026-01-10 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9f38bbd-0879-3228-9159-0ba3b0ff072e | -2.14619 | -54.39398 | 2026-01-10 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8df6cae-8f20-32b3-9ef3-a94c95c6649a | -3.64966 | -42.02152 | 2026-01-10 04:55:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8fabd870-225e-343f-b590-5c2e4b422e05 | -2.19354 | -46.38899 | 2026-01-10 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d5bbc52-0b25-3330-ad72-34901e2f120e | -12.40399 | -58.03395 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2458ee15-9996-35cc-b444-07f726b5fd06 | -7.49317 | -45.56355 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2df09f4e-a5c5-3de6-90c4-5fdec857de0d | -9.03879 | -46.98375 | 2026-01-10 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ebc7643-66f5-389c-aa85-8bb75a2bbc0e | -7.49071 | -45.58258 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 02fe60c2-f05b-3cdd-acb0-bb668a58469c | -9.04322 | -46.98438 | 2026-01-10 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e1108c4-2e86-3339-a2ef-fd243f534721 | -13.16867 | -56.88514 | 2026-01-10 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c9eaa8a-7d3f-3896-a070-70277fcc97e9 | -12.39406 | -58.04647 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb3f520f-7688-3e62-bb5e-0be7ddecffee | -7.36497 | -47.02575 | 2026-01-10 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16cc4504-c379-3b90-b7e0-42602f461071 | -12.39862 | -58.04252 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 68c57dc9-f216-3189-910f-7fcf32a92e07 | -12.38399 | -58.0374 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 370fc635-859d-3f9c-acbb-f281bd2d46cb | -12.38896 | -58.03128 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1edd817-df47-3fb5-b9f6-74e0a5f4a98b | -7.69957 | -46.85036 | 2026-01-10 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59105a96-3984-36e4-8806-0b90228989fb | -12.39325 | -58.0511 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7a2d4f1e-72e5-3b42-bd5a-643767678ed3 | -11.83832 | -48.64288 | 2026-01-10 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1b35c1ec-a4b3-32ef-9309-8c245c670c18 | -12.39272 | -58.03195 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46d95f98-dd45-31a9-8487-6d84ec9af0bd | -7.49039 | -45.58389 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 031f687f-4ac2-36b0-8c23-8c3c16c74698 | -12.40614 | -58.04387 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6ed18f5d-66c4-3531-bed5-2c8dd61b322e | -12.38358 | -58.03989 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b72b489e-89ff-38ca-9273-0a74d84c96c7 | -14.26704 | -47.83294 | 2026-01-10 04:57:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c82a8ac-d361-3f65-b77f-45e9f6b75d03 | -12.40158 | -58.04782 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 561ce077-9a03-388d-9e36-0a3383624df6 | -12.2902 | -57.39553 | 2026-01-10 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 464414b6-d8a8-3fcc-a6af-5ec8bd8686eb | -11.80867 | -58.18021 | 2026-01-10 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca0e5a3-35df-3511-8ff4-ebddaaf8b4dd | -7.36066 | -47.02517 | 2026-01-10 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfa8297d-8d73-3b02-a61b-2fbffa5d1049 | -7.48595 | -45.58188 | 2026-01-10 04:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README10.md)
