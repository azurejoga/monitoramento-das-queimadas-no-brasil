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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d4beff7-f2d1-3d9a-9b79-d323523e20fe | -8.54022 | -64.0309 | 2026-09-11 05:50:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cda48571-8f26-3c7d-9115-caa9be729d95 | -9.04128 | -65.72874 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a27419a5-5f58-3454-bb44-a4051ba7deee | -9.23455 | -65.75199 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbb4c6c4-9534-35a8-93b5-a1d955e77f2d | -13.32852 | -61.68244 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52486988-7023-39e3-988c-15a05d5e08b4 | -8.64172 | -66.51378 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53920d36-b802-3223-b88b-02e564201fd8 | -9.07191 | -65.48984 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46f6c322-fbb4-3c19-a5a0-a5b9e6e48d80 | -8.83601 | -62.48235 | 2026-09-11 05:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1bc2f63-db68-3d4c-93dd-16b3042188d6 | -9.84291 | -67.55907 | 2026-09-11 05:50:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0fa86e9-5a20-3bf2-9764-184fef371559 | -9.0372 | -65.40856 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5a649777-d524-3c95-a015-cd43e72509fe | -12.15229 | -64.13623 | 2026-09-11 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc8950fc-9b61-39c0-86a9-9108a070d5cb | -9.72189 | -67.08913 | 2026-09-11 05:50:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da93d340-6b4a-3664-8e60-87879bb901ee | -9.17826 | -68.21065 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95daed44-34f4-3722-ab95-dd1aca2f7049 | -9.0802 | -65.48036 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 380cf381-9ddf-3954-9bfa-dfcb48168a80 | -7.80068 | -69.98569 | 2026-09-11 05:50:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dae5bb4e-f08e-3617-b4cf-62db95036960 | -13.3388 | -61.66855 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cfc5576-ae06-36b9-be4a-64235e55929d | -8.939 | -64.33056 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5aa59696-1b58-3371-8194-acaf1e4155bb | -8.74505 | -71.08256 | 2026-09-11 05:50:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e1ad9d1-3342-35a0-ae31-ec35f1809fcd | -9.1078 | -67.69607 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7b14430-06b2-38ca-b978-ff9d4815eed2 | -8.98232 | -65.38908 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b12bd4db-6e38-3e8e-b9a1-1d64f9482b4b | -9.14203 | -64.39928 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31dfca93-b50f-3d0a-88f5-a85e2df0eca0 | -9.19202 | -68.21291 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 134d2021-b90e-39fb-9914-34688f3e0e73 | -10.19159 | -68.76819 | 2026-09-11 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4a673d6-803b-3d92-b812-219d9c4f3c6b | -8.86713 | -72.70515 | 2026-09-11 05:50:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddc7c3c8-8e76-3af4-905e-19c3014a3d71 | -9.42506 | -65.85783 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6e2e235-83f9-34e7-a631-3d6162d98bff | -9.16116 | -65.80801 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be4aecaf-b7ad-39a6-82be-840e9e8a5892 | -8.53469 | -66.99055 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b2586b9-6944-3259-a316-b90a3159419c | -9.41124 | -67.41082 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b16d0dc-ab3f-35d2-a69d-f9a97e7e41e3 | -7.13821 | -73.11921 | 2026-09-11 05:50:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3df3a1e-8afe-3342-86b0-bba387df5692 | -13.34343 | -61.66536 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6223882-7cf5-393d-96f4-5dedef2c9121 | -9.2234 | -65.58505 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc8fd3cd-498b-31ea-bc9f-bf43b49d9824 | -9.43994 | -68.26453 | 2026-09-11 05:50:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8f0ccb8-04dd-3358-a8a1-1efe8baca882 | -9.89418 | -67.60461 | 2026-09-11 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f748b48e-02a5-3341-85a0-9e7350ba96b1 | -9.10559 | -67.68819 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d3ceefe-f1ce-3a4d-bf61-6c7a6c416263 | -13.34652 | -61.67349 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f496847-0dae-337f-ba4d-c4a6d708c31c | -13.21703 | -61.64752 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fac7a02-b688-3234-9b7b-3ed530dc9504 | -9.4365 | -68.26397 | 2026-09-11 05:50:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 958e75ca-62c4-3e9a-89b1-44c5547a169c | -7.63224 | -67.25665 | 2026-09-11 05:50:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04a4f7dd-908d-3d48-b3c6-49907e1a004a | -11.81232 | -60.45558 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33c16242-be8f-32fe-90f9-b820a4ef3557 | -13.2122 | -61.83612 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51cc563b-d364-370a-ab92-24fd4aacb0f4 | -7.36228 | -70.14811 | 2026-09-11 05:50:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a37025d7-1305-372e-bc9d-4e032b64781b | -8.64885 | -69.7886 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6e80c33-5827-3f76-aa58-a24a8e0bc2d5 | -9.17951 | -68.20307 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f12c6193-29b6-313e-ab5e-afd278d3a84f | -9.01452 | -65.44455 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8377eca4-2865-3bd0-9c92-279af5bcfbf0 | -9.41123 | -65.85891 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 306576aa-4c04-3da0-9811-38ca15be3e4e | -13.26033 | -61.60747 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7f0a992d-faaf-33de-a1ff-c28099290d44 | -8.98177 | -65.3926 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b795282-6272-338c-8eab-8bce22545c8c | -8.83904 | -62.48728 | 2026-09-11 05:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53c16d42-248e-35f0-85e3-576501eb8491 | -8.98791 | -65.41875 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a689dd97-e69c-37e8-b6fb-b2b708e9f1f3 | -13.24433 | -61.60133 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fadced26-95d6-379a-b5ca-12716ab44f09 | -9.01062 | -65.42595 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06a80c52-131d-3dc6-b09d-69fcab712634 | -13.22472 | -61.62171 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f91b5e88-8cd7-31b6-bdae-763770aa5e6d | -9.43712 | -68.26019 | 2026-09-11 05:50:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38251821-1135-3349-bda3-91f86c303e8c | -9.18108 | -68.21499 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7804b32b-126a-3936-a036-18825560f0bd | -9.21786 | -65.577 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61212566-c675-396c-96d2-659c44ba5354 | -13.26085 | -61.60368 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b1ca8412-6bb4-35fe-88e8-1ad0a4dee165 | -9.30423 | -65.89191 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4af135f-2737-3114-ad61-de73a4e7a725 | -8.63344 | -66.5017 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b60567c7-f53c-3752-93a3-585cd4ecb8cf | -8.63063 | -66.54066 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06674628-da0b-34b8-a0db-b801136cb39b | -9.45931 | -68.83232 | 2026-09-11 05:50:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 403c3aba-af08-3069-b75c-d300e41ca997 | -13.30895 | -61.67197 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcb26821-bea2-3ca4-872c-462694048ea8 | -9.21731 | -65.5805 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0b95cd3-0067-30a9-a54c-8191f4d1879d | -9.08907 | -65.48895 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b7f0ff5-c844-3ff7-a336-cdf5df893656 | -9.01947 | -65.41296 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7242f4c4-b0b7-3a35-8071-dead0f95037b | -8.79538 | -68.99167 | 2026-09-11 05:50:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f05d49b-9da9-30bb-91ad-ba714354a7fb | -13.21754 | -61.64376 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb73fddf-ce5d-3b96-b2db-7ecd2ba9c956 | -8.93819 | -66.84991 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3b47bed-bdb8-3ce9-8cbf-cbb3d80c183c | -9.0791 | -65.48737 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b603e9ff-166f-30c6-a3b8-6c9ae4114a80 | -9.35139 | -65.67738 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79cdef67-2687-30bf-92f8-1613b1e16d34 | -9.42117 | -65.8605 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2376d303-a5e7-3d4f-a74f-44e1908e6634 | -8.45992 | -64.05353 | 2026-09-11 05:50:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 503ef818-4a86-39ee-80a6-252b59a6626e | -9.18638 | -68.20423 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c3a09e6-0304-3ef2-a9ec-7c0071047045 | -9.1892 | -68.20857 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ac461ca7-29d4-3e88-9b3a-86266345e01a | -8.34968 | -71.02404 | 2026-09-11 05:50:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deac5f02-6ed4-33c4-95e0-1b8ffcdbb0e1 | -12.15875 | -64.14131 | 2026-09-11 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35b3fc31-bf76-3155-b311-69f1a229b131 | -13.31307 | -61.67256 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3246357f-e2c3-3e2c-a0cc-f29c305b73e7 | -8.62547 | -70.57765 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d59ef599-207d-38a2-bb3b-d31ac2f86365 | -9.50081 | -66.7929 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faf66267-8305-3e64-add6-1e2334c46566 | -8.63177 | -66.51217 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1041dab4-e7b2-3f74-9f7d-1ec4c0dd5196 | -9.75377 | -64.94871 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e76718d5-d426-3bc2-8ec0-663bba6e3ec8 | -9.18514 | -68.21178 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 927597cb-83f1-37f9-948e-a24026eb98f7 | -12.15522 | -64.14078 | 2026-09-11 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fc1f7f95-2a7f-3d00-8fc4-d3fbe7f563e6 | -13.21958 | -61.62867 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71903020-948b-3c80-a019-6d4e0a3d64aa | -9.50494 | -64.70597 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81f32c9a-7727-33d7-93d4-8bc0e10a6126 | -9.23169 | -65.57558 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b53802c5-9836-3408-b03f-5eb34a587543 | -8.6384 | -66.51324 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1b0ad26-6400-31f0-ae62-eb63a6def0eb | -9.13746 | -67.84039 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fc0ae00-eb16-3677-8788-39ee93f5a7d0 | -8.46277 | -64.05779 | 2026-09-11 05:50:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71f363d4-2efc-314b-a436-e17b8fb377b1 | -13.21856 | -61.63622 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6428bcdf-ad3e-3550-b646-fe304809f56c | -9.09626 | -65.4865 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e9a589-ca3f-302e-8bbb-b7f4b6fa25be | -8.98619 | -65.3861 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb010921-1755-3757-9e9c-34bfd3aad1c2 | -9.29038 | -65.80741 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a450edc-b4a4-3a97-86f8-56abe286a3f9 | -9.03854 | -65.74619 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f48ce21b-0ae2-3eb6-9435-b023ea3bbd4f | -9.75771 | -65.03419 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25b0afba-6201-35fc-9126-aea28c4c3aca | -8.8787 | -70.84018 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24edf48d-974b-386d-812a-14748c58f117 | -8.63121 | -66.51567 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85d82ec8-a331-3c1c-9ff2-264b0b1288fe | -8.71626 | -63.98079 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29309602-7c10-3efc-803c-89012e09e332 | -9.07245 | -65.48632 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a396c0d7-bff4-3d40-8c1c-70c5d49be41a | -13.2925 | -61.82516 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9800d70f-bd17-36f7-b515-17717dd50f30 | -8.92541 | -69.4321 | 2026-09-11 05:50:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b920e42-ff79-3034-b2ca-54ef6aa88847 | -9.22285 | -65.58855 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README35.md)
