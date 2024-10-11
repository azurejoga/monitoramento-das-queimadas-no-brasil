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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b69cb7d-d61a-30ae-b366-a1254af42a9a | -3.44533 | -52.71905 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55014f59-d7c9-3b9a-8cf5-e49ccf1f9ce4 | -3.32774 | -53.00734 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 875d01e6-b148-3293-8bfd-0965c58706f0 | -2.98513 | -52.91204 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 0c769135-6322-3bca-b416-46eb99b1ef15 | -2.984 | -52.9155 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 514c9d46-45fc-394f-9f3b-5cd517377f16 | -2.98038 | -52.91122 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| beaa0a2e-5624-3fe8-9f67-cee34d7c8c83 | -2.97647 | -52.90548 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 445d8c35-e281-3924-ab9b-b1f7d558492c | -2.97611 | -52.90382 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 09d0183d-e049-3568-85c4-26f865f09485 | -2.97057 | -52.90796 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f88de30a-3184-3a82-a68e-04e9d2559c54 | -2.94677 | -52.55257 | 2024-10-11 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 317439a8-1568-3f69-b8bb-246dd55ec89e | -2.8527 | -52.90835 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bda46ac-23ab-3af4-8d19-cf789aa91300 | -2.84778 | -52.93883 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b989297-38cf-37eb-acd9-d1dc6a88970f | -2.84712 | -52.91262 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beabb467-c1ca-3ae1-b29c-022736a04bf5 | -2.84238 | -52.91175 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c34d693-0b85-3072-a3b4-a2f96051e356 | -2.78412 | -52.4871 | 2024-10-11 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d0c6240c-5443-385d-83d6-c14ab77c0b08 | -3.44653 | -52.72348 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fa341ed-4a9e-32bd-ab21-59f0d27e1b21 | -3.32385 | -53.00134 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 247f1367-781f-3faf-90a5-3b931bc782cc | -3.32301 | -53.0064 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08b9d641-96c4-3956-abe3-ad571188f2b2 | -2.98598 | -52.90699 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| c5d43fca-5f59-38e4-a68e-76f297969656 | -2.98481 | -52.9104 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| ca2115f4-9a3c-3c0a-b0fa-4327a1bce5c8 | -2.98086 | -52.90462 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 0b50a164-b0fa-3cbf-96dd-2197e4cd8cb4 | -2.97731 | -52.90052 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 38a3185c-2d07-3ef4-a39d-f92a63db0c56 | -2.97531 | -52.90879 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 884c664f-f615-38ba-81fe-ef03a4ae79d3 | -2.97451 | -52.91381 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| aee4a73d-b167-3c90-94c2-88515549362b | -2.97089 | -52.90963 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3bd73a4d-6386-39e2-a546-cf0a8f48394f | -2.97004 | -52.91467 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 876b9778-e5ba-3b20-8990-932cc69b19f7 | -2.96977 | -52.91296 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| db58199d-fc5f-39a3-a726-949328cf87ad | -2.96664 | -52.90211 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c287186b-988c-3e26-8f89-fbb6b9713553 | -2.96584 | -52.90705 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 893dd9f7-ec9c-3241-b6f4-e5540a13a65b | -2.96504 | -52.91198 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fc342e63-cfbc-3619-b854-1b93a3564224 | -2.9619 | -52.90124 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 98ecec46-be76-38fe-8ec1-6c2de9c8a2fa | -2.9603 | -52.91112 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7fde3159-2c0e-3597-9e20-9d4db1032532 | -2.95143 | -52.55321 | 2024-10-11 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95490e0c-ffe4-3102-9237-e0e099d64571 | -2.84692 | -52.9442 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2acccaee-de63-3b3e-904d-440865292071 | -2.84302 | -52.93804 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1e1a94c-399f-331e-8c0e-9a79e6144b52 | -3.3538 | -53.37921 | 2024-10-11 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4975a451-e01e-3d9d-adb4-6706c62d6dc4 | -2.67825 | -53.35323 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7f0275b-8d00-3d8f-81bd-bd92dfdf2555 | -2.6751 | -53.34138 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 256c836f-f04a-3629-ae3e-c9070c976d5a | -2.6684 | -53.3516 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e7632fcc-c78b-367a-b3f5-22287b7657bc | -2.66438 | -53.34526 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f8546695-fab5-3568-9f14-12836d4802f1 | -2.66259 | -53.35632 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1620d529-f332-35a1-8ddd-4205a83d9319 | -2.65856 | -53.34996 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 26971fe1-011f-3c00-920a-d7802ec094bc | -2.65766 | -53.35548 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| e50b6688-f872-3693-a166-61fb36b5c090 | -2.65274 | -53.35466 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 017f74e6-1fc2-36cc-9743-e48cf1cbb38d | -2.78028 | -52.48151 | 2024-10-11 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1d7d7056-5efb-3ebb-bd80-4807917f7bfa | -2.7795 | -52.48631 | 2024-10-11 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d8ea80a7-45a1-314d-a66f-70b79c730ed2 | -2.77566 | -52.48076 | 2024-10-11 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| fe630a91-d20e-3070-91a4-d9d9d795d3f7 | -2.77487 | -52.48556 | 2024-10-11 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5de5cd84-f76f-3379-82d3-bd7b5295d08d | -3.83354 | -52.33154 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad8d61cc-03f2-3067-a094-3d785f7bf8c6 | -3.72608 | -52.36517 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b6f321e-714b-3427-8ee2-00dd3901e294 | -3.83493 | -52.33485 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75379cf3-ac17-3ef7-b428-2cc06252ef86 | -3.72448 | -52.36711 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4223324-25ab-3a0a-b5a1-ce10d4014f39 | -3.98288 | -53.43373 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa60276-d6b2-365c-9e9d-c78656c73ca3 | -3.97985 | -53.43195 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8dc1a96-a54e-300e-b829-a0370d2ab9b7 | -3.90705 | -53.57055 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2995d02a-5988-309a-8cd9-ab9f9bfb9d3c | -3.83283 | -52.3359 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f393dc8-f7e1-3609-a381-96eafc1740f6 | -3.97804 | -53.43291 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 162a2737-d4d4-336d-a245-4149df3a55be | -3.82893 | -53.58549 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eef87782-ec68-33d6-810a-67ab76916260 | -6.37714 | -53.63401 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed9c600e-f2bc-3696-a4db-85f8b147d4f2 | -6.19198 | -53.36695 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bbff6880-7459-3db0-af2c-3e90e63d372b | -5.6935 | -53.63522 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce2704dc-a7eb-3962-9e16-8f1e0d8ee010 | -1.59156 | -53.34651 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3975233-e699-3343-ba50-107784345dbd | -1.5911 | -53.34942 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c804d60f-5e05-3815-869d-11ed4e339f7f | -1.58657 | -53.34564 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd926983-fbae-3402-bc8b-9879e1e21e89 | -1.58611 | -53.34853 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55cfa9ab-6f17-35be-b396-e77594b4a24f | -1.1858 | -53.3852 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4d9234f-609b-34b2-8a54-d0f71c2d9ae4 | -1.18534 | -53.38814 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b37857dd-bef6-31f7-9ce9-a808a2f944b6 | -1.1842 | -53.38724 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44c15fd6-f57d-3e32-b828-8ae961ce4200 | -1.17867 | -53.38935 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddeabe80-91e9-3149-8578-fe70ed86da17 | -1.17525 | -53.38637 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd8d0dfa-d6a9-3fa9-8156-3ad4312396cd | -1.17479 | -53.38932 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f4eab2b-378c-3fff-a1d1-934f21ed5932 | -1.17433 | -53.39225 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0899450a-66e0-3503-a6ff-bf2e1e439145 | -1.17364 | -53.3884 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd973ad1-f573-3dc2-a2bd-056b0ad8840e | -1.1734 | -53.39817 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bee958d3-e971-3d74-b9df-f490fd229ff9 | -1.17316 | -53.39134 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0387f484-30cc-345d-9935-902fd1754f39 | -1.17294 | -53.40116 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 083cf671-66f4-380c-9543-c1794d2e6e89 | -1.17247 | -53.40415 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6ac29f5-2626-3404-aef3-bf2db075451c | -1.17219 | -53.39723 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7486a98b-3293-39a9-a3c7-5044da89de0e | -1.17201 | -53.4071 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d4db447-f64f-3eae-95de-2a7bbbcde621 | -1.1717 | -53.40022 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ff3dfc9-bb2c-3797-af9a-057693e24746 | -1.17121 | -53.4032 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 020085ff-bc1e-30b4-84bb-531242ffc780 | -1.17072 | -53.40616 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f112cbb5-0387-3d96-890a-81f6b3dc02d3 | -1.16284 | -53.39937 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aca68c54-7cff-3bcd-8ba5-6e6bdeca277c | -1.16237 | -53.40235 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 977df964-0c12-3197-b0f3-51cb0fe501a5 | -1.1619 | -53.40533 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a10fbc4-4493-3b1b-ab1e-e319817ae698 | -1.16143 | -53.40833 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f47acdd6-07a0-3032-be4c-d46f0adde060 | -1.15779 | -53.3985 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c276402-5d1c-35b9-9967-152d996153a4 | -1.15733 | -53.40142 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cacdac50-65af-3257-b758-6855c6e31895 | -1.15686 | -53.40437 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17cc3e12-3336-34a8-920b-45d1107c0031 | -1.12571 | -53.63545 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| edaa151f-d5f9-3abb-ae57-f2e3c29ecd4e | -1.12523 | -53.63849 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4744a33d-7744-3e38-aa97-57f4fe4c482e | -1.12474 | -53.64165 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b947d9d-d541-3f2d-95be-89c6911c7717 | -1.12424 | -53.64484 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc217c37-6541-3993-b0de-a28f49e60073 | -1.12399 | -53.4477 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e79642b5-fee1-349f-b928-738067b5d1bc | -1.12352 | -53.45064 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9364d980-d516-3e0d-b851-c0b0cbfdc53a | -1.11919 | -53.64331 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34b49705-53c1-3f11-8eee-522510db14ff | -1.11279 | -53.61708 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 918aac3a-e829-38e7-b2a5-ad37c0646224 | -1.11233 | -53.61994 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1169f28d-1054-3877-91a1-117dd294ce60 | -1.11187 | -53.62289 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8b37091-3be2-3c1b-bdb7-8dd96a502422 | -1.10713 | -53.61954 | 2024-10-11 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c0ae0bd-ad41-30b2-b10d-a73cf66688a8 | -1.02615 | -53.72772 | 2024-10-11 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README52.md)
