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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be78b114-ca93-31d6-994e-600756987cda | -3.3588 | -51.2887 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67bd3b57-b603-3b70-bf2b-474781cc9f5f | -4.21917 | -48.34898 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f74f37-145f-3b72-ae3c-2e590835d8c0 | -3.06825 | -49.37492 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78a7ae92-8409-31f7-84a2-900136622611 | -2.61556 | -49.22915 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad24862d-b63d-318d-98eb-bf41f99be3b0 | -4.12293 | -47.28978 | 2025-11-09 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c2b7e116-251a-3dd9-b599-d05d015a595f | -3.45507 | -48.82133 | 2025-11-09 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01f65e15-52a3-3a97-8896-c6d248100b4e | -2.51081 | -49.46207 | 2025-11-09 04:38:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 580914d4-7efb-30c8-85f2-66c640bd9351 | -3.10295 | -50.20021 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8394e5f-ef1f-3e05-82e9-97601665157c | -5.0928 | -56.1605 | 2025-11-09 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dab9d030-caec-34c2-a128-eead4b0de863 | -4.4692 | -46.45241 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44a2873e-16e6-3a04-9080-2d4487f90155 | -3.86281 | -49.37949 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79e1598a-8da1-355a-93e8-1f62398b94d5 | -4.37628 | -45.49108 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d68016f9-cda1-3f88-9076-b15331cc7828 | -3.11891 | -50.14377 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91358080-5204-3fb3-8db2-0f8e51cf4a8f | -3.12228 | -50.1443 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81b37877-7953-3177-bce1-09d66f5900c8 | -3.43247 | -50.11637 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d683885f-b407-3576-b2a0-b6223ddf2c6b | -4.58861 | -49.38829 | 2025-11-09 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e51e469-d6ff-303d-b900-1ec22f486061 | -3.34662 | -53.22536 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f483a6f-bf7e-35cb-a935-7b798067d844 | -3.6135 | -50.15946 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f669c71d-3610-39e8-aea9-a0a2dee971b3 | -2.61611 | -49.22569 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1f50ba6-aed0-3c33-aff6-5b52ce59d1f7 | -4.6842 | -45.85044 | 2025-11-09 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29509e4a-76e0-3405-aa86-c7a2ecd4bb23 | -1.5925 | -54.30552 | 2025-11-09 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfc07d78-a3f5-3158-bfdc-b62c0cbe9a60 | -3.32728 | -44.37281 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cec25bf2-a6db-390e-8a26-f6cb55fd9098 | -5.73441 | -46.45717 | 2025-11-09 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01b1a433-bd40-381d-8cce-95318ee1f154 | -2.97666 | -48.70699 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2634776a-529e-3679-9a04-2269520d3f94 | -4.58401 | -45.62564 | 2025-11-09 04:38:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e4aaf279-60a0-3a99-99f5-7d12a99db9df | -6.18494 | -52.66665 | 2025-11-09 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a20ff685-d7a2-363c-bfb3-cc276de01bb6 | -3.24756 | -50.14953 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d88e9c7-8c4b-3435-9891-680c8c33c4f1 | -3.08235 | -45.36646 | 2025-11-09 04:38:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eae67254-2370-3553-bf5f-d5da677258e1 | -3.76585 | -44.28844 | 2025-11-09 04:38:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f23c8b48-a3dd-3ece-8196-c330f06fc801 | -3.95221 | -49.02995 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47985c16-21ef-3fa0-b7bf-3dffae7d56cb | -6.34458 | -46.76874 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25ec5aa4-0b3f-38ef-a6c7-0b206b6d84b8 | -4.48848 | -45.71178 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fc868ca-654a-3fe7-8d54-eccb823b2e68 | -5.37936 | -44.73143 | 2025-11-09 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47d98392-3efd-3a89-921e-88c81433f076 | -3.82804 | -50.15622 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a740e36-03f1-3239-8c30-4aefca63acea | -6.32034 | -46.20909 | 2025-11-09 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86a8ac38-15ee-373c-a31a-49f36f69a3c1 | -2.60561 | -49.22759 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a22d558e-4646-3fce-9737-14bad5d70471 | -3.34673 | -50.20907 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0896d4c5-6a67-327e-9e05-28679ba33c0b | -3.69072 | -51.38707 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1bc2efca-4b10-35e1-883d-8af6b56d2cdd | -3.31771 | -50.15304 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b61fcbf-8df3-3bea-a350-5f1791cc9d3f | -3.44056 | -52.63663 | 2025-11-09 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4670e6ab-838b-33a3-8663-0920a763e890 | -4.1834 | -49.77946 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53dbc307-be81-37bd-a3dc-481809ac3dee | -4.14758 | -46.26143 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 207f64af-15c2-3f56-811f-bab8b1a1afc5 | -3.45009 | -50.02801 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9a6366c-afbc-3f20-845b-123ffbc4576e | -3.77418 | -49.99861 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7517a241-8d72-34a7-b8c5-8b1546381702 | -2.5907 | -49.23589 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3dfb2ce4-8107-3889-881f-1b5acd7201fb | -3.01353 | -49.44108 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f9d7ca3-eeb3-3ecc-9212-b2c1b5bafc9b | -5.30829 | -47.28192 | 2025-11-09 04:38:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7494ac56-f7aa-3162-bee4-566fdc744656 | -4.6172 | -46.38196 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41d59109-ae69-3971-99e4-8132a2bd8beb | -3.09737 | -50.3215 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b9553132-81bb-315d-9027-ad7ba7084530 | -2.61003 | -49.22119 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebbf95e1-bd17-3af1-88f6-9b73efffe905 | -0.86215 | -47.31293 | 2025-11-09 04:38:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1626e71f-0a28-3bb8-8cca-fa13463afb24 | -4.3919 | -45.96958 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8aa2d4f2-7e6a-349c-b02e-d4f6a670c0d1 | -5.7751 | -49.83573 | 2025-11-09 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fbc201a5-3b08-38eb-8d0b-06c9666f5b75 | -3.7981 | -48.90729 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5233838-7777-3c88-865c-97fe71c99285 | -4.05254 | -46.43158 | 2025-11-09 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 805929aa-dea9-31bc-a4d1-39dc6088b8c8 | -5.36731 | -44.62159 | 2025-11-09 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c87dd8fe-8e39-3bc1-bada-06eec46abc3d | -4.80421 | -38.69635 | 2025-11-09 04:38:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b39c5ec1-ea9f-3bb4-9e8c-7289f63077ab | -4.77461 | -48.64164 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 803bf44d-0bc6-3cc0-b8e5-f76b1c126d17 | -4.17674 | -49.79989 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c799b0d4-cf82-3f49-a6f4-56eabec7e809 | -6.00011 | -57.83341 | 2025-11-09 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee5b4685-c66c-3eb6-863f-9d14c27cbbef | -3.0906 | -50.32043 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c74f726-b80b-3a6d-bd47-b0334c5bcb6d | -3.46776 | -50.32798 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e56fe146-e1cc-3ec2-8058-dfc76a3d554d | -4.00259 | -48.32192 | 2025-11-09 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09d22a0c-e1d1-39ac-a644-02c5541d470a | -4.01192 | -48.04609 | 2025-11-09 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06f7b577-0a33-3996-9b62-58ebe4c9e323 | -4.75524 | -47.52692 | 2025-11-09 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fb67b88-f177-300d-bf69-85f952f2e06f | -3.34393 | -50.20494 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a036762c-88e9-3dfc-a227-95ed7376f496 | -3.45575 | -49.84739 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 514d2a69-a6ae-385d-a1f5-ef74476c0484 | -3.3314 | -50.08928 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5bdbf314-0935-3754-858e-2721f890f4b0 | -7.54308 | -45.85588 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cf28127-8da8-33eb-9e20-d5167bb5cb60 | -5.19952 | -47.8404 | 2025-11-09 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d328b0b-9382-3825-a491-33a281b6af04 | -4.29095 | -50.66468 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b778b9a2-6e21-3484-bfaa-0c4c5a89366b | -3.49869 | -50.04658 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4249a43a-7e4c-31ab-a935-3c3a2afebe84 | -4.04905 | -46.43102 | 2025-11-09 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b01106fc-32e6-325b-aead-f1b691094484 | -4.4745 | -45.3413 | 2025-11-09 04:38:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f753f14-a250-3d45-beca-ed7734937472 | -3.57999 | -53.52218 | 2025-11-09 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c96bc65e-07fb-3d0f-b842-56fbbbfae38e | -2.10909 | -45.35219 | 2025-11-09 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2751c59-ad1c-3eaa-9f13-01ef49a6a724 | -5.0975 | -37.78921 | 2025-11-09 04:38:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2a64400b-9d25-383c-b292-010e58d55e87 | -4.88985 | -48.59954 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1532d867-6acd-3954-b4a4-47f1386f9faa | -6.34167 | -46.76431 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fd21550-28a8-3a79-845f-c492dde793ae | -3.3335 | -44.38359 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| d8e4190a-7bc1-33b4-953b-8d983f932aa8 | -4.88155 | -48.58764 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8bd4b36-9cd8-380c-9252-07594c0390eb | -3.67633 | -50.44933 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90f99929-da8b-3a58-b7d4-a9065bcdf849 | -4.80999 | -38.69728 | 2025-11-09 04:38:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 166f2a5a-b227-3d02-8b1a-8be9c9c20a66 | -3.79853 | -51.30364 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aeae6ecc-cf60-331b-bd46-6f18068748d6 | -3.27358 | -50.05113 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 250f17cf-e771-3c07-915c-79c782de4fcc | -3.58539 | -41.65786 | 2025-11-09 04:38:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a6e963f4-a7e4-333a-8860-42ddb3175fdd | -3.36239 | -49.51379 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4417717f-51fe-3ed8-825e-1e6efee079fb | -4.63932 | -46.40171 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab9e9a43-5817-3650-bfd2-2e0449e5ea9a | -4.51955 | -48.83773 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d78ce3d-a903-3a63-9623-f30e616dced5 | -3.64228 | -49.86987 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25d3be89-7e45-36fb-b91a-2b126f16628c | -2.2272 | -50.93457 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c60f160-7107-38ab-ad00-43ecd2bb2792 | -3.09519 | -49.26913 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 317cfc57-3bc2-3128-ade6-1a720049af6d | -3.75333 | -52.10695 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97c987a4-200a-3292-9d5f-48a4bf548e58 | -3.91315 | -50.04617 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eae6619a-34dc-3f97-9567-3077124c7698 | -2.73948 | -45.16705 | 2025-11-09 04:38:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ade67c0c-e32c-3aec-b11a-cca9889a118e | -3.26186 | -50.03831 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1df1956-1689-34b7-b3b2-2240a7b3c766 | -4.84321 | -42.37669 | 2025-11-09 04:38:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8dd365bf-acb1-3b43-865a-2c33fd689ca4 | -7.92381 | -47.62886 | 2025-11-09 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 527cbd23-af31-3cbc-aef8-226e8dc0c394 | -3.80249 | -48.90094 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b66b4a4-0751-343d-8c46-67db66739158 | -3.40375 | -50.27348 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README27.md)
