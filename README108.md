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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf42de48-a2aa-32af-9558-1564108fee54 | -14.57339 | -52.46888 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a3a1b31-1ade-3294-a7f3-22fb80c21106 | -16.34697 | -51.45864 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e347e3f9-4adc-3fc2-847d-56f85a72253b | -16.05025 | -50.99788 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d70e69ed-5489-33af-89ac-558830b90eb6 | -15.29672 | -47.32838 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28cb4e70-1427-365f-a178-0b1775be644e | -17.94601 | -57.59533 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7d5a6e89-5945-3838-a9dc-bcea762ae3ea | -16.3361 | -48.06516 | 2025-10-05 04:49:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f3a83da-5949-3099-a836-188e312e8194 | -18.25174 | -53.35477 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efaa6138-18a1-3330-9b80-04d97955bc78 | -17.70845 | -56.74802 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e18aae12-efff-3281-8ebb-c9e9b691ccb4 | -13.84177 | -47.91494 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ed0c98d-0349-3864-a617-ab92b2797c51 | -14.33042 | -47.70013 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1eaa50f1-7257-3759-988c-8b43ece90f84 | -18.20705 | -53.38054 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad8409d9-5b16-3e5e-bd6a-9e76e302c466 | -15.98365 | -50.90369 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ffdbefc0-229d-3e8e-b0b5-ab28974078e2 | -15.98707 | -50.85585 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7428b894-13b4-3445-84d8-c1c5ecad4c04 | -14.5833 | -52.4486 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c8675f7-90b3-30a2-8548-1ff63fcc73f0 | -19.8413 | -46.52446 | 2025-10-05 04:49:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2f59cb2e-cc38-3267-9f74-a8f916741826 | -14.74508 | -54.6226 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 89b48661-2858-37b8-b076-40219a2fa40f | -15.29204 | -47.33144 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4b98631-0255-35a1-b797-432b8c8444b6 | -14.8769 | -48.13577 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c50c8323-3f7b-3fb1-ad8c-dc7d6e77abc9 | -11.84719 | -63.72157 | 2025-10-05 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a2f704e-e1b5-38d0-835c-38485929df12 | -15.21535 | -56.81082 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bab0908f-375c-3a43-b431-7260ed754874 | -18.20211 | -53.36856 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8f3851b-3a65-3920-b9d0-f94e7b457b65 | -15.87465 | -46.25316 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8195153-fdff-3b84-8ba5-7574a0152b26 | -17.85355 | -57.63119 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 2dbb7e7a-f9e8-3eda-a909-ad32e9d59bc1 | -16.03979 | -50.94783 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc7981d7-239b-3007-904c-f2eba64f9106 | -19.94726 | -44.64008 | 2025-10-05 04:49:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 02e54682-efe6-3fc1-9f83-6ac9e7e80338 | -16.00559 | -50.85063 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 29333082-5d43-37ff-abc8-ded4384ea2be | -15.51281 | -46.84834 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ef4beef-d56e-38fa-b762-7ecc1dc0cd34 | -16.00032 | -50.93512 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4737a305-efab-34b9-9956-ac37501d3734 | -14.68956 | -48.30681 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69a6f78d-0d51-36f3-9175-eb3f074b45bd | -14.60338 | -52.49604 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43d6bade-642b-3204-a725-ceb6ec4c2372 | -15.42616 | -50.20801 | 2025-10-05 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbcd648c-c4f4-3258-ba09-717aaeaf9439 | -17.86837 | -57.63398 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6e1e6a9e-454e-38e1-9be4-2b4ee319695f | -14.60121 | -52.53213 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1fb0865-b814-3c9f-97b0-332935cbc6c8 | -17.97766 | -51.14637 | 2025-10-05 04:49:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6dfe0cc4-1c91-32ea-aedf-258680c8b61c | -15.3014 | -47.32526 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc63d7ad-1871-3932-9cec-c23edee22fe1 | -11.84615 | -63.71892 | 2025-10-05 04:49:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c69be9f-b28c-3e03-8188-8dae6bc6d678 | -14.6537 | -48.33066 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c465d221-932c-3044-b3d1-1833882cdff6 | -14.6078 | -52.51135 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c9f9a9d-b184-3fab-aa8b-f1a804c4ff6a | -15.24964 | -56.76612 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b39e8c3a-5842-394f-8d13-56e4f496a841 | -14.68607 | -48.33278 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55d19427-6d28-3172-861d-11898b4ef485 | -13.73042 | -51.30917 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b582257f-02ab-350c-bb8e-09639bcc8542 | -13.85296 | -47.92175 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d852ed13-ad3c-3354-b64c-d751c8ff7eae | -13.63784 | -48.68511 | 2025-10-05 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bda8ce7a-65c4-3134-beab-01d9e94e6e3a | -15.29771 | -46.31197 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7bb418c-5cf4-38ab-9f77-623922f84982 | -14.59971 | -48.34766 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ceefe0b5-6ffd-3ddc-9428-b50ab29d2e84 | -16.34526 | -51.47019 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7b1cdbff-796e-36e5-bd5a-9acff528b5a3 | -14.2739 | -45.87165 | 2025-10-05 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e48ec684-5493-3c15-bf62-0b3aa2464e3b | -14.91875 | -46.85707 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 02ab7331-4d43-3d9f-8b48-1b944a83ca3e | -17.95405 | -48.53801 | 2025-10-05 04:49:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 319e8529-0e8f-3653-9ace-ba646cf079f9 | -16.16475 | -57.57098 | 2025-10-05 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b81ce73b-4b93-3e05-9820-bc55a958f528 | -17.95254 | -57.60157 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| a481e8bd-cd5a-38b2-90fb-a77dc8876865 | -18.17346 | -53.35644 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43422d97-3cb0-3aaa-bb75-1dde857848db | -16.00554 | -50.92371 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 49fcef35-c423-3cb0-af73-b5935b6d8492 | -19.95231 | -44.64353 | 2025-10-05 04:49:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b315ae8-eed5-3393-bb5b-8f39717158bf | -12.9118 | -54.73798 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0454e17d-938d-350f-b20f-97ecb56cae23 | -18.33856 | -52.01567 | 2025-10-05 04:49:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8cb19c5-5137-34fc-a9c0-4ef0d1465f9a | -16.04112 | -51.03653 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2141c05-b4aa-333c-8af8-6e02fb091f0b | -18.25123 | -53.33605 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1daeefca-614c-38da-b3d8-141902652a09 | -16.03227 | -50.95093 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5f716baa-5185-3754-8f0a-6d43df631228 | -15.55547 | -46.96326 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d1cd5cf-8028-337c-89e2-e0cf3e0bf71e | -15.98246 | -50.86309 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f0bc97e-23c3-367e-94be-d52f553f63f2 | -17.91001 | -57.62598 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 917b76bb-29a0-358b-850a-e9dd0a65c4ff | -15.31904 | -47.32114 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5babe996-776c-326b-b16c-dc38dc9b6cd2 | -14.58495 | -52.45984 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f73aa31d-d0eb-30c6-9264-6ea45fb448a1 | -18.16413 | -53.3288 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c0e9faa0-9450-3e92-b7cd-0ebefbcf88d8 | -15.97905 | -50.91099 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 74d2060c-ad77-3c57-b457-6b8145be4d8a | -17.9736 | -51.14983 | 2025-10-05 04:49:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1aa0eeee-9695-391c-949f-10006c876335 | -18.19055 | -53.35548 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7eb55731-e5e4-3adc-b46f-1d8f90d93d01 | -15.76159 | -46.26036 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9baa093b-9432-3184-9454-d1592f81d241 | -14.26933 | -45.87111 | 2025-10-05 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a87f528b-9995-3566-9b84-4513c48acd8b | -14.67791 | -49.60828 | 2025-10-05 04:49:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e921a040-304d-3607-9d70-36f733b01897 | -14.74758 | -54.64978 | 2025-10-05 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ceb28b3a-5f60-3d10-a890-12e13b8ba48a | -15.70452 | -46.2748 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f83dd2f-9ffd-34ba-af2e-9c6dbec612fe | -13.72633 | -48.0904 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7f2ad8e-6043-3316-94d2-16ecfeac72a5 | -14.64672 | -48.32365 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 51708c02-2835-3291-a90d-bf5924181e47 | -14.64917 | -48.33464 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b8ef3569-0c9f-3e2d-8c13-9e217caf1be6 | -15.54866 | -46.84443 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27898ac1-714e-33ef-8eaf-0570c3ac9495 | -16.00906 | -50.85122 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9a0537d2-6fd3-3592-89fe-cda699ae67c5 | -15.30074 | -59.23471 | 2025-10-05 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dce83b2-f944-360f-b1e4-fa49e38819bc | -15.98826 | -50.92076 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bb088c83-d2a7-399b-804b-91d601a747fa | -14.68336 | -48.3529 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9acb9455-10d4-3db8-8622-7bd747a7ccab | -15.31073 | -47.31936 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd00bc32-7642-3698-9451-2864536ab691 | -16.3872 | -52.16191 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5b5d32b-a1e3-3b7d-a7c9-d21b7140fe41 | -15.58888 | -52.45451 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47d86bbb-15f4-3733-a625-bc3326947453 | -15.40051 | -47.95473 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ac0b2ce-624b-3273-8fa1-c85224d053ca | -18.19946 | -53.2976 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2450cfe4-7435-3436-9257-15c1c9eb2f5e | -15.13834 | -45.7534 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9080f9b1-d94b-3758-87f1-36402299eb5f | -15.74771 | -51.00869 | 2025-10-05 04:49:00 | NOAA-21 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f08b5c5b-4afa-3a8b-b4ae-4ada08df65f1 | -14.75036 | -54.65402 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e0dbe24-90de-307b-b2e4-7f8da4f3fb24 | -19.02044 | -50.60456 | 2025-10-05 04:49:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2570166d-246c-30a4-b35c-a2c8eda51012 | -14.69223 | -45.17546 | 2025-10-05 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfe056d9-5e6f-32fe-a336-937908f41d86 | -16.04839 | -50.93735 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a805f76-297e-34ad-b403-c2165be47fa8 | -14.91547 | -46.84858 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da1b15b0-75b0-3205-b5bc-882c2420cada | -15.77582 | -46.25718 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a293921-928f-31a3-bf71-e436e551bac3 | -15.20863 | -46.38281 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d56679f6-39c5-38d2-9ff2-4fa73465c5eb | -14.1969 | -46.67779 | 2025-10-05 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddf8911b-aeaf-36ee-9a04-a62ac8b4f6e8 | -15.13958 | -45.74327 | 2025-10-05 04:49:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dcbb81c2-dfbb-3806-8c5f-581f26c07d06 | -16.91438 | -52.04862 | 2025-10-05 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b91297cb-0fd3-3c4f-9e02-31d1f8d3d184 | -17.89552 | -57.64277 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 90a0b02f-8601-3c79-a195-f2837d2f801d | -15.98883 | -50.91682 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README109.md)
