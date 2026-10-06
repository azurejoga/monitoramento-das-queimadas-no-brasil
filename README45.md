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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d4d1156-6910-3bc6-a9eb-dd975537fd52 | -3.07071 | -54.16072 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93d87ae1-82c9-3cac-b897-aafb8177d134 | -3.10504 | -53.7536 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d2fa948-11f2-3a5d-910c-c22b02ab1ce4 | -2.9293 | -54.13427 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f26c5720-d686-3e66-a7ee-6269aad8a573 | -3.10049 | -53.72598 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6291c784-170a-35de-8e73-1f8adcedc626 | -2.87325 | -54.13239 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 663b1e45-a5a7-312f-bb20-68f789956f36 | -4.19576 | -44.26249 | 2026-10-06 04:38:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21a11ac5-bcc1-3879-911b-16b09edae05c | -3.0917 | -54.1666 | 2026-10-06 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b6c649d8-e123-36b5-b1f8-016a7e081c40 | -2.8714 | -54.1318 | 2026-10-06 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 46605b91-2396-30bd-86ef-3349ac6e3e80 | -3.0191 | -53.9071 | 2026-10-06 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f50c05e3-9f39-3a31-8f44-06cb2f2510ca | -3.0734 | -54.167 | 2026-10-06 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 312e57ad-c4f3-3d28-b246-29216b50572a | -3.0192 | -53.887 | 2026-10-06 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| feacf1d8-50c9-3151-97e3-77979df83e0f | -3.0548 | -54.2076 | 2026-10-06 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| fadb0950-54b1-3ef1-8486-76d74f1e7431 | -3.0 | -54.1287 | 2026-10-06 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6b84cdb8-1885-3d64-98e4-8fe3e47093e2 | -3.1115 | -53.7637 | 2026-10-06 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 843e173a-2a61-3a34-8ef6-2b1359f4d79c | -3.5128 | -54.6162 | 2026-10-06 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a5869979-ce84-32d6-8702-3e68be3fcb73 | -3.4944 | -54.6167 | 2026-10-06 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ec094421-3067-3663-9167-a4374d1c13db | -3.0932 | -53.7239 | 2026-10-06 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| dac35d48-6c3c-3150-8665-feee93537f8f | -2.9448 | -54.1501 | 2026-10-06 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2818a29f-1f4e-357c-b9e2-b1eddb371976 | -3.3502 | -59.5039 | 2026-10-06 04:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2f90fedf-9811-3811-ba1a-f074dbcc3592 | -3.0732 | -54.2273 | 2026-10-06 04:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c91739d2-77bf-3b89-bae6-7e7a5d5171ca | -2.7796 | -54.0937 | 2026-10-06 04:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 2c7ec498-edee-37cb-8cdd-52eee349773c | -3.5127 | -54.6362 | 2026-10-06 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 718db636-73d1-386e-9a17-8cb4fb227a76 | -3.0548 | -54.2277 | 2026-10-06 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 63f31533-542f-3f5e-971b-a0c96982dcce | -3.6732 | -55.9425 | 2026-10-06 04:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| fb275086-b05d-3cd8-b687-5aafacd95daf | -3.0731 | -54.2473 | 2026-10-06 04:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| e4565abf-1c02-3a39-83eb-27915ae8d249 | -2.8713 | -54.1518 | 2026-10-06 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 35299e1d-712c-3621-89ad-5a2fa784473f | -3.4943 | -54.6367 | 2026-10-06 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| a8957102-8faa-37b0-b853-3eba26fad861 | -3.0375 | -53.8865 | 2026-10-06 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 16282112-954e-313d-b99e-ea273a7281a3 | -3.0915 | -54.2469 | 2026-10-06 04:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| cd2cb65a-7844-3eed-8b60-ac64907a3414 | -7.48261 | -42.8102 | 2026-10-06 04:40:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2455bf50-4978-3111-9660-d8fb6cb541a9 | -6.42315 | -43.46526 | 2026-10-06 04:40:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b61b3580-1646-3e4c-8a26-a2d4d9035334 | -9.74488 | -48.17166 | 2026-10-06 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 176ed683-3d4d-30d9-9d08-933e326ebcf9 | -6.81188 | -39.2986 | 2026-10-06 04:40:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91e55b43-884b-3600-851c-881842afe80f | -6.34994 | -42.55001 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 33898eb7-c4d7-3932-8a90-96d8434832de | -5.83359 | -45.0159 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| cdde0630-cea8-3fdd-bf08-a6fb724ee84f | -6.00233 | -47.39479 | 2026-10-06 04:40:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 999345ed-2c9d-3d5f-918a-8c52cc547d34 | -6.32066 | -43.348 | 2026-10-06 04:40:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd58bdcb-4e7e-3d5b-8cc6-18d6a14e5a89 | -11.28445 | -45.51687 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 54b350f9-e6b0-35c0-82dd-643e1768b4ff | -6.42243 | -43.4702 | 2026-10-06 04:40:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f49de5c5-7dca-31e9-a8fb-2aeaebe76e94 | -5.81171 | -53.84066 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 908160ed-ca8c-3df9-bdcb-14cf608cf7cb | -11.36438 | -46.68393 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5743bf09-ab8c-3bda-aea1-da6f7fee5f88 | -11.82371 | -43.53491 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a6b076f-cd81-3408-844b-a6763eebfe9d | -6.00995 | -53.51094 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae0131e1-2cb4-30ff-880f-545fd743f328 | -7.82507 | -45.5624 | 2026-10-06 04:40:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dadd207c-6338-3a82-82ad-003628756393 | -11.67607 | -43.6622 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fadb1fb-a808-38ad-9bf9-f3ec4122082d | -11.26293 | -45.5091 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 615bc393-b9be-3753-a298-d56cf73bb782 | -6.0051 | -47.39878 | 2026-10-06 04:40:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 92fe18f3-de26-3444-ab92-30d57aff7d90 | -3.99134 | -56.26817 | 2026-10-06 04:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d7a7c4e-ae2e-35a1-a6d8-ad292e3bfddb | -11.36665 | -46.66081 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 304fdd38-1406-3355-a1d7-bae990db8e4c | -4.0605 | -56.33714 | 2026-10-06 04:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 282adc97-f736-329e-b17b-1f5098cf7f8e | -6.82182 | -39.30817 | 2026-10-06 04:40:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2097b2f-fd50-3869-9437-4f54c37ba2b4 | -6.18715 | -44.85595 | 2026-10-06 04:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 561a5c62-1a63-3037-8045-c2e125c548bd | -6.45807 | -55.47578 | 2026-10-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72adccaf-1566-348b-bc3e-f06a16c801be | -11.2875 | -45.52187 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 29fe51aa-3824-3a6f-b968-f15bc56c6103 | -6.72443 | -44.27697 | 2026-10-06 04:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b1301110-87a8-3fa2-a0ef-f81e2c877498 | -7.24506 | -45.26011 | 2026-10-06 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f09f37de-002e-39d1-903e-d223d165d8e7 | -7.57268 | -46.63437 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce0da6a3-9b1b-3394-a488-a0d598dd2957 | -7.09367 | -45.57061 | 2026-10-06 04:40:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7065c12-456d-3ee0-bd24-cf0f6776c9db | -7.87536 | -49.05821 | 2026-10-06 04:40:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 860c4a59-07af-3cd7-8ad4-fddbbd8287d6 | -6.93339 | -43.67233 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5ffb7022-dfbb-3c40-8bc2-c0f19e6a4cff | -5.67794 | -53.49948 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08fd2089-2dac-34cc-9ea0-135416032621 | -8.70062 | -45.21481 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 379ef79f-0f58-3e64-a0bd-7b438d41c836 | -9.8612 | -44.81485 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43486052-d81d-3f76-bcf3-f3c14dadccd7 | -5.81239 | -53.83662 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcd16281-c52c-39c1-bbe8-5909410c1d69 | -13.00171 | -40.14582 | 2026-10-06 04:40:00 | NOAA-20 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8b7ba14d-df22-3112-ad41-3a19477fa8de | -7.71546 | -45.45167 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1653fb76-f049-3644-937d-fa854358414d | -8.6927 | -45.21799 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 856344f6-3471-3944-887d-d4e97867d870 | -8.27374 | -47.91712 | 2026-10-06 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e478aa0-b6e5-3f73-8f9f-c6aaa153cc98 | -10.27535 | -60.5491 | 2026-10-06 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06ae5aa4-e79a-3bff-ae23-2eea802c6e26 | -8.69333 | -45.21373 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 718b7232-721f-3b12-8813-12a01ba59897 | -6.72345 | -52.91025 | 2026-10-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9aea3e3-1461-37c7-96e3-63eeab799be7 | -11.27467 | -45.50634 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 19b19b12-80d1-31c6-98cf-eb5b2dc4afb8 | -7.89905 | -44.18207 | 2026-10-06 04:40:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d661dae-122d-3546-a200-38450a131383 | -12.93396 | -47.44156 | 2026-10-06 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d16312f-22f8-3d1c-bc4d-abbc6504c989 | -11.26422 | -45.50024 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dacc2640-46c4-3206-84bb-ae88b8f63cc3 | -4.45623 | -54.9649 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e434a80-f1d9-3095-9dac-a4432270f486 | -6.33297 | -46.95164 | 2026-10-06 04:40:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf7e4d5c-71a0-3421-b3ac-cb1bbdd5cb35 | -11.68509 | -43.62849 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84b157a1-2185-37c8-b6b9-d0bd1ba063a4 | -5.58417 | -47.26807 | 2026-10-06 04:40:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd3b1fd5-bb38-3f16-8c45-150b4d5b4085 | -6.72748 | -44.28207 | 2026-10-06 04:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8b093dd-301e-3169-a3a1-d83df1a65ee0 | -7.24316 | -45.25656 | 2026-10-06 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56c68a3a-8b74-32ae-a15c-e359fb1139ef | -8.69698 | -45.21428 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5284b05-6ee3-3459-aa3d-49cc71ffc43c | -12.32419 | -47.841 | 2026-10-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17ead9cf-5aa9-32dd-84ea-d63eeb46b138 | -7.33287 | -44.37392 | 2026-10-06 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01bc3db3-ae1f-3f3f-8b86-21ef7e8f6fb1 | -11.27097 | -45.50578 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 37cd6591-9b96-3da1-bfb8-faa13c8aa531 | -11.35901 | -46.68755 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8990c5a-7c6c-361d-b3c2-2fac7a6a489b | -11.82675 | -43.54424 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bceb9b1-b7c5-3a00-9c97-33ea112ba15f | -7.45408 | -46.83588 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d52482cc-1d3d-3995-81ad-b3db2865873a | -11.68488 | -43.67039 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9333f425-88b9-330d-9f4a-fd8fd1f843a4 | -10.27628 | -60.54445 | 2026-10-06 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 800b57ca-8fea-37a4-955e-272ff643eaf4 | -11.36316 | -46.66024 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 639b5fbd-9271-399b-b920-53f98f7fc657 | -7.8467 | -42.92641 | 2026-10-06 04:40:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 15596acf-181a-3ac6-a9a7-8203f0c9d1ef | -6.88031 | -43.67739 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e905cecd-1596-3f17-95e2-421266b2c74e | -13.00209 | -40.14258 | 2026-10-06 04:40:00 | NOAA-20 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0a97a61e-28c8-38e2-9a0d-cf07b471b0b3 | -7.24252 | -45.26067 | 2026-10-06 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a26fdd8-0598-3145-8e8c-1a2523552a84 | -5.83003 | -45.01534 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c875eb60-eba4-3bc3-bf72-ce7b1c613ec8 | -8.60496 | -45.65972 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcefc0de-a7e3-337e-a0c7-66e00b747db1 | -11.65151 | -43.65553 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e1f0285-f088-3f01-8ccc-a6ea9cc4e43a | -11.28948 | -45.50843 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 88f400eb-2a93-3960-890d-4cb82f67abe6 | -8.58654 | -45.66124 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README46.md)
