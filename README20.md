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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e23a7086-df38-3542-a673-97c6beffc099 | -4.74785 | -46.64936 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccb0f1dd-5749-3870-bedd-f094d209c997 | -4.74598 | -46.6223 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 891bee0c-b3e3-3ed7-b62f-f210a6b75f2e | -4.7458 | -46.60354 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bb8e988-c7db-3d16-9fe3-5cf7bc842aa5 | -4.74489 | -46.60866 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a5aeaf5-696a-315e-b150-f2789345ae0e | -4.74299 | -46.61923 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af88e9a1-3d59-3908-946b-e02b44da41fc | -4.74242 | -46.6052 | 2024-10-24 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d8c53f3-8f06-3a63-901a-4f21d622c730 | -4.71631 | -45.73862 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1a52063e-62ec-371f-b495-5e93cd670db7 | -4.7103 | -45.73776 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 86754959-737c-3dd3-ad40-3b048abe3f74 | -4.70948 | -45.74248 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5a6723da-0419-3ea1-868b-5e6784efeb86 | -4.6785 | -45.81298 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 474fb3b0-a404-3646-85ea-8068bcbd5100 | -4.67672 | -45.81142 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a212d528-d630-3b45-85fd-82e595a2c98a | -4.66657 | -44.49499 | 2024-10-24 03:40:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51cc7c45-560e-3bb7-a3a7-49a2be5d2ebc | -4.6644 | -44.61179 | 2024-10-24 03:40:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ed383b7-4405-346e-933b-07eb491af78a | -4.66378 | -44.6155 | 2024-10-24 03:40:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a77c54a-0aa8-324d-8b2b-0202ff37b40a | -4.66314 | -44.61193 | 2024-10-24 03:40:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48dca619-7ac4-36ae-961a-c5755bfeb1e8 | -4.6625 | -44.61561 | 2024-10-24 03:40:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f16c544d-2c70-392e-8a2b-c7036e17ca53 | -4.6582 | -44.61458 | 2024-10-24 03:40:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b0974b3d-4d8f-3697-ba00-95ef3e986abc | -4.65757 | -44.61834 | 2024-10-24 03:40:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c7652bb-202b-37ca-9d5f-66e4037cb132 | -4.65691 | -44.61474 | 2024-10-24 03:40:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed650b16-78cd-3639-a4e1-9560b788c4b8 | -4.65626 | -44.61846 | 2024-10-24 03:40:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f613e25c-b325-329c-b3d0-c7617487957e | -4.65437 | -45.68962 | 2024-10-24 03:40:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9d2f28f-37f7-38b3-9607-e988ce08bcd4 | -4.57853 | -45.61464 | 2024-10-24 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af0c7ff4-5b2e-3063-9e28-bfbee90e04d3 | -4.5759 | -45.61213 | 2024-10-24 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a057633-78fb-3691-9c4c-50624eb1ceb4 | -4.57254 | -45.61385 | 2024-10-24 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f03a06a4-eaca-31ce-b624-4c5d2a1b774b | -4.57043 | -44.00383 | 2024-10-24 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1ff4e118-f92e-3a36-a0c5-d9034db8e0ae | -4.56985 | -44.00718 | 2024-10-24 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 700c5b3a-34af-315d-97d2-a05baf7cf051 | -4.56927 | -44.01053 | 2024-10-24 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| feabdaa6-c790-3ace-9d04-b717af5e76a2 | -4.56507 | -44.0029 | 2024-10-24 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9165547f-3c09-376c-a90d-f286b0063ace | -4.56449 | -44.00625 | 2024-10-24 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 52ed9e0d-ee70-3479-9718-f5d9c9e70243 | -4.56391 | -44.00962 | 2024-10-24 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e0581904-5ff2-35fa-be5f-8528bd512fd4 | -4.55914 | -44.0053 | 2024-10-24 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 74bd8fc1-8750-3647-8908-2d3708af6631 | -4.55856 | -44.00867 | 2024-10-24 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8d03dd25-a7c6-368b-b70b-d088ced7fae0 | -4.55381 | -45.8054 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 154120b0-6063-3e70-b3af-ef4198f503c9 | -4.55256 | -45.80291 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d91c7434-8c32-3b87-a38e-1153cc3dde7c | -4.55179 | -45.80746 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a21fa5e0-23c7-3f5d-81bd-9ef2fcd20b23 | -4.5486 | -45.79979 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 02fe5268-f98c-30ab-8750-d32faf21655b | -4.54785 | -45.80404 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e3780d2b-acf8-312b-a8c0-95ef886d6815 | -4.54704 | -45.80857 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| be8250ba-85c6-3477-9bf5-1b621b054a19 | -4.54658 | -45.80167 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 399c0367-5dd6-3f16-b194-9408a5952a1c | -4.54583 | -45.80602 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f4a51e82-7c6a-3462-a938-d3bc113b5ccf | -4.54188 | -45.80273 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a0b4ba27-539c-3238-a983-175170502432 | -4.5406 | -45.80037 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ae8987a-bf6e-3eca-9f42-b0a5dfa2e4e1 | -4.53987 | -45.80461 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74a6316b-6d88-3482-bb61-d07533f1c7c9 | -4.45927 | -45.64858 | 2024-10-24 03:40:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cac7d7a-dd32-3237-8f16-8fc62008b5ea | -4.45856 | -45.65274 | 2024-10-24 03:40:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90d7a60e-b194-3759-bc54-e8a7f3e9d259 | -4.45326 | -45.64782 | 2024-10-24 03:40:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94487c56-4f8f-3701-b2d6-143c72923246 | -4.42573 | -46.46912 | 2024-10-24 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c34f3de-2ade-31af-bbda-b84c23fe6eb5 | -4.42237 | -46.46984 | 2024-10-24 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc2fc77a-eb5c-36dc-a3eb-996d4117944c | -4.29405 | -45.50343 | 2024-10-24 03:40:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6dde9b21-783e-36fb-b7f1-217f4314d28c | -4.29334 | -45.50764 | 2024-10-24 03:40:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| daf7fad5-4272-3ba2-944a-a8bfb4a78c35 | -4.29219 | -45.99931 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52887b91-6722-3b18-944d-a9ebbdfbee2c | -4.29183 | -46.00227 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfa69695-2ff1-3a04-8917-d7bde9dc2c28 | -4.29132 | -46.00422 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa89569c-067d-36c3-9226-44b190eb413a | -4.28202 | -46.75903 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c698098b-7536-3913-a47d-3491daef3d32 | -4.27735 | -46.75531 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c084912a-e500-3452-9b2c-d6c7914a388e | -4.27636 | -46.76084 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1a7fd841-d301-3c4d-a8f0-8b5dea031c69 | -4.27566 | -46.7576 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 697b9d4a-9fe7-3569-942a-e0e72ab09f88 | -4.27472 | -46.76304 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b4c3a69-a91c-3f02-890a-dafc8b27bb34 | -4.24788 | -48.34414 | 2024-10-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e2679576-4eb3-3725-9675-9207b613cf15 | -4.24648 | -48.35195 | 2024-10-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d61b2b29-96e3-3953-ad61-dd255cd48b38 | -4.24282 | -48.34571 | 2024-10-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f499e61c-d5ef-308f-a90b-73aaf2a0269e | -4.24151 | -48.35333 | 2024-10-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b9bb55dc-c3c5-3b63-87ce-dc3552de9e4a | -4.2394 | -48.35093 | 2024-10-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d328bfc5-0414-3bcb-8303-bfcf9f8fb128 | -4.21897 | -44.26538 | 2024-10-24 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 824c4588-b98e-31ac-89a9-c82104981fbe | -4.21835 | -44.26898 | 2024-10-24 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d298c528-e06b-3b21-a46c-e2b5a90255dc | -4.21774 | -44.27255 | 2024-10-24 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca3bae61-5969-3fd1-aaa5-98c6da088e54 | -4.21288 | -44.268 | 2024-10-24 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5326353-4a3c-3a0d-90e5-40b1270a3ba2 | -4.21227 | -44.27158 | 2024-10-24 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed542e95-a18f-3b9e-b5c1-e02f3700e162 | -4.17661 | -48.60081 | 2024-10-24 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c430b2d3-2be8-34c8-8c14-2dda4a15b8f5 | -4.11024 | -44.23941 | 2024-10-24 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ce10310-4014-3538-82af-2e8d760a57be | -4.10475 | -44.23857 | 2024-10-24 03:40:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| efcf8f22-fdcd-31da-ac74-d2b9d6ab7641 | -3.98691 | -45.79583 | 2024-10-24 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b690d742-94f1-3b2c-92d4-ef9416308541 | -3.94515 | -46.4363 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7c80bd87-0fe8-3373-ba23-b1fc04ef6ddc | -3.94427 | -46.44135 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| dd1624d2-fd70-3c55-bdac-58da1c4e0203 | -3.93973 | -46.43008 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| a2e30394-3380-3f3d-bb67-b6d2c9af61f1 | -3.93884 | -46.43516 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b0e1790d-febd-363a-b5ea-1123de070c54 | -3.93795 | -46.44025 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| dcc56eb3-67d3-3f83-8cc7-c570726974cd | -3.93737 | -46.42686 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2b9c5a3d-e6cf-3a56-b13f-23a4f89ab3ce | -3.93653 | -46.43186 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 816222fa-a596-3ed4-9f3b-8b5d20cf0a1f | -3.93567 | -46.43699 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e0f5056e-c57f-3d2f-b0f0-be2b353224f1 | -3.93338 | -46.42919 | 2024-10-24 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 5dc15eb0-75b4-3faf-ade3-b28cbead2120 | -3.29845 | -44.0845 | 2024-10-24 03:40:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c31fd1f8-3712-35b8-80a4-ab372b03b399 | -3.10566 | -45.23414 | 2024-10-24 03:40:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 138178d3-76e4-3f2a-b34d-57c4ad60d9f9 | -1.94355 | -46.55366 | 2024-10-24 03:40:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fd35784-76fe-3ccf-9e8f-beec258f5287 | -9.91882 | -36.28018 | 2024-10-24 03:42:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6a893230-b66a-372e-a5c1-cdd87989cc7c | -9.90283 | -36.27404 | 2024-10-24 03:42:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2a4575a4-cffa-3a0f-8f52-410209c67bbf | -9.64492 | -43.90804 | 2024-10-24 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| deb03bdf-cb84-3d93-b57b-effc646a0622 | -9.64395 | -43.91352 | 2024-10-24 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ec08b366-ae70-356d-9218-5b2a08f42979 | -9.6421 | -43.90865 | 2024-10-24 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bcb1cb18-6517-3a01-b479-4a7cf1adb6a2 | -9.64108 | -43.91417 | 2024-10-24 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 857eb5cd-4316-3f7b-aecb-ef4e7aa27b37 | -9.63727 | -43.90746 | 2024-10-24 03:42:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bb015c63-3697-36bc-be96-90f949268a8f | -9.17636 | -40.31775 | 2024-10-24 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90664358-4ea7-31b4-ba90-baecb008a9aa | -9.17508 | -40.32059 | 2024-10-24 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 295faf3b-1aea-3e2e-98d0-cdef17b78378 | -9.12497 | -43.15218 | 2024-10-24 03:42:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4df8d4f1-44ea-3ec4-841b-e0540ccd5d11 | -9.12325 | -43.15025 | 2024-10-24 03:42:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0731649b-3a37-3d53-9e20-297b0778d9b9 | -9.12241 | -43.15506 | 2024-10-24 03:42:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6e4f0790-03dc-30bd-b2ea-5d22fc773f55 | -9.12025 | -43.15155 | 2024-10-24 03:42:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 38f80c70-402f-3b87-9ecd-7e8893284c25 | -9.03474 | -40.58349 | 2024-10-24 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2f20e14b-614f-3d7b-93c1-2fcca57d5ee6 | -9.0333 | -40.5855 | 2024-10-24 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7994a572-c552-3ebc-8152-d3c588204c1a | -9.03078 | -40.58282 | 2024-10-24 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
