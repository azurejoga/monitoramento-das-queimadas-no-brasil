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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56670572-dd3e-334c-9f61-d5d7f7d18e56 | -3.16381 | -53.07133 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1f129dc-d352-3319-827e-2843494389a9 | -3.11622 | -53.17586 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4aba30e7-8e05-3c32-9fd9-5163fe41fa3e | -3.10482 | -53.05455 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc093426-a895-3f33-9098-0a9be02ea2c0 | -3.10037 | -53.03977 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9a2cf10-7848-33eb-a0e0-3218127b7ef7 | -3.0801 | -53.06126 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbaa3f74-e73c-3dec-999b-99516c510b02 | -2.35217 | -51.98972 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50c6eb37-d472-3efe-8755-b14ac2f59222 | -2.32728 | -52.89372 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26f4954c-7861-33bf-95f7-12e6aa2ea7e7 | -2.32398 | -52.89321 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df4a061f-ab8a-3bb5-a521-379ffe7898d9 | -3.06379 | -53.27314 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e5bb731-e1f1-3d38-af28-2ebb51d8e71b | -3.05329 | -53.25395 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c3c9201-5b2b-3200-9c31-b0b592436405 | -3.04259 | -53.03776 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f3c0b81-d47c-30d2-9d36-eaea53120ad7 | -3.00666 | -53.44338 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 664e89a2-507b-3ef5-b948-e90995ec1e62 | -3.0006 | -53.43893 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3eff6584-add4-391d-a775-c3597aba800d | -2.99731 | -53.43842 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2c07e72-41bc-34dd-b95e-ce3141027299 | -2.98618 | -53.26798 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51225271-380e-3f39-a151-3acb4f795c65 | -2.98342 | -53.26405 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9dcbaa00-6a47-3a08-834d-20ee8a284a8a | -2.98288 | -53.26747 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b89e94c-13e8-38d4-9b9f-5a1de18e064f | -2.98012 | -53.26353 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 492857b3-a626-395a-8f1b-9f7fa5f3d166 | -2.97958 | -53.26696 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f8694d5-2714-3e92-b00f-c88bd0de095d | -2.97628 | -53.26645 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95404969-8922-3ae4-9d05-e36b4b4f8ba0 | -2.97299 | -53.26594 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fafc682-0d74-3879-91c5-49e0aaa3f580 | -2.97245 | -53.26936 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 259a6e20-369f-3731-95fc-7c4e5c2e95f6 | -2.97165 | -53.03731 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36cd1f98-8576-3f56-ab59-d4d88f2f79c3 | -2.97057 | -53.04417 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68111f13-678a-3343-a723-2b2c5d1c19b1 | -2.96969 | -53.26543 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 709cf0cf-fea4-320d-9207-9284a627f6f0 | -2.96835 | -53.0368 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b0767cb-e059-347a-81db-3dae670ef506 | -2.96727 | -53.04367 | 2024-10-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0acd601f-c7a9-37de-b15d-4846a79d2e20 | -4.21249 | -53.45805 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ab0bc18-e300-3abf-8982-f63e3b751347 | -4.21195 | -53.46149 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f0f0279-f91e-3e45-8a85-31429238b4c5 | -4.21141 | -53.46492 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b16eec41-1a5d-3c0e-9fc3-8a90d3fa9a7a | -4.21087 | -53.46836 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bd838ca-a5c9-3618-9dd8-9003093d2271 | -4.20935 | -53.86557 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 653c3603-2320-3cbc-919e-2300c6871c7b | -4.20919 | -53.45754 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f1dfcdc-9b29-3704-ae1d-2ce3abd3fb9a | -4.20865 | -53.46097 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd0c56f3-47ab-3891-8582-f4d8121bced2 | -4.20811 | -53.46441 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27633adc-5368-3da8-aee1-f793d6696283 | -4.20757 | -53.46785 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 314ec7b0-30ee-342d-8511-2fa1f7ff5098 | -4.20605 | -53.86505 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed5b65e1-4a2e-3f9a-8884-8396f76319e3 | -4.20589 | -53.45702 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 308e833c-2a51-3c7c-b787-bca4108a5bbb | -4.20535 | -53.46046 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36da8727-cab8-36c5-8b6d-4084c87458e5 | -4.20481 | -53.4639 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba743202-e4fc-3906-b2c8-e473b209d94d | -4.20427 | -53.46733 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9806f4ab-6624-3781-8f34-7c96faf540eb | -4.20222 | -53.86796 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 551e02c8-a57e-3515-951d-b313d30c9f70 | -4.20205 | -53.45995 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab408513-389c-3059-a5e2-5b75952e7f57 | -4.18325 | -53.77361 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa43671c-f832-39d3-9ade-bef3940f866a | -4.0456 | -53.41378 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe0e9b44-4871-3b09-9e41-d703c43ba8c9 | -4.04506 | -53.41722 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f0e39d5-ed25-389c-9e32-53299fdfd7f6 | -4.0423 | -53.41327 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8f5d53e-6553-37dc-934e-192002ac0e09 | -4.04176 | -53.41671 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73a60e3e-185e-3039-9038-fc4f43a2a82c | -4.38262 | -53.65416 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f89c15b-6abf-3436-9940-f5725ac908a0 | -3.9378 | -53.47096 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc1f62da-6fbb-3840-a2c6-39dd42d4ab49 | -3.90531 | -52.39611 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 222dfe33-1183-3bbc-9eb7-82cb9c34dd15 | -3.90476 | -52.39963 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 472a8348-7c0e-3d70-9a3a-5102d4b84573 | -3.89444 | -52.81431 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b68f37-fbe3-34a7-9fd5-c86c09a8daa9 | -3.88971 | -52.3864 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fb8a0c3-e1be-3598-a07f-f555482c6fea | -3.88745 | -52.37888 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0715b69-43fa-3fa6-ae5a-c3c2121fa1d5 | -3.88691 | -52.38239 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cd4e06c-9839-33fd-a8e9-d9e10839ac97 | -3.88636 | -52.38589 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 825bca2e-d84c-30e9-ae0c-589dcd83897e | -3.83852 | -52.40744 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f92c4bb8-c394-3e5e-a45e-d3c129881e60 | -3.83518 | -52.4069 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43c29a1b-d318-34d8-8400-70a6c70669f6 | -3.77595 | -53.42112 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acfb6409-2eae-304d-9054-06c1af607c45 | -3.75322 | -53.40988 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc99e054-6029-3200-a226-db35b7fbef71 | -3.75268 | -53.41331 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c63702fe-44ef-38d4-9b0d-b7952f7cf684 | -3.74938 | -53.4128 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45fbdfcc-544d-354a-a9e5-7e073cf3bdde | -3.74386 | -53.40491 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61c64ffa-ad44-324b-ba92-0587c9c426c4 | -3.74056 | -53.4044 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57135cd6-c0a4-3e31-af96-e5763d17e539 | -3.72238 | -53.39103 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9edf47b-682f-3f64-8d66-1e5e142f7b14 | -3.71909 | -53.39052 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b80d2e5-9c9a-37aa-b20c-b3cc03331a2b | -3.71048 | -53.75193 | 2024-10-28 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4f44035-595f-38b7-bf40-0043930597e7 | -6.16959 | -53.58303 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d23c85fe-4a1b-3223-ab5a-09655de7b243 | -6.16629 | -53.58253 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71bff4b6-11ee-3ee4-9cc8-257d74dde1a6 | -6.10352 | -52.82622 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d2c7c6c-3aa2-3f05-be40-dfc27b190d26 | -6.10296 | -52.82981 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d7bde5e-ce25-34a3-8c30-514f3f93783c | -6.10073 | -52.82209 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db5d97ea-a18e-32a1-ab2f-83aecafcac57 | -6.02786 | -52.8109 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaa5bdee-d3bd-34ab-bff0-ea1cb7ddc69f | -6.02451 | -52.81039 | 2024-10-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3187450e-1f4a-3438-beff-5e4f56af1bae | -5.83193 | -53.39088 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6197c62-91c3-323d-814e-09aaf45eefbc | -2.2539 | -53.64099 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84ce8b32-17b0-3021-a059-36cf47e5e7b6 | -2.20612 | -53.68645 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 56440bed-bc07-3ad7-8dd8-378abf862a82 | -2.20558 | -53.68989 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d0f27a64-5636-373a-bb0c-22039e931e1f | -2.20282 | -53.68593 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8adb33c6-925f-3c1c-be2b-927636a0895e | -2.20228 | -53.68937 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 87a76e22-b7a2-3d8a-a996-6a601a6722a0 | -2.20173 | -53.69283 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 09c018f2-848d-36ab-b988-759c42212015 | -2.19952 | -53.68542 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df39613a-d1c3-3929-97bd-e5033834b4aa | -2.19897 | -53.68887 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe821732-90b9-3f4d-bd37-9a5bccc9791e | -2.19843 | -53.69231 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64654809-0f5f-30ac-800e-a561e1cb9ab7 | -2.19788 | -53.69575 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0eb1be0c-d659-3b35-a383-830dfb7fad7b | -2.19734 | -53.6992 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c95cdc8-b10e-3ff1-96dd-5e1e01e4e842 | -2.19408 | -53.71986 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e11431c-dcfd-3b76-809b-63bd1218097d | -2.19354 | -53.72329 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28087f37-43e1-3962-9a58-7c5f41a7ebf2 | -2.18969 | -53.72623 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eea73213-d837-38f8-bc68-ff31a40e7c76 | -2.07647 | -53.55634 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e48d33a-fe9b-3582-94a2-1dc2b8100ad5 | -2.02632 | -54.92894 | 2024-10-28 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec7f409a-3e49-3dc8-b8d9-7892aabf358c | -1.95952 | -54.04074 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3153cccf-8a49-3b89-b575-8f0978f462c6 | -1.95456 | -54.05062 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d111222-fe15-33a1-ad1c-ba2eab17da33 | -1.90736 | -53.53005 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9129d0c8-b653-3725-a551-59a368a011c2 | -1.86712 | -53.76365 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40512b42-6244-384a-b65b-d694022218ba | -1.85954 | -53.72348 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96db0326-a989-3eb7-91de-0352d7612acb | -1.859 | -53.72693 | 2024-10-28 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee07c230-df52-3dbd-8a76-bd4fcabcc8b4 | -1.17912 | -53.89634 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5307803a-847b-3d6c-8b54-681cf361a960 | -1.17857 | -53.89981 | 2024-10-28 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README65.md)
