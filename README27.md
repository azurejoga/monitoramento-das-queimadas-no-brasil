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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 261e380e-5d23-31fa-bb13-d4e868e7d2ff | -7.87418 | -49.78131 | 2025-07-24 12:32:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3494ea55-dc57-32d7-9eb4-57da643264b2 | -10.88094 | -54.30746 | 2025-07-24 12:32:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0c4d5dbe-c231-3d3a-a762-1f2dc1ba37ae | -8.34083 | -44.93616 | 2025-07-24 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 66def60f-5005-3202-801b-d9fd6dd59b3b | -19.00188 | -44.99873 | 2025-07-24 12:34:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f3c9608a-af2d-3de6-9342-108d3c0b1c5a | -18.5162 | -56.40687 | 2025-07-24 12:34:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| b15a5732-690a-32da-a0e7-45c3c4cd5ea4 | -17.68447 | -46.80426 | 2025-07-24 12:34:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fce7a407-b1fe-3fdb-92e2-3661ba0c71d9 | -17.6953 | -46.80566 | 2025-07-24 12:34:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b0a9e3c3-db19-39f5-ab49-f335a7f9bf91 | -21.59428 | -57.60391 | 2025-07-24 12:34:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 355806cb-1720-3cc4-a674-bf5151f40224 | -22.79545 | -52.57224 | 2025-07-24 12:34:00 | TERRA_M-T | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 94244f1a-384e-3b6c-b530-56ee44f80ab2 | -17.686 | -47.85604 | 2025-07-24 12:34:00 | TERRA_M-T | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 50722260-be5b-320d-ba2e-af9300fdcb33 | -17.85691 | -46.32068 | 2025-07-24 12:34:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c1dfae50-a9f6-312d-b78c-fc4336f062a0 | -23.69727 | -51.80182 | 2025-07-24 12:34:00 | TERRA_M-T | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 79f4921a-5cd2-3b37-a2aa-e91c487f507b | -16.74508 | -49.18527 | 2025-07-24 12:34:00 | TERRA_M-T | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4dc6e108-a69a-3494-af6b-0a913ea63de1 | -19.56262 | -51.00082 | 2025-07-24 12:34:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 4f1ed3ba-69df-3668-944e-2083dc455d1a | -15.75982 | -47.77047 | 2025-07-24 12:34:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5fdf3049-45f9-32bd-b969-9e466a2c9b7b | -20.2985 | -54.07686 | 2025-07-24 12:34:00 | TERRA_M-T | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| feffabf4-6c67-3b53-b92c-d8c773c067f7 | -18.65987 | -55.03178 | 2025-07-24 12:34:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b9eee990-8279-3769-9667-06fd6059d879 | -21.8739 | -53.37442 | 2025-07-24 12:34:00 | TERRA_M-T | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 47025c6a-3260-3566-91d0-930f69c33ae9 | -16.94424 | -48.30813 | 2025-07-24 12:34:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 63c90c14-4498-3d45-a7bc-a2a9abd58c76 | -18.33426 | -52.47643 | 2025-07-24 12:34:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac78d24d-2b87-3204-b99c-d8d092b9186d | -16.34216 | -52.08494 | 2025-07-24 12:34:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b7299255-faad-3953-8e47-1095331e75b7 | -18.09145 | -54.28609 | 2025-07-24 12:34:00 | TERRA_M-T | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9dbb90b4-6711-39ca-b73d-fd61f09b4857 | -19.27603 | -55.16028 | 2025-07-24 12:34:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 15.8 |
| dcb3e3e1-785c-34ec-b577-57031ee0a6d4 | -15.34059 | -51.05424 | 2025-07-24 12:34:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d0b33b64-4808-32e8-bc83-d0ee57d26c9a | -21.41752 | -54.11864 | 2025-07-24 12:34:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 782c4e0d-9b4b-368b-83d6-6d3940014408 | -19.01503 | -55.76001 | 2025-07-24 12:34:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| de69361b-73af-31b3-b15e-2ec59baee0c0 | -18.15697 | -51.48049 | 2025-07-24 12:34:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5ca831de-eda3-363c-be54-f4668a721fb4 | -16.67591 | -43.23382 | 2025-07-24 12:34:00 | TERRA_M-T | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| f89b6627-c952-3245-8a53-909ac0712424 | -16.34356 | -52.07551 | 2025-07-24 12:34:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e8cb7031-f6f0-3b50-877b-5880b1fd6f56 | -22.39845 | -55.73874 | 2025-07-24 12:34:00 | TERRA_M-T | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1405e6d9-2acf-3911-8f66-f301e0a43481 | -19.27808 | -55.14756 | 2025-07-24 12:34:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 3cd1d353-e269-307f-a557-e0226cf67524 | -18.1583 | -51.47128 | 2025-07-24 12:34:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b596a232-91ca-32e6-abbb-1b4fbca837eb | -19.00181 | -45.00515 | 2025-07-24 12:34:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 97069845-b21b-3717-a761-9aa2ad3d4cb3 | -16.74644 | -49.17525 | 2025-07-24 12:34:00 | TERRA_M-T | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 61fb0d24-d72c-3061-bed3-b60b5a5782d1 | -6.9992 | -42.7836 | 2025-07-24 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 174.7 |
| fdfa1ede-6c52-3a3f-b2fe-3736e47b3b87 | -6.9804 | -42.7854 | 2025-07-24 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| e52825f6-e1de-3626-850b-f11995a70f58 | -4.0569 | -42.5118 | 2025-07-24 12:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| fef2e83f-cb17-3dfe-af95-4316d0b9b5b6 | -14.1697 | -45.3509 | 2025-07-24 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 66a3b376-957b-3e52-b029-018ee67e8f4b | -6.9804 | -42.7854 | 2025-07-24 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 152.9 |
| 62a4f30c-62fb-34c2-bb00-fa88e39ce6a9 | -14.1892 | -45.3474 | 2025-07-24 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 08f18d85-3e4b-3b02-a8b8-4e13210e7448 | -4.0382 | -42.5129 | 2025-07-24 12:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 51ef688b-913f-3a16-95f8-da2a6e60c627 | -6.9992 | -42.7836 | 2025-07-24 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 281ca632-456b-3b1f-ab05-e8699723e4a2 | -4.0569 | -42.5118 | 2025-07-24 12:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 23cc8e79-2abd-3088-9904-d7cbc87cf570 | -7.9557 | -46.2976 | 2025-07-24 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| bacbd47b-6ffa-399e-a1ef-2ac9357d8b2a | -4.0382 | -42.5129 | 2025-07-24 13:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| ddde1ded-1dd4-3f1c-a3ac-89468b16540d | -6.9992 | -42.7836 | 2025-07-24 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| 55fa1625-7350-3bc3-bbc3-d7fbb2a46281 | -6.9804 | -42.7854 | 2025-07-24 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| 761d1714-52dc-3ada-8a4b-bb8500ef68ee | -4.0569 | -42.5118 | 2025-07-24 13:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 00542c00-6d6b-3805-93f2-6715dd5c21d1 | -14.1697 | -45.3509 | 2025-07-24 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e64aba79-720f-37f2-94c5-4fe1fdd18ac8 | -6.9804 | -42.7854 | 2025-07-24 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 47acbf37-60a6-3d07-ba14-265727651494 | -6.5766 | -49.5076 | 2025-07-24 13:10:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d9e0013a-b7fe-3661-8097-53b2c81b8831 | -4.0382 | -42.5129 | 2025-07-24 13:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 703371fa-0113-33c0-8406-5365cc05a140 | -6.9992 | -42.7836 | 2025-07-24 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 993b461c-c16d-3429-894b-f19a5cabb1d0 | -11.4584 | -45.1126 | 2025-07-24 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| d2765af5-a7ad-3e47-a504-efc505b8dd14 | -4.0569 | -42.5118 | 2025-07-24 13:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 171.0 |
| 027275a6-b471-35b2-8eb7-bd62e6f6132e | -11.4584 | -45.1126 | 2025-07-24 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 1b1a6730-475e-3a88-8cf8-14cdd7535d83 | -14.1697 | -45.3509 | 2025-07-24 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 61e66ff3-b9f8-3688-be85-2f68b053da3a | -6.9992 | -42.7836 | 2025-07-24 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| c17f602c-9b08-33de-9298-a48b2815898f | -6.5766 | -49.5076 | 2025-07-24 13:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| bf3b9960-a378-3eca-a054-1c211cff58e4 | -4.0382 | -42.5129 | 2025-07-24 13:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| c61fbac2-5809-321b-94e6-a7d2fb4467d2 | -6.9804 | -42.7854 | 2025-07-24 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| c495a267-6d5b-3d7f-a630-669dd96ff1ae | -4.0569 | -42.5118 | 2025-07-24 13:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 165.3 |
| 3385f51c-d742-3e7c-9bc6-ad34cf005685 | -6.9992 | -42.7836 | 2025-07-24 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 1da48832-2348-3856-8337-50eee7199c14 | -4.0569 | -42.5118 | 2025-07-24 13:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| e2842b1a-ddd1-3661-acbc-b95f43577360 | -6.9804 | -42.7854 | 2025-07-24 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 9a87636c-1c47-3c59-ad95-857d66ff7494 | -6.5766 | -49.5076 | 2025-07-24 13:30:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| ef06315f-6f11-361d-862f-1ca0584d78e1 | -7.9557 | -46.2976 | 2025-07-24 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a413714e-4bd9-3170-993c-12b60983ce1c | -11.4584 | -45.1126 | 2025-07-24 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 0b7f4b90-f279-3fac-ac62-6696545335ec | -14.1697 | -45.3509 | 2025-07-24 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 99e6237d-2bbd-350d-94cf-8b6096f4b9ee | -12.6488 | -45.0486 | 2025-07-24 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| de0cb6a8-27cf-350d-bc88-0b17bca81e35 | -7.9557 | -46.2976 | 2025-07-24 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 7747997f-e79c-3d7e-8279-5a533753c6ad | -6.5766 | -49.5076 | 2025-07-24 13:40:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 9324c890-e064-352f-a156-9779fbe98149 | -7.9369 | -46.2994 | 2025-07-24 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 32f5293b-7c30-3b99-a231-fba2a84244f0 | -14.1697 | -45.3509 | 2025-07-24 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 88db146e-40d2-3819-a56c-9b3dfcae2ed2 | -11.4584 | -45.1126 | 2025-07-24 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 6e68e605-b122-37a1-a566-ed60a543b749 | -6.9992 | -42.7836 | 2025-07-24 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 46f4e8e4-dc04-3cc8-b094-8318edfc3749 | -12.6685 | -45.0223 | 2025-07-24 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| afd5ef50-5ac2-3567-b81b-b6e890870590 | -15.5935 | -44.5434 | 2025-07-24 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f15d4be2-1073-3f87-a1f1-8aa818489d54 | -6.5766 | -49.5076 | 2025-07-24 13:50:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 001cb948-2205-38f7-903c-b1f470c41370 | -12.6681 | -45.0455 | 2025-07-24 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| daf2b046-6760-3ff3-92ab-6d66404c44cb | -7.9557 | -46.2976 | 2025-07-24 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a6b00dcd-cc82-3757-b8ec-5aff2f5aaa4f | -14.331 | -52.0863 | 2025-07-24 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 04bcd25a-104b-3b95-aace-059526dd2d5f | -8.3299 | -44.9261 | 2025-07-24 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| cff3ef43-59cb-3717-8555-baf1d3f7c177 | -14.3306 | -52.1076 | 2025-07-24 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| a4f2f064-adbb-3a6a-b39b-744d08e00d00 | -11.4584 | -45.1126 | 2025-07-24 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 5e1773e7-4445-3509-aad4-878d7cb822ca | -12.6488 | -45.0486 | 2025-07-24 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 57f05d20-da73-394a-be35-a010a7c22b29 | -12.6681 | -45.0455 | 2025-07-24 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| dbc3478d-383c-30e6-b66e-063388746e2e | -15.5935 | -44.5434 | 2025-07-24 14:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 63c43d56-6ae7-3c18-acae-5de3ff0edd12 | -6.5766 | -49.5076 | 2025-07-24 14:00:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| d6ecfda8-69c0-3a4e-9bc5-635762a41d14 | -7.9557 | -46.2976 | 2025-07-24 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 9760616f-846e-3f10-978c-451c23141cef | -8.3488 | -44.9241 | 2025-07-24 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ede5b8ee-c360-31fa-8de3-2e3ea29fd966 | -12.6685 | -45.0223 | 2025-07-24 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 1a1e657b-51bf-342d-b31a-5e302779bb29 | -8.569 | -63.8967 | 2025-07-24 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9d9ca8c7-716e-3a90-b272-4ba7b2808e5b | -8.3299 | -44.9261 | 2025-07-24 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 56e4573f-4be9-3a26-ac77-d19a9250f120 | -12.6681 | -45.0455 | 2025-07-24 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 7ad26a21-468d-31ab-b963-fb7ddf5d2bcf | -12.6488 | -45.0486 | 2025-07-24 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 815f3306-a076-339b-b462-6562435c9e05 | -12.6685 | -45.0223 | 2025-07-24 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 6434bbf0-fcba-397f-8ca8-a55ecf225894 | -7.9557 | -46.2976 | 2025-07-24 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 68aae9ec-3228-3889-b207-d1e03ffa5b91 | -15.5935 | -44.5434 | 2025-07-24 14:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 1779a4dd-0a20-3767-accc-511b6c630c71 | -6.5766 | -49.5076 | 2025-07-24 14:10:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |


[Clique aqui para ver as próximas entradas](README28.md)
