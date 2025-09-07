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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ded840fe-1bb6-3450-9685-8cd9c6ecc282 | -14.24457 | -53.37992 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4e8b3299-e49e-3348-a1aa-cae193481bf5 | -19.89737 | -41.44088 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e79fad47-d7f5-32d6-8fa2-5dbf316acb74 | -13.00568 | -48.07965 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 909f7352-ad1b-34bc-a84e-b934329d664f | -19.06928 | -46.77779 | 2025-09-07 04:21:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d1c6d41-8a17-34d5-bfea-e63012ab61c4 | -17.69713 | -44.48795 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ae7edae-68aa-377e-a1ad-d6e7a643f2e4 | -17.55749 | -44.4039 | 2025-09-07 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 429cc3f8-1cdf-3fde-947e-e4b308bcd846 | -13.83636 | -46.28091 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ad29fad-da07-360b-babf-5a9122aa3926 | -14.82213 | -48.17649 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 990e8653-604f-31f0-8641-810daaf9e986 | -16.92089 | -45.79716 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54e0abba-dd5d-3264-b568-2a867f9ca7bf | -15.02581 | -50.0232 | 2025-09-07 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf24de4e-7981-3498-824c-dcf8292208ae | -17.36329 | -42.6414 | 2025-09-07 04:21:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 178729f5-7ae3-3d97-9af6-1976fbd06b15 | -20.53897 | -46.44662 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 8d546ee0-4dad-3d02-8fc2-7eca000c9359 | -13.83691 | -46.27737 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42eb07ca-5c68-339d-8e87-3ed319beea59 | -16.91808 | -45.79292 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df66d328-4af9-3c86-ab4f-0bc0e6c153d2 | -13.74301 | -46.91273 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ca52451-4c0b-3ad6-a0c3-1bf4db6df585 | -13.70794 | -46.87754 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 90e997a0-e69a-330a-a07a-e0e6e54f7e4d | -19.48086 | -47.77938 | 2025-09-07 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 63efbd36-cba7-31e8-a991-7702f5e29cf6 | -18.30041 | -43.33553 | 2025-09-07 04:21:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f7e8c72-816d-3e84-b715-0ecac866f72b | -17.9266 | -49.45451 | 2025-09-07 04:21:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c951923e-faf9-334e-a790-a7981debfe17 | -17.20657 | -46.86929 | 2025-09-07 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7f7a554-b5af-3a56-be7c-51812bd18cf2 | -14.5636 | -43.73111 | 2025-09-07 04:21:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83dca4d4-1008-3bae-8edf-27be01ab64a3 | -12.94311 | -54.77496 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 5be5104b-e489-3196-9874-aac8878cde5d | -12.93304 | -54.77299 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 146492d3-c4fc-342a-a3a0-3b83a128a786 | -17.68728 | -43.54203 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9222959-1ef5-39e6-b53f-468e0ad9fb38 | -12.94813 | -54.77603 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a8a9f38f-7d18-3e25-ba94-868c0d01eb14 | -14.48328 | -48.75979 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c88df9e-67b0-3a95-8845-dec44dadb6cf | -13.83694 | -46.25559 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca9e2fd3-d74b-3b52-9968-75bdd3255639 | -13.04785 | -47.09399 | 2025-09-07 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a39d0a70-1671-3942-84ca-e80a7b34a8d4 | -12.93808 | -54.77392 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| d32bf8c2-e5e0-3be0-a814-9d2a6100f0dc | -13.91534 | -48.03176 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86896eac-dcb6-346d-b7f7-37ea998a036d | -15.83621 | -52.28136 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e8552f5-ad2e-3a28-856e-591ce8549312 | -15.70548 | -47.51304 | 2025-09-07 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c954d654-56a4-3055-a883-b33ea93a8665 | -15.84945 | -52.27573 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d9fa9a80-6acb-38ea-a1a3-f7085563ba5f | -13.55185 | -48.10957 | 2025-09-07 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f841db8a-1fa1-3b8a-8037-70ba441026d7 | -15.5454 | -49.82122 | 2025-09-07 04:21:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baa3fb09-36cb-312a-a5c6-dccd33a04049 | -12.78551 | -52.95691 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1687da2-3182-3fc0-adfe-02cbe2851739 | -16.78446 | -51.35768 | 2025-09-07 04:21:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89f6ca3e-b106-3531-842d-05a1a8874cb3 | -15.83579 | -52.28127 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea141e22-b5f9-3cc2-82fc-2e0af45e7c65 | -13.0091 | -48.0802 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9c1a51b-d78b-3e12-83a1-2ed74ddff310 | -18.07541 | -47.98897 | 2025-09-07 04:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c208431-e592-3137-a4f3-10979498d8da | -13.66778 | -46.95852 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40a4b5ff-22e0-3c12-b981-74150daa793c | -19.59509 | -46.11581 | 2025-09-07 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b8beebab-5dd1-3b72-b9c8-36ed5b6202b6 | -11.15687 | -59.1583 | 2025-09-07 04:21:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 339392e8-959f-302a-a7af-4a7552668dc7 | -18.72307 | -43.65355 | 2025-09-07 04:21:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 92f4519d-bf99-3ce7-a0db-125d60d68f67 | -12.93921 | -54.76798 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 771a55af-95a7-35c8-b5aa-fbfce587f8d3 | -13.66058 | -46.96088 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a087f95-1799-30e4-95e1-765e2b4908d5 | -13.89926 | -54.00046 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a7a576d-c455-30a5-86b0-e4782ff482b3 | -13.27766 | -46.39959 | 2025-09-07 04:21:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98c67051-6894-37e9-a1c0-3f5e6cf8927d | -19.94199 | -43.61302 | 2025-09-07 04:21:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 325dbdf2-ea70-321f-9bb0-1fc6aa5630d8 | -17.68667 | -43.54653 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc8c059a-7ff6-3186-ae8a-de932052e13b | -13.74244 | -46.91627 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fb5d82c-8772-354b-8b5b-c707d35cfe9a | -17.67007 | -43.54236 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1419f435-f7d4-3a2b-8cce-dafc72cfda1d | -14.49172 | -48.77307 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68e3cb62-2a0d-3ebe-96d5-6f32b51904be | -17.57927 | -49.78956 | 2025-09-07 04:21:00 | NOAA-20 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 956433f8-fa93-35f4-af96-7974071777bc | -20.0179 | -44.59921 | 2025-09-07 04:21:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 535f9db2-c5bb-389b-ab67-c8bf0dac988f | -19.46932 | -47.7661 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4b449ed1-a384-3534-8cdd-bdbbdd9d0815 | -15.33488 | -52.7444 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2743f6cd-c658-321a-bf31-4e652d0073a8 | -12.77809 | -52.95784 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da0caeb7-132d-3485-9c22-e5dbe800cfca | -17.57579 | -49.78889 | 2025-09-07 04:21:00 | NOAA-20 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c802fae-d53b-389b-b491-8b4b77858eaa | -18.13336 | -45.33813 | 2025-09-07 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 918f13d4-2ec2-3a94-b451-bffb26bb6869 | -13.02743 | -48.07537 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23b64720-7c2f-3080-9934-5655e1a5de3a | -19.06594 | -46.77724 | 2025-09-07 04:21:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32fd5213-e095-3501-b554-d4e74d197d10 | -17.06684 | -46.47908 | 2025-09-07 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e576f1b-c6dd-36df-826a-2f9bd18f76bb | -16.31785 | -52.93895 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cae9e94-4b15-34aa-9412-ca34c99d71bf | -13.83418 | -46.25151 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df4f75f4-19ba-38d8-84e4-be526b27e111 | -17.90822 | -47.07206 | 2025-09-07 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 56f49de5-0a06-36b1-83d6-d38be0264f18 | -17.95239 | -42.77518 | 2025-09-07 04:21:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70131a20-fb9a-3a94-8fa5-a054bc3c15e9 | -18.35901 | -43.91523 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f37335d-0dbf-3c83-9235-cce2ee5d10b4 | -19.59824 | -43.68007 | 2025-09-07 04:21:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b615bd3c-6f23-355a-9aca-9e4941d5876a | -17.68183 | -43.53955 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee5e2d04-2576-384d-80e9-81fc7fb07cff | -13.82587 | -46.28282 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af89ee01-12a4-335c-841f-b35e500269a7 | -13.05989 | -48.06987 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d3a2350-25a8-3af1-9ed7-b1298461f651 | -16.93703 | -45.74628 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2fdfb03-3668-3424-937b-9abb6186e752 | -13.72371 | -46.9057 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0fe30a89-1c68-39c8-8ff4-de234d519f01 | -17.55487 | -44.40104 | 2025-09-07 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ab8cd09-ebfb-3192-9f95-3b85510030c9 | -19.83392 | -44.23729 | 2025-09-07 04:21:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0574ad1a-cab6-3d9b-b80a-1ba019dc6758 | -15.13649 | -52.35371 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e34a994-308c-3495-9f5f-920d8883fc4f | -13.85515 | -46.24768 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c20e6a0c-3b33-38ae-a534-1ef0ec27b8b7 | -18.01488 | -44.91024 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59291d9e-5183-3704-b3e7-577fde83960b | -18.38417 | -43.89614 | 2025-09-07 04:21:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a44164b7-9e38-3157-8688-442eae9cf1de | -18.02117 | -47.08726 | 2025-09-07 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c14fcfe-5746-3aa9-95ee-12ad50c207a6 | -17.95073 | -45.29836 | 2025-09-07 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9dcbfab-574a-301e-8b69-9b9ebdbc354c | -17.6707 | -43.53786 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 49a25d16-0a57-3408-a973-bfb0abe81662 | -13.71069 | -46.8816 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5e6a9fe-47db-3d69-8eb1-6b4b7aef31ef | -19.48042 | -47.76054 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10d7b507-6013-30e6-a796-53f1c1bfaa33 | -19.07911 | -44.65614 | 2025-09-07 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c81784c8-c504-3b22-b73c-e2702c61e995 | -13.82036 | -46.27466 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1101dcad-e02d-39ed-b298-368ea02d1832 | -14.85466 | -46.69247 | 2025-09-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c1c218f0-582d-39b8-a1e9-95743cb806ad | -14.44424 | -48.46381 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 221fdbcf-36fd-3a8e-883c-a577fafd87fe | -12.77256 | -52.92607 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6cb6a79-6131-3b9c-bc7c-c34b1f48b49b | -13.74575 | -46.91686 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19ccb66f-0a71-37d8-bfdd-fc24005da4ca | -12.95088 | -54.78908 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7819e09f-f14c-3868-87e5-98a09bcb543b | -13.0633 | -48.07051 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34eeb50f-08ed-3bbd-999b-9ad546625431 | -13.02062 | -48.07417 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46d8e99f-1c13-34af-8e0f-9e8ba2ad1876 | -13.05118 | -47.09454 | 2025-09-07 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69d1a83a-247b-33d6-88a7-1078297006cf | -18.23909 | -47.64454 | 2025-09-07 04:21:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7c681096-65bd-3efb-b19a-4f562fefe1ad | -13.05185 | -48.07613 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3ea78ed-acfc-3df5-abe2-451aef471612 | -13.82607 | -43.86283 | 2025-09-07 04:21:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c8547ca-3af3-3190-8094-f2b29a998440 | -13.78743 | -43.16233 | 2025-09-07 04:21:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c2fb7ba-d333-3c11-8a51-45d8980f78a7 | -20.09879 | -45.32068 | 2025-09-07 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README58.md)
