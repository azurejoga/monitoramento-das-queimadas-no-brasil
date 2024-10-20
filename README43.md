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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a81b7c61-c8bf-3405-b77c-14c9bb9bb8a7 | -5.13375 | -46.1564 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a07e484-7b68-343a-bbe8-bba20ddb4903 | -5.13083 | -46.15466 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0afa5544-6040-3708-8729-ac8301348282 | -5.13008 | -46.15966 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 146bd1aa-5a74-3b45-9120-06fefe31fac3 | -5.12887 | -46.15588 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0878ca6-a0bd-3921-8411-7ab6a7c98d4b | -5.1252 | -46.15912 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a8bfadb5-0d5e-31b8-84cf-dba552d4b46d | -5.12253 | -46.16559 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5520cc3b-9df5-39d3-972c-3f1246b7c810 | -5.11954 | -46.16378 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce3e8d8d-e1bf-3798-94d0-99ed3913c99c | -5.1184 | -46.15977 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6200b921-9b16-39f8-84b3-9d3e04878ffb | -5.11765 | -46.16507 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dedf9d0-abd3-3f41-b777-f1bb5d15df2c | -5.09608 | -45.94944 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c98c0eb9-524d-3dfb-aa4e-72368450f582 | -5.09443 | -46.1322 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 97a10ca6-55a0-3a2b-9b3d-02b1b4e6bdb1 | -5.07359 | -45.81725 | 2024-10-20 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e76af6a7-20aa-3597-8d66-8fab483e28b0 | -2.65535 | -46.05463 | 2024-10-20 04:55:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98d86098-b131-313a-8c95-1c71359a3006 | -2.65385 | -46.0519 | 2024-10-20 04:55:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8dd06c57-a3db-3389-98b5-0f1266de61d0 | -2.65062 | -46.05402 | 2024-10-20 04:55:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17c5382a-f212-3de5-8f53-24547b4297f4 | -2.62918 | -46.90893 | 2024-10-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 148da2a0-a303-38cf-a557-e26ee5cd155a | -2.5467 | -47.12378 | 2024-10-20 04:55:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2004790-7e7a-3938-80cb-46adf31e17e6 | -2.51247 | -45.98861 | 2024-10-20 04:55:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 123494a2-908a-3267-bf6e-a230a65eae30 | -2.51171 | -45.9936 | 2024-10-20 04:55:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30adeecb-6e44-3af4-af39-1ca4f71c88ce | -2.6285 | -46.91327 | 2024-10-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e075df6-aab5-3801-9d48-ca578b15388d | -2.62474 | -46.90828 | 2024-10-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 931c0e85-c995-3578-af90-b7753368b89b | -2.56445 | -47.06587 | 2024-10-20 04:55:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8d5fad3-9500-320c-ac24-872dec49d0bc | -2.5638 | -47.07018 | 2024-10-20 04:55:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58650647-26bf-3bc6-8338-aea8433342dd | -2.5554 | -47.29892 | 2024-10-20 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54450472-922d-313b-ab71-4fe7a9c66966 | -4.63739 | -46.41103 | 2024-10-20 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2f7e627-06bb-319c-af8a-59bf57f72439 | -4.6164 | -46.64685 | 2024-10-20 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24b2ce8f-f89e-3362-8a7c-0b4b756424ee | -4.61444 | -46.64722 | 2024-10-20 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84dcc202-7179-39fe-8cd4-80ded2bfe678 | -4.61175 | -46.64606 | 2024-10-20 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7934fdcc-bbd5-31a3-8247-888966830451 | -4.6098 | -46.64638 | 2024-10-20 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 463f2a69-9bfa-33ee-9d5c-4f962448d488 | -4.5928 | -46.67737 | 2024-10-20 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcad24bd-f36c-3cdf-9aaa-ce34d5949820 | -4.59207 | -46.68227 | 2024-10-20 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 447a3c4c-049b-3f58-b880-561775b418a6 | -4.24036 | -46.61747 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c2df6f6-2dae-37aa-adf9-4075502ae6dd | -4.23573 | -46.61675 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa0721bd-5bbf-325c-893e-2e64f886ee64 | -4.20059 | -46.63883 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 9e1368d7-9908-35b0-807d-e2ec8effaceb | -4.19975 | -46.63604 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9d3eb2d2-a4cf-3d35-ab33-017351ec5388 | -4.19666 | -46.63358 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cee86394-3bf9-3634-97a1-7f5db2b1c9f6 | -4.19594 | -46.63826 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a12ec604-b9ce-3af2-990b-8d86ad5055b3 | -4.19577 | -46.6308 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f0cf430-7b98-3bcd-be31-02486a652d9e | -4.1951 | -46.63547 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 833232df-d59e-3cce-8346-910935b7e74f | -4.19442 | -46.64017 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 4c347d46-485f-36e9-a21b-f0bd67a19246 | -4.19272 | -46.6283 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0049d3ad-4210-35ba-b89b-27afd6cd62e2 | -4.19202 | -46.63295 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d685b038-94da-3726-b786-49fc99f0caf6 | -4.1918 | -46.62551 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 584298ce-2b1d-303c-adb8-42d55af057d1 | -4.19131 | -46.63762 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8629120-ba0b-35cb-b668-10407b88de40 | -4.19113 | -46.63014 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b045f2d-43b8-3a14-a830-f0fd5ac5c272 | -4.1354 | -46.85174 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4cd4c76-f424-374e-8bc5-68671c56ddba | -4.12416 | -46.86456 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c5fde5a6-f551-30c8-8bc1-89f893bc293e | -4.04113 | -46.94461 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d37554a-fb2d-3b6f-abac-90c2eb51140c | -4.03861 | -46.94141 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9dcb6e5f-b771-32db-ade1-0d59f53bb06b | -4.03795 | -46.946 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 19e2c7d9-00cd-3991-ab02-7f558cd97f7d | -4.03661 | -46.94388 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 157d4383-fe3f-3066-a7af-0d9b0b597d5b | -4.0314 | -46.94772 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f8f9b8db-1546-32db-b995-c1ecfd1d39c3 | -3.89233 | -46.44461 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e240640-21cf-3b07-9c97-608db78427cc | -4.85363 | -47.72823 | 2024-10-20 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91b84236-b3e0-3b05-81a1-e8350a911d6c | -4.84868 | -47.73171 | 2024-10-20 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ceca6d3-ad14-3097-9220-68d8737bca28 | -4.83068 | -46.903 | 2024-10-20 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2aa8ef86-49ff-302b-9ea4-40eacc1ef71e | -4.60839 | -47.53498 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d579b8cd-2b54-3df8-a3a5-24930751acfa | -4.60775 | -47.53935 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a9f1864-78d6-3e34-b23b-9591551f7565 | -4.60336 | -47.53878 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8371bee8-43cc-33bb-a4e1-1aaf92683bb1 | -4.60323 | -47.53532 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba6bc588-1428-3870-a5e4-2081da871197 | -4.60256 | -47.5397 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f4226f2-d725-31d0-8639-3e0039bf9043 | -4.47157 | -47.7332 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f5c5d43-b903-3dc8-bd87-af6edead8542 | -4.32021 | -47.53593 | 2024-10-20 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25093869-5a85-36fa-a607-e427d05b57ec | -4.09383 | -46.91211 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8c5ff57-87c7-32c2-9d8d-161faea45878 | -4.09314 | -46.91675 | 2024-10-20 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb498daa-0c82-3cdc-b6af-4e8aa9f09135 | -4.03343 | -46.94528 | 2024-10-20 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a04859f4-208b-3a61-bcd2-4ed9a91d21f1 | -3.8129 | -47.49759 | 2024-10-20 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c14179a8-84db-393a-8378-85faf006e4d3 | -3.61663 | -47.51284 | 2024-10-20 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70d3a483-46e6-3473-911b-3bdf1d23fbba | -3.61232 | -47.51217 | 2024-10-20 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31ee7a4d-4f9f-32c0-afb1-49009e59c730 | -5.42921 | -47.2326 | 2024-10-20 04:55:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76cd4e2a-88b5-3afd-aee8-67e37dc44d7f | -5.39728 | -46.90485 | 2024-10-20 04:55:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62c8449f-4a51-3384-b8dd-2962b88fc61a | -5.83604 | -46.64793 | 2024-10-20 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3dbd9949-c444-32c7-805e-1395c4d8510a | -5.52123 | -46.5242 | 2024-10-20 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fa96893-fbf3-3cc4-93f6-d677c0616fda | -5.40191 | -46.90551 | 2024-10-20 04:55:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7980df5a-e640-3c1f-b96a-9295905b9644 | -5.40119 | -46.91045 | 2024-10-20 04:55:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| deab57d2-4ebb-3bc0-b880-e52389857f75 | -5.39655 | -46.90983 | 2024-10-20 04:55:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30349f62-cd28-3ad3-b9cc-d4c9761a8ad6 | -7.68056 | -47.32708 | 2024-10-20 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 419f6944-7b3b-3c2d-a4a7-29d1c964dd5c | -7.89663 | -47.3536 | 2024-10-20 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71ba1f86-3edb-3df7-97f4-ea434f4caf7c | -7.68521 | -47.32776 | 2024-10-20 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f45b340-cd70-3b46-847a-f6d95838404f | -7.68123 | -47.32225 | 2024-10-20 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2396c3c5-bffb-3ddc-ba73-576fbcd0f890 | -7.67191 | -47.32096 | 2024-10-20 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1aa26d88-88f0-3119-9e4e-1035b9048d96 | -7.66726 | -47.32026 | 2024-10-20 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f8cc334-c19e-3806-a132-9531efb81dc0 | -7.25239 | -47.91555 | 2024-10-20 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94988ff4-0bae-3442-b6a2-7c6a5027b563 | -7.05635 | -46.8297 | 2024-10-20 04:55:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75a06adb-7699-3210-a809-3b923bb3281b | -7.05548 | -46.83246 | 2024-10-20 04:55:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a40a4872-040d-32cd-a614-5750f5678e67 | -2.10367 | -48.36898 | 2024-10-20 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2656ced5-2df4-3e57-86e5-9ad75078e5ef | -3.48772 | -48.24208 | 2024-10-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e04193c6-185d-339e-8a9d-8d4bc82c280d | -3.48363 | -48.24137 | 2024-10-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 224b5ee2-515c-3871-9663-b3e5501cfc40 | -3.48307 | -48.24501 | 2024-10-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49fa2177-5cd0-360e-9290-c1d8b14b0936 | -3.46273 | -47.66831 | 2024-10-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36c39461-ce68-32d9-92ee-e68e7c15eee9 | -3.21846 | -48.6128 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6b1f4cf-53f0-31f3-a3a0-838bab830832 | -3.21793 | -48.61623 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f724efdb-38c2-3a7c-b010-38f890497a30 | -3.21447 | -48.61218 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63c5dca7-ee86-31dd-856b-a0d86cf64210 | -3.21395 | -48.61562 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32e1f771-2b9b-3a19-a04e-23f325d1815d | -3.21342 | -48.61906 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a0bc77e-3361-350a-9f0e-e11a7e3ac2f5 | -3.20996 | -48.61502 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1433ba9-cbb6-3769-a3aa-5357cdd86b50 | -3.20943 | -48.61845 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af3a154d-a7d8-3348-b21c-17e7960b8152 | -3.20597 | -48.61441 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52700b7e-c09b-3a31-869e-383b17ea0fd5 | -3.15976 | -48.37086 | 2024-10-20 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9180951-3c66-3527-8e50-ae2280143601 | -3.11129 | -48.63118 | 2024-10-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README44.md)
