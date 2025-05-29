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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a9db158-11b3-3f94-9a56-f69fc6b0a21b | -7.66998 | -46.09782 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f513f2e5-c6db-39a5-b00e-892d03af0c46 | -5.21657 | -43.30216 | 2025-05-29 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7a6a1ce2-7b20-3fc3-b4d9-a1df668d74bf | -7.67352 | -46.09841 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4d8623dc-85dd-3633-9b4a-2195cae2ceb7 | -5.64703 | -43.58751 | 2025-05-29 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fedc294b-4a65-3443-94eb-cddfb82c1682 | -7.94801 | -49.76253 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba6a7761-fb58-34a6-b84d-9af2fa9f1bfa | -6.24043 | -43.37934 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b49ab89a-ba65-3326-956f-74dae464d6af | -7.6357 | -45.93084 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1aebbff9-66fb-3661-ac95-dd5e08e52b90 | -7.67836 | -46.09103 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 884f3927-f9da-3a8c-9b37-7fd7b1e685bb | -5.21602 | -43.30563 | 2025-05-29 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 95faa573-a6de-3c57-a53b-3a7ef6b607c5 | -7.32285 | -43.68682 | 2025-05-29 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ad8f387-8a57-34cb-9668-7658193e1759 | -8.01617 | -49.68486 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8d1f13fc-7a65-3b7d-a610-d1f911069c39 | -7.6392 | -45.93142 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b61e1168-e5b8-3004-b0c9-c9e8d09de679 | -7.19012 | -43.10777 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5565ed5b-4289-3ebc-867d-967dc2a22932 | -6.20495 | -43.34502 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 871b16fa-c72f-3052-a6b6-804361203a89 | -6.24098 | -43.37589 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e66159c6-5ed3-3e39-8ae7-9eed2f18aac3 | -6.31877 | -43.37758 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03c32079-d2f4-3e17-8b98-cb297d7e91cd | -7.58423 | -45.95882 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e172d60-5eac-38ed-8acf-d70155da859b | -7.5605 | -43.32269 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b99e5f4c-3056-3066-83f0-26be2d0d8c6d | -7.58097 | -45.86937 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a309ca45-d861-3639-abef-8f4958074f49 | -7.98735 | -49.69067 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a46deeb-6ad4-3f6e-9f3b-494fb11dd23b | -4.96074 | -37.93637 | 2025-05-29 04:12:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 323a78e6-6fd3-342f-9bff-326669f2c570 | -7.34161 | -43.67556 | 2025-05-29 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ecfa3e94-f917-3e3b-b593-6ca71f593cab | -6.23877 | -43.36844 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daec3ebc-2164-3742-9e06-fa05f596a980 | -8.45501 | -48.33025 | 2025-05-29 04:12:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c0b1811-5ac7-3541-acdf-670f932d0937 | -7.24249 | -43.09828 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c16797a9-97d4-3079-ad89-734dfe7e80eb | -7.46984 | -47.06264 | 2025-05-29 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b9c9571-8f1a-361d-98fd-f764dd45773f | -6.55935 | -44.49279 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2035f6cd-f5bb-362f-b709-c1b1ae30f770 | -8.00575 | -46.15037 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbf0ade7-7883-323b-915d-9aa7df64a913 | -8.7509 | -49.76839 | 2025-05-29 04:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a87c9245-d8cc-31e9-8ec6-807566ce2465 | -7.63155 | -45.9342 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8e37d2b7-4353-3863-be41-cb4d97851fb7 | -6.91326 | -47.85538 | 2025-05-29 04:12:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27bf4adf-2517-3a76-bc93-ee77baeff4da | -7.0802 | -44.92143 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a3f5c120-312d-397a-bd13-e1fca0158302 | -8.4044 | -47.09369 | 2025-05-29 04:12:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ede0120e-b3e8-3a4e-98a1-3a4994a43025 | -3.81247 | -48.99301 | 2025-05-29 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 798e9f30-02ce-32ba-9555-edeff87deb0f | -6.83248 | -44.65022 | 2025-05-29 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc1fb57d-e601-313a-b24f-fe60fd048eac | -6.81043 | -45.37185 | 2025-05-29 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcd4412d-e552-3ead-b430-7210549434d5 | -5.20939 | -43.30459 | 2025-05-29 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91f30d81-5331-39cc-8cee-e638073fbe4e | -5.28245 | -35.48112 | 2025-05-29 04:12:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ab7dd74-1668-3cae-8ea8-81eaef1d3b4e | -7.62244 | -45.74812 | 2025-05-29 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61f05b53-1f9e-379d-be13-75c789cdd3c4 | -7.58227 | -45.86151 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f32b56c4-8f24-3154-89ad-8113b893a797 | -7.6218 | -45.75201 | 2025-05-29 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d8c873f-7f78-3fbb-af26-b4060f1c3dae | -8.40222 | -47.10676 | 2025-05-29 04:12:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73a75f15-6f96-311b-93bb-8aab4b8ce63c | -6.3392 | -43.37729 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3cd8799-fbbe-3184-bacd-7ff4a9999ce6 | -6.82234 | -44.64869 | 2025-05-29 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d347f71c-bd10-3d7a-8893-cb33d15cf4ad | -6.85584 | -44.82926 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6778d224-955c-343c-a4bb-070070080c4a | -7.94522 | -44.85764 | 2025-05-29 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b583b11f-65b2-3d2e-8e99-48db1d7f3d47 | -7.07561 | -44.92821 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 187619ac-4831-347e-bf6d-0949e88e3ac7 | -7.27834 | -44.22454 | 2025-05-29 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6779cab-94be-3633-a517-997b96912953 | -7.46684 | -47.05757 | 2025-05-29 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed1c07e2-888d-3001-b69b-4b3115aa149a | -7.91411 | -43.70628 | 2025-05-29 04:12:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bbe80a1-3ff9-3bab-89c6-4799285e5735 | -7.51781 | -43.35524 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de84b7e2-21da-31d9-992e-2578d29a99ac | -6.22591 | -43.34123 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0223db4f-c08e-39c5-8a0a-5bf341c97ba1 | -5.10726 | -44.453 | 2025-05-29 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e556ca77-9b16-3fe9-a6de-f3c9a1b080f4 | -6.80414 | -45.36692 | 2025-05-29 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| addd3782-181f-376b-a162-045393c12f54 | -5.0899 | -45.83118 | 2025-05-29 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d27e42d3-fc92-3af6-aac4-fd9ad07ca04c | -7.58292 | -45.85758 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1622e43a-631f-3c6f-bd08-b71a494d1bc3 | -7.07621 | -44.92455 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 13cba234-eca2-38e9-b6d6-bde34269427d | -7.58554 | -45.95091 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ad56aee-2238-32bb-8fe5-ff0f4022007c | -6.33587 | -43.37673 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22279c2a-4086-307c-affd-e1f89b188107 | -5.21383 | -43.31949 | 2025-05-29 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e794c692-f7c3-365d-8fcf-3efc67904503 | -7.95131 | -44.85129 | 2025-05-29 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0392033d-eccf-32b3-ac72-2552ee63b64a | -3.58045 | -48.94872 | 2025-05-29 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c62baa8-2d87-38f0-93e1-c694611ae430 | -7.57657 | -45.85252 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c6b705f-7947-37b6-9c52-de972b881201 | -5.76559 | -43.48147 | 2025-05-29 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 563859a7-f900-39bd-9a82-896c71c40a6e | -6.33975 | -43.37383 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0f3a768-7100-37b8-ae80-930a0aa458bb | -7.66863 | -45.24981 | 2025-05-29 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53bf683e-50ec-364a-bc63-38a385aeae50 | -7.47056 | -47.05822 | 2025-05-29 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 976cf4e8-372a-3b14-ac15-bbbeb6023d3a | -9.34818 | -40.26888 | 2025-05-29 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4f60fc8a-8cbc-35c0-b31e-9ee9d0fc7a68 | -7.23311 | -43.09325 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 81220339-9c78-3e4d-a165-75c17817c8e1 | -6.2226 | -43.34071 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| abecfe66-1c8f-387b-91a9-06ae2ea66937 | -6.80822 | -45.36367 | 2025-05-29 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98d5b3e6-a1ad-3a9f-ae27-11d1b3f2c117 | -7.23256 | -43.09672 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8ddc6864-70eb-3a93-91a2-2bc8e12d09fa | -7.07501 | -44.93188 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc908823-94ed-3164-ba9f-4638ef81d2ae | -8.67189 | -48.28311 | 2025-05-29 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a1afabc-1ffe-3b2c-a317-d31f515b9a42 | -5.7651 | -38.90674 | 2025-05-29 04:12:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af61ce3a-6fae-3268-b747-7a8d3b4b5586 | -5.05252 | -43.24396 | 2025-05-29 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba41e937-842c-3b93-8718-abaa20e7d2c7 | -6.3436 | -43.37088 | 2025-05-29 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 026bf43e-b297-3395-9c14-acae7baccfdf | -7.63506 | -45.93478 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f019714a-04cb-32db-a45d-6064a205c604 | -8.01087 | -46.16337 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 045b546f-d5a1-34bd-960e-85751243d4b3 | -6.24153 | -43.37243 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27d5e4e3-5fd5-3dd8-ab14-1462db6e16c0 | -7.67771 | -46.095 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c77438c7-4bb2-38bc-bb4e-16056f8b2f65 | -5.21106 | -43.31551 | 2025-05-29 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 40292a4d-b14f-33bb-b173-35e7b7037270 | -6.80476 | -45.36312 | 2025-05-29 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e686ab8-542a-3bcc-b108-a82c512a6085 | -6.90933 | -47.85472 | 2025-05-29 04:12:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d1ba04a-4b97-3989-82b2-0b7175005aee | -7.11993 | -43.33799 | 2025-05-29 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b96adf04-92e1-33ce-b669-c42eef6419f8 | -8.01504 | -46.16006 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7256d3b8-3ac0-33d3-afd7-79735532457d | -4.81481 | -47.32349 | 2025-05-29 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 904ad156-2a9a-34e5-a923-ddca11d8c589 | -8.02053 | -49.68559 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ca51c32-96e0-3085-a2ba-f32253316159 | -8.01493 | -49.68671 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0d7084d4-688c-3fda-8ce9-6279d54b5172 | -7.54784 | -43.33844 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e03d26ce-263d-3060-8773-ec343f32ef72 | -7.33775 | -43.67851 | 2025-05-29 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 650505bc-88d3-3d68-943f-3ef58257966d | -8.01564 | -49.68252 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a3a39b97-3ebb-3f12-b1e2-3b828e1a7754 | -7.57526 | -45.86038 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 128a3415-44ac-3989-9407-6c113583e9c6 | -7.58489 | -45.95486 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bad248ce-bdef-38d9-bd88-732eebd1a397 | -5.10785 | -44.44934 | 2025-05-29 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b1a107a-33d5-3c45-a2e3-85366bbbe616 | -5.76504 | -43.48495 | 2025-05-29 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6df6e972-3370-3e31-8ab1-f59a0701c2db | -7.32671 | -43.68388 | 2025-05-29 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 80213578-783b-3cdd-b083-7ae91a7fdfe6 | -7.54839 | -43.33498 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94276104-385d-3435-83ba-93ddb6974bad | -7.11938 | -43.34145 | 2025-05-29 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e894f467-3c5d-3158-94f6-ef743eddb369 | -8.19632 | -49.81562 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README9.md)
