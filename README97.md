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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6060aa05-8643-36b0-8e17-638aa449be98 | -2.8018 | -51.01356 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5524baec-bfba-3bf0-9a9e-d5162c54f520 | -2.80136 | -51.01657 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 606b53c1-c617-334e-86bd-fb98b79cbab8 | -2.80042 | -51.01273 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7e846d8-db9a-3116-8c50-c659f8187d51 | -2.79994 | -51.01579 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 862a187c-ebba-3bda-9995-e398449deeac | -2.78663 | -51.36292 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8eb95049-8b87-3e6f-8080-f55a72168df7 | -2.7862 | -51.3658 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 61a78071-cd76-3136-9d4c-3255633b5f56 | -2.78577 | -51.36867 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e9746320-59ad-3631-b9ef-289639cf5faa | -2.78158 | -51.36217 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fa4f448d-c65e-343b-94bf-cf3855b3f165 | -2.78115 | -51.36507 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8cc63d22-6269-3077-ba11-ae8a4db7fb13 | -2.78072 | -51.36796 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| aa11a353-ba0f-30b0-873e-fac31203d8e3 | -2.7761 | -51.36432 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d25ef7e1-9020-32e9-adea-21d9f10859ed | -2.77567 | -51.36722 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d1d3ed4-d4e6-37d3-9b12-3a3d1d235607 | -2.77524 | -51.37012 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90a9a0be-dd77-32a1-a880-fdae75912b05 | -2.77063 | -51.36646 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3803b38-fe6a-3002-85be-e5e79eacd6cf | -2.7702 | -51.36935 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59f88c4e-f932-33de-a89d-a18653e45840 | -2.76977 | -51.37223 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 349a1e48-c11b-3342-a5f8-bcc2001a26ed | -2.64313 | -51.70464 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d870fe98-c126-39f5-9505-ccfc6d8864cd | -2.6423 | -51.71011 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32477552-b7d0-39f6-8d1a-a0d6c7a0bb8c | -2.58563 | -51.92088 | 2024-10-12 05:21:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd553473-bb80-3352-a4c3-cd3075d24754 | -2.32299 | -50.6368 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9098996-93c7-3a6d-a67f-5db6fcbd3788 | -3.33971 | -50.80793 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0448e7e1-afe0-392d-86a5-3b27b7825c0d | -3.33491 | -50.80393 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a810691-a99e-31da-97c1-01bb542e6dc2 | -3.33442 | -50.80716 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af14cda8-406e-355a-a93f-4ca68cb96bf1 | -3.30478 | -51.10952 | 2024-10-12 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc0e6613-1151-38fa-9d4a-d896a562d1d7 | -3.30431 | -51.11261 | 2024-10-12 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c39b2822-dcb4-3a97-9742-dabad2ef32e7 | -3.2866 | -50.94719 | 2024-10-12 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8042d532-bad7-3436-a174-b93d08fb956e | -3.28613 | -50.95036 | 2024-10-12 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b047e35-00a5-3cd9-a377-79113c31c899 | -3.28137 | -50.9464 | 2024-10-12 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3b78725-3814-37c3-92c9-7425176a40b7 | -3.2809 | -50.94954 | 2024-10-12 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40c3ef59-2564-35eb-8286-8f6d61acee98 | -3.28044 | -50.95268 | 2024-10-12 05:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 160169ae-dde9-3ba1-bf06-ca87672aa5f2 | -3.28005 | -50.77266 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6ec1cc7-c4aa-30ee-8d66-c519ae979245 | -3.27474 | -50.77192 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ddc47b1-c90d-36cf-9b84-0af38d51c8c9 | -3.27427 | -50.77515 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 599fa621-d46c-3e2f-966f-185adac95f34 | -3.27019 | -50.77401 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fe2d2ea-feed-361e-a239-934e7e934a63 | -3.26897 | -50.77441 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a98d45d9-dfb1-3add-8d8e-593df9b9a733 | -3.23732 | -50.84793 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46de55fa-0f95-3d0a-ab84-11a4e84059dd | -3.23684 | -50.85112 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdfde147-cef3-38bc-90cf-8d31cb0fdd3c | -3.23204 | -50.84727 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7838a9e-908d-3215-8450-5092b2f8b433 | -3.23156 | -50.85042 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfa4a4e1-90c8-3914-b772-f3e011125890 | -3.18773 | -51.24304 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3043311-59f6-3e01-b6b8-066b0be10935 | -3.18532 | -51.24064 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 241328d9-d3c7-37c2-9373-fe2515efb5a1 | -3.18488 | -51.24371 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 414ba84f-c275-33ee-bd5f-0fe4b047dafa | -3.18307 | -51.23921 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b244de1-4c7c-321d-b8b5-13402a1f6487 | -3.1826 | -51.24231 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41682c0b-b769-3125-992b-a86745c563bb | -3.17794 | -51.23851 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 568a03ac-1ef5-3eb2-9cb7-2dc2e2675a73 | -3.16792 | -51.30433 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 709b5d9c-d4e7-3bae-9ead-252ca791b155 | -3.16747 | -51.30731 | 2024-10-12 05:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 61cb3333-2b88-3f0d-978e-62e69c0ab85f | -3.03852 | -50.56954 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2930eccb-22ae-3c10-839b-6c6f0db55a3e | -3.03369 | -50.56532 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d00698d-4f6e-3a33-8f03-582ab1287992 | -3.03317 | -50.56878 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fb55d76-1bc3-3903-9f0a-a5627c0e449a | -3.02834 | -50.5645 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b58bc2e-4813-30a3-8cc3-e83be221078b | -3.02781 | -50.56802 | 2024-10-12 05:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ddf6355-fc00-3597-bd17-466b7a696bf7 | -0.41454 | -52.04928 | 2024-10-12 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4860a62d-adfa-39d1-9164-f642ea0e9e18 | -0.42232 | -52.06034 | 2024-10-12 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5495539-dd09-3f00-8a21-aca94a994a48 | -0.41768 | -52.05965 | 2024-10-12 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a841939-33f1-3954-8c68-8b26cd5dd62a | -0.41378 | -52.05419 | 2024-10-12 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8988dc4e-f3d7-3227-a804-5cf88cbb3ab3 | -0.40823 | -52.0286 | 2024-10-12 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fcba5175-8735-3edf-9de2-a014837a6518 | -0.40358 | -52.02792 | 2024-10-12 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6eb2dae-c896-3eb4-b97e-2e22b73f87e4 | -0.40132 | -52.02595 | 2024-10-12 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a708966-4d40-3694-ab89-28d95c3c5e2e | -0.39966 | -52.02244 | 2024-10-12 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51f2bf7c-241b-30be-b0b9-9557815d59b7 | -0.10396 | -51.65607 | 2024-10-12 05:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a82a1ef2-5187-3a29-80f1-c19943068558 | -1.89726 | -52.49367 | 2024-10-12 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c3517fb-62f5-3230-bd7e-354ba696bb0d | -1.60082 | -53.34289 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2f50f086-4bd6-3a0e-adbe-a585ac3fea31 | -1.60021 | -53.34696 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b5d88901-ff28-3a12-8a2a-1a784289a585 | -1.59651 | -53.34223 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5ebf1ad-c7d2-3a78-9d14-f4e85a55116c | -1.5901 | -53.34295 | 2024-10-12 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e590f61-6d91-3b6a-b34b-ba5f6d4be935 | -2.98455 | -52.90145 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0c510be-8365-34d3-a3a6-c14d571d1037 | -2.98385 | -52.90611 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bd1a320-0acf-3f85-a07c-a9d13140339f | -2.98316 | -52.91073 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 770e4cd6-4f16-39c2-ab75-abd8006efff7 | -2.97931 | -52.90536 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0190ab4c-cf12-3ac3-92de-127fc189b5c9 | -2.97861 | -52.91005 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de0e933f-5d65-3a6e-9dea-9c223b27caa7 | -2.97546 | -52.9 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68e1d2b8-66bc-3971-9d54-c06816844de9 | -2.97476 | -52.9047 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e7c3a4f-8841-38ca-9b5f-a5ae20c3fe04 | -2.97406 | -52.90937 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef83b113-b28b-30f6-ac89-4214a61f1a6d | -2.97021 | -52.90405 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef09f5f2-47db-3c45-8400-ecad60b05255 | -2.96951 | -52.90874 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d53069-7d58-369e-bdce-a0e47ad484a1 | -2.96565 | -52.90345 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0d9e2ed-b3fe-34e0-a929-c6ac22ac6bcb | -2.96494 | -52.90816 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70b6e98b-baac-39bd-9c60-526572fd6b92 | -2.96109 | -52.90281 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 722efbe3-1193-3448-83a6-b66fd8b7f8ea | -2.84883 | -52.93469 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36c3b82e-3a47-39cb-a760-c1dff753450d | -2.84816 | -52.93918 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f83d3c9-d00e-34dd-b91d-cfd9936a4fe5 | -2.84431 | -52.93394 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5f9cc5fb-b8d9-3f31-8075-7be276b98f9e | -2.84363 | -52.93849 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 05846dc3-1dd7-353a-91e3-b73be1b14a53 | -2.8409 | -53.32048 | 2024-10-12 05:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e6c1aab-03e3-3a5d-b149-170881b68805 | -2.78257 | -52.4829 | 2024-10-12 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6557e97-2e94-3bda-84a2-b95954544f41 | -2.7806 | -52.48093 | 2024-10-12 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 855bf695-545c-3a9b-823a-71d3246bd672 | -2.77989 | -52.48581 | 2024-10-12 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dd4326e-0b3f-3f09-8848-31bb4eded8f5 | -2.7779 | -52.4822 | 2024-10-12 05:21:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66c0c0b6-2ad3-3633-972a-42bd8868274d | -2.74425 | -52.45217 | 2024-10-12 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6429d454-2bc6-3164-8c2b-c9c35bab15e5 | -2.68495 | -52.43286 | 2024-10-12 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 444feeae-8aba-38bd-a532-e7d2c34c6c2b | -2.683 | -52.43546 | 2024-10-12 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dc6276f-d857-3321-ad8f-e75bfe057a27 | -2.67655 | -53.34084 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b29bf9-3b1f-38bb-b461-279a57c7a665 | -2.67592 | -53.34509 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d6dec9b-a2b1-320b-b55f-91599859d5fd | -2.67529 | -53.34932 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6f6691d-1640-36bb-9973-26372295d7c4 | -2.67216 | -53.34016 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 423ddee4-d1e0-315d-81f4-74f7bb021a16 | -2.67153 | -53.34441 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fe28bf0-319e-39b1-9cc2-ab8f632093cb | -2.6709 | -53.34864 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90b60215-26d5-3d89-9760-e9c8021db797 | -2.67027 | -53.35287 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1672e9e-41f5-36eb-859d-b9c586af6ad7 | -2.66714 | -53.34373 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b62bdd1-cee1-3e5a-828a-992e948b1d45 | -2.66708 | -53.34425 | 2024-10-12 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README98.md)
