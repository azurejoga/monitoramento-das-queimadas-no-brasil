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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13454a96-ceca-377f-9266-a2201223e3d1 | -18.01123 | -42.13771 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f7e8b9c9-c3c4-394c-b794-97cbc45db60f | -18.00287 | -42.13868 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| df1409d1-eb1c-3f88-8d91-433f0990e9f5 | -17.95115 | -42.70679 | 2024-10-09 04:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e62e722-ef2a-326c-8c2b-e8f338c393bf | -17.84197 | -42.22567 | 2024-10-09 04:19:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c66f20a5-11ea-3e88-9c16-36a8dc46816e | -18.01083 | -42.13529 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| c3440338-2d80-3ff7-b36f-d401ab7347ef | -18.00816 | -42.13284 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7b614caa-eb5e-374d-b365-146ff6e387cd | -18.00655 | -42.13923 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 468c3d08-2e60-3cc2-bdaa-1753d56fb1ae | -18.00387 | -42.13671 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 29cad1b9-e6db-353e-909b-9dc9dd451dee | -18.00325 | -42.14111 | 2024-10-09 04:19:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 75c36b16-0c2c-3e9e-8636-03c482ae4ae6 | -18.0008 | -42.13179 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e4a6b03d-3ac1-3b6b-b4c1-c39dc05c5f02 | -18.00019 | -42.13612 | 2024-10-09 04:19:00 | NOAA-21 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| c8f1eeaf-75ed-3905-a7ee-8beb316cb1bc | -17.95531 | -42.70304 | 2024-10-09 04:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 53950718-7a9c-38d8-a6aa-1a196889c596 | -17.95471 | -42.70734 | 2024-10-09 04:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 66282d80-d154-3ed3-b49d-888be2db9496 | -17.95054 | -42.71118 | 2024-10-09 04:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a16027cf-793f-3cdc-a60b-d7ea1007209b | -19.44778 | -42.51523 | 2024-10-09 04:19:00 | NOAA-21 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0e3a5c39-55e2-3611-9e2b-9edf45cca32b | -18.84881 | -43.10514 | 2024-10-09 04:19:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 08737806-c28b-35ae-b54a-1e19464fe4a4 | -18.77153 | -43.08892 | 2024-10-09 04:19:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2ec6fdbb-47c0-35a8-a6d9-0fa8daf99d1b | -18.41148 | -42.61607 | 2024-10-09 04:19:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e2f814a6-9d45-3987-92ee-cba5c8532ac5 | -18.25121 | -42.23449 | 2024-10-09 04:19:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7e2a5014-8444-33cb-8d74-ab8e9f6015c7 | -18.23878 | -42.94871 | 2024-10-09 04:19:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4cd80e8b-ac6e-3641-9f71-85c2a67d6805 | -18.23706 | -42.96102 | 2024-10-09 04:19:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5a934241-eeb4-3779-84fa-d85e9c55a067 | -18.2317 | -42.94763 | 2024-10-09 04:19:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 20fad675-8776-3c0c-af65-2132a800d0c3 | -18.18458 | -42.58462 | 2024-10-09 04:19:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dabb21eb-93e6-31bf-87b4-fca76753eb6a | -19.12939 | -42.71696 | 2024-10-09 04:19:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b7e1da36-c86b-3ecc-a339-384de7b6e22a | -19.12816 | -42.72604 | 2024-10-09 04:19:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d3da6532-3c8c-386b-923c-4abd7876fa9c | -19.12578 | -42.71626 | 2024-10-09 04:19:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fb8109ef-2899-3a8a-a9d5-3a298b9d2c1b | -18.92843 | -43.15519 | 2024-10-09 04:19:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 42ed9c88-25cc-35af-957f-3567bffeaed8 | -18.84897 | -43.10328 | 2024-10-09 04:19:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 7a98f28a-317e-346e-8b25-519103f88d90 | -18.41807 | -42.62165 | 2024-10-09 04:19:00 | NOAA-21 | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 934e05ce-9970-346c-9656-d7a3877c7115 | -18.41387 | -42.6254 | 2024-10-09 04:19:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7fa9653f-45ff-32ba-829b-997e40b955b3 | -18.41027 | -42.62483 | 2024-10-09 04:19:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 55dc9d00-9bd9-3418-a009-5fb915dc27f0 | -18.25913 | -42.55178 | 2024-10-09 04:19:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3c1641e-13cb-3f91-ba76-2f4a18b86aae | -18.24473 | -42.95791 | 2024-10-09 04:19:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b33c1306-8b7a-307b-a1a9-344a0d7c9e36 | -18.24176 | -42.95329 | 2024-10-09 04:19:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3e0166d0-a9c3-359d-9788-58087b3f8aee | -18.23936 | -42.94461 | 2024-10-09 04:19:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9ed5ef85-9c51-3f0d-b355-946594b0b484 | -18.18817 | -42.58525 | 2024-10-09 04:19:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1b36f9a1-2565-39e3-bb8d-a3aa271599aa | -18.09772 | -42.34826 | 2024-10-09 04:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 30c8e3d7-52db-37c5-b449-5d4767398118 | -19.5429 | -42.10601 | 2024-10-09 04:19:00 | NOAA-21 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4fe320f7-0f75-322b-a103-24f3e1dade72 | -18.41087 | -42.62045 | 2024-10-09 04:19:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 92c300b8-a004-3010-8ea0-6468af6fb109 | -18.24751 | -42.23413 | 2024-10-09 04:19:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bc74c803-4656-3c0d-8d43-9067f8318c03 | -18.23524 | -42.94819 | 2024-10-09 04:19:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b87fb5b5-2463-3d9a-816f-ab7a3882fd8c | -19.27797 | -42.85161 | 2024-10-09 04:19:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4a7a8267-e638-353f-b3f5-c297839ffd39 | -19.13 | -42.71241 | 2024-10-09 04:19:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5bfcc109-1ad2-3027-963c-346c51093cd7 | -19.00633 | -43.21669 | 2024-10-09 04:19:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 40941f0c-f362-3cef-9c74-358811803a3b | -19.00574 | -43.22084 | 2024-10-09 04:19:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 787f6db9-71c7-3407-8029-d3372094ca07 | -18.78721 | -42.79151 | 2024-10-09 04:19:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 383ceca4-9150-3b8d-9b9f-a1b21d6da196 | -18.59864 | -42.34098 | 2024-10-09 04:19:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 44552b84-ef68-3238-99ee-a1cfda219b8b | -18.59802 | -42.34549 | 2024-10-09 04:19:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 7cfe1e54-5880-36d5-8a02-0c1d001b8f15 | -18.59436 | -42.34493 | 2024-10-09 04:19:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| cec97c82-4c71-3db7-8308-b4af7f1b348b | -18.25851 | -42.55613 | 2024-10-09 04:19:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a0d90e73-2565-3aba-ba01-d06769b7c5da | -18.18398 | -42.58895 | 2024-10-09 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 75c1ee44-9551-33cb-ac05-ee96fca7cac0 | -18.18099 | -42.58397 | 2024-10-09 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c08ffaca-8a72-325f-b8aa-d15c5f09abfe | -19.80637 | -42.40403 | 2024-10-09 04:19:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| acc4e7a7-f917-3957-854b-62d1626468bf | -19.80574 | -42.40862 | 2024-10-09 04:19:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9c3b03dc-eee5-3a8d-b059-022f599dfe0e | -19.77426 | -42.33415 | 2024-10-09 04:19:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 88388233-9c0f-3778-8aa6-f97fd8d64733 | -19.77363 | -42.33881 | 2024-10-09 04:19:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7f6234ef-0aad-32a2-abac-9dba6ee8160e | -19.7283 | -42.21314 | 2024-10-09 04:19:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 3e0fbc48-1f60-36b8-9069-a4ceee2a1c7d | -19.72915 | -42.21602 | 2024-10-09 04:19:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e85e46b6-9404-3c29-8514-77d4bc8f1784 | -19.82926 | -42.06777 | 2024-10-09 04:19:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 78ad3b32-29b9-3b4b-8617-e7e398ed4735 | -19.80268 | -42.40338 | 2024-10-09 04:19:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 53088691-0a91-3def-a430-6283afc3c038 | -19.77055 | -42.33358 | 2024-10-09 04:19:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 8e4bb329-6bdb-3cee-8d7c-6f0c25aef209 | -19.76992 | -42.3382 | 2024-10-09 04:19:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 6213fdb7-e840-3473-b7bf-3146096373e2 | -19.82863 | -42.07249 | 2024-10-09 04:19:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 740d60a2-b769-37ef-b1ce-e892c204c3ad | -19.80205 | -42.40799 | 2024-10-09 04:19:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2d559435-339d-367e-a35d-d7b6371a4738 | -19.72976 | -42.2113 | 2024-10-09 04:19:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 34636ea3-6035-30fe-8954-863017931566 | -19.72603 | -42.21067 | 2024-10-09 04:19:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3a0b874f-d264-35eb-81fd-4ece4cea4dd8 | -17.8761 | -43.29002 | 2024-10-09 04:19:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e556541-0ece-318e-800c-925fa1fa3a75 | -17.3946 | -43.42556 | 2024-10-09 04:19:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1441177f-8fe3-3097-bcce-2def5e4d071c | -17.86566 | -43.28844 | 2024-10-09 04:19:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5d73325-e59f-3212-8bcd-749e5515e119 | -17.87146 | -43.29765 | 2024-10-09 04:19:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| deddbcdc-65b2-30fa-9175-a7080b2970aa | -17.87957 | -43.2906 | 2024-10-09 04:19:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3210aade-64e5-3489-bb47-d29195648750 | -17.87897 | -43.29482 | 2024-10-09 04:19:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 822de05c-b178-34ee-86c2-d35e105de019 | -17.86972 | -43.28487 | 2024-10-09 04:19:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 90cbc772-9950-3390-90ce-08d1e8076194 | -17.70737 | -43.8279 | 2024-10-09 04:19:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bc7f635-f23e-3298-a2b8-517b764680d7 | -18.07032 | -44.51786 | 2024-10-09 04:19:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7ca63ec-c546-303d-b5a2-0d805f94541e | -17.97467 | -44.54473 | 2024-10-09 04:19:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3062d9b9-5046-3096-b052-c4e46f8c2028 | -17.97411 | -44.54844 | 2024-10-09 04:19:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b51aa28c-a62b-3f29-b0e9-87ce7bf78946 | -18.4446 | -43.4296 | 2024-10-09 04:19:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7537d4fc-6e96-3082-a6c1-25a2b6d1d9bd | -18.22739 | -43.66926 | 2024-10-09 04:19:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09b34d7a-0fa0-3d52-81f7-9abf87c0eb01 | -18.9949 | -43.47221 | 2024-10-09 04:19:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c0d8e750-7cd0-31b0-97a1-d270f6297010 | -18.96349 | -43.3415 | 2024-10-09 04:19:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 47997444-d780-3c58-8bf5-9dad33914842 | -18.44806 | -43.43021 | 2024-10-09 04:19:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cd4ef321-b836-3c8e-9bad-f5794d3f8766 | -17.10165 | -44.58845 | 2024-10-09 04:19:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8b32b90-7f83-3bbf-bfa1-6d2223b6c8fa | -17.93393 | -44.56462 | 2024-10-09 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5d3cc55-b59c-31dc-819f-cac33db5f5b5 | -17.04491 | -45.30999 | 2024-10-09 04:19:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 202bf74e-e114-36ae-b928-fedda722f791 | -17.93003 | -44.56777 | 2024-10-09 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3f0f24f-0b9f-3881-b4bb-6dfc8c722d0f | -17.59718 | -44.49964 | 2024-10-09 04:19:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d12ba6c4-20d2-3364-8a55-0277f71612fd | -17.93059 | -44.56407 | 2024-10-09 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 352a356b-ea47-3d59-b704-9d01395d187d | -17.59663 | -44.5033 | 2024-10-09 04:19:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50471e7b-610b-3016-8913-b47874a0176e | -18.96887 | -45.0892 | 2024-10-09 04:19:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 128ddfd9-b021-3f01-b175-a8225fbca652 | -18.97221 | -45.08975 | 2024-10-09 04:19:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8e295de-4c14-3600-a0a4-56435f5d5c7d | -23.7044 | -46.47646 | 2024-10-09 04:19:00 | NOAA-21 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29f89eb5-760a-3441-b44b-f64abea40bf7 | -23.68792 | -47.3083 | 2024-10-09 04:19:00 | NOAA-21 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 17de56cf-3ac1-340a-8ab6-e724a0723a45 | -23.64271 | -46.27905 | 2024-10-09 04:19:00 | NOAA-21 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fca72094-5ea9-3ebd-aba0-e87d211cbb8a | -23.46498 | -47.34083 | 2024-10-09 04:19:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 411eb316-1d5a-3a4c-a872-300ad010c540 | -23.46168 | -47.34022 | 2024-10-09 04:19:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4370ea81-c689-3fc4-b074-1cc8faf8b333 | -23.40695 | -46.55624 | 2024-10-09 04:19:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 42bcfeba-2df2-3170-a75f-6f1dd3751703 | -23.34818 | -47.02338 | 2024-10-09 04:19:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a135dbb4-a487-3294-8519-fc3e10c44401 | -23.33974 | -46.77174 | 2024-10-09 04:19:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2c0e6204-9f3e-3fa4-b31c-5b6149ae21a5 | -23.31369 | -46.78629 | 2024-10-09 04:19:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README102.md)
