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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e5ee2a2-ca2e-3200-8650-0ee246065b43 | -5.8998 | -48.0461 | 2024-12-10 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 249a5221-ad36-3448-8fff-aebf2e4283de | -6.9158 | -43.5185 | 2024-12-10 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 5e9dd2ee-fbfe-3a57-b477-b7b07e9f984f | -2.9859 | -52.8554 | 2024-12-10 01:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 68137ab6-3523-3a1c-87bc-caf0f9d54ffe | -3.0043 | -52.8549 | 2024-12-10 01:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 7ee2ebfd-ab97-32ac-a2f7-bf94d7619a23 | -3.0043 | -52.8549 | 2024-12-10 02:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| ccba1b52-3ae7-33e4-ba40-2222bdc23419 | -5.9185 | -48.0449 | 2024-12-10 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 9c2178e3-0e41-3d08-bcd7-18917cd9d84f | -3.0044 | -52.8345 | 2024-12-10 02:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5b2aa95a-c584-3d26-9272-95c580967496 | -2.7757 | -45.0157 | 2024-12-10 02:00:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 0e67fc64-cb9d-3abf-852a-348a7ee0b6bb | -2.7758 | -44.9931 | 2024-12-10 02:00:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 01f22cd4-b3dd-3b71-b0e4-a9deba9d2c6d | -2.9859 | -52.8554 | 2024-12-10 02:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a1c94353-ddab-38d0-aa7b-be2216d5e9c6 | -4.3959 | -47.7618 | 2024-12-10 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 73fc5d9a-172e-3624-88ef-b1878861127c | -2.8199 | -52.9816 | 2024-12-10 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 54569577-2ead-3111-8d2d-b21ae0f26a22 | -5.9183 | -48.0667 | 2024-12-10 02:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 9f21fb78-832a-30d5-a840-cbe92ac445ff | -4.3774 | -47.7627 | 2024-12-10 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 66c7aced-97c4-3977-8f6b-4c4dbb40b4c3 | -6.9158 | -43.5185 | 2024-12-10 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d0823a2c-d084-33b4-b1b7-124f89bdf396 | -4.3961 | -47.74 | 2024-12-10 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| f755f6b0-a80a-37ca-86e7-1216b000ec82 | -4.3774 | -47.7627 | 2024-12-10 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 812315a1-c700-3ab8-898c-1800eb6894db | -6.9158 | -43.5185 | 2024-12-10 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 317def77-222b-3417-a7a8-60c12f4740dd | -2.7758 | -44.9931 | 2024-12-10 02:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 272.3 |
| 0655868c-1c8e-321d-bfb0-622d997af536 | -2.7943 | -45.0151 | 2024-12-10 02:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e8f71fda-af09-3605-8c59-d5419322aea9 | -4.3961 | -47.74 | 2024-12-10 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 40d9f2c7-42b2-3dd1-825c-3818ca564fd8 | -2.8199 | -52.9816 | 2024-12-10 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| db0da133-cf15-380e-9644-84065dfccd6e | -4.3959 | -47.7618 | 2024-12-10 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 7a5c3a22-23f3-3cdc-96d1-992501e07ad1 | -2.7757 | -45.0157 | 2024-12-10 02:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 179.0 |
| 791324b0-4c5b-3220-b96b-67fcd245ff40 | -5.9185 | -48.0449 | 2024-12-10 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 199.3 |
| c301b813-33a0-3292-96d4-7377b46ad5b8 | -5.9183 | -48.0667 | 2024-12-10 02:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 2e92b7b7-5903-35db-9c9e-7083329f3e01 | -3.0043 | -52.8549 | 2024-12-10 02:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| a0af070e-546d-3af3-867a-6a410c5536e2 | -2.7944 | -44.9925 | 2024-12-10 02:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f77fb9bd-e90a-3e8b-b152-4702c4678968 | -2.9859 | -52.8554 | 2024-12-10 02:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 044da842-1653-3443-81b9-d0b67931ae6d | -2.7944 | -44.9925 | 2024-12-10 02:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 95de329d-d815-3971-affa-e15759bb73be | -2.7757 | -45.0157 | 2024-12-10 02:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 81226db3-34d0-3cdf-a753-f30684f297bd | -6.9158 | -43.5185 | 2024-12-10 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e63e1769-970e-3bf7-a7a2-980da9578a01 | -11.5426 | -56.4438 | 2024-12-10 02:20:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ad9aae91-230c-3ab1-ac29-da6564cacf8e | -5.9183 | -48.0667 | 2024-12-10 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 11ebc42e-b674-3a31-af9a-f84d72bc6f4a | -11.5237 | -56.4453 | 2024-12-10 02:20:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a3e78b59-08b1-386b-b572-9d72657c9c05 | -2.9859 | -52.8554 | 2024-12-10 02:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| ca7f24a5-c4ec-3428-8c55-db4955800960 | -2.7758 | -44.9931 | 2024-12-10 02:20:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 7f998adc-5f5d-3f97-9129-712264fb611c | -3.0043 | -52.8549 | 2024-12-10 02:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 6c1a5c5e-962e-3741-ab50-0bdf9beb9ad6 | -5.8997 | -48.0679 | 2024-12-10 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 51e72429-5b42-3f1a-84e2-d4028a83679f | -5.9185 | -48.0449 | 2024-12-10 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 184.1 |
| c428c642-5f54-3426-8af9-8a18f97c9512 | -5.8998 | -48.0461 | 2024-12-10 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 4590d885-2b9e-38ef-9738-7280cc20b33b | -2.8199 | -52.9816 | 2024-12-10 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 641a669e-3fd0-3964-8c8a-3bba336f740a | -2.986 | -52.835 | 2024-12-10 02:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3c4a972a-efd6-340d-b856-1a018baa0c06 | -5.8997 | -48.0679 | 2024-12-10 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f7e1dec9-f20b-3455-9bc2-24bcf3963919 | -2.9859 | -52.8554 | 2024-12-10 02:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| a3990df3-3c1b-3a38-93bb-f9a53c321768 | -2.7757 | -45.0157 | 2024-12-10 02:30:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 1f15c08e-3b2d-3925-95f7-a6251ad231e1 | -5.9185 | -48.0449 | 2024-12-10 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| f6b886e7-e56b-3bd6-bf0c-86fdf2e286c8 | -5.8998 | -48.0461 | 2024-12-10 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 0df9fbe4-f0e0-3bfc-9ab3-4b4cb4c7614c | -6.9158 | -43.5185 | 2024-12-10 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 751f5c2c-8d96-38fb-95a3-1d087d6b4879 | -2.8199 | -52.9816 | 2024-12-10 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 9921a6d4-d55c-367b-b67b-d4879b6e2880 | -5.9183 | -48.0667 | 2024-12-10 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| eb87b390-9aab-3641-be36-07bddbd8b0b4 | -2.7758 | -44.9931 | 2024-12-10 02:30:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 0c734da2-912c-39a8-83ec-591cc0881374 | -5.8998 | -48.0461 | 2024-12-10 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| b89cec58-25b8-3b33-8847-887231a11d88 | -2.7758 | -44.9931 | 2024-12-10 02:40:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| acd1f3f8-46d5-3679-847f-4f01acd65213 | -5.8997 | -48.0679 | 2024-12-10 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 246e3d7e-671c-3ac9-93b3-29b2b961a11e | -5.9185 | -48.0449 | 2024-12-10 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 34972b72-0421-30d8-853a-e07ff8bb0513 | -2.9859 | -52.8554 | 2024-12-10 02:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 631e397a-cedd-343e-bc48-2dc63a9e98ec | -5.9183 | -48.0667 | 2024-12-10 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 2129d7de-91a8-37f7-ab42-e1d8ada1804a | -2.8199 | -52.9816 | 2024-12-10 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c892a5e8-e339-38c4-8218-3e19144542df | -3.0043 | -52.8549 | 2024-12-10 02:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c9aa0f6e-4faa-3e69-8f10-46dbded330ee | -2.9859 | -52.8554 | 2024-12-10 02:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 44ac34cd-e53d-391f-beaf-082c38e67a07 | -2.7758 | -44.9931 | 2024-12-10 02:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 843bb944-0a0d-3025-9878-29191cf1a9b7 | -3.1105 | -54.0657 | 2024-12-10 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| e3e240ca-b7e0-32b8-b151-38ad1954997a | -3.0043 | -52.8549 | 2024-12-10 02:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f2deff21-9593-3e15-9805-8b28577a8d85 | -5.9185 | -48.0449 | 2024-12-10 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d1ea4890-a181-355b-b51d-135fd2a4d40b | -2.8199 | -52.9816 | 2024-12-10 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| bbf84083-59e7-36f5-8cb0-cc982ff808e6 | -12.5615 | -58.3546 | 2024-12-10 03:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5341a597-ec98-3bff-9295-18dfce82eb3c | -2.7758 | -44.9931 | 2024-12-10 03:00:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 219fc96f-cd5c-3094-977d-1221720a656e | -2.9859 | -52.8554 | 2024-12-10 03:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 8e1b4eeb-c021-35e3-adde-e0c2c278d878 | -12.5425 | -58.3561 | 2024-12-10 03:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 03286302-6615-331d-8890-0edd33b17f33 | -12.5427 | -58.3362 | 2024-12-10 03:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 130c4d42-b1c0-359a-86ee-25532be50ffe | -3.0043 | -52.8549 | 2024-12-10 03:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 99cfcae5-4e02-3a28-9e2a-75d881a66bcb | -12.5615 | -58.3546 | 2024-12-10 03:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| ad163183-15fe-3164-a75e-d175368a52dd | -2.9859 | -52.8554 | 2024-12-10 03:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 430d0c0d-7957-396c-a52f-16c58fdb4dca | -2.6339 | -48.0681 | 2024-12-10 03:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 756bcec6-09be-3e5f-9cad-02c56229a07d | -12.5427 | -58.3362 | 2024-12-10 03:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| d7df5c95-7081-37a1-a7e0-cf2fa051c3e5 | -2.7758 | -44.9931 | 2024-12-10 03:10:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a06ab209-510e-3889-a45a-4019d9d02108 | -2.8199 | -52.9816 | 2024-12-10 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 4b8abf18-fe3b-349b-8b90-02be465a93a1 | -12.5425 | -58.3561 | 2024-12-10 03:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 6d0a3a85-10ba-3ae6-8521-5e462ff9ca48 | -4.61875 | -37.69808 | 2024-12-10 03:12:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5f8ad20d-7b7d-351c-a9ca-7eadb61a92f9 | -6.40014 | -35.20157 | 2024-12-10 03:12:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8149bdfe-e61c-392c-9eb2-347242f62531 | -3.06984 | -40.0477 | 2024-12-10 03:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 7138bd9e-27ca-3367-aa46-06a571054ecf | -2.84129 | -40.29927 | 2024-12-10 03:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 992c3a08-c587-3dba-a11d-3ffa7363bdf0 | -2.8401 | -40.30606 | 2024-12-10 03:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| edd7ce60-229a-3794-89b3-d1fe2600c818 | -3.06996 | -40.04995 | 2024-12-10 03:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 63589181-6afd-3f1d-b85d-b28a8ae8aa02 | -3.86021 | -40.44524 | 2024-12-10 03:12:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a09b24ef-d2b4-3e72-bdd1-7aa664c184df | -3.85202 | -40.45087 | 2024-12-10 03:12:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4bddef1e-8ec2-3d35-ab31-ca241ff14dcf | -7.00243 | -38.65462 | 2024-12-10 03:12:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b6273f33-681f-323a-8d57-dcbf51b13562 | -8.11029 | -35.0583 | 2024-12-10 03:12:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 785e4903-4854-3a38-882a-cc981aa011dd | -3.07677 | -40.04877 | 2024-12-10 03:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 9ba9ee05-a4cd-3f6c-b16b-3fc829411ec9 | -9.04117 | -35.70713 | 2024-12-10 03:12:00 | NOAA-21 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9d997e08-fcda-3962-ba61-4d5ac5b9f68d | -7.75613 | -35.14054 | 2024-12-10 03:12:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 3b4e0565-2247-3a1c-b830-38924bec8a29 | -3.85835 | -40.4457 | 2024-12-10 03:12:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 37aebebd-7d5c-3322-ba84-e60d9e4d76dd | -6.58982 | -38.45279 | 2024-12-10 03:12:00 | NOAA-21 | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b07e4799-57f2-30b4-a89a-486e653ab5e1 | -6.58387 | -38.45172 | 2024-12-10 03:12:00 | NOAA-21 | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3c39fcbf-131f-3eb7-b4ff-18028d8594c8 | -3.07689 | -40.05104 | 2024-12-10 03:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8811e1d8-01a6-38ff-8057-91d95810bab9 | -9.03645 | -35.70596 | 2024-12-10 03:12:00 | NOAA-21 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 50452e6b-f635-3c45-9228-5041ca2814b8 | -5.68727 | -37.35938 | 2024-12-10 03:12:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 16.0 |
| aa68f7e2-4d75-30f4-b48c-eed5b63eb245 | -7.74992 | -35.25927 | 2024-12-10 03:12:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5a38be6f-4d28-3d92-8270-843ac7e68a9e | -6.15728 | -35.2742 | 2024-12-10 03:12:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |


[Clique aqui para ver as próximas entradas](README9.md)
