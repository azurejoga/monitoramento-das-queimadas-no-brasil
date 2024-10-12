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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28287e94-dd4f-3558-b0b1-f759eea8dd75 | -4.5859 | -47.0968 | 2024-10-12 04:35:32 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f6c39dc6-e71b-3934-9f39-56685d11594b | -5.2486 | -48.0424 | 2024-10-12 04:35:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 77ffe5d0-508d-313e-b3e1-57d7c459766d | -6.747 | -59.3259 | 2024-10-12 04:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| cb4d533f-57a8-36ec-af30-595515f76edd | -7.8717 | -54.6814 | 2024-10-12 04:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 16b45b45-2e07-349c-8abf-baa9409ffeb1 | -7.8901 | -54.7004 | 2024-10-12 04:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 9c32000e-0f73-336e-af50-df7330892659 | -7.8715 | -54.7016 | 2024-10-12 04:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| fd07f81d-1930-3a28-a91f-2d0e777ee4f9 | -7.8713 | -54.7217 | 2024-10-12 04:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c2229c1b-e65c-350d-b41d-397323e89ac9 | -7.8531 | -54.6825 | 2024-10-12 04:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| cf5c96a2-79b5-3940-9989-b896da091425 | -7.8529 | -54.7027 | 2024-10-12 04:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| b13ffce5-e441-3db4-99f3-3ecbdb27cb11 | -11.8377 | -58.8445 | 2024-10-12 04:36:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 682bb4f8-ac68-39b4-8b11-8d61a9ed00ef | -12.4367 | -54.5778 | 2024-10-12 04:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| df6731e5-1cbf-3b27-96a3-2640733b2af6 | -12.437 | -54.5573 | 2024-10-12 04:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| decdaeeb-a606-35e6-a9c5-deab0300c620 | -12.4558 | -54.576 | 2024-10-12 04:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| a09b3784-420c-31d6-9203-eaa3ccb835ef | -12.456 | -54.5554 | 2024-10-12 04:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 37bac53f-aaa4-3014-a308-130315ebd73c | -12.8896 | -53.4986 | 2024-10-12 04:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| eec1e192-e4f3-3fb6-b9b2-6484f4ee101c | -12.8893 | -53.5194 | 2024-10-12 04:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 05edc48f-d431-3285-97fa-b25a6850ec4b | -12.9464 | -53.5339 | 2024-10-12 04:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 08e25d16-6d1c-3fcb-84b0-72bf8ad49474 | -12.9655 | -53.5319 | 2024-10-12 04:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 141.5 |
| d13cfb09-7fdc-3211-aaf7-999b14932c28 | -12.9467 | -53.5131 | 2024-10-12 04:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| babc2e54-6819-3fa4-9e42-2c70aedab7d3 | -12.9658 | -53.511 | 2024-10-12 04:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| b5eb44bd-c305-33e5-9c00-b20cc11468c1 | -17.1761 | -57.4585 | 2024-10-12 04:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| c45528a9-2032-367a-b652-453f1cdb6914 | -17.6471 | -56.3084 | 2024-10-12 04:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| f2caf8a4-fe1d-3000-b216-b409571b9425 | -17.6467 | -56.3292 | 2024-10-12 04:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 1a2563a2-8c76-329b-8e30-cba799884af5 | -17.6679 | -56.2435 | 2024-10-12 04:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| cb8748aa-1980-3045-9f4d-3a347b1c9803 | -18.2158 | -56.5249 | 2024-10-12 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 24590f78-9de7-3fb0-833d-3b03d07f6a88 | -18.1964 | -56.5066 | 2024-10-12 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 249eb367-3cd9-3f40-959a-69dc6dc4106f | -18.2162 | -56.504 | 2024-10-12 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 4a8a07af-f387-3eb0-9757-ad03a67d589e | -18.196 | -56.5275 | 2024-10-12 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 25e0267a-81f1-3e53-b19a-db92d34df5be | -18.1956 | -56.5483 | 2024-10-12 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 8dbf161e-e12f-35b9-a29e-f0cc4aaf6553 | -2.7701 | -51.3622 | 2024-10-12 04:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 3618d42b-bc94-3322-99b5-445796a2cc63 | -2.7885 | -51.3618 | 2024-10-12 04:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b2e73d28-25f2-3760-a1f6-a0d4899e5bcb | -2.807 | -51.3406 | 2024-10-12 04:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 1ebf0151-60e4-3b78-92d7-69b80336a120 | -2.8254 | -51.3401 | 2024-10-12 04:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 9562b564-1eb8-3361-b48d-896972835149 | -3.1426 | -50.3724 | 2024-10-12 04:45:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 73953eff-205f-3bed-b3a4-b361a9c60dc3 | -3.1427 | -50.3514 | 2024-10-12 04:45:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| fc9bec81-0bd0-33a6-9494-014898721ed9 | -3.1611 | -50.3508 | 2024-10-12 04:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 5202b569-718a-3790-a0fd-9a1d550f578e | -3.6978 | -50.1225 | 2024-10-12 04:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 77e673ca-af0b-32fc-a7ee-d3489cd59d43 | -3.9265 | -42.4246 | 2024-10-12 04:45:26 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| 20d81186-ca12-3ae9-8455-c0dd006b5369 | -3.9267 | -42.401 | 2024-10-12 04:45:26 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 9d2ac798-eda2-3ac9-ad73-47ecdc62c896 | -3.9394 | -46.445 | 2024-10-12 04:45:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| aac88cf3-2db5-33af-bb1b-07ca6b63bac7 | -3.9396 | -46.4229 | 2024-10-12 04:45:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 55ada1b2-1f20-3d82-8208-90a517f79687 | -4.4538 | -44.5763 | 2024-10-12 04:45:29 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 54e08a18-7152-3d93-8e88-6414d446fe73 | -4.5859 | -47.0968 | 2024-10-12 04:45:30 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 3773fa17-fbf4-36e5-a51b-0939cd4512d4 | -5.2486 | -48.0424 | 2024-10-12 04:45:33 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 7dc68a99-6ff1-3263-af2c-65fe88a5f655 | -6.747 | -59.3259 | 2024-10-12 04:45:42 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fb38e012-7dc6-369f-89b7-e2277139b1ac | -7.8529 | -54.7027 | 2024-10-12 04:45:48 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5b83ab52-3351-3f0c-b0ab-f0cc84e8e7b3 | -7.8713 | -54.7217 | 2024-10-12 04:45:48 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e72525e2-c32c-3fd7-b1e6-3296ca522ea1 | -7.8715 | -54.7016 | 2024-10-12 04:45:48 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 5b21c14d-63f7-3b85-b5ec-685c81061ab4 | -7.8717 | -54.6814 | 2024-10-12 04:45:48 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3d8260fc-f28a-3365-b664-f53c0e51e028 | -7.89 | -54.7206 | 2024-10-12 04:45:48 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 8646ea1e-c4b9-35e6-b63e-622435e642ae | -7.8901 | -54.7004 | 2024-10-12 04:45:48 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 9e9a2bf8-d9ab-3a5f-91b5-bb90965e4ff0 | -11.2719 | -50.9441 | 2024-10-12 04:46:07 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| b2f94092-ef02-31c0-b63e-edb822f2be99 | -11.3295 | -50.8954 | 2024-10-12 04:46:07 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 52c6f074-3d55-361d-9c35-e9f4eed9ef7d | -11.8188 | -58.8459 | 2024-10-12 04:46:11 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 579df7cf-2ba9-31d1-83d1-f076c9ae5688 | -11.8377 | -58.8445 | 2024-10-12 04:46:11 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 9507470f-6199-3d03-a045-565d38b637ff | -11.8379 | -58.8248 | 2024-10-12 04:46:11 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| aba59ff0-0c51-34a3-b7e1-f93d9973292d | -12.4367 | -54.5778 | 2024-10-12 04:46:14 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 19658729-dfa0-3188-83ec-b9b51c154201 | -12.437 | -54.5573 | 2024-10-12 04:46:14 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 1803deb4-568c-3171-886d-cf132599987d | -12.4558 | -54.576 | 2024-10-12 04:46:14 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 49df5470-6cb0-3dee-9ec1-32302e9bca35 | -12.456 | -54.5554 | 2024-10-12 04:46:14 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 19ebaf31-e3a5-349e-86e7-75117bd98e84 | -12.9464 | -53.5339 | 2024-10-12 04:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 0cb1350d-3cd8-39a2-8df6-a78b3381143e | -12.8129 | -53.5277 | 2024-10-12 04:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 8e85eaf3-1614-385e-91a3-ad01b1046903 | -12.8132 | -53.5069 | 2024-10-12 04:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| ae26fc46-6392-32f6-807d-f9828cb6bfd8 | -12.8135 | -53.4861 | 2024-10-12 04:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| ccc22062-9158-3334-8843-910a43d0c45c | -12.832 | -53.5256 | 2024-10-12 04:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 14a4f76c-8878-3920-8b89-c70d16f58a63 | -12.9467 | -53.5131 | 2024-10-12 04:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 80b15463-bf64-3291-a46f-b4d2d90de15c | -12.8323 | -53.5048 | 2024-10-12 04:46:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 3073007d-4ca7-3969-8cdb-642f077d3354 | -12.9658 | -53.511 | 2024-10-12 04:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| d4a9c293-0dd3-3cc8-a985-8002bd39e963 | -12.9655 | -53.5319 | 2024-10-12 04:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 149.8 |
| eae48b23-d371-3abf-aba0-d4262dcca66c | -13.7346 | -60.6079 | 2024-10-12 04:46:21 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 518dd145-28d8-36c7-b623-1d66a2577883 | -13.7348 | -60.5883 | 2024-10-12 04:46:21 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 26369e59-261d-3838-8482-536f5aa6c579 | -16.9805 | -57.4404 | 2024-10-12 04:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| fd3b7213-3d77-30b0-8824-c217fc617858 | -17.1761 | -57.4585 | 2024-10-12 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 00a8bea8-3d15-36e1-b02b-0f0058d79816 | -3.93349 | -42.40135 | 2024-10-12 04:53:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 08dafaa7-d451-3279-9ea4-865db4c6e9f8 | -3.93233 | -42.39553 | 2024-10-12 04:53:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f2a9de71-0927-30f9-9a22-1b25d192d2bb | -3.93174 | -42.41249 | 2024-10-12 04:53:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| adae668a-160e-3410-9777-1362a79377d8 | -3.93065 | -42.40668 | 2024-10-12 04:53:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 129.6 |
| a7c28b1a-081f-3ab7-a82a-342be5ef11c4 | -3.92898 | -42.41785 | 2024-10-12 04:53:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 2b1df810-5935-3b02-8456-03551e35c4af | -3.42632 | -43.34849 | 2024-10-12 04:53:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| eb0432d6-f9d4-3f48-bc16-c1d1b69600c4 | -3.42148 | -43.34209 | 2024-10-12 04:53:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fa7d8678-8de6-35ec-a6be-a06b952924dc | -2.82735 | -40.35122 | 2024-10-12 04:53:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9561c3a2-0578-31a5-936f-6489c3796e28 | -4.60081 | -45.63374 | 2024-10-12 04:53:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7519f0ae-67cf-30b1-a4f2-356ec27d4807 | -2.83471 | -49.52879 | 2024-10-12 04:53:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 8a50e461-52e3-3b58-be09-830d2788b27a | -2.83252 | -49.52415 | 2024-10-12 04:53:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d9c4636b-d289-3c34-bbb8-37d70e831f5d | -7.47244 | -40.22092 | 2024-10-12 04:55:00 | AQUA_M-M | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 11fe3a2d-1e50-3528-993a-6db72ad5944a | -5.40602 | -45.35088 | 2024-10-12 04:55:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ca4cac83-aba2-3452-b7ca-9f4e370f4b1f | -5.39731 | -45.35658 | 2024-10-12 04:55:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 73a86c67-b681-30a5-87e9-17fc6606aab0 | -5.39398 | -45.34882 | 2024-10-12 04:55:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 91aac731-bb8f-3850-b1e6-617d30e36040 | -5.3225 | -45.40847 | 2024-10-12 04:55:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8248eda7-41cd-3155-858c-d0d26810e879 | -5.26101 | -48.02169 | 2024-10-12 04:55:00 | AQUA_M-M | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 488ca6d8-015d-325f-ac91-948b90c6fd33 | -4.85639 | -45.6752 | 2024-10-12 04:55:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 8f439852-b6ad-3f88-81a6-0b52b815fe7d | -4.58625 | -47.09888 | 2024-10-12 04:55:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f234826a-a11b-3ec0-94b2-9d479a67c3bd | -4.58369 | -47.09074 | 2024-10-12 04:55:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 81217686-6551-3b97-a1de-b13f265e723a | -0.57657 | -51.69796 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8e76614-75e1-3409-9a29-c9b179e0f38a | -0.42367 | -52.06361 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3931e00f-4062-39b2-9bf5-cc2f520ee965 | -0.42091 | -52.05963 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 968b6e9a-3e31-35d9-99d6-01f9597ce22d | -0.42036 | -52.06309 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7d71e26-25d1-391f-8608-23873c00945e | -0.41759 | -52.05912 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8266cbd7-c966-362e-af51-a69f38ae89c9 | -0.41705 | -52.06258 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3842b5cc-aed2-3201-bf00-165b00aab649 | -0.41537 | -52.05167 | 2024-10-12 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README57.md)
