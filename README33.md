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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b28a3a27-fc3e-341b-ba52-19620cf890f0 | -7.52384 | -47.33337 | 2026-09-01 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7080fe6a-b23a-3b67-bd1d-1758d93f512a | -7.11914 | -45.79486 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f111c02-ec07-36a2-b029-6138359888e6 | -8.23621 | -54.94003 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c433a2e0-366b-3436-91f2-8e6dcc3b88ff | -10.03217 | -44.69205 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f2d86a2-d1cb-3cf0-a694-5a249946054f | -10.06121 | -48.70653 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e87dd614-c39b-3e01-8dae-aa181bf9ae2f | -5.88161 | -45.57486 | 2026-09-01 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 855b4476-187d-3877-8f7c-f70699b45c52 | -9.47162 | -51.57854 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cccd969-80aa-3c22-8646-8fa6bef9864f | -6.15296 | -57.40368 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7a0a1e99-cab2-358b-81d9-4892a097ebc9 | -5.95882 | -53.61272 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e028916-9663-3187-9fe7-82ed21a9e37d | -11.94166 | -45.05032 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ee0e5a1-f2ea-3f1a-8cff-37da2615d255 | -8.50144 | -55.31944 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 573c1cdc-687d-3fa6-b2a6-2493fd34234d | -11.79436 | -47.67233 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc8cf393-ca6d-3383-b15e-1f8633678dab | -9.40295 | -51.60757 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d4fbe6f-4be0-3426-a157-f32aaac2a1f2 | -11.29206 | -50.60731 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67f67097-c77f-386a-b12e-51a15fa01569 | -6.62454 | -53.17454 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47a3718f-7c1c-38a0-8574-4ac197c5c413 | -8.58778 | -54.773 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efd6b7bb-b571-3f05-8221-56c70bff177c | -5.98231 | -53.6093 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fe97ee1-85d5-397a-9745-6400a44a9d49 | -6.73876 | -56.34237 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9b07def-9842-3384-a293-170e2e1465b8 | -6.41679 | -52.19972 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 762f960e-2654-309c-81a8-76c7bd6ed23a | -9.15726 | -59.54349 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f2ae630-b62a-3b5e-a28b-e262e9256784 | -7.28657 | -49.82153 | 2026-09-01 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7070cf3-51fb-34bc-9c46-994fa06eb7d9 | -6.69744 | -55.41016 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0d0d1019-7640-3636-8be5-1bbcb47ad326 | -4.34619 | -55.44202 | 2026-09-01 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5289d638-d63e-3be6-9bec-b5b2fe85552f | -8.93263 | -62.37054 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dbd92c5-fc5a-3855-9988-b8fc51022bc9 | -4.22347 | -59.86624 | 2026-09-01 04:40:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70618e3f-fa83-3b3f-8cab-be7b0536edbf | -7.34363 | -55.19105 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e22762e3-247c-398b-8baa-52adf3fbd650 | -5.31161 | -47.04426 | 2026-09-01 04:40:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f17fb23-5d5f-3e65-8c09-da62e4b1d461 | -7.09696 | -45.81503 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fd7aee2-2ae0-3559-903f-8b919065d1fa | -11.27221 | -50.60415 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b75a4df-4a2f-3fc5-b87a-ea2edd178c17 | -6.75887 | -44.58191 | 2026-09-01 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c55367c-4933-38f2-92ff-aaab55f0dbd8 | -9.14208 | -61.09801 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fec2da1-3e08-349f-b218-8b59d7ab7009 | -10.85886 | -45.33295 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85a0f5de-944b-3e86-935a-0b8945cc8b65 | -11.2273 | -51.28039 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3683c0d4-ccec-3eef-b00f-c1e91ce0a464 | -10.83035 | -50.71193 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a1367fc-8ae4-35dc-98b6-4c32ad254640 | -11.65627 | -47.61172 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 92406810-ff3b-3935-9cda-d00e81d25415 | -5.24942 | -55.89987 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b2fad83-79fd-37f0-8d02-ae1f9a6f4773 | -10.8265 | -50.7149 | 2026-09-01 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 622694c2-47ba-3041-a9cb-72074dda76ce | -11.21434 | -46.08714 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32ddb131-1b48-35b0-9eaa-b703d2a7e475 | -8.59096 | -54.77653 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f04ac4a1-1580-30bf-b4f1-7e29d1e79b75 | -5.48789 | -57.14524 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db074e37-ac12-3204-ad90-00fc8d9a0b13 | -7.45629 | -59.93657 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d577734-e72e-3e5e-97ba-893c778b1ae6 | -8.92824 | -62.35878 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d52d3a3-8dcb-3ef3-8ba6-e5d05c679263 | -8.70822 | -52.36778 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abe29b7e-3321-3266-b7a9-43d896a84444 | -11.65927 | -47.61639 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f689d092-0091-3e11-8535-b6fcc174d453 | -7.34622 | -60.57641 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 479e9638-bf25-316d-b905-7c010d694dec | -5.96015 | -53.62512 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0bdc084-6325-3453-a3f2-1c9e2f554ade | -6.20972 | -42.52302 | 2026-09-01 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 89d0c38a-0f0a-3acf-8bfc-bffa5e18862b | -3.63232 | -60.55526 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 665c2646-502a-3ffe-8536-06386f052650 | -4.79797 | -55.97501 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cbbcf26c-10cd-377d-964b-7edffcbb095b | -11.29642 | -50.5793 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| c09f8fe7-d30a-3353-81d0-fc0c916e8a1a | -11.94586 | -45.05106 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40f85491-7425-3754-9839-14323dabc1d9 | -11.71996 | -47.6413 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbe6e63c-3ec9-325f-9a25-18c3ed34aa3a | -10.73735 | -54.02152 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af1afef6-21a9-3039-8c4f-fb46138871e2 | -6.34993 | -44.09742 | 2026-09-01 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b5a1ef34-3ab8-3d36-8a1b-be950dd39839 | -10.75574 | -47.98611 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 936c631d-f6c8-3776-a695-023b8111513f | -7.35864 | -60.5844 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cc6114da-8654-3393-9002-b5bd425f0280 | -6.93987 | -55.64516 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51bc8492-49ff-3dcb-ba01-52cdb4993737 | -11.00195 | -48.39219 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f615806-966e-3222-86cf-ff63df0f9ffa | -10.3526 | -50.00154 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4f596504-7b7c-3cea-8ee8-a4f087f1bb1f | -10.05552 | -48.69816 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4238d8bc-54a3-3d9e-bb4d-3e7edc244b63 | -10.2046 | -50.36443 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 115cc588-0249-3625-a357-1ca26bb1f54e | -6.57206 | -55.61577 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fd32765-1cd7-3423-9c5f-295eab070327 | -4.94941 | -47.65138 | 2026-09-01 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5c13e01-1793-31e0-a63d-27a824fea216 | -5.24638 | -55.90107 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3d464101-4619-3bb1-9e6d-36e23ab065d9 | -7.51976 | -47.33674 | 2026-09-01 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89a5ae04-3e86-37e2-a93c-5d3fd8fd34c8 | -9.95544 | -46.77042 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f25c2496-b6c9-3e1d-b941-163ae54f7337 | -7.04243 | -59.22806 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a4cb57e-21f7-3b82-90d4-d9399e1d50ba | -9.17577 | -59.63948 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fc6f2df-61cd-39bd-a80e-d51e4533d15d | -11.07148 | -51.53421 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19b12bd7-0199-34e7-bdd7-1a37b26addbe | -7.358 | -60.57851 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c0dc00a9-30f4-3c01-a0f9-456c452288a0 | -6.60626 | -58.60117 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3300cffc-d3c0-3db1-9c69-20c82acb2aff | -10.4013 | -48.23298 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2522ccfc-7a70-30b1-82e5-fb512ad9b59d | -11.29919 | -50.58332 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 6c3c06c6-84a1-3d6e-b5f7-3d85bd591331 | -11.67488 | -47.61045 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ba7250c-761c-35fb-a9ef-ee51348f621e | -9.48477 | -57.02277 | 2026-09-01 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 710f5932-3d1f-37e0-82b2-b679799f7523 | -7.34544 | -60.58057 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dd8b2f65-4098-3db5-8c1a-eb30ac2d0deb | -6.72295 | -50.46551 | 2026-09-01 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc887891-63d5-3354-94cd-a53df7f4dbf3 | -10.83973 | -54.03754 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 836226a9-eae4-37ef-ba90-264329d7cd72 | -11.25177 | -45.13802 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e67ca9ba-762b-38de-bff4-bba67758c1e2 | -6.35936 | -55.86296 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67f5986c-fc3d-3eb2-b607-b0ab17c60382 | -7.63596 | -55.29068 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b055c0e-cd35-320d-8298-22d677003cd1 | -9.39004 | -60.5731 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4082a752-92ee-3ab2-a26a-aefb3144cf9b | -7.29325 | -49.84383 | 2026-09-01 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa8d99bf-d969-3fcf-a295-1b992de5b5f0 | -8.41767 | -44.99275 | 2026-09-01 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e6f0281-1bfb-3ed4-9442-6e0c9e3775df | -11.52614 | -45.49323 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24ec45d5-d879-380d-a389-711a44226000 | -11.67846 | -47.59667 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 308551f0-0a74-3e78-a666-9069f55210fe | -9.39077 | -60.56915 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d4c46c4-8614-3d71-a371-438c7d4dfe9d | -10.74248 | -54.03576 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bab20d2b-f75c-3917-988b-8015999dcd68 | -11.28541 | -50.58472 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| d0be1953-03b9-329f-b1f2-36d1ab31e592 | -10.74986 | -54.0592 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fccc6d4f-1498-3181-b1ec-e276d85be4e7 | -9.94613 | -53.99134 | 2026-09-01 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a192627-184e-3998-a334-c173ec359ce8 | -7.68199 | -55.34431 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b06e4e8c-4ad5-3139-8ee0-b663d2e9e987 | -8.80795 | -62.49797 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0113c375-8689-39e4-a6cc-1a1dc5a6c381 | -9.67078 | -50.86225 | 2026-09-01 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1033c99f-a6ac-34fb-8f7e-212d3869ab8b | -11.94948 | -45.05626 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e82a810-62b9-31d8-bcdf-7fd133f2b506 | -6.60738 | -58.59471 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3a3eec2-b862-3131-8f23-7aaf8d2c2a7f | -6.59798 | -58.58666 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 791ff55e-795f-336f-b4cb-301e552944ae | -6.59218 | -58.58897 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7710f13d-3a4a-3468-b883-ccf28386ff80 | -8.50506 | -55.29758 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 923f7f8a-7bd5-3665-9029-73f46a2a768f | -5.60088 | -43.99791 | 2026-09-01 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README34.md)
