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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b0d7979-ec9f-351e-948a-6d0622f5e735 | -14.65356 | -45.08825 | 2025-05-27 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71e7cb80-97f3-36cd-ada0-f18b74ffe203 | -14.03179 | -55.13174 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9058b33b-1033-381d-a6da-f4cc574e2d18 | -14.62912 | -47.94098 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 266fc0a3-78f9-3af3-869b-13e4f940aade | -13.09992 | -52.29017 | 2025-05-27 04:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b16cbc7a-e4ad-3125-9cf0-e2ff814ebdb5 | -12.65787 | -52.43045 | 2025-05-27 04:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e7e6fae-f240-3206-a526-bc90d103a45b | -12.16953 | -54.2645 | 2025-05-27 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cdb914f6-a3e0-340e-9bfb-7440dc5e50cb | -16.59038 | -45.87999 | 2025-05-27 04:29:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf5ae0c7-9b74-3788-981b-3cd110e05b97 | -17.26767 | -49.00584 | 2025-05-27 04:29:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e77623f-1665-3dd1-b3d0-bf2c0c502008 | -12.0349 | -51.59914 | 2025-05-27 04:29:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f74bd39e-23b2-3d59-a204-5faf2f910af1 | -15.56935 | -47.85522 | 2025-05-27 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64cd228e-d35a-3f14-80cb-2349a52ef506 | -10.29195 | -57.1426 | 2025-05-27 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25b0249f-9201-34ce-bdaf-705df611e30e | -14.03 | -55.14116 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f81f3f11-be88-37b5-a460-67f91e5a1884 | -11.40159 | -52.94916 | 2025-05-27 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3220202f-9b74-3e6d-8208-2471b8433b70 | -12.65826 | -52.43385 | 2025-05-27 04:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74ded239-f160-31fe-85e9-44b9f1342e55 | -14.1514 | -45.47887 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c6c5b141-caf8-32e1-ad1f-e93327525fd5 | -11.13959 | -53.92927 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1428b91a-caa2-32c0-b580-a22d65d1f659 | -10.83115 | -56.96204 | 2025-05-27 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed4694ab-13ee-3ca7-b816-ad450451f25b | -10.29755 | -57.14348 | 2025-05-27 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7b8cc49-ac8b-39df-a955-6892cec79307 | -12.42455 | -49.97883 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04c1d21a-9cd7-3468-b011-28a01209227e | -14.59387 | -48.35991 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fba34e22-b780-367f-90b1-8c523671103c | -14.0181 | -55.1291 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fa946ee-eb1e-3376-877b-04b795055ccc | -10.82203 | -54.01815 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8514b28-9b77-3d1b-a717-072aeb43da9e | -14.14433 | -45.47778 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03472657-cdb2-31cd-b3a9-699a521b92e2 | -10.83467 | -54.0252 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5562b2c-567e-3781-bfad-185b50988a58 | -14.04454 | -55.13939 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bf81003-3e86-3818-8b8f-7f5a9011965a | -14.63245 | -47.94153 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf38bd8e-633e-38e5-a04f-bbfbf4658b79 | -14.03269 | -55.12706 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd68588e-28cc-3707-a275-afe5215cc8b2 | -12.03568 | -51.59451 | 2025-05-27 04:29:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fb8172b-81ae-3f4b-9249-563a98e4094d | -13.7875 | -54.31746 | 2025-05-27 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f95de056-5668-3418-9c08-37f988437215 | -14.69738 | -48.10965 | 2025-05-27 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1be82716-6c23-305f-abef-609cfc79ca36 | -10.83996 | -54.02147 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e503f5b-e7e4-3ccb-a509-816be7cc3e31 | -14.03724 | -55.12797 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ea75b70-c874-3349-b973-a4bf9c8a12a1 | -12.65697 | -52.43546 | 2025-05-27 04:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa5b9c2e-8496-3c72-b2a1-e2ae7824d7cf | -14.66441 | -45.08991 | 2025-05-27 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f41e6a24-dbe6-3dc6-b353-87d7b4610ad1 | -12.35167 | -49.92227 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 342fa4e1-5dd5-3797-ab28-afbf2c38291e | -11.6237 | -54.93613 | 2025-05-27 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dbe89562-3d36-39fa-b904-cf315d64c3d4 | -10.83834 | -54.03064 | 2025-05-27 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7ecb190-1fb0-367a-83cf-69971a1334f5 | -10.83183 | -56.95847 | 2025-05-27 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 916d57fd-df62-3c5d-9db7-608600a60e4f | -14.02544 | -55.14026 | 2025-05-27 04:29:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9be4c339-d5c0-3eb8-8a58-1025342c57bc | -12.40303 | -49.97908 | 2025-05-27 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ba17825-5fe5-3eba-9354-5147a78248ab | -12.75691 | -48.34206 | 2025-05-27 04:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e415e0ab-1e50-3156-b2cb-1f46da5905b2 | -14.23961 | -45.66363 | 2025-05-27 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b08a7e2e-a936-3c57-99c5-4e5f1dff8852 | -15.88943 | -43.45827 | 2025-05-27 04:29:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 56394469-1509-31c6-9a12-171072aaaae3 | -18.8479 | -53.6251 | 2025-05-27 04:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 81.7 |
| beb34726-d491-3dbc-bc87-a3f13ac11866 | -18.8679 | -53.6218 | 2025-05-27 04:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 512bd160-3fde-38c2-be96-d8194ce22e1c | -18.8484 | -53.6035 | 2025-05-27 04:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 80.2 |
| dc1184e7-af28-372c-8698-8ecef0fb5b70 | -18.84948 | -53.61729 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9a6ff83e-d863-3761-8ab6-4c1666d6d9c3 | -18.84471 | -53.6216 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee2d15c6-a8a4-3ef4-92f6-c26357608780 | -18.8415 | -53.60753 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 219076db-7c96-31e9-a112-b479b1a08796 | -18.84088 | -53.62088 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86a75372-11ff-344a-bad8-ebd42b9f475e | -18.8388 | -53.62263 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a8c1140-2299-35e9-9fea-7854e760a10e | -18.84622 | -53.60326 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28721a83-1499-391b-bb76-1b5a6f8bd390 | -18.8397 | -53.61758 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b1b22f8a-f974-3815-96c5-5f4c6da8dfc0 | -18.85322 | -53.6307 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca1eafa3-68ba-3e2d-8596-1a77d53c5890 | -18.85006 | -53.60396 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 021ffcdc-5f9d-32ed-9678-b8fb4cbca8ad | -18.83994 | -53.62592 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 136ae73f-4417-3d9e-b351-0d285b2827f2 | -18.83384 | -53.60604 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa2c6315-e579-3a85-93b0-83c31cfec614 | -23.33789 | -46.77398 | 2025-05-27 04:32:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3872e02f-ede9-3608-961f-55f13df6728b | -19.05344 | -53.46308 | 2025-05-27 04:32:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b86c890-1429-37b9-b6d8-a0bab914e70c | -24.29773 | -49.93959 | 2025-05-27 04:32:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bba3b702-bd26-30b4-b0c5-861c1b242543 | -18.84377 | -53.62665 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af7ca98d-3c7d-3785-a4a1-211d857a1499 | -23.60599 | -49.00578 | 2025-05-27 04:32:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f248f48f-e9b9-33f5-a22e-6628237169fe | -18.84239 | -53.60252 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 841b364b-b812-3410-b01b-03e1e5cef03d | -18.83587 | -53.61685 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f9235830-d1c0-399f-a807-315fe92ccfaa | -22.78597 | -43.75846 | 2025-05-27 04:32:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7beafd17-5eb1-3d89-91dc-4c759a4ed361 | -23.60644 | -54.7674 | 2025-05-27 04:32:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f0b98788-fc86-3bc2-b5da-5e059daffc2e | -18.85503 | -53.62053 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 24.7 |
| b615bdec-236c-337e-b8d6-9f579b5358b5 | -18.84557 | -53.62916 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92145083-2f5b-3320-9058-0258c3ddd961 | -18.84264 | -53.62336 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60dfb6f9-21b4-33b2-9f35-25db82ef4c07 | -18.86003 | -53.62458 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 354be71c-c52c-38f3-867a-867fb313c602 | -22.51825 | -47.72423 | 2025-05-27 04:32:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae864a2e-5d20-375e-8acf-20974fa4ca7b | -23.42853 | -46.75729 | 2025-05-27 04:32:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0750864b-eb17-3e7f-bca3-3ace83a70bc2 | -18.84173 | -53.62841 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b84a30c-f1e7-3341-bbf8-5ce2b587257d | -18.83294 | -53.61106 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 655d65db-a638-375d-9b2d-f811139e0518 | -18.41187 | -55.57712 | 2025-05-27 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8a50abde-d7e5-3a30-af45-d51277c290ca | -22.0397 | -56.81432 | 2025-05-27 04:32:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82c4495d-57fa-3272-8f08-e76753e9a77c | -18.8512 | -53.61977 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 24.7 |
| b0b5e259-d599-35bb-9762-b9c13a102060 | -17.53202 | -52.11862 | 2025-05-27 04:32:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8edb784a-5c1b-3f1e-98e4-4b4932e9c3a6 | -18.84354 | -53.6183 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 5f907b0a-1ccb-3174-ac6c-ef4f25e26972 | -18.84854 | -53.62234 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b9337fd3-4ce8-31f3-b53f-1ba00d1ccbd8 | -23.42406 | -50.19426 | 2025-05-27 04:32:00 | NPP-375D | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e6351208-941c-3a29-a5b1-84bb22601883 | -18.84939 | -53.62994 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7d2bc76-7b45-3078-9b5c-a9c3672f4f8e | -23.59922 | -49.00457 | 2025-05-27 04:32:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 083e630d-f4ca-3ab3-bacc-f485bc3dcd1d | -18.85143 | -53.62818 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6fc1fa1d-572d-3df4-8073-1fdb7e4ca35e | -19.17372 | -57.54222 | 2025-05-27 04:32:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 574378d3-4b24-3d93-a2e1-7ee6012cfac3 | -18.85412 | -53.62563 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5eb3e15f-9c01-337d-9efe-787b62345355 | -17.53126 | -52.12299 | 2025-05-27 04:32:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f014a69a-0c63-37dd-b9ca-6891b387e063 | -18.84329 | -53.59752 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c0404862-5b70-34b1-b707-e3021f34cdd0 | -17.83938 | -50.80996 | 2025-05-27 04:32:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c80dc556-c117-3b8d-9546-15354b8bd842 | -21.26534 | -48.61489 | 2025-05-27 04:32:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 162dc53b-eb2d-31f7-aa76-57a0cd54924d | -19.43708 | -54.77785 | 2025-05-27 04:32:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfe496d7-a9e8-30c2-b1d1-14d9e9a568e9 | -17.53487 | -52.12366 | 2025-05-27 04:32:00 | NPP-375D | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffff1c4e-5e06-3ad0-b6a2-a859985e60a1 | -18.8521 | -53.6147 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 24.7 |
| ecf71237-2bd2-3dec-8ec6-76f456772c59 | -18.86096 | -53.61951 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cfa9a365-2f90-329b-a822-1114178690e1 | -18.41102 | -55.58147 | 2025-05-27 04:32:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ea0e57d7-5f51-3d0b-a1ab-b8b4289616ca | -21.13863 | -43.95808 | 2025-05-27 04:32:00 | NPP-375D | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 70e3f520-3d5d-339b-b7b8-f2f4e7d57bac | -18.83564 | -53.59602 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 774bbca4-5224-3f2f-8919-9aca7aa82024 | -20.47687 | -53.6753 | 2025-05-27 04:32:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a77be1de-1f82-3b6d-93dc-747f4435968b | -18.853 | -53.60966 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 826f9882-0190-3fd6-a593-93179b4c7da7 | -18.84842 | -53.60156 | 2025-05-27 04:32:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README13.md)
