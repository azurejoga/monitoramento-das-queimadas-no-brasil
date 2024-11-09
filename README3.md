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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85e1068c-81d1-37f0-a435-b574fa7e3938 | -3.1069 | -45.768 | 2024-11-09 00:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| d72ec11a-2e9b-35c7-b652-24b5b8e7fcaf | -3.2808 | -52.7251 | 2024-11-09 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| bfc477ef-b41a-3a9c-bc1e-23391add555d | -5.4887 | -43.6589 | 2024-11-09 00:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 1bf13654-c564-30e7-b576-68db3af74cfe | -3.5649 | -43.5654 | 2024-11-09 00:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 99e6ab1b-ba4a-3361-a7e7-6340aa2d31fa | -4.2486 | -47.5729 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 211.4 |
| a0384632-aa40-396f-83ff-eca291c61bbc | -2.2479 | -53.7829 | 2024-11-09 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 59cdb88c-f84c-3fd8-ae1c-320caf21ed5f | -2.2295 | -53.7832 | 2024-11-09 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c745438a-474d-3dfa-a0e0-241ef21e175a | -5.4701 | -43.6371 | 2024-11-09 00:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 4a1e19b4-87f2-3848-9e5c-bd9e715b8e0a | -3.068 | -50.5631 | 2024-11-09 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 49c8d642-50d9-3c50-90bd-5b5d03e4aa72 | -4.2671 | -47.572 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 0645cf87-5aed-3b64-911b-29f107bd4f32 | -23.9095 | -54.0606 | 2024-11-09 00:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 95.2 |
| 7a922efd-1679-3eeb-9428-89593ab948a5 | -4.2032 | -45.8762 | 2024-11-09 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 37ab5e52-fc49-32e7-a02f-eb3d05806c70 | -2.2479 | -53.7627 | 2024-11-09 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f9a9f337-2b0f-36f4-917c-49e977309849 | -7.2536 | -38.9209 | 2024-11-09 00:30:00 | GOES-16 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 137.0 |
| 15623439-9ab6-321a-95c0-6d6a032df9aa | -1.5078 | -47.1813 | 2024-11-09 00:30:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 306969ce-b144-31e0-8798-6e5781cdba51 | -3.1641 | -54.4854 | 2024-11-09 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| e40cdf9c-16ee-3483-8c22-7052d3b86fe0 | -2.5932 | -49.1416 | 2024-11-09 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 8a9a66c2-c02e-3efb-85c4-dc7af9dbf854 | -3.9668 | -48.1932 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| b3874467-ef4f-311e-a3cf-3aa1c4c0b188 | -1.5164 | -52.1696 | 2024-11-09 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 413e0c65-975e-31bf-bc3e-399750f3be2b | -3.0864 | -50.5835 | 2024-11-09 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 98617d32-9335-311e-a42a-d455821ff0af | -4.2484 | -47.5947 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5e847d05-1cc5-3eee-abc7-f56196217bb2 | -0.2115 | -51.6455 | 2024-11-09 00:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 727e0a24-68cc-3d92-bf77-756e2f708b1f | -6.9747 | -40.0297 | 2024-11-09 00:30:00 | GOES-16 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 84.4 |
| f078d01b-ee2b-3d5b-af03-b233a75577fa | -3.9854 | -48.1708 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 443d96ad-c64a-359f-b6bb-eb9dedaccd6c | -4.2218 | -45.8753 | 2024-11-09 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1a305640-274a-32a8-a4e1-f597f309309a | -4.2219 | -45.8529 | 2024-11-09 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 56985539-4a6e-3d1a-a36c-22767f48ef6a | -3.735 | -54.2292 | 2024-11-09 00:30:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 4df334ad-777b-3178-8de5-ce3fb7ba33b9 | -3.967 | -48.15 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| bebd7adc-d1b0-317c-8408-df0489f93883 | -1.5163 | -52.1901 | 2024-11-09 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 9afbc858-9d12-34da-ba74-741c3bc3558a | -2.4104 | -48.5265 | 2024-11-09 00:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 30e22356-0bbc-34a5-9330-9ff9b8cabc42 | -0.3952 | -51.9536 | 2024-11-09 00:30:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 55f2a7fc-5c64-302a-befe-00a4bb6552bf | -13.41652 | -41.3309 | 2024-11-09 00:37:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| dc3da263-2acd-3f67-aa89-618e1377bc2c | -7.45933 | -43.57051 | 2024-11-09 00:37:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4645dde8-c30f-3c89-8122-5a113289d24a | -10.50922 | -42.39319 | 2024-11-09 00:37:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 3a516105-2cc1-3376-a796-2ff0796e74bf | -6.987 | -40.03672 | 2024-11-09 00:37:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 261.6 |
| 64db24ba-38aa-33da-b95e-792eeb2b6a12 | -11.24548 | -47.91055 | 2024-11-09 00:37:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 22cbab8e-b31d-38b8-a44d-8d321f0bd837 | -11.83352 | -44.23357 | 2024-11-09 00:37:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b2c9ebcf-1332-354e-89ce-909c2139b087 | -8.69669 | -47.95893 | 2024-11-09 00:37:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d965f270-0d79-3811-b02d-d56f3b7aa271 | -11.18542 | -44.61304 | 2024-11-09 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5714aac6-c909-3e60-bbb1-96a67fdaf084 | -9.77336 | -43.5827 | 2024-11-09 00:37:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 64dc9c54-f80d-3769-bd42-23ad16ddd661 | -6.98079 | -40.03062 | 2024-11-09 00:37:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 83.9 |
| a4ce74a8-65b0-320b-8b9a-68ce08dfe613 | -10.33593 | -36.61424 | 2024-11-09 00:37:00 | TERRA_M-M | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| f6f4f99c-be00-332c-b9dd-557afb01a004 | -9.11356 | -43.14127 | 2024-11-09 00:37:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 37abda5a-0c0f-31aa-98a9-0678ce066650 | -10.0818 | -42.11214 | 2024-11-09 00:37:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| bece9e75-cf31-36fa-9798-01419edbc5b3 | -9.41417 | -41.1965 | 2024-11-09 00:37:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7c638b23-cf33-3a39-b371-f4dfbe58522a | -8.90361 | -43.88739 | 2024-11-09 00:37:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 393620e2-9d7c-3075-a00f-a9632ca7ae60 | -6.99144 | -40.02911 | 2024-11-09 00:37:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 982325f5-17fe-3d60-8cec-56cc743a3eee | -10.54108 | -44.6799 | 2024-11-09 00:37:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8af5eb00-267c-3f72-b8ab-26ecbe9e59e6 | -10.89479 | -44.71099 | 2024-11-09 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 87164e2d-cad9-33ae-a111-e3e39c29c54b | -10.93286 | -44.44787 | 2024-11-09 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b308b867-048a-32c6-ac97-8f2f133464ea | -9.3901 | -40.34396 | 2024-11-09 00:37:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 8e91ae9d-99e5-344f-ba86-fa0d3ae52b31 | -10.33896 | -36.6204 | 2024-11-09 00:37:00 | TERRA_M-M | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 9e62a987-154a-37de-a570-f28dc4a76d4c | -10.66436 | -44.50362 | 2024-11-09 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 211bfeb4-670b-377d-b640-6713864c2d09 | -10.51817 | -42.39185 | 2024-11-09 00:37:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 6bb774d7-2e98-3b21-8a17-3b5993c54f73 | -11.18668 | -44.62245 | 2024-11-09 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 318dcce8-3a92-3309-9cba-182f072de943 | -6.98271 | -40.04379 | 2024-11-09 00:37:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 165.5 |
| add01bf9-af73-388f-b02c-8ef66ecc9d83 | -9.1123 | -43.1323 | 2024-11-09 00:37:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bde0225f-7929-3a8a-93ba-87dfe32c4fab | -6.99334 | -40.04225 | 2024-11-09 00:37:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| f0239c63-e1e2-3c60-9de4-84e6f67d6044 | -9.12876 | -43.18481 | 2024-11-09 00:37:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| f6de9b43-5288-3c98-bc03-c1339e555e5c | -6.989 | -40.04979 | 2024-11-09 00:37:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 39.1 |
| c34ea15b-9d9a-3c96-812e-21ab351e04e6 | -12.26755 | -44.59064 | 2024-11-09 00:37:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d25abe22-a028-3df1-b232-0c99b46a00cc | -9.1275 | -43.17586 | 2024-11-09 00:37:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 86caca47-cb4d-386e-9c88-ba64c76fb222 | -10.51053 | -42.40237 | 2024-11-09 00:37:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 932210a0-f5d2-38ae-9a02-79801d711045 | -7.24142 | -38.91731 | 2024-11-09 00:37:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 249.1 |
| 0c2ee268-095d-3184-8481-80346c8836e2 | -11.24731 | -47.92529 | 2024-11-09 00:37:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5d10b471-258a-34f4-a41c-f90e8d104bb7 | -7.24374 | -38.9326 | 2024-11-09 00:37:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 268.4 |
| 403cd099-27eb-3786-b1eb-3d51aedcf758 | -10.51948 | -42.40104 | 2024-11-09 00:37:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 9f089793-b42c-377b-a6a5-180361177c41 | -6.21749 | -41.66645 | 2024-11-09 00:39:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 214438bc-4e8d-307c-b64e-6142ca8b470d | -0.21758 | -51.63183 | 2024-11-09 00:39:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 65.2 |
| cb0caeb5-8129-33fc-9ea7-b6b24aafb957 | -1.51279 | -52.17278 | 2024-11-09 00:39:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 81a4f868-402f-3ea6-8b9a-ba4fed343cbb | -3.29611 | -49.17305 | 2024-11-09 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 18223c08-a59a-3032-a325-1566b59755e4 | -4.24484 | -47.56686 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 2930cb69-65d5-37fe-ba71-22b2c9c0b8a3 | -2.43158 | -46.30571 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| f53ba9fb-daf1-351f-addb-7d7f083f1916 | -2.61708 | -46.2488 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 07573fc0-8940-3bc4-ab5d-a2c7dd4aaf64 | -2.18361 | -48.33302 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 832ad374-9c21-39be-a749-4ba76d4fdc29 | -2.63516 | -46.77978 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 78198ec1-e5f7-34ed-ba1d-a5f27c6c6462 | -4.24781 | -47.58853 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 99bdef21-5efc-3e06-924c-2b469e5409e6 | -2.74645 | -45.71594 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bc865ff3-bb1c-31fc-91cb-4fba62fd3f3a | -4.86928 | -45.68177 | 2024-11-09 00:39:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2999f553-521f-36fe-a8d8-be65f33b2f7b | -2.61888 | -51.29078 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 4e1345b6-72d1-3351-b60e-3fec0a7d9e5d | -6.24491 | -39.7103 | 2024-11-09 00:39:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 41c5f8ca-6314-37cf-90bc-ef5c567ce4bf | -2.67194 | -46.77465 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 67d0f083-1788-3734-adcc-963d17656477 | -2.63384 | -46.7702 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 004c86d8-63bc-3d39-9160-7b038eb81f61 | -3.4087 | -50.00935 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| db72020a-9230-3e0f-89e6-04d18754c1b2 | -2.48152 | -46.13483 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a8ba2ec9-1384-300a-a923-6445c58b6263 | -1.56521 | -51.1665 | 2024-11-09 00:39:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 8d9afe61-a60d-3c58-951c-b6c4befb0f04 | -2.38227 | -46.7463 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a141d2c5-c9d2-32d8-b240-18303393f585 | -2.79646 | -45.47623 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 068c4c23-1ae6-3d45-b396-ae4aaa296e42 | -2.4602 | -53.69707 | 2024-11-09 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| fd0a4bda-57d5-3e9d-96a5-dcb037cf91a8 | -4.016 | -44.58058 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 783f6f39-d02f-38c5-9bd3-937cfa87b7fb | -2.40672 | -48.3956 | 2024-11-09 00:39:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 98721fc5-d6f7-3235-a0ab-b1dc4a0f92b5 | -2.63214 | -48.47144 | 2024-11-09 00:39:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c2e98ec0-a05d-3d35-aa9b-13cb9c1db5f0 | -3.13681 | -44.41806 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 250d59ca-ff50-3dbf-ae42-031c0cb7d273 | -3.56223 | -43.57654 | 2024-11-09 00:39:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| bdb08ba5-bad0-3dd8-adb9-2dd1c7586424 | -2.96328 | -47.37127 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a2c4482e-b5b0-3140-aec2-fdbda3b5d60e | -3.14672 | -45.94669 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 50601dcf-a943-3375-9d6b-30847a5c8b62 | -4.12761 | -43.59921 | 2024-11-09 00:39:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| c0b60f1e-9f7a-36b4-8327-c83f40f3e7f1 | -2.62465 | -46.77149 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2788cdc5-1e52-3186-bc7e-ac78f17edd01 | -1.95408 | -46.51589 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 719fdab4-549e-39bc-b335-7cdebf319523 | -4.12633 | -43.59008 | 2024-11-09 00:39:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |


[Clique aqui para ver as próximas entradas](README4.md)
