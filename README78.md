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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43d557a4-9e3f-3ec8-a7b5-135ce2e93f8a | -1.61006 | -52.28644 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 777c9b39-8894-3887-8efe-f2d66026869b | -1.37858 | -53.63904 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce9dd4ed-4d76-3bb8-bfc2-f3cdaef4f7f8 | -1.09856 | -54.12564 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2cc1df5-48ce-3843-b959-6259fdae0a27 | -4.44154 | -46.58448 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8e2c06c0-820b-3d69-98ef-cf2fd3fc21a6 | -1.14247 | -48.33133 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ac78c16-a00d-3884-8644-b25ee326aa57 | -1.7126 | -52.47819 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 222096ae-0e10-3257-b58e-3468c20d0451 | -0.99951 | -51.72772 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 687ebf5e-738e-38c1-9dfa-3f74c5d424ba | -3.03445 | -54.0149 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d96e58c5-0510-32c1-8894-b73ba5b57693 | -3.24694 | -53.63321 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3bed09ea-0a89-3498-a254-72bd11601e8a | -3.04704 | -53.71784 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8da3a0cb-7795-3aa9-9caa-2f64ad4b6a79 | -2.53448 | -54.03541 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61e51f62-f6dd-3ef2-8fbf-115f108b8f1c | -1.5009 | -51.9364 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 097e1425-98f0-3ed5-8d24-92d7345871bb | 0.6631 | -51.63622 | 2024-11-29 04:57:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a360c0e4-d41b-37c6-8c24-88641a14e68a | -3.05954 | -53.6811 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d48ad1f-d9a2-3b5d-933a-0eeffe5a02f0 | -4.21696 | -54.76091 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60227939-54cd-36d0-80aa-92a1f5760a4d | -1.10416 | -53.39211 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 01187b20-937b-3014-8717-f2d0c844a7d5 | -2.16774 | -53.66046 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16a2dcc6-37cd-32e2-a865-b2bb4b855dd0 | -2.79214 | -52.99416 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3beed25-08ef-31be-bfee-e88812a66b91 | -2.75374 | -51.66111 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e301788-4c99-38d6-ab4f-160eb4b80fe4 | -1.39116 | -53.62344 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 875ff4bd-d781-3a25-8892-368aba73aae9 | -2.75204 | -54.07967 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f248cb0e-683e-388a-9021-c4e353c70241 | -1.09925 | -53.40188 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44fb7347-4ce2-37cf-8f70-24b51a37ad3a | -3.15551 | -52.44847 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eda47c1-61f7-3953-b06c-9442ec842bd8 | -3.60558 | -51.44112 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84c6e691-bc1b-3d1d-8530-cd46f95d1a66 | -4.09534 | -50.33009 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aee70f8d-60ac-3d9c-842d-500f16011e25 | -3.22383 | -54.06609 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 604260f2-a17b-33c2-9cdf-6bbb2d1476b8 | -2.5996 | -53.96797 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dfd707f-e067-30e0-bb06-39dc20aefd0a | -3.95883 | -49.34431 | 2024-11-29 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82a341f0-5c65-3107-a0b0-1e951227153f | 1.87447 | -55.74863 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bb72bd5b-cf76-346b-899c-89dffd80d2b4 | -1.34202 | -51.66922 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dea1c192-0c59-320e-a76b-d0010912d156 | -5.27921 | -45.12651 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee46e755-1ddc-35ca-aa26-00e329d1793c | -1.08382 | -53.39249 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7e97cd96-418c-36c4-8818-b2580794b943 | -1.6274 | -52.72052 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c4c209b-dcd4-36bf-9af8-cd1266e87b68 | -3.0432 | -53.72077 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16be445d-7bfa-3d2d-b5ac-4bd2123dea8b | -3.00966 | -53.21572 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c01be69-8b36-3828-9c17-10f121a28e56 | -2.86257 | -53.96002 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2178aa5-5354-379f-83a2-db816de1b540 | -1.95186 | -52.97259 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9588256b-208f-3249-9161-8c036dd6950b | 0.03774 | -51.10896 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dd3cf9f0-8911-3958-b5ca-87cdd4666e31 | -3.21981 | -54.1783 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b7da8ece-1d83-3bc0-ac96-b978d4aa3db0 | -2.96489 | -53.93719 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40ee5533-1dbc-3c26-920d-94163012be14 | -3.26859 | -54.10469 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bc0e47c-9443-3c09-8045-bd4156b94090 | -3.52639 | -53.78277 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25e57baf-9d54-39e9-91c0-97b7ed11633d | -3.39175 | -53.27172 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bd221e3-b164-30cb-b8bb-72924d6a7fd8 | -1.62041 | -53.33288 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b71d6dd9-432c-370a-bc43-855b54cfd5c7 | -2.97565 | -53.73835 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1602ff75-9f0b-3307-b9a5-685790e53499 | -4.92538 | -44.52802 | 2024-11-29 04:57:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 150c190d-e44c-3181-9943-0d598830efb6 | -3.70485 | -47.13667 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 961a6290-4b4e-33ea-9d01-134d9fdb808c | -3.35049 | -49.91515 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ce1494d-bde6-32c7-97d6-0e5cc60caecf | -1.2824 | -51.74134 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41153413-79bd-3e78-ac4c-e01dcf4f9c7b | -3.10707 | -53.17774 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1beca968-0fa4-3676-9f06-8257877385ff | -1.27502 | -52.16634 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29e3f253-27dc-3901-a6f8-54c71c77bb4f | -0.12313 | -51.47644 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d67d77e-eaec-3f26-9dd5-ff9fbfb25d1e | -1.63342 | -52.26468 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4907c887-ca97-3864-92ae-0caabddd6c6f | -2.08873 | -48.55073 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 297f0565-b7c7-38ab-8f6f-496c803233d4 | -1.98595 | -50.67025 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1780c651-eec6-3131-878f-afafb0426699 | -1.70496 | -52.6373 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c319b9e4-6d44-3943-ad9d-6033a37947d6 | -1.4739 | -52.65797 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76fae8c2-1700-3921-b213-ad544ad0e803 | -3.16345 | -51.09422 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68045ca6-443e-3fc3-a9bf-96114757ea2d | -3.73671 | -51.83844 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0d99487-f0ee-3b91-9541-5925f601c364 | -1.70927 | -52.47767 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 18b69612-3395-3ae4-8b7b-a2b5fbfd7fb1 | -1.36606 | -52.12606 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bec4152-a51d-39b4-8764-e8e7bb8407a7 | -0.79887 | -53.06009 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 65bb54a7-b28a-373a-aa7f-10401f527943 | -4.26311 | -47.61442 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa35edf5-00d9-3d8f-867d-28ed7079f3d0 | -0.26441 | -51.49044 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d81d37c-e5f8-3b11-89fa-54bcc8541a6b | -1.36885 | -52.1301 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5aff0c9b-0dd4-355a-ad4a-16ca3e454e5e | -3.04998 | -54.04548 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b11f5b9d-b5ad-3832-95b4-593da82c2afb | -2.77692 | -54.03139 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7876bfce-53c5-3724-8bec-539d402f8ef4 | -2.83314 | -54.04005 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 096857fc-9679-3956-8df4-b4fdb82a53ea | -0.07447 | -49.66483 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d58c6cdb-94b5-32f1-893f-431c74c6524d | -2.45936 | -55.28053 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a6fb911-2a16-3b54-9e52-957403685f09 | -1.15433 | -53.681 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa86f309-4724-32ed-bc8a-d08d21e616e8 | -2.75793 | -54.13082 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3736ac60-7d2e-3124-9e3b-766fdb215abe | -2.50738 | -54.16556 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67486a22-2842-3ac9-9b1b-f9fb030b7f8e | -3.59324 | -50.38645 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaa3d1df-47a9-372e-8f32-7c9aa0e5f089 | -3.87471 | -47.07337 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83d1cdce-d870-3bff-95ba-50fdf8079f41 | -1.30143 | -55.74384 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9823aa0f-ef2c-39f0-83bd-92e32a0debe4 | -4.64713 | -47.14753 | 2024-11-29 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c8811e8-e2bb-34cd-9def-2fd31a50e2e6 | -1.00255 | -53.69627 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69ef2560-fb4c-3c3c-83b0-71a0600e3ec7 | -4.43207 | -46.58294 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2a66d155-f757-3010-869c-01b0297facee | -1.21211 | -53.55349 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4ae371de-c852-3bf8-8bf6-9620c184587d | -3.25412 | -54.21892 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a26e0343-1006-3634-a5de-d7380daf717c | -3.10212 | -53.73336 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b453790d-4f5d-32a9-bef7-ce677e2f673d | -2.01155 | -51.1937 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8bf6afc9-531d-31ee-9a9a-196643d4f319 | -1.47071 | -52.35116 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0b053ac-74ae-3b3a-88d0-790a3b8e4ddb | -1.52874 | -55.37502 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad332dd4-7399-3369-8288-72eb8bbf41c5 | 1.45471 | -55.89367 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6ca404b-965d-31c3-9ed0-7521016fa9ba | -3.78676 | -46.68932 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de75bea1-b9cf-3df2-8c4e-98f484d5b5d9 | -2.87763 | -46.86226 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e50952d5-28e1-3cc8-bab6-69e810da5aac | -1.06402 | -53.64945 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a4e01b0-167f-3727-918d-2db84d8fa83f | -2.59223 | -54.23182 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 021ad495-4618-3e3c-b3f1-6ada647cdff5 | -3.51907 | -51.65707 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2dc67282-9b0e-36d1-8ab5-51a1415c7160 | -1.35443 | -55.03207 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98282067-8f65-315b-ae54-d75486888a4c | -3.27934 | -50.04351 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2ef6c815-dfbf-302e-a131-b26863fdc27e | -4.14976 | -53.471 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40f1b052-52fd-3a3b-b5a2-634413467ea7 | -1.61977 | -52.46334 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fee5f18-dfef-375e-aaf3-80981d579bfa | -1.31899 | -51.75067 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f4a3936-16ad-3877-aaf1-e9bf8c3c15a9 | -1.89749 | -53.01711 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e9dbb6c-8d7e-309b-bec8-e4b42fe89150 | -2.79953 | -54.0384 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ccf9557-a3c6-3b86-a2e8-2e02b250c6d2 | -1.288 | -51.72746 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 324a0d34-3b1c-34be-9273-f3d8ce6626b6 | -2.97807 | -53.28492 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README79.md)
