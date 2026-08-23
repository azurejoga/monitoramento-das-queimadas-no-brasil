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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a023059-d061-32e8-9167-21753574542d | -7.25819 | -49.89142 | 2026-08-23 06:42:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bf1c2783-73b7-3900-9c7d-ff2d24a1f817 | -10.81749 | -50.96162 | 2026-08-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5ec57407-e1a7-3a4a-b6d5-1d2e4d9cafb7 | -12.84977 | -48.46843 | 2026-08-23 06:42:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 61e91471-2058-3d5c-9b66-5ca252a3be3c | -10.46015 | -49.96868 | 2026-08-23 06:42:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 070ff97e-4091-329f-868f-63e6d58614de | -9.78832 | -46.62345 | 2026-08-23 06:42:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 25beccfd-23c0-383b-9c7b-916bf033c47a | -10.47105 | -49.96007 | 2026-08-23 06:42:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 9c223e62-5a7c-3d44-9e10-bf84dac04827 | -13.68644 | -51.84401 | 2026-08-23 06:42:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 707a81b0-0a59-3140-af8c-7c176760dddb | -7.03439 | -48.02073 | 2026-08-23 06:42:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 424ad37d-46fb-3013-b5cd-d9c3161c3115 | -10.79596 | -50.96975 | 2026-08-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 36.3 |
| f9fc2cee-2f87-3a66-ac6a-5bbd01b5a14c | -10.78611 | -50.96814 | 2026-08-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c424198b-fafb-3895-945e-3a0951dd005b | -6.1957 | -53.52689 | 2026-08-23 06:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9d6c245a-0a6e-382f-a8ea-a58315a01d0e | -13.66459 | -51.85228 | 2026-08-23 06:42:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 96eddce5-5ccc-34e3-a61d-4cc997b41d00 | -10.81934 | -50.95028 | 2026-08-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ef246b89-23ab-3e8c-900f-dca8f0a7beaa | -6.19711 | -53.52215 | 2026-08-23 06:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 4ece0eab-3e69-3de6-bb9c-25a1ebc40cad | -9.80017 | -46.61306 | 2026-08-23 06:42:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ef161e7b-adfe-30b6-8728-2721f5c9c39b | -8.92629 | -48.53249 | 2026-08-23 06:42:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c6852ffe-1665-32e8-b536-069536ed1461 | -10.82916 | -50.95189 | 2026-08-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4e90c910-8852-3628-9a45-5e95b3e53679 | -11.55228 | -46.94429 | 2026-08-23 06:42:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 585dad6b-7f11-392b-a85b-d7bc9bb33b15 | -13.19081 | -51.41385 | 2026-08-23 06:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 06310dad-7646-31de-a5be-d679407e46aa | -9.7897 | -46.61426 | 2026-08-23 06:42:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c5656a35-f699-3c17-830e-4992166789ea | -8.96008 | -50.75161 | 2026-08-23 06:42:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f7d9d863-8017-3d73-9ec9-5d8dd7a029e6 | -10.83716 | -50.96484 | 2026-08-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 720cd823-5bf8-3e06-b6ee-e33acb5bfa8f | -10.82733 | -50.96323 | 2026-08-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.9 |
| cac464c2-6c75-3c3a-ae2b-59030b8099f8 | -10.78635 | -50.96149 | 2026-08-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 700ebcdf-1478-33a3-b960-1fb0e50a5aec | -10.46947 | -49.97017 | 2026-08-23 06:42:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 69265e0d-fb2f-3557-ae72-d0f5d98f5ea1 | -12.75056 | -48.37667 | 2026-08-23 06:42:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d2cd856b-1a9d-3780-b0ea-99f2bbb255c1 | -12.74514 | -48.41236 | 2026-08-23 06:42:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a373b366-f595-358f-bda8-9b92869caba3 | -10.78798 | -50.95679 | 2026-08-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bb2357dd-0236-37b2-8dda-9b12a8ed5437 | -8.92489 | -48.54155 | 2026-08-23 06:42:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 26.7 |
| f6e77722-ce31-3e4a-9e7a-ec8316e65246 | -6.18407 | -53.51994 | 2026-08-23 06:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7b156d1a-a23a-35e3-8aba-e55635f062b3 | -7.26606 | -49.90421 | 2026-08-23 06:42:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| bf03cc8e-242e-3484-8f21-420777f9264b | -11.43756 | -44.52628 | 2026-08-23 06:42:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9c847968-95e6-3b7d-ab93-db8c561c77c9 | -13.14988 | -51.41854 | 2026-08-23 06:42:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a910da4a-ed50-3134-909a-3b81dc8e1b0b | -15.34036 | -43.95359 | 2026-08-23 06:44:00 | AQUA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 1738f031-d608-3708-b635-aa3384c02638 | -14.9961 | -52.69103 | 2026-08-23 06:44:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 407630b7-e02f-3862-a249-7eaa071bb1b2 | -16.06071 | -50.42538 | 2026-08-23 06:44:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a6244cee-125d-3ce0-8d93-acef3afa2b51 | -14.78909 | -48.7825 | 2026-08-23 06:44:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| cc66467d-49b5-3b40-95c6-b102589b00a0 | -17.74917 | -47.03062 | 2026-08-23 06:44:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 7f82ccef-2a4f-3c69-ac91-486514d64666 | -15.51689 | -49.82846 | 2026-08-23 06:44:00 | AQUA_M-M | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a8502285-11e0-3627-94f4-ea899684cb00 | -16.05918 | -50.43499 | 2026-08-23 06:44:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 213f3f2b-e00c-3a1d-b022-a57c6f5e7616 | -16.04107 | -50.43506 | 2026-08-23 06:44:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7f50ec50-d169-3792-89f0-fb44553daba6 | -14.9537 | -52.64984 | 2026-08-23 06:44:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b525cfe7-d926-3166-ae92-e498db73b6d9 | -14.79922 | -48.77489 | 2026-08-23 06:44:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f7bdabd6-4790-3d1e-bd94-3363f62df8d5 | -14.96733 | -52.67239 | 2026-08-23 06:44:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 69a09adc-71b2-3a46-be75-56d4c4d13ee2 | -15.35151 | -43.95513 | 2026-08-23 06:44:00 | AQUA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 36462cc0-02d8-3597-8361-087e385399ef | -6.6256 | -69.85249 | 2026-08-23 06:44:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2521e452-6726-3c08-8300-3c153e89438a | -17.90539 | -44.5019 | 2026-08-23 06:44:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 328c84b0-6b68-35cb-bce9-6da004cb5cc8 | -16.04258 | -50.42545 | 2026-08-23 06:44:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6c248df1-81f6-304e-976e-0db316f8433c | -16.40544 | -51.83666 | 2026-08-23 06:44:00 | AQUA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 49cde4a3-9afa-380e-ba7b-8fc57a404090 | -16.05006 | -50.43665 | 2026-08-23 06:44:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 05a67eb5-c4b1-3ba7-ba38-6a22dbee5309 | -16.05156 | -50.42703 | 2026-08-23 06:44:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7f6281a4-d348-3884-b279-7d61ab6cd4bb | -20.65638 | -46.56274 | 2026-08-23 06:44:00 | AQUA_M-M | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 863f7b7e-450c-3eac-8cc0-7bb2a42ea0df | -15.3178 | -53.79119 | 2026-08-23 06:44:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0193dfa5-c6d1-31d0-ad19-77732942d0ec | -15.33847 | -43.96863 | 2026-08-23 06:44:00 | AQUA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 3d64034b-abc7-3bc2-9b3d-baa04f804acf | -14.95922 | -52.65767 | 2026-08-23 06:44:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 86180f87-26b5-32cb-aedd-99653fb66930 | -14.79785 | -48.78388 | 2026-08-23 06:44:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3cb2b3f0-0c98-3118-a66e-f3f2e04b2d78 | -16.04856 | -50.44624 | 2026-08-23 06:44:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 78feba6e-0eef-3b3c-b2b9-f685a0debfc6 | -14.96956 | -52.65935 | 2026-08-23 06:44:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e1120adb-3152-3b10-80b2-f00b6b35dde5 | -16.05765 | -50.44459 | 2026-08-23 06:44:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 61500a94-2642-3a5f-bfc7-80f3a7b706eb | -14.79046 | -48.77351 | 2026-08-23 06:44:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f1201f3a-bce8-3c51-964a-2330f9705f38 | -6.6766 | -58.7299 | 2026-08-23 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| e75b3635-503a-317d-ac32-b88a9807caa8 | -6.695 | -58.7291 | 2026-08-23 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 2388c6f0-4f76-3bb0-8789-e11d7ecae304 | -10.7982 | -50.973 | 2026-08-23 06:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| dea551b6-0fbe-33a6-a19b-0e37d4e8ade6 | -6.6949 | -58.7485 | 2026-08-23 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 55d9f8de-ce06-3c52-a704-3e99fc7d4104 | -6.9699 | -59.0658 | 2026-08-23 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 7893b197-cae1-303d-89e1-1528796550fc | -10.8172 | -50.9711 | 2026-08-23 06:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| b3e3fab1-5e02-3b9e-8465-350747863101 | -10.4716 | -49.9624 | 2026-08-23 06:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ea8dd420-d8af-3437-b72e-ae673a752739 | -6.8062 | -58.6469 | 2026-08-23 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| daee2b62-b405-3dcc-9b2a-901bc3ed191b | -6.6765 | -58.7492 | 2026-08-23 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 8c623572-4f76-3a4c-97a1-3375144b5377 | -6.1101 | -57.84 | 2026-08-23 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 6f4816d7-27fd-3805-b6c4-a1015f43e5fe | -10.7985 | -50.9518 | 2026-08-23 06:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 75a7f564-c791-3463-b7b8-81ed4ebbfc55 | -16.0509 | -50.4363 | 2026-08-23 06:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e6d9e1fc-c1cc-374b-b6cc-656a8c835a82 | -6.9514 | -59.0666 | 2026-08-23 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 85f97296-b8fc-3ca0-8257-f913c77a08e7 | -6.1285 | -57.8393 | 2026-08-23 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 9562cda1-db4b-357e-9b27-19e97f1d1a2c | -6.6765 | -58.7492 | 2026-08-23 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 38d88318-86bb-333f-a83e-697e88bc8616 | -10.8172 | -50.9711 | 2026-08-23 07:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| d506f6da-a6bc-3b82-b4d5-9b274005cd36 | -6.9514 | -59.0666 | 2026-08-23 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f316dbf7-a31a-3744-963c-6b4aa7bf3463 | -6.1285 | -57.8393 | 2026-08-23 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d06e4cfa-6681-314e-8c4f-4fd475939279 | -6.6949 | -58.7485 | 2026-08-23 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| c69a545b-14a3-3e86-85e1-9e37b9d4f7f9 | -10.7985 | -50.9518 | 2026-08-23 07:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b08769b4-f502-3c73-a1ee-601297602cf6 | -6.9699 | -59.0658 | 2026-08-23 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 6b0e2e6b-6014-3775-ba45-5babd83b2460 | -10.8174 | -50.9498 | 2026-08-23 07:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| f111030d-9585-3b33-af91-6b6d3acb777a | -6.6766 | -58.7299 | 2026-08-23 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 204ab954-a9a3-3e47-8546-8b92c123d0d3 | -10.4713 | -49.9838 | 2026-08-23 07:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 7b90e86b-0813-3a77-9fc6-832ee5cdf957 | -6.695 | -58.7291 | 2026-08-23 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 343c74da-c08c-3baf-8a87-5e64c8991d8f | -16.0706 | -50.4332 | 2026-08-23 07:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 62ffd20d-7f50-3570-b574-fffc9c8a36d9 | -16.0509 | -50.4363 | 2026-08-23 07:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 7cba5776-75f7-314e-b69d-1381d9787971 | -10.7982 | -50.973 | 2026-08-23 07:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 6dd2b35c-7da5-369e-bb94-9c730cd5e369 | -10.4716 | -49.9624 | 2026-08-23 07:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 0dce9853-86dd-396d-8c25-8a0035c89b20 | -6.695 | -58.7291 | 2026-08-23 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 9cc68681-e7b3-327c-9fa8-215a731ce324 | -6.8062 | -58.6469 | 2026-08-23 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 27d4f94d-0939-3b57-ba3c-ffc6ce193059 | -6.1285 | -57.8393 | 2026-08-23 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| aac79385-2289-3d96-9779-8f9e3e03bc10 | -6.9514 | -59.0666 | 2026-08-23 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ac222689-d0b2-3a45-b7be-7fde148a7973 | -6.6766 | -58.7299 | 2026-08-23 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| f41455be-4bb7-3304-925d-5933e20b9efd | -6.6765 | -58.7492 | 2026-08-23 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| cca0f6b1-0ca8-302a-8141-2501ff257273 | -16.0509 | -50.4363 | 2026-08-23 07:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 79af4351-ff81-3d6a-9fde-dc718b80291b | -6.1286 | -57.8198 | 2026-08-23 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| eaad856b-6e65-3596-ad49-9de64341cfe0 | -6.9699 | -59.0658 | 2026-08-23 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 3c461b9d-cdbf-398f-ba6b-c5a2a5546091 | -6.6765 | -58.7492 | 2026-08-23 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| e6de2ac4-5b14-331f-901c-b4458db7bdfb | -6.9514 | -59.0666 | 2026-08-23 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |


[Clique aqui para ver as próximas entradas](README71.md)
