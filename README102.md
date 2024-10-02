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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f50870b-3046-3f42-98aa-ed1dbaafdc89 | -12.32624 | -54.10196 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4c07dec-54f1-3789-bfd4-57ae4026deff | -12.32563 | -54.10568 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bfe21ed-25f4-3471-8600-4800583f6324 | -12.32406 | -54.09396 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a55d8b4-fae2-3c6e-8585-1b0865e7d28f | -12.32346 | -54.09767 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53fd7c5c-4ade-3c95-8a6b-a8cddb26dc2f | -12.32224 | -54.10511 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 210f9dc0-ad46-3843-b2b3-885b33f61159 | -12.32007 | -54.09711 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17228e1c-2aa4-3107-a376-779e4b656191 | -12.26951 | -53.9938 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bca9283d-94f7-3c11-91b9-34422c528080 | -12.26831 | -54.0012 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 273f9d93-6d7f-3676-a8a1-0438cd63289b | -12.26612 | -53.99325 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0bbcd38-1508-3abf-bd03-3eb182fab01c | -12.26553 | -53.99694 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1ff4f45d-7182-3975-ba27-419eebd302d1 | -12.26493 | -54.00065 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 48850054-9d1a-3d68-8721-656612b6aee9 | -12.26433 | -54.00434 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a6b8baf8-4226-355f-90b0-122dde17bbda | -12.26155 | -54.0001 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ad1bb0e-a729-377c-9247-d2f8f99543e0 | -12.26095 | -54.0038 | 2024-10-02 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7b925f01-1105-39b0-8f91-aeab481b9ae5 | -16.11424 | -53.53872 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a49f902d-ae93-3686-a46c-d33771871523 | -16.11206 | -53.53102 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc80ffce-36ca-387a-ab45-b5f5c74b50c3 | -16.1115 | -53.53458 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1a51bab-b793-3518-9848-fbb3c4d1d95e | -16.11094 | -53.53816 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 190e9883-c372-37ef-a398-5d193fbaadce | -16.11084 | -53.56019 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9eec09a-863b-3500-a57e-3adb85091df6 | -16.10933 | -53.52687 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29c8c844-dd17-3e19-86ca-089c4f87efe0 | -16.10876 | -53.53045 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9eca9e39-c1dd-385c-b2af-2a67b28b3b49 | -16.1081 | -53.55605 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b686d6d-24b6-3d2b-9f1d-5a24141175f0 | -16.10753 | -53.55963 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ff6d50d-782c-37f2-b36c-b093cabcf729 | -16.10603 | -53.5263 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9d0a633-a04b-3296-a017-e3007facd41b | -16.10546 | -53.52988 | 2024-10-02 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49ca0191-118c-3590-828b-98ab5cfa1d17 | -15.77454 | -54.19345 | 2024-10-02 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4fcbae14-4fdb-3e26-b27b-805fb696f50c | -15.77395 | -54.19708 | 2024-10-02 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 417eee42-f796-3348-96db-48f0bbb662f8 | -12.32842 | -54.10997 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2276e763-2dde-3953-848c-10e65acc7189 | -11.64259 | -54.52187 | 2024-10-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d400f3c9-cfa1-378c-bbca-d66ec6aa26a2 | -11.43515 | -54.30582 | 2024-10-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34e7e4da-fef8-3eba-9b00-926f38aedcf9 | -11.43452 | -54.30965 | 2024-10-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f391b4c8-1399-3d76-8e0e-519d29023c07 | -11.43171 | -54.30525 | 2024-10-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97478225-2030-3169-9789-bccf1273685c | -11.43109 | -54.30908 | 2024-10-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c65aa4b-c9b1-34c1-82ae-09e48fdb787c | -11.42828 | -54.30469 | 2024-10-02 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc09ae97-1767-32d4-9f21-773cd85de0da | -11.41984 | -55.06068 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51d4e594-279a-3629-b923-7987584f818e | -11.41916 | -55.06477 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e539948f-1ba4-31c7-be48-fd912df649c0 | -11.38545 | -55.11378 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68402916-0788-38a1-b5a8-0a8299c7d213 | -11.38476 | -55.11787 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a2a8d10-b8dd-3969-9e95-1e9396d4f6bd | -11.3819 | -55.11317 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 570163fb-7692-3baf-8990-2d3f0f236337 | -11.38121 | -55.11726 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c6b5411-b204-3c47-907e-16932f32290e | -11.38053 | -55.12136 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcef9661-37ed-3950-9449-25039879dc86 | -11.37766 | -55.11664 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cb8eea5-0df1-373d-8afc-2e0547d6fecf | -11.37697 | -55.12074 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a197f1b-d9f3-36b9-9503-db203e418a3d | -11.37628 | -55.12486 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aec5c9e-e0e3-37cb-a956-5471a72c573e | -11.37273 | -55.12423 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dbfa1be-8da4-31b9-b3f2-e54bf9b6985a | -11.36876 | -55.19162 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b2478be-6938-35d2-8b26-cddecff30dbe | -11.3652 | -55.19098 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbe223d1-db97-31f7-9235-9deda3244a08 | -11.36451 | -55.1951 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee1bc4fc-e739-35bb-b6cb-39774c5e6b69 | -11.36094 | -55.19446 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f46fdd9d-28b0-379d-95d1-969b3eb50ab8 | -11.36025 | -55.19859 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f48572b9-a7ca-3589-927f-187c28573a2e | -11.35668 | -55.19796 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 22eeed2e-c571-3786-b90e-6b945d225599 | -11.32173 | -55.20905 | 2024-10-02 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6a2a920-7ee2-3e2e-9014-fdac949c74a8 | -11.30047 | -54.31143 | 2024-10-02 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 366dded5-ea54-3e31-bc45-3e9a50031a51 | -11.23711 | -54.18393 | 2024-10-02 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79905b8d-5e20-348d-9333-5c2643ada2c5 | -11.23369 | -54.18335 | 2024-10-02 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c30029f-a352-3d2b-ba9d-5152e449ea18 | -12.65975 | -54.66204 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc9b8a85-4322-369f-a057-3f08dd508fe3 | -12.65912 | -54.66588 | 2024-10-02 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c2638d2-4edf-36bf-9358-a62c1c93d6af | -14.9569 | -54.93451 | 2024-10-02 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df3d956b-96f0-33eb-8f68-b4458b541d32 | -14.95646 | -54.93516 | 2024-10-02 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 821961a8-0a83-3e33-aa47-b4efa63b5071 | -14.95625 | -54.93835 | 2024-10-02 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3691bf3c-6a3c-33e8-90f3-9844c6135d0f | -14.95584 | -54.93899 | 2024-10-02 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63757db8-0ffd-3fe0-9d02-462b142485d8 | -15.12449 | -55.83072 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49a2e48f-f007-3091-860c-6fc5aceafb0c | -15.12378 | -55.83496 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5274dfda-dac4-3157-a1d1-a9ebbf496446 | -16.53137 | -56.02709 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 997ad89e-d3a2-3c9b-97b0-3f0585dd3065 | -16.52788 | -56.04739 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c0c582e3-abdd-3f1b-b381-56543f9c120d | -16.14286 | -55.41581 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e192eddb-8a3a-3473-ba4a-3dde2cd92593 | -16.1422 | -55.41978 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1d3dc92-6059-3cfa-a5f5-086af999489f | -16.13939 | -55.41543 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8fff7b91-63ba-3619-9fb7-d86d45fa462e | -16.13873 | -55.41939 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0cbae1c2-ce97-37e5-866c-a4e90f8c1205 | -16.13593 | -55.41499 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 328606ac-0157-3fff-adde-6e7c5713afaf | -16.13527 | -55.41891 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7976008e-ea79-3f96-ad3b-8a2045757a57 | -16.13462 | -55.42279 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a2bcacbd-6e81-357c-86f4-91de93e8af60 | -16.13248 | -55.41447 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dce8572c-5d2b-3965-a097-23bd860d005c | -16.13182 | -55.41839 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5b1d12df-188b-3d39-8cb2-44d8548f9dce | -16.12903 | -55.41394 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e14c440e-7526-33ed-9032-981ad17c2a8b | -16.12838 | -55.41786 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49929aed-1470-3a7f-bef8-cc8df8ff419e | -15.90239 | -55.40154 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee725579-143c-3af9-bd7c-f740930a3b77 | -15.89897 | -55.40084 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a08cb1f-51d8-32ee-82fc-7922c2256f3b | -15.50154 | -56.11651 | 2024-10-02 04:49:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1cb5e33f-4ce3-37f6-999b-791f5797111c | -15.89555 | -55.40015 | 2024-10-02 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e500d71-e609-3475-a328-e339c42415a1 | -15.505 | -55.75358 | 2024-10-02 04:49:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fd1a3b5-3e4b-3f8b-82ed-b3eace1c105a | -15.50431 | -55.75763 | 2024-10-02 04:49:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e31077f3-e692-3045-a82d-f231dcce4375 | -15.38466 | -55.84064 | 2024-10-02 04:49:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2cd4a11f-6da5-3987-8b66-0e98c1e999fb | -15.38115 | -55.84 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 495dd4e0-6def-3e5f-b01f-cf33bbf62934 | -15.38043 | -55.84418 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be09fd83-af8d-3489-88f4-035c18acb81b | -15.37834 | -55.83522 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f04c38f-2df3-34ac-bb96-185a3a45e193 | -15.3762 | -55.84772 | 2024-10-02 04:49:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5c148fca-36aa-37f5-bbfd-b33d33cc29b0 | -15.37554 | -55.83044 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 558729e0-aa16-3504-b724-730a90d5567c | -15.37483 | -55.83457 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3ebd3596-caf4-345b-855f-1dcded4745cb | -15.37268 | -55.84711 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3753228-6dee-3323-9233-087eb0502e34 | -15.36915 | -55.84657 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dadd2ea1-3422-37d5-8323-72b24aef8ae0 | -15.36777 | -55.83353 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a1cd12b-47dc-31ba-baec-8cf6ef7c56ec | -15.13746 | -55.84054 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| df9246bf-8918-3ef5-a900-1f62ded92d5b | -15.13464 | -55.83581 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4caa10e-c773-3162-ba32-199a4aa29232 | -15.13224 | -55.82777 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 638658f8-bcf0-3196-b054-09d938dbcb1f | -15.13083 | -55.83623 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ea5d103e-432e-37f9-bf23-c2ddefc0c782 | -15.12872 | -55.82712 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a53c49fc-24a7-384f-b82b-baeafd734b2b | -15.12802 | -55.83133 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3509db7e-a87f-3976-b9c8-9c61f44ec49e | -15.1273 | -55.83559 | 2024-10-02 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89797551-f1fd-345e-8764-331d8c78e870 | -16.58983 | -55.93771 | 2024-10-02 04:49:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |


[Clique aqui para ver as próximas entradas](README103.md)
