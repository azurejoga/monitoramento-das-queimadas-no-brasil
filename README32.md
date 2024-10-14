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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4a5e40b-ef65-3f50-831d-392b7bae6c64 | -10.06186 | -44.25713 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ef4b46de-4bbc-39ae-948b-c996499d3559 | -10.06151 | -44.25898 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| ac31cf32-88f9-3f63-8e03-b98a9ad70252 | -10.06093 | -44.26196 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 20ff4ebd-a7d4-3bbd-8cc9-c72d60aa0f90 | -10.06055 | -44.26381 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 28487926-9411-3d37-87a5-635a058de35f | -10.05949 | -44.23649 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63a6f124-4728-3022-89d3-fecfd9027018 | -10.05346 | -44.235 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bcfb8f4-0ce7-3e7a-a97e-7b26630b877d | -10.0812 | -44.22197 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a77c68cb-2637-3db4-aa68-1d350894b54e | -10.08112 | -44.22386 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 783274ef-bcb3-3068-b1aa-a26882575ad1 | -10.08029 | -44.22674 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd7b957f-10ff-3eee-9333-a9ad89bd974a | -10.07938 | -44.23154 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d400040b-92ab-3d25-93c7-1041bbd7f1ba | -10.07923 | -44.23342 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5e1e86eb-9615-33da-bacf-507b0373ab3c | -10.07884 | -44.20348 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 650f8160-7290-3852-b6c7-0d3f8d371798 | -10.07791 | -44.20821 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14c3c215-d346-359c-94cc-b66e7a9dcdf2 | -10.07789 | -44.20627 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a88c241-aeee-36a3-a91d-69b099eafbf5 | -10.07698 | -44.21102 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10d58811-eba7-3ea3-94cd-43982f63a819 | -10.07696 | -44.21296 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 524b68d6-7429-3dc2-985d-2c95e71889ec | -10.07607 | -44.21581 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c28f6abb-a875-3f64-a229-2afc76f01d0f | -10.07602 | -44.21775 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb311d64-690a-3283-9cdf-33c23c02a652 | -10.07516 | -44.22059 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 797aae7c-625a-3638-b5a4-8bc941a67997 | -10.07507 | -44.22251 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9958c64e-2293-3519-9c53-cfd6ce4a9b3c | -10.07425 | -44.22536 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91d28d6a-dcb3-3ba0-84ff-e1551785c0b7 | -10.07413 | -44.22726 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a399953-2fc0-3e2a-a18c-b0f5e2dcd3f8 | -10.07333 | -44.23014 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc8f446f-ea54-3cd2-a17d-24a33c46ff50 | -10.07318 | -44.23204 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a4fe5fa-4772-3ab2-b5d2-7947f6d2ffea | -10.07276 | -44.20235 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d4292ef-3906-3da0-a9c9-f04129ed9d4d | -10.07183 | -44.20702 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff093961-9707-3adf-8428-595c3999c96b | -10.07181 | -44.20509 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25ce8bd0-e6f1-3a92-a948-4e14e01e5702 | -10.07092 | -44.20975 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bc54f36-d861-3a1f-9f69-57eb7622e3d2 | -10.07091 | -44.21167 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 424abff6-4830-3153-93eb-4525be5644ab | -10.07002 | -44.21444 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cfe2cb7-e0c9-36a5-908e-36812d9694a8 | -10.06998 | -44.21637 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e9cf674-3b71-3179-9c43-a7fa9756b17b | -10.06912 | -44.21918 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f412104-48e1-3583-9885-3cf2b9f36167 | -10.06904 | -44.22111 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d89c921c-2974-3a28-b7c0-8489ac68d832 | -10.06821 | -44.22393 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f2a4163-39e9-351a-b9a9-e4d6854fbc68 | -10.06809 | -44.22585 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10290b02-8010-3b00-9a73-5d31ab3a89bc | -10.0673 | -44.22869 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef3599e9-eafc-344d-8806-e1f1db27fe01 | -10.06715 | -44.23058 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7fec4a7-0c4b-3b05-ad91-690babfbc6fb | -10.0664 | -44.2334 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9511cd57-abb6-3f65-a97b-40f0f82ae1ef | -10.06575 | -44.20383 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8330c9aa-d824-3340-aa7d-61a469622d4f | -10.06487 | -44.20844 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 133468d4-5cf0-36c6-a0c0-6f53bbc645c8 | -10.06398 | -44.21308 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 754f49ef-f880-3ba2-acef-9adf7dae5986 | -10.06307 | -44.2178 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b4a45bb-5662-39e5-867d-0fc23dda7233 | -10.06217 | -44.22252 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b83d2e8a-6d92-3c02-b450-1de96148f469 | -10.06126 | -44.22723 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54095d71-559f-37ee-9eb3-30d490c87e91 | -10.05789 | -44.21196 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3075940-9a6d-3029-b97b-c67e3cfbef50 | -10.05699 | -44.21661 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff0a606d-ae7c-3747-8aef-f5548fab5045 | -10.0561 | -44.22124 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f64f315b-477d-3a53-90a8-620791ba6a9a | -10.05522 | -44.22585 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c535df0-c757-3964-ac73-1e77b092dd62 | -10.05002 | -44.22004 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f50fcca-488c-3b30-9f62-80a8aef51b5a | -10.04914 | -44.22461 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 947c31b0-ade4-3293-9b6d-12b4fb5da296 | -10.04661 | -44.20498 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a41b62a7-f3b2-3b38-9f03-b7d2ed6eeada | -10.0457 | -44.20971 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd962831-2f8e-3b0d-8370-9b4937a49b6c | -10.04393 | -44.21889 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1b8874a-3dee-329e-a0fc-b929c3ec5f24 | -10.04061 | -44.2034 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2413a7ec-e8fb-3b09-9df4-49cd75bd1d10 | -10.03967 | -44.20827 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a803a25-9915-314b-9fbf-a998dda18c22 | -10.03872 | -44.21321 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f687161b-af46-3f7a-970e-c939cdf089d0 | -10.03783 | -44.21781 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16b8a534-27f3-3f9b-8fdc-9f3c6e071245 | -9.44504 | -44.17132 | 2024-10-14 03:28:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9a5fc8f5-527f-3fa7-824b-e6b53bc45937 | -9.44498 | -44.17452 | 2024-10-14 03:28:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 580fc500-0b76-3716-87ca-a20afe80150b | -9.4441 | -44.17611 | 2024-10-14 03:28:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c1dab34c-4eeb-3d15-ad0e-452c54ff7e5e | -9.4389 | -44.1702 | 2024-10-14 03:28:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 995d961c-8317-32b8-a008-00a31c8be419 | -9.42315 | -44.15567 | 2024-10-14 03:28:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10b0f5a9-e268-35c9-8136-4858b0710ad8 | -9.42229 | -44.16023 | 2024-10-14 03:28:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7e2e643-42e9-3034-8588-647be3e58fc6 | -10.11592 | -43.94149 | 2024-10-14 03:28:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dafdc9a-a26b-3852-b9f4-b7d215157eb6 | -10.11508 | -43.94593 | 2024-10-14 03:28:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b6c75a9-ed13-3c17-8b0c-142e2d1508a6 | -10.11422 | -43.95042 | 2024-10-14 03:28:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c332104a-757a-3eed-bad6-8394ac42f326 | -10.11246 | -43.95965 | 2024-10-14 03:28:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31f0808b-fb17-33d9-a98f-f91b24f2eafc | -10.11157 | -43.96432 | 2024-10-14 03:28:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44741eb8-4196-37b3-80f2-39d1c1ac531e | -10.1091 | -43.94478 | 2024-10-14 03:28:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6600bd0-0e72-3201-a069-0df1704ddc6f | -10.10825 | -43.94923 | 2024-10-14 03:28:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c9e27f1-63a8-3494-b950-6da917ad7f20 | -10.07368 | -44.19769 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8f93ef7-357d-32aa-a970-756ad56689e2 | -10.0736 | -44.19576 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb964f10-bbf9-342e-ad9e-43ae2ede5993 | -10.07271 | -44.20042 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28a8949d-ac5e-3bd1-a209-75b1d061c5bb | -10.07022 | -44.18049 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4801a24c-0601-391c-b09c-303640dcfcfb | -10.06752 | -44.1946 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c002c9f-fac8-36f3-8931-75942f06c21a | -10.06663 | -44.19924 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 283cf4c5-988f-3852-9f55-a63ce6fbc5b0 | -10.06509 | -44.17443 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1f515472-8b73-33b5-805f-5475cb0c4e0e | -10.06419 | -44.17916 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0595bedc-dc0b-3302-8cc7-d96d561126eb | -10.06327 | -44.18391 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 956f46ec-8045-33f7-a034-4cfe3e22b9b7 | -10.0581 | -44.17806 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 63957f2f-f6f2-318e-85d7-1ff48a7cddc8 | -10.05721 | -44.18272 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d16fce6d-d450-363c-9eb1-09ca16127ab9 | -10.05113 | -44.1816 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1da8f3ba-524e-3c14-ac76-95dc626ee662 | -10.05025 | -44.18617 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58283a28-27b6-30b1-80cd-8da749790685 | -10.04934 | -44.19086 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8d6d7601-438c-3bab-bc74-76f93cde6f4f | -10.04843 | -44.1956 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 397a6eda-2499-3158-8c68-6958d4d58684 | -10.04752 | -44.20029 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cd06f1a-2972-3830-8f57-9cf36da43f0e | -3.43312 | -43.07795 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bacf628b-7076-3a14-bfbe-d2540732c681 | -3.43015 | -43.07365 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d92304d-988f-3594-a920-0040bf1a2dd3 | -3.42769 | -43.07161 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3756d99e-5f37-369d-96c6-a9816fb86b4c | -3.42681 | -43.07685 | 2024-10-14 03:28:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e32aefc-ad2a-33bd-8e3a-909297d4ad04 | -3.41419 | -43.35403 | 2024-10-14 03:28:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc59e00f-ceaa-34b0-a43a-84fe77057558 | -3.40778 | -43.35286 | 2024-10-14 03:28:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ef9c6c4-a8ea-3bf6-8c77-28d0a9485161 | -4.03371 | -43.05123 | 2024-10-14 03:28:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88abe76a-fb06-3c6c-a61f-be58cc4dc79e | -3.92319 | -43.14652 | 2024-10-14 03:28:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15dd598a-ecc6-3f56-9940-dbe04e4bff8a | -3.92233 | -43.15154 | 2024-10-14 03:28:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7aa58704-e347-31a6-b40e-046c951073b9 | -5.19288 | -44.76265 | 2024-10-14 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b287037-2489-3e01-8522-51a3642aec49 | -5.19174 | -44.76889 | 2024-10-14 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bfa38eb0-45a8-361d-adb0-447ae4f3c1d4 | -5.19062 | -44.7667 | 2024-10-14 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2bfaa113-170d-3dab-8f6d-e8b31c01e791 | -6.26581 | -43.90503 | 2024-10-14 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3de88257-0454-3881-9cb8-1a57e8253e0c | -6.26353 | -43.90645 | 2024-10-14 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README33.md)
