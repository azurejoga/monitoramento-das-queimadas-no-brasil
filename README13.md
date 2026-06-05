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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92a5f374-dcfd-343a-9180-ec229ded3e08 | -21.80956 | -49.12298 | 2026-06-05 04:46:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c02c42bc-4eb0-32f3-a56b-a8c8f894d67e | -22.09196 | -47.06252 | 2026-06-05 04:46:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e814eeb-2291-3591-a64e-dc931d804c20 | -16.12886 | -58.51306 | 2026-06-05 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 18f22ed2-2955-3928-afde-465067196d44 | -19.73903 | -53.54084 | 2026-06-05 04:46:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcced275-15cc-368b-abdd-bd1ff8bd0d43 | -22.42045 | -47.14861 | 2026-06-05 04:46:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70eb223d-4c3e-3805-994d-f7ea7a5f216f | -21.81083 | -49.11359 | 2026-06-05 04:46:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e0c9c90-3c2c-3fa9-859b-415a6b1b2f49 | -16.59397 | -58.23701 | 2026-06-05 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4bd4272f-1de5-3351-898c-219ce26a5033 | -19.73508 | -53.54394 | 2026-06-05 04:46:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 305b1811-082a-315c-a516-8fd5fb1394fc | -18.93139 | -53.21912 | 2026-06-05 04:46:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0b9c158-f5ea-3da3-8abf-3a26ba84e2a9 | -18.62947 | -48.1944 | 2026-06-05 04:46:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76adfd98-3025-3a26-aad6-2e626764c7a8 | -16.5983 | -58.23791 | 2026-06-05 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c080004f-09d7-3db9-aabf-4d001ea2701d | -16.60345 | -58.23445 | 2026-06-05 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 80487718-b1f9-3ddf-8bf2-44175f675625 | -22.21671 | -56.18929 | 2026-06-05 04:46:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 881cba9f-5667-3eea-838a-2f607add5d47 | -19.71883 | -54.65308 | 2026-06-05 04:46:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 115bbe7a-fd86-3aa7-a83f-cb9bccdd428e | -22.91154 | -47.23984 | 2026-06-05 04:46:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 098563ed-9c40-37a3-9372-d08ce5d7d94a | -19.73781 | -53.54827 | 2026-06-05 04:46:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e014ba48-581e-36be-a477-4eed993aba92 | -22.21595 | -56.19357 | 2026-06-05 04:46:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3db4654-6df2-3fe4-a402-14f1ecf97d50 | -19.74176 | -53.54515 | 2026-06-05 04:46:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f06cc982-6090-3ff0-9c61-97d476559b3d | -19.16958 | -55.18278 | 2026-06-05 04:46:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 69c5f76a-5bad-31f3-98b5-c855d2392c76 | -21.80709 | -49.11304 | 2026-06-05 04:46:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bdf39b41-dc21-3043-aa6f-547d47a6aaff | -21.80647 | -49.11772 | 2026-06-05 04:46:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6aaccacf-73c6-3cbb-a4ff-3a1b1e208ccd | -18.49528 | -51.6654 | 2026-06-05 04:46:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc354066-a22b-3eff-81e3-40bd7199895e | -22.79116 | -49.33553 | 2026-06-05 04:46:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80e92f43-9cf9-37bf-9740-171d7444e9b1 | -16.59912 | -58.23355 | 2026-06-05 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 75ae991f-580f-325b-9b21-90a59d10cd44 | -23.25995 | -55.07507 | 2026-06-05 04:46:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| bcfa390d-738b-3039-8fd5-bfc85c7f5fe5 | -23.81911 | -48.71147 | 2026-06-05 04:46:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35fbf5d7-068c-3c18-b0d6-a5c8c4a6b393 | -16.84361 | -53.47251 | 2026-06-05 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 258a417a-edfd-3884-8415-19e8f7cf5aad | -18.63324 | -48.19498 | 2026-06-05 04:46:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5dc3f85c-0f32-3e99-9baf-499f3b5ce6e3 | -22.67243 | -47.40614 | 2026-06-05 04:46:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9752ba4b-8880-3f47-b3d3-bcfd6252e7b3 | -19.17007 | -55.18007 | 2026-06-05 04:46:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ad98e05e-fb0e-3c34-811b-6101b894c9dc | -23.31847 | -55.28907 | 2026-06-05 04:46:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 59bedebc-accb-3b33-ac4b-4ea1e3366429 | -19.73842 | -53.54455 | 2026-06-05 04:46:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ec8d82cf-0de0-3ed3-87ce-7eff5f26ccce | -19.7195 | -54.64917 | 2026-06-05 04:46:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 423d7895-8764-3243-8487-b023d30bcb76 | -16.84463 | -53.47141 | 2026-06-05 04:46:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77973380-6d2c-374d-ad6a-ecdc86f1e872 | -19.72292 | -54.64983 | 2026-06-05 04:46:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3ff9bd7-1a7e-338e-9988-adbff51f7828 | -19.73448 | -53.54766 | 2026-06-05 04:46:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61536e3c-3b17-3bb4-af32-99de51e16de1 | -17.77807 | -50.46987 | 2026-06-05 04:46:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f033977-96e5-39ca-8d82-b304cf3df483 | -19.74115 | -53.54888 | 2026-06-05 04:46:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 20ac95cf-296e-3b43-911f-ec50ae136d3c | -21.09539 | -49.76266 | 2026-06-05 04:46:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c0cd11b7-01a2-3f97-bf0e-514ab07863a4 | -19.16656 | -55.17939 | 2026-06-05 04:46:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 98d9b232-a652-32a1-ac4a-08ebf955d5ce | -16.95581 | -50.49054 | 2026-06-05 04:46:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7527f07-085e-38e1-abd2-2e4978221e87 | -21.8102 | -49.11828 | 2026-06-05 04:46:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 36a0892b-9785-338d-9874-683c7a41b3ec | -19.72226 | -54.65374 | 2026-06-05 04:46:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bba30284-d6a1-3d49-bb71-b7458e3e5e71 | -17.8661 | -53.26297 | 2026-06-05 04:46:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6341f61-c95c-3f21-9efd-14fd8a1a11fd | -21.19638 | -48.26925 | 2026-06-05 04:46:00 | NOAA-20 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc1eba5f-8a19-3aaa-8d3e-3d504a840e59 | -22.91206 | -47.23558 | 2026-06-05 04:46:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8a00ad77-151c-3103-b343-a5d372ee8f30 | -21.80583 | -49.12241 | 2026-06-05 04:46:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 904322ce-35ad-35f3-ab3c-0a2b01c67478 | -16.60262 | -58.23881 | 2026-06-05 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 34d29282-8f21-321d-b520-169fbf41c819 | -18.92294 | -53.22896 | 2026-06-05 04:46:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f76de21-3288-3598-a671-da7809a34ace | -17.7832 | -50.4529 | 2026-06-05 05:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 40cc7760-9654-3bda-b0d9-b0786360dd8d | -17.7827 | -50.4751 | 2026-06-05 05:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a7611448-326e-34c1-9381-bbd19cdf2e45 | -3.98823 | -47.93113 | 2026-06-05 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae8de3d4-ec73-3e2d-a5d8-3cf8918a73bf | -9.37492 | -50.54474 | 2026-06-05 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 830997e6-5e87-3443-9e78-94b32c4004b5 | -9.37361 | -50.54567 | 2026-06-05 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f803621a-808b-3fa0-86b5-dd5589dfe66a | -7.35472 | -49.82072 | 2026-06-05 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16077e79-55b0-3b3a-9b18-b415fb5a9eac | -9.08799 | -50.61433 | 2026-06-05 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee11371b-54c3-3679-a785-d74e8e6d875a | -7.86447 | -61.49135 | 2026-06-05 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0f7d7a9-7ca7-3094-920c-9c3ec0b21c05 | -7.94549 | -63.45473 | 2026-06-05 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd08629c-b42c-32d9-8115-50d4c8600b0d | -6.55114 | -55.03851 | 2026-06-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7338ee05-73a0-3dda-aab2-f0cc2e8b5042 | -9.08096 | -50.61861 | 2026-06-05 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63315e13-6d6e-34b8-ad53-9a3acac6f449 | -10.38718 | -49.44646 | 2026-06-05 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8d5016a9-6bac-31f8-b7c2-9f94f47e6e6c | -9.37556 | -50.53931 | 2026-06-05 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ab16b4d-7f87-32e9-896c-283a374a32d0 | -9.08161 | -50.61328 | 2026-06-05 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1d15e45-bc24-3da1-aaba-25c8a7b800fa | -9.37429 | -50.54025 | 2026-06-05 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 436dd2d4-e5cd-3f4c-bcc1-2cc44d51edc6 | -7.34665 | -49.83119 | 2026-06-05 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a63c562a-dd74-349e-bb21-814ff57ce697 | -7.34571 | -49.83229 | 2026-06-05 05:29:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 74674ae0-b0f2-3e00-be34-aa322a0275df | -9.09439 | -50.61512 | 2026-06-05 05:29:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 604badfa-ce71-3e69-b1e1-d60dc3525b65 | -9.89034 | -52.43916 | 2026-06-05 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83284120-f23f-303f-913e-dcd7f48dbeb3 | -21.1021 | -49.752 | 2026-06-05 05:30:00 | GOES-19 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| 210aaae6-e018-3650-a636-73e4f6892544 | -9.54188 | -64.50372 | 2026-06-05 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7515e8ea-c597-3ee0-a096-02497d6f1d1a | -12.73432 | -54.73359 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f362c366-5a8b-3308-b74c-cb1cc3378fa2 | -14.30076 | -58.64598 | 2026-06-05 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d14d41d-cf1b-3323-bde2-8ac7535880ce | -11.34254 | -53.96506 | 2026-06-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a786733-bbeb-3efb-8ec8-e9bb5621b859 | -11.87852 | -57.82493 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74adfb0b-299b-3a88-9706-df5a5f8947c9 | -13.52126 | -54.31216 | 2026-06-05 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71664a39-c00d-335e-b756-55a8b6f333d9 | -12.44052 | -58.40444 | 2026-06-05 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 61b80f5e-9be8-306b-82d4-faf324d58ca0 | -11.57027 | -54.58651 | 2026-06-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 882da510-34c8-33d8-86d5-c2c42e2f5b7b | -11.00434 | -54.31236 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeb56bc2-ba78-34fc-91bc-a63f147e93d3 | -12.72844 | -54.73898 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6e727a1-2ab8-3670-92cd-31b5f3ff8bcc | -14.30172 | -58.63881 | 2026-06-05 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9c1e0b1-9054-3b67-984c-6b70675e85a5 | -10.02791 | -59.342 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a0cc870-fac5-3335-92c4-15f514fc8cf9 | -10.03091 | -59.34819 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4b30872-9ba5-3489-b566-6d91fdb3cfc0 | -10.77513 | -54.09818 | 2026-06-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61993a71-5d23-3163-8cad-50aba7f6fd9a | -10.03524 | -59.34308 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61a0fc78-d2c9-362d-9b25-6718df7b5c51 | -14.77114 | -52.6763 | 2026-06-05 05:31:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b7c4a70-afff-3d22-aa59-a00a36a244cd | -12.44452 | -58.40497 | 2026-06-05 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 51817f89-10a1-3af7-b861-d0e35cc08366 | -11.56138 | -52.80201 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ebabf224-160a-3cab-a808-0783833e3e21 | -11.55439 | -52.80172 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1158d53c-8919-3599-8566-d3cb45a68d59 | -17.7815 | -50.47218 | 2026-06-05 05:31:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70e3efde-6bda-3708-9d2b-515a97d3d1f6 | -12.44797 | -58.47002 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 85115226-3c5b-3d10-ab98-356f8cf20ac8 | -16.19191 | -58.4654 | 2026-06-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 382db13f-4783-3f96-9884-37e0ad9d5e7f | -14.09981 | -59.38794 | 2026-06-05 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6ebdcb0-a928-3aea-bf7b-300c53c89417 | -12.43775 | -58.48567 | 2026-06-05 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12e55fe7-0c19-3859-978b-264662a625e9 | -11.5609 | -52.80611 | 2026-06-05 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4c876255-d3c0-3aad-828c-b963b2f365ab | -10.02363 | -59.34578 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 014ac116-e978-36ea-a9dc-1db187ad9edf | -12.4431 | -58.41556 | 2026-06-05 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9c039a1-806b-3c48-afa5-1fd64ce7594c | -12.2322 | -57.27457 | 2026-06-05 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7939487a-ebf5-31d7-8f95-3ac79c02f5f8 | -12.72919 | -54.73277 | 2026-06-05 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e219b94-3e67-3383-8bbf-c39c0a9550f3 | -10.02423 | -59.34279 | 2026-06-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5ecab66-9ab0-3f6c-9a32-86840c376aaa | -11.88625 | -57.82985 | 2026-06-05 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README14.md)
