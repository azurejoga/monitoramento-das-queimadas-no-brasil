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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1863ebe8-5e0c-335b-be8b-bb6615f87d96 | -8.93207 | -66.90063 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b2e160a-51c0-336c-985d-d031892b8eb8 | -9.91394 | -65.02768 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b404605a-4195-35a9-8d93-cb186bf7116c | -9.78259 | -63.80986 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3510250e-96ad-3639-acb3-bd703611bbce | -9.01009 | -65.93971 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 28017300-9b99-3abf-b78f-b2adf60709ba | -8.85199 | -66.79239 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 746b5463-11ee-3379-93e7-6416a5c7b9bb | -9.81054 | -67.59608 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 136e3014-840d-3668-ab54-b5611f6787ae | -10.07781 | -66.9084 | 2025-10-22 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 300b745d-c599-31a2-b7b9-0baf26d3db88 | -8.93311 | -66.89336 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76e3c805-42b1-34c3-a82e-8f68c5b6e112 | -12.3807 | -63.87665 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79f605cd-131a-3a91-aa73-2eb7c7abe91b | -12.1327 | -63.21008 | 2025-10-22 06:08:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a8bd5b7-a3ae-3af6-9295-5fa9ec390e6d | -9.72402 | -67.47224 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 58b236ee-fa1e-32f8-b526-42bbb3e75fb3 | -9.89806 | -63.58696 | 2025-10-22 06:08:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90b2d46b-c001-334a-a866-453aa7f87ef6 | -9.55135 | -66.6465 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58823eb1-5050-3fe7-997d-581c351dee34 | -9.11537 | -65.93683 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 783ecd69-938e-3668-9a05-ae008449ad70 | -9.0103 | -65.94076 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 013f97a9-1546-37ec-bc44-7520860c1551 | -9.01102 | -65.93494 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b95c1a24-00d2-3833-9e46-4480da24371b | -8.99906 | -65.92129 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0443829a-c7ea-351b-9aab-af9080af526d | -9.01175 | -65.92906 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d154d212-eba2-3d0c-a8bd-b913abbf91b2 | -9.00504 | -65.9281 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae454b65-c933-3812-b379-c43bdf55ce76 | -9.00431 | -65.93402 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5c4cecee-8370-38e4-97bd-1bf642d712cc | -9.00358 | -65.93988 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7298ed99-7ee0-35f8-9182-e6cb5336edf4 | -9.00957 | -65.94654 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 632855c8-cfb2-307f-a123-785ee3c3e16b | -9.00577 | -65.92222 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| def429b9-edc9-3cc5-a8d8-04b0f032646b | -9.01249 | -65.92316 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa6c98e1-ee04-352d-a9f5-55dcf86b1d32 | -8.99235 | -65.92036 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ba00275-752c-3e8c-bf19-e9f083ab1712 | -9.10863 | -65.93613 | 2025-10-22 06:35:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1286ebcb-a972-33ab-8fbd-bac9d9b37dc3 | -9.722 | -67.47487 | 2025-10-22 06:37:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7297d203-a91e-3a89-97f1-2ad0e9d58bbe | -9.7298 | -67.47461 | 2025-10-22 06:37:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59cb2b6c-d0af-384c-9c9c-4cff34055a9e | -9.09189 | -67.69516 | 2025-10-22 06:37:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 130ae072-7855-3544-a551-477e5e7c39a4 | -9.09246 | -67.6907 | 2025-10-22 06:37:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b23a646-5480-3a83-b5ff-e0bfcc0be5e1 | -9.72361 | -67.47395 | 2025-10-22 06:37:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8412b69d-5e17-35ef-8669-0e824d87ff2f | -9.71468 | -67.48347 | 2025-10-22 06:37:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e31ca5c-dc77-3987-9d7b-0cbe5ec9b992 | -9.72085 | -67.48421 | 2025-10-22 06:37:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 148e3e12-885c-3b11-8aed-c26e2e53bf6d | -9.72918 | -67.47932 | 2025-10-22 06:37:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc3fc6d2-ad19-3137-8435-08dfdfa4f14c | -9.7276 | -67.48026 | 2025-10-22 06:37:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02d1251a-33cb-3caa-aa6f-068b3e44277b | -9.72818 | -67.47552 | 2025-10-22 06:37:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63b7e5f0-de00-3e95-b0cd-efb334fdca6c | -9.73253 | -68.88818 | 2025-10-22 06:37:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc6b6f5a-da01-3309-bf3b-236370e88fdd | -9.73302 | -68.88442 | 2025-10-22 06:37:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bd0a8b3-6a15-319e-9dda-6ebb4bf7818d | -9.723 | -67.47866 | 2025-10-22 06:37:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5833b40-8e39-3d3a-be70-3f16863db181 | -9.09849 | -67.69153 | 2025-10-22 06:37:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c50539d7-d28c-3088-bd29-2a9cda66a665 | -9.71623 | -67.48258 | 2025-10-22 06:37:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2f717ca-d205-3577-a380-53dfff81465d | -9.09303 | -67.68626 | 2025-10-22 06:37:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0986841d-0b51-3c88-ae48-b4f970ff3d94 | -9.7261 | -67.46727 | 2025-10-22 07:18:00 | AQUA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2d1e2418-0e39-3120-9ba4-2085e6384155 | -9.56957 | -65.22009 | 2025-10-22 07:18:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d79cb943-822e-3ca7-94fd-a9caeee168ba | -9.72474 | -67.47617 | 2025-10-22 07:18:00 | AQUA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2a0fe0d7-a877-322f-9b51-f828e0977a78 | -9.09049 | -67.68417 | 2025-10-22 07:18:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0ca89c47-bd16-39de-b468-ee3f8018f57d | -12.13355 | -63.21212 | 2025-10-22 07:20:00 | AQUA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c02641d1-2e96-3a7e-bc14-d15611264072 | -17.9676 | -51.0813 | 2025-10-22 10:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 243.5 |
| e0f0c9e4-a446-34b9-8475-a8233e243ce2 | -17.9676 | -51.0813 | 2025-10-22 12:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 9af317cc-1926-34c7-a04b-ca0174fc7c73 | 0.21644 | -51.10683 | 2025-10-22 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3defc919-6017-3adc-9882-a6cdb120756c | 0.13051 | -51.08911 | 2025-10-22 12:34:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ce2950a1-20aa-3f5f-8c02-9ab5ae681bf5 | 1.17444 | -50.77169 | 2025-10-22 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b3342846-fbb9-35ff-8208-fcaae9f9a884 | 1.73221 | -50.92432 | 2025-10-22 12:34:00 | TERRA_M-T | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 4493babe-df82-3580-aef0-f6464d2a6775 | 1.66985 | -55.73397 | 2025-10-22 12:34:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 13ba55fc-a1ce-3b31-ab12-3e236f869e92 | 1.74101 | -50.9231 | 2025-10-22 12:34:00 | TERRA_M-T | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a4a14e77-88b3-3d9c-b643-dcebcc4c96e7 | 2.17122 | -50.91006 | 2025-10-22 12:34:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f4a99025-c162-3050-ad03-3acdb34afb95 | 1.67189 | -55.74055 | 2025-10-22 12:34:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| de0f3afd-18c8-37fd-99a6-809dececb6ff | -3.25489 | -50.12765 | 2025-10-22 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3c7a29d5-c5f3-37d3-9777-e1fa3b48c5c0 | -2.81021 | -50.27081 | 2025-10-22 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7ec90b08-938f-3c1b-ba99-a47965a18a9a | -7.07883 | -45.21083 | 2025-10-22 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 610c4f92-d0d6-3b74-a1ff-11d8eadc9791 | -1.5874 | -46.95466 | 2025-10-22 12:36:00 | TERRA_M-T | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 24ca6016-d3c0-36a1-9a2d-a671094cd3bf | -6.99949 | -42.78899 | 2025-10-22 12:36:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 52.5 |
| 6fae4d5d-ef33-3b89-919c-1cf4947c7341 | -7.41644 | -45.20493 | 2025-10-22 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 428a57ef-d128-3b20-938e-7f31c7d4df94 | -7.65636 | -46.88182 | 2025-10-22 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f1ec9361-6c65-3180-86ad-0f45a326e759 | -2.87623 | -50.71423 | 2025-10-22 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b07555ff-3f3f-35d4-81a1-52e40107ad02 | -3.40826 | -42.49121 | 2025-10-22 12:36:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| f6aea47f-6a5b-324b-8bfb-bfd8dedbce52 | -3.81842 | -50.76794 | 2025-10-22 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 25e03d58-2b23-3617-80a7-df1017522514 | -1.44302 | -47.16726 | 2025-10-22 12:36:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 1f14e189-dfa5-3c53-b7ce-5fee15a494d1 | -3.25354 | -50.13711 | 2025-10-22 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 664db9de-b006-3eb7-a57c-4968b2566a15 | -3.02672 | -49.45041 | 2025-10-22 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 22a07243-d87f-3247-bc31-3f21bbc946b1 | -7.07934 | -46.19541 | 2025-10-22 12:36:00 | TERRA_M-T | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4cfabc3f-c563-3918-94fb-20014d9e601d | -4.71111 | -48.58128 | 2025-10-22 12:36:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 2baf7584-0286-3b6d-b74c-11854497ee1d | -3.82471 | -51.05133 | 2025-10-22 12:36:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 27eb2f39-fdb6-397d-93a4-cb3a6970e4a6 | -1.43226 | -47.16571 | 2025-10-22 12:36:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5ae3b284-c612-3494-b9b1-cb376221f406 | -2.11775 | -47.10687 | 2025-10-22 12:36:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b4c88aa9-7574-339f-a888-1a2240aecbe9 | -2.94989 | -49.34064 | 2025-10-22 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1d783064-c96c-385c-8ba7-90ca2ca09941 | -7.6587 | -46.86396 | 2025-10-22 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 44dd26a9-03e8-310e-b577-7242448f9d32 | -7.40246 | -45.20324 | 2025-10-22 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| eeb0aaa7-aab3-37b4-af21-76b045165ee2 | -3.14821 | -50.16417 | 2025-10-22 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| e97e06ca-ee61-36a2-82d7-afd57b571a56 | -2.80891 | -50.28009 | 2025-10-22 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3950cb8b-90d8-3339-9f17-104c920ea607 | -2.86346 | -50.74 | 2025-10-22 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 596d1322-476e-3cde-b857-2d08c11661dd | -3.40075 | -42.48508 | 2025-10-22 12:36:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| d7abf9a6-afb0-337c-8f61-584ee2990f5d | -2.85454 | -50.73876 | 2025-10-22 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ec6927c6-a217-3ad3-b91e-cf9a34c5c4c3 | -3.02531 | -49.46048 | 2025-10-22 12:36:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c85f1fca-029a-395a-9610-3f54cb389d26 | -1.43038 | -47.17913 | 2025-10-22 12:36:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ddee6647-639f-3529-a933-17ac3a0db5dc | -11.98364 | -49.77706 | 2025-10-22 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8fdc8f7e-178b-3ee0-a4a3-1d3ef3ea7254 | -12.08339 | -50.35536 | 2025-10-22 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e9f59049-5f64-3b07-ac7c-02dc6bd7a90f | -13.94981 | -54.48862 | 2025-10-22 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b7ddb09-f85f-3078-87c7-4a11cefbbb53 | -11.97575 | -49.78307 | 2025-10-22 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 778631c1-c7b3-330b-a56f-95426ec047e0 | -12.73632 | -47.63834 | 2025-10-22 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 3d401e11-6bd2-3c7e-b6b5-cdee990669fb | -12.08182 | -50.36705 | 2025-10-22 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a8e84209-fed4-3a41-b503-d363f1c7aa93 | -11.99288 | -46.77217 | 2025-10-22 12:38:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 43d45ec3-0c0d-328b-ab0b-093ec53fcf59 | -11.98952 | -46.77736 | 2025-10-22 12:38:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7b30de81-74e8-3e75-b7aa-8127e281997f | -11.89072 | -50.11212 | 2025-10-22 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cf90d760-4910-36d6-bc07-a06890c89174 | -17.6167 | -46.614 | 2025-10-22 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 0f400029-77a1-3efc-9385-ea50d239ad2a | -16.25268 | -51.81077 | 2025-10-22 12:40:00 | TERRA_M-T | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9865d9d2-7802-30ca-a127-9a52ccd06ce3 | -17.23438 | -52.25766 | 2025-10-22 12:40:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 82ac7e35-aad0-3677-811d-0a53df8ca51c | -17.96317 | -51.08976 | 2025-10-22 12:40:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5a11dc5e-64b1-3775-8473-09640e7d42b8 | -16.52645 | -51.0191 | 2025-10-22 12:40:00 | TERRA_M-T | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 996d6f28-8c44-3cde-a328-5d6f31339868 | -17.41577 | -55.07333 | 2025-10-22 12:40:00 | TERRA_M-T | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |


[Clique aqui para ver as próximas entradas](README22.md)
