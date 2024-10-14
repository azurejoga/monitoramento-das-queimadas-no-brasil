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
| 26fe387b-0cea-35f7-bf00-68e5a3867791 | -19.0724 | -48.3148 | 2024-10-14 00:16:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 00248954-6fcf-38a9-97d0-0dacf8a4cadf | -2.4344 | -46.9195 | 2024-10-14 00:25:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| dff4d117-5e2a-33d3-baf0-0a9a661170e8 | -2.4529 | -46.919 | 2024-10-14 00:25:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| cb285c19-7ff8-366a-ac31-05167c696b3f | -2.6117 | -49.1198 | 2024-10-14 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| ba28177d-14f2-3dbd-9114-cbc13ca39ac6 | -3.0656 | -51.1883 | 2024-10-14 00:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 06822752-14fa-3be7-8f85-e12401a9b195 | -3.0657 | -51.1675 | 2024-10-14 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 865ee695-a86e-3936-83a7-f58fff97b150 | -3.084 | -51.1878 | 2024-10-14 00:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 0f42b15b-d41c-3b2e-8b43-c4cf48dde058 | -3.1606 | -50.4766 | 2024-10-14 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 5bc97a74-c274-339a-96ff-37553fba0b49 | -3.1791 | -50.476 | 2024-10-14 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 87d08851-012a-366d-bd35-45defdd3ed30 | -3.1792 | -50.4551 | 2024-10-14 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| e240cdaf-94e3-36a9-a2fe-3f415e070fd3 | -3.2889 | -42.8561 | 2024-10-14 00:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 40e0ddaa-61c3-3487-8d46-5960f57c5290 | -3.289 | -42.8327 | 2024-10-14 00:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 2434b07d-3e62-3da9-90ad-b84d63a70198 | -3.3076 | -42.8553 | 2024-10-14 00:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 216.0 |
| f398d880-90a3-3f2a-aef6-3aec5778d055 | -3.3077 | -42.8318 | 2024-10-14 00:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 381.6 |
| 21d1ed24-0900-32f6-874b-d7ba6bb1b58b | -3.3078 | -42.8084 | 2024-10-14 00:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 2a210bf2-d64b-3344-a2bb-79699c9b4668 | -3.1982 | -50.3077 | 2024-10-14 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| f649d0e8-bbf3-30e9-bfe7-b45ae5b40ea3 | -3.3274 | -50.3245 | 2024-10-14 00:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 8b9b7c18-5c04-3646-ab98-d4fc8f1a2a7c | -3.3275 | -50.3035 | 2024-10-14 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 6f572186-e567-311f-b230-78738cf014fd | -3.3643 | -50.3233 | 2024-10-14 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 4fe8f127-33b3-3596-babf-b9ad6f22fe4b | -3.4279 | -52.782 | 2024-10-14 00:25:26 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| dbf39174-e505-33f3-ad78-c58eac1bfcb6 | -3.8722 | -52.2974 | 2024-10-14 00:25:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 136e13bd-4880-30e5-94d6-32c3f71bf212 | -3.8723 | -52.2769 | 2024-10-14 00:25:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e8ccf4b8-a3a4-3d96-8f4e-23493ccf9342 | -3.9102 | -48.3682 | 2024-10-14 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| de19b930-5aee-3943-9f8b-74fabc28b2df | -3.9103 | -48.3466 | 2024-10-14 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 63ab75a9-9440-3d1b-8385-f2217005901d | -4.1145 | -48.2947 | 2024-10-14 00:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 79fec5e9-5108-36cb-afbf-5b1b5711ec8e | -4.1146 | -48.2731 | 2024-10-14 00:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| c4960f3a-d92e-3fa5-a001-9e08afb04bc8 | -4.3428 | -50.5172 | 2024-10-14 00:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 6c8eb559-d19a-31a9-ba61-5361eb579a8a | -4.343 | -50.4962 | 2024-10-14 00:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1b969ebd-d622-3d56-8a7d-6674c363b585 | -4.6197 | -44.8626 | 2024-10-14 00:25:32 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 327343df-af0f-36e4-a4d9-f10764d47905 | -4.9097 | -46.0163 | 2024-10-14 00:25:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 7bded9d6-1117-3f87-8ede-50500cf0f09d | -4.9099 | -45.994 | 2024-10-14 00:25:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 38aba788-a237-302e-a887-e01ebf25c18d | -5.0625 | -48.0745 | 2024-10-14 00:25:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 505fdd11-251b-3512-901b-a93d71f57e80 | -5.0627 | -48.0528 | 2024-10-14 00:25:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 6ffe5a43-59df-32a9-8ed6-de5a197d38b6 | -6.1342 | -42.7906 | 2024-10-14 00:25:41 | GOES-16 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 12f73893-a823-3166-95b4-2674524dcf4f | -6.3749 | -59.9936 | 2024-10-14 00:25:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 562502a5-a800-3f81-93d7-a88fd50b6292 | -6.3933 | -59.9929 | 2024-10-14 00:25:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| bfda93d3-e5a0-3ac5-b59a-7206d6809465 | -7.9623 | -49.0823 | 2024-10-14 00:25:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 119.8 |
| d4537cf1-5435-363a-b649-3e172f7872fe | -7.9625 | -49.0607 | 2024-10-14 00:25:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 243.7 |
| 68f3aac8-4f49-3861-a1c6-d20d4162a97e | -7.9418 | -63.6365 | 2024-10-14 00:25:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| cbec8105-da28-35ea-893f-e132063bf0bc | -7.9419 | -63.6177 | 2024-10-14 00:25:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 0320dd17-30d7-30fe-86f7-c28ad4d4e544 | -7.9603 | -63.6359 | 2024-10-14 00:25:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 59b9c8aa-469b-30cc-b36c-d85fd1eb9669 | -7.9604 | -63.6171 | 2024-10-14 00:25:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 521bddc4-7bce-3a38-882b-28079824e703 | -8.3207 | -42.7394 | 2024-10-14 00:25:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 57bab2ab-a69d-3359-bf66-d385109770ff | -8.3396 | -42.7372 | 2024-10-14 00:25:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 513843e9-5465-3e71-8de0-27e60e2905b8 | -8.4734 | -48.6276 | 2024-10-14 00:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 108.5 |
| efaf17cb-8cc7-3ec5-b1b2-e289cf4c4c0e | -8.7377 | -63.4952 | 2024-10-14 00:25:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 232030ec-86f0-39a6-8126-7b81ce618303 | -9.1021 | -47.9355 | 2024-10-14 00:25:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| a9a94cdf-7ec1-34bd-a347-2d0d617436fb | -9.1042 | -61.1811 | 2024-10-14 00:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| ce112d97-4ebd-3656-8a0b-245cdc6f6741 | -9.1043 | -61.162 | 2024-10-14 00:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| fb319c31-ae4d-3d72-b243-8ae3596f3726 | -9.7988 | -36.1213 | 2024-10-14 00:26:01 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| 2b804456-d79e-3c8e-bdc0-9953d5e6b2d6 | -10.0622 | -44.2391 | 2024-10-14 00:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 127.5 |
| ad9dfa40-8eb8-3e10-9b72-6fe3e8e8f24a | -10.0626 | -44.2158 | 2024-10-14 00:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| a528c913-fb15-3b98-946d-bca3d5a51148 | -10.0629 | -44.1925 | 2024-10-14 00:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 6a27c93e-a444-3495-9fe4-a20483c54a76 | -10.0813 | -44.2366 | 2024-10-14 00:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 81cf59a5-ff72-3e46-b360-c9f932a99384 | -10.0816 | -44.2133 | 2024-10-14 00:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 28a0d7f6-1d12-38ba-9050-e9d26bea35db | -9.9973 | -47.3329 | 2024-10-14 00:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 34f85b28-35b1-38da-b1ba-75a5b40d0346 | -9.9976 | -47.3107 | 2024-10-14 00:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 321d534e-d5fb-33e1-919b-0f8daeb8b7d8 | -10.016 | -47.353 | 2024-10-14 00:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 936ae108-b8e6-31cd-8f4f-654fc7bc57ea | -10.0163 | -47.3308 | 2024-10-14 00:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 199.4 |
| c59f5d8a-1e0f-3e17-8422-5ce2258e5216 | -10.0166 | -47.3085 | 2024-10-14 00:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| a00fd837-6de2-374c-9dd6-89aac60dcc2a | -10.0352 | -47.3286 | 2024-10-14 00:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| d6909eb4-2a38-37c9-81e9-0bb5025cc279 | -10.2831 | -47.2112 | 2024-10-14 00:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 123.6 |
| d87a0340-4b72-3c18-ba10-3d39e165eae7 | -10.4317 | -44.931 | 2024-10-14 00:26:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 12710080-3da5-3d8c-a2f8-7284780b20e0 | -10.4918 | -42.433 | 2024-10-14 00:26:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 124.2 |
| 8c712adc-940f-3f27-b50b-4c84ef3e0917 | -10.5307 | -49.7843 | 2024-10-14 00:26:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 8974713f-5419-3b4c-8fe3-3d0a0dfa475f | -10.9116 | -44.7048 | 2024-10-14 00:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| c244bd43-6e45-3f0b-86f8-96367358bd38 | -11.17 | -39.9192 | 2024-10-14 00:26:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 54.3 |
| e0a11aca-1d16-36d0-98b9-d8a5cf35adb7 | -11.1705 | -39.894 | 2024-10-14 00:26:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 43c8f31c-2abd-3af2-87d8-17204aa4dce4 | -12.0925 | -50.7023 | 2024-10-14 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1dd93eb7-8a8d-3284-8111-b8b510986738 | -12.0928 | -50.6809 | 2024-10-14 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 144.4 |
| d43777b0-e759-338a-9399-bc762704acdf | -12.1102 | -50.7857 | 2024-10-14 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 9dcbfbd0-c4b4-368b-a9f9-23c6aec52d5d | -12.1106 | -50.7643 | 2024-10-14 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 236dc04c-8fea-3424-b4dc-9517bec2add2 | -12.1115 | -50.7001 | 2024-10-14 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 9af3060c-828e-3a9d-8c61-7d2a8fbcefd6 | -12.1119 | -50.6786 | 2024-10-14 00:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 5cbeead8-6378-321b-a215-c884247df4dd | -12.3092 | -50.2473 | 2024-10-14 00:26:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5ad597d7-dd3b-373d-a679-f88c7f2b3b6e | -12.3283 | -50.2449 | 2024-10-14 00:26:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 33c7e4e8-7e82-3fc1-85e7-faefc959d21b | -12.3286 | -50.2234 | 2024-10-14 00:26:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| e9e14681-422d-358f-9588-062f32cf6a36 | -12.4981 | -63.0148 | 2024-10-14 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 54d58ac4-7105-3f04-a686-f2116af246b0 | -12.4983 | -62.9956 | 2024-10-14 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 698c8082-56a8-3fd8-95d1-73d51fcea2ae | -12.517 | -63.0137 | 2024-10-14 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7b4b2ff0-60b1-32a3-b3f5-c7111bf0d130 | -14.55 | -43.127 | 2024-10-14 00:26:27 | GOES-16 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 619affee-818d-3995-b0eb-f895404c4165 | -17.0001 | -57.4381 | 2024-10-14 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 36d71e18-fac5-39af-9090-d352a5664293 | -17.0004 | -57.4176 | 2024-10-14 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 756dabe0-f52f-3701-b078-2490e9ad50c7 | -17.0197 | -57.4358 | 2024-10-14 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| bf37ad8a-b465-35bd-8967-4f144b377977 | -17.02 | -57.4153 | 2024-10-14 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 18d9fc1c-3a7c-3b19-b368-2d9b5e837efc | -17.0626 | -56.01 | 2024-10-14 00:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 1d46db04-589c-399d-a7aa-dabf9526fd7d | -17.0823 | -56.0076 | 2024-10-14 00:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 4bf10dde-ef56-340f-9b6f-c57d4b80565b | -17.0826 | -55.9868 | 2024-10-14 00:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 40a14f33-df01-3b1e-9e15-a7e7a50dec64 | -17.1267 | -56.8693 | 2024-10-14 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| d8816de3-62d9-3e5e-80e1-b05a5f589d34 | -17.1464 | -56.8669 | 2024-10-14 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| c8c05659-3e9f-38d1-868b-548b84124dc2 | -17.1957 | -57.4562 | 2024-10-14 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 19145b9d-5989-3380-b9cc-8e19a31c437e | -17.196 | -57.4357 | 2024-10-14 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 77e86275-b299-3ee8-b537-7dacb6150430 | -17.7074 | -56.2383 | 2024-10-14 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 33be7881-385e-37ff-9c9b-f82c892645e4 | -17.6471 | -56.3084 | 2024-10-14 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 0980eef4-b68c-38f5-86f5-baa54f706873 | -17.6474 | -56.2876 | 2024-10-14 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.5 |
| b2f34657-38a7-3fef-8715-123f1dc4afe7 | -17.6668 | -56.3059 | 2024-10-14 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 5d0db347-9a71-3b8f-9bd4-ed243172d618 | -17.6876 | -56.2409 | 2024-10-14 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.1 |
| df52ba53-6fc7-372c-b568-7cacf7371f7a | -17.7264 | -56.2774 | 2024-10-14 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 0e96ae67-b5f7-3dd7-a390-088a21dab875 | -19.0724 | -48.3148 | 2024-10-14 00:26:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 08276786-2c46-33b2-8eea-65829040a589 | -22.288401 | -49.111599 | 2024-10-14 00:34:02 | METOP-C | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
