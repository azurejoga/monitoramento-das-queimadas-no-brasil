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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df6834dd-fcd8-3fcb-b08d-466917f45b6c | -13.2798 | -54.2435 | 2025-09-16 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8dfa2754-fd95-3691-92f5-f4d087f89a78 | -8.9259 | -45.5231 | 2025-09-16 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| b399c1aa-bb6d-3f1f-a299-5d12660a74dd | -8.9412 | -45.7933 | 2025-09-16 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| b5f734df-3d24-3bae-9e02-1e8c0a4ae8b2 | -14.6143 | -46.3806 | 2025-09-16 13:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ec4c25dc-9591-39d7-9026-2e3aa4b8890a | -9.1523 | -46.9589 | 2025-09-16 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 5dbcf87e-b422-3b7c-b1e7-3bac84f3dd94 | -13.2801 | -54.2228 | 2025-09-16 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 188.3 |
| 5f799b0a-f0c0-3339-99ff-9abb0867a4fd | -9.7325 | -47.3403 | 2025-09-16 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 12ee0e1a-4bed-3568-9e02-de472bb1ce32 | -8.5939 | -46.4143 | 2025-09-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3b2d10af-1d45-3c3f-9f2c-ce62cb074e41 | -7.2771 | -46.5814 | 2025-09-16 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 152645db-a351-3781-896a-17b6eeb2679f | -6.8343 | -47.8284 | 2025-09-16 13:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3173dbd3-3359-3d98-9172-6a94983afc6d | -8.9731 | -46.2405 | 2025-09-16 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 167.7 |
| d90fd39e-6e7e-375f-b06e-72d10a2601f1 | -8.976 | -46.0152 | 2025-09-16 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 471da937-87db-3a23-ac64-00de43068d6c | -8.9793 | -45.7665 | 2025-09-16 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 6ade2697-19bf-3fec-8119-2f15ffcdcaa7 | -8.8795 | -46.183 | 2025-09-16 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a8766167-193f-30a7-86a4-145ba0865e30 | -12.6356 | -45.7422 | 2025-09-16 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3e401966-1167-37d5-b199-36258ebf3c2e | -5.8086 | -43.4956 | 2025-09-16 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| e85cf4d7-0c69-3951-8847-c5d44574e863 | -7.2581 | -46.6052 | 2025-09-16 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 64a615d0-0711-34b6-b80f-ac45ccd7ddfa | -11.4477 | -43.5514 | 2025-09-16 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 5c191b5c-5044-317b-832e-44522989a5f8 | -6.337 | -43.1727 | 2025-09-16 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| de87bbbb-4369-3d78-aea7-c4958018d221 | -6.169 | -41.2114 | 2025-09-16 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| d9b799c2-74f9-3db2-9b38-d41ef357f128 | -11.6434 | -46.591 | 2025-09-16 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 466ccd44-9ad7-3628-a80f-16ac27c89d05 | -6.8341 | -47.8503 | 2025-09-16 13:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 11df5746-8e7a-3250-a50b-5b5d3ff6ff0e | -12.6821 | -45.3209 | 2025-09-16 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 92afa9bd-b294-3974-96ca-74a109b9b6bf | -11.7151 | -46.8739 | 2025-09-16 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5a405fe3-d37e-3847-af5d-0eae87445e09 | -8.9571 | -46.0172 | 2025-09-16 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 814c3d92-bdb4-30fc-a2b4-9ce04ee8cff6 | -11.7342 | -46.8713 | 2025-09-16 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 1702be35-4207-34bb-a63d-494a159f7de4 | -10.9004 | -47.8027 | 2025-09-16 13:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 26da2cb3-b0a1-3b9e-bca1-7633947d6d71 | -9.1709 | -46.9792 | 2025-09-16 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a044a496-fee9-3420-8ff1-959b4ee8c9d1 | -8.613 | -46.39 | 2025-09-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 15ef4402-fdae-30b6-afb7-f7c9c23bf8a1 | -11.1299 | -45.3426 | 2025-09-16 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 93e6a7d3-f487-36e0-bf2d-1094c2da4796 | -5.7871 | -45.9155 | 2025-09-16 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 8c32899a-4130-3915-b0b7-0ba2844e00ed | -7.2768 | -46.6036 | 2025-09-16 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 6a194d0c-8705-3b93-ba7d-e42453fdeb00 | -6.1881 | -41.1855 | 2025-09-16 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| af43ea5f-959b-3ec0-9991-dc8b62949e98 | -8.5759 | -46.349 | 2025-09-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 655b2d61-15d1-338f-b202-8aef38498965 | -8.6127 | -46.4124 | 2025-09-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 6a8dac6e-e65c-303c-93f6-6273e51e663a | -12.6572 | -47.7277 | 2025-09-16 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 93be8d5a-9495-33b4-86cb-d4957086a79f | -8.0005 | -45.6864 | 2025-09-16 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 7d7ad158-6fd6-3428-b1e7-37e39be203b9 | -13.2027 | -47.3126 | 2025-09-16 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| e0e6684a-d4db-3b86-be98-74c18da633ae | -6.6698 | -45.5118 | 2025-09-16 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 8b43e99b-03fc-31cb-82d3-d8653efb3446 | -8.5947 | -46.3471 | 2025-09-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7ca21211-8054-3813-a5b7-66e19b62e390 | -5.7858 | -43.9378 | 2025-09-16 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 50331202-2138-3e69-b548-85cfb7fa2cae | -3.8416 | -44.0824 | 2025-09-16 13:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 400.5 |
| 7d330a53-2e44-38aa-b53a-96ea7d075975 | -6.6696 | -45.5344 | 2025-09-16 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 984a7bf5-6d54-383b-9384-81999a446292 | -11.7147 | -46.8964 | 2025-09-16 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 78b94011-8715-3347-9327-dd6866ad477a | -6.1878 | -41.2097 | 2025-09-16 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 126.4 |
| af1c290d-c344-328e-a177-eeafa88fc176 | -8.6124 | -46.4348 | 2025-09-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 78e5fd2e-7c2c-35d4-8dfc-e2110fb0b6ea | -11.4853 | -43.5929 | 2025-09-16 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 88b03a22-285f-33eb-9e3f-73e775134678 | -12.7286 | -48.029 | 2025-09-16 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 88032649-64aa-3cc6-85d3-fac61dfb3fc5 | -6.356 | -43.1476 | 2025-09-16 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 327.8 |
| 579cf895-309e-3da3-867f-77d5db1ef481 | -8.8984 | -46.181 | 2025-09-16 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 20ad67c7-a39d-320f-9d65-79e45549380a | -8.0007 | -45.6638 | 2025-09-16 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 1fbe30dc-a27a-3d77-98d3-2d5a2c361a4c | -11.0804 | -49.7456 | 2025-09-16 13:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 992fd3d4-a3a6-3f43-a614-1f344b0be172 | -7.6949 | -44.486 | 2025-09-16 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 36e4c883-4a72-3b35-9c20-24ef99d110f2 | -12.1147 | -44.8304 | 2025-09-16 13:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a2f6c515-db3e-3700-aaca-04651353e9cd | -7.7229 | -45.3056 | 2025-09-16 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2217d2a3-29d3-34c8-aaea-8580436d2d57 | -8.9728 | -46.263 | 2025-09-16 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 758c3654-5bbf-3659-958e-a9ea97585c6f | -14.1727 | -46.1354 | 2025-09-16 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| b716f1e8-4380-38c5-a9d4-24170dddbc50 | -6.1878 | -41.2097 | 2025-09-16 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| 315d75f0-11f2-35c6-b788-47fb550a0abf | -11.7147 | -46.8964 | 2025-09-16 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a9e726c6-ebba-3d29-85e4-d18eedcd5bda | -14.1727 | -46.1354 | 2025-09-16 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 6945a38c-01ea-3c9b-bb0e-349eca0f6c5c | -15.5341 | -48.0381 | 2025-09-16 13:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c513c776-08ae-37c2-b1f0-9e34a6e529cb | -8.9167 | -46.224 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e6f1e028-bfa9-35a4-8892-84c9bae6f893 | -7.7229 | -45.3056 | 2025-09-16 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 776fbfbb-5863-3f63-a4d6-14180f33b32d | -8.9731 | -46.2405 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 39f173ec-791c-3765-8c08-9c1766d44f80 | -5.7871 | -45.9155 | 2025-09-16 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 266d1e30-b371-3a47-b485-2faa36ab82cd | -12.4322 | -49.7135 | 2025-09-16 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| f42d0be6-76b0-361d-97cd-7928d7db60d1 | -7.2956 | -46.602 | 2025-09-16 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 5e256283-7268-355e-86f4-4ccf1c4a7323 | -10.7299 | -46.5307 | 2025-09-16 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 365.6 |
| 36716b89-d55c-383b-96d1-ed97e0232f84 | -8.613 | -46.39 | 2025-09-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e4df3bbd-29de-3e35-8df1-764c8f3c71ff | -12.1861 | -44.0958 | 2025-09-16 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 873fa6c2-a2b0-3696-aea7-15ab719016b6 | -7.6738 | -44.6717 | 2025-09-16 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4fbd1a52-333c-3ff4-aa7c-dafc31d0e319 | -9.1709 | -46.9792 | 2025-09-16 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cdb13f18-3801-320a-8c6f-f2f714964172 | -8.22 | -49.4901 | 2025-09-16 13:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 989a3776-735c-3caf-ad47-09635dcb082b | -6.6696 | -45.5344 | 2025-09-16 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| bd16724d-397c-3e79-8ce8-880a272c8efe | -8.935 | -46.267 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 35f0f000-da53-3815-9cea-74e4688172ff | -10.6548 | -46.4727 | 2025-09-16 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| dff8668c-f43e-3f92-838c-1f4c594184aa | -8.9571 | -46.0172 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 45d9aa15-507e-32d3-aa9d-8ff6e943a41e | -5.994 | -43.7134 | 2025-09-16 13:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 9797e2ff-b316-3e4c-b81c-0842c5525a77 | -4.5934 | -43.3239 | 2025-09-16 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6bdd741e-203b-3414-8360-3f00d0337d94 | -4.5936 | -43.3006 | 2025-09-16 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 7055136f-09e3-3bad-a99e-661bc0e98103 | -10.7302 | -46.5082 | 2025-09-16 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 258.9 |
| 4953a34f-eb42-380f-bbcb-540ed659141a | -8.976 | -46.0152 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 50d2fc3b-2d75-3bd9-987f-564515569e3f | -8.9359 | -46.1995 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b8ca78ac-ec1f-3d8b-80df-46e83a0f2b4e | -5.8086 | -43.4956 | 2025-09-16 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 84c14aed-f3b4-3c25-83e2-a4294339cc00 | -12.6906 | -48.0121 | 2025-09-16 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 842eb029-4da0-33d4-912c-75e84122dddb | -8.9728 | -46.263 | 2025-09-16 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b558bcd0-aaa2-350a-9470-c87d7f47d091 | -11.7342 | -46.8713 | 2025-09-16 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 3fd376e5-465e-3128-a320-632e5da941bb | -10.9671 | -47.1729 | 2025-09-16 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 2549c80b-2ddc-3321-bee6-ee079e4f3461 | -6.3372 | -43.1492 | 2025-09-16 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 0e4e6554-21f9-37aa-8839-5ff9fec793be | -14.3751 | -52.9059 | 2025-09-16 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 86620be1-34dc-333b-b61a-e9fd961382fb | -8.6696 | -46.3842 | 2025-09-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 5dac1c65-caa9-3eeb-93ed-8f19a5c8e1e3 | -7.1505 | -47.9786 | 2025-09-16 13:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 5a93261f-ea6e-395f-8fdf-cefef591e166 | -12.4514 | -49.7111 | 2025-09-16 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 209.1 |
| 28e2a566-bcba-33f2-8348-a74a7d4b074e | -8.9262 | -45.5004 | 2025-09-16 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 79523bd8-3db2-3865-a246-74ade18e86b7 | -6.356 | -43.1476 | 2025-09-16 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 344.4 |
| c44607b4-a161-3d0f-b131-b9ae3c048384 | -9.7445 | -47.8468 | 2025-09-16 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 5071593d-1ec8-3dc4-a9c0-24679ed54ad3 | -3.8416 | -44.0824 | 2025-09-16 13:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 257.3 |
| 34ec3d94-363c-32c5-8e4b-76a04f4106d7 | -10.7493 | -46.5058 | 2025-09-16 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| f636d1af-18c4-332a-896c-6f649f5bec6e | -5.8088 | -43.4724 | 2025-09-16 13:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| cf29233a-da68-38b6-9538-7e7e9c33853a | -7.676 | -44.4879 | 2025-09-16 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |


[Clique aqui para ver as próximas entradas](README95.md)
