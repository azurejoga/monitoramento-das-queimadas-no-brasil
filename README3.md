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
| 7dcf3098-8981-360b-896d-7b4301fe6795 | -10.9397 | -43.0593 | 2026-07-07 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| d81a453f-de13-3d3d-9850-68652ed64f88 | -6.9135 | -43.7281 | 2026-07-07 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 744aa2e1-15be-3696-8425-857b6246c281 | -10.7666 | -46.616 | 2026-07-07 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 1b7bd6f1-f204-3351-9ce4-7e6cef9968cb | -13.261 | -54.2249 | 2026-07-07 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 221.2 |
| cb03bf2a-b222-3a1f-98e5-6d0784bb51c0 | -13.2783 | -54.3469 | 2026-07-07 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 182.7 |
| bfdc2bb2-fb1a-3981-b1a6-f69c6e2a37f3 | -13.2607 | -54.2456 | 2026-07-07 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 7b869482-7df5-38ba-b6c5-73bd8790f5e3 | -13.2613 | -54.2042 | 2026-07-07 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 0f10637f-4bd4-31ef-8dab-7d9ae2aa7458 | -6.9138 | -43.7049 | 2026-07-07 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 182.7 |
| a0b5115d-94d5-3a2c-b71a-cd580293c678 | -4.2811 | -48.3518 | 2026-07-07 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7c362b02-56ef-3587-9649-b10aa889f491 | -10.9397 | -43.0593 | 2026-07-07 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 68b30a91-0ceb-3b4c-953e-8db68392b253 | -10.7666 | -46.616 | 2026-07-07 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| bb0d7e7e-5107-3916-9481-fa9c8b54bd29 | -11.6981 | -44.545 | 2026-07-07 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 723d6013-467d-380e-8591-9b51f4622445 | -12.7548 | -44.5428 | 2026-07-07 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 07049c7b-d19b-3f6d-be20-b4e264b41f59 | -6.9135 | -43.7281 | 2026-07-07 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 49db9ac2-a3bc-3ad8-aa3e-3b73aa92e4b6 | -12.7741 | -44.5396 | 2026-07-07 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| c29750bd-912c-3a29-90b0-1c363e757d28 | -6.9138 | -43.7049 | 2026-07-07 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 172.6 |
| e729977a-d477-3440-a6c0-41b543831700 | -6.895 | -43.7066 | 2026-07-07 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4c3c2624-195c-36eb-b6ee-01bfa2650807 | -6.9326 | -43.7032 | 2026-07-07 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 3bc843dd-43ef-3c3c-8843-be88d5d5ecbc | -10.4023 | -46.8402 | 2026-07-07 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| bada99b0-c9e4-3a2c-831b-94de8d6484b2 | -10.9205 | -43.0622 | 2026-07-07 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 54254628-786d-3933-9677-0ee760af80e2 | -11.6785 | -44.5712 | 2026-07-07 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 0d6f7f59-830e-30a6-8a08-e57c3bcab083 | -13.2607 | -54.2456 | 2026-07-07 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| bbe94ae0-ed56-3202-a03b-3026c5eae2e7 | -13.2783 | -54.3469 | 2026-07-07 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| c2b7dae9-0f76-3c8a-8b53-400c5a041758 | -11.6592 | -44.5741 | 2026-07-07 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 97500f13-d20f-3004-8d77-d75815f3e776 | -13.261 | -54.2249 | 2026-07-07 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 856149e4-6a9b-3280-8c45-6cdd6431ebd4 | -11.6597 | -44.5508 | 2026-07-07 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| cfd1278f-16cf-3f61-9d1d-2b82b0e7390a | -11.6789 | -44.5479 | 2026-07-07 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 8e22c88c-e830-3e44-a692-344308c940db | -13.2218 | -54.291 | 2026-07-07 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 76659379-ca34-3088-b19d-21e07b377b78 | -6.9135 | -43.7281 | 2026-07-07 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 081f929a-3f4a-33e5-b2ab-277d8847b74e | -12.7548 | -44.5428 | 2026-07-07 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 349317d0-547e-3507-8064-a248a12847eb | -10.9205 | -43.0622 | 2026-07-07 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 54252d87-83d1-3c9a-a89b-d7f0cf64a94c | -13.261 | -54.2249 | 2026-07-07 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| bf7758ec-9486-3817-a70f-b737a56f1594 | -11.6597 | -44.5508 | 2026-07-07 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| cb19e8af-78b5-36cf-9349-537c7bd14462 | -6.9138 | -43.7049 | 2026-07-07 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 8997ed44-3dfd-3d4a-9b6e-41d9d4e7ebee | -21.0705 | -47.2568 | 2026-07-07 00:30:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 8610e32f-3042-3d00-81f9-2e026bc26fb9 | -13.241 | -54.289 | 2026-07-07 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 716081b2-5d77-3985-b9f3-d4b34dc77813 | -11.6789 | -44.5479 | 2026-07-07 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 22ec445b-a537-3a0a-a203-78dba0e75b81 | -11.6785 | -44.5712 | 2026-07-07 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 387290ea-f1d3-36f4-a685-ec26d75ab522 | -11.6592 | -44.5741 | 2026-07-07 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8eff004f-0b3b-370d-9b10-66f8833dce5e | -10.9397 | -43.0593 | 2026-07-07 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5368cbfa-8028-3e1c-a766-9152284ce50b | -6.9326 | -43.7032 | 2026-07-07 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 143.1 |
| f2d79ee0-c648-3ad3-a824-a4afd19f9b40 | -12.7741 | -44.5396 | 2026-07-07 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| b344fdf9-c54a-37fa-bd3b-07b9c38433ea | -10.9205 | -43.0622 | 2026-07-07 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| aedc4690-bc25-303e-8fe6-f8c4ea2805ef | -11.6785 | -44.5712 | 2026-07-07 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 56e72a0d-de3a-394b-9387-a36dc7a79c65 | -6.497 | -42.238 | 2026-07-07 00:40:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 465406f3-720b-3e20-b24b-30722067ab26 | -6.9138 | -43.7049 | 2026-07-07 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 233.8 |
| bcf14688-81b0-35f4-b89d-5a69794e7784 | -6.9135 | -43.7281 | 2026-07-07 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7c086258-56b6-3c0c-9a27-4b968c0d185c | -6.9326 | -43.7032 | 2026-07-07 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 6f853bfe-2cbb-345d-8819-3d6aabb699b1 | -11.6597 | -44.5508 | 2026-07-07 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 63e1accc-8543-3335-9aca-49acdabdceb2 | -11.6789 | -44.5479 | 2026-07-07 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 9e9814a1-3472-3bf5-b715-ece38ffdef86 | -6.895 | -43.7066 | 2026-07-07 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| cd332900-cbcc-3543-8be2-dc2259829d95 | -13.261 | -54.2249 | 2026-07-07 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 154.6 |
| 0edf50ba-63b4-3ab5-a29b-aaadfcfa8eda | -4.2811 | -48.3518 | 2026-07-07 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 250bb674-7cf0-3f02-9bba-bc36ffc0be60 | -10.9397 | -43.0593 | 2026-07-07 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6a24a618-936a-3bcc-99e3-e3c18b0c46ed | -12.7548 | -44.5428 | 2026-07-07 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| befc82e9-727b-3614-b29e-2a366d919999 | -11.6592 | -44.5741 | 2026-07-07 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 84559706-057d-3574-939a-e3a0a2007a5d | -11.7485 | -51.528702 | 2026-07-07 00:47:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7190eaad-3c26-336b-b3e7-8106451ff4d7 | -6.4265 | -55.7911 | 2026-07-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e445154-8739-3dac-af5d-0d3f3d7b71ad | -13.7657 | -52.7178 | 2026-07-07 00:47:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e00878fd-1ea1-3cbc-bd3d-cbc18ad87f47 | -13.3274 | -54.351601 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4959a2fe-adf6-3067-b074-250a2d17d80c | -13.3293 | -54.359798 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7c9c61b-a4d5-3f0b-9230-0d9f5e8ad8bb | -7.6301 | -50.0168 | 2026-07-07 00:47:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a522f8c-c4a9-3053-a44e-1fc12f6bdc3f | -13.5423 | -52.9067 | 2026-07-07 00:47:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa02d5e7-7801-3a73-aef1-56c478979caa | -4.277 | -48.346298 | 2026-07-07 00:47:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2472538-b40c-3383-b575-1802801f71ca | -21.0609 | -47.2509 | 2026-07-07 00:47:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bed84872-c0b7-3e97-a2da-2739cfb3da7d | -13.5303 | -52.899601 | 2026-07-07 00:47:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0673a51-e421-3f43-b6de-d76ada0682ea | -13.2556 | -54.222 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db564398-7483-3151-a631-5d4ef6dd8599 | -13.3195 | -54.362202 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0da63cd-210d-3fda-9977-212e5dc5ab29 | -13.2654 | -54.219601 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7e40e4-0168-3a28-a95c-0db6bec33f6f | -13.2728 | -54.3391 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f523a6f-6f39-3a36-952c-72cfbb96ad2d | -23.557899 | -47.503899 | 2026-07-07 00:47:00 | METOP-B | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a95f657-4171-3667-b47c-2907a1229acc | -13.3176 | -54.354 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ca56199-f7e3-3a5d-b62f-27a152805882 | -4.2835 | -48.3727 | 2026-07-07 00:47:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a715d5af-9379-3c48-a5ef-aca8b96d838b | -13.2942 | -54.342499 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16389ce9-13d2-3340-a0a5-f8aa8d409b48 | -21.056499 | -47.234501 | 2026-07-07 00:47:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ebfa0ecb-17cc-31e0-8745-dcd43b4ee830 | -8.5525 | -63.357399 | 2026-07-07 00:47:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f4add649-c9ac-35f7-a028-203ead883df7 | -13.23 | -54.289001 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb889827-96d8-3094-855a-094a20ecf2ee | -13.5326 | -52.9091 | 2026-07-07 00:47:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| db0b38d1-7165-3185-8c94-c34b1dfb9331 | -13.5989 | -56.613098 | 2026-07-07 00:47:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 52b2e969-776c-31da-8aff-58f511fc1086 | -8.7356 | -54.5452 | 2026-07-07 00:47:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c86e3865-e0de-39bb-8ce8-c9c1999360cf | -13.2673 | -54.227798 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc9f03a-23c3-30a0-a9ac-08048c62a5f0 | -13.2844 | -54.344898 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c41a2f40-deb7-389f-907b-235a7dbe3ea7 | -13.3214 | -54.3703 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b8bfea9-d47d-3ebf-8c19-7ae8eb093531 | -13.2536 | -54.213699 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7993bcce-2f10-3069-ab25-80f43f10d40a | -13.2825 | -54.3367 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81d0f44a-97c1-36bd-930d-810ca77c9b3f | -21.0513 | -47.253799 | 2026-07-07 00:47:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0772c7cf-ed83-3a5a-9300-7a5c2af309d5 | -12.7439 | -44.506401 | 2026-07-07 00:47:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1aab550-89ad-39e7-bc74-623cac1b7857 | -13.2747 | -54.347301 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a658cbd0-a69f-3eac-ae9f-0ff9a0a3f675 | -12.7344 | -44.509201 | 2026-07-07 00:47:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b572333b-fa47-32ab-8402-2b03fc11a4d4 | -11.7455 | -51.516499 | 2026-07-07 00:47:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20943600-75eb-3bd7-afcf-f1680fe8890c | -13.2766 | -54.3554 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8606c1-496a-38a5-b0a0-8904c299ec3f | -13.2806 | -54.328602 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93bca723-0c77-3bbd-8071-fb77f0f27ccf | -6.4284 | -55.799301 | 2026-07-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa7251f4-afcf-37cb-870c-df8e9aa8b1aa | -13.5973 | -56.605999 | 2026-07-07 00:47:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7384e7d5-fe2e-35a9-8e51-754774a60fe0 | -12.744 | -44.543598 | 2026-07-07 00:47:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a932806b-b2e3-3a31-a144-53ef8ed5f597 | -10.899 | -56.847599 | 2026-07-07 00:47:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efd2e91a-0082-3d87-8595-b3eab52dbb4b | -13.7681 | -52.727501 | 2026-07-07 00:47:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be96c0e5-c3b9-3c10-a480-27996e3618c9 | -12.7535 | -44.540798 | 2026-07-07 00:47:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4135db48-7147-391d-91e5-56f2e33bd180 | -13.3312 | -54.367901 | 2026-07-07 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b91369e7-87e1-3d41-88c1-055de118b3b1 | -11.6981 | -44.545 | 2026-07-07 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |


[Clique aqui para ver as próximas entradas](README4.md)
