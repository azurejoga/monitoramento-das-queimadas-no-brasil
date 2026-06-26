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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2140f5d5-c43d-3a4d-9f38-d1d58f82b1af | -11.24625 | -43.31622 | 2026-06-26 05:59:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 8aad82d5-60f3-3064-935e-6e1aa37d7d32 | -12.74605 | -44.49205 | 2026-06-26 05:59:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0d485179-9499-32e2-905e-9626b7e6506f | -12.75749 | -44.49405 | 2026-06-26 05:59:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 19ce9f4e-62d4-3553-9529-01447cb9f493 | -15.58928 | -48.36621 | 2026-06-26 05:59:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 29e9365f-a4bc-337b-9126-9724ea1374b3 | -5.7758 | -45.0599 | 2026-06-26 06:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7d54c960-3a37-3f1b-82df-0eed0c8d204c | -5.7945 | -45.0586 | 2026-06-26 06:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 55fbe748-ca15-33fa-80dc-5de92e865315 | -5.7758 | -45.0599 | 2026-06-26 06:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 6923cdb8-9613-32cd-8568-2740244770c4 | -5.7945 | -45.0586 | 2026-06-26 06:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 0d2d4b76-d541-34b1-ab7a-09861d932a46 | -9.48644 | -57.32547 | 2026-06-26 06:12:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28567980-4709-3e3c-9434-9de26b87aa9c | -9.47936 | -57.32444 | 2026-06-26 06:12:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b797f02-4108-356d-abd7-d1bd4ec475ff | -12.62416 | -57.8869 | 2026-06-26 06:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 74f31bd6-c74b-37e2-aee3-d7961cfc1bc4 | -12.62345 | -57.89369 | 2026-06-26 06:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0767b3b1-f149-3e92-9211-803b7b54fc82 | -12.62642 | -57.89608 | 2026-06-26 06:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1ec2d795-019a-37aa-937b-9114d335a8d0 | -12.62715 | -57.88939 | 2026-06-26 06:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1f01397b-6063-3ef9-b6e0-471aff0607f8 | -5.7758 | -45.0599 | 2026-06-26 06:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 36a57904-daef-3f25-8f5a-f262ebcc278f | -5.7945 | -45.0586 | 2026-06-26 06:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a099aac1-6dec-36fb-89ee-4a7c5fe35378 | -5.7945 | -45.0586 | 2026-06-26 06:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 6913687a-1530-3567-8917-9f09724d39c4 | -5.7758 | -45.0599 | 2026-06-26 06:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| a281d4b0-b788-3d60-8063-f8f158e506e8 | -5.7945 | -45.0586 | 2026-06-26 06:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 92bbf755-914a-3912-bcb9-34f0e5f35940 | -5.7758 | -45.0599 | 2026-06-26 06:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| daf42c0b-2836-3165-9b35-5f1fb89e95c5 | -5.7758 | -45.0599 | 2026-06-26 06:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5bad5f03-0edd-3eaa-b9cb-b8397d8ff7ff | -5.7758 | -45.0599 | 2026-06-26 07:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6bb91dd6-1d7b-3779-afd5-d0d1609ef52c | -5.7758 | -45.0599 | 2026-06-26 07:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4036fdc7-8e63-3561-bf6f-243d538d18cd | -13.258 | -54.4315 | 2026-06-26 07:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1ef16e58-76ec-3854-9bd9-29342eda4190 | -5.7945 | -45.0586 | 2026-06-26 07:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b9b69b87-2d44-338e-9034-b7ff0d811ec7 | -5.7945 | -45.0586 | 2026-06-26 07:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 3fb0577a-addc-3f79-a4f5-85ca9b592010 | -13.25282 | -54.43233 | 2026-06-26 07:37:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| aadd0088-7c65-38a4-9eb0-af0500231eab | -12.62052 | -57.87902 | 2026-06-26 07:37:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 3c285469-0226-3968-9bd0-1a5019837108 | -13.2635 | -54.40605 | 2026-06-26 07:37:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d497d518-ed5f-33b9-b907-5c3660517c30 | -5.7758 | -45.0599 | 2026-06-26 07:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 92005b5e-9da9-361a-88f6-1e097f761094 | -13.258 | -54.4315 | 2026-06-26 07:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4fc15c90-36b6-3a92-8bec-0ee899cd7a17 | -5.7945 | -45.0586 | 2026-06-26 07:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| a77461a9-647e-33f5-9eef-644d01eeaa7c | -5.7758 | -45.0599 | 2026-06-26 07:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| dcab8da9-72ac-3b54-aceb-81841c3c51d7 | -13.258 | -54.4315 | 2026-06-26 07:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 1b6b03bb-399d-3fa1-8ef3-dce63099d125 | -5.7758 | -45.0599 | 2026-06-26 08:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| bee48ef5-b1c5-3dd3-9088-8e75e3a52ac3 | -5.7758 | -45.0599 | 2026-06-26 08:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 998fb7e1-4dad-37bc-b3b3-7262d0402d45 | -13.258 | -54.4315 | 2026-06-26 08:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 229223d7-857e-3df2-848c-ef53fe1cbd83 | -5.7758 | -45.0599 | 2026-06-26 08:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 51439cac-17b9-3420-8387-2a858ffc8551 | -9.0687 | -44.7535 | 2026-06-26 11:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 1f24a5cf-06a1-333c-8287-fd94ec7444be | -6.50594 | -42.22173 | 2026-06-26 11:47:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| a60d23af-cc76-32c8-ad04-8488a9e17d4e | -6.55213 | -38.27922 | 2026-06-26 11:47:00 | TERRA_M-M | VIEIRÓPOLIS | PARAÍBA | Brasil | 2517209 | 25 | 33 | nan | nan | nan | Caatinga | 15.2 |
| ab197043-be69-380a-a21e-1fc60aa7f3ce | -5.77898 | -45.06153 | 2026-06-26 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 058472c8-0556-37b0-98a8-c549c8b9ae6f | -5.90368 | -43.85236 | 2026-06-26 11:47:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 54bc62c0-c173-3a11-9844-bfba9ada8515 | -5.80933 | -45.11708 | 2026-06-26 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fc0b4c45-f57d-3c12-9460-581897f6a1f6 | -5.79158 | -45.0512 | 2026-06-26 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 66488a05-149d-3c2b-9331-32e316d4d38a | -5.79033 | -45.06013 | 2026-06-26 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 077b2cdf-442a-3eb7-9b24-b7806db7de16 | -5.32462 | -44.69382 | 2026-06-26 11:47:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 5831bd23-4ed9-34a9-956a-663062ab07f4 | -5.78025 | -45.05264 | 2026-06-26 11:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| be121183-7ac3-3b55-bed0-e9de4b01052c | -5.3259 | -44.68478 | 2026-06-26 11:47:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 6378d052-15f9-3424-b8d4-0d75432c286e | -2.96384 | -41.05875 | 2026-06-26 11:47:00 | TERRA_M-M | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 939b2a6c-0f4c-3ddf-bb59-c6f4bfab1af3 | -12.50929 | -48.26267 | 2026-06-26 11:49:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d65c88fd-92d7-361f-93c4-906d66c99e04 | -15.60644 | -48.35957 | 2026-06-26 11:49:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d5bc9a8a-fe96-388a-b7d5-0ba041aad55f | -7.73992 | -44.1762 | 2026-06-26 11:49:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3da5c2c8-7b59-363c-a62f-aaee6f6d93d1 | -8.86369 | -46.93069 | 2026-06-26 11:49:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c232667-0642-326c-b574-d79d5e44776d | -8.23559 | -47.11651 | 2026-06-26 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ccecd0af-8e70-3080-ac17-41aa2b5e3d27 | -14.70017 | -45.06066 | 2026-06-26 11:49:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3397fd62-6c00-3b96-8a98-0ea11f954cae | -12.51686 | -48.27319 | 2026-06-26 11:49:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 60ab7079-357b-31bf-bbdb-9a612ae9d271 | -14.7008 | -46.14634 | 2026-06-26 11:49:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f823bd5e-2da4-3d36-a68c-580662a73814 | -6.30921 | -44.64769 | 2026-06-26 11:49:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5ebeed61-e1f3-3636-a4a1-5ba4e14729ef | -14.84477 | -48.13263 | 2026-06-26 11:49:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| badc6740-3dca-3a86-8f50-0988ffbe3254 | -8.94598 | -45.64209 | 2026-06-26 11:49:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 742cb741-813d-369d-b2ac-66d7b53c7bef | -8.22674 | -47.11517 | 2026-06-26 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aeae8c5a-b7d3-3f4c-aa72-4daa379912bb | -10.27968 | -47.6007 | 2026-06-26 11:49:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 737311a5-5367-3504-87b7-a546eac81075 | -7.7507 | -44.62508 | 2026-06-26 11:49:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 5973fe04-f82f-3f18-a548-efb40ddad886 | -10.51975 | -48.97548 | 2026-06-26 11:49:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 5ddef696-1d2a-3bc9-9c3b-f3b34d86b753 | -12.1723 | -45.84166 | 2026-06-26 11:49:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 99920717-5710-3f3f-9838-e8dcb19e5a6e | -6.98609 | -42.8989 | 2026-06-26 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 4826ca39-7cd5-350e-8d70-57aa080e4048 | -13.87318 | -47.12251 | 2026-06-26 11:49:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76213896-6401-3e5a-ba1a-eed5a3f8d723 | -9.13778 | -46.8257 | 2026-06-26 11:49:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c1b6a794-60a4-3382-862c-758caddb99ff | -10.6376 | -47.04033 | 2026-06-26 11:49:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 2189e935-0779-3855-89a7-8ab1d48ac06c | -9.07946 | -44.74496 | 2026-06-26 11:49:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c3ae5ffe-4de0-36f1-8100-4f8c9f178007 | -12.86286 | -44.35193 | 2026-06-26 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 033430f2-c010-34b6-af9f-8d360b48f893 | -10.81824 | -53.52459 | 2026-06-26 11:49:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 727bea59-8e08-393b-b31d-0a8069e0f89d | -8.93208 | -45.67681 | 2026-06-26 11:49:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 0ab7a927-9120-3c20-a850-d9abf389f4ac | -8.31193 | -47.54784 | 2026-06-26 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 01321e44-9e05-3e21-937d-8586f1a2ea49 | -10.57047 | -47.19432 | 2026-06-26 11:49:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b844af7d-d941-31ca-b7f8-559a9631140c | -11.31094 | -51.41409 | 2026-06-26 11:49:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 65ac9691-993d-3eb1-b0ec-295a89c74aa1 | -12.51552 | -48.28242 | 2026-06-26 11:49:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 638597d0-4c48-3db5-8f19-fdf750ce5085 | -10.63888 | -47.03144 | 2026-06-26 11:49:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| db45fff9-6aa8-310a-8790-a40c22bf43dd | -10.93452 | -49.41645 | 2026-06-26 11:49:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 88dc0b11-b37f-30b2-a152-f65ec534ea3e | -12.76251 | -44.48881 | 2026-06-26 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a64e3494-a3d4-327d-b970-d25864ef2f53 | -9.07813 | -44.7546 | 2026-06-26 11:49:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 39.4 |
| c58bf027-a745-38d2-8e3d-86cf08c726be | -8.22566 | -47.44476 | 2026-06-26 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 06291f0e-52f4-30ae-a99c-68dc2d6ec357 | -11.31318 | -51.40016 | 2026-06-26 11:49:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 84309a7c-ee80-3e99-8d76-b454d6d48dd0 | -11.16528 | -48.67671 | 2026-06-26 11:49:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e63322b5-2efd-3ab2-924d-55edf5cbdb1c | -8.93968 | -45.68702 | 2026-06-26 11:49:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7824a500-5890-3b97-8b9f-c8c17d43acc3 | -6.97618 | -42.89762 | 2026-06-26 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| a101247c-637f-3a21-893b-7cf7777265dc | -14.05466 | -45.40375 | 2026-06-26 11:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 4c82478c-cffe-3ed0-b837-aebb5116516f | -12.17359 | -45.83231 | 2026-06-26 11:49:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| aa19f41d-13d8-3882-9e00-834482484321 | -8.13241 | -47.89029 | 2026-06-26 11:49:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7e88d329-2a78-3199-a309-d2f2b9415b90 | -11.30852 | -51.40755 | 2026-06-26 11:49:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 5819321e-452b-3f87-b9fb-028603c54696 | -13.08567 | -48.17034 | 2026-06-26 11:49:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f23537f9-57aa-3d10-9319-5fb46eaf2ade | -10.36415 | -47.34365 | 2026-06-26 11:49:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3b2eb805-13a1-3c2a-9921-a93f0cf5eac7 | -9.07031 | -44.74374 | 2026-06-26 11:49:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 508c75fd-2f3a-3f39-90c3-3a9c00d13571 | -11.63434 | -52.86338 | 2026-06-26 11:49:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 19f3d70e-9e24-3f27-9f3c-60a7e43556f4 | -6.97774 | -42.88623 | 2026-06-26 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 1cb832a3-a3b6-338c-aa14-74119c363e8a | -6.98765 | -42.88756 | 2026-06-26 11:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| cefe23ca-26dd-3ef3-8e56-87c2b0d84f38 | -9.06899 | -44.75338 | 2026-06-26 11:49:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| ae7c7d4b-9b81-39bd-b2b7-202be7d4b581 | -12.75285 | -44.48752 | 2026-06-26 11:49:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2d773010-9aab-348c-af66-e0b32474b84f | -8.31767 | -47.12523 | 2026-06-26 11:49:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README18.md)
