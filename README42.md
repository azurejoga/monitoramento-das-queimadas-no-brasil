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
| ab359048-1c46-3dd7-acd1-63234496b896 | -3.03555 | -53.26561 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 474c1118-1cc8-3a3f-bedb-7fbeaecb8f6f | -2.4128 | -47.78522 | 2024-11-07 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f99a7e97-eac1-31aa-be3d-de9a113809e9 | -3.17698 | -51.25995 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ec6bc49-486c-3f15-aac0-2d06b82cd96c | -3.57338 | -50.54774 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1183e0cb-9bfc-34cd-99a8-b013bca74044 | -1.24214 | -54.18013 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c4412be-2b92-3759-b134-2eb427328cc4 | -4.04896 | -49.27231 | 2024-11-07 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 48150630-87a9-3e92-afa1-ee7997e91d8c | -2.85155 | -48.6769 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7f8bc0f9-6393-3349-9c19-1802d3ced50a | -2.76238 | -53.21554 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef6429bf-34a2-341c-89f8-efba31ed036b | -3.22351 | -50.44616 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1a2ed7e-75ae-3f2c-9489-91aa7475d21f | -1.44219 | -54.49737 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58068540-90c1-3172-bec6-332ea0ab10cb | -2.74633 | -54.11905 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecb304a2-554d-3681-83f7-4a358570557c | -4.40272 | -50.69374 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc0c8bdd-1b1c-3aaf-a675-e117c97ce05e | -2.82156 | -52.95338 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8fe96bb-0ada-3709-a9a3-5ab73e22b872 | -3.80787 | -52.156 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc0608ab-3887-32b7-925b-7f5d1c1933d4 | -1.26947 | -53.37971 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff4997a1-1770-3305-bb5e-3be055691ff7 | -1.3769 | -52.26295 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5148b0ea-6d31-38e3-823c-fddb0e9b9b53 | -0.36833 | -51.4273 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 810fc1ce-8a71-39f9-a769-913fc29e1a5b | -2.75314 | -53.22701 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7687046-c552-3842-9110-0b89e4ad1e75 | -1.5019 | -53.4953 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da53f6e5-fc79-39c1-a82f-a8c3388e4352 | -1.48246 | -47.21878 | 2024-11-07 05:10:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73ca4dab-fba9-3942-80bd-7c9b30952600 | -1.3893 | -52.20774 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3e418ec-ebc3-3a45-b374-46fb916c2c9f | -1.27009 | -55.67472 | 2024-11-07 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 247618be-2819-3414-a045-2539fa3a966c | -1.21131 | -54.1747 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92f17f6f-8812-358a-9c7b-af5fa12d6a40 | -3.01915 | -53.42374 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfa985ee-64a6-3a47-a70e-fa01f6220a3e | -3.58755 | -50.26569 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ad39618-c0f2-363e-9e94-8ffb5c3adfb3 | -2.9401 | -51.05487 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35b9a3bf-3e65-3894-b3c7-74589dcd5d91 | -3.53485 | -50.29248 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02038fba-b863-3fcd-9147-da92945c457a | -4.25793 | -50.6971 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2cc1742f-1baa-3f89-920d-f12aadf00041 | -2.81687 | -52.93444 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da15abe4-4212-3e4d-b5ca-4d57452635d5 | -1.96254 | -51.07844 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3b192cc-5324-3090-94b4-209154bffff8 | -2.87208 | -51.3145 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 446aad92-85cc-3225-9d55-2747926c6451 | -2.41328 | -47.78203 | 2024-11-07 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4006a789-e2d6-3153-a6f7-927ef4ad7d92 | -2.84832 | -48.66502 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 61412618-0d9e-3f8a-8a67-7ebe67276a59 | -3.58375 | -50.22876 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c43f2ba-5528-3626-80ec-bf28892f80e5 | -3.03856 | -53.27051 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 658647a2-9b58-387f-90e1-bb510242b624 | -1.33526 | -54.59759 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 738b5dce-4e4b-3b2e-9be4-94ff1d4c9208 | -3.03382 | -54.20826 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a9a4836-22bd-333c-a9c4-5d808b464a44 | -2.24011 | -53.6666 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54f2e063-fbfd-36e5-a5bc-6b4a35f97772 | -1.40731 | -54.49241 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 129e947a-0782-3891-8d0f-e49229acfe3b | -3.57401 | -50.54347 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3a0cd28-bc20-3858-831a-f04b104b90b4 | -3.65936 | -52.3401 | 2024-11-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61ce22e9-0cfc-3080-9750-48da752e42ef | -3.03124 | -53.26937 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79bfdca3-7191-3093-93b1-3907fae9aa23 | -3.09626 | -50.24365 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acdddcef-3f3d-35de-a4bd-57efcac7c3c7 | -2.61159 | -51.30664 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3af0df95-11cc-3ad5-9e0c-437ccfd6412c | -1.84462 | -52.34857 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 024fb8d7-7b5a-34a7-8028-d880cea517de | -2.31942 | -53.881 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca4ecfe4-e89e-38eb-b21e-6ebe065e24bc | -1.41592 | -55.15458 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e56f1e54-4852-3060-8aae-cb28b68b0038 | -2.75014 | -53.22221 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5aa60f64-46cb-3930-b2bd-71bdf3cb9551 | -2.61215 | -51.30296 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53c1406d-4376-32d6-8adc-7b55a14107f3 | -1.59323 | -53.86418 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f58db65c-5304-3e3c-9667-c6d74f48aa68 | -3.08409 | -50.95982 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bca701c0-9ed3-3d63-99e6-18bd05051353 | -1.40849 | -54.48489 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c00af86-e50e-357d-bcb2-9b37abf3e93d | -3.39377 | -52.83759 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1095281-067d-321b-815d-e0a31d382bf6 | -1.47396 | -52.0294 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e44ba57-ea8f-32df-9b63-8ca7a063017c | -3.2136 | -50.30365 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 38a9f421-4168-38c0-8917-fee1002c9d27 | -2.85284 | -48.67907 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 36fb6aa0-18ec-366f-a68d-203d72fa19b9 | -2.80352 | -49.78569 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 67904682-6d21-3a45-90d6-74536eab1f75 | -2.82536 | -52.90401 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bb704de-edca-3227-8573-66383ce04f5c | -3.88851 | -51.96059 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8d75b8f-3b19-32f6-9978-bb928f4e2ad2 | -3.03539 | -54.08075 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 312ca823-94af-36db-88b7-9df8a8b0d502 | -3.18291 | -50.5951 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccf5af1c-2b47-3ac5-99e5-a0326fda77cd | -5.03026 | -46.84721 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 318bcfa5-59a1-3cc2-80e5-1132f3b34985 | -2.54916 | -54.01123 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 262d80d8-35d4-3996-947d-bebb089c8c51 | -3.08046 | -50.95514 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64a744bf-8a45-3ed6-8605-416de836886c | -1.02721 | -47.06009 | 2024-11-07 05:10:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4aeccd3d-6998-365c-880d-dc58fc3f69fb | -3.01063 | -53.43105 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a1c8217-6c16-3f20-87aa-bccb01d9810a | -2.99938 | -51.06003 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcca19c6-0d57-3b84-8051-de484c1db1f6 | -3.16314 | -50.2149 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a11c60d6-661b-39bf-b3be-9683d97409ac | -0.84792 | -52.85051 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9be0c0a7-f1ba-3588-9674-00bc4cf9fe65 | -3.01836 | -54.09821 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b22f3e8f-ed8b-3e53-ab8e-33f2153af4e4 | -3.03188 | -54.08022 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5ab4906-7503-33f6-84d6-622b18cbef07 | -1.14838 | -53.71984 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| df41bcfa-63cd-3fb6-af19-50d1c72c79cb | -0.84924 | -52.84193 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db006bd1-97b2-3119-b484-6f7ba5bfdfb8 | -2.95909 | -52.91334 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ffc5ce5-9669-30fb-8c3c-cce17cb18849 | -1.95651 | -53.0729 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4d15c9f-3a6e-3fc9-8434-56523e31b0bb | -5.04764 | -46.84919 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63e4d0a2-b022-36a3-ab37-5d84cd14c3e1 | -2.82908 | -52.90463 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e473c3f-1c4d-3922-81e7-14bfc924e5aa | -1.32568 | -54.63704 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f482bcec-3572-3abb-a7c3-79dc220e0a82 | -2.82393 | -52.96265 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6e2e43bc-064b-3946-895b-353d4824a906 | -3.03426 | -53.27423 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 96fd7f14-0056-387a-93a5-81dac47bb3b5 | -3.29477 | -53.11097 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d1c3328-015b-3d0e-a41d-52c8d01fbd42 | -1.51729 | -54.51148 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29935956-6f46-343f-a3d0-825d5cfc77af | -2.57796 | -51.33509 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a827fc88-ad7d-3f31-a9f5-2bb49fab9dc9 | -2.01863 | -53.29764 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 023ee67f-09be-3353-bbf5-bbe8e58143f0 | -1.39146 | -52.19373 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a6eee08-fc8c-37a1-80f4-31a3e8198308 | -3.45908 | -50.37499 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 473a2576-2bac-3d74-a3e1-082b63c85a4d | -1.62959 | -53.44334 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adf521f8-dc96-3339-9db9-dd73e510c724 | -1.16531 | -53.72623 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f8a9e549-9fc0-3a1f-a49c-d4d518fb3aa5 | -1.23871 | -54.17951 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5615c04-6433-3f46-afe0-55b051a6e3bb | -2.01847 | -52.35166 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 540bc1e2-30d7-3dbb-95af-f63f96dd96d6 | -2.87895 | -51.30515 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 507576bf-90e3-38a3-afb9-ed00e1e75c5a | -2.93896 | -51.06259 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8e01a3b-8413-37b5-b29d-a0d0f84d4a13 | -3.41834 | -53.03685 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53ed2647-f99a-3d23-9308-a58070af9b63 | -3.1007 | -50.24434 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0e22156-e5b0-31c2-96fe-eb247736eedb | -1.7053 | -52.67964 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3154c22c-7071-3d15-93c6-29a26cbea16d | -1.16301 | -53.71793 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27c37806-af75-38c7-82b5-be2eb2cba558 | -1.511 | -54.80059 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 587a3406-f5e0-3d00-8702-5d36c3e1adca | -1.06324 | -53.65957 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cf774f2-6fce-3cba-98d2-0dfb8abaec1b | -1.41494 | -54.49327 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4c8a66d-eb4d-3531-bd54-f9f5f5c98fa1 | -1.24147 | -54.18279 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README43.md)
