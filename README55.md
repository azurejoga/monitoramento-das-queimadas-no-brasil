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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab368790-e37a-35c7-b67f-212fba503f68 | -2.13218 | -54.80862 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d78086ba-78bd-3fe3-b1e4-9079e5e33bca | -7.19141 | -46.5248 | 2026-10-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfa9f1f5-66c9-3d05-a025-77e0d0a02b17 | -7.60471 | -42.37962 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 87acf375-26a5-31c7-b4be-94471a4c6cdb | -8.58604 | -45.66845 | 2026-10-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8994d60-32ec-3643-a2d9-f99b78fef61d | -3.8144 | -51.03986 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b7b6436-fcca-3590-8f46-44290093a073 | -3.85404 | -55.99771 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a79a77ba-8be0-3905-ab1e-98e6512c4717 | -2.99549 | -51.12102 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a729a0e-afde-30f1-8c29-3e7823c10420 | -2.87274 | -54.15322 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16394c09-326b-3117-9504-5e58f03d0640 | -6.21151 | -52.83571 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0602af38-f500-349e-90f8-633f247beda4 | -3.00042 | -54.12788 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 96b9daf6-f978-3ec7-aeff-7810b386fa65 | -6.87556 | -43.68666 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e6d5505-e892-3bd9-bdae-571da314ccdb | -3.5916 | -54.56912 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3930e44-5dda-373b-8d80-c69fbef850ce | -3.42173 | -44.32994 | 2026-10-07 04:19:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8691085-bcef-3660-8518-4401338bf5fb | -4.8421 | -45.98671 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b8852a4-c332-3174-a928-76c544aac094 | -5.5469 | -44.83216 | 2026-10-07 04:19:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30da237d-68f4-30bb-aef7-6c82b7f21d48 | -4.79863 | -42.75115 | 2026-10-07 04:19:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd0b66c5-8cf8-3de1-8bbe-c57754dabdf2 | -7.99375 | -45.49329 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75836014-4d55-3543-bfd4-828f7300b69e | -5.91777 | -47.15005 | 2026-10-07 04:19:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4031067-6d0f-336d-8f12-210d260fe328 | -3.04339 | -53.91481 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4b07717-fbb4-34a3-8d17-9dca9d16ce06 | -5.47865 | -44.25928 | 2026-10-07 04:19:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35549dbb-eb23-3371-b1a4-0667e4e7eb12 | -4.92676 | -55.86759 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fcc748f9-3bb5-3c4b-acfd-e976b4e20bac | -7.97451 | -44.50735 | 2026-10-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b2246b3-805e-3504-8161-863f7c2318c5 | -8.04229 | -47.81185 | 2026-10-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 368442bf-1d38-3874-b204-f0ddf95a3be0 | -5.98175 | -40.92614 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 669644cb-ae14-3817-b92f-34213c3dbd0e | -3.28296 | -54.0632 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4cf93414-9f75-3fb2-93d2-064f9846f705 | -3.10966 | -53.78521 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fabfd0db-0c51-3936-b986-defa2070744e | -3.20633 | -42.95805 | 2026-10-07 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1176d572-c38e-3170-8514-8e0c682f3d56 | -3.35802 | -50.76255 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da9979b4-7373-3f30-8efa-633880f98219 | -3.06408 | -54.24783 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 579dcc09-25c0-3ba3-b1af-e85efaf22261 | -3.49266 | -50.10648 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1035e9eb-bddc-3493-8812-29a47d7a008f | -3.21839 | -53.88434 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a74d1f23-68ae-31fa-b151-f40b13d76ecc | -3.08418 | -54.30066 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4a0da4c-3b5b-37ed-a596-c05c6f42b13b | -7.18162 | -44.30367 | 2026-10-07 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fba12770-3d84-31dd-a7c5-b18d3e0db2e3 | -5.969 | -40.93977 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| be42c6a6-7e2e-398c-aac3-ee2f5a619a88 | -2.78481 | -51.67316 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 251410da-d933-38f3-8ba2-d22678fc9aaf | -3.28999 | -54.05942 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6a922b40-3e44-3e23-a9b5-74a9a51c081b | -8.66108 | -44.86449 | 2026-10-07 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b47c61b0-de2a-3376-8e6a-ea6d026f3146 | -3.02819 | -53.89249 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6edf7f5f-202b-32f7-b8f3-eb187c07447a | -6.72735 | -45.79777 | 2026-10-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 990d185b-6724-3cfa-a6f2-a14fb3cb79bb | -3.58614 | -54.31921 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0ab6b46-3fd5-3872-88df-8ca94bb10471 | -5.72601 | -45.15683 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a5c7a57d-a003-3727-8ad2-9bd0f2654569 | -5.94638 | -41.31054 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0a87bb30-00c9-39bd-8bfb-c17ec4413f7c | -5.74497 | -43.276 | 2026-10-07 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 798d2bfb-6ef2-3733-9203-cb46f8410f00 | -4.75414 | -45.76824 | 2026-10-07 04:19:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b9efbd9-0c19-3705-98aa-6ff7042b7098 | -3.50681 | -54.63986 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd4ab53b-ca46-336b-bdaa-761f6edf3c0b | -4.758 | -55.65335 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d8883e2-ad8f-33ce-843d-2fd5800a54de | -7.60192 | -42.37554 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a5142b0-b893-31af-9730-8974d5d0bcb4 | -3.42689 | -50.4423 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b26b08d9-1669-3634-a44c-2fc798d0dc71 | -7.86448 | -44.15523 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed3094c5-02a5-3476-a27d-cfafffbe905d | -6.88163 | -43.69118 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e47d1808-a79d-36d0-8ff9-468bbb00d215 | -3.06648 | -54.17847 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd4d38cc-677a-3dcc-a934-269a12f65587 | -3.07593 | -54.25447 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb8ef335-7181-3a7b-b294-9d1a852d014d | -2.6009 | -48.26311 | 2026-10-07 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7856abd1-47ed-3677-93af-7b8bc2161e77 | -7.60638 | -42.36897 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bae494fa-1327-3576-a8ce-e607e44fbc11 | -8.20994 | -46.35251 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a743acef-9900-3895-9df8-e9a186a29f8c | -3.537 | -54.6496 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a4160bf1-e4e7-3e94-8a8a-a09a3478ccd9 | -3.27345 | -50.41479 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b861136-823c-3604-8a13-d8347ee6a687 | -1.19716 | -54.21548 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ecf565d-3fd2-3aae-9eeb-b79f009385cd | -4.07693 | -54.88863 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57c840d4-4b3e-3510-aded-81d7d5a04030 | -5.97369 | -41.36006 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| deceb0fa-95f9-3253-b793-457fdc04e629 | -7.76683 | -43.8078 | 2026-10-07 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 34a5934f-284c-3e30-a658-837a76428d77 | -1.28541 | -54.57324 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e4a9c91d-de0b-3dd1-93cc-29965c3fd2ef | -8.19798 | -45.53024 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| af124351-a98b-3de2-93ce-b8eb461d0dfb | -3.56425 | -38.88412 | 2026-10-07 04:19:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7ee7411d-5573-3fbf-a30c-fee083385ac6 | -3.07962 | -54.2894 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 81aa0cb5-bff2-3773-a3b4-9f02e7e6c5f9 | -3.07507 | -54.18184 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e12e238-fa19-3c61-a86b-a8eafe5287d3 | -3.08945 | -53.71913 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a20f6224-9cdf-31f0-8f96-d8dde8a8082c | -4.8397 | -45.79775 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfc04ef2-0025-34e0-846f-afb9ec10394a | -3.61479 | -55.28836 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 3bc3447b-9bd5-32df-a6f3-eae6022225d3 | -3.07399 | -54.24688 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7e0860d-b120-3b7b-ae1a-da2c9c4ddd68 | -3.60939 | -50.20282 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 587bd633-70ef-3d73-9cde-19eb0d606983 | -3.74307 | -51.22441 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7cb9a0a-9df2-3c15-89d4-7b2aace06b29 | -2.56493 | -50.68457 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 228fc51c-dfd6-3391-83f6-8927e56f1e2c | -4.75868 | -55.66877 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b809001-70d2-36c1-b3fc-a6d63f98ca87 | -4.91629 | -55.86174 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 80e669d3-9e16-3f08-a354-4b5cad2ec705 | -5.09502 | -45.8335 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 320d70ba-2d2f-3245-85a2-e2c75a898c4f | -2.78537 | -51.66979 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| beab675a-5b26-3f34-b7cb-8532367c4f2a | -3.27386 | -54.04156 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f8bc4e6b-8fc4-31a8-94a4-2086e1a66394 | -7.4746 | -42.81816 | 2026-10-07 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 976f854b-dd9f-3f85-970d-cbbce0877d69 | -2.76022 | -54.11068 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| a8178145-77c9-3fc2-b152-31d631a80fd5 | -5.97246 | -40.9403 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 40622a96-4c36-3bc6-8544-4757de75bcca | -5.96959 | -40.93597 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 20108964-5def-3406-9beb-0c62aebd9051 | -6.23289 | -41.98915 | 2026-10-07 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 31814774-61ca-3f84-ace3-8a1bc6581a4d | -4.15755 | -55.15297 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| caebb9da-bd45-3abd-9311-b36847038dda | -3.06241 | -54.25783 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 075e8619-8abe-3311-b86a-e0a7c1fa465d | -3.84131 | -50.31554 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28189d3d-9cbf-35f0-b99c-0dc2485984a2 | -3.27714 | -54.02226 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11ed9469-86f5-33f6-b716-e9d9c960f911 | -2.98353 | -54.05239 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2496bd89-2dfe-3864-8c88-55b35740882e | -5.97779 | -37.82944 | 2026-10-07 04:19:00 | NOAA-20 | UMARIZAL | RIO GRANDE DO NORTE | Brasil | 2414506 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9d4d75d3-ddee-31c6-b7c0-5005a758110b | -3.66231 | -49.19172 | 2026-10-07 04:19:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d78f31f8-97eb-30fb-a300-10c8475da319 | -3.28267 | -54.05638 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 82f7418b-14e9-3363-802e-53490f354874 | -4.83851 | -45.98609 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77f1ff15-f8c7-30a6-8b36-cbdc0000ee24 | -3.57625 | -54.65784 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3d9fcf03-3ea0-33a7-b21b-52aa78eabf47 | -6.03243 | -42.26928 | 2026-10-07 04:19:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d5048cc-5d53-3ffd-a7fd-20ecbe4417f9 | -1.30785 | -48.06248 | 2026-10-07 04:19:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 783243fa-62a7-37ac-a961-e3314c25e68c | -3.03931 | -53.93864 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9f5a2fa-e95d-388b-97b2-ae412da67aeb | -3.26858 | -50.41394 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4facc720-f689-3f7d-ac71-5de0a927f275 | -2.99058 | -54.04854 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 933425e6-e6c1-3802-944c-ceb6bd9a276b | -7.18495 | -52.62112 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3232ea31-d10d-383a-9385-167959a1c8d1 | -5.72702 | -45.17244 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README56.md)
