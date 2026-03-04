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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d44e6fc9-d550-3654-b071-be25baad3e44 | 0.2825 | -60.6203 | 2026-03-04 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e3e57fa6-3b7b-3f03-a13e-f49411ea3fbe | 1.5047 | -59.9116 | 2026-03-04 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 113.3 |
| b86b94ab-ba8a-306e-a7ec-bb1038b15fd5 | 0.2643 | -60.6203 | 2026-03-04 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3ee5ce64-8ab4-3f77-9050-ef05a695d3ae | 0.2825 | -60.6203 | 2026-03-04 01:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 4b8dbd08-d2bf-3d9d-aae3-7428ec05ddc8 | 1.5229 | -59.9114 | 2026-03-04 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 83a2406f-0d76-3b23-9dc2-02a76df4a257 | 0.2643 | -60.6203 | 2026-03-04 01:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.0 |
| f818f58b-0e26-3946-a591-e8246c310c11 | 1.5047 | -59.9116 | 2026-03-04 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 998f9052-0154-33e3-8461-856de83f2ea0 | 1.5229 | -59.9114 | 2026-03-04 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.0 |
| d34b642b-638c-3ec9-bb8c-024332174125 | 1.5047 | -59.9116 | 2026-03-04 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.5 |
| f163cf54-a8f6-3a8b-b5fe-34b06f6fa000 | 0.2825 | -60.6203 | 2026-03-04 01:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 53a9a9f8-fcd1-3b5f-a762-d38edf2a1aec | 1.5046 | -59.9306 | 2026-03-04 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 19ec0ac8-d05f-34e9-848a-cdf740aac444 | 0.0455 | -60.9988 | 2026-03-04 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 70f18390-4a06-3c88-bcfc-422388fe9ecb | 0.2825 | -60.6203 | 2026-03-04 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a17b227c-098a-36fe-8dee-7672f113aa27 | 1.5229 | -59.9114 | 2026-03-04 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ecaddb25-5376-3752-848e-75616868a88f | 0.0455 | -60.961 | 2026-03-04 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 4b1306a5-6da1-3655-8db9-1fd51da17610 | 1.5047 | -59.9116 | 2026-03-04 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e06a01cf-9354-37f1-b1a1-7b56e9a2b05e | 0.0273 | -60.9799 | 2026-03-04 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 8693e513-adb0-3fd3-809d-b1bbd2e56c5f | 0.0455 | -60.9799 | 2026-03-04 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 831.9 |
| 45e1359e-485f-3ca0-a241-093097946652 | 0.0638 | -60.9799 | 2026-03-04 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 131.0 |
| eb6879cd-ffe5-3d77-8aa4-2d2010b446fb | 1.5229 | -59.9114 | 2026-03-04 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b5c42375-29dc-3996-8565-151c09f81971 | 0.0273 | -60.9799 | 2026-03-04 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 51beaef0-786e-360a-a286-627d0311334d | 0.0455 | -60.9799 | 2026-03-04 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 789.5 |
| f73116c2-c548-3607-a07d-2b0882d93ec1 | 0.0455 | -60.9988 | 2026-03-04 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 171.6 |
| cf7a9e31-6991-37ba-88a7-6153634377a5 | 0.2825 | -60.6203 | 2026-03-04 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4554839b-d874-398e-9392-05a9c2a3e6db | 1.5047 | -59.9116 | 2026-03-04 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 8edcffb9-d894-3bc6-aa5b-98968fdd0f17 | 0.0455 | -60.961 | 2026-03-04 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 9162f602-8c88-3ea2-a1ec-85224ca8d303 | 0.0638 | -60.9799 | 2026-03-04 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 96011789-2ca6-3e06-9dc7-752ca4b09ede | 1.5047 | -59.9116 | 2026-03-04 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e0ae4089-e0f4-31a2-bcc8-2cba20a25508 | 0.2825 | -60.6203 | 2026-03-04 02:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8271d1f5-12ce-3a02-895d-95c6236a26f0 | 0.0455 | -60.961 | 2026-03-04 02:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 123.8 |
| d77132d0-e1c6-311f-8f14-b44eab87bfdd | 1.5047 | -59.9116 | 2026-03-04 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b6784c54-a546-3a0a-8d47-ca69c01cad06 | 0.0455 | -60.9799 | 2026-03-04 02:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 591.0 |
| 87b231ca-82f9-332d-ad23-313ad8be144f | 0.0455 | -60.9988 | 2026-03-04 02:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 143.1 |
| a5570f0c-9dba-3975-80c4-1bd4d17bf2a0 | 0.0638 | -60.9799 | 2026-03-04 02:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 123.3 |
| a17cb469-dfc2-3d85-9776-001f00e085b5 | 0.0273 | -60.9799 | 2026-03-04 02:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 02320946-3ce7-39e2-9f55-3ad0a4d3b3ef | 0.2825 | -60.6203 | 2026-03-04 02:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ee84bd88-f8a9-34df-998f-b03e6399b1b6 | 0.2825 | -60.6203 | 2026-03-04 02:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 37e6ecaf-87de-33f5-807a-675d1697708c | 1.5047 | -59.9116 | 2026-03-04 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f5dc4edd-2d5c-3ccb-9702-eff186cf44bc | 0.0638 | -60.9799 | 2026-03-04 02:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 21c83f1a-7c60-3614-b328-67442b212be1 | 0.2825 | -60.6203 | 2026-03-04 02:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 33c942b5-e45d-313b-87e9-720e4dc2e5b0 | 0.0455 | -60.9988 | 2026-03-04 02:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 176.7 |
| b35b822d-1bfc-3aff-af1c-cbadd45ce12d | 0.0455 | -60.961 | 2026-03-04 02:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 93.7 |
| dba879a7-a799-3458-9332-3cb08b381ef4 | 1.5047 | -59.9116 | 2026-03-04 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ea80281f-4293-3c0c-bd9f-82a56e483812 | 0.0455 | -60.9799 | 2026-03-04 02:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 595.9 |
| 0a439c48-134f-3cdb-af9c-6d25c02bfcb7 | 0.0273 | -60.9799 | 2026-03-04 02:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 6780f264-cda7-35b1-95eb-15e05f43b882 | 1.5047 | -59.9116 | 2026-03-04 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 75d0f829-05c7-3c7c-ab9d-26880fd6ea9f | 1.5047 | -59.9116 | 2026-03-04 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| efd3f6b8-e466-3136-818a-7f048323009a | 1.5047 | -59.9116 | 2026-03-04 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| c9daf66e-0b92-3ecf-b605-692849955825 | -25.00384 | -49.30515 | 2026-03-04 03:27:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| be7ac02e-bad0-3060-b715-4a01624e28e0 | -23.38704 | -46.23431 | 2026-03-04 03:27:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9a8da1a9-4dff-3aa9-9cfb-dfe58a6a98d5 | 1.5047 | -59.9116 | 2026-03-04 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a2d133ae-2a34-3000-864b-8d7d9e988146 | 1.5047 | -59.9116 | 2026-03-04 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 01f13cba-b728-3621-aff6-360ec6ecea74 | -6.08506 | -37.3078 | 2026-03-04 03:44:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6d9c4d16-58b3-3f79-9773-5ee7f22d858e | -5.57182 | -40.60394 | 2026-03-04 03:44:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 7bbafedc-febc-36a0-bd94-5513fb9688dd | -8.25962 | -44.01748 | 2026-03-04 03:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3a5d07d0-c10c-39fd-9b76-52714ef92e5f | -8.4962 | -40.09695 | 2026-03-04 03:44:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 151d7782-9eac-3972-a185-f8d8eeaf2fa1 | -4.49519 | -40.12777 | 2026-03-04 03:44:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8962c14e-a6a4-3f45-852c-3b714a0cd788 | -9.85982 | -37.09364 | 2026-03-04 03:44:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.3 |
| b7b9dd61-7976-3445-9609-f744875a4cb3 | -14.56213 | -41.35688 | 2026-03-04 03:46:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 5582a0c4-3178-3614-a0e8-48f6f1b19751 | -10.77764 | -40.95926 | 2026-03-04 03:46:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a185754-7c9b-3669-9a9c-367c37741f06 | -11.17216 | -38.60118 | 2026-03-04 03:46:00 | NOAA-20 | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 74bbc28d-02d8-3e87-9d55-099278d5dd8d | -16.44268 | -41.49927 | 2026-03-04 03:46:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 966c67a1-9fc1-317a-9609-7c897a03955e | -16.74242 | -43.2742 | 2026-03-04 03:46:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5eb3e579-79e8-381b-8352-f002abdd70aa | -14.88046 | -48.36664 | 2026-03-04 03:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| a14c0f90-729a-3952-958a-4117729fc295 | -16.0809 | -40.57909 | 2026-03-04 03:46:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bf107aa9-d8c5-3d50-8335-72e53d0f5e44 | -14.03218 | -45.60987 | 2026-03-04 03:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd702ca7-e546-3fd4-8364-c44e0f3bf84b | -14.7276 | -45.54696 | 2026-03-04 03:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 85051ee2-9b45-33a3-94dc-955411f9ce3d | -17.25916 | -39.75551 | 2026-03-04 03:46:00 | NOAA-20 | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fd05c6d8-1710-3f4a-9b11-8f58e1f1de1c | -14.12429 | -46.39552 | 2026-03-04 03:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a7eb16ee-822a-3002-a918-86f228777ccb | -14.60456 | -44.40817 | 2026-03-04 03:46:00 | NOAA-20 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 7e46327a-0039-3319-b5e8-21b6b267ff47 | -14.3933 | -43.3736 | 2026-03-04 03:46:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 12aac22d-f664-3d00-980f-add242a356f5 | -14.6102 | -46.16232 | 2026-03-04 03:46:00 | NOAA-20 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| c124855c-f437-392d-b788-02bbff7dcda0 | -15.43072 | -48.96838 | 2026-03-04 03:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6e24de9-77e6-358b-b75c-f30895947749 | -13.40059 | -48.26164 | 2026-03-04 03:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15924a19-5b2c-3b0c-ba74-773f7143a85b | -21.1054 | -49.26191 | 2026-03-04 03:49:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c60e7e41-9eff-39d4-a5f5-55058e190c48 | -18.37084 | -39.9554 | 2026-03-04 03:49:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 93136281-2fee-3b65-a183-82ac9345c0d8 | -20.89872 | -48.84878 | 2026-03-04 03:49:00 | NOAA-20 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| f899791f-c242-32c9-98ac-add37efcd764 | -19.16928 | -40.13792 | 2026-03-04 03:49:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86f59333-c686-3e5b-ab4c-ace8a4d29201 | -20.8166 | -48.28174 | 2026-03-04 03:49:00 | NOAA-20 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cfd11ff-e5b7-3b8a-ae94-37c5701e75bd | -20.82976 | -46.54189 | 2026-03-04 03:49:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| a462098b-c171-3aaa-87a7-71201d477793 | -21.70536 | -47.10533 | 2026-03-04 03:49:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57077d68-3a7c-36d3-89a1-a6491d375d07 | -20.68508 | -49.29631 | 2026-03-04 03:49:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 440a7fce-16ef-339a-8380-f679822708b9 | -17.34209 | -45.46926 | 2026-03-04 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| a0e14822-4f40-3523-b609-e6e873526031 | -20.52975 | -40.59254 | 2026-03-04 03:49:00 | NOAA-20 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 22ef86b3-92fa-3651-b707-289eff3008c7 | -20.73656 | -47.86506 | 2026-03-04 03:49:00 | NOAA-20 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 03596537-207f-3f7c-9878-ad260845115e | -19.68274 | -39.98883 | 2026-03-04 03:49:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8f96ec3-f0ab-38ae-820b-973d732df6f7 | -20.30219 | -49.5849 | 2026-03-04 03:49:00 | NOAA-20 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a55521c-679f-3c2d-bc0b-5645c0dcab9f | -20.09368 | -44.6108 | 2026-03-04 03:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3458f9ce-25b6-3947-9c12-e7cdcccadb3e | -21.70054 | -48.43509 | 2026-03-04 03:49:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63ae3e32-466e-3ed6-81e4-c1449ca8c93e | -20.06941 | -50.51401 | 2026-03-04 03:49:00 | NOAA-20 | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 857ed450-42da-3635-a3d1-45274c5bb214 | -21.69982 | -48.43844 | 2026-03-04 03:49:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33e6e964-4145-3a38-8e78-22ec852b2cb9 | -20.91645 | -50.53179 | 2026-03-04 03:49:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 30d84128-b15b-3ac3-89fc-b6d310872cf4 | -18.547 | -47.93699 | 2026-03-04 03:49:00 | NOAA-20 | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9b8360d8-efd7-311b-a350-30decff26817 | -17.8392 | -44.84921 | 2026-03-04 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d334c525-0953-3a90-8492-a530a9c5e662 | -20.93599 | -53.42375 | 2026-03-04 03:49:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e5f16486-dedb-3788-b277-23701372ac9c | -21.31189 | -48.5383 | 2026-03-04 03:49:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62d25ec6-91fa-37fa-a565-0796303f49b0 | -20.87594 | -52.54534 | 2026-03-04 03:49:00 | NOAA-20 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49b1eea2-c535-39fc-9e2e-0418c3948210 | -21.70476 | -47.10735 | 2026-03-04 03:49:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a50aeca-71f1-36c1-abc7-082f177e1177 | -18.80435 | -51.61286 | 2026-03-04 03:49:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb8a28cb-c34a-3d9d-a60d-4c0d4e7db4a4 | -20.79506 | -52.06104 | 2026-03-04 03:49:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
