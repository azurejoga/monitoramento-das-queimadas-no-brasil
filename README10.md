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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9998314f-c731-3932-8fee-c354f465125f | -3.10291 | -51.50167 | 2024-11-25 01:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 832f3f00-b086-3822-837e-b0f27589b5cd | -4.01644 | -48.08115 | 2024-11-25 01:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 41054162-5d28-3a29-b605-8d56ac65ee26 | -0.92547 | -52.65254 | 2024-11-25 01:28:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d3e40ddc-0a28-3309-b19d-af54901fe9fc | -3.71309 | -51.79047 | 2024-11-25 01:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f3bdc021-a765-3d4c-afb8-2ab3e3aabd49 | -3.65296 | -51.39634 | 2024-11-25 01:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 15ab9ff4-0fed-3540-8a47-32ed8fb0aaa6 | -2.60957 | -54.2535 | 2024-11-25 01:28:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bdc01ce3-0f58-39b7-b1e7-4e6323d4e112 | -3.10299 | -53.98606 | 2024-11-25 01:28:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 99069939-d304-3f87-8e9e-d80e5cfe8b64 | -3.70487 | -52.40641 | 2024-11-25 01:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6407223c-c161-37c8-8405-882dd14ed922 | -3.50614 | -53.80987 | 2024-11-25 01:28:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5b678398-a324-31c2-9441-c24209eeb3a6 | -2.89294 | -51.58272 | 2024-11-25 01:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 44931f7f-58e1-33cb-83ad-d8e66a9009f2 | -3.70704 | -52.42149 | 2024-11-25 01:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 57782cb9-a447-3761-8da1-27970fd299da | -1.11225 | -53.39458 | 2024-11-25 01:28:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9d16d4fe-d72f-3756-9f6f-ffa28849d12b | -2.80253 | -53.00305 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c6de8664-1bb6-3035-8ff7-fd79eb74f8b9 | -3.24535 | -53.27988 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 06c86303-1177-3c67-abe2-beb13a38e7cc | -3.53639 | -50.45817 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 69d16e1e-38ee-3c3a-ad7e-80843acd887b | -2.33102 | -53.88042 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| a6c5d810-4ca3-3a5f-8ce2-6e0e756be625 | -1.18118 | -54.12769 | 2024-11-25 01:28:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a5bddd18-b1b3-35dc-bc53-fcc7215f6e67 | -3.2265 | -53.93043 | 2024-11-25 01:28:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e1fc646c-b5d4-3e1c-b6de-236e14c9589a | -3.51821 | -53.82023 | 2024-11-25 01:28:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9075a6b2-86fc-3225-b7a2-da361a74817c | -3.94967 | -50.84981 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4694c1b3-6593-3ac7-99a2-5be356101a75 | -1.52283 | -51.62452 | 2024-11-25 01:28:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3bb45008-0aa3-371b-bd98-c4fbc648ac6e | -3.952 | -50.85532 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| fde1d890-5233-328b-aaa1-e4878792dd20 | -2.57235 | -54.06195 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b018d747-4a5d-3a2f-bf14-63eb684b4829 | -3.94299 | -47.98066 | 2024-11-25 01:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 0cac1061-08ee-3c3f-9198-451d066e4f6a | -1.38739 | -52.33183 | 2024-11-25 01:28:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7bda8e48-5abd-3135-a943-aed1cd605219 | -2.66453 | -51.72944 | 2024-11-25 01:28:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f9697505-833f-358d-a1ce-676d39eec5f3 | -3.46368 | -50.83353 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| c735edc7-f4c5-3313-9611-6fd864c662e9 | -3.78507 | -52.10577 | 2024-11-25 01:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 668187d4-fa4d-38f1-af21-cc8c7d1bea2d | -2.90269 | -51.56229 | 2024-11-25 01:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a817e942-bf26-3eef-8ece-7d843842f099 | -2.64511 | -51.7694 | 2024-11-25 01:28:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6bfbb97c-dc23-3a0f-959b-6704e150976a | -4.24373 | -47.99189 | 2024-11-25 01:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 101ca6a0-b4ad-319d-ad41-b50c73b1e337 | -2.79346 | -53.01938 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ae306b03-a744-3306-acf7-e69b9b62d716 | -0.04872 | -50.8338 | 2024-11-25 01:28:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| dac0a428-0d76-32be-be8f-b99e9e098596 | -3.6412 | -51.15039 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6b670d92-0c73-3832-9dc5-63a05c928114 | -2.577 | -53.96796 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 88f92375-4e2a-3945-b898-39ad64095a8d | -3.80197 | -51.16961 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 43941051-7122-3ebd-bddb-1a40034900ba | -1.48134 | -52.51857 | 2024-11-25 01:28:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ad472f8f-9db9-3148-8717-877ef3ffc487 | -2.81473 | -54.12053 | 2024-11-25 01:28:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7c4979d0-5391-3c25-b809-e48f833264e7 | -4.02412 | -48.07372 | 2024-11-25 01:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| dbb26b1a-63db-3224-9997-6f0adccf43f5 | -1.23908 | -51.74269 | 2024-11-25 01:28:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b9f6ba9d-a367-3e7d-b7c0-9c56936f56f6 | -3.70889 | -51.79678 | 2024-11-25 01:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 16e827fa-8b2c-3056-8882-9750fe30bfbe | -2.24928 | -53.61418 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 45de34bf-7eb3-31c0-b47b-af024469482b | -2.7901 | -51.67976 | 2024-11-25 01:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3fe843e9-5121-3e03-aacc-1a37f54a91b1 | -3.28323 | -51.122 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| f12ed170-e779-3b18-8055-cae6b6d02d01 | -2.70315 | -51.99535 | 2024-11-25 01:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8785f747-45e2-3274-a515-692f7d9b274c | -1.12863 | -54.17927 | 2024-11-25 01:28:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 67372df4-2f26-3dcf-b6dc-ffc0f53811ee | -2.80459 | -53.01777 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 46f71c8e-d0d1-3114-883a-655569d9dadf | -2.33973 | -53.86624 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f99fefee-8768-3582-a7e6-a54a54987b64 | -0.88176 | -51.71991 | 2024-11-25 01:28:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c17899ec-2618-3670-b896-0c361ba08eb7 | -3.41887 | -53.28344 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 9a338d03-98a9-3ccb-b313-7503b08fb592 | -2.32922 | -53.86774 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 157.6 |
| b93f75e3-a8bd-3e3f-b2fd-a554dd4c1b72 | -0.04532 | -50.80991 | 2024-11-25 01:28:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| bfe0cdae-fd79-36a5-bed9-c4240b8bdc2e | -1.60572 | -52.57766 | 2024-11-25 01:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ef738ec4-7da8-315c-ab2a-b22de9b0dc10 | -3.85099 | -52.14595 | 2024-11-25 01:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 17779089-0a6f-341b-8a7b-e439799f8dab | -3.05314 | -53.22215 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 85f5e7c9-623c-3dfe-a168-5ef5e188a815 | -3.95236 | -47.98606 | 2024-11-25 01:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| f0968cdf-d64f-3677-b780-7cb1c6f6628d | -3.04657 | -54.03138 | 2024-11-25 01:28:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 23e14374-d688-396c-9692-9df1c5421091 | -3.1047 | -53.99812 | 2024-11-25 01:28:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d3413e3c-dad7-3d6a-97d1-646d8c4ed5f0 | -2.17484 | -53.77088 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b874e0c0-baf5-37ef-9e9a-2e3e6b3118af | -2.91195 | -51.71111 | 2024-11-25 01:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 49fb68c1-25b7-3a50-a01c-e87e153f5fe8 | -4.26114 | -48.71216 | 2024-11-25 01:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 1cd5a164-a85e-3554-bf8d-28ca2abe058d | -1.7741 | -52.72078 | 2024-11-25 01:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 87c68e50-08f6-3616-b431-882faf84a256 | -2.79356 | -53.01366 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| ec62eed9-0b7e-37e9-a382-34c6ae13e088 | -1.49319 | -52.51686 | 2024-11-25 01:28:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 2c6ce56d-bc14-36e5-9e94-332ab4edba63 | -0.27675 | -51.60553 | 2024-11-25 01:28:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 235117ef-26fd-3eb5-ac86-c0d2b61f3afe | -0.94928 | -51.64418 | 2024-11-25 01:28:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 77bfca66-efe2-3380-ab77-fbfd25a9821e | -3.4987 | -50.44709 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f36aaf9e-aed8-347f-90d1-44bb00d221d9 | -1.74303 | -52.7318 | 2024-11-25 01:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4d9368be-9fcd-3fd3-8951-9ddcaa2552ca | -3.94845 | -48.01471 | 2024-11-25 01:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 35dc008a-63ba-3d8b-ae91-45d81f7ac3e6 | -0.27961 | -51.62592 | 2024-11-25 01:28:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 684d6bd3-3e5b-3fa0-a384-78433312c4c6 | -1.09083 | -53.64258 | 2024-11-25 01:28:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c176bbe2-3ad6-37d5-9e07-4adbbaa5f7b4 | -3.81777 | -51.99998 | 2024-11-25 01:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8606264d-3ddc-3915-a215-2d29bcee9388 | -2.31547 | -53.61806 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8bdba560-0e17-32a2-b762-954b4a6ea6a5 | -2.90543 | -51.58094 | 2024-11-25 01:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c1a91927-af3f-3daf-9de3-275db5d7e34a | -1.13246 | -53.62206 | 2024-11-25 01:28:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6843636a-0d3d-30e3-8b9a-f774a6849c08 | -3.64054 | -51.14476 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ba5cf404-3b05-3b7b-a831-0aa587ca2b92 | -4.24578 | -48.71441 | 2024-11-25 01:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 3c23558d-d81d-3fdd-891b-93e3f5780ae1 | -2.31361 | -53.60485 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 06dad4eb-c9ab-3d4b-b200-50925f786dfe | -3.50789 | -53.82195 | 2024-11-25 01:28:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c17d7a70-c7d8-316d-801f-c87ad5da713d | -1.99382 | -53.29219 | 2024-11-25 01:28:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1454d0fc-d175-3f43-b988-741f3356eaac | -3.07513 | -50.95786 | 2024-11-25 01:28:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1bc4302f-1954-3bf9-aa9c-0aa5f9185156 | -3.71045 | -51.77313 | 2024-11-25 01:28:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 474c9658-54a8-31c5-877a-004ef4437393 | -0.91173 | -51.65537 | 2024-11-25 01:28:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| bfa7b8ca-6645-3082-9db2-0669073e889c | -4.02927 | -48.10702 | 2024-11-25 01:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 633d62b6-77f6-3434-98c8-e1bd1ef3b6a6 | -2.35576 | -53.7137 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ef267928-abb2-3970-be61-173cd891c026 | -3.80201 | -51.17481 | 2024-11-25 01:28:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3b852e80-e9ae-30b3-a5cb-75f8ae578ca9 | -2.25123 | -53.62754 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| e3a3bfe0-df85-3092-812c-01eb292f3f0a | -1.17077 | -54.12976 | 2024-11-25 01:28:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dfb0c97d-27fb-31a3-b7da-05fc07aa9e86 | -3.55393 | -51.53648 | 2024-11-25 01:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d250f189-d21b-3474-9035-a18e0cc726f7 | -3.71581 | -52.41383 | 2024-11-25 01:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| dcd2f5f8-fc1b-3e53-806b-e50aa11f9222 | -2.79139 | -52.99905 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2b296980-eb81-3aa0-a2e4-28b159ad9484 | -2.80469 | -53.01199 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 7c854ee8-843a-3873-a393-dbba994e24ae | -2.18476 | -53.80317 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0b4650c7-3901-3f91-a32a-d764b364ce11 | -2.24577 | -53.62116 | 2024-11-25 01:28:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 3701e107-06f5-3da5-b2d2-fd6ac3e21ffe | -0.35474 | -51.97807 | 2024-11-25 01:28:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f350bc1c-ca15-3df2-abd0-b864bac526ca | -2.63276 | -51.77119 | 2024-11-25 01:28:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4e75a7f5-78f2-3112-a71c-2b5e5dbff13b | -3.649 | -51.38357 | 2024-11-25 01:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 79034cc8-3a5a-3582-9fe3-5f4b6f2da66c | -3.55122 | -51.51808 | 2024-11-25 01:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0ff09278-9a72-33ba-893c-0c82c30bc7cc | -2.79141 | -53.0049 | 2024-11-25 01:28:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 9f857445-ba53-3410-ab45-b348e0e44628 | -0.95031 | -51.64983 | 2024-11-25 01:28:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |


[Clique aqui para ver as próximas entradas](README11.md)
