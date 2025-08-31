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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c40fccb-6757-39bf-97b3-34b5d52f0ba3 | -8.74798 | -62.38861 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d569246-39c0-3811-bf39-f3782e1e81b2 | -8.92143 | -62.42693 | 2025-08-31 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae0ce871-9c3b-3ffb-81be-b51b7e8447ef | -9.45354 | -62.33173 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed840ee1-7d01-3f4a-8394-8c57c7b1d338 | -8.6816 | -62.42046 | 2025-08-31 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4766798b-6a47-368d-b474-7680b315f9d6 | -9.45304 | -62.33558 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c72b5ff9-cc28-3d7b-a4e3-c149742db675 | -11.31765 | -63.27007 | 2025-08-31 06:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7b95217d-ee07-3f3d-a508-dc54810a394f | -8.44606 | -70.14067 | 2025-08-31 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd42d090-7ab3-33eb-839d-a06b8954bd52 | -9.45918 | -62.3324 | 2025-08-31 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35057c35-33a4-30e4-b89b-3fb5cd5cc862 | -7.91876 | -63.009 | 2025-08-31 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e1cef853-a379-380f-ab8e-12538bdc58a2 | -9.44523 | -60.56885 | 2025-08-31 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de4584e4-42ac-34bc-b870-3115f6c01df9 | -14.79801 | -59.72582 | 2025-08-31 06:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0fc265d7-b663-3816-9736-92cd33d01398 | -14.79079 | -59.72678 | 2025-08-31 06:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74ae337c-955c-3d83-b6c5-bfab19fa8ce2 | -14.79328 | -59.72472 | 2025-08-31 06:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8385fe81-5bde-391a-8317-447e7b3f7b5a | -14.79853 | -59.72053 | 2025-08-31 06:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fb1f82e-819f-39a4-969f-9ef74b5376b8 | -14.80054 | -59.72351 | 2025-08-31 06:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26d21fa5-bffd-311f-bd87-6e825f3ba35a | -14.80581 | -59.71896 | 2025-08-31 06:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b0d5535-1f50-34cc-8f18-18de5a573be4 | -14.79276 | -59.72973 | 2025-08-31 06:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 215b0fe0-c908-3efc-a2cd-aa28e118127b | -11.4233 | -63.2444 | 2025-08-31 06:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| f97ef246-82c5-38f7-95f2-3ffe94fd5b5d | -15.7303 | -48.9223 | 2025-08-31 06:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 64611e2c-6d58-3244-ab08-e3e8e047a238 | -15.7098 | -48.9702 | 2025-08-31 06:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 85508357-3dae-3a47-bfb1-df1dea4b1c28 | -15.7107 | -48.9255 | 2025-08-31 06:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| b521a8c7-e4cb-3810-9181-7fa3ecd96331 | -9.4432 | -60.5692 | 2025-08-31 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 5ec07605-1bfc-35ed-b190-7facf24e30b7 | -15.7102 | -48.9479 | 2025-08-31 06:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 0447a436-31b9-3a16-93c6-f61d69a45d36 | -9.4683 | -62.3476 | 2025-08-31 06:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f94fe0bc-b4fa-3724-bb59-b68aba5397d7 | -15.7298 | -48.9446 | 2025-08-31 06:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 65e30565-cbd7-3ac7-8309-fbc31a8cd757 | -7.9265 | -63.0158 | 2025-08-31 06:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 3e786689-714a-3bfe-82a9-52e11848cf4e | -11.8181 | -46.4314 | 2025-08-31 06:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 136d5690-41fe-34ce-915f-fe9497ccc9e6 | -15.7294 | -48.9669 | 2025-08-31 06:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 30e80a3d-32bd-3a35-87e9-2bc07da90409 | -16.2225 | -52.6565 | 2025-08-31 06:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| f60b7e6b-66ef-3b62-bffe-5a63405aa142 | -9.4497 | -62.3485 | 2025-08-31 06:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 84eb2541-bc54-3f63-a7b4-4cd7a5849554 | -11.4045 | -63.2453 | 2025-08-31 06:20:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e2c3a710-fbc6-3e3c-b0b6-f01df9f4e84c | -6.1853 | -43.3257 | 2025-08-31 06:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 17540325-0af6-3dc8-80b6-f931893d02aa | -6.1665 | -43.3273 | 2025-08-31 06:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 330303a5-9984-381e-8f2e-cbff5aeee2e1 | -9.4683 | -62.3476 | 2025-08-31 06:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4f5d834f-7b3b-3d00-b334-e955dc900214 | -15.7098 | -48.9702 | 2025-08-31 06:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 3f15e15c-ac22-3b96-812f-6058d8bc64c3 | -15.7102 | -48.9479 | 2025-08-31 06:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 19fd0ca4-f9f1-339b-8baa-3dcafa099d95 | -6.1667 | -43.3039 | 2025-08-31 06:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 5a4615d8-6cbf-31cc-9fa2-19671b7c57e8 | -9.4497 | -62.3485 | 2025-08-31 06:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 9818abc9-d263-3e89-830a-b111ee012a5e | -15.7294 | -48.9669 | 2025-08-31 06:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b61f1274-9c8a-31d9-bc8f-796bcd18fef2 | -9.4432 | -60.5692 | 2025-08-31 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 852ef075-cd95-3a00-a8fa-44be394a3a8b | -15.7298 | -48.9446 | 2025-08-31 06:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 6dfe02d4-487e-344a-aad9-1ebfe0de08f5 | -7.9265 | -63.0158 | 2025-08-31 06:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5f7c982b-ec02-3788-88f7-29d641aea3f3 | -9.57057 | -66.69041 | 2025-08-31 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 156daf20-a55b-3a6d-9bd8-5ea029d9fa88 | -8.38933 | -70.82925 | 2025-08-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79ac487f-01de-3016-bdc6-69ca7ca761b8 | -6.91556 | -71.75152 | 2025-08-31 06:31:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a380bb6f-1854-37c8-a076-43ef7ff7c5ad | -8.39415 | -70.82996 | 2025-08-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a0259b4-0b04-3797-8149-b06c8d689f2c | -8.23534 | -72.81365 | 2025-08-31 06:31:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 619538ce-d398-3611-91bb-6f238039072c | -9.2819 | -67.64504 | 2025-08-31 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3c3a1bc-d78f-3895-bf2b-3c7829e177ba | -7.66702 | -73.2989 | 2025-08-31 06:31:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8016c4a5-c9ec-3a9d-80a0-81de929865d1 | -8.2359 | -72.80976 | 2025-08-31 06:31:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a75bafa1-8acb-3218-9b0b-1a44678e816d | -9.27798 | -67.643 | 2025-08-31 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b69099d5-64de-3285-86cc-0ad5d84793a5 | -7.20539 | -69.8983 | 2025-08-31 06:31:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d880846-4869-37e5-b82d-b1b8abbc0afc | -7.46358 | -70.13853 | 2025-08-31 06:31:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ea108ca-0bcb-3e69-9935-5c5abf08a896 | -8.38377 | -70.83393 | 2025-08-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67756815-9a20-34f1-9d9f-9af9f91b1dbe | -7.66596 | -73.29848 | 2025-08-31 06:31:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 023e5d31-e930-36d8-b99d-59f9691e0221 | -8.38843 | -70.76416 | 2025-08-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fe17900-49fe-3286-a4a9-f55cb802a733 | -8.69323 | -71.60285 | 2025-08-31 06:31:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc5915c0-88ef-39cd-ad57-8c73fcd549f2 | -6.9162 | -71.74721 | 2025-08-31 06:31:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6d8b987-a144-3f25-a28e-a6fea1ad0e22 | -7.67149 | -73.00817 | 2025-08-31 06:31:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbb64a09-dc14-3664-82b4-42a8004ca2c8 | -7.46242 | -70.14232 | 2025-08-31 06:31:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ab3a182-5d9a-3b96-99dc-b0a5b8327a99 | -7.7338 | -71.99141 | 2025-08-31 06:31:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb0f2f35-d915-3e11-87a5-a0b40cf0f141 | -9.27528 | -67.6487 | 2025-08-31 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a69a0f20-f760-3f68-9922-a34c360a009a | -7.97899 | -71.39549 | 2025-08-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9ead1bf-de6c-3c2e-bccf-da2d2d3b6b72 | -8.23114 | -72.81301 | 2025-08-31 06:31:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7caade6b-10e8-37bd-91c1-0a8a998b006f | -7.46323 | -70.13662 | 2025-08-31 06:31:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6bd81863-ce51-318f-9991-753a65d1e2a6 | -7.82996 | -71.94624 | 2025-08-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fad132f-662c-351f-bf85-740c224c31a5 | -8.65953 | -70.03893 | 2025-08-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2a52051-713a-3584-aec9-c2115af1a19e | -8.66384 | -70.0457 | 2025-08-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7db7f499-b803-3e25-8180-f9e1d2b5496d | -9.95719 | -66.87871 | 2025-08-31 06:31:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 347a4d24-e538-35b9-87d6-21584690ff23 | -9.27587 | -67.6442 | 2025-08-31 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 960575e8-125d-35e2-9f31-d915e173327e | -7.46405 | -70.13086 | 2025-08-31 06:31:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e470603d-fec2-31e2-bff7-c427d45fd1d1 | -9.26926 | -67.64787 | 2025-08-31 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7010b487-212f-36a9-a6e7-77b01820a864 | -6.91584 | -71.74418 | 2025-08-31 06:31:00 | NOAA-20 | ATALAIA DO NORTE | AMAZONAS | Brasil | 1300201 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57af08b4-e95d-3e07-b5f2-4ac92888e9e1 | -9.26984 | -67.64337 | 2025-08-31 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e654460f-8b4b-367a-9452-6c5eaa4b8b75 | -9.06266 | -71.25813 | 2025-08-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edda1733-45cc-3d62-8716-7199a743ef7c | -6.91524 | -71.7485 | 2025-08-31 06:31:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5bd972e-d708-323e-b17b-6eb9f3e53044 | -8.65914 | -70.04193 | 2025-08-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b8e877e-d023-32e0-8699-988c95dd6f11 | -8.97745 | -70.74385 | 2025-08-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c399332c-d3d6-32d1-a906-7e035d43d5d3 | -7.45936 | -70.13216 | 2025-08-31 06:31:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce147da8-84c0-3fbc-84e7-eb162ef92d99 | -9.95079 | -66.87801 | 2025-08-31 06:31:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 245b192f-e952-32c3-9dce-d42ae0bff430 | -9.56415 | -66.68952 | 2025-08-31 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b763d68-be6a-34ec-b31f-cab02742cf23 | -7.46436 | -70.13278 | 2025-08-31 06:31:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f5c05d1-23cb-3368-8b3b-9367ba1f25db | -9.27743 | -67.6475 | 2025-08-31 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c23f8546-65c0-3fe0-83db-6bd2d569d8b8 | -8.85166 | -70.62326 | 2025-08-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f16733f6-eb22-3e82-a758-585d4842daa5 | -7.8313 | -71.99937 | 2025-08-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 496e879f-9523-3319-97d0-eacfec663b45 | -9.28131 | -67.64954 | 2025-08-31 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca15b648-754f-31d6-8741-d7a0a252c0f0 | -8.66155 | -70.04147 | 2025-08-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb07577a-a920-3b41-87c1-5c3a139f4296 | -6.92866 | -71.78137 | 2025-08-31 06:31:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97a5c93c-9edb-30e5-82fd-685fe04dd7c7 | -8.66424 | -70.04269 | 2025-08-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a0c4a3b-8481-3b0a-afd5-5c3f3636e79a | -7.20498 | -69.90128 | 2025-08-31 06:31:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b274b9fa-f4a8-3d76-8c69-eca71d54f1e8 | -9.28345 | -67.64837 | 2025-08-31 06:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6192e0ea-4048-3763-9505-717c37468e48 | -8.86928 | -71.27788 | 2025-08-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74c30414-f6ab-3aa6-bf71-81ac65b8071d | -8.66114 | -70.04446 | 2025-08-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b4c3805-c3f1-31d6-aaec-0a21182ae83e | -8.73329 | -62.38287 | 2025-08-31 06:33:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b384102b-015f-31d9-aaef-7aabcf978c17 | -6.70751 | -51.41069 | 2025-08-31 06:33:00 | AQUA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| c1168044-4e15-34cb-a612-8cb9b9e3b215 | -7.91649 | -63.01583 | 2025-08-31 06:33:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| bc7d35c5-7758-387d-9d74-73c7b84e42b7 | -7.92265 | -63.00301 | 2025-08-31 06:33:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f7b14d35-ce07-36ec-a445-7054a4a835b3 | -8.88158 | -62.38686 | 2025-08-31 06:33:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ef4646ea-c390-393b-b47d-f123e41914fa | -10.03058 | -48.08879 | 2025-08-31 06:33:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| d0899546-b837-356e-be33-bde562ac3fc4 | -8.67246 | -62.41551 | 2025-08-31 06:33:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.5 |


[Clique aqui para ver as próximas entradas](README83.md)
