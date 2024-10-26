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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 367bf400-b972-3b0e-988b-44c696acee96 | -3.21399 | -50.17571 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8805f064-dfea-3751-846b-9afad71da197 | -3.21122 | -50.17176 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d1817ee-8496-3003-957e-f5f20bf0ee22 | -3.21108 | -50.30187 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb04d798-0c89-3cbf-b96a-6e4f609a8c6c | -3.18164 | -50.20938 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d8dd34c-ebff-3a47-8b03-cdaafa3e2836 | -3.16859 | -49.53215 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be1fa8b7-5825-38cd-bf97-38efbf8388d8 | -3.1623 | -50.35406 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0838dc9-f9b8-34ba-9090-1324165e8f42 | -3.15822 | -50.46595 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5349838b-8c51-3ebd-b52a-1f75c17788c7 | -3.15503 | -49.77129 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 829b381b-a393-3fb8-b144-d703391db280 | -3.15449 | -49.77474 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 430e151a-0a79-3afc-bcfa-eefc77d83bcb | -3.15162 | -50.46492 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6300e582-d9b0-3078-a278-9a47e6314555 | -3.14994 | -50.45411 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f548be17-dfe4-3c71-a54b-724e91430030 | -3.1494 | -50.45754 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14fa5b02-7597-35a3-b547-1d2895f1c359 | -3.14886 | -50.46097 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f270fb6-2363-3c8a-af82-e3d548c3198f | -3.07315 | -50.50856 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e7f13d3-0c4f-35d4-bf8a-0d6dcada1964 | -3.07039 | -50.50462 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85b0bbd4-bda6-3010-a935-510bb3162e24 | -3.0621 | -50.49277 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5a63d8e-3162-31ae-a459-d559810a128e | -3.04275 | -50.27173 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75542a43-23b3-3f3a-adc1-99cac6d8e3e5 | -2.72027 | -49.38081 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42f60339-7358-3e7c-b0b8-66a20e39d420 | -2.69243 | -49.31944 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 162a544b-ec0f-3b25-ae7e-7af6cae00ee1 | -2.66236 | -49.27191 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eddc44c3-9412-3c10-ba6a-e0b8e1e3fb7f | -2.66182 | -49.2754 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a0a351f8-a624-38d1-84ed-bf448a045756 | -2.66127 | -49.27889 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6ade29c4-0937-31b2-9c33-81068345c915 | -2.65869 | -49.51351 | 2024-10-26 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c94eb2b1-c794-3a74-8bf7-b597efbbc803 | -2.65849 | -49.27488 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e431956-8b74-38e7-a28c-23b9eeb9940a | -2.65795 | -49.27838 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d63e231d-2350-36b1-ae8b-9f32c076e791 | -2.65591 | -49.50953 | 2024-10-26 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 56f52db9-9c51-3ce2-b28f-ce2466dd775d | -2.65516 | -49.27437 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9989932d-59ae-33fe-9c74-82cfe11cf8c1 | -2.65462 | -49.27786 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62ec1a56-9f3b-317a-84b5-379502cb6701 | -2.6527 | -49.27011 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee76582f-71e7-33ea-8fc6-cc3c87ae633b | -2.6526 | -49.50902 | 2024-10-26 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b315d673-cd21-3bdb-92f0-e6e5b89d23ae | -2.65205 | -49.51249 | 2024-10-26 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 145b41f2-6a99-3db8-b639-e7959e92ab80 | -2.63935 | -49.2466 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3124dd2-b3d4-318f-914f-316eb6cd93b9 | -2.63712 | -49.23909 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2cca862-9de9-3917-bc61-a218ea3532a8 | -2.63657 | -49.24259 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d689564-a5a4-3481-ad43-71b33eb47af5 | -2.63602 | -49.24608 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 476aa82f-0493-3026-b0cf-cc8e936a3046 | -2.63383 | -49.26005 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a9091ad-3529-3dcf-aa4e-b154f1d1c574 | -2.63105 | -49.25605 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71f7bce1-26f7-3726-ac75-d40b12bd4c81 | -2.6305 | -49.25954 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a790ded-f4d7-3cc5-b621-843db3238400 | -2.62881 | -49.24855 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89a37ef7-3375-3de9-9502-5f565eccccef | -2.62827 | -49.25204 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6155a53-094e-3c06-b8dc-5fc517abf102 | -2.62439 | -49.25502 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 175f93b8-e04a-381a-8e29-5651da961509 | -2.58941 | -49.23888 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7a01817-8631-317f-8d92-7697cb85806a | -2.58663 | -49.23487 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75108812-a06a-3330-bb00-0056177a85ce | -2.58608 | -49.23837 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d68074d4-db2c-320f-9082-a9f0d61365bf | -2.58275 | -49.23786 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4cc87e27-6f4c-3efa-b453-9cf694cf5c16 | -2.58263 | -49.19487 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5d038c7-7181-396f-b408-adb2cc7dbec9 | -2.575 | -49.24381 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acda0974-2be0-35e5-bb41-4b5d62b54355 | -2.57331 | -49.23282 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6347076-4dcb-35b5-b475-6a48e723127a | -2.57276 | -49.23631 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7272fb1-a245-3cd8-b237-681ac1f17e77 | -2.57167 | -49.2433 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3a490f2-10d3-3ea7-b7d2-578373035f1b | -2.57052 | -49.22881 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f794262c-79f4-3079-b34b-5f66d31cb7e4 | -2.56998 | -49.2323 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34711f40-400f-34da-a676-0d7467e56d2e | -2.56943 | -49.2358 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d92f04e-bf27-316e-ab32-4e9bcfc0687c | -2.56719 | -49.22829 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a166a14f-82d8-3da9-852b-8eaa0c06a30a | -2.56665 | -49.23179 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5218f08-b5f6-31ec-b165-eb36ae6ef6d5 | -2.5661 | -49.23528 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| adc90c07-1568-39bc-9885-169a59ef7a7d | -2.55347 | -49.27266 | 2024-10-26 04:42:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93b28c86-91fd-366c-a1da-935b7aad5175 | -2.39705 | -49.20948 | 2024-10-26 04:42:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4c0780e-81ee-3b5d-a276-45ad77ff6d27 | -2.38701 | -49.18647 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b39f071c-de57-3782-9ad5-f1b591ad14e2 | -2.38693 | -49.38257 | 2024-10-26 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13f7c503-956f-348a-bcbe-bbca85b0f11f | -2.38639 | -49.38604 | 2024-10-26 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fac95441-c3c6-30fa-a3b7-b3073ae19334 | -2.38584 | -49.3895 | 2024-10-26 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9765dc82-f1e0-3d8a-a151-12c344f0af9c | -2.38361 | -49.38205 | 2024-10-26 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7082f54-ca43-3193-b5d0-e6aa38887eaa | -2.49911 | -49.12163 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d783bc86-9f61-392f-93ac-4afda18a993d | -2.49577 | -49.12112 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27899ad1-cc74-3d75-970d-0e24fd26349d | -2.49189 | -49.12411 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 083132cc-3c12-30f4-a56e-60e07855a694 | -2.49166 | -49.03773 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd1a3494-0b6b-3f4e-9051-29cc3c84c5c3 | -2.48965 | -49.11658 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ca4e38f-8584-333a-8986-bdd292d9d85f | -2.47461 | -49.10348 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1593a054-54eb-33d3-99f5-60a5b1fc54a7 | -2.47406 | -49.10699 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 482b19a3-6713-340a-8d8c-73e5f7fb26c6 | -2.47127 | -49.10296 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 38ad337f-4f2f-3f91-b23b-82a743d21724 | -2.47072 | -49.10647 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e2204731-f320-3d0f-8998-1794800e5930 | -2.46793 | -49.10245 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5ed5262-7a16-3375-8ecc-e3ffd461038d | -2.46739 | -49.10596 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c7104b6d-d671-3ab0-a1d3-be08c5d9ab9f | -2.46684 | -49.10947 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e10238d0-eb63-3656-a08e-a9d1260f354c | -2.46405 | -49.10544 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd67fde6-de8a-3d83-8d72-d0af515d9f48 | -2.46118 | -49.01834 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b811822f-28cd-388d-bbb6-d13fdd14e4e4 | -2.41973 | -48.889 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f735e6c-8a16-341c-aa61-91632e0a8558 | -2.41638 | -48.88848 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a66f8b18-d4f1-3e8a-8b38-b57db625946a | -2.41473 | -48.8991 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3abf3092-a52a-3cab-91d0-22e103bed0bc | -2.39138 | -49.1585 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54be0519-362e-38ba-91c1-7277ea2628d0 | -2.3847 | -48.93792 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2380943b-648b-3dbf-8307-01d9f100e0a6 | -2.3757 | -48.95828 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee2f7d16-3bcd-3fa9-b4dc-6bc3928b51c7 | -2.36844 | -48.93909 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 19874f2b-5d02-3a6c-a2fa-aca4e19d8be0 | -2.36572 | -49.02166 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7831492d-51c4-3cd6-b480-18d83563b438 | -2.35896 | -48.93402 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a34cb48-7348-3c5f-b1a2-147f07bc89a0 | -2.3584 | -48.93755 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58c9081c-58f5-30c9-930c-29aad9a951f6 | -2.35226 | -48.93298 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cb4dd90-7fab-318e-a1d5-c0e1856846d5 | -2.90389 | -50.50671 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75beb337-3240-31ff-a75a-a3d3c5190141 | -2.90059 | -50.50619 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35993ae1-1a63-3939-8bfb-0bf296da561e | -2.89918 | -50.40412 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac6c4129-fd2f-320d-bc70-61c4db7cef9e | -2.88755 | -49.57059 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5533b13-04df-3f64-b2da-1bbd8bdfb13c | -2.87606 | -50.40052 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c2cefa5-7d9e-33ec-9968-8853a1b1a343 | -2.86456 | -49.82523 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe9780ba-0ec9-3ad4-a393-17fb9c77f5f9 | -2.74726 | -49.77139 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7289f849-b129-3759-a4e7-1121cfade0da | -2.74395 | -49.77087 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21ef0539-52ff-3de2-a6bd-c0471dcf9498 | -2.69826 | -49.78143 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 309753a5-c8df-39d6-9865-0d629372fac1 | -2.69157 | -49.75922 | 2024-10-26 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 416d38c4-442a-37c1-a694-2476341611cb | -2.67531 | -49.73193 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d21c5e6-efed-32d8-a11d-af046e8c3981 | -2.672 | -49.73142 | 2024-10-26 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README67.md)
