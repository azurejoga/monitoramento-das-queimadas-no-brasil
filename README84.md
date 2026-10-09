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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fedd650e-8d8e-3745-aeea-cbd4f98f5ee0 | -5.10387 | -46.2231 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8cd5d1cc-5eb8-3959-9991-cffcc9e90a7e | -4.06506 | -51.03994 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95fa9ba6-a12d-3d3e-a9c4-0cc5054a0e5c | -6.88666 | -45.89516 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3989585e-5b17-3162-ac03-8b27da16ee1e | -2.8779 | -54.19714 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81d3c426-c9bf-308b-ad7a-541f21887e38 | -6.32853 | -43.82771 | 2026-10-09 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da56c27e-d138-3846-9d82-27a72fe068d7 | -5.73392 | -44.02567 | 2026-10-09 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 647f7f88-d001-39f6-b770-66b5065d1009 | -2.75551 | -54.09318 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae3d9ec5-c843-3ab3-b01c-4e4f1f233431 | -3.11709 | -54.17263 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0c748abd-55e5-3e0d-aac7-25881e4cd79e | -1.54717 | -54.55807 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6531074f-b160-34d0-9251-9a141168ad24 | -2.99818 | -49.21544 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebe1f696-832c-3843-8c72-e179ac8ca775 | -3.2004 | -50.82741 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb24ce75-eebc-304f-9f09-7dfbc41c57d0 | -3.2783 | -50.03906 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61427f9e-9124-3042-9bba-e7a8f0a77ced | -4.61989 | -49.21127 | 2026-10-09 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 520c7fea-9170-3e10-b628-20bedf229caa | -2.9854 | -54.07146 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57d4c26b-1a76-3e20-a781-564065153c76 | -3.00145 | -53.90994 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a90d725c-d8bd-3840-8b05-d561a5fe2828 | -3.30773 | -53.69692 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94fb71ec-5515-31b1-987b-3a88530528f4 | -5.38166 | -45.94658 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae6be635-0460-3f7b-8417-e0c89d52b454 | 0.50885 | -50.77722 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 81f5cfed-6bf2-3b27-997d-973f5232a1a5 | -3.54158 | -54.62852 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9f626f1-7fb3-3534-a8e5-daf1f746418b | -5.99654 | -40.9367 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9d888f85-9524-3461-a0c0-a81a461219aa | -5.70186 | -41.74383 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 262351ac-16cf-379f-a1ff-8c354c6231da | -1.33248 | -47.96015 | 2026-10-09 04:25:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c300adb4-68b5-3966-b0ae-8dfce7b60106 | -5.61338 | -44.84264 | 2026-10-09 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49b411f9-3310-3512-afa8-718a84117c84 | -5.70271 | -53.48175 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 55232b42-1818-3c6f-8b88-0e95c3511e85 | -5.28429 | -47.91056 | 2026-10-09 04:25:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ea89571-b02b-34b2-9ba6-94c5d2d68c94 | -4.62415 | -49.20769 | 2026-10-09 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35d1a394-4642-3acf-8fd5-06eb3529066f | -3.29469 | -54.00376 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 635ea107-bdc7-3197-8d48-a202a38d61e0 | -3.53724 | -59.40789 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a92feb44-b960-3cdc-bc5e-1beef52e16c5 | -2.32534 | -48.49438 | 2026-10-09 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2582d584-a315-364e-9d1e-07f5c459f052 | -2.73868 | -51.54862 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e013357-5850-34d8-8917-179ec22f16fb | -4.1281 | -46.86845 | 2026-10-09 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bbd296ce-6798-33b6-bc12-b67287e782fb | -5.68426 | -49.04488 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a7411c6-96d2-320b-ba1a-f27c558f0416 | -5.25478 | -55.9169 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1404bd50-f03c-3b4f-bc2e-854784caa89b | -3.08189 | -53.95227 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e97beadd-6975-3970-80bf-aa0318180f9a | -4.20297 | -55.63255 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbafff4c-9c8d-367b-bc02-c024c9364103 | -3.08561 | -54.26609 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d780e8f-6bf1-3820-b74f-d69ee9bd66ef | -0.16571 | -50.40573 | 2026-10-09 04:25:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4201aa8-79d5-3749-aea5-bcc277da744a | -5.70049 | -53.4664 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 00550507-980c-3405-bd62-209b5fb2fa2b | -4.06968 | -51.03708 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1361a33-10e2-368f-81ce-0e0d90bf93bb | -5.98043 | -41.35753 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5a9b60f1-d6f0-383d-adc3-bac0f4816caa | -4.29324 | -54.81195 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6216e9a-e819-31b1-812e-2b3dd6701a94 | -3.00924 | -54.07809 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae2d5888-711a-350b-af7f-52c7d6aa6a85 | -3.00675 | -54.09285 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5787ce0d-9be0-3698-90d9-6bda941f1750 | -3.88694 | -51.93532 | 2026-10-09 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 477dccd7-ed32-3a45-9d14-ac4b4e71d903 | -4.50484 | -43.62249 | 2026-10-09 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 18e29ce8-f3ed-39c2-8083-9ca75b77640f | -3.73613 | -51.20967 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7517c5a0-fa68-3a35-9c3e-606f38f3a420 | -4.9362 | -45.72818 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c724e8ea-5459-3faa-8da5-33bd12114faa | -2.32955 | -48.49088 | 2026-10-09 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8cd77c10-82a6-300f-b1e3-a7c2bd4329b5 | -3.48301 | -50.49183 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87d71eae-869d-3d89-abb3-aa685bc62473 | -3.00009 | -54.07682 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4abf34ba-251a-34ce-adbd-02b8786549ba | -3.05289 | -54.03399 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a11e839-918a-39c2-834a-5f1de299af0c | -5.87826 | -49.87755 | 2026-10-09 04:25:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33e10d0c-5da3-359e-b20f-48f1cc645e10 | -5.74556 | -43.27238 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ed1c830-ca87-3d54-ba5b-26c869e58cb4 | -6.14703 | -47.92048 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f35c868a-c8f0-39a3-8b3e-f4e96a49f819 | -5.98638 | -41.37274 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9cdfbc4e-c176-3c1c-9e8f-6c2aa5b2d05d | -3.60324 | -54.58594 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4a40d7a-0c41-3513-85b4-d0d0719a5aec | -2.84134 | -54.13266 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fc19746-7b96-34f2-9faa-655fcbbf24ca | -2.90402 | -57.21503 | 2026-10-09 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d6e2ded-560c-396a-a524-a4a3dcbab84d | -6.9682 | -45.14072 | 2026-10-09 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90222d65-073c-38e5-aa4a-6ff2a7fedf1f | -3.1044 | -54.18604 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e717c661-6d14-3bff-955c-b9dbc08a2c08 | -5.88047 | -43.41269 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ff1302eb-9291-3e7d-954c-75e42173b9fe | -3.01997 | -54.04984 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1283c2e-dcc8-396b-8ea3-af019d4d96b3 | -3.00485 | -54.04737 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acb17cac-b3fc-3b83-a9e6-249ee64f3a2a | -4.92449 | -55.85772 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f72bc319-f322-3540-a6f2-0eb8db07e780 | -4.62349 | -49.21183 | 2026-10-09 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a1b0de62-004b-3b8b-8224-e31dbf90f512 | -3.05671 | -53.91861 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ea7d935-b3a6-3222-a67f-92b7c8fdf6db | -5.69956 | -49.08735 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0731a194-9f55-370d-9d8b-0f8ac4e69376 | -3.17267 | -50.44298 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4257661b-2b4e-35ee-8b77-52a2f6009cca | -5.07539 | -48.40671 | 2026-10-09 04:25:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93fe55e6-d192-3832-942d-ceed249b2a08 | -4.50135 | -43.62197 | 2026-10-09 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f69ba23f-3e3c-3d5a-8db2-1727410f4030 | -2.21803 | -53.70047 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f23dab2-168e-3ec3-a796-1a90326d7b70 | -3.56459 | -54.68393 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1b7dc86b-7353-37b2-9092-7a453c44df6a | -6.88173 | -45.90508 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4605da02-3758-3bbf-a8c7-eeb5ea89d980 | -5.32976 | -45.1842 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 979aa1e3-e2e9-3482-a994-7f51f9dd7b13 | -3.53175 | -54.65564 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c6c0679-cf9c-3b8b-b320-ba431e322f0a | -6.91861 | -44.56341 | 2026-10-09 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9f5c869-4c84-33b2-8cd4-839f7d462f79 | -4.74574 | -55.67593 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 33c21c91-cb02-317f-9879-13df862bd6ee | -3.30405 | -54.69574 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04be2213-ee57-3d9a-bc51-f38eb83a6eef | -3.10842 | -54.1931 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5396c28-887e-32c6-9b4e-03d3728aa646 | -2.78017 | -54.0696 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9533e342-e623-3f5b-8c82-2f35ffc1c966 | -3.03364 | -42.10962 | 2026-10-09 04:25:00 | NOAA-21 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6378fec7-203a-3b5f-8c34-9a45f11dfeb7 | -1.40569 | -55.41669 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97e0d127-7483-3b0f-bf89-8f21d5fa1e66 | -5.83847 | -44.92852 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 173e1d4c-dabf-3a64-a881-3c10657f2420 | -4.49576 | -42.5423 | 2026-10-09 04:25:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab2a0458-e8bc-3dc5-8c9d-e01252f0dbe6 | -2.74242 | -54.10949 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0a1d5bb-ae11-359c-bea4-0e9cbd57f6d6 | -4.09994 | -54.0255 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eb4e82a1-6030-30a7-a5b8-b190c49f730d | -4.07962 | -59.8372 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c708d4e-6ef8-3c23-a676-248805885ac3 | -2.73849 | -54.13346 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f680efe5-a8b0-3243-abe3-eaa7fb15ce08 | -2.77921 | -54.07553 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3aad0aa-0bc4-3f29-a2ff-62015cc7448d | -5.70428 | -53.47227 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e479010-0a96-33ee-9eb7-6785abfcbc91 | -3.25733 | -54.04267 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 871de466-c187-33ac-b68d-3e11517d9377 | -3.11398 | -54.16793 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78a99692-24b1-39ae-ad35-36952d82fc12 | -2.73635 | -54.11466 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 998dd41d-d530-3bad-bf4e-32f2f530a33e | -3.01173 | -54.06336 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c3f2c6d-c7f6-3c1a-93ad-40427513c3dd | -2.08356 | -46.58051 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3777e190-b3ec-375b-b6f1-406e59657428 | -1.15888 | -54.23132 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5c8549d-1a7d-3ce8-a8bc-0dfb9d128af6 | -2.75704 | -49.53309 | 2026-10-09 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d30500dd-460c-3a1b-a9bf-8b15eff7f960 | -4.9831 | -46.03901 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ac3c5c8-a69f-3420-8dd8-00cc6945eb1c | -4.76215 | -44.00602 | 2026-10-09 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16f4e835-f663-3437-9436-e2be31b02d3a | -1.15467 | -54.22411 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README85.md)
