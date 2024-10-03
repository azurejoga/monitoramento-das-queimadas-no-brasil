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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78064054-9ddc-36c8-b9be-8a9145aafc55 | -9.96216 | -64.77795 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61572cb2-0b7c-385d-9867-97c655a3fb30 | -9.96155 | -64.78151 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0685ec42-c83e-31a3-8b51-4a2d19e86c0b | -9.9346 | -64.76942 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89832fd3-6398-3f4f-8c9b-eaa761209206 | -9.93399 | -64.77296 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d314565f-155f-3f8f-9dd6-4d1a24699739 | -9.92997 | -64.7722 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfa43bfc-0b59-336f-937e-64609d61a7af | -9.89972 | -64.77423 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 416f8907-bc77-3bf3-9f13-f8ebb29bb937 | -9.89569 | -64.77353 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb9dddef-34a9-3840-8940-7cca9e6ad69b | -9.89508 | -64.77711 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 070dd88b-0931-366c-9005-bb455560d920 | -9.8757 | -64.69637 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa241f5e-b73f-3c33-a3bd-e3c9ff69b499 | -9.8251 | -64.70207 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dea0b46-7878-3706-861f-a9014eff3c41 | -9.68385 | -64.7176 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b63dbe6-fedb-31f0-82c0-3b1e0663701b | -9.68263 | -64.72482 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0caa5b22-0f45-30d5-a314-e29bc9e9b063 | -9.67982 | -64.71688 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64fb0f0c-3b2f-38c5-b273-c45906a32d6d | -9.67921 | -64.72047 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b12f839-fce2-312b-b3dd-81427e6f9928 | -9.6786 | -64.72411 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d86c6ffd-a484-3c99-bd97-167603aa7363 | -9.67798 | -64.72774 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47d81215-4d46-3459-a060-89c2e3f5bb27 | -9.67457 | -64.72338 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47d511a6-d327-3a6b-8d7a-c48c35554996 | -9.67395 | -64.72702 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 806ed601-567a-3a5f-a161-f49e47201d78 | -12.0143 | -64.90145 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 35307663-9561-3ecc-a502-9c1ae348756d | -12.01341 | -64.90658 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4890576e-8371-3bb4-8c14-f29ef41e1303 | -12.01252 | -64.9117 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c77f5d3-f73f-3dc0-b9cd-1c1eb729f26c | -11.95689 | -64.91022 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6dd31eb0-a5ba-38fa-8b3b-3e689f4f3910 | -11.95571 | -64.9118 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f972134-aeba-3b37-af86-0511e6ed889b | -11.2914 | -64.99935 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f73ae0af-391b-3141-bb9d-20c335c431e6 | -11.29078 | -65.00287 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f91d75f9-c33a-30a6-90ac-0e85ae79b117 | -11.28803 | -64.9951 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a38ef3e6-5db5-37f2-8302-7ddd66a6a9f2 | -11.2874 | -64.99863 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d73c83f-f663-31a3-af2d-744772846343 | -11.28736 | -64.96619 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c5142d3-ce72-3c2c-afe8-2fb92b22b22a | -11.28678 | -65.00214 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bb5e58b-1bed-3e9f-b150-63747b16abab | -11.28676 | -64.96972 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0fe78c9-2849-3b73-afec-d6ce3b0faa5c | -11.28503 | -64.96555 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcc785f2-cd3a-3fe7-9d73-85d444758092 | -11.2844 | -64.96908 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2240d9d-adab-3ed6-a37d-5443d12cd2d3 | -11.26267 | -64.91847 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3e118fe-85b3-3215-ade9-419a3e88a8fa | -11.26207 | -64.92197 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abb8c158-e025-3d3e-8e76-74ba24c20d48 | -11.24225 | -64.96539 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a5e2d19-8cfe-37fc-858d-c5b18e7e7472 | -11.12504 | -65.06192 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eba1734d-e825-347d-8c5c-b905c3e0240c | -11.1204 | -65.06478 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 470dfd5c-4424-333f-beac-fd7356837443 | -11.04379 | -65.1926 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dbfa904-e66a-3410-8e7a-703b5602c95b | -11.63257 | -64.98593 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 70705088-552a-37e6-9f6c-79cd30edc21c | -11.6286 | -64.98518 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b48cd74-4607-3057-9851-a38ff6580d19 | -11.62768 | -64.9904 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d599032f-9a0c-3fe6-82c6-4b0fa514a8f9 | -11.62371 | -64.98968 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52636994-605b-31de-aefb-f93a5f2b19bb | -11.61881 | -64.99419 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2439a067-94bd-3859-bb0a-f0dc679d2a40 | -11.61689 | -64.99252 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 14d12b79-c6a0-3a26-a3b3-8a1d0aaece32 | -11.61484 | -64.99346 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f32ab2e2-828c-3637-a550-6fec409ce4ae | -11.61391 | -64.9987 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da1b1f80-d37e-3819-b654-c45d35ee09b2 | -11.61321 | -65.18967 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| edde149a-e798-3e10-a302-0d445189a423 | -11.61085 | -65.15594 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2271212-5da2-3280-b6d3-b56b891d9305 | -11.60994 | -64.99794 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f1c713ab-684a-3b6b-86e4-1bdd22feb005 | -11.60919 | -65.18891 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25832396-c539-3af2-8c1d-08699af95bca | -11.60917 | -65.0023 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 304b4f6d-a47f-33be-903f-4c3988a5de3e | -11.60855 | -65.00578 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f202c6a9-c91c-3ba7-8ac7-bba1c57cacb8 | -11.60746 | -65.15164 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dabcb52-e2a8-3d9e-b20b-469bd6559d36 | -11.60701 | -65.00234 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3733be45-cde7-3d10-a25b-1ebef099aac7 | -11.60683 | -65.15523 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4380e16-4775-320c-bc7b-aef4ca8f3440 | -11.60642 | -65.00584 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1a43573-e1e9-3a44-be61-945c14a6da1d | -11.60582 | -65.00937 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d40e88e-dba3-3dc5-aabc-e80f14088373 | -11.60396 | -65.00851 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 443a742c-c250-361c-9080-dc251786a37f | -11.60345 | -65.15092 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a816f3f2-426c-328a-b694-ccc4f2d8b7a6 | -11.59786 | -65.00789 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 61e5d8c1-9818-3b90-b0e6-90ab9b3da1e6 | -11.59726 | -65.01141 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14b515d8-381e-36b9-85bb-011591bfcf8c | -11.59666 | -65.01495 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0911f88-cdba-33b8-bb43-abfdcf51987a | -11.59605 | -65.0185 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 274cf662-7c55-392e-bfbd-0191c0e7b701 | -11.53842 | -65.06618 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8307b2a8-6547-3294-83cf-6d404217ade7 | -11.53381 | -65.06901 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7f8e10c-5c00-3e6b-a10f-f1668a9739c7 | -11.52146 | -65.09235 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5f72e53-a977-3d48-8576-6ca5bedb0bd6 | -11.51683 | -65.09517 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5297aa9f-990b-38bc-a18b-7e3e4bfedb69 | -11.69201 | -65.02131 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf54ff0b-9137-34bb-a20e-b54bec6dc914 | -11.68994 | -64.98573 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 83b0803a-3b62-3238-ad32-78e49d82c3be | -11.68903 | -64.99099 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0376b6f1-4785-3178-9940-3dc4c646260a | -11.68863 | -65.01711 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed907d1f-427a-3056-b69f-8725e256fa97 | -11.68803 | -65.02061 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e768cfe-0147-3ac6-b5cf-c692e4409e1f | -11.68598 | -64.98496 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 600a4791-e053-3817-800f-906a009a730e | -11.68542 | -65.01197 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 49a34b03-2a54-37e8-bd10-286005015770 | -11.68507 | -64.99023 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| ec63937b-e9e6-3c41-9b4b-4595d3af2aa8 | -11.68466 | -65.01635 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f45be87-2774-3fec-8804-011b77587db0 | -11.68405 | -65.01987 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10ce8e21-394f-35fa-b369-3ade063082b4 | -11.68345 | -65.02338 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80af628d-3d11-3733-b0ab-c3d2b406bb3f | -11.68202 | -64.9842 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f738d734-bd7f-32da-aecc-2b1ca96b7518 | -11.68145 | -65.01119 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a47a000e-1606-345d-8fe2-738a41170e65 | -11.68111 | -64.98946 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 946822bf-46de-3c19-bd3a-264709555ce7 | -11.68069 | -65.01559 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fdfc534-e400-37d0-95c2-a2ebcc8cbcff | -11.68008 | -65.01913 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ec49352-c4f3-3c94-b2df-f26f39cdf7b7 | -11.67947 | -65.02265 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7dfdce4-a0a2-3999-a9e1-cbb6d8872854 | -11.67886 | -65.02616 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96948efb-be87-30a0-b059-799a9d5c0d71 | -11.67805 | -64.98347 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77ccd029-d0d6-3593-982e-6950ffb50ddd | -11.67748 | -65.01043 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 846a22a9-6544-3d31-9e59-f0400f0d8933 | -11.67714 | -64.98872 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64e99217-6da7-398b-93c5-602b42d2b9d4 | -11.67672 | -65.01483 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 115f3082-9e2b-3229-9402-c7773ce0badd | -11.67622 | -64.99403 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cfe82d39-5eaf-3292-8561-6dfac8af341a | -11.67611 | -65.01836 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd697793-3f6d-3317-a47e-9c7a989dc3e9 | -11.6755 | -65.0219 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67521512-c96b-306c-a2a3-31e4513e2ea1 | -11.67489 | -65.02543 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50afb8ea-6cf6-3023-95c6-037aafcec1d6 | -11.67408 | -64.98276 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b6163ba-d07a-39dd-957b-b6da2133b603 | -11.67226 | -64.99328 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 521ddb5d-50f5-344c-99ef-50d9a93377cb | -11.67213 | -65.01762 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20f51605-d2a2-3d55-9bb9-c2994b03f840 | -11.67152 | -65.02116 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3be8f37-cdcf-3ee3-afbf-692a741c3601 | -11.66893 | -65.20352 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f4e37b2-53f1-3e5c-835a-3f807a8bf10c | -11.66755 | -65.02041 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4db7f6c6-7d89-3508-81f3-0365f7d34582 | -11.66694 | -65.02393 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README176.md)
