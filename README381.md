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

## Dados Diários - Página 381

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56831f9f-e4cd-3981-a255-3f18c946d752 | 2.43698 | -50.81205 | 2026-10-08 16:41:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d54ad0c0-e716-30b9-8440-14168e0108f3 | 1.66359 | -55.80271 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3310c7cf-bdbd-3fec-8c65-bae05c7c76a0 | 2.4328 | -50.81553 | 2026-10-08 16:41:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d6ff7c0-9ea5-3dc8-a824-99982bd226fb | 4.22296 | -60.24215 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa0ee895-f329-3e4f-a8ba-544eee7dfdeb | 4.26965 | -60.10473 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c3a71809-ed6b-3497-83fd-2ff54570de6e | 1.65139 | -55.78348 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 82ba7f3d-5d9b-36bd-9f42-65372d680c46 | 4.45465 | -60.95023 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| df8544cd-ba47-3cd7-b290-46c27f2ed0a5 | 4.62323 | -60.47601 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b88bf5d0-2aff-36fc-859d-0b0ad3fc396a | 0.44611 | -60.53488 | 2026-10-08 16:41:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f37c832b-abb0-3cba-98d4-a1d7ad750a29 | 3.67311 | -60.67926 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d14c6479-fb47-3d9a-bc1d-62d9c7b746ea | 1.66447 | -55.79706 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b437eb4d-e0c2-34a9-a1af-feafd9ad0b9d | 3.51044 | -51.25807 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 700110a3-ef31-3011-a17e-88f724f3afb2 | 1.49969 | -55.67736 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b6825fb8-d370-3821-ab9f-63da277a84ce | 1.74025 | -55.58555 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 75c2a70d-be70-335e-8254-4e376e34d46f | 3.71105 | -51.5045 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 31b9cba1-579d-3988-897f-f96db8d71992 | 1.35568 | -50.83611 | 2026-10-08 16:41:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8f25b364-102a-3c3b-a2a8-54fe8d6f441a | 2.77569 | -51.40668 | 2026-10-08 16:41:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a8cfe96a-b4ac-3a0b-b07c-6aa045b37ed1 | 3.73964 | -51.63346 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 902a8db8-965a-38b7-81be-8e3f7ecfc379 | 3.3129 | -60.05543 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 71e90062-f096-3da3-b3e9-8cfcdea20c9b | 4.45381 | -60.94247 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| afb90365-0a1e-3e3c-ae14-4832f1b114c8 | 3.51468 | -51.25452 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 743a5645-3393-3b0e-9a9c-ce2245248655 | 2.10381 | -50.83715 | 2026-10-08 16:41:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9ad039af-18cb-3446-aeec-80dd17c54af9 | 1.69123 | -55.6258 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 8b8c637d-d4b1-3d96-891d-4b4ff72e6bcf | 1.37854 | -50.95889 | 2026-10-08 16:41:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0385fd7b-5860-39ff-9fd8-c87d5c3daecc | 2.45414 | -50.81881 | 2026-10-08 16:41:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9903fac7-78d6-31f9-a5a2-312da8486411 | 1.38151 | -50.96362 | 2026-10-08 16:41:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 61054a34-388a-375f-a3a0-96f00599f846 | 4.78827 | -60.67939 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 088e1c48-81c2-3d36-bd09-500c7a9c7695 | 4.37854 | -59.7778 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a47a1143-7873-353a-a669-98daf5dba140 | 2.11345 | -50.82199 | 2026-10-08 16:41:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1cf3b75c-0b14-3aed-a9e5-76d9e4e450be | 2.09729 | -50.83199 | 2026-10-08 16:41:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a8f7e85f-9c72-3bbe-8e89-09f3f0da5be0 | 1.66523 | -55.79919 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bdc0665b-3faa-356c-916a-46c7dc6ed0ee | 1.69037 | -55.63128 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 36ec83cf-cd1d-3b9e-926c-a71cd763ebf4 | 4.62142 | -60.09265 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 186ccefd-1574-37d4-9eb5-0263becafb31 | 1.65634 | -55.78427 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 79101b47-89ae-37ba-85e8-932ca862f2ef | 3.86694 | -51.79819 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0460c247-e5f0-3051-9ded-5891f0ba2bd4 | 2.0786 | -50.92943 | 2026-10-08 16:41:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e913e368-bd81-3b8e-a204-217ca24c50c0 | 0.69812 | -51.41775 | 2026-10-08 16:41:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5ab60e65-52d3-31e4-bba5-0d1666f234b0 | 4.44791 | -60.94988 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 50734880-b610-3cf6-963c-81ba5c08c693 | 4.45264 | -60.94898 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1fbd1a58-c4e6-3aea-b26f-56ad4dbbd97b | 1.71096 | -55.5955 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| efa30a81-fc49-3bfb-b64f-634669893b84 | 1.69209 | -55.62029 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 670689ee-c3db-3e02-9c9c-bae99b954d3b | 2.53045 | -50.83825 | 2026-10-08 16:41:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f3bac08-8f98-353a-b22d-162ae47ae7b2 | 1.49341 | -55.6744 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c1e12313-fa89-3629-b71c-daa9a1805eea | 1.34847 | -50.83502 | 2026-10-08 16:41:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 134445a6-c81c-315e-95c4-423e526d1953 | 1.76091 | -55.55001 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7fbdf80b-a702-327e-a440-03928cefcd1a | 3.74618 | -51.61402 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6b2a87fe-13bd-3b1e-9a0a-7ead7ecb422f | 3.34491 | -51.30547 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 220458a2-bda2-3bd1-9646-1f9b8c9ed0ef | 2.45059 | -50.81826 | 2026-10-08 16:41:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1e982859-4798-3717-9e3c-59b20973baa0 | 4.27275 | -60.10373 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b714e9af-ab92-343b-927a-658662d6db00 | -5.7319 | -41.6589 | 2026-10-08 16:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 174.6 |
| 1f4071d1-a3fe-3bdc-b27d-4185abe1de79 | -3.3912 | -58.0017 | 2026-10-08 16:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9e5e1b2c-f457-376f-8256-f9d186836dac | -12.232 | -44.7194 | 2026-10-08 16:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| ec9534df-0b05-30a9-945b-44887caf5780 | -12.1545 | -44.7547 | 2026-10-08 16:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 285.2 |
| 7ddced5e-e880-3c97-874a-be310e825126 | 1.6937 | -55.6263 | 2026-10-08 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 82292dbe-7d0c-3634-aef7-16bad01e374d | 1.7121 | -55.6063 | 2026-10-08 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 789de8eb-8b30-3ef6-8eb2-48549065a108 | -8.9501 | -45.1334 | 2026-10-08 16:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 304.8 |
| bd50b2eb-07bc-3106-be84-f2f4f8a2996c | -6.6879 | -45.578 | 2026-10-08 16:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 4f260be0-5ea2-3f2d-9875-8b121a3461a3 | 1.6937 | -55.6461 | 2026-10-08 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ca83b6ca-8432-36c4-bd6d-2ea694f9d648 | -12.1733 | -44.775 | 2026-10-08 16:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| c56be8c1-7644-3f9d-b897-b4ea4aee3a46 | 1.7672 | -55.5463 | 2026-10-08 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 3cac9ac9-9666-3378-9058-8109b01066e0 | -1.3264 | -56.4176 | 2026-10-08 16:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8efbd630-3839-3b70-82d3-f640e991a5e4 | -1.2082 | -49.2539 | 2026-10-08 16:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 3f9480bf-43c4-3aca-9692-5ad599e09d47 | -5.7321 | -41.6349 | 2026-10-08 16:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 187.4 |
| ff8b1bbf-dd6f-35f0-8601-a516376bb35b | -9.6757 | -65.0401 | 2026-10-08 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 30b85940-4c4b-3ba1-ad0a-56f0d1796ba6 | -9.4819 | -66.7836 | 2026-10-08 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 174.9 |
| 91f1bf8c-1d19-3ccd-a8ce-c397731fbc0a | 1.7121 | -55.6063 | 2026-10-08 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 2a7bff12-6663-3a72-9411-4d396e3b9c05 | -0.34 | -52.0359 | 2026-10-08 17:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 2f841d5f-0162-3312-ac2a-690a95caaa39 | 3.5448 | -51.2772 | 2026-10-08 17:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 71ff5ea9-f3dd-3fe5-9e31-dac87915c825 | -12.232 | -44.7194 | 2026-10-08 17:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 82af2e3f-8068-3090-a4b2-73204a1bdede | -9.6572 | -65.022 | 2026-10-08 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f3d7f7c5-f23f-3448-b2f4-da7c28177aa4 | -3.3912 | -58.0017 | 2026-10-08 17:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0a6e06a5-ffb0-32bf-9510-b551001cf0b2 | -12.1742 | -44.7284 | 2026-10-08 17:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 302b5d3c-b961-3d54-ba4e-fdfb1de9db8b | 1.6937 | -55.6263 | 2026-10-08 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e3a41f94-2859-3b1f-a438-daa62c2be08b | -9.479 | -67.4897 | 2026-10-08 17:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 1302e63e-18cb-344b-9570-9432527f0561 | 1.7672 | -55.5463 | 2026-10-08 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 41ecd07d-4d1c-37bb-ab84-8c55a6788cce | 3.5447 | -51.2979 | 2026-10-08 17:00:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 95132744-989d-3874-92fb-3e3a348c215a | -8.9501 | -45.1334 | 2026-10-08 17:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 248.8 |
| 2fcbb7d6-1248-3e32-a33f-40725b18806c | -3.4095 | -58.0013 | 2026-10-08 17:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f839f033-2b4b-3764-b4fd-7a4231132cc7 | -1.3264 | -56.4176 | 2026-10-08 17:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d2d5372f-1758-30db-b43d-9be74f4c0424 | -11.2661 | -45.1859 | 2026-10-08 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 5580c07c-ac61-33e3-ad41-9ffc7d4fd547 | 1.7672 | -55.5463 | 2026-10-08 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 6b924ab6-fcb0-3f5f-b89b-a717f538a957 | -8.969 | -45.1313 | 2026-10-08 17:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 74c40ec9-3090-3c2e-b83c-939164debf74 | -11.2657 | -45.209 | 2026-10-08 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| db4e8ba3-213e-3fd0-b04b-1109307f2d4c | -3.4095 | -58.0013 | 2026-10-08 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 1058c390-6e80-36d8-a6e5-6cee22a8a501 | -12.1738 | -44.7517 | 2026-10-08 17:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 0e7ab842-3d1b-326b-a0c8-e38d2288e50c | 1.6568 | -55.8045 | 2026-10-08 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c9ca8087-afa8-3590-b7d1-196f6f75039d | 1.6938 | -55.6066 | 2026-10-08 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| daa7f29c-fba3-3cd2-bd8e-3466b547e7ab | -2.572 | -56.1646 | 2026-10-08 17:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 262.2 |
| 3bab9784-3ce0-3868-a71b-9896aeeb1eda | -0.3768 | -52.0153 | 2026-10-08 17:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3265621c-1b23-3987-b21c-25fa43f1cdd9 | -9.6572 | -65.022 | 2026-10-08 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4ad25345-1249-3312-b8f1-2be198caaded | 1.6937 | -55.6263 | 2026-10-08 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 1c0d7d47-ad91-3801-ad90-d6f329c4a151 | -3.3912 | -58.0017 | 2026-10-08 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 282562d5-9fa2-378f-bbcc-0148558133b9 | -12.232 | -44.7194 | 2026-10-08 17:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 5aa11d28-3823-3a4c-b6ca-8c40eec9b777 | 3.5448 | -51.2772 | 2026-10-08 17:10:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 87.1 |
| d61e7889-bd14-3d7d-ba55-ecacd64c4436 | -9.4819 | -66.7836 | 2026-10-08 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 2be23e8c-e990-3d05-8ed4-cd6a374194be | -1.2082 | -49.2539 | 2026-10-08 17:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a1638d43-695c-375b-8575-8a6b48de7580 | -12.2316 | -44.7427 | 2026-10-08 17:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 325.1 |
| 804a3109-05e3-3017-ad6c-6280ea895822 | -9.6758 | -65.0214 | 2026-10-08 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 8f6d2234-d141-3a0d-9ee3-a09ea9d183ca | -8.9501 | -45.1334 | 2026-10-08 17:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |
| f002f853-3b83-3d0c-aeeb-305ce003f06f | -4.64 | -50.91 | 2026-10-08 17:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README382.md)
