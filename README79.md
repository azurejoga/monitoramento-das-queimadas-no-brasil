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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6cbe118-50ae-3644-b91d-9ffe8b26c260 | -9.74791 | -53.1755 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a31d5459-d101-31f9-a047-0468245546e6 | -9.73305 | -53.19437 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd998d47-fa77-34c3-b438-b43ee98d4134 | -9.72909 | -53.19377 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a431762-0695-37be-912f-d9086008a4b8 | -9.68592 | -53.49551 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2656396-b3c0-3cad-b82b-b435b6468620 | -9.68521 | -53.50048 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ffa15f70-859c-382a-94b9-2f6f3740d1ab | -9.57184 | -53.42727 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aa099247-395a-35ed-8a02-da8cafc3dd2a | -9.56224 | -53.41081 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35b55f5c-2ad6-3976-a25b-0c4bb0a76a09 | -9.55833 | -53.41025 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 11b62117-40e5-3f3b-a498-c7bcd45b470f | -9.40051 | -53.19828 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b4e3261-2bd0-3c0a-aa3e-3f559f6a3a16 | -10.75776 | -53.55393 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d002ab35-6a4f-3f9f-9535-94b1451a33ec | -10.05553 | -53.34686 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22f69f74-d158-3540-9b03-6e345d2e4473 | -10.0548 | -53.35195 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79ae58b7-683d-307c-86c5-5051bfae288b | -10.05378 | -53.33101 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efbb066e-3bdc-3ae3-bca7-c879d8d446b2 | -10.05306 | -53.33604 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbeabfc7-1719-31bb-b48b-ca2ca0f8bc80 | -10.05232 | -53.34115 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db1717a8-09a1-3860-a0fd-1d30e37a6211 | -10.05086 | -53.35131 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7d1c8a4-7354-387b-ae8b-a3ac8a1fff24 | -10.04909 | -53.33559 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32eeaec4-0cb5-384d-b40d-b06117e1b6cd | -10.04836 | -53.47965 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7a72719-e07f-31b9-ab4c-ecba80cbfecc | -10.04519 | -53.47403 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f20f38f-eb64-38a6-a117-14a2e3f65f36 | -10.04243 | -53.43774 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 34de4eb7-8dc2-3b45-bd6c-236ff18051ab | -10.04128 | -53.47345 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 602eac61-2982-37bc-9042-51abe620b626 | -10.03998 | -53.42702 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 7d652f9b-7f3f-388d-a2c9-fa2678791f67 | -10.03925 | -53.43208 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 11f5b205-1723-3e9b-9584-538884c9d5b7 | -10.03852 | -53.43713 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a7921f61-2fdb-3e6c-a19f-11054ce61bd6 | -10.03779 | -53.44219 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f651b4c-4a2a-3f7b-8490-8ac8e8539b72 | -10.03605 | -53.42646 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 963d6ae7-cd79-3fd5-8e84-369028daa653 | -10.03532 | -53.4315 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 96f25744-7617-3b79-b0db-87df749f543d | -10.0346 | -53.43654 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 62cffd7e-9522-37e2-8c3a-a2f2789e4226 | -10.03387 | -53.4416 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ea29524-5949-3407-8e48-3a05f3faa4db | -10.03285 | -53.42081 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| ea5fc627-f235-32a6-b7cc-8243d0a5f8e7 | -10.03213 | -53.42587 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| fd128667-50b6-3ea0-b3da-bc6dbcd9ce83 | -10.0314 | -53.43091 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 3b0ca9fa-3e91-3aac-85ce-051b5ce673f3 | -10.03068 | -53.43596 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f8caed85-ac55-3e14-bf33-85e4da420206 | -10.02996 | -53.44101 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ee16748-a81e-3d95-b366-d8b3aadd6770 | -10.02953 | -53.47182 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e35e8def-8d26-3ac5-a372-a48206ddb5f4 | -10.02923 | -53.44607 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e47c125-c6fb-3181-a88a-da6b63c0bfe1 | -10.02881 | -53.47682 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d9f6f75b-ce7a-3954-aaee-61d2e40148a7 | -10.02821 | -53.42529 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0ad77372-9578-3483-9e6e-da4fbd4c0119 | -10.02809 | -53.48182 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 76d4a938-aaf4-35ba-ae51-8d9d5fcbb8e4 | -10.02794 | -53.34272 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89ad332d-9a67-3470-9759-e041a4274a71 | -10.02748 | -53.43034 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 3da23b59-9fe0-3cde-b9bc-e845743321fe | -10.02676 | -53.43539 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| f08467cb-3305-35b5-b854-8bd2b357aee4 | -10.02603 | -53.44045 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c22f2ff4-10cf-38ef-89b9-597efe14551b | -10.02561 | -53.47131 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a12c0d89-4333-3c3d-b7e7-67fa2df3a771 | -10.02531 | -53.44551 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36047db5-5fde-38eb-812f-74d64635d692 | -10.02489 | -53.47631 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b268d64a-b8af-36e5-a3b1-521c85ca1340 | -10.02428 | -53.42474 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 48b53ad2-1a56-3026-806a-a9e557fd03ca | -10.02417 | -53.4813 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| f15eaca1-f1b1-3ebc-ab36-3e6ea04cfe3e | -10.02356 | -53.42979 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| a783174e-a953-31e5-938c-7f515f60a112 | -10.02284 | -53.43484 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| e05d03e3-6300-36cf-b543-3181f199a80d | -10.02211 | -53.4399 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0bdc00a-5868-35bc-a0d4-38275edf855d | -10.02189 | -53.30006 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a19804d-31a5-30ab-b337-43ac1251b36e | -10.02169 | -53.47079 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41d33419-ef6a-3dbc-a9d1-73c0520f68fd | -10.02139 | -53.44496 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a8b3e84-06bf-3143-9b73-f100111c532b | -10.02097 | -53.4758 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6b4e9c6-8dfe-3976-aad8-47dd61c7dbe5 | -10.02035 | -53.42421 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bf2689b-7867-3bdd-8e12-e34df5503b53 | -10.01963 | -53.42925 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e9aa60b-5383-3500-8980-480798029d5f | -10.01891 | -53.4343 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3165418b-46d0-3b70-b4bb-9c30e39ce4c1 | -10.01747 | -53.44439 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8f6de8f-a3f3-38a6-ae55-4eaf7919b858 | -12.25987 | -53.43849 | 2024-09-28 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37b94e8a-fece-3194-94a1-1411683865ad | -12.86472 | -54.0111 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 021110e7-da54-3a14-bc0f-ce5d3c5b30c3 | -12.86401 | -54.01624 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51db4943-177c-3f3d-bc89-472ddb1fe3ad | -12.86079 | -54.01053 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9e48548-34e1-3f00-9d1b-e24a1c58b52d | -12.80879 | -54.01248 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 06fa27c8-a9f2-32cf-ac3a-bf380ceb8493 | -12.8083 | -54.01336 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5c86dcf3-7eac-313c-9022-b1e0dcdc708f | -12.80486 | -54.01189 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a2d3a762-4e62-3ece-a61a-4a6b17f48e5b | -12.80437 | -54.01278 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 631fb547-16fe-3327-aac8-c80f5d6c6954 | -12.80093 | -54.01133 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b07e554d-1fbd-325c-b975-d8d16f6882fc | -12.80044 | -54.01221 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1dd1cecf-46e3-3489-949d-4a66b747f41a | -12.797 | -54.01079 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 89954553-a07e-3884-9e44-ee6392b491e2 | -12.79651 | -54.01167 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 98d8bd60-09fc-3f19-b01a-ffd67243e61c | -12.79628 | -54.0159 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ac2c166e-c032-3743-84f2-25494a902bf5 | -12.79582 | -54.01678 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 36a5c38b-333f-3e78-899d-fcf3408025e6 | -12.79307 | -54.01023 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ebf5ed07-bc75-36bb-b0d9-cc0d5266b019 | -12.79258 | -54.0111 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90cefec3-e7ee-30fd-9328-52743491330d | -12.79235 | -54.01535 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c9f05ef-dffc-3fc5-b7f5-e6670caa1e54 | -12.79189 | -54.01622 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f073647e-9beb-3c2b-b976-7ecea73d8073 | -12.78842 | -54.01478 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22f9671c-64cf-36c9-a0fe-667b7346c10e | -12.7877 | -54.01988 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8df15492-ffeb-36d9-9144-a7f679869e89 | -12.78449 | -54.01423 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| a5fad432-0102-3811-9115-00d9b48a1af1 | -12.78377 | -54.01931 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 3848428d-226e-3920-85ac-f4b15f4a0454 | -12.78057 | -54.01366 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 6b89fc9d-b80c-38e8-9f69-6eea45c02e2f | -12.77985 | -54.01875 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 5c6abefc-bbe4-3f0a-a6c4-63b2c49406ff | -12.77913 | -54.02382 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f7b6a56-0e4f-3544-8efb-a25205fc9dd7 | -12.77664 | -54.0131 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 532bc892-4619-3523-bd4c-5cc9780dccb3 | -12.77592 | -54.01818 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0cac821f-4bc1-3262-8308-57a05c06fc70 | -12.77521 | -54.02325 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 207f51c4-2ba1-360e-a3e4-c645ffe1f761 | -12.77272 | -54.01253 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 77748c19-8280-3298-bb6d-072b0d31ec17 | -12.772 | -54.01761 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df5da380-f481-3e78-af2a-c41a7f93b552 | -12.77129 | -54.02269 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c2ce7189-bd65-3f44-bc70-4a954b67fbad | -12.77057 | -54.02776 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 50121843-3c05-3e5e-a5d9-258f0d5c6f73 | -12.76879 | -54.01196 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83977ed3-521c-3f8b-8f57-fa2d6b90673e | -12.76736 | -54.02212 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3bbcb895-790d-3109-8667-4ae5c3226870 | -12.76665 | -54.02719 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a2f2e4bc-64dd-37c0-85c8-dbef17c81276 | -12.76273 | -54.02662 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 614f2a11-29a2-3575-961f-e931e3858a28 | -12.76202 | -54.03169 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d8a13dc-d64e-3797-9316-181a7432fee1 | -12.7581 | -54.03112 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5800cb41-6afd-33aa-8632-e1a040a87966 | -12.71838 | -54.08705 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 328fcc21-c571-3f95-baf9-76962a9ed6f0 | -12.71447 | -54.08652 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1836f129-04ff-3be4-ba11-dd5bdf0b09d7 | -12.71125 | -54.08095 | 2024-09-28 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README80.md)
