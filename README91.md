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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7cf6957-e965-3c21-a451-3e1d1d11f6ed | -3.05447 | -54.05558 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10f93161-a1a7-3164-991e-31dff852d742 | -3.69838 | -51.80844 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51787c7a-8316-36f3-986e-d9a575868698 | -3.79044 | -58.98133 | 2024-12-01 05:08:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2889de16-44b7-3e75-9e6c-eaf0b0b07a77 | -3.639 | -54.43864 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58fe8cef-1a16-3432-bbcd-07475791fffa | -3.30835 | -53.86786 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e134e3b0-0e71-3ece-be2a-1b68ca3cf168 | -4.00627 | -54.62024 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e7edaad-803a-3415-ae10-18c8eef03df5 | -1.18914 | -54.03671 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80d09a3b-9b98-364a-9cb6-b775c6b855ac | -3.34689 | -50.82427 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c24e792c-5ec7-33ad-a810-9201d275a569 | -2.63205 | -54.00156 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c16dd47b-db63-36e6-aca2-4333952c7417 | -3.11395 | -53.27399 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7834240-bb44-3865-8cbe-6c5bf6f1b6ec | -2.46428 | -53.96824 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ccd36b9-bdc7-387e-a5e4-a3e8393b7a59 | -1.05413 | -55.23874 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94f88fa8-e133-394e-91d5-ae5d23b672df | -3.2949 | -53.83836 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f94d6bf-3271-3471-ada4-57f1348863ed | -1.32936 | -55.67089 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be2f6119-babf-3574-a1d6-c4967694a649 | -2.52453 | -54.25805 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31affe0d-4704-3cbb-bbc0-0390700760fb | -3.03351 | -54.05236 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97e7c232-39bb-3701-b1aa-ea053626d71e | -3.22243 | -54.23349 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b138934-04a0-3fca-8de2-e01c2ea7590e | -2.87381 | -54.0125 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e670071d-ce66-3dfa-ad26-712fbb385041 | -3.86728 | -50.17022 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fabad6d4-7442-36bc-beb5-6aeb48ec195f | -2.83406 | -54.10889 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 484f3f91-dc29-3aa7-9d2c-47f8c2b05843 | -2.97725 | -53.28832 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54e3cef3-bf61-3dff-9487-095cfae445b0 | -2.71827 | -54.3867 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67c8a976-d687-3af2-9d1a-ed2323b76bae | -2.69682 | -52.9199 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d60f7477-c2bc-377f-b217-5193a34708dd | -3.05923 | -54.05551 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 159385af-f755-3edf-982d-19f7dba9be53 | -1.32659 | -55.66693 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ded2d75f-d2ad-32e6-b558-9d0f16691003 | -2.84813 | -54.04016 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00977456-99fc-31f3-9510-f3898b703d6d | -3.32368 | -50.22276 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f59f321a-cb20-38ee-88b3-39e6574d2d50 | -3.69229 | -51.82157 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b202af4b-53db-3edd-9154-9c0ca7502053 | -2.42407 | -54.02096 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab10349a-42d1-3b78-9108-5157c9092aee | -3.00797 | -53.23295 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a70245d6-f554-37b4-bfaa-0c74bf307581 | -3.32838 | -50.19238 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 980b64af-78e8-3138-8b17-95a64181dd44 | -2.74022 | -54.03685 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83562075-303b-3a89-8116-c50107d9acde | -2.45659 | -53.71351 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7027acf1-73ba-37b9-a1e5-fca330b712e0 | -3.23573 | -53.63229 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1da536e-aa15-3347-9d24-dc227dfc218d | -3.63575 | -51.45677 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 661efac6-fc5d-32d7-aa1a-4b861c9a7d7a | -3.10743 | -53.80999 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18af6b7f-a7b7-33c9-95ac-baebfb90fb06 | -4.18301 | -47.9895 | 2024-12-01 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6dc5f3c-60bd-3424-ae4c-8c9328e99586 | -5.48514 | -46.34838 | 2024-12-01 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d3a54a7-f0ca-33af-b15a-19f7dec17b58 | -2.88151 | -53.32697 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f9aa7ac-9d3c-342f-9d08-4213d027334f | -2.83572 | -54.1105 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d09cf3b6-f765-32ae-aba9-07643e097e75 | -3.06953 | -50.5702 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d780d6e-978f-3290-a197-9f85c9418ca4 | -6.70772 | -47.27753 | 2024-12-01 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e86c8fd6-eee9-37c1-8000-69e08a778e54 | -2.70598 | -52.00151 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9b5ea1e-eff6-3775-8f6a-f115374f60bf | -3.06581 | -53.6821 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11b29cc4-7f9c-316d-bdf5-8ea0c769be10 | -1.37694 | -53.6484 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3525499-ded6-3230-864a-d3f37a91802f | -3.25001 | -53.63447 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68d2d6bc-8fb8-3857-a180-c2fdd112d8b0 | -2.80982 | -54.07119 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a1ea986-8b64-3740-b589-78e4a6760b43 | -2.16886 | -53.6098 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 831c7fbf-19e2-3815-94f3-d6a8c18a9b30 | -2.3357 | -53.86686 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66bef595-0fb6-3531-b6e6-6e65486453d7 | -1.44495 | -55.19506 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5f8194d-64bc-3d50-ae41-65aa96db2dd2 | -3.06226 | -53.68151 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0811d6bf-4141-3692-b884-b3dc35695298 | -3.33417 | -53.37324 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ce9ecb7-ae04-33ad-8282-76360100f46f | -2.88954 | -54.16437 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7cf3aa4-ca12-337b-ae47-1a16376bad32 | -1.3321 | -55.84751 | 2024-12-01 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfcdad51-9955-3c11-83e6-0a5dc635a16e | -1.26617 | -54.55402 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62ba919c-d39f-301a-b110-fae9ddef90e4 | -1.73142 | -55.07739 | 2024-12-01 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c44c68c-508c-3a70-9b11-a2d00aafe351 | -2.47847 | -50.36726 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1acf7e7e-b298-3c71-9095-e888fdb49354 | -2.26454 | -53.46118 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4a31f3e-c86b-308a-89bd-b2dd73e2b992 | -2.63483 | -54.20066 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e59256e4-7086-3eef-a893-cfc37bd92342 | -1.37345 | -53.6478 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94457cea-627a-3937-b7c6-272aa69446ff | -2.8686 | -53.99979 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c51f4747-acca-39c9-bc7f-265dadaa8370 | -2.63137 | -54.20015 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8a754572-30c4-3a69-9834-f7f72acdad56 | -3.99693 | -44.76192 | 2024-12-01 05:08:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 564e6870-dac7-3e2a-aaaa-bace69d750f4 | -1.52527 | -52.66352 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 53d6e36f-2dec-30d7-b6ff-7f4c8d4748a5 | -1.59891 | -52.29446 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 056bd98a-93bf-37fe-bb91-53405bd43abf | -3.48998 | -53.81683 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4890a19d-8c8e-312f-bfaa-2fdb22e005b9 | -1.94593 | -53.34526 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8c461568-eb52-3f51-8304-72a12f1879a8 | -3.74857 | -52.26571 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8efd23a1-d82e-367a-97bc-96f7e4940217 | -2.99624 | -51.06129 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c18682fd-23ae-3fb9-bff3-efecc0569d95 | -3.38552 | -54.75919 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03576974-d204-395b-9fc6-a26e4fb44a2c | -2.98341 | -53.34496 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b1a4741-1804-3534-ab14-db3c02e42497 | -3.32361 | -50.19046 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa584ba9-5da5-33ee-b763-a7c1495f736e | -1.61816 | -53.8915 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ef586bb8-cdb2-39c1-a3e6-15c4df8965c7 | -3.41432 | -50.1597 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2859172b-8e57-31c1-87d8-9eaa37953f7d | -2.76048 | -55.33719 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a5ab1a7-f719-3be2-b83b-7cc272099e2e | -2.65694 | -51.87898 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 377d5f17-eec8-39d0-9947-9bbc2ba6abc9 | -2.544 | -55.22789 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc4f2f8e-0c82-30be-95f2-b24a1c0f6741 | -4.04018 | -46.93688 | 2024-12-01 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| befa8dfa-e1ca-34d8-8472-9cca9829b1b0 | -3.11545 | -53.99257 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc3a8db1-7c8f-3502-ac93-9915742be278 | -3.76695 | -50.17917 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8577907a-9bdc-3ddf-8ba4-10086bef71da | -1.73027 | -52.49821 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 225e5988-87ac-3db3-9b6c-328adfdfe9ea | -2.75055 | -54.08568 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24c7859f-7a4a-3b7c-a0f8-bf74d5346fd7 | -4.54083 | -45.70118 | 2024-12-01 05:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18cc7a13-b048-3d0d-8838-073db25ef393 | -2.03443 | -53.49724 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 736fc4a9-78e0-3d37-b395-f3b076f0b687 | -4.06351 | -54.24959 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10bfe2da-6d35-3925-a328-854fd80697bf | -1.46354 | -54.36506 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a4cad3f-6b42-36c1-80a7-638c6a751c88 | -3.49597 | -53.80155 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0955290c-70e5-3752-be49-7b09c1d18618 | -1.54517 | -52.99006 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 11411e5a-1b47-3e21-9046-68bf84217e11 | -2.69747 | -52.91556 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a168b37a-1e4c-35be-be93-b104da0414f8 | -1.48326 | -55.38337 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1f9bdaa-b2d5-3e9b-9e63-5d9f0cb9e3a9 | -3.05982 | -54.05164 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab027b50-cbb0-38b5-ad43-65c859856fab | -2.31587 | -53.84829 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6707255-bdcf-30d5-84c1-a2bc9f2bf9c1 | -3.28785 | -53.67327 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7e8493f-d26a-3043-b400-8ae711bf9c12 | -2.90062 | -51.57725 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14c21dfe-b308-3089-8d04-c2402aeabdd1 | -2.9779 | -53.89685 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff5d96bb-18d0-3db9-b5b0-acd6904ebe85 | -3.10307 | -53.27231 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 673cf96c-8d5f-3aef-8a0f-a3d3bad7cee7 | -3.29905 | -53.83493 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dfaffd0-53e2-3f71-8dd9-3bdd205b6581 | -2.74838 | -51.75498 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 10019294-676b-3726-91c0-066a3c024197 | -1.27631 | -54.55558 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5cc1f8e-7920-3d24-8049-4dbadd40af37 | -2.27421 | -53.77023 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README92.md)
