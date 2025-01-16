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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb5221f4-2268-3d65-bf8c-931d66f327cb | 2.11178 | -61.81396 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47fbbc29-4318-35b3-b557-72cdb31a9d19 | 3.82673 | -59.71918 | 2025-01-16 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfc047a8-ab88-30fb-b429-2821faa3c535 | 3.14046 | -60.70018 | 2025-01-16 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5df21bf3-1b56-307b-8b01-0bcb42cd5084 | 2.17612 | -61.86018 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ed1fcd4-99bd-3d6f-b67c-c57b550851a9 | 1.17083 | -60.49057 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5132f9b2-2b8b-3579-b659-c7f182dec7eb | 0.85042 | -59.53671 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67d2d3e0-15b2-3b79-9a6a-13cc1bc95db1 | 1.32584 | -60.03488 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be1b91e5-5752-3b49-837e-0e71eb0f0f52 | 2.15274 | -61.86278 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7492ebc5-2fa5-3c7a-9690-d5195d871d90 | 4.14765 | -60.0358 | 2025-01-16 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f907e8c2-2d1f-3150-9fd8-dcef44e9d0cf | 2.10587 | -61.82339 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4641adfa-cb4e-3a8a-8497-31362f527ec8 | -1.424 | -55.31614 | 2025-01-16 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13bca5b0-3423-3089-9b7a-396c45f8a09d | -1.41815 | -55.31529 | 2025-01-16 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c63dd487-e732-34cf-a700-da0ef6d7d642 | -7.35237 | -72.9227 | 2025-01-16 05:48:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3dbdb4b-7930-3a7f-8240-8b95650581ff | -16.1099 | -58.19624 | 2025-01-16 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5bf838a5-eb09-3319-983d-0f91dcc44b42 | -16.11856 | -58.17072 | 2025-01-16 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b9200303-43b9-340a-8e45-4c2941a70f98 | -16.11128 | -58.18307 | 2025-01-16 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 394c9df1-cfd7-397f-b8d0-484f84b1fbdc | -16.11265 | -58.16993 | 2025-01-16 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1d1885f8-9ccc-386e-8a28-84fe43e79a90 | -16.11174 | -58.17867 | 2025-01-16 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b1980a15-b98e-33d0-bd62-0ba07c2a4af3 | -16.1158 | -58.19705 | 2025-01-16 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1c6ec064-4cf8-3ff1-b978-e0a65d94a75f | -16.11219 | -58.17429 | 2025-01-16 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e7ad5bc2-d0d6-3168-afcb-b6e55d67b1a8 | -16.11082 | -58.18747 | 2025-01-16 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 798ac82b-eec1-3f45-a0cf-f17a96debecc | -16.11764 | -58.17955 | 2025-01-16 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 953c446a-6f40-3a4f-9ea7-53c9a8f4f4ad | -16.11309 | -58.16566 | 2025-01-16 05:50:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4d1e9fb9-bac8-3cb6-9e99-52c188c02aca | 2.5255 | -60.5843 | 2025-01-16 06:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.1 |
| b061fba3-9f52-30a8-af77-e0879f6e0711 | 2.5437 | -60.584 | 2025-01-16 06:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 938615e7-f507-3ec9-93c8-7c0ffa754e2a | 2.2059 | -61.80495 | 2025-01-16 06:16:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b9236b2b-892f-357d-8b00-41c76ad5bb5c | 2.11762 | -61.82403 | 2025-01-16 06:16:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 5c99a25c-46c1-3d99-ada5-380f540952c2 | 0.72622 | -60.11659 | 2025-01-16 06:16:00 | AQUA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3bb28b93-aa01-361c-9272-202d05009178 | 1.29512 | -60.43292 | 2025-01-16 06:16:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 80a922c2-0573-319e-825d-91d992c7600a | 1.3587 | -60.30292 | 2025-01-16 06:16:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 83dc2253-4614-30df-a66a-f33ce27841fe | 1.29476 | -60.42649 | 2025-01-16 06:16:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3d821abb-72a2-3be7-baa9-a9ec5973fe1b | 2.17813 | -61.85627 | 2025-01-16 06:16:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 39842286-f0df-3c39-8001-9f4ed51c892b | 1.18109 | -60.48631 | 2025-01-16 06:16:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cf0c2cba-d513-3d9d-aef3-cd9cd68eec2f | 0.8444 | -59.53782 | 2025-01-16 06:16:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 86735352-90b5-3ba7-9f6e-7c59ac651c44 | 0.85395 | -59.5365 | 2025-01-16 06:16:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4e1e5ca5-ccc7-3f0f-8d1b-3206543ee7d3 | 2.19438 | -61.80645 | 2025-01-16 06:16:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5fc2ce3e-70da-3060-b4f8-8bfc82d67f0e | 2.11533 | -61.80857 | 2025-01-16 06:16:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 1292b0a3-db10-356b-863f-b9ad5c59bbc8 | 2.5437 | -60.584 | 2025-01-16 06:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 927bd5f7-4ccf-3185-a407-b0178e76405b | -16.11235 | -58.1767 | 2025-01-16 06:22:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.7 |
| 9ca024f5-8d32-3fa7-8b0b-9859cd7b0997 | -16.11384 | -58.16603 | 2025-01-16 06:22:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 65618ded-7778-3b64-af69-c9ddc10531c9 | -16.11537 | -58.18383 | 2025-01-16 06:22:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9bf04e8c-b5c3-3c65-ae54-0181d3068edf | -16.11682 | -58.1731 | 2025-01-16 06:22:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| d8be6dcb-2282-3efd-a3d5-977bad5bff59 | -16.11085 | -58.18741 | 2025-01-16 06:22:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| fc614a45-1dff-36f2-a5b2-bb7b61017e0f | 2.5437 | -60.603 | 2025-01-16 06:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 3d53b070-f9e6-3803-a182-b8fc4e096d3f | 2.5437 | -60.584 | 2025-01-16 06:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 6e7a96eb-39fb-3f7e-a7ff-9a52902e5665 | 2.5437 | -60.584 | 2025-01-16 06:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 4a20fae6-5ba2-37ca-95b6-7b320dbf189d | 2.5437 | -60.603 | 2025-01-16 06:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a10fa07f-4c20-3874-bf82-2f9acae95baf | 2.5437 | -60.584 | 2025-01-16 06:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f129c595-b5ba-3719-9e3b-8f69b6fe51f6 | 2.5437 | -60.584 | 2025-01-16 07:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.7 |
| a63d1e80-1608-361b-a8d0-5b33f9a62f72 | 2.5437 | -60.584 | 2025-01-16 07:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2d0965ed-c482-3eff-8728-fe37b756c0b1 | 2.5437 | -60.603 | 2025-01-16 07:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 34.6 |
| cee4a908-fcbf-3adb-9673-fa4a414a319f | 2.5437 | -60.584 | 2025-01-16 07:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 2637fa49-6de4-302e-ae2c-74a10b3285b2 | 2.5437 | -60.584 | 2025-01-16 07:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f33ecaf4-7119-3c33-90fa-729732cb2e26 | 2.5437 | -60.584 | 2025-01-16 07:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| d41e5c92-5005-394e-a725-2bd13cc70e32 | 2.5437 | -60.584 | 2025-01-16 07:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 063672e4-939c-3643-936b-04c71e89dce1 | 2.5437 | -60.584 | 2025-01-16 08:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5b4cd4b4-8ed8-33de-a145-24e234d634cf | 2.5437 | -60.584 | 2025-01-16 08:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| adc3c08c-82ef-3f9c-8633-ddf3d631fedc | 2.5437 | -60.603 | 2025-01-16 08:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 34.1 |
| cda6a8a0-c037-3f2e-b3bb-7ec4e3a8fbae | 2.562 | -60.5838 | 2025-01-16 08:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 33.6 |
| d91e5f4c-8035-32ba-969c-2257d4006d0d | 2.5437 | -60.603 | 2025-01-16 08:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 84b94407-729b-34d3-b247-731a96026879 | 2.5437 | -60.584 | 2025-01-16 08:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 25046fba-895f-3453-b0ae-7be102b15053 | 2.5437 | -60.584 | 2025-01-16 08:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d1afacdb-bc5e-38e3-8cbc-e9248c77a539 | 2.5437 | -60.603 | 2025-01-16 08:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d87c39aa-9b6b-3314-b6c2-0ac3491790a6 | 2.5437 | -60.603 | 2025-01-16 08:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b8b7130b-f100-3957-a726-e41889b63a94 | 2.5437 | -60.584 | 2025-01-16 08:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| e18b3d4f-923e-3e10-987e-e52710467154 | 2.5437 | -60.584 | 2025-01-16 08:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.7 |
| ba5306e2-f80c-3b64-8eb3-992811c132bf | 2.5437 | -60.603 | 2025-01-16 08:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4ff1f048-1a0d-365a-9d30-a9b41150317a | 2.5437 | -60.584 | 2025-01-16 09:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 6cac0b03-29e7-304a-b23c-4d10b7665f20 | 2.5437 | -60.603 | 2025-01-16 09:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.8 |
| e1f92a78-34d1-39b5-85a8-2d7e44be23b4 | 2.5437 | -60.584 | 2025-01-16 09:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f76daefa-9489-365d-b4ca-22e4e846cc0d | 2.5437 | -60.603 | 2025-01-16 09:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 4b5bfbd5-5bae-3210-b068-1d2ca58d61eb | 2.5437 | -60.584 | 2025-01-16 09:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.7 |
| c37ca669-83ff-336e-89e7-8cfabee97efc | 2.5437 | -60.603 | 2025-01-16 09:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 8af69a4d-9106-33a6-aad6-19e8894dea73 | 2.5437 | -60.584 | 2025-01-16 10:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 10c67e1b-3e04-3fdb-b924-b6076c4986e2 | 2.5437 | -60.584 | 2025-01-16 10:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 4080a48a-4cee-3949-b73c-f392f8235b15 | 4.1537 | -60.0406 | 2025-01-16 14:20:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 104.5 |


