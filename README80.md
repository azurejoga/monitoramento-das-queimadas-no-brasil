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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3451fd7f-80a9-3707-bd70-2dce9e266ce9 | -11.23149 | -54.78504 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3fe271fd-0136-36a6-a75d-97a611796205 | -11.22852 | -54.77953 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c323f882-711f-3e2f-881a-f475799152b2 | -11.22768 | -54.78435 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b80e1296-27fb-3909-a38f-56112aaba311 | -11.21325 | -54.78321 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5fca8638-3188-3046-b0d0-e126bd78269b | -11.21244 | -54.78158 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0db9f55e-4e7d-3ef7-aaf7-86f5a743fc00 | -11.2116 | -54.78642 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79661980-48d4-3831-acd6-13d92812ed50 | -11.20944 | -54.78253 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 96d06937-aa94-3ad5-9573-cf2159ea6905 | -11.20863 | -54.78735 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51f00b00-cc16-3ddc-9ca9-0b20b87b5790 | -11.20863 | -54.78091 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b30553b5-980d-391f-84f0-3f2fb4cb0013 | -11.20781 | -54.79221 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17c1e77b-8a66-3cb7-a136-442ce95c8a51 | -11.20779 | -54.78572 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6a46734-9913-3987-b6a2-da49d671e909 | -11.20694 | -54.79056 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59f82a65-f1ee-3f27-8384-1586c7b2c09c | -11.20563 | -54.78184 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b11f3ac5-768a-3de7-b87c-421154de8a0e | -11.20482 | -54.78024 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c68e190b-c477-3d7a-89c2-11333348f6d1 | -11.20481 | -54.78666 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2d30f30-8980-3da2-b9d0-fa9021d51632 | -11.204 | -54.79151 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51f058ea-ce7f-3a3e-b1b9-d6325acbbf4e | -11.20398 | -54.78504 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff49a0a4-c0ea-39f2-bc82-cc75e84b9d54 | -11.20313 | -54.78986 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 767daee7-616a-3397-915a-6fb5aced3bfc | -11.20181 | -54.78115 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8e8fd34-b233-33c2-84e2-2f5e358fed7f | -11.201 | -54.78597 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a27c8038-29dc-397d-a82e-dabed1662126 | -11.198 | -54.78045 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfefb288-a7fc-339c-9f1e-62f0ba318c32 | -11.19719 | -54.78527 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1eb4909-aa1f-344c-b3c2-c8b81c69008f | -11.19419 | -54.77976 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4725f02b-75ef-34c9-9564-861a4776ef52 | -11.32281 | -54.0369 | 2024-09-27 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d930c08-def0-3d72-bed8-f29c3c703f46 | -11.31842 | -54.04064 | 2024-09-27 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cabb058-1fe9-3ca1-9fe0-565b6e456d12 | -11.31769 | -54.04502 | 2024-09-27 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e012a22-4a76-3ddf-871b-00ab67a22c5b | -11.31476 | -54.04002 | 2024-09-27 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f25fb4b-a4e4-3f0a-8926-10745adcc7f8 | -11.22666 | -53.9373 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ffba015-05dc-33c4-9c92-7562b1f5abb5 | -11.21938 | -53.93604 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a69c83fa-ccb3-366e-bbc8-8b017aeb5a77 | -11.21574 | -53.9354 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d0a4217-c4eb-32d1-b5e4-4eb0cebce854 | -11.2143 | -53.94401 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4eacf235-95d5-3c41-ba86-5b66e0622553 | -11.20996 | -53.96996 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56c819c4-177a-3fa1-8eab-8e8592c425a7 | -11.20777 | -53.96063 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 441df840-6e2e-3116-a1d1-3426e866cde2 | -11.20705 | -53.96497 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d0820f4-dfaf-3adc-bd5d-09cecd8d3cf7 | -11.199 | -53.90143 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 087c8cca-dfb7-3568-a85b-aa5e45f87d50 | -11.19756 | -53.90996 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09b09dcb-ac53-358c-89bb-5661ed4709c3 | -11.19684 | -53.91425 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84c6576c-83df-3199-9c76-4d916dd5f3ca | -11.19612 | -53.91854 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b74a083-a4bf-3e0f-a166-f74d310beed9 | -11.19536 | -53.9008 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 949e9de9-3f58-36cf-914b-2ac4be51434a | -11.19464 | -53.90508 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a242b405-26e3-3712-93cf-3a3c6b4c9ba1 | -11.19392 | -53.90935 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a21a3d8c-1f5a-3e08-9d75-c6d39c68569b | -11.1932 | -53.91362 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebf133d3-e5eb-30ee-846e-c05d2d4723f3 | -11.19248 | -53.91792 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c12c0747-d838-318d-9fce-371f46ea31e0 | -11.19101 | -53.90445 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a9b82745-2f29-362a-a528-9f048160474b | -11.19029 | -53.90872 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5089560c-b485-30fa-b165-ad00327da760 | -11.18957 | -53.913 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc0813f3-69e2-3634-84cc-874e044a29de | -11.18884 | -53.91729 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01b3ba0f-4207-3d68-b639-20bbbea6c336 | -11.14067 | -54.17938 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 994a39da-13b9-39a2-b47c-8f9ec0fb4239 | -11.13992 | -54.1838 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 16ac7add-2a1e-3984-9495-e7e40aa86c26 | -11.13623 | -54.18317 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23dbec72-97eb-337f-9292-ca34c8c81e09 | -11.13547 | -54.18762 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc5849cc-0044-3612-80b6-7a9f5bf3bf6b | -11.13254 | -54.18252 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9758a14-d84b-3b7a-a873-485631352586 | -11.12885 | -54.18188 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e9f2ab8-bc6c-3157-b8fe-c16299e9001f | -11.03291 | -53.99502 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 36e5c25f-eede-37c6-bbe4-5796cecd24a8 | -10.93898 | -54.26375 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2fc6e0a-73b6-3ab0-85af-085130a01810 | -10.93822 | -54.26827 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ccad743c-65ac-39c8-936c-4cc3f9ad61aa | -10.93526 | -54.26311 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6acc160-85ea-3d98-8dbe-0c39aa4f6143 | -10.9323 | -54.25798 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 67e37b15-0c7f-35b1-b4f8-7dc4312cc906 | -10.93154 | -54.26247 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 70624323-8fe7-314a-a21e-1eb5f2227ff0 | -10.93078 | -54.26697 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5861cad5-fd3c-3f1d-ba66-5f742a692f7a | -10.92934 | -54.25285 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 716d01a7-0e0e-3e77-a255-0de9670f0593 | -10.92858 | -54.25735 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 2d128942-8eb6-3c3c-8458-58b8d195e4af | -10.92782 | -54.26184 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 82d0d6eb-1ed7-3811-85b3-ad9c7c19515e | -10.92706 | -54.26635 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5320d848-6795-3953-93b2-b743aa8744fa | -10.92563 | -54.25221 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9a44a6b3-ec4a-33ca-9750-d13eb2733976 | -10.92487 | -54.25671 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6f11dd93-4716-3f44-9df7-b6962406029b | -10.9241 | -54.26123 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| af0de3f4-f00c-3477-a3ee-7d3c2812affe | -10.92334 | -54.26573 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 79e88afa-7d05-31a5-967e-305b30f1fa95 | -10.92191 | -54.25157 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 84da29f2-a9b5-3972-b022-d165e6d53801 | -10.92115 | -54.25607 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b43f9db2-8176-3245-9f21-fa15fe5a9479 | -11.21199 | -54.76172 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0eda3520-b02c-3af6-8f64-8c784d9d3518 | -11.21187 | -54.76807 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4bd6ce8a-6f18-3e63-9654-24f9e9d6451d | -11.21116 | -54.76649 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45f95a32-6b7e-3cae-9a68-c31b93e5af1e | -11.21106 | -54.77287 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9231068f-fe38-393e-8f7b-b115a0711314 | -11.21032 | -54.77128 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 78f59100-181c-3c42-8923-057455911de2 | -11.21025 | -54.77769 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 04bbccb8-f316-3ef5-8088-31f811b29da3 | -11.20966 | -54.75787 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| de0d524d-f26e-3800-be3c-3dd33db5e205 | -11.20948 | -54.7761 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21a0ad79-e934-315f-9763-27a75bea9ea0 | -11.20901 | -54.75634 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ca9e9e5-91ab-3a7b-8e76-8ff86b8ded03 | -11.20886 | -54.76261 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3183667b-fb4b-3735-baf0-444737d4d9b0 | -11.20818 | -54.76107 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3726eaa6-41e2-31d5-8477-daf37bfc320d | -11.20806 | -54.7674 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf9de5fb-427f-3d6d-8c17-070bde6e965a | -11.20735 | -54.76583 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6270a669-be40-33d7-9707-8c3ca23370f5 | -11.20725 | -54.77219 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e9dcfd00-3703-3209-8055-6bc4233f3982 | -11.20651 | -54.77061 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ca9a34d-61f6-385f-9e03-f58e8f65ba16 | -11.20644 | -54.77702 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0a0041f5-e726-366d-9f14-fb5b9b09f947 | -11.20585 | -54.75722 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 43194eb6-b85a-37ab-97db-261d438623dc | -11.20566 | -54.77543 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64c104c6-51ef-3cc4-8d68-3f41cf65a30f | -11.20505 | -54.76196 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c217d3c1-43c6-3d49-9d1d-05fe6d1d783e | -11.20425 | -54.76673 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64767f85-c2fd-3cd4-8918-ccc3b270c54f | -11.20344 | -54.77152 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77d3cc41-b84a-3895-9c39-9d2e493d3194 | -11.20263 | -54.77634 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86bd0ee1-bde7-3968-9525-f98b1494bc75 | -11.20204 | -54.75657 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3d15cdcb-df0f-3fde-bec7-834720a6cef7 | -11.20124 | -54.7613 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 94f762e6-d248-39c0-90c8-5eeb32925ec0 | -11.20044 | -54.76606 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 893291c3-0613-3176-bb9e-acd3f7d89635 | -11.19963 | -54.77084 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87e74c28-aee7-326f-ae72-d8760e341fea | -11.19882 | -54.77564 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49dd1b57-b166-3e40-83ed-5b169fa48fba | -11.19823 | -54.75592 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5601242b-1ac7-3c11-b92b-a27136c6fe67 | -11.19742 | -54.76065 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cc1fe41-e8b4-3cbe-85a9-3cb024daaaa3 | -11.19662 | -54.7654 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README81.md)
