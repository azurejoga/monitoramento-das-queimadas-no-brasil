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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47a81fe1-9ffc-3111-bd6f-c79b99db55e0 | -5.29755 | -56.01262 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a81e7379-1d58-3bd1-8db6-5bd576c9cc72 | -3.20414 | -61.22925 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7297ab9-a2cf-31b2-81d7-7ffde0b5923f | -3.79474 | -55.8782 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4afa97f-61d7-33e1-9e71-7159982de847 | -5.65738 | -60.24017 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 66fc8487-ed1b-311d-a3ab-c3d399da1a1f | -5.34915 | -56.03146 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1c89949f-c869-37b4-aa15-e93556bdaa6d | -3.76303 | -61.75638 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49d3b57d-134f-31b6-be31-bc9c305cbe05 | -3.22965 | -50.57459 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7381795-6c4c-3a5e-a97e-6f8d47c0970f | -3.07657 | -61.08553 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31e60c0c-ff59-3333-9098-9a33471a15ba | -1.95764 | -50.20135 | 2026-09-05 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88e061ae-3d12-3169-ad57-bce315d085cd | -5.59992 | -60.24366 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbb01256-24fb-304d-9f36-4425f2169507 | -3.39028 | -54.72145 | 2026-09-05 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27bb96cb-56e0-34f7-808d-249ac17e0926 | -3.89191 | -52.03276 | 2026-09-05 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad9cf2a7-2660-3bee-a0ba-bdf4b76eee8b | -3.71578 | -51.13581 | 2026-09-05 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49ad575e-0d54-3718-b77a-c6c5fdfeda41 | -4.65579 | -55.74543 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a5f61a7-b80c-3f22-bbdd-80d6b65ecd3b | -4.65249 | -55.74492 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14cec71a-8852-33d8-9b50-b26e5e63f54a | -1.47636 | -54.25771 | 2026-09-05 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33be0ac7-2c68-37eb-b2e6-c6aa0838c9a6 | -3.52636 | -50.19791 | 2026-09-05 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3671078-1537-3f89-818a-d16f6b7ea83b | -5.29641 | -55.99831 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c5bc0c8-024a-3081-960c-df1ce69475a7 | -5.14712 | -55.95328 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c55f4a1-a9b2-35cd-a2f1-a1569aa50954 | -5.3014 | -56.00969 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58fe49e6-529d-32ea-b897-72fb1561425e | -5.28655 | -56.01798 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20bd37a6-a808-3e02-a4d3-2fd9b9b27267 | -3.44173 | -52.81073 | 2026-09-05 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 133d137e-ab13-3435-a087-3f3daf3e7a22 | -5.25328 | -59.98122 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d912d2d-de18-3932-bad0-d68c88ef69b2 | -5.30971 | -56.02158 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0512bbf4-64ed-3764-8aee-ca9e98e0ef1d | -4.10451 | -60.65782 | 2026-09-05 05:04:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e0da0e9-cace-33da-9d53-ba9fbb4429a1 | -2.80586 | -48.67247 | 2026-09-05 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94c7c15f-1fe2-3aea-883f-b60281ddd542 | -3.77557 | -61.76284 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce8d048c-6a21-3a65-a948-4e2e2f8263b2 | -2.80965 | -48.6775 | 2026-09-05 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 48c0a770-7906-3c14-a19e-b3fd113b985b | -6.35405 | -46.11432 | 2026-09-05 05:04:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d4c8141-e200-3f21-93cb-6271747df105 | -5.9275 | -47.89108 | 2026-09-05 05:04:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0c42d305-4ca6-34f8-8f80-fafb6b798751 | -5.17443 | -56.06013 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 048240fe-bd4c-3145-9a54-52fb26578b85 | -4.15722 | -49.70282 | 2026-09-05 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f1873e7-fb8a-3c47-9fbe-9601088ffaa2 | -5.29533 | -56.00521 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f890305c-2442-3633-aef9-9765519a8ead | -5.15096 | -55.95035 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea99f467-edb9-3fa3-a4a2-69c9c140c688 | -5.3064 | -56.02107 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0613d0c-52f2-30ff-b34a-db988bb3414b | -1.94618 | -54.05697 | 2026-09-05 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c1e0f99-0a83-39e2-b32b-75db63d3f980 | -3.38137 | -61.33587 | 2026-09-05 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20724768-0bc5-3bb9-b0d8-6e5aedc1700a | -6.12873 | -59.92676 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 267dfd09-ed3d-319b-b639-a4738ae0c692 | -2.50208 | -54.7913 | 2026-09-05 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ebd6f17-ac65-367d-85f9-d1fadecca199 | -5.30032 | -56.01659 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77fc09e0-578e-3a67-a710-897579765e0f | -5.31301 | -56.02209 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 785bcb5b-98ad-3303-80e7-17e1e5d9d576 | -5.59684 | -60.2381 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 204914b4-fde1-3963-99fe-2fe59aa9f92b | -1.83648 | -50.65393 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a341c896-4e42-3a07-b349-5de86f3e51dc | -2.89831 | -57.18482 | 2026-09-05 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a659bd9-faf5-31ee-a562-6f06ace3e911 | -5.15373 | -55.95431 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 795ce462-ed06-3872-91df-16f151523156 | -3.17101 | -61.14571 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48b51efb-62a6-3936-bcbb-c0bb8610b15c | -5.29364 | -55.99434 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a17ad7e5-ffea-3197-9cbe-3680d23dfe7e | -5.15427 | -55.95086 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f5c7b5c-dacd-3d1f-b99b-6b0f065c4796 | -5.31409 | -56.01519 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c335203-7e82-38da-a02c-92ed040699af | -5.31025 | -56.01813 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09ca6f64-d957-36bf-bd19-38bea8f7c631 | -5.46433 | -60.04456 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42806cc4-a4a9-3651-ac8b-5ab2e99cdd58 | -6.15368 | -59.94043 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cc45f1f-6221-332f-af59-5f9696b94216 | -3.19917 | -61.23262 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 457b613e-5a7c-3a6b-a88a-a643dc30d143 | -5.16781 | -56.0591 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3addb4fc-2bde-3936-9ca7-533d23ec2d29 | -5.326 | -56.02786 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b8b2d17-79f1-367a-8d1a-3b22eabd8606 | -3.13928 | -60.63947 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7c5c0229-c4ba-3ce4-8c6d-33bcc928172f | -3.77115 | -61.76212 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8382082c-a274-37bd-8833-c589d7f85e4c | -3.44465 | -43.26192 | 2026-09-05 05:04:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d28d9dbe-1edf-3da3-ad39-cba334a932b4 | -5.31355 | -56.01864 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 396bf4c3-15d1-3edf-88a4-dc1e6cfe348a | -3.24249 | -54.31483 | 2026-09-05 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4db4689-4d64-34cd-a264-67b34a993abc | -5.33754 | -56.01905 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7349c350-d66e-34a6-9efe-264b9884a32c | -6.12417 | -59.93079 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cda5cbbc-b7d4-3b0e-abe3-7ac488b7088d | -3.07959 | -61.17691 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c460325-c726-3481-853b-18077c1d1b32 | -1.67266 | -55.50608 | 2026-09-05 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31233a5d-0d23-373f-9888-1262827888af | -3.13621 | -58.6363 | 2026-09-05 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e66623c-c43f-3a7d-944f-2261546b05b1 | -5.31963 | -56.02312 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d88cb2f-e0e4-357b-bc66-62362e479e14 | -5.31078 | -56.01468 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c39e536-9362-3fbc-b7dc-b813fa34a904 | -6.51596 | -58.29747 | 2026-09-05 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a09f91-9002-3da1-94ec-5ce5427cece3 | -3.43825 | -52.81013 | 2026-09-05 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5bb00d31-dee7-3d35-8bbd-5a9ea64b5de6 | -3.46303 | -58.86427 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6f68952-494e-3f7a-b282-b99d88fc6080 | -5.84135 | -60.25047 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea7d2cac-b9c8-3fd0-8756-78c440d8383c | -1.41815 | -54.21634 | 2026-09-05 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f921bb49-8fb5-36e8-9e93-829068226f6f | -3.07166 | -61.08883 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d9ebbcd-a940-3e9d-8a16-0d33d6da4385 | -5.46965 | -60.06018 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 606e870a-d0c5-3cd2-be7b-5670ff52d342 | -2.99044 | -60.94637 | 2026-09-05 05:04:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bed33c8-0935-32ca-94cb-ffbe0ecad638 | -4.67354 | -55.63183 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 197d0d22-c5b8-391f-a575-53a696e2062f | -3.41588 | -54.77488 | 2026-09-05 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61c36d73-823c-3146-8540-142c44d66dc6 | -3.76971 | -61.7708 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8fc0c06e-8be9-3bf8-a00c-6c3434ddb7ae | -6.02697 | -60.169 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 12edb2f8-cb72-361a-9ec0-6b8b5187036b | -5.1722 | -56.05271 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6488678-29b4-3b51-bdcb-9d5708accd41 | -3.08755 | -59.30891 | 2026-09-05 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7195fbc3-c9fb-395f-9cbe-dff6b114acdd | -5.92673 | -47.89657 | 2026-09-05 05:04:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 88ed3ac6-7074-37ca-8ee6-ae49ba7665a1 | -3.44309 | -43.27246 | 2026-09-05 05:04:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3711e056-9911-3b2d-a898-74d9b91e345b | -5.85626 | -52.05389 | 2026-09-05 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88073f56-acba-3cab-9237-5e957f3bb67c | -5.76419 | -59.17957 | 2026-09-05 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03c492d5-e7b8-33bc-893e-f2290d46c8db | -2.82672 | -46.71094 | 2026-09-05 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42be040d-7ee0-3bf8-9bdc-136fe5a73d76 | -6.13234 | -57.69033 | 2026-09-05 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9efea975-1d39-3989-b980-343058d3b69b | -5.33923 | -56.02991 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 54ab86ea-6b78-3145-8fdc-3cb7228dc100 | -5.3224 | -56.02709 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4918f3a9-f9f7-3ba9-aa79-4b5f4c5bb5a0 | -5.31578 | -56.02606 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1982ae75-0da7-378d-855f-fffb7da00013 | -5.17713 | -56.04286 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e2f82b0-0096-36b0-933a-66df37ae5290 | -2.81474 | -48.67383 | 2026-09-05 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 177ef3d0-96ac-3d8d-977a-15054642d4d3 | -5.33369 | -56.02199 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1de7646d-5c75-3767-88b2-8aa2839b9033 | -1.02017 | -53.73548 | 2026-09-05 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0bb94ee-4e9b-3f7a-998e-30bc88ce3ad9 | -3.23079 | -50.56818 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b790bda-5a57-39fe-9fcb-93b72a95b455 | -5.55986 | -60.17207 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e8ffc34-b7e6-3376-b01b-67b14043e79e | -1.41761 | -54.21981 | 2026-09-05 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40a2dca2-5521-3e70-a74a-eedfa6704cf4 | -4.48987 | -55.08445 | 2026-09-05 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e82408b4-ea21-3530-8d04-a5cb0abb78cc | -5.43335 | -60.18345 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f3ffa38-39e6-3cde-be27-740751bab6a9 | -1.77519 | -56.24362 | 2026-09-05 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |


[Clique aqui para ver as próximas entradas](README21.md)
