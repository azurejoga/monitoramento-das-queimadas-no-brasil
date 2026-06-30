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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a42a645b-379a-32e2-a4f4-47d78c08ea94 | -12.84862 | -44.39364 | 2026-06-30 04:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 765934f6-e41b-3294-8a33-921e4c5528c3 | -16.17612 | -59.33998 | 2026-06-30 04:57:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04f5a292-ba77-33e3-81f3-e008a47a95ae | -12.50833 | -48.27451 | 2026-06-30 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d0f1060-2be5-3299-8266-079877ea8fbb | -11.37784 | -55.80536 | 2026-06-30 04:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05269819-21e8-3826-a7fd-717766bc15e3 | -17.44634 | -47.16648 | 2026-06-30 04:57:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cd6e6fe-7bc6-3b0a-81ae-688c4eed4711 | -11.89159 | -57.13742 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e85f097d-af59-38c1-8203-24fa7966d2fd | -18.24761 | -53.8474 | 2026-06-30 04:57:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05fc536b-cc57-392d-8166-ddb9ce345634 | -13.25905 | -56.80658 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60d28f2f-1255-325d-8c23-8df0dbfb0bf5 | -13.2607 | -56.79731 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7372f98c-d97d-3956-b4ed-0eb8cef18803 | -10.04568 | -59.11414 | 2026-06-30 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 915bf1f9-391c-3b23-b364-b5ea513d3eb3 | -13.26281 | -56.80729 | 2026-06-30 04:57:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7f83498e-f099-398d-ae18-61326624f61c | -12.50903 | -48.26958 | 2026-06-30 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| da630618-e270-3267-9481-a54475296ee0 | -11.95377 | -58.61429 | 2026-06-30 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f2fa847-5191-3e03-bf64-1fa569899654 | -12.21802 | -56.56027 | 2026-06-30 04:57:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 27e51d07-1758-359b-92ec-d124ad9cd22f | -10.25099 | -59.30454 | 2026-06-30 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aba63e72-de2f-3006-89a3-c0e1540d5a43 | -12.4517 | -58.48824 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9302eafd-904d-3707-8da6-c29903c47761 | -11.89724 | -57.12803 | 2026-06-30 04:57:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dc382c7-0cfd-3ddd-a5ef-5cc38595eb01 | -12.44325 | -58.48665 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eeacdeb5-72c3-3c81-97c7-17d872fc8ef8 | -10.91328 | -56.85373 | 2026-06-30 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c3f3765-7687-31aa-addc-bde558cb8ac3 | -12.28718 | -57.54952 | 2026-06-30 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8bc2117-10bc-32cd-b269-80823f559a70 | -17.44133 | -47.17041 | 2026-06-30 04:57:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2605c9dc-971c-3aff-a1b1-3144998fc261 | -12.45445 | -58.49717 | 2026-06-30 04:57:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ddae6b9-28b3-36a9-b1db-1ccd9406787c | -21.31634 | -48.53838 | 2026-06-30 04:59:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad17214f-ab91-3a5a-82c9-e2de4d4a3e87 | -22.79167 | -49.34841 | 2026-06-30 04:59:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3126cdb4-065f-36d6-bada-17245ee83eb1 | -22.80517 | -49.34195 | 2026-06-30 04:59:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 049b66b4-d8f7-3cd1-950a-74cc298ba058 | -18.77801 | -57.3476 | 2026-06-30 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| dbeb4145-79e9-3b6d-aa9d-97ee5f79ef78 | -18.79585 | -57.37352 | 2026-06-30 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 36469f8a-e254-3929-a222-2e017b9b9895 | -21.31388 | -48.53893 | 2026-06-30 04:59:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecfbbc87-ad97-31db-b6cb-cfb9ba82a77f | -22.7875 | -49.34786 | 2026-06-30 04:59:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60bc7e25-e834-3557-8274-012f9b0b6247 | -20.97147 | -49.74348 | 2026-06-30 04:59:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 611379fc-244f-3b57-b39e-5439e3fe3c08 | -21.31584 | -48.54256 | 2026-06-30 04:59:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d4b167b-5df2-3c53-9870-3ce1925f4c62 | -22.79216 | -49.34442 | 2026-06-30 04:59:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f21718fd-51b9-37b9-accb-f7f4f7793970 | -18.78161 | -57.3483 | 2026-06-30 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d37b9240-8452-3357-ac19-1ec5aefa6cc9 | -22.788 | -49.34386 | 2026-06-30 04:59:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30ca00ed-9f7c-3ef1-84a6-dc811c02dcb9 | -21.31335 | -48.54311 | 2026-06-30 04:59:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 208becb1-b548-34fb-a08f-43ff32e6203d | -22.78383 | -49.3433 | 2026-06-30 04:59:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 70065cb4-5cb6-3dc9-aa2c-e3f03a64a008 | -10.9401 | -43.0355 | 2026-06-30 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 90eff1a4-93b3-3b3b-a1b7-b4100a5cda28 | -10.9593 | -43.0326 | 2026-06-30 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| bc4de07d-6c02-305c-a5a8-e3519c581404 | -10.9397 | -43.0593 | 2026-06-30 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 8e734c82-e4c0-3fe6-9795-3eee74addfc9 | -10.9401 | -43.0355 | 2026-06-30 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 239.2 |
| 340cd877-c53a-33de-bd42-ef7f065c10d4 | -10.9397 | -43.0593 | 2026-06-30 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4f178ad2-c983-308a-96ba-abfbf12d51ce | -6.92079 | -51.94779 | 2026-06-30 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4301f55-d2f8-3326-b63e-f8a208f44a15 | -7.4302 | -49.87531 | 2026-06-30 05:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 435e1911-dbb7-3093-bd54-09cf973870d1 | -6.22811 | -55.65236 | 2026-06-30 05:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17b985c7-0052-331b-9500-9bb05818379c | -7.63837 | -50.02734 | 2026-06-30 05:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2ee0f7f0-8f21-3d19-8c0b-516e292f0208 | -8.35605 | -46.82328 | 2026-06-30 05:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a206a57-fb32-3f07-9e2f-f7d946cc9e2c | -7.42952 | -49.88013 | 2026-06-30 05:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1289cfde-6dab-342c-b26c-13c6e9b18044 | -8.35661 | -46.81899 | 2026-06-30 05:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7db35a1b-1b11-3944-a9b5-1dbf8feb6dd9 | -4.33893 | -48.96191 | 2026-06-30 05:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 224e59c8-b5fe-3245-826f-998d30531f96 | -7.63912 | -50.02202 | 2026-06-30 05:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b0ae47d8-b0ac-38a0-8d90-70b3ead38e03 | -7.43517 | -49.8753 | 2026-06-30 05:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2b3be47-e6a5-39c1-bb6c-78be6f0824f9 | -6.92136 | -51.94392 | 2026-06-30 05:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1180d62d-73a8-3a1d-936e-081fdf6c6122 | -8.20819 | -49.8639 | 2026-06-30 05:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe96b90b-d48a-3bb1-97e5-7f06ca4fc13f | -11.78266 | -47.56917 | 2026-06-30 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82b7532b-574f-3d10-8aa8-503958d0ce3e | -13.7218 | -47.86776 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57f35225-3116-3d53-a1bd-27df99e8f75d | -9.31463 | -58.02675 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fd55af0-0c2f-3828-858e-034fd68a84a9 | -9.75109 | -49.03307 | 2026-06-30 05:16:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cce2362-d6de-33d2-b13e-e8befd4ef7f2 | -11.95711 | -58.61106 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f0ede5f-1234-3232-bf78-5c346279290e | -13.69789 | -47.87134 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7b95e97-a603-33ad-a288-9a360032dc44 | -11.37908 | -55.80656 | 2026-06-30 05:16:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bda0e6ad-39e8-39e5-8aaa-51666bbb3d20 | -11.87313 | -57.09264 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 227b23e1-57ae-3da4-a973-786dd0517092 | -9.60406 | -56.93318 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58f2e164-2710-3ef3-ab7d-22f003a63239 | -10.30463 | -57.14151 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| caa5a9cb-fc56-3dbe-a836-9744f99fd093 | -11.95986 | -58.6151 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6d904b4-e3e8-3ba6-b8e9-41d7852a56a3 | -11.73679 | -59.35378 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f334c5e-9fa2-3a92-ab01-3c9d201ebbb8 | -12.44787 | -58.49223 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4e4e7239-1de0-39e3-b136-7bcdd77e47e8 | -10.13835 | -52.4038 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dfb9b8d-450a-3ba4-88b7-269f5144e06f | -10.30799 | -57.14204 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b34e08e2-c51e-3701-8682-3e0dfbee74c0 | -13.71523 | -47.87137 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32172526-ed20-3aa3-8ada-9f7303653fb3 | -9.0842 | -59.484 | 2026-06-30 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a2e9a35-03aa-3c23-bde6-b450812c85d8 | -10.05318 | -59.10741 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e98606a8-67bb-3f6c-ac59-dd2413516821 | -10.29751 | -57.12962 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 89b98d41-24e2-3233-8b8c-9baa377c5e7b | -12.44897 | -58.48518 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bd7e5eb8-0ba4-391b-8831-319342b58d05 | -11.87086 | -57.08472 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7ee136a-a1b3-3312-b922-b8df98dff460 | -9.45349 | -50.84028 | 2026-06-30 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d2b0522-f76c-3130-a4dd-049a2c621cc9 | -9.08083 | -59.48345 | 2026-06-30 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c1b5bfd0-e1bb-3320-9434-b387fd0a9670 | -10.13014 | -52.40793 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9ef5657-4808-340b-bc08-69706f99574c | -11.89684 | -57.11903 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9e0f18b-2ddd-3f0d-8593-19cdc13ddf70 | -10.06611 | -60.49669 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc3f8f90-2c75-31f4-8d90-eb8bb2e8a22a | -13.25906 | -56.79073 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d87a45ad-adf5-3161-a601-e1b19c8cc330 | -13.66983 | -52.19483 | 2026-06-30 05:16:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af30ee32-5fdb-373e-b9ef-a0ca2190ed53 | -9.19407 | -45.32725 | 2026-06-30 05:16:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8f9ff66-2fb6-3f37-be9b-f61dc1672c81 | -11.89985 | -57.38132 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b1c2faf-05a7-3d87-acd9-1aa3ae36cd2d | -9.5923 | -56.92032 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a5bfa0b-f10f-3064-a208-c1792dc7613e | -10.30142 | -57.12654 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3a45762-8935-341f-9f8a-8000ea285db2 | -9.60181 | -56.92548 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13862d7f-677b-35a0-a318-9837ee774dd9 | -10.04597 | -59.10986 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ef53931-4356-3909-973c-4ed82b3a79a6 | -9.33005 | -58.01494 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edf06c6b-3ed8-3119-9dc4-53663212a9f6 | -11.21522 | -54.33955 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcdf2246-9922-3473-b7b9-394c188f7252 | -12.2036 | -52.86785 | 2026-06-30 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1f0dd22-286b-312b-93bb-e883841a2490 | -11.90417 | -57.13908 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5b098b6-f134-334a-bb03-1883cfe193f4 | -13.24012 | -51.56049 | 2026-06-30 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc171918-a893-3d64-b4ab-26cc27e11234 | -13.71813 | -47.85505 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cad2ae6-f637-3bf3-94a2-6cf1596d14d1 | -10.80373 | -48.56761 | 2026-06-30 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d63b153-7e6b-3109-81ec-f7af255d231d | -12.66951 | -56.38402 | 2026-06-30 05:16:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e09b49dc-58ed-3bb7-abb3-cf54d0b51da8 | -13.71625 | -47.86268 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e14b522-ed28-3361-9bfe-9a5a418baea6 | -11.92733 | -57.40425 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a100667-0662-3f9e-aa86-fd2868fcf05e | -10.14317 | -52.4004 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf762058-f732-3945-bc6d-60a56a8af822 | -11.23084 | -54.31255 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49458576-9d3c-3aa7-9283-7836012abb67 | -10.13409 | -52.40316 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
