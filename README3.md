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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8494905e-76a7-33aa-b363-e7cbfa5364e2 | 4.0733 | -61.187199 | 2024-12-08 01:32:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 29f39be7-4e73-3e81-bfd7-ee26cab3644e | -13.8952 | -54.616402 | 2024-12-08 01:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a4d1001-5768-3dd9-84cb-a16b1613a368 | -1.5216 | -60.3321 | 2024-12-08 01:32:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b656ea15-71ea-3519-9182-1a8f43fcb176 | -12.8551 | -51.917301 | 2024-12-08 01:32:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6bae1d-c0fb-3bfc-98d2-04b5f8959ddf | -12.5372 | -57.726299 | 2024-12-08 01:32:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46f980ae-97d0-3da6-afd4-9ee44729dc86 | -1.5199 | -60.324501 | 2024-12-08 01:32:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba2fbf33-fd71-32b4-828f-b7b0bd6da0b7 | -15.9818 | -57.162899 | 2024-12-08 01:32:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84da5da8-422e-36c1-ae16-45abaf10f2c7 | -15.1657 | -56.4701 | 2024-12-08 01:32:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98b9fbc2-9683-31b5-8ce6-5e526c7d70a2 | -1.0719 | -62.636398 | 2024-12-08 01:32:00 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07ea430c-3e1c-37b6-ab74-8c928ca94629 | 1.9912 | -61.149101 | 2024-12-08 01:32:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5e9a49-1c21-30b3-ba72-f9d4c602da9e | -1.0734 | -62.6432 | 2024-12-08 01:32:00 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd9c0e58-c8b6-35be-9c75-7e1c9eeed636 | -12.7917 | -54.219299 | 2024-12-08 01:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6b82db2-624c-314a-9d39-3837cd9ab716 | -11.7553 | -54.710499 | 2024-12-08 01:32:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16c0fc2b-20ca-3b37-b317-e3f3dd515777 | -11.7484 | -54.724499 | 2024-12-08 01:32:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11a463b9-516a-3290-b836-1c04bf9a7c26 | -12.7887 | -54.207298 | 2024-12-08 01:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3fce6b8-fe03-3f01-b129-9329d3ecb611 | -12.8595 | -51.9342 | 2024-12-08 01:32:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0b77049-4779-37c8-87ec-0e54852736a4 | 1.9929 | -61.141499 | 2024-12-08 01:32:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dcca8070-5a31-32e0-8381-b2d48774e26a | -15.2691 | -53.567902 | 2024-12-08 01:32:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1df238ba-6040-3680-b26d-d21f62c91d08 | -12.782 | -54.221802 | 2024-12-08 01:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45d5e2cb-af5c-36b3-8b68-4a6d87ba4dbd | 4.0751 | -61.179199 | 2024-12-08 01:32:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 14db4d39-735e-3190-a43e-43d774e77e02 | -13.8979 | -54.6273 | 2024-12-08 01:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56b8e7d9-eead-304f-9297-71d3b78801fc | 1.9955 | -61.1394 | 2024-12-08 01:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| e23499a9-fc42-3086-9881-eda20dac7292 | -11.752 | -54.7255 | 2024-12-08 01:40:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a50047d6-8fde-3b24-b245-d8e747d7722b | -11.771 | -54.7237 | 2024-12-08 01:50:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ae87294a-82de-3849-868e-0ec4474e6dc5 | -11.752 | -54.7255 | 2024-12-08 01:50:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 99971846-664e-3109-9de3-b00ab30b1122 | -13.89977 | -54.65107 | 2024-12-08 01:51:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ced1aef8-4a3e-39b9-8a44-94d63de797aa | -13.89099 | -54.63355 | 2024-12-08 01:51:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 3fddc428-fbbf-359c-af6f-7d0c691a052d | -15.16003 | -56.47007 | 2024-12-08 01:51:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7549ba32-e7a5-3296-ac48-aa08c1e11c38 | -12.85589 | -51.95148 | 2024-12-08 01:51:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| cfa53088-9a0a-3aec-87bd-0dc2d23f5a72 | -15.35956 | -53.12834 | 2024-12-08 01:51:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| fa4d8654-9a44-3f70-b82c-63bfe8b5bf2b | -15.37145 | -53.12059 | 2024-12-08 01:51:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 4ede2d71-3460-3944-9e8d-2c890e3f020b | -15.25707 | -53.58083 | 2024-12-08 01:51:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| c684cb06-c3ef-37b6-bede-3b5b73bfb99e | -15.1629 | -56.48732 | 2024-12-08 01:51:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a9238ab6-8c79-36ab-a327-e2c20f99a8dc | -13.89538 | -54.62623 | 2024-12-08 01:51:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| fdd461a1-116f-3489-82f5-d287ec2e38e9 | -15.97824 | -57.17336 | 2024-12-08 01:51:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a00fc53d-11bd-31b8-b216-5e6a431c82ba | -12.78137 | -54.22426 | 2024-12-08 01:53:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 081301d9-d3f2-326c-90e1-b3da121ac797 | -11.75252 | -54.74416 | 2024-12-08 01:53:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| c2ec9bd4-91cc-3370-8289-c7cdf922e1d1 | -11.74806 | -54.71794 | 2024-12-08 01:53:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 1a87a6c3-5fd3-36c1-a900-777268c65203 | -12.85118 | -58.22195 | 2024-12-08 01:53:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 0ffc601c-0ad1-3ce0-9c91-a40c1e6f291e | -12.53098 | -57.73109 | 2024-12-08 01:53:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9ad6b056-6c9c-37ad-8fd4-fa0f92680e5b | -12.78168 | -54.22976 | 2024-12-08 01:53:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b6e41d28-4f11-38b2-b806-e3e831235a64 | -12.85333 | -58.23551 | 2024-12-08 01:53:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8007bc6a-682d-3cde-90d2-c4ef528b6413 | 2.57687 | -60.69933 | 2024-12-08 01:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bed6f663-fa37-3b29-bfb3-68880ac261d1 | 1.99889 | -61.14731 | 2024-12-08 01:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 72821b9e-6864-37e6-8ec3-3804bfdc19e5 | 1.98781 | -61.14573 | 2024-12-08 01:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d84e3b55-4f50-3f7a-8087-f6277a1f579b | -11.771 | -54.7237 | 2024-12-08 02:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| bed5eb3d-7fd4-3811-b5a5-ae5bb2bc0e68 | -11.752 | -54.7255 | 2024-12-08 02:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 8af77a23-8665-3b1c-8c20-908aa3a2540c | -11.752 | -54.7255 | 2024-12-08 02:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 0e9e31ac-adb8-32d0-842e-7639ba567ff4 | -11.752 | -54.7255 | 2024-12-08 02:20:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 728d9e85-d589-30f4-b873-cfc42429a2c3 | -5.9186 | -48.0232 | 2024-12-08 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| d6d37c71-fa2b-3865-b8c8-b470581d0eea | -15.0867 | -59.6288 | 2024-12-08 02:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4168244d-d24c-3121-94b4-047f61999e64 | -11.752 | -54.7255 | 2024-12-08 02:30:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| d8379f03-09dd-36bd-87cf-65ef4decf149 | -5.9186 | -48.0232 | 2024-12-08 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 26516f65-6b51-32c1-952a-8af0baaa53ce | -11.752 | -54.7255 | 2024-12-08 02:40:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 3ead1af2-2fb4-354f-84d7-b067a72a2862 | -4.58 | -48.0132 | 2024-12-08 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 6ecacd16-397e-3e2e-9c7b-fc54b38e154a | -11.752 | -54.7255 | 2024-12-08 02:50:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 4bf63c98-3b58-36ab-a038-72626acbd704 | -5.25058 | -37.51389 | 2024-12-08 02:55:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6f69fe87-a027-3cdf-8e76-2df1a4db9568 | -9.98729 | -36.51563 | 2024-12-08 02:55:00 | NOAA-20 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f3f1e427-f249-39f3-ba7e-aeba5b5e32df | -5.25186 | -37.507 | 2024-12-08 02:55:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0b055c27-266c-314b-973b-0495cfb3a15c | -5.25496 | -37.50983 | 2024-12-08 02:55:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d0168e14-a185-375e-8d16-48068e937d81 | -5.24788 | -37.50839 | 2024-12-08 02:55:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5ce87a1d-b377-3131-9cee-9694fcdceabb | -11.752 | -54.7255 | 2024-12-08 03:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| ce582c36-6e05-35ad-865c-ab6212920f6d | -11.752 | -54.7255 | 2024-12-08 03:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| eabf80ae-b34b-3b8b-a9bf-58d1f1fdf224 | -11.752 | -54.7255 | 2024-12-08 03:20:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| d55c89c1-c03b-3796-ba95-92b94e5ecbdb | -11.752 | -54.7255 | 2024-12-08 03:30:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| e078421c-a6cb-35de-9fcd-58aaea7c2a05 | -11.752 | -54.7255 | 2024-12-08 03:40:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 86fab6d9-a62f-342f-b5ff-03722efa80e6 | -1.64936 | -45.90992 | 2024-12-08 03:46:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6407b006-a9c5-328c-a5da-d9e87f21631a | -1.65063 | -45.9023 | 2024-12-08 03:46:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43380f00-6392-35c1-bfeb-61eb04ca76d6 | -1.65 | -45.90609 | 2024-12-08 03:46:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5b9784b-63c3-35fa-807d-5c26e157bfa3 | -1.65195 | -45.91082 | 2024-12-08 03:46:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d10dcc3-5907-3fcd-b48e-4e9add3f4924 | -1.64631 | -45.90989 | 2024-12-08 03:46:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77fc232f-95bb-3072-8d17-101f338e387f | -1.64691 | -45.90606 | 2024-12-08 03:46:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ca8db54-8bfd-386d-8261-f7a25f4e7998 | -1.64752 | -45.90225 | 2024-12-08 03:46:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99c34885-4a59-371d-97ad-16b70c35a57d | -10.00208 | -36.33786 | 2024-12-08 03:49:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2831038f-334e-36d6-9a82-145f18fcd7ad | -7.80192 | -46.2314 | 2024-12-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc36fb08-4255-38e9-a825-8a88a03940b5 | -10.0017 | -42.17516 | 2024-12-08 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 88103404-8119-3a3a-9cea-59bed4518aa1 | -5.493 | -46.77042 | 2024-12-08 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c730627-8925-326e-a7b4-6a74f5278144 | -6.55417 | -44.20341 | 2024-12-08 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 950c3c41-d24b-3145-8f9e-96f400454968 | -3.8582 | -40.44503 | 2024-12-08 03:49:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 748e071a-9632-3818-a41d-b491371ee185 | -7.99287 | -45.79284 | 2024-12-08 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6142ab4-3757-3b57-8dce-999c263ac625 | -5.91081 | -48.02959 | 2024-12-08 03:49:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 04039512-d054-3016-a09a-3f6e13cac63f | -7.88364 | -44.20486 | 2024-12-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2937f831-4526-3a96-a042-a643362497d9 | -5.00831 | -40.70515 | 2024-12-08 03:49:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f6b0c32-5960-30ed-9c38-5b14f9f190ec | -7.88305 | -44.20214 | 2024-12-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a161892-ee79-3cf3-897f-68378b72f7b8 | -8.15954 | -42.94325 | 2024-12-08 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e1bc675-e515-35cd-8059-23b4986d7cc8 | -5.58055 | -45.20968 | 2024-12-08 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 043bd48b-23b2-3d0b-8266-f5eb32867a45 | -6.29271 | -43.85285 | 2024-12-08 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa843615-e22e-3684-a927-a62d224aa759 | -5.25502 | -37.50394 | 2024-12-08 03:49:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 60cc0efd-e829-311d-931f-0d7d83bfdc21 | -7.21409 | -35.61013 | 2024-12-08 03:49:00 | NOAA-21 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 007eea98-be94-3374-a6a1-e4ad8709a3da | -7.79609 | -46.20379 | 2024-12-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea908810-5402-3d5a-ac7e-64535993ce63 | -6.90786 | -39.87249 | 2024-12-08 03:49:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5b8d6a00-e083-30fd-bbb0-0be745aef047 | -5.47557 | -39.41707 | 2024-12-08 03:49:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1979bef5-27b4-3893-879f-5c808f2b24dc | -5.59313 | -41.38272 | 2024-12-08 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aff28581-e51d-3422-9dab-0fde8ff97ea0 | -6.68936 | -47.66433 | 2024-12-08 03:49:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1afc17f-78eb-3e94-b699-7e7346f74b1a | -5.25448 | -37.50742 | 2024-12-08 03:49:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 07edba18-7feb-3517-ad3a-6a0ded9d5333 | -5.90884 | -48.03168 | 2024-12-08 03:49:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9a30d846-171e-3ff9-9fb8-420734b747df | -5.47908 | -39.41763 | 2024-12-08 03:49:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7f1813f2-af86-352b-99fe-d8aeaed62d54 | -5.50716 | -42.87707 | 2024-12-08 03:49:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5ed53b3e-4277-3359-b9d6-135951664141 | -7.98727 | -45.79508 | 2024-12-08 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 492d75fb-0385-3b22-9a7d-80e000dea085 | -6.94107 | -43.53976 | 2024-12-08 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README4.md)
