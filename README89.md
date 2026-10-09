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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b98a439-8d93-3f91-bdf0-bb6601a1d71c | -4.09395 | -48.96006 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 23f6f978-0cd0-3345-a91d-dc4920292577 | -5.74976 | -43.26878 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da1a355f-953b-3dc8-8af9-411acf2de7a6 | -4.88801 | -43.34126 | 2026-10-09 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07985d8b-2b25-39db-9411-bcf9cbdab917 | -3.0138 | -54.08181 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf50ec46-3be9-3eec-9088-42e3074d7e95 | -3.32237 | -50.18344 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec0356a8-556b-318a-9d4e-ff2b3a95f26c | -3.76962 | -58.84091 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce1d7469-1c1e-36e1-92f3-0d35f3d6247d | -3.8404 | -44.14022 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24237975-2543-3a9d-bc72-7edbf682d48c | -2.98997 | -54.07522 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19da8532-79cd-34ab-81d7-4f09f0bcd81c | -5.70104 | -53.48378 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d55d7d6a-2418-32d2-9471-e5c5d5feac97 | -3.0993 | -53.94011 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 73fdbd6f-307d-397e-8ceb-8f09874788ff | -5.06254 | -46.18502 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cefa7ee5-2911-3689-8254-edf4297f57ae | -3.22469 | -54.29974 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d403f72-7387-3106-a6cd-8604acae726d | -3.36326 | -50.48601 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1445ce8c-ada9-3739-a122-b541def42692 | -2.74571 | -48.42933 | 2026-10-09 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fd4992c-abb8-3e6a-b4de-87ef425e075e | -2.97306 | -54.11529 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a584ccc0-f1e1-32bd-ba8d-6d8c8cc024df | -3.58266 | -54.31583 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a51f9d43-2fd8-3332-9253-5dd168617e38 | -6.9357 | -44.56615 | 2026-10-09 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91cc52ae-933d-38db-8155-8b30e9161209 | -5.85528 | -47.41839 | 2026-10-09 04:25:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e0032bd-750f-3471-a86e-55b339698879 | -4.2864 | -49.0938 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 761374b0-9157-3997-8fa6-8c73f7dc0678 | -3.0103 | -54.10256 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b043ace0-719a-33ab-b007-3af7fae9f51e | -2.49835 | -56.06274 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 52f61b71-c172-3ad0-8e00-601ceb82dc18 | -3.4599 | -50.58666 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 40f55d78-56ee-34b7-8810-2df13f549a93 | -5.35215 | -45.72309 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ad69364-a8ea-3a72-85ae-2f458e92e2e0 | -6.8959 | -39.53657 | 2026-10-09 04:25:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c58fee97-c6b1-3966-96ad-54ae415d83a8 | -2.73947 | -54.12748 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82e95f3f-0740-3c85-9b49-21d12c8cd8ae | -3.01288 | -54.09399 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a299663f-f011-3314-a64e-3fcdba017e03 | -4.09885 | -54.02361 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ad47cc3-af14-34c9-a9c8-583fcb0b1c08 | -2.99787 | -53.90047 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb4bf96d-af2f-322e-a756-e965ce23a8fe | -3.74766 | -49.38559 | 2026-10-09 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 362c4b14-812a-3738-9f35-b17235e9cea7 | -5.5949 | -47.27961 | 2026-10-09 04:25:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3af064c-2cee-351e-a6cd-cb7b9e00d8cd | -3.92889 | -54.57721 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 094dd124-b06b-3c14-93a4-87df9b6cc266 | -2.74897 | -54.10133 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b33ee2c5-bafe-375d-823a-fb1ca14344cc | -3.16424 | -50.59335 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c341b926-a663-3293-8533-2849251c3e7e | -4.82374 | -45.83773 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be2f6375-ca56-31c7-84d2-31ad9f949cdd | -4.32657 | -44.65333 | 2026-10-09 04:25:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfb5018e-e2ac-3ac6-bf18-b32ad7534168 | -6.88227 | -45.9016 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af103bd6-35ab-344a-9f59-d6651780ff06 | -3.19486 | -50.55524 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54d244e5-2d39-368e-a69b-a9c7e8e9f21c | -4.28706 | -49.08971 | 2026-10-09 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 760e9ca3-b2b1-3457-afea-6602560bd2c9 | -3.47621 | -50.33294 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d0f4047-97e6-3281-a3b5-c839ecf61ed6 | -3.34303 | -50.41102 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 90b5b661-8d2b-3af5-b47b-6928a4e9b3af | -6.9614 | -45.27569 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58c8343f-977e-3c97-93c8-50b5f878b215 | -4.20239 | -55.63596 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ae7e2cd-a355-3608-9d82-19c605a9ab31 | -3.57031 | -54.68167 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0a1e3407-6474-3f71-93dd-0faf68b86058 | -6.89518 | -39.53894 | 2026-10-09 04:25:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3bd7824b-9411-3b1d-8bcd-ad1c64b710ae | -3.55731 | -54.69572 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78198d2f-5d59-35e1-b678-85176f19dfa7 | -2.07745 | -46.57598 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11b0ea36-10b3-3954-9e2c-9f96f293cf2a | -4.80302 | -54.67596 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb102398-d437-3d0a-b496-9e3b745b5641 | -5.3822 | -46.18623 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36d8f380-3cbc-34ac-a01d-e46fe9b18bf2 | -2.4861 | -56.17157 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b4f6526-50a8-3ec5-91fa-08417434854f | -3.00972 | -54.08135 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de9f4a47-31a4-39bc-8ea0-5e2d6b43b6ac | -4.11601 | -55.03502 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5580aa2f-f851-3577-a5ea-58975bee6484 | -3.07501 | -53.96281 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ce4672b-534c-35b0-bcb7-210fd5b0d6f0 | -3.00705 | -54.0658 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78bdc23a-517f-31ad-b58a-29077b452edf | -5.75159 | -41.62528 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6982418e-b512-3408-a518-fab105f07405 | -3.29014 | -54.00018 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22624b29-f276-3335-8242-1361b707c59e | -3.57105 | -54.68127 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c1bacffe-e3e3-366c-a8fb-e56da3cc3869 | -6.92356 | -45.87588 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebbaa017-9df6-368a-ab5d-3bba5a2a6b95 | -3.08548 | -53.96167 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bc2a905-6a27-3673-b78d-96dae09b44e6 | 0.50035 | -50.77854 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9e4d9ade-f79d-331d-852d-1aebda3edd59 | -1.39508 | -48.94235 | 2026-10-09 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70118882-7f2b-3fce-a123-04b3a449626d | -3.11166 | -53.77207 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 511e44c2-1f54-3760-b649-4e72851f8d33 | -3.28967 | -49.13028 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76a2585d-9c5a-306c-b742-66ed32daed49 | -2.88707 | -54.07585 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 08ad0030-6021-3f97-94f9-2b7a15dd5b09 | -7.10675 | -42.52807 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 00eedc0a-a819-3afc-8cf9-d5c60632e67e | -3.00877 | -54.08726 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fd6952c-374d-338d-b5e9-cd0fb714de58 | -3.31078 | -53.69354 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f870fd5-4bc6-397d-a110-8fa2e4ad198e | -3.29301 | -54.04504 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 44c1c1ec-a77a-336c-839f-3ec16b368323 | -3.17186 | -50.44792 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d932b0d7-61d7-39ea-8873-b9dff3157566 | -5.47482 | -41.22652 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| efe451f9-5927-3449-97fe-6e690915b3a2 | -3.10271 | -53.76492 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b67ce67e-5511-3406-8ceb-9b4722e86228 | -3.30862 | -53.69138 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea28427b-06a6-3b2b-87dd-ca5c79943d09 | -5.94642 | -45.68419 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1c1df929-7b38-33a2-8a03-cf97af47719a | -6.16368 | -39.44485 | 2026-10-09 04:25:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| de9079c7-9b15-3e2e-be53-4c7f60586597 | -2.75362 | -54.04111 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5e47719-c993-30cd-958b-7b6705e11725 | -5.32104 | -43.42357 | 2026-10-09 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5c21a5d7-7ff0-3c62-bf36-be6fdb25f11c | -2.34414 | -48.8722 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 60224210-be6d-38f1-abfc-aaa6a39f8b75 | -6.4562 | -46.01627 | 2026-10-09 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f1cf7a3-22c0-3814-9061-6c41b41a4eaf | -3.25478 | -54.02718 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e68b3eb4-e27f-3c07-b76f-bb59db66d02f | -5.71904 | -41.62912 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6de5bd51-44b8-3d58-b4d3-fbcadc64e900 | -6.87511 | -45.90409 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2a23036-d5b6-3a03-a510-f9d0fa781b3c | -2.89586 | -49.36623 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c00412ff-78b6-3690-92e7-08e2c0b7be6b | -1.19926 | -54.2149 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a23d9949-cd09-3ce7-92d5-4d990b1c6171 | -3.00782 | -54.0932 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5dcf9d3-67c5-36b8-8374-f678bdda65a8 | -3.65975 | -54.28189 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bf8732e-a306-35e0-8523-cdbec0025936 | -2.99865 | -54.08567 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23b7008f-47db-342d-a895-0f25279ea5e9 | -6.00265 | -40.95273 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| d24eb027-9894-3d96-b7ca-0d4fbe111d09 | -2.55266 | -58.03526 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 02d25d03-555f-3b2f-bafd-b10ff1ea579a | -4.51752 | -54.89529 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95107142-809d-33b2-8bb2-fca3a3ba99d7 | -4.55328 | -54.969 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7345bfff-0de8-39e1-8391-b17f5d78e01f | -2.93634 | -54.05456 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28a6a6a5-41cd-3172-afcc-e0c4be58d001 | -3.02477 | -54.04746 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a0ab0ba-d040-3238-ae7c-49c9c38732e4 | -2.75961 | -54.10003 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1eea3820-f30f-3411-8bc9-c3396fc3dab8 | -1.32301 | -55.44278 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b76ed3f-4fdd-3376-945a-ff8c7717171b | -3.00275 | -54.11648 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 810dd3d5-efdf-3ee0-8e99-08a5d7009839 | -2.94148 | -54.18063 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbef254d-207b-3adc-bd14-d162a22e6156 | -2.90023 | -54.02647 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c9532dc-b551-3bf7-844c-4aad450da7df | -2.82376 | -51.28508 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d270e17c-bd76-3370-b863-dfea4230ed9e | -5.68421 | -53.47834 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f25f2eb-c89d-3329-a3d1-78ee84872144 | -3.77655 | -58.58217 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0ca45f96-5c80-3124-af8c-db7bb33b41b7 | -3.53298 | -59.50436 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README90.md)
