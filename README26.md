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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 944223c4-e9e1-32bf-8f36-d37aaa316f4e | -23.8521 | -50.00719 | 2024-12-17 04:50:00 | NPP-375D | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 067fe704-2c7e-343c-b63e-df1c1beab5fe | -24.24392 | -50.73968 | 2024-12-17 04:50:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 85ab4bd4-515d-30ac-a5dd-707192b7332c | -21.32691 | -56.11513 | 2024-12-17 04:50:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9969030-01a9-3235-903e-1e4ac5005014 | -22.08715 | -48.94599 | 2024-12-17 04:50:00 | NPP-375D | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a2035d4-82e7-3a44-ba1a-b7c7dd95645d | -23.4528 | -46.06555 | 2024-12-17 04:50:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 043faba4-7ce2-3a4a-81d4-d6bff435f22f | -22.53839 | -48.81278 | 2024-12-17 04:50:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62831f7f-3868-353a-a395-7253ed610fd1 | -21.68091 | -56.0058 | 2024-12-17 04:50:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 546880dd-63d4-3503-9c88-bda553b14dc6 | -22.67885 | -42.85272 | 2024-12-17 04:50:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4ec36a00-d032-387b-a8e7-bbd92a9e7582 | -22.54004 | -48.81075 | 2024-12-17 04:50:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a77a3780-f3d2-3cb7-bff1-ce051863ef5a | -21.3303 | -56.11579 | 2024-12-17 04:50:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7bf37df-52c8-3988-8b77-eeb6b87e7040 | -19.02168 | -57.622 | 2024-12-17 04:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 56d944ab-5682-3b02-a77d-41e7d02b105c | -25.56866 | -49.36528 | 2024-12-17 04:50:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c05af787-5b28-386d-96d8-cf0af1cf6c98 | -20.9183 | -56.54857 | 2024-12-17 04:50:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68a117f3-a9f4-346f-8616-d13bf735cc97 | -20.99712 | -51.79387 | 2024-12-17 04:50:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b6f36c07-5161-35e5-8794-59ab9800ee3b | -22.08752 | -48.94418 | 2024-12-17 04:50:00 | NPP-375D | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b1b6fc4-04bf-333e-83d6-961d016d3c58 | -6.9346 | -43.5168 | 2024-12-17 05:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 07193019-15b6-31b2-969a-fe389d84c5bb | -3.2968 | -53.3749 | 2024-12-17 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0652ee74-5d95-3883-b4c8-547b6f92f3f1 | 4.4435 | -60.9846 | 2024-12-17 05:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 005e2ec4-4dd5-3266-9b74-3e6645784557 | -6.9349 | -43.4934 | 2024-12-17 05:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 4a64bb93-5f22-3692-99cd-1eca3d19a3bc | -5.0936 | -43.9176 | 2024-12-17 05:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a535c070-ccbd-3bfa-aa6a-02a858dc50ce | -5.0938 | -43.8945 | 2024-12-17 05:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 5f7abccd-f304-30c2-b2f3-827134a09d30 | 4.44153 | -60.97401 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68b5d904-4f76-3a94-9035-a3cf74b9c5ce | 3.3217 | -60.63115 | 2024-12-17 05:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4d5adbd-97c6-3de1-a112-8e5f1662183d | -0.16687 | -51.35534 | 2024-12-17 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c75f1ec8-c952-3f01-b9be-3fe161519bc0 | -1.72798 | -53.31629 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 422b1a5b-fbfb-3271-9531-f44b61beee64 | -1.22144 | -50.69523 | 2024-12-17 05:05:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af35580e-d318-3843-82d1-4eb2633d6bb7 | -1.72504 | -53.31172 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22827d8a-e9d3-3ca2-adc9-225fa19a9896 | -1.2729 | -53.0361 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89edfab5-dce3-386e-bbba-50bb847ce9ea | -2.05335 | -46.66273 | 2024-12-17 05:05:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3efe776e-63cf-39b4-b622-f82ce8fd85ac | 4.45772 | -60.96332 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95fa8f32-b91c-3dc6-bb35-36cc33755d40 | -1.37355 | -53.48112 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c0bb742-e856-371a-a767-b19115322519 | 4.4434 | -60.95686 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6dd330cf-9a39-3c3f-95f7-0c5cdc5860af | -2.76721 | -47.39338 | 2024-12-17 05:05:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41f6d07a-8c61-3a89-b503-866d96bd0c01 | -1.37476 | -53.47332 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b6691c5-2a27-3699-80d1-ab1616fb7770 | 4.44769 | -60.98532 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8c1accf9-1777-3189-a612-3334c62d1517 | -1.28564 | -53.18806 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b17757f-3771-3414-997e-1474bc153692 | 4.44214 | -60.97806 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0a35856-1666-37e5-9146-22134f422501 | 4.4366 | -60.9708 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c68ff69-5239-3653-aed3-98de598077f3 | -1.285 | -53.19211 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60a025cc-097f-3919-b636-cd8ff9edff5b | -2.03218 | -48.57484 | 2024-12-17 05:05:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7fe243a-14ff-3e34-9116-4376af8a9e99 | -1.28079 | -53.47173 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bddf2320-9aab-3634-bcc3-3aacc92f62a0 | -1.27727 | -53.47121 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d15b04-2892-3ccc-8677-745d87eb42d4 | 4.45141 | -60.98044 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a30dc882-2b23-3e01-99ef-2790080f629c | -0.75267 | -47.75748 | 2024-12-17 05:05:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 121443a2-f59a-30bb-94ca-ae4377b5c592 | -1.63601 | -45.85695 | 2024-12-17 05:05:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b85f4dbf-3e17-3215-aa83-7e190981fe28 | 4.45578 | -60.97993 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 91dd5850-debd-3aef-b706-13de00606bc2 | -1.37124 | -53.47277 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1b2b27c-672c-373c-b3cd-706154e39a7c | -1.1806 | -52.55168 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 602db619-71ec-352d-94ad-57361367cbf0 | -1.72148 | -53.31117 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3587da4f-d9df-3664-897e-c665917d61cd | -1.78694 | -52.02589 | 2024-12-17 05:05:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 263d1e50-6f5e-339e-8577-17c69860b263 | 4.43965 | -60.96152 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 88755043-2237-3778-9bcf-fb100ac0936a | 3.32229 | -60.63496 | 2024-12-17 05:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0da4657e-9133-33d1-98dd-2cc83b2f74c0 | -1.29608 | -52.84021 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fe1cc6d-fce3-3571-95b0-2b7a21b778ba | 4.4378 | -60.9788 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96f55594-4b52-3b53-bcd5-55a3341a45c5 | 2.61207 | -61.31044 | 2024-12-17 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b68d194c-ff08-3073-9a7b-343408401e3c | -2.58749 | -47.48431 | 2024-12-17 05:05:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ce0545a-a53a-3919-a32d-b2df3324af14 | -1.28207 | -53.18752 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bcd896a-8e05-3c98-affe-f4b43dd0a68f | 4.45644 | -60.98425 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ef6f27f1-a833-3910-b1cd-9e42c59258b5 | -2.14379 | -48.03699 | 2024-12-17 05:05:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd6dbaa4-72c2-3ce9-965e-7f3031bf1c39 | -1.62961 | -45.8601 | 2024-12-17 05:05:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e76d9f58-53c2-3474-b7ce-c6ee9e828ac7 | -2.0528 | -46.66633 | 2024-12-17 05:05:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daecce9d-35fa-30a6-84cf-dfd7612fa254 | 4.4508 | -60.97641 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3091f397-2f22-308f-bf4a-b182d16bf895 | -1.46053 | -53.47844 | 2024-12-17 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40dd6dca-3f00-3744-8935-a7531f54322d | 3.98637 | -59.97507 | 2024-12-17 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 727d7f89-6c3c-39a5-8ecd-dbda2387e891 | 4.46037 | -60.97429 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22d8b405-6e4a-3823-8c50-f514658e5e7b | -1.54469 | -53.73263 | 2024-12-17 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 029bd8b4-33ae-34d7-9e14-f73b189a4f4a | -2.0539 | -46.65914 | 2024-12-17 05:05:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| debf0e9e-5621-3355-b9b3-46ce2f8ad8e6 | -1.55062 | -53.43465 | 2024-12-17 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17baca4d-96bc-3ccc-b7a8-13b858e7ce37 | -0.16654 | -51.35273 | 2024-12-17 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 704534ee-90cc-39a4-a871-f05ad59d7af8 | -1.27353 | -53.03203 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fef88b89-1ffc-3b9d-babf-498d60b466e2 | -1.3979 | -52.68967 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7da6f2ad-6898-373b-97bd-bb61e59f9c3d | 4.43901 | -60.98685 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c3d65e4e-b1fb-3379-b681-fd9bdc30410f | 4.45202 | -60.98452 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9053908c-7381-35ec-9918-59b74c176b6d | -1.27417 | -53.02793 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dd9b857-91fe-3360-8595-9de3eb0b88b4 | -1.37064 | -53.47667 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 767f9170-e24a-3fcb-8657-35c01780e66e | -1.54709 | -53.43409 | 2024-12-17 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cca0bb4b-83b4-30ab-9794-5a850fea59ef | 3.98239 | -59.97606 | 2024-12-17 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2630a8c2-9d0b-3ced-afec-b2d39bec2813 | -1.30037 | -52.83653 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df08792a-75f6-36c3-9b09-c41aec54835d | -1.37707 | -53.48167 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b37cf55-aab4-3c75-ad77-38ebd91e446b | 4.44028 | -60.96571 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b80110c3-e0d6-3c74-a550-23e0e348db4d | -1.53952 | -53.73284 | 2024-12-17 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9092cfc-b988-386c-8be4-ae328b6708a7 | -2.51278 | -49.05688 | 2024-12-17 05:05:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32322072-3af4-3bdd-9057-6b84e59ec673 | -2.57113 | -45.95721 | 2024-12-17 05:05:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d97e664-bb14-39a7-a8dd-08a791c681c4 | -1.72442 | -53.31574 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6559a528-30e6-3a43-b8d4-95afecdc2d03 | -1.89447 | -46.81664 | 2024-12-17 05:05:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 256004a7-1e61-39c9-b89c-c1e0ef527c92 | -1.18007 | -52.54911 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08ecb164-3dbf-364c-a67f-9053861df13d | 4.45962 | -60.97584 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ff7a737-8350-3532-937b-8c54d68b5ba5 | -1.89393 | -46.82018 | 2024-12-17 05:05:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55bccef9-f4e6-330a-be20-757efe604175 | -1.40656 | -47.47746 | 2024-12-17 05:05:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c54085c-19b4-3655-9eaf-c74220912744 | -1.27787 | -53.4673 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09c6bd27-55ac-362e-b789-0af2de972a7f | 4.45452 | -60.97157 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd6042a2-0a24-3fb6-9ab2-49a5dd5b9aea | -1.63023 | -45.85603 | 2024-12-17 05:05:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbb36f2e-9bfb-35f5-a5bf-a45ca6be0372 | 4.44401 | -60.96092 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9451a397-7ec7-3aa0-a66f-ab44d1a3e8ca | -1.4599 | -53.48238 | 2024-12-17 05:05:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e03bfbb-ce84-3dda-9fa1-45998a5ffce5 | -1.28143 | -53.19157 | 2024-12-17 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1270fc12-e417-32e5-a270-70f6629b01c0 | 4.44773 | -60.95615 | 2024-12-17 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b0f6731-d738-38fc-a7cb-9a30279a68c3 | 2.6164 | -61.30979 | 2024-12-17 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c29bc0a9-6977-3314-87b9-5531e51ddda3 | -2.14335 | -48.0399 | 2024-12-17 05:05:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 408ed143-1dc1-3feb-a738-7c79dd8d846d | -2.58701 | -47.48746 | 2024-12-17 05:05:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f509fb63-5718-38d0-b0d0-adcad2aa83bc | -0.627 | -51.79308 | 2024-12-17 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README27.md)
