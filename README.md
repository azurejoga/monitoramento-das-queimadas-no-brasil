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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba918b08-ae41-3e48-b8df-bc54cad81f43 | -3.3292 | -42.3129 | 2026-09-13 00:00:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 34b26633-b345-34df-af33-c66b8f90ae43 | -6.8632 | -55.5601 | 2026-09-13 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| fa855d25-cbe9-3104-be00-1eb7504b56bb | -10.9707 | -58.9642 | 2026-09-13 00:00:00 | GOES-19 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 08c6b084-b148-3e2e-bad5-3335300742bb | -8.5417 | -54.6985 | 2026-09-13 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 061296bb-e914-3c83-9f1a-7be1c5e14c2e | -6.6757 | -58.8847 | 2026-09-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 01966367-c5e9-35f8-937e-06e4a992b5e0 | -6.1111 | -57.6645 | 2026-09-13 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| b6f60a53-1031-30ea-b3fd-327b73986b1c | -6.2832 | -59.9202 | 2026-09-13 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 2170eba9-6ac4-3e19-88a8-511bbf9d5d38 | -16.3267 | -49.4217 | 2026-09-13 00:00:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| bd0d48e9-b70f-3327-9269-89c44ed8b332 | -6.2243 | -51.6949 | 2026-09-13 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ae9237df-e222-3e4a-a1de-79271d76efb4 | -3.728 | -61.7555 | 2026-09-13 00:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| a3195c14-5001-3872-ac4f-c6b2320fe4a6 | -2.9578 | -50.4198 | 2026-09-13 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3cd95673-b74a-3d75-84a8-7b6e20af29f1 | -6.6573 | -58.8855 | 2026-09-13 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0be111fb-1055-3594-948d-db50f81c259d | -2.6785 | -57.531 | 2026-09-13 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 239.5 |
| aae07eda-42fa-35c4-a5d1-5dba12b1d338 | -2.9723 | -57.214 | 2026-09-13 00:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3ca2c803-3c3d-3d40-b5cb-5f0692e8534a | -2.6784 | -57.5504 | 2026-09-13 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 17684a92-8755-3792-8a6f-ee52915235cb | -6.8445 | -55.581 | 2026-09-13 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| fa5910f2-7485-373e-8ac7-0d88c92b8d2f | -2.6785 | -57.5115 | 2026-09-13 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 0450db02-382e-320f-af2a-25f0c327d46d | -8.5415 | -54.7187 | 2026-09-13 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 85d2abcc-b68b-399d-9aa6-cd7a01f48ac9 | -10.9519 | -58.9655 | 2026-09-13 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| e9fbf28d-aa5d-3d6b-8191-5d996a4c3746 | -6.0731 | -57.861 | 2026-09-13 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a4ac345b-c3cd-3d25-b37f-f6e06242a287 | -6.6021 | -58.849 | 2026-09-13 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ed4ebd48-6dac-38bc-a2e2-b26eb293945f | -5.8206 | -53.8052 | 2026-09-13 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0a604bd3-b007-3413-8a9d-94e7d94a1057 | -9.3948 | -50.1334 | 2026-09-13 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8968106e-094d-3320-82da-4bf974fd9248 | -10.6824 | -54.1884 | 2026-09-13 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| b4f5b997-6b10-3bbc-860e-cb8d57db855c | -2.6602 | -57.5313 | 2026-09-13 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| ad72aeb4-70f4-3e94-8ff2-559cc688d530 | -12.6821 | -54.7174 | 2026-09-13 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 8aed8516-ea9d-3df2-9e19-6f8d8a97b75f | -6.2831 | -59.9394 | 2026-09-13 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 27a0174c-c39e-3212-8603-474de4455de0 | -2.9579 | -50.3988 | 2026-09-13 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 168d841f-7b4d-35df-8f59-bf0cfe9e4edf | -6.863 | -55.5801 | 2026-09-13 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 9547fe4e-236e-39c6-94d7-9dcb8db55a43 | -16.9887 | -49.7291 | 2026-09-13 00:00:00 | GOES-19 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 2f5488ec-7f82-3f4e-ba9c-079291ec7fa1 | -9.3765 | -50.0925 | 2026-09-13 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 48d9305b-2890-314b-ac1f-545aba0ae63f | -10.6827 | -54.1679 | 2026-09-13 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 343.4 |
| a66a643a-43e3-3ab5-bbfa-af421bcaf042 | -9.3763 | -50.1139 | 2026-09-13 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 720b9b05-c6a0-3eec-bea6-776167e093fb | -12.6818 | -54.7379 | 2026-09-13 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 6ae0853b-2020-3b33-9960-9ec2c3f24ca2 | -12.8543 | -44.386 | 2026-09-13 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 8f3f20ee-36b8-33ed-a56c-bb25c687f2d9 | -10.7015 | -54.1663 | 2026-09-13 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.5 |
| dae398b3-29bf-3135-b339-e4572a509a23 | -10.6829 | -54.1475 | 2026-09-13 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 41576e8f-675b-3a1b-8fef-bd9e6395953a | -7.0166 | -44.6184 | 2026-09-13 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| fd4f489a-1b5e-356d-a668-0f7e09834b26 | -9.4137 | -50.1317 | 2026-09-13 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 01c10662-3897-3123-b8db-09f67cc8e0c4 | -3.3293 | -42.2893 | 2026-09-13 00:00:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 7d1d0b78-20e0-3c9d-9851-1de6c8147bc9 | -17.33765 | -42.52571 | 2026-09-13 00:01:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e4ba2c72-0b94-39ed-912c-500d44a62752 | -18.49183 | -42.80634 | 2026-09-13 00:01:00 | TERRA_M-M | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 4118e362-f9b1-3d2b-9bee-c454d78d4881 | -18.61891 | -46.32103 | 2026-09-13 00:01:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b006d92-3e34-3e6d-844b-7fa2872ff45f | -17.52231 | -40.192 | 2026-09-13 00:01:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 34.2 |
| 1db9ac1a-6657-3b55-aa6f-50d9199ef493 | -20.02646 | -44.07619 | 2026-09-13 00:01:00 | TERRA_M-M | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 432e616c-e0ec-374a-a2d2-2522ca154a3f | -20.33402 | -47.58195 | 2026-09-13 00:01:00 | TERRA_M-M | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 36679621-9838-38b2-9763-8f38225a1344 | -17.33958 | -42.53093 | 2026-09-13 00:01:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 0da862ab-3230-3816-8fc1-305e15a268cf | -16.67385 | -41.84567 | 2026-09-13 00:01:00 | TERRA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.2 |
| 0871fa22-8fae-32bd-af3c-a7f277eaeac0 | -18.64758 | -41.98966 | 2026-09-13 00:01:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| e9a5c44a-5b07-3f31-a255-378f8ffe5a95 | -17.51108 | -40.17524 | 2026-09-13 00:01:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 3d3cb189-7dd1-33b0-9f83-4d62ff3ec509 | -16.6768 | -41.86353 | 2026-09-13 00:01:00 | TERRA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 8b8cc1cd-ba63-33cd-8f9c-8b798801c1db | -16.66869 | -41.8597 | 2026-09-13 00:01:00 | TERRA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 89c8efb6-c992-3cf5-b674-d20309326c91 | -20.03621 | -44.07467 | 2026-09-13 00:01:00 | TERRA_M-M | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ba28d87c-4151-310f-aad0-30b683ec9a3f | -17.34898 | -42.52364 | 2026-09-13 00:01:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 79524b45-b884-3cbd-9f69-fe484bf7b090 | -18.60841 | -48.65744 | 2026-09-13 00:01:00 | TERRA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| be44d38f-d90d-341f-86c2-d2192bc89684 | -20.04112 | -45.19414 | 2026-09-13 00:01:00 | TERRA_M-M | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c596b514-0085-3b0f-8bdb-e2f2041c3f62 | -19.36758 | -41.67943 | 2026-09-13 00:01:00 | TERRA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 98e44d71-5a3e-364c-9c6a-d0c36d15ec59 | -16.66558 | -41.84178 | 2026-09-13 00:01:00 | TERRA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 6ca4d733-df69-3e72-a09f-22c0de7590db | -18.64696 | -42.00049 | 2026-09-13 00:01:00 | TERRA_M-M | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| bf2d6e6f-27e5-37ed-ae43-3281170c0bf6 | -18.496 | -42.81484 | 2026-09-13 00:01:00 | TERRA_M-M | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 98226813-1d4a-3e4a-99ae-981e50ffa8b4 | -18.49418 | -42.82102 | 2026-09-13 00:01:00 | TERRA_M-M | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 04950067-b3fd-39e9-b311-fbd32141fc88 | -10.69134 | -54.15516 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 182.1 |
| 7e1c54fc-d83b-3a1e-bbbb-1dad3ce90368 | -10.68155 | -54.16226 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 210.3 |
| 316de46d-f57c-3064-9ff1-05df7ec3b7d8 | -13.10434 | -44.62701 | 2026-09-13 00:03:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4ad88bed-7b30-344d-b3d6-188058bbc44d | -12.66641 | -54.66919 | 2026-09-13 00:03:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 68a92b00-a4a7-3dfc-a0a5-d5415d14cc95 | -11.38702 | -43.96801 | 2026-09-13 00:03:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e46066f0-d713-346b-8dc5-ba84062bd5d1 | -10.95571 | -58.94825 | 2026-09-13 00:03:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ea8682b1-6014-36bd-b00a-14637ce17e48 | -9.63125 | -49.02266 | 2026-09-13 00:03:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e68889c4-976f-3efb-80b7-eb763161bbc2 | -9.37315 | -50.09019 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 6b6218d2-22d9-389d-b792-575c8c0a6232 | -9.89104 | -47.58506 | 2026-09-13 00:03:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 05d001cf-370e-35e5-b9a0-c3cc0d0bb59d | -9.40703 | -50.1403 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 5f556c73-97be-3f2e-aadf-df5483f54842 | -10.52622 | -47.90215 | 2026-09-13 00:03:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 90cba874-28be-3af3-8197-0e2915869ded | -10.94215 | -47.91088 | 2026-09-13 00:03:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a9d6ffdb-cea2-3a4f-a6d7-36b8611cc2da | -11.51581 | -54.63191 | 2026-09-13 00:03:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 316b0d20-ac70-3879-ae05-5accaf0d015a | -13.76117 | -42.61219 | 2026-09-13 00:03:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 41.4 |
| 7ce37180-4e6f-302b-8fe8-da27df1380fb | -10.21015 | -45.25565 | 2026-09-13 00:03:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 251a69ab-07e5-352f-8909-48d9908678c5 | -11.71585 | -46.73606 | 2026-09-13 00:03:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fa26b37a-9559-3abb-9d4d-fe2c37a2f4d6 | -16.31887 | -49.43279 | 2026-09-13 00:03:00 | TERRA_M-M | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9ce8e299-07a4-328c-9266-9b37c8e2582c | -13.31812 | -51.72999 | 2026-09-13 00:03:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 388ea41a-1ca0-3ba6-a738-dd6ad9a5cb2e | -10.6439 | -46.11354 | 2026-09-13 00:03:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 114debc5-2013-3bbe-8fc4-68491270cbf6 | -10.67999 | -54.15668 | 2026-09-13 00:03:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| abe44480-de74-3621-9ebd-9e61cbf48672 | -12.49432 | -47.152 | 2026-09-13 00:03:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 928e3523-d6fb-38d3-9c4f-e4ce12a796d0 | -11.33638 | -48.54301 | 2026-09-13 00:03:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 921f6475-45a1-32f6-920a-f68dde7adafc | -11.34619 | -46.79691 | 2026-09-13 00:03:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5bf5b27a-14b4-3ede-85a0-13e1f01bbf68 | -9.39817 | -50.14155 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c876a121-b327-3a93-8ae0-d3a8c3c25f58 | -16.66351 | -48.21997 | 2026-09-13 00:03:00 | TERRA_M-M | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f3117f7e-7aa7-3507-8ddd-5dc653a31324 | -9.36552 | -50.10041 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 417b01d2-4448-356b-b2a0-7c863d4573b5 | -9.39695 | -50.13257 | 2026-09-13 00:03:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 1da0bffd-d235-3baf-8f57-098877234252 | -13.45735 | -48.48497 | 2026-09-13 00:03:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3ea8112c-8945-3a4f-82e2-f0436c71c389 | -10.41929 | -54.35562 | 2026-09-13 00:03:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ccc7bd6a-c884-3479-8827-b3daebf032ea | -14.03726 | -48.01479 | 2026-09-13 00:03:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 25b26160-b28b-330e-9c2b-1837265fb3a3 | -15.25806 | -42.79934 | 2026-09-13 00:03:00 | TERRA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7ea4ec1e-5ec5-37a2-a1f5-5a2f61ee1e36 | -10.14013 | -49.15751 | 2026-09-13 00:03:00 | TERRA_M-M | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4584cd60-4985-3815-9717-0c78c7ad352f | -13.50399 | -47.18381 | 2026-09-13 00:03:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cd5914cf-8d81-36e8-8bea-fbd2dd2bc754 | -11.29644 | -44.1974 | 2026-09-13 00:03:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c2f3ffd2-048f-3a0e-b745-e3a700c3e71f | -11.79378 | -47.8638 | 2026-09-13 00:03:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 159147c9-248a-3733-862f-a378a0980fba | -15.57161 | -53.78432 | 2026-09-13 00:03:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 338ea691-3ce1-3e72-8969-7b3851b3f7f8 | -9.59811 | -46.72673 | 2026-09-13 00:03:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a075b95a-eaa4-3813-ab53-e9822c84e632 | -9.89241 | -47.5947 | 2026-09-13 00:03:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| f08ae285-04a9-313e-a675-36693f9263bd | -13.45104 | -48.50424 | 2026-09-13 00:03:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README2.md)
