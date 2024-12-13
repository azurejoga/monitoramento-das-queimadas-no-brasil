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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28e12650-6901-3863-9554-3cb0ae42fe00 | -11.1962 | -53.8142 | 2024-12-13 01:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5333a414-faa1-3f97-990f-a19cec15290a | -6.9346 | -43.5168 | 2024-12-13 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 362.6 |
| dfadc84e-a7aa-391a-8423-875249f849ba | -6.9158 | -43.5185 | 2024-12-13 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 347.6 |
| 75022c09-d4a5-32a9-adf1-cce2c3df070a | -1.6385 | -46.6743 | 2024-12-13 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9adc0911-7abe-3521-a329-ac2fed1f6c26 | -13.0641 | -52.0538 | 2024-12-13 01:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 237b69c6-5a3c-3410-a402-9ea6b72f2315 | -5.2108 | -43.3067 | 2024-12-13 01:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 31982177-a57f-380a-bc01-d60cfbe03c29 | -13.0836 | -52.0304 | 2024-12-13 01:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 3fd2131d-a638-3ef2-8083-84cab06f6588 | -11.1962 | -53.8142 | 2024-12-13 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| af9fd856-d550-378f-bc88-b2c0ebed6a05 | -6.9346 | -43.5168 | 2024-12-13 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 384.7 |
| a9a4ade9-b909-3355-bf08-eb1da303a18a | -6.9156 | -43.5418 | 2024-12-13 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 4a89ce40-8bd2-30f8-9d62-63ad0484c383 | -2.5108 | -51.8023 | 2024-12-13 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| f2e9508d-3bee-395d-a936-927b747fb870 | -2.4923 | -51.8233 | 2024-12-13 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0cc74497-8434-355d-a290-3cdf89d02942 | -1.62 | -46.6747 | 2024-12-13 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| db2e5567-0ef9-35ad-9620-33bca3b5c98b | -13.0644 | -52.0326 | 2024-12-13 01:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| d1b9029f-bd97-3c1c-822f-587c44fd6c28 | -11.1959 | -53.8348 | 2024-12-13 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a6b05420-94c6-3acb-8181-c848c6856395 | -14.7655 | -52.6446 | 2024-12-13 01:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a46d3070-55c0-37f2-927d-2239fe2bbbf6 | -11.2148 | -53.833 | 2024-12-13 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 4d161c14-9c19-3061-8fd7-380180c2867b | -6.9161 | -43.4952 | 2024-12-13 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| e9eb2d07-0740-329e-8c4f-c19992572398 | -5.211 | -43.2833 | 2024-12-13 01:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 7b19ddaa-bf7e-3162-bca5-e3d09f20c358 | -6.9349 | -43.4934 | 2024-12-13 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 873ec4a2-72cf-354a-90f9-20fa7677280d | -2.4923 | -51.8027 | 2024-12-13 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 22598ed5-9aad-3a3c-9f57-df0fa0137ad1 | -1.62 | -46.6526 | 2024-12-13 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 52eb9b25-5ee5-3389-93ca-9637742aa141 | -11.2151 | -53.8125 | 2024-12-13 01:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| df1b2d2b-75ad-3356-ac78-7753d466bb10 | -6.9344 | -43.5401 | 2024-12-13 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 1b91fc48-7967-313c-9ed5-2de8cda6c76b | -11.21061 | -53.82166 | 2024-12-13 01:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 96a02bfc-2e19-3a0f-8f67-df7591d8bbf8 | -11.20583 | -53.82775 | 2024-12-13 01:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.7 |
| cb7b3a85-255c-336d-b03e-0db238273703 | -11.4387 | -55.93139 | 2024-12-13 01:58:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| e029e97c-0145-3656-8ccc-a47c4db909a6 | -11.44246 | -55.92435 | 2024-12-13 01:58:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4d6b0f53-b4e2-3975-8256-b4ac7322b1b4 | -11.19405 | -53.8247 | 2024-12-13 01:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 4b56b24a-6a48-3601-b227-b577d5c6b08c | -5.211 | -43.2833 | 2024-12-13 02:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 8732b0bd-eb20-3175-8029-e9d88f1041f4 | -11.2148 | -53.833 | 2024-12-13 02:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 90b03114-646b-349b-a936-61ff8effbfb3 | -6.9346 | -43.5168 | 2024-12-13 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 388.3 |
| b776fdd2-5aa8-3f77-a256-99c6d56c173b | -2.4923 | -51.8027 | 2024-12-13 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 1cf24d8f-2ed3-3ca5-8b07-ba4dfae63063 | -6.9349 | -43.4934 | 2024-12-13 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| ef2e950d-6bda-3200-8454-dd0cb36f09ba | -2.4923 | -51.8233 | 2024-12-13 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 636c9c37-5966-3a92-af67-9d7cb80d8555 | -1.62 | -46.6747 | 2024-12-13 02:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 5b8ed6e5-2649-3448-8cda-385c70824eb7 | -11.1962 | -53.8142 | 2024-12-13 02:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| dc27d329-26c8-3842-9bc5-bf9258415a74 | -6.9158 | -43.5185 | 2024-12-13 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 328.8 |
| 62d821fd-9218-3650-bb20-5c25c4dbbe34 | -14.7655 | -52.6446 | 2024-12-13 02:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 48146ab6-fe8b-3980-997a-f4c34cfd7ae3 | -6.9344 | -43.5401 | 2024-12-13 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 0cc2e705-7d79-38fc-8472-ee4d11dfb2e2 | -13.0836 | -52.0304 | 2024-12-13 02:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| bd64659b-75b2-3bb0-b129-f4bf5eee1cbb | -13.0641 | -52.0538 | 2024-12-13 02:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 5be34c51-f04c-373d-b593-160831f184f7 | -6.9161 | -43.4952 | 2024-12-13 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 86aa1881-70f7-31f8-bc67-892b95be77a1 | -11.1959 | -53.8348 | 2024-12-13 02:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 165d8243-9d13-353e-9497-5ca3c92b6c4b | -13.0644 | -52.0326 | 2024-12-13 02:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| ff245569-89c5-36f2-a2b1-03652eb27479 | -2.5108 | -51.8023 | 2024-12-13 02:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 66257e1c-9b81-3a01-8622-0e69c8a8edb7 | -11.2151 | -53.8125 | 2024-12-13 02:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 43a0c975-d672-3154-bf1f-6d316d7dbac4 | -6.9156 | -43.5418 | 2024-12-13 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 5bde5302-9bd3-33d3-9271-f674978c7733 | -5.2108 | -43.3067 | 2024-12-13 02:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| e0bd9c84-6bf5-3df8-bff8-50d59f029133 | -6.9 | -43.51 | 2024-12-13 02:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 91ec8f5f-74a2-39f5-9c93-c52726a7acb7 | -6.93 | -43.56 | 2024-12-13 02:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| afb197a1-110a-3656-a002-688095b53b8f | -6.92 | -43.52 | 2024-12-13 02:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4aebec64-54ed-378e-bc50-0d6880c10b5f | -6.92 | -43.47 | 2024-12-13 02:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d5a9724-9e02-332c-aac0-52a632d49d7d | -2.4923 | -51.8027 | 2024-12-13 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| b38d3c6a-b568-3c6a-915c-b7801b801f14 | -6.9344 | -43.5401 | 2024-12-13 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 262.8 |
| df435fe3-42d0-3141-84c6-375294ecddce | -11.1962 | -53.8142 | 2024-12-13 02:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2d649943-2da4-3da6-9f3e-05300c6c3f33 | -2.5108 | -51.8023 | 2024-12-13 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| aa095189-5f7e-3b45-aefb-eea4aad46cee | -11.2151 | -53.8125 | 2024-12-13 02:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2ea36f4e-cb42-3b8a-b05c-debbe065ebb7 | -11.2148 | -53.833 | 2024-12-13 02:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| c2e641b8-749d-3bbe-8c2c-185ed323132c | -11.1959 | -53.8348 | 2024-12-13 02:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 5a8badc8-1413-354d-8029-ab48bc35808a | -6.9161 | -43.4952 | 2024-12-13 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 68211092-b0ec-3e1f-8c56-36e2f2c649fc | -13.0644 | -52.0326 | 2024-12-13 02:10:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 66b7b233-59d8-3c5b-a654-02588905635e | -3.2685 | -46.9362 | 2024-12-13 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| ffebe7b0-6456-3ba6-ac63-35233b18d793 | -14.7655 | -52.6446 | 2024-12-13 02:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 173ffaec-1634-3d30-89b2-9f3ca0033f77 | -6.9346 | -43.5168 | 2024-12-13 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 418.0 |
| 1fb67cfc-476e-3a67-b7e0-c992ad2d810c | -5.2108 | -43.3067 | 2024-12-13 02:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 83eee426-08a4-36d5-8592-b6ddb0bb5801 | -6.9349 | -43.4934 | 2024-12-13 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 81251e9b-c080-32ed-83ee-d34a5ad9ea78 | -6.9158 | -43.5185 | 2024-12-13 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 308.1 |
| 4c1bfb5e-3517-381d-9efb-24c47f3a5625 | -2.4923 | -51.8233 | 2024-12-13 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a3272f45-d835-3a47-a5f6-4725eea49bb8 | -1.62 | -46.6747 | 2024-12-13 02:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 72cc8656-23e2-3add-83ae-3cdbd7c99f96 | -5.211 | -43.2833 | 2024-12-13 02:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 0483b414-99d1-3526-9ccf-9b6443c7c679 | -6.9156 | -43.5418 | 2024-12-13 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 210.2 |
| e0d9b085-9e17-3593-bca0-f8675d89fa31 | -2.5107 | -51.8228 | 2024-12-13 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a6305245-23f3-3554-a1fa-f9c21ef59a24 | -3.2686 | -46.9142 | 2024-12-13 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| ad7e3f45-e337-3c9e-809f-92c3eee8217e | -2.4923 | -51.8027 | 2024-12-13 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| e02e96d0-8a0f-35aa-a9cc-f12b06f1e846 | -2.4923 | -51.8233 | 2024-12-13 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a8b7302c-4b4c-33d4-ae64-62f8f25d02c6 | -6.9158 | -43.5185 | 2024-12-13 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 374.3 |
| 35c122a9-5855-3380-a8b4-f1fa47848991 | -6.9349 | -43.4934 | 2024-12-13 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3fd5bb0d-54ab-3645-be63-f89743ba0f41 | -6.9156 | -43.5418 | 2024-12-13 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 272.7 |
| 93245440-0a2f-31bf-b1d5-1dd7457427c1 | -1.6385 | -46.6743 | 2024-12-13 02:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ebea0345-ec1d-3109-8954-58a8f1369488 | -1.62 | -46.6747 | 2024-12-13 02:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 458dc378-4b50-36c3-a93a-b5d5357a27f5 | -2.5108 | -51.8023 | 2024-12-13 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| e3e06a9c-b35a-3bc0-89fd-6541ed71d31f | -5.2108 | -43.3067 | 2024-12-13 02:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 28dd4a86-f18d-33e0-b445-bc1f5e68f626 | -13.0644 | -52.0326 | 2024-12-13 02:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b2fd630b-7f8c-363d-995f-b2339d796b7b | -3.2685 | -46.9362 | 2024-12-13 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 6c43e0ce-23c1-310c-a563-c09c3697b983 | -14.7655 | -52.6446 | 2024-12-13 02:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 1acbfb2d-1676-39ae-9a21-b955c6c35187 | -6.9346 | -43.5168 | 2024-12-13 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 362.2 |
| 067e1ed4-db09-3a79-b59a-66ac5badca80 | -11.1962 | -53.8142 | 2024-12-13 02:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 7885ff42-0480-3903-95c1-c08df924b344 | -11.2151 | -53.8125 | 2024-12-13 02:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 39158ccb-89ed-3289-89d3-c2c02260ca75 | -11.1959 | -53.8348 | 2024-12-13 02:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| aa0edba0-44b0-3f0b-8527-7428f4edb3f1 | -6.9344 | -43.5401 | 2024-12-13 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 224.8 |
| 69543394-3be0-3519-bcde-978ef9506363 | -3.2686 | -46.9142 | 2024-12-13 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3b079245-9cc6-3ca1-aa5a-0ae43dae8663 | -5.211 | -43.2833 | 2024-12-13 02:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 75f11f85-3502-3fa4-8739-1e7ae623d416 | -6.9161 | -43.4952 | 2024-12-13 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| e0edb736-dfd8-3186-95ef-61e4ec1c50f3 | -11.2148 | -53.833 | 2024-12-13 02:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| f4bd1a2f-8ccb-36f0-8ac1-d199257f0a0d | -11.1962 | -53.8142 | 2024-12-13 02:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 836ac644-1941-33aa-a404-49efeb5ced36 | -2.4923 | -51.8233 | 2024-12-13 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| be7f5c75-4c92-31f7-b02e-40be199fc22f | -5.2108 | -43.3067 | 2024-12-13 02:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 29fb1daf-5042-383a-ac84-b353aaee931a | -11.2148 | -53.833 | 2024-12-13 02:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 62eef854-5625-3f8b-ba68-a60d2102fc9c | -3.2686 | -46.9142 | 2024-12-13 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |


[Clique aqui para ver as próximas entradas](README8.md)
