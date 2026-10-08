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

## Dados Diários - Página 203

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef4dd36d-200e-3fce-ada8-5fa2d2c4d8c6 | -8.62052 | -67.05982 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a81d663-167f-3a65-a9ac-929f2efc84c4 | -8.63012 | -67.02945 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 1ae38d44-14c9-3af5-9c86-e08f1cdb6b22 | -8.61535 | -67.05518 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d5b4429-4efb-3568-ab2c-ec41cdb35944 | -8.62495 | -67.0248 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ca10a620-ac5b-391c-b929-8ed686380b30 | -7.31624 | -72.70894 | 2026-10-08 06:27:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9e89f74f-a9d6-38ec-bac5-a0ced216e3d3 | -9.0499 | -65.91849 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f69cf92-4ef2-304a-9244-633011478953 | -8.61928 | -67.02399 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 377663e1-bd62-3d21-9c47-326c6fba07cb | -8.59888 | -67.04889 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8af0bed9-1ef6-3dab-afff-464f6934c515 | -8.61978 | -67.02007 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3784fe2-8fa3-3695-9b71-bc4d99e688bf | -9.20374 | -66.0899 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f6ed264-fd7d-3c20-a4ee-bc646c25aeb2 | -9.05515 | -65.92934 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0a5e04db-23ba-36e1-896b-18b8e7962a7d | -9.20315 | -66.09465 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dc796d9-1039-3928-8159-36ae677e37cc | -9.12577 | -66.01073 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ea6cb5c-5c4d-36d0-af67-0938d145cef8 | -8.61487 | -67.05904 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcb14645-9517-3793-afda-1f5ef401ded6 | -9.07275 | -65.48481 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a33f2ad7-29e5-380b-8b60-08532d7af6c2 | -9.04869 | -65.92797 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 206039ce-f68b-3921-80f3-9937506b81f0 | -8.61879 | -67.0279 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6ef9c164-e634-3caa-992f-ba8c681c9a7d | -8.84844 | -66.80242 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67979b29-3f9c-3d25-933b-8fe8218f0c9d | -8.62363 | -67.05503 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f29cd66-4330-3984-b765-dac56f7bfc4d | -8.61411 | -67.01926 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a677e880-0253-3880-937e-b7f227af4d45 | -8.62779 | -67.02402 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| f35f4fc9-1d83-38ea-9798-40a28ed29692 | -9.05479 | -65.92893 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aea17b1f-4fb2-3e5e-9eee-b10dfbf7a04f | -8.62544 | -67.02093 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 75b127b5-e24b-3afa-abfd-5f7318539a6a | -8.62101 | -67.05594 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 424017b3-f5db-3ca2-a313-923a81dc4de0 | -9.06091 | -65.9297 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| de617efb-899f-392c-a96a-2d689cdaf225 | -9.65467 | -63.75741 | 2026-10-08 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b08dc87d-2963-3418-9a36-1436375637b0 | -7.44542 | -63.55404 | 2026-10-08 06:27:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b4e72d0-7e1a-3235-a72e-79ece7e03124 | -9.05957 | -65.48808 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c6df812-8174-3e71-b9da-e259ee429c37 | -9.11969 | -66.00983 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e55f5c9b-c4bd-3a64-b4fb-ee4041910228 | -8.61746 | -67.05814 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ac0487c-9877-3c9d-b348-813c210df918 | -8.63061 | -67.0256 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 19d89f3b-58a4-380e-8ce7-00fdcdbf94b1 | -8.61595 | -67.02631 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0e96a46b-2b81-337b-8675-48ee708c7df5 | -8.76153 | -66.92398 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2d9c698-0461-3c6a-b6f2-b8bc2d288a11 | -8.84793 | -66.80651 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69c4a6bb-7eff-36ca-8969-d0af9d8416e0 | -8.62161 | -67.0271 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| e7647737-c350-3992-80f6-f8d5fe4de150 | -8.62446 | -67.02869 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| d079ed3e-ef55-3d17-905f-bc1769a4318d | -8.6183 | -67.03181 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9acf0146-b445-3eb5-b109-1fcfeda5d800 | -8.59937 | -67.04498 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81eb7a87-5ef8-3796-b611-5ce5eaa1aa6a | -8.61699 | -67.01849 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7c427a4a-904e-3639-bb1c-88c04d1eb0e6 | -7.44625 | -63.54753 | 2026-10-08 06:27:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9886cfbf-b268-36a6-8a39-a8bc05b7b092 | -9.11453 | -65.35526 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49308628-9e42-3cfb-8cbe-652d45a09c04 | -9.07903 | -65.48566 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a58504a-1316-3693-9da2-a8c8952174e7 | -9.06031 | -65.93436 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cfe68292-b0c6-3267-a231-d03b94b50e49 | -9.35204 | -65.74853 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 292f8397-7d0f-3dbe-842c-fe0652fbfc16 | -8.62265 | -67.01931 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9eca6494-cb00-3bfa-b36e-a3ac24c59eb3 | -8.61362 | -67.02318 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d54103c3-8712-3d1f-a70a-9925a1a263f2 | -8.61647 | -67.0224 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ef31fac9-7951-3dc6-94b8-d86cd43121cf | -8.61543 | -67.03021 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c55caf0d-e081-324a-ad8d-b968e835c716 | -7.43934 | -63.54653 | 2026-10-08 06:27:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ec971c8-72dd-3388-ae0b-06e291bc14d7 | -8.61313 | -67.02709 | 2026-10-08 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1a736fa3-22a8-3c28-86ff-e1ffb44eae5b | -8.6292 | -67.0111 | 2026-10-08 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f9244498-ed32-3bd9-8f57-b3e332827a77 | -8.6107 | -67.0116 | 2026-10-08 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a563581f-994b-3590-b86c-45a9f64a7019 | -8.6291 | -67.0296 | 2026-10-08 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 5ce4a30c-5db7-3ba2-9c6f-9df5ebc863e6 | -8.6107 | -67.0301 | 2026-10-08 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 362e322d-6a02-38a2-bcd8-fd45b5076087 | -8.6107 | -67.0301 | 2026-10-08 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| b99ee4c0-16bd-3ae2-a517-1593c2f4ca23 | -8.6291 | -67.0296 | 2026-10-08 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| fe84fb5a-fd35-38b1-ac03-20941814b894 | -8.6291 | -67.0296 | 2026-10-08 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 6cb004cd-df5c-38db-b611-462b8c7c1b9d | -8.6292 | -67.0111 | 2026-10-08 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0a229b5c-e9ba-314e-aeab-9b0c27445df8 | -8.6107 | -67.0301 | 2026-10-08 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0e400c82-8349-3f2e-a55d-b22a62c0939c | -8.6107 | -67.0116 | 2026-10-08 06:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 28b1d7f7-fa0c-3c1e-af3e-a7e5a1bcdc4b | -8.6291 | -67.0296 | 2026-10-08 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| ba998503-dda3-35e1-b8ab-72c034051f33 | -8.6107 | -67.0116 | 2026-10-08 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| dc8352ee-962e-304b-98fa-202999d0c924 | -8.6292 | -67.0111 | 2026-10-08 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6e69bddc-0f70-384d-b72a-1299b7559ff3 | -8.6107 | -67.0301 | 2026-10-08 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7d3296fe-871f-36e8-acfc-3431dbebfb33 | -7.31709 | -72.71029 | 2026-10-08 07:03:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67d2657b-53a0-3299-9bc3-2f373ff4adb3 | -7.31136 | -72.70943 | 2026-10-08 07:03:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5d01246-ec58-3c17-a59e-ceb2679a6f1a | -8.6107 | -67.0116 | 2026-10-08 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 6c48d724-d5bf-3a37-935c-ff58416935b0 | -8.6292 | -67.0111 | 2026-10-08 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 93b808fa-b5c4-3bac-93de-d650e6c966a0 | -8.6107 | -67.0301 | 2026-10-08 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b1fe6083-46c7-339d-953e-a71be9dd0802 | -8.6291 | -67.0296 | 2026-10-08 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| dc6a16d3-bc40-384b-8089-f6dbfef0f53b | -8.6107 | -67.0116 | 2026-10-08 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f18c27af-b3bf-316d-abcb-a9e504e24663 | -8.6292 | -67.0111 | 2026-10-08 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 91e6ae87-b8bc-3093-bda3-c51eec2e594a | -8.6291 | -67.0296 | 2026-10-08 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| c045550c-5870-3868-a93f-5d962fa6a8be | -8.6107 | -67.0301 | 2026-10-08 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e050c72a-fa4d-37e7-9222-7a15225023cc | -8.6107 | -67.0116 | 2026-10-08 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 10e46e2d-aecb-388e-b0de-e2eaba566f91 | -8.6107 | -67.0301 | 2026-10-08 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| be16544c-a092-317d-89c2-f060c1f1c9e3 | -8.6291 | -67.0296 | 2026-10-08 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 166fcbe6-8a6f-33ad-aa1e-cbd5ff3839f1 | -8.6292 | -67.0111 | 2026-10-08 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| dca39d81-3365-3af6-8ac3-ab3bf9749e24 | -8.6291 | -67.0296 | 2026-10-08 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a756faf9-7bbd-3f6d-b813-f8331aa85de3 | -8.6107 | -67.0301 | 2026-10-08 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2c424d67-c806-397c-a523-0473838979a4 | -8.6292 | -67.0111 | 2026-10-08 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| ef0e4c42-72bc-3fad-9c19-f1bf47b8a502 | -8.6107 | -67.0116 | 2026-10-08 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| ca3d6538-c37c-3bbb-9e86-d0e4afbf6514 | -8.6291 | -67.0296 | 2026-10-08 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| fddf2eeb-7f96-350c-8375-27e11c82b611 | -8.6292 | -67.0111 | 2026-10-08 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 418cb49f-6d0b-3b8a-8ace-8933a593a03f | -8.6107 | -67.0301 | 2026-10-08 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 70b88c9c-dfa7-368b-b344-1beb1a56d09d | 4.27332 | -60.03314 | 2026-10-08 07:54:00 | AQUA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 088a32c8-1814-39b4-9909-2e3cc879993e | 3.1193 | -60.64815 | 2026-10-08 07:54:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54a38a89-1e17-3523-8b0e-9a3dd2d30f66 | -3.09677 | -59.18543 | 2026-10-08 07:56:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 03722d14-9ce4-300b-aba3-54ff8e1b7dc1 | -2.98691 | -54.07716 | 2026-10-08 07:56:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 5a1d4637-b5e5-34ce-9670-eabe79aebb4b | -2.78355 | -54.06567 | 2026-10-08 07:56:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 05f35f85-2fb8-34ba-9590-989cebb19866 | -3.56036 | -59.46949 | 2026-10-08 07:56:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 732e52e6-5592-3931-87ed-e2bd6387b90b | -3.0485 | -53.96498 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 8824108c-1573-3eba-86ac-10e65fdf948a | -3.10912 | -54.16756 | 2026-10-08 07:56:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 7c317662-0a8b-3527-badd-fa28df7521bc | -4.11348 | -59.87991 | 2026-10-08 07:56:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b258b9a3-d7ed-3049-9ce4-084c0b3a4708 | -3.10059 | -54.28053 | 2026-10-08 07:56:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| e44f1dbb-9ae1-3b90-875e-d0d4ab68338b | -3.30158 | -54.02522 | 2026-10-08 07:56:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 52c243b1-86f4-382a-9866-f6494683dbab | -3.16702 | -58.62263 | 2026-10-08 07:56:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e3e14893-2a14-3c14-8bb9-8b3984a28959 | -6.48783 | -62.85192 | 2026-10-08 07:56:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4b358dbb-8311-3b29-9322-3bf43b384718 | -2.9989 | -54.07092 | 2026-10-08 07:56:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| bc0845bf-76da-31f3-9b06-f1956dc4928b | -3.09473 | -59.19967 | 2026-10-08 07:56:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |


[Clique aqui para ver as próximas entradas](README204.md)
