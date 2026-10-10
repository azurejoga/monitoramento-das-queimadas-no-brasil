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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4ea044e-5c73-387d-a444-2f527159ae11 | -7.2191 | -55.06884 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a16ed387-a2f9-3aa8-ae59-dd757a9b6999 | -3.35607 | -50.42012 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0424799-e7e0-3bad-b6fd-5032d8b989e5 | -6.06222 | -44.65976 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c6a1219-bcde-3147-ba87-ef37cd92dc6f | -3.95531 | -51.88792 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8f1cc4f-1d02-3d4c-8f2b-9e78960fe2a4 | -7.24248 | -44.16444 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42e98db9-9992-3ecc-82e8-4cfe745f8c33 | -6.96453 | -44.95691 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b03f800b-4c56-3553-921c-18b4fdcc5800 | -9.31499 | -47.37769 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 134e3fa7-e4c8-3d1f-b7e9-91d446509935 | -3.60198 | -54.60789 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 779906ea-7caa-3922-a596-953881acd92f | -8.97949 | -45.8966 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1fbc90f-d4da-3bbb-a048-32d763196ef3 | -6.46234 | -55.49464 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 836b653a-3e7a-32e6-b12f-084405ce5ec6 | -9.11578 | -45.82346 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccf7c020-2d65-3ed0-bd66-bee32f13f590 | -9.94063 | -44.79673 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e1665a44-c2c2-34d5-9308-e2fa1c1e5233 | -4.1025 | -54.01831 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a96133b7-8833-3bd4-ad86-c26d853d39e5 | -6.99586 | -47.70861 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9024285-bce9-3eee-9ab5-d808ce70dc6b | -4.09645 | -53.99392 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7c5c8f04-2b39-3c2e-b02d-fd364de02447 | -9.22115 | -45.66094 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d093adb1-3ad3-3b4b-a34c-233e4002ddce | -3.30249 | -54.00431 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed2b315b-b02f-3e52-aed1-7a7c13c674b7 | -6.4382 | -55.05175 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d8852d19-a6be-3d5e-b5a8-42ef17346e4b | -3.57888 | -54.7085 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 91545e1d-126d-3c5e-b4b0-2734c14591b2 | -6.3285 | -44.25075 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e5aebb60-e2a2-3565-b8ec-f02b444d0a50 | -3.01046 | -51.01561 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f17f0af3-607e-3adc-917f-acb4ef9b403e | -4.40393 | -49.77064 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cb19c0a9-50f9-3082-b52b-83cb4728918a | -8.27717 | -46.41311 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70dd7636-ca40-3355-b713-9fe9b8f06281 | -6.87129 | -45.04055 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e09732a7-0f13-3b12-b50a-b90b0545cb11 | -3.34641 | -50.41156 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f1e656c-0058-3fa9-9154-f530d756e264 | -10.28181 | -43.93533 | 2026-10-10 04:08:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bfae151e-6a2d-3425-827e-b33dc397bd5e | -4.61356 | -49.20477 | 2026-10-10 04:08:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 094aed21-ba00-39cb-a651-69a9061edcdb | -5.67271 | -50.08039 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8142d532-ce6d-394b-b5f0-1edf5c433daa | -5.09679 | -46.22496 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8acb1964-f0f1-3527-a4ca-8bf71c95288f | -2.98835 | -54.17432 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f3666ce6-4597-3972-9945-8422dea4d60e | -5.79287 | -53.79515 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b8d22e3-eff1-3d79-9a56-b57ca2c940b8 | -7.53265 | -45.31019 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 10d6bcd1-9c59-34fc-b2ef-db7b75b596c6 | -5.33934 | -42.93059 | 2026-10-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cff87fb9-db08-3e44-914f-79c50761fe67 | -9.00843 | -44.37104 | 2026-10-10 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bdf96567-8cdd-3124-b54b-c4e4b63c5aa3 | -7.56488 | -45.64245 | 2026-10-10 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ff99fec-a587-3097-b32a-3afb4cb28181 | -5.95133 | -45.38517 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27d574dc-e15e-30b6-8ed8-20106bd57899 | -6.49537 | -55.31853 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db3041e5-32b0-34fd-9405-92ad691a8a1e | -6.8264 | -39.56365 | 2026-10-10 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e9a5d63-e30b-37c1-b19f-128439c02f83 | -6.19517 | -45.43516 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b399f359-2d48-33d6-895b-a0a35125cab1 | -3.66345 | -42.92502 | 2026-10-10 04:08:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5582687b-02db-3d64-a93b-6e09dfdeb4dc | -7.18317 | -46.54077 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffb8217b-d564-3f18-b9c4-8a80d0c3218d | -4.11938 | -54.04055 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ede332d2-2d2c-31dd-aa82-9030017d2ad4 | -7.23937 | -44.18369 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cee3fb81-be80-365e-a1c1-ef6cf130d0e7 | -6.07229 | -44.6655 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3c5e7d2-cb35-39d6-9044-ed0a0dbe6098 | -6.15932 | -43.99457 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b16065c2-0f5c-3cf9-a9ed-e6713561edca | -7.16943 | -41.98854 | 2026-10-10 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d343b91-c58c-3e78-9b87-149af79c0d5d | -3.25586 | -54.18652 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2685851a-4f7e-3f24-88a5-f82b82a6d13b | -5.60252 | -47.28508 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a627dc12-c253-31cc-9334-72b298f24c46 | -3.3504 | -50.40816 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60e141e7-69a2-3368-b9f5-a32a5a71e7a5 | -7.08464 | -52.67524 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a2989fe-77af-3bba-a3fa-2391eb23242c | -5.72119 | -53.49152 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9abe419-85d4-3ec5-90de-e81e6dc7062f | -7.16667 | -41.98457 | 2026-10-10 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e210b48-97fc-3b0b-8583-95eede52f68d | -3.22083 | -50.54926 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d281b625-145c-392a-a87d-4a784d2f635d | -7.1106 | -52.66622 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9206e369-91d7-31c7-9c86-2b1a66122547 | -7.92529 | -54.71957 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f375b3bf-393e-3115-b261-2acf95ebee3b | -8.26933 | -46.43637 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9113371-e62e-3134-a481-da482a23596c | -5.93899 | -43.35498 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21fbcd44-225f-39d2-95da-71cb4cdab177 | -5.36103 | -48.56466 | 2026-10-10 04:08:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c57a812-26e7-3505-b20c-f78ec764b6ff | -3.35723 | -50.41328 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca09803d-1923-3a40-90eb-acc527c338bb | -7.90875 | -54.70868 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a77bf4d1-ee99-3d18-9ef2-d6d1c8e0dd1a | -3.5663 | -53.01003 | 2026-10-10 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e69eb7e8-f6d6-36dc-ba79-eb86419e022b | -3.11272 | -53.78775 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 325cf84e-0818-35a5-a995-9ac426135b39 | -7.09446 | -55.73309 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1001ee1b-35c4-3572-8e76-51511b5e9a00 | -3.89575 | -38.35909 | 2026-10-10 04:08:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| eff17853-9f9f-36fd-a97f-d3f5b9c5dc0b | -8.9502 | -47.37545 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58714e23-4fab-3142-87de-8d09ca27d967 | -3.24893 | -50.41658 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc14b148-4600-3adb-b304-56759dbdd3d5 | -7.23903 | -44.16385 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d32d2160-17c6-30f6-9811-586866e2d882 | -5.59345 | -47.28756 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b3f16c0-1c1d-3ba5-9d9d-9f6512992edc | -5.95766 | -40.92051 | 2026-10-10 04:08:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 643dec82-a217-3b4b-9587-a46fd1f44dde | -5.69691 | -53.46537 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8eddda71-808a-3b88-ac7d-df8816244a4a | -3.34985 | -50.41158 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d66330f8-a06c-365b-a563-9b9f689e7ac4 | -4.12339 | -54.03614 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8e1150b-3fdd-32c0-8ba8-1dbd536d9282 | -8.89796 | -51.70884 | 2026-10-10 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18949b86-0436-32d8-92fb-6ab3c0baf111 | -3.24834 | -50.42005 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00077100-fe72-388d-abe2-226d2a2230e7 | -7.03101 | -47.65439 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd656efb-ab55-33f5-b936-48d4af6789fd | -8.92992 | -45.13131 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aec1e7a6-3e51-3b45-ade8-5d1669fe560a | -3.2356 | -50.18128 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09ce7351-c7f1-3f80-90ae-171bb379c907 | -3.27545 | -54.70249 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6276f03b-58c6-3f86-ab69-3bc3f77dcf5d | -3.4585 | -50.58447 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 394c6f35-2ecf-3eca-8d7e-029e15444aa9 | -3.47917 | -50.3308 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0d6deac-2a09-303e-8dfe-ce9f7c2d97bf | -8.37312 | -44.1918 | 2026-10-10 04:08:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfdc5b27-ceb8-359e-9d47-d586d07355a2 | -4.39807 | -43.12164 | 2026-10-10 04:08:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb191668-730f-3100-9b75-d69cd62f0894 | -4.41312 | -49.77836 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ec27d8e3-9283-37b0-aa52-e37500b2a9ec | -8.9732 | -45.892 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ca87ffd8-f40b-3ce7-9efa-94bd3c5f38ea | -7.04231 | -47.66465 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1833040a-8c55-329c-a718-1f127bb03abf | -3.30927 | -54.00544 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3e4195c1-10d2-34d6-abcb-6ddd04c95693 | -5.94888 | -40.93339 | 2026-10-10 04:08:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d67f74b6-b6b2-30fe-9c6e-68aaad9e60fb | -4.02776 | -46.98312 | 2026-10-10 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3df00950-dfce-3008-838c-e232f74eba9b | -6.24181 | -53.30983 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5eb4ed71-9368-3124-acd5-499327089caf | -5.7481 | -45.13503 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b2b482a6-f807-30e0-b4db-012ba6e45936 | -7.07408 | -41.59899 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6bf20657-8818-3204-b01b-764d0acd4956 | -8.36388 | -44.20567 | 2026-10-10 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a9b96fa-dd8c-380c-95ab-b981aa9f99e4 | -5.75615 | -45.13192 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93300b51-fafa-39b2-b6bb-9db04c4f3cc1 | -6.44055 | -55.03913 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 742f0f86-9e90-3f76-898b-f355fcc945ed | -9.21893 | -45.6518 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce18b3a6-9771-3d95-a0f6-351d1df8a5e9 | -7.33415 | -43.98854 | 2026-10-10 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 311d78e0-4b9f-3e12-b9c1-6018a99ea050 | -6.0593 | -44.65518 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01188869-141e-3a56-b5aa-1e5f6d85266b | -9.73701 | -44.79571 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 068347fa-a0db-3af0-92a6-249fb62d27f7 | -3.57305 | -54.70034 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c9a9796a-3db2-3de4-a13e-d4d0c6a0efb4 | -7.53127 | -45.31868 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |


[Clique aqui para ver as próximas entradas](README43.md)
