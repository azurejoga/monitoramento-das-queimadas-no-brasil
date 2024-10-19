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
| 81fcf08e-8cb6-3da2-b864-d4371f419dfa | -2.84972 | -53.32521 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33d5bdd2-0723-31bd-8c4a-68c4c8035198 | -2.66365 | -52.57807 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aa2184d-9540-39c4-b8ba-6e81663bc08b | -2.66202 | -52.57952 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aba84a3f-f953-3f90-bf20-9d1b084746e4 | -2.65947 | -52.57746 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2025c01-afc2-3226-9a91-129fed12290d | -2.65785 | -52.57891 | 2024-10-19 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c125a4a8-7903-3b23-9146-0b8f7c2a09e9 | -2.09155 | -53.40083 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c63f9cc-46e5-3096-bf51-b841cfc51849 | -2.09123 | -53.40281 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b69b748-3074-3060-8eed-7e821678a461 | -2.08764 | -53.40023 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e76cb73-0e23-357e-8077-bf66dd8accb6 | -2.08295 | -53.40452 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 977af9dc-78bf-3803-9980-a853342fcead | -2.08217 | -53.40951 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f47105f-084a-37cd-a1e2-1296b0152813 | -2.07904 | -53.4039 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a83a4a9b-e34f-3cfd-b33a-bd01ceaeb772 | -3.95427 | -53.40731 | 2024-10-19 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1c99713-5e10-306b-8a49-a1546660adb1 | -3.95375 | -53.41085 | 2024-10-19 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1749605d-a6cd-3a2a-8c9a-32b3d02f60dd | -3.94972 | -53.41026 | 2024-10-19 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d499d704-7ae1-34de-bf48-fcda45c8a8d0 | -3.8922 | -53.64106 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c84f93f-3e38-34b7-82fd-d3d0978c47fe | -3.88762 | -53.53852 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 191c10d0-0b29-3251-84af-325cf53d5a1d | -3.83054 | -52.69488 | 2024-10-19 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0977955-3232-3179-b44e-6362fcde568b | -3.82993 | -52.69508 | 2024-10-19 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c05b5675-6389-37eb-95ce-590bca707491 | -3.75175 | -53.39762 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbef6c8c-ddc4-30df-af8b-c26c5b24896f | -1.92776 | -54.58545 | 2024-10-19 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b55e605c-d862-3226-b1a6-2b7b23d5e708 | -1.33566 | -54.65956 | 2024-10-19 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a235ecf1-95de-3f8a-b511-6cf546d1196f | -1.32359 | -54.66596 | 2024-10-19 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec395c1b-54dd-342a-ac30-cb6eeaf8d259 | -1.10316 | -54.21177 | 2024-10-19 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a62bde02-6c88-352c-91bd-2114210b51fb | -2.08947 | -53.57302 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b757574d-3ba6-3e20-bb9b-354c7b2da4d5 | -3.59184 | -54.68632 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da046c48-0d02-3421-a413-83af7dd7a876 | -3.58814 | -54.68578 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 827b4224-27ce-3af2-a6eb-4c20154d2d99 | -3.52856 | -54.5652 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb3ed3d5-084f-3c3a-838a-cf972056bf20 | -3.49586 | -54.45474 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ace3bf8-0bcb-3667-a193-4682d32fbc28 | -3.49211 | -54.45417 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fd95728-b108-368a-bfe4-33507aaea70e | -3.4417 | -54.14982 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b93e1060-763e-3271-bd3f-615126433ade | -3.43789 | -54.14929 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 79e634d7-5c43-3c67-9f56-4b3f0ba1cfd9 | -3.43761 | -54.12545 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 135d742d-4733-3ef3-bb7d-55d246bbdccc | -3.43407 | -54.14877 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2ff44af1-9150-3563-9ef2-506cfea8cbe7 | -3.43025 | -54.14825 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e4e80352-ddb5-353e-9906-c441543ef9e0 | -3.42643 | -54.14771 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ec060604-abaa-3f6a-b77a-aeb14220ca9a | -3.42262 | -54.14717 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af241547-9af3-3a59-8ea3-2115b3050cee | -3.4188 | -54.14662 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65ad1c71-db84-3cc2-a173-65a95d155483 | -3.40034 | -54.06899 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8550a2c7-045b-35ca-8a55-28ab474b1259 | -3.3996 | -54.07371 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e92e84d8-bf76-39de-a444-ad17b4d36c25 | -3.39953 | -54.0667 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 952ed0ee-332e-3449-9f12-451c6ca84618 | -3.39882 | -54.07143 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 201a5794-cb46-3a21-8a90-e09a307fae8c | -3.39651 | -54.06844 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccaa37e5-1099-3d40-a9d1-ee72daff673b | -3.39578 | -54.07314 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a452e028-dc43-3f95-90cd-406fc9648bf6 | -3.34495 | -54.80797 | 2024-10-19 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e58a8b4-f2f0-336c-a31b-e5e07eb228d4 | -3.32786 | -54.08241 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0689b494-0df4-3f80-b181-fa2f42283666 | -3.32404 | -54.08188 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b0ddae1-434d-3c74-8d0f-554dfb73de9f | -3.27071 | -54.18076 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f3f245e-7192-3949-b3e5-2854a2df0f61 | -3.26691 | -54.18021 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b20c154-62b9-391b-8465-f1357003b501 | -3.26618 | -54.18488 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b5d1c28-8db9-315a-97be-dba695775197 | -3.15881 | -54.92199 | 2024-10-19 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2cf2b97-1785-343d-882a-97ec6ae86a14 | -3.15815 | -54.92622 | 2024-10-19 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e639afba-dc6b-3fc4-80b0-911ff9ce49a2 | -3.14626 | -54.25798 | 2024-10-19 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4045813c-001e-3370-a947-e51e9689cd3f | -3.11511 | -54.98821 | 2024-10-19 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6fe16e4-a2ba-33b2-8164-90a3fe8a0230 | -3.11149 | -54.98766 | 2024-10-19 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba7f4d83-177c-3f90-a7eb-9dc7ddf94c40 | -3.66084 | -53.84492 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd3ec719-47d2-3f7a-ab0e-00c8f6545be8 | -3.53862 | -53.85221 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5c67cc5-b0d5-39d2-8320-a916d3ebc2d1 | -3.53473 | -53.85161 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb291ce4-53dd-34ca-95d8-1763658aaa6b | -3.12164 | -53.74555 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04889217-38a4-352e-9eb4-070451ddab5a | -3.12088 | -53.75044 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3cbe5ca-3b0c-33ec-aa9a-a467cdf36dcd | -3.11775 | -53.74497 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b19a090-6595-3ad5-a955-6950d3475a3f | -2.94817 | -53.70245 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dd0e38a-ccbd-3551-8ffe-496005f22ea9 | -2.94743 | -53.70734 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b446221a-2735-3d2f-ac62-1c33432fcea8 | -2.93892 | -53.71105 | 2024-10-19 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e267104a-dd6d-3d7d-a70f-c730f39dd5ae | -2.95091 | -54.14441 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cad94fcc-1ebe-379b-a6c3-4d5d4b80c94a | -2.95019 | -54.14902 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0db5d0e-298e-36b8-b0b9-e79e6a0df77d | -2.94875 | -54.15825 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a3c3f03-4d79-3d95-ad9c-aac1ea3bee2d | -2.94496 | -54.15769 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a63246ab-be10-30e3-8960-d881cc241ed2 | -2.91729 | -54.03501 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 306c3f6b-ff54-3841-b652-6810dfc238bc | -2.88554 | -53.98706 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33d3387e-e7e2-385a-85b7-c3cf5fbba99f | -2.8832 | -53.98434 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e97cb0cb-e4d3-3eee-abf0-a80931c3d393 | -2.88246 | -53.98903 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85c0b36d-e88b-388d-8e8a-d8dc48c9b762 | -2.88172 | -53.98648 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 449b2132-cd95-360e-8be3-77cfab7e1737 | -2.87509 | -54.18462 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d91e62d1-a7f7-3585-9fa7-cee39a6d2d4f | -2.87439 | -54.1892 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9739f579-9e77-36ac-8c32-6ffccc4cedd6 | -2.87131 | -54.18405 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 047a15bd-4bc2-3d3c-8273-519ff4debcea | -2.83034 | -54.86802 | 2024-10-19 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 670ff480-6340-35af-af15-3614880036b6 | -2.80469 | -53.98679 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7890028f-df68-3da1-86a2-d0249cd9d562 | -2.80088 | -53.98621 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 492dc28f-22fc-37a5-b269-c1ee1d3b8b45 | -2.80017 | -53.9909 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19de223d-d330-346a-b846-ab2dafd041d8 | -2.79635 | -53.99032 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81a1ff5f-cdf4-3646-a590-8d84462b6369 | -2.79254 | -53.98973 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e9b937d-e537-3228-8b43-bfd0a1205783 | -2.78687 | -54.02711 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fbfcbb7-3944-34ce-be61-d97e2abfe2f9 | -2.78307 | -54.02653 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edd6042d-4c0d-330c-8942-e4ca84d5a086 | -2.7109 | -53.99285 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c7002ff9-7706-32b4-9b2b-5552f7fd4664 | -2.58305 | -54.29411 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 625e8f45-4fcb-3e26-99f3-294dc971b997 | -2.56471 | -54.01192 | 2024-10-19 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f559de79-0e82-3961-b837-ee64872a98ce | -2.55507 | -54.42524 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8689825c-3cb5-3994-af8b-c224dc0aba43 | -2.32972 | -54.38147 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1379bdb1-2117-37a0-bbdb-335316ad1b69 | -2.32904 | -54.38586 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bccae7c6-d5ed-3479-b909-cb0ef0f6f700 | -2.32669 | -54.3765 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ae8d83e-9ce5-3b00-a4a9-fc62f56c9453 | -2.32601 | -54.3809 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 71d35ca2-8074-316d-b7d3-7e6a714c60a9 | -2.32534 | -54.38529 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9009ad29-e145-301c-a584-0cfd079dd542 | -2.18632 | -55.0001 | 2024-10-19 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fa3a1886-6def-3c14-8c7c-d88948b8092e | -4.32675 | -55.43208 | 2024-10-19 05:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6222eb4-d7cb-3d7d-970d-981c394576d3 | -4.25541 | -54.6758 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49e5fce7-4b24-3a40-bfec-01c5a12e3d15 | -3.83136 | -54.23225 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9ee623f-40d6-3908-9c99-8160d868743c | -3.82802 | -54.60996 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1f79e3a-0169-34a1-bd4c-f6a1ff595a40 | -3.68806 | -54.21109 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21ee7f62-cf18-36b2-81be-6296a257c8db | -3.68734 | -54.21573 | 2024-10-19 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 027ae6e4-7795-37d9-ac3e-a3670048985e | -3.68476 | -54.56275 | 2024-10-19 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README43.md)
