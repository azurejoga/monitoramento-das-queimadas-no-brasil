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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21fea479-b765-3953-9fb2-fccbbd936739 | -17.06764 | -56.84523 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 871e0033-11b7-3357-b255-98369cac390b | -17.06403 | -56.82903 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6aef6bef-45fd-3808-baab-09bb3adc009a | -17.06234 | -56.8362 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 83a934ec-863f-3943-b328-8966b5b23712 | -17.0596 | -56.8304 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| da220ba5-dd2b-3f84-9cdb-f23f75380d07 | -17.05795 | -56.83759 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fccabba1-20f5-3e6c-a70e-b571d42dd2a4 | -17.05534 | -56.83439 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4140c50e-629a-35c1-be52-ec9b8cfdaec9 | -17.05365 | -56.84154 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a8f29e59-0bdb-35d4-84fc-0e07b7953b65 | -17.0526 | -56.82857 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bd75d6f8-51af-30b2-a630-f2b3f08aadb4 | -17.05096 | -56.83572 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 99736bf6-c3e1-379c-8ab9-f22fb9fb9c3d | -17.04835 | -56.83253 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ae869079-b06a-363b-be6b-884cca6d2935 | -17.04562 | -56.82667 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c6956333-30c2-34c4-8685-67655054affe | -17.04398 | -56.8338 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1072d9cb-4a88-3eaf-ba8d-1c6982f81535 | -17.04233 | -56.84095 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| b571c271-7418-3c93-8cc9-240358b18772 | -17.04137 | -56.83064 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f6173e21-6af5-3123-949f-fb87036cd98d | -17.03969 | -56.83775 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ee058410-c687-3ebc-b20a-281d6c8ad119 | -17.15265 | -56.75393 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 26f65e83-43c6-3339-b3f2-b7900e790d95 | -17.15099 | -56.76091 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 73d28f5a-a440-3adb-9e98-3a2a5e2d5a77 | -17.14824 | -56.75346 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 33c32b14-1a05-371b-ab78-1903dc08c0a1 | -17.14662 | -56.76048 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a092d3e8-2a92-3591-ae93-69ef8d8a14b2 | -17.1457 | -56.75208 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 38e2227d-9d46-3773-a3be-3a3e1bd051ef | -17.12889 | -56.82272 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| dcf21c03-821e-36d1-9a3f-295141f808cc | -17.12652 | -56.8154 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 08748bd2-61f1-3d39-8a1a-02b1b17ffb93 | -17.12529 | -56.8067 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 61913560-4c2c-372d-bd4f-e9fdcc09b0f4 | -17.12487 | -56.82251 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 333070fe-331c-3ccf-83ae-631ede57c2b9 | -17.12451 | -56.79215 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| a26c5c4c-92ef-334f-b72f-51b4f1775404 | -17.1236 | -56.81378 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| 713a686d-2e71-3633-8bc2-13379b6d7251 | -17.12191 | -56.82087 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| 2af9f591-5dd5-3726-ac99-c12de0ed8a3a | -17.12171 | -56.79068 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 7f40117f-456d-32e1-b15f-822381930cf6 | -17.1212 | -56.80641 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 3580db65-9fb5-3cd4-afcd-c23a3a0aa8a9 | -17.12084 | -56.77611 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0e347e98-153b-3e17-a58e-b903f72d16f1 | -17.12002 | -56.79776 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| d5722b78-46cd-3c73-9672-f0eef38e26e6 | -17.11955 | -56.8135 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 2c7d0ff2-ee19-3d7b-8c29-5afcd57f749b | -17.1192 | -56.7832 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 84c4e5c1-1850-32e8-8550-31eafe254898 | -17.11832 | -56.80488 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 533f122d-cf32-33d7-9a5f-b7a9cdf8abf7 | -17.11812 | -56.77473 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 5581e8e3-2cff-33e9-91a9-a031e44f23d0 | -17.1179 | -56.82063 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| c90ad7e8-6310-323d-909f-cad43c39cfd9 | -17.11663 | -56.81195 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| a42d9107-6e1c-388f-80eb-38ca74e06bb6 | -17.11644 | -56.78178 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8e82b197-28c9-3323-970d-5853a455ba85 | -17.11423 | -56.80453 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| d7697bb5-5522-3761-b9b2-1f0add77d9f5 | -17.08833 | -56.8203 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7f19191e-553b-3a12-80d6-a8354a1f492c | -17.0657 | -56.82193 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f9ae0a80-325e-34fd-9714-f3f621ba12df | -16.86839 | -56.74278 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4033cde6-9597-3bb5-887d-85a039c694ce | -16.86464 | -56.74055 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 43dc93f3-912f-345e-bd3f-368e12b1e0ec | -16.8614 | -56.74096 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 188eb6f3-6c77-378b-92f8-68124d0908d4 | -16.85602 | -56.74584 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| cade4281-746c-3cfd-a825-e0ffc2cb76a4 | -16.85442 | -56.73912 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6753def0-e65e-3b8f-bf04-29f9c69b7066 | -16.85274 | -56.74628 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 34430547-1d70-388e-b5f7-1b88cacfa85d | -16.84904 | -56.744 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e5fe4864-38f7-33b0-8c19-c1346df59d68 | -16.84744 | -56.7373 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| be0b040a-3919-3e0f-8bb1-fd87a8a9735a | -16.84739 | -56.75117 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a0f8d626-7978-3d20-804e-f7a8f405dc89 | -16.84575 | -56.74446 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 12e48512-7957-3914-8a17-50371f57745e | -16.84407 | -56.75159 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4ef69ba4-3ef0-3111-9e78-07716141f4d6 | -16.84206 | -56.74214 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 22724182-eb61-3384-92c9-93e3eef7f171 | -17.03099 | -56.84307 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 941884dd-94fe-3762-a117-b8a8aa972a0e | -17.0267 | -56.84435 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7822fbeb-32fe-3d54-b455-9dff488afe98 | -17.02399 | -56.84124 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c2a4e7ed-25b6-3219-97e2-a8676967a9dd | -17.0197 | -56.84248 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 57d3bec2-5070-3f7a-aad4-978ebfc075f1 | -17.01699 | -56.83943 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6fdd6be3-948c-3d0e-945c-04ef5dbe4314 | -17.0127 | -56.84067 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 58499859-4421-3d1a-afe5-74c27d69d055 | -17.00998 | -56.83764 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d02970f4-9202-3a35-b03e-9635b7ec02b9 | -17.00917 | -56.69658 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ae532737-5381-37e4-9f8a-2fcd8f0d91ad | -17.00827 | -56.84481 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e55e9fb4-87da-3c8d-bdd0-152d0e0f6c73 | -17.00568 | -56.83887 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 591fd782-a1c8-3ab2-9f76-252d971f8001 | -17.00297 | -56.83586 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 39c41b32-3900-3d25-81bd-c2a7f5d1ddfe | -17.0026 | -56.72476 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6257ac94-e14b-32f0-9b2b-caaee02dc2e8 | -17.00222 | -56.69475 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d4ca7307-a065-3df8-b2da-f642bf3e3a52 | -17.00096 | -56.73182 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 11eee2e5-9eef-3e83-92af-d91dbf762550 | -17.00058 | -56.70179 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 579bf80c-c348-3d12-8e7f-2fdc77c444bb | -16.99893 | -56.70886 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 793cda0c-016f-3c93-a4a4-f7f300b6715a | -16.99729 | -56.71589 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 90d364a6-2077-32af-a734-11b49534f317 | -16.99597 | -56.83402 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d38a530c-6edc-310d-bbd9-dcbbb37f6f9b | -16.99564 | -56.72293 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d8e931cb-8573-3157-9f22-4da53cfa978c | -16.99399 | -56.73001 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| be316158-fe25-320c-b6ae-04a5dc22be35 | -16.99362 | -56.7 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 940b3a05-25b5-3620-8b4e-93c7c766d855 | -16.99233 | -56.73709 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dc0cbf04-8333-3b72-a1fe-97a2a5af0115 | -16.98867 | -56.72113 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 178a4ddb-1e00-3541-9934-b3388c55a2e8 | -16.98537 | -56.73527 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 50e3edd4-2449-3464-9d1d-07487242574a | -16.98337 | -56.71225 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8e6c1354-dbf0-37c2-b03a-dbd7c06f74cf | -16.97406 | -56.81521 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2cbd55dc-584e-3c8f-9d9c-d1af51f3d2e7 | -16.96874 | -56.8062 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4945eea4-41ee-330d-860c-a1c758862d89 | -16.96773 | -56.76151 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 5d30bb4f-1ed4-3da2-b6b2-65f208c7e2aa | -16.96707 | -56.81333 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 0ffc7a0a-b8f4-3a24-80a1-8775c4fe3501 | -16.9661 | -56.76861 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6911a957-885c-35a8-904d-e4294cf704ad | -16.96539 | -56.8205 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 6dcfa0e9-add2-315e-9338-e5a6319ca533 | -16.96478 | -56.75992 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 67e4b20c-b66b-31c3-b7a6-a13553019488 | -16.96342 | -56.79723 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 22129e75-9386-3954-99c4-200a7f7bb2ad | -16.96311 | -56.76701 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 12f375d8-41a1-3f0f-bf75-8583b1fbe465 | -16.96286 | -56.78282 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ee2199c2-6ee9-3203-acea-324d753c48b7 | -16.96123 | -56.78994 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 93f2cb03-9db7-315f-9ed6-b5c2dade5087 | -16.95978 | -56.78118 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| c0637fe4-bdea-3f14-9260-b157f90a992d | -16.95913 | -56.76675 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 07c7e48c-7d5f-3d70-b4e8-9d3f91ce1c4b | -16.95811 | -56.78827 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c287606d-ba1e-30b6-87f2-52ec04892894 | -16.9575 | -56.77385 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 071c9b37-cd0a-315c-9b53-c1d06966e95d | -16.95587 | -56.78098 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 77674fb9-6024-3a6d-acfd-2abd0bb2117e | -16.95425 | -56.78808 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 090774cd-3881-3684-911c-9c12660d8526 | -16.95279 | -56.77935 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0a18f8e6-5d6a-3d49-874f-2904a569a72b | -16.95112 | -56.78644 | 2024-10-07 04:02:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3f78e98f-e1bb-303a-933c-d700f88d8e74 | -14.1022 | -45.50387 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 71de40fd-0918-374e-9d5c-5fbeaf3f26db | -14.10185 | -45.51974 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26ec4131-6861-3f2c-90c8-f4e6562f1752 | -14.1006 | -45.51293 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README63.md)
