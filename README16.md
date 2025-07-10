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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ac82422-4928-39d0-97a6-16966b6c99d2 | -21.77402 | -52.75779 | 2025-07-10 04:08:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| acb218ce-38bc-323b-ab1b-f09c9f4810ff | -21.7733 | -52.76115 | 2025-07-10 04:08:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 082caea0-f2d4-310f-8283-5a89d9347929 | -20.96272 | -56.58936 | 2025-07-10 04:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 030c529b-cdba-3734-a0fa-9539f99dd846 | -21.35152 | -48.62598 | 2025-07-10 04:08:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c970b6a4-0205-3cd8-a304-1538f1dc8734 | -22.24533 | -49.60957 | 2025-07-10 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 374e01b8-e4af-3549-9bd6-46b3dca96f12 | -21.76208 | -48.12495 | 2025-07-10 04:08:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05666342-478c-3779-a88c-c017af740ca1 | -21.43857 | -54.57736 | 2025-07-10 04:08:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ffcbf04-5f51-3cee-a752-d167dd01fd36 | -22.67888 | -42.85666 | 2025-07-10 04:08:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0e42fa22-ebe2-3a3f-b31d-543f1b5fc541 | -21.34754 | -48.62513 | 2025-07-10 04:08:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e4279c82-cb64-3821-b192-09b1290fa2d8 | -21.43954 | -54.57314 | 2025-07-10 04:08:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 480262bc-cf4d-3cc6-b41b-13bb5128c55e | -22.24831 | -49.61177 | 2025-07-10 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b777d7e9-93a5-36f6-ab93-23c91b69ff6f | -22.24419 | -49.6107 | 2025-07-10 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4a6e5019-50a5-3b42-a941-14c4b92e2920 | -22.6761 | -42.85227 | 2025-07-10 04:08:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 86d0a5e7-6508-3d0d-8986-2a6983e03e85 | -22.24453 | -49.6136 | 2025-07-10 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6d432fb3-42b6-340d-8786-c44f9b3d844c | -21.35252 | -48.62059 | 2025-07-10 04:08:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5da66ddf-8591-3e8b-a137-61098c5b0091 | -21.7625 | -48.12675 | 2025-07-10 04:08:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1b1b9e6-0d35-3fcd-a10c-4474fc00eff2 | -22.67553 | -42.85608 | 2025-07-10 04:08:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8d18c921-5694-3455-857b-d7cd81369a62 | -8.5211 | -43.3063 | 2025-07-10 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| c2d60a47-9e80-3630-b468-a9396477a4ba | -8.5022 | -43.3085 | 2025-07-10 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 289.2 |
| eb81f1ad-0ac5-3f92-b79b-667cff096034 | -10.5773 | -49.1533 | 2025-07-10 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| ba4f8edf-8c79-3709-b8b0-67bb6a41b470 | -10.5776 | -49.1316 | 2025-07-10 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 10ad28af-0391-383e-9d32-c39886e81a8e | -8.5018 | -43.332 | 2025-07-10 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 69f22d0d-825d-3f28-bedd-8b752b5c5fab | -8.5025 | -43.285 | 2025-07-10 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 225.3 |
| e1db5c80-1b86-36eb-912f-6d7649421d91 | -22.6647 | -42.8699 | 2025-07-10 04:10:00 | GOES-19 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| d9dab027-aafc-3ab0-8fbd-302089ab64be | -10.6675 | -49.4679 | 2025-07-10 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0a5118c6-0fd0-3f44-a129-09320b003f26 | -8.5214 | -43.2828 | 2025-07-10 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 0c565537-d61d-3ab5-8dde-263fa275094e | -8.5028 | -43.2614 | 2025-07-10 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| bb7b4f94-c6a6-3e91-91c7-ed402c0c46e8 | -28.58685 | -49.44211 | 2025-07-10 04:10:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d7a15060-918b-3044-82b9-4842e7251d4a | -10.5776 | -49.1316 | 2025-07-10 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| fcd54850-a872-3377-8029-9c784d127e5f | -10.6675 | -49.4679 | 2025-07-10 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 21d08121-a910-33fa-98fb-73fe3f667e98 | -10.5773 | -49.1533 | 2025-07-10 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0839a71a-f665-3551-9a56-72128be5a496 | -10.5583 | -49.1554 | 2025-07-10 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| dce4a3b1-29fd-382a-8612-9a0dbc3a6a28 | -3.45156 | -48.88381 | 2025-07-10 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53030dd2-4c59-31ee-b0d8-1bb0f2932265 | -3.74698 | -47.1185 | 2025-07-10 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ede836c2-88e2-38d3-ada0-7cee6f703c54 | -3.10978 | -47.51148 | 2025-07-10 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b0d43d7-5341-3ec1-9fd8-baf1ef51bcd3 | -2.98953 | -47.45189 | 2025-07-10 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df26c834-2b53-3881-894c-ebb9460663dd | -2.44097 | -47.32584 | 2025-07-10 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 981a6b2a-ab99-3cd5-90a5-8206910641d9 | -3.81191 | -42.54718 | 2025-07-10 04:23:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d411dac4-7efa-3fb6-a9bb-5457d78a9d0a | -2.74661 | -54.06404 | 2025-07-10 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 600e5072-f6c4-3014-aa1e-d779fa2676a5 | -2.44104 | -47.32954 | 2025-07-10 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b65705b-0cfd-384c-b10d-cfab6df1945a | -2.4404 | -47.32951 | 2025-07-10 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43d7f310-3aa8-3eef-9279-4fb45455285c | -3.74641 | -47.12207 | 2025-07-10 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0950886f-6529-32a6-b3f7-9c489415a40e | -3.46215 | -47.67597 | 2025-07-10 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f2dcacc-1757-3928-b6c4-bba20a08a8df | -2.44444 | -47.33007 | 2025-07-10 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b4d414d-8999-3501-83c2-2fe5414d6f97 | -2.44163 | -47.32587 | 2025-07-10 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f93a86e-509e-3d9f-b5d5-54e3599ec7e0 | -3.4509 | -48.88793 | 2025-07-10 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dfac0e6-e615-3c0a-ad66-ada0a2db598a | -2.63355 | -47.30641 | 2025-07-10 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c46e45c7-b411-3b76-ac40-8dab7301f7af | -3.39545 | -43.37111 | 2025-07-10 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb75c60d-e17b-3e6a-9cf4-08aa10985170 | -2.44365 | -47.46587 | 2025-07-10 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6586adc-c3dc-31ad-afee-5263c69f6db6 | -2.44425 | -47.46217 | 2025-07-10 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e1bd6d7-cbec-3c8c-bab0-205044b410ed | -3.41017 | -48.91117 | 2025-07-10 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dca474c-2190-35b6-a4ae-f3a4fc0cd7c0 | -3.10648 | -47.48841 | 2025-07-10 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06a6c43e-2d17-38ef-8e30-6f7f8a27323b | -3.44796 | -48.88322 | 2025-07-10 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de260fbd-1ecb-3391-88d9-27efaedf224c | -2.44503 | -47.32641 | 2025-07-10 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b34c851-1c1c-3fda-99b8-b4c92cba7408 | -3.74977 | -47.12259 | 2025-07-10 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1a8d246d-9381-3b3a-a12e-4ba66a60c0c0 | -2.30858 | -46.99314 | 2025-07-10 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6659b3a-eede-3b90-bed8-0dd20cfba7ca | -3.10637 | -47.51093 | 2025-07-10 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e47022e8-ee0d-319c-a948-ee0dbf08c829 | -3.81256 | -42.54299 | 2025-07-10 04:23:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5b6fdfc-d75d-360e-8dc3-d1038a70dbc7 | -3.39604 | -43.36728 | 2025-07-10 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20931310-79c6-3ded-8247-f6c56be6fc02 | -3.46156 | -47.6797 | 2025-07-10 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c93ac6-731e-3c6f-8558-5c626c61a946 | -3.51438 | -47.21409 | 2025-07-10 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a60c045-b45f-339c-8052-0d3ca233fb17 | -3.75033 | -47.11902 | 2025-07-10 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec36cf87-462f-33b1-8925-9bb28854d477 | -8.35851 | -43.95288 | 2025-07-10 04:25:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f05e79af-35aa-3cca-8775-8d36f049db42 | -10.64479 | -44.48917 | 2025-07-10 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce1fdf87-3948-3fae-a057-01ea01eea3c7 | -10.57777 | -49.14985 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0cbea176-cfe5-3091-bfaa-e6e14966ca3d | -10.65767 | -49.45628 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 433d2db0-3fbb-39b4-892a-e0b5f3c60ec9 | -7.16027 | -43.70041 | 2025-07-10 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4890b610-c6b3-3d46-8e72-c92ef646c323 | -6.84045 | -43.35893 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f816229d-c845-3c51-a2f9-30675fc08d43 | -6.87093 | -42.78276 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f3b2fe39-2eb7-3bd4-99ef-da94fcf0d476 | -7.0903 | -43.4178 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fb3ecffd-22ea-3221-83f5-b00e0c6be804 | -7.71084 | -43.74001 | 2025-07-10 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 12d7c735-d178-32ad-a31c-889128221741 | -4.43783 | -47.97894 | 2025-07-10 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa842635-6903-32e5-82cb-a69bb869beb2 | -10.57739 | -49.13077 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cf321466-7d07-3580-8131-fc9d878af89c | -11.38018 | -48.05246 | 2025-07-10 04:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67994e3e-44f0-37e5-b44b-2c09ef89c69e | -7.20238 | -45.34899 | 2025-07-10 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62e26dad-cf01-3dc6-9c83-40a5fbea5695 | -11.13864 | -48.87645 | 2025-07-10 04:25:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd2809c3-c5c0-3ca7-9e07-120923c77e23 | -6.62413 | -56.27691 | 2025-07-10 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a559f469-1b07-3327-82e8-871e72d4d50b | -5.46044 | -44.81885 | 2025-07-10 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9f4d768-75ae-3ed6-b450-16636babbc22 | -5.35018 | -45.26902 | 2025-07-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2085410a-d14e-36cc-a6a0-a03f9f050f45 | -10.65299 | -49.46331 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39fe6baf-ac51-3ff8-bea7-1c0bde56b47c | -8.28042 | -46.3175 | 2025-07-10 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f300d69a-4e35-38a0-b44b-cbf8c76c5b36 | -7.23353 | -43.08146 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1e5ab06a-4592-3343-91cc-98bf20bf65db | -6.68496 | -43.10371 | 2025-07-10 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9af3dcd-b3ee-39ad-9fb3-ffc68a212d85 | -4.73954 | -50.93843 | 2025-07-10 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b3828e4-5bc4-3919-b354-d7e2c44e1863 | -6.99094 | -43.50573 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 623b3b77-b314-33cd-ba88-9d0535a4b4e7 | -4.81953 | -47.31979 | 2025-07-10 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1c0329d-cbb2-3f31-9793-52235c2d862f | -11.06074 | -45.86983 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e84a1a9a-de1b-3f97-ab61-3ea12f01536c | -8.50162 | -43.27488 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| e49a1452-97ad-380a-9322-63aa4eca7337 | -7.48334 | -43.93133 | 2025-07-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a417e02-36af-3c7d-b9f3-f679db6add1b | -8.49881 | -43.31272 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| a3cfb563-a21b-3c7d-84f0-2e8acab3b2cc | -2.75171 | -54.06488 | 2025-07-10 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 020ed58d-0915-32c2-800f-7d90e0fc4cd9 | -8.67521 | -44.29955 | 2025-07-10 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98ecb166-ed9b-398e-a351-e96128e06465 | -10.57437 | -49.1493 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b5063ea7-eb72-3fbc-839c-84c3f4db7b09 | -10.57558 | -49.14189 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 9159951d-8750-3953-8140-b594995256cd | -7.00656 | -44.4207 | 2025-07-10 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 825edf72-57e7-34dc-a5fe-485e9c0d3751 | -8.49831 | -43.29018 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 1310f029-4bc0-350f-b9ed-3622097a30f9 | -7.74148 | -49.86243 | 2025-07-10 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddbfd63a-5910-3af8-866f-ad3955bbc630 | -10.56817 | -49.14448 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| bdf02386-4579-39ee-bf47-cd9f6513a2cd | -11.08105 | -45.8729 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1509b04-2390-3000-8299-84ebf9ed7964 | -4.22496 | -47.20802 | 2025-07-10 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README17.md)
