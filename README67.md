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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ccf3a62-6a5e-30f4-aa67-b26a050ce8d5 | -10.9204 | -45.3253 | 2026-09-02 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 246.0 |
| f9db2859-045a-38ff-b355-4f6cf4085391 | -10.92 | -45.3483 | 2026-09-02 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| fa59d388-0168-35ee-ad57-fc02c47fb0e8 | -8.4671 | -54.7035 | 2026-09-02 07:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| c2287867-d461-3598-8fd5-8190476663d9 | -10.9208 | -45.3024 | 2026-09-02 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 83e9c1dd-71a3-38f5-a57d-bae01ce41ccd | -10.9013 | -45.3279 | 2026-09-02 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 991d07a2-4097-361a-82b4-3bc5a738b8b9 | -10.9395 | -45.3227 | 2026-09-02 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2bb47ee0-a239-331e-b73e-2a44d265bd47 | -10.9204 | -45.3253 | 2026-09-02 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 264.9 |
| c1f53166-3cc0-32ab-af91-8b4f3f1b7469 | -10.9009 | -45.3509 | 2026-09-02 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 13f42f13-d7d9-3a8c-b2d4-9bbf054c29b6 | -10.9208 | -45.3024 | 2026-09-02 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| a6c64cfc-6c34-3117-88d5-2026b38abec1 | -8.4671 | -54.7035 | 2026-09-02 07:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| d8ee9fa7-338e-3b72-9773-d4b306047a5f | -10.92 | -45.3483 | 2026-09-02 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| baaebe7c-b5bc-3390-8cfc-69a4fd0e4533 | -6.6948 | -58.7678 | 2026-09-02 07:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 501a461b-d918-33d0-acc5-197b0b0a329c | -8.4669 | -54.7237 | 2026-09-02 07:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 76bb5924-e316-3fd1-9275-34b4b65c38a0 | -8.4485 | -54.7048 | 2026-09-02 07:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9f3a162a-125e-311f-8d91-daabf91b7363 | -10.9395 | -45.3227 | 2026-09-02 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| c20721f8-f16e-372b-b8cb-c85b953e3ef5 | -10.92 | -45.3483 | 2026-09-02 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 51b9d435-588c-32da-b2e6-d99791c4ba20 | -15.3659 | -47.6838 | 2026-09-02 08:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| d6f48892-7b05-3505-b19d-6c4f343cbee0 | -15.3855 | -47.6804 | 2026-09-02 08:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| a12f359d-602d-3fa8-a926-2a30c8d82988 | -8.4671 | -54.7035 | 2026-09-02 08:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 1b31f44e-d414-34f1-95dc-053836263029 | -10.9013 | -45.3279 | 2026-09-02 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| bcf37c05-9c2d-3f67-bc32-f1e7b7a35c54 | -10.9208 | -45.3024 | 2026-09-02 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 25dfc51e-0af4-3cc0-89b7-5488dc3375f8 | -10.9204 | -45.3253 | 2026-09-02 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 544.5 |
| 85d594fc-1275-3473-a308-3dd84bfa2e19 | -9.43887 | -67.44093 | 2026-09-02 08:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1eed2f22-03ed-3052-9308-cfc184b1d19b | -7.69367 | -67.12247 | 2026-09-02 08:07:00 | AQUA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6b6ef467-93ab-3796-8229-4dff0bc988c1 | -9.00755 | -65.41184 | 2026-09-02 08:07:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4f9b8f6e-160b-3627-a207-455d41687f98 | -8.90346 | -62.35351 | 2026-09-02 08:07:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ef5ba36c-4d81-3059-8d94-be52a941c570 | -9.44158 | -67.42269 | 2026-09-02 08:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 403679ef-79bc-3346-b6eb-346421ed1c58 | -10.19004 | -69.02505 | 2026-09-02 08:07:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a84ffe3-dc4b-3d0e-90b3-8405dba630c7 | -7.68478 | -67.12115 | 2026-09-02 08:07:00 | AQUA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| adfbd312-2d66-3c89-93a3-12e5af76800e | -8.76416 | -62.58137 | 2026-09-02 08:07:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a73b5379-dbcc-35aa-afca-07efc539abff | -9.43752 | -67.45004 | 2026-09-02 08:07:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1084ab84-4599-34fe-9fc7-6e894baa681f | -9.03104 | -65.39915 | 2026-09-02 08:07:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 11af81c9-38d8-3536-b754-1cde6d99a2a6 | -9.01347 | -65.45343 | 2026-09-02 08:07:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4f4d8654-11c6-3482-b2ea-e1496acd2673 | -9.0849 | -65.37243 | 2026-09-02 08:07:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 95fed8ac-e07b-3ba8-a386-b7dc56239e85 | -10.92 | -45.3483 | 2026-09-02 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| ad8e00c2-c6e8-30ca-b709-8e598b0aea05 | -10.9204 | -45.3253 | 2026-09-02 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 8a8fa173-457a-31cd-b871-5a80704adc57 | -10.9013 | -45.3279 | 2026-09-02 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| e2ce2af5-fdb3-3712-b251-e273c9374688 | -8.4671 | -54.7035 | 2026-09-02 08:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 6e8032ed-7019-3466-affe-118e024fb8e9 | -10.9 | -45.3 | 2026-09-02 08:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec93bf62-a5b3-3db4-a921-c1528dfc71c0 | -10.9 | -45.35 | 2026-09-02 08:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40b62fc1-1c2e-30e0-965e-a0e119b8f61b | -10.93 | -45.35 | 2026-09-02 08:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e69f210-7998-3340-83c0-42d5d736f964 | -10.9395 | -45.3227 | 2026-09-02 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 3830bf3c-5019-3fe7-a377-d87d7d57434c | -8.4671 | -54.7035 | 2026-09-02 08:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 97d420fd-1a7a-3d3b-a445-289709129d42 | -10.9204 | -45.3253 | 2026-09-02 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.7 |
| c4188b8b-ac82-3f0c-8d1d-5d273ccd67e1 | -10.92 | -45.3483 | 2026-09-02 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 416b2075-b960-37b3-957f-e85342e3edd4 | -8.4669 | -54.7237 | 2026-09-02 08:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 567ec921-e015-3021-802a-a204b3c612d4 | -10.9013 | -45.3279 | 2026-09-02 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 81afe0e0-b715-3f86-84b1-986d0da23109 | -8.4669 | -54.7237 | 2026-09-02 08:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c2dfdcb9-788d-352f-ae18-61ed8232c1e6 | -8.4671 | -54.7035 | 2026-09-02 08:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ad05fcc0-8b63-3495-9b8d-b97b01e7fd47 | -12.865 | -45.8213 | 2026-09-02 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 0afb8037-6e69-3a5b-acef-40aeef60dc71 | -10.9752 | -50.4864 | 2026-09-02 08:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8ee87c6d-0679-3fb5-a7c6-85314ae19959 | -12.8843 | -45.8183 | 2026-09-02 08:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 635a2c75-95f4-3749-bf76-897b346582dd | -8.4856 | -54.7225 | 2026-09-02 08:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 88d38b5a-e890-33fb-997f-373ecdb1ca40 | -8.4485 | -54.7048 | 2026-09-02 08:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 5c253fff-fbec-3106-a8be-e2979b9982db | -8.4669 | -54.7237 | 2026-09-02 08:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| fccc50cb-2d63-3ff6-a913-68152962f005 | -8.4671 | -54.7035 | 2026-09-02 08:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 3e097d0e-14ff-3f73-ae01-7c96de34ccab | -8.4671 | -54.7035 | 2026-09-02 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| b98764ea-ba9c-3d7b-9409-ca79bf800b24 | -8.4856 | -54.7225 | 2026-09-02 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4c8a3ec4-cfc5-321b-a109-edc0d737a243 | -8.4858 | -54.7023 | 2026-09-02 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 8ce3a373-dc40-3e3d-9c7d-3393f86ed515 | -8.4669 | -54.7237 | 2026-09-02 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 6b9c1c39-9ad2-33c2-88dd-6c5b21b7b670 | -8.4858 | -54.7023 | 2026-09-02 09:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 07ba6a04-593b-3da2-b91b-6867284ec4c0 | -8.4669 | -54.7237 | 2026-09-02 09:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 44dff4a9-fbfe-35b0-b608-3aa5753e8152 | -8.4856 | -54.7225 | 2026-09-02 09:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 53474469-91c3-3b73-8140-66b009fedaca | -8.4671 | -54.7035 | 2026-09-02 09:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 12ba5be3-bc3a-350d-a89d-974f7fdd9985 | -10.9204 | -45.3253 | 2026-09-02 09:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 35bc8ae3-14ec-3623-b40f-1417c47629a3 | -10.9204 | -45.3253 | 2026-09-02 09:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 6e74c9d1-c64c-3c64-b052-546ed1bed0be | -11.8248 | -46.0448 | 2026-09-02 09:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 32651b84-5b78-3cc4-a2ef-63f5d1c36173 | -8.4669 | -54.7237 | 2026-09-02 09:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| c22fc24b-ea37-3ce0-ab19-acfb88201b1e | -11.8435 | -46.0649 | 2026-09-02 09:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| f1538b38-b727-38c0-a8c1-37a5b3ef5a78 | -8.4671 | -54.7035 | 2026-09-02 09:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 150.6 |
| b01ca9e3-ba73-3d56-a294-cc1873999597 | -11.8244 | -46.0676 | 2026-09-02 09:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 68a91c11-1d30-38f9-9eae-7d9286c7ab3a | -8.4671 | -54.7035 | 2026-09-02 10:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 14ce1158-ab72-36bc-b263-d626bcc10129 | -11.8244 | -46.0676 | 2026-09-02 10:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 442.2 |
| 156750ec-0806-387a-96ed-7e78efccb0cc | -11.8439 | -46.0421 | 2026-09-02 10:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 204c8646-b57f-339b-884c-548a4f6be318 | -11.8248 | -46.0448 | 2026-09-02 10:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 242.7 |
| 1619ae6b-e64a-355d-8477-f8cff7f1d320 | -11.8435 | -46.0649 | 2026-09-02 10:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 317.9 |
| 77dc4510-484e-3032-9746-a7ca31ab96cd | -8.4669 | -54.7237 | 2026-09-02 10:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 9ea3d211-2bad-3ece-a5a7-0b843b122a6f | -11.8439 | -46.0421 | 2026-09-02 10:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3dad26b3-7437-3097-b730-47f8a1908d6e | -11.8248 | -46.0448 | 2026-09-02 10:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| db8cd82a-f7a2-34aa-b63e-6788e36b3a53 | -11.8435 | -46.0649 | 2026-09-02 10:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 222.3 |
| bd68a48e-94f8-3494-b0e8-462116d1e232 | -11.8244 | -46.0676 | 2026-09-02 10:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 3827b461-eae4-33b0-b43f-18060a4d9c38 | -11.84 | -46.07 | 2026-09-02 10:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f7ddf130-7138-386c-bbe6-7a17e1ce173a | -11.8244 | -46.0676 | 2026-09-02 10:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| e33afdce-2f3c-37fc-84b6-7f182c4d3a43 | -11.8435 | -46.0649 | 2026-09-02 10:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 6adbb2b6-5e9a-302e-b531-03b956b869c2 | -11.8439 | -46.0421 | 2026-09-02 10:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| aad28807-35d7-3b9b-b2c6-d24bf6386565 | -11.8435 | -46.0649 | 2026-09-02 10:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 475e01d5-b456-3dd0-94ba-6a7223fcc4e4 | -11.8248 | -46.0448 | 2026-09-02 10:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d673bf53-0167-3809-b443-5cbc1edbe16b | -11.8244 | -46.0676 | 2026-09-02 10:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 317161c0-95b7-3700-ba98-1438d1b22ebc | -11.677 | -50.4939 | 2026-09-02 10:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 469d00f5-61aa-3809-8854-d821439d3bda | -11.8627 | -46.0622 | 2026-09-02 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 4f81dbaa-d91f-3775-a09c-081dd732cf31 | -11.677 | -50.4939 | 2026-09-02 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 46214d04-de54-348e-a7b5-89ebd9e4e4e6 | -11.8248 | -46.0448 | 2026-09-02 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 33128b01-610f-3aa0-92cb-ddb9655948f3 | -12.865 | -45.8213 | 2026-09-02 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 50f1f063-c7a2-3969-8d21-cfe417893e33 | -11.8435 | -46.0649 | 2026-09-02 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 678.1 |
| 26cb14b0-f8c4-3953-aef9-5f01a4b19e29 | -11.8244 | -46.0676 | 2026-09-02 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 161.0 |
| b2b835e2-dc57-3389-9ed9-732e81707f78 | -11.8439 | -46.0421 | 2026-09-02 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 4ea6b63e-e7e8-3cb3-888c-8e844baf7d00 | -11.8431 | -46.0877 | 2026-09-02 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 363.6 |
| 55808cdd-eeaa-30c2-b496-a456a45a8328 | -12.8843 | -45.8183 | 2026-09-02 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 43017ee3-2f28-3d90-9d3d-56338be89ae6 | -11.677 | -50.4939 | 2026-09-02 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 176.5 |
| ecef9aec-1411-3e55-857c-7c23d8848dd6 | -11.658 | -50.496 | 2026-09-02 10:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |


[Clique aqui para ver as próximas entradas](README68.md)
