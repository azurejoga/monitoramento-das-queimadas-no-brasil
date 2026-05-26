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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfee058a-150a-3027-a000-11dec8680772 | -5.81406 | -43.20861 | 2026-05-26 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 245d03c2-2024-34e3-a72f-b40cfd69042f | -7.13819 | -44.06781 | 2026-05-26 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 00956102-08d2-3f39-83e0-7971d41e8d99 | -6.73069 | -44.36829 | 2026-05-26 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f1ec2d5-adb8-38e7-afa1-ee85e4b97d60 | -5.35321 | -45.18551 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6490d77-73d6-320b-ba0a-6b3757538d4c | -7.00995 | -44.99059 | 2026-05-26 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3466309-1a67-3430-8246-01c2c98048d1 | -5.53375 | -35.52643 | 2026-05-26 03:36:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35c94138-8898-3f9e-a18d-e600e9fb9df4 | -5.79687 | -45.12166 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c38695ad-0522-3b53-aa66-5a5d87e78674 | -7.01429 | -45.00119 | 2026-05-26 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b7e1b86-e29d-3df5-9fe4-a7bb224f2c21 | -5.79495 | -45.13214 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca2f3bc4-0c79-3d5b-a460-3d35bb8ef8ac | -5.30003 | -43.06616 | 2026-05-26 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0f902ae7-689f-3108-9cd7-46b429808e88 | -5.95343 | -43.48888 | 2026-05-26 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9bad0a50-070a-3b47-9fc4-0245b83add05 | -5.79061 | -45.12046 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3ab8eb04-fb0a-3022-b365-bfe793da3f20 | -5.78773 | -45.13613 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c920a3b-d85a-300b-8221-c3ea8f0d46ce | -5.34902 | -45.1864 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 576d8bed-1d17-35c7-9415-e4a251378fa8 | -5.1825 | -35.86097 | 2026-05-26 03:36:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b9ae0c05-0640-3fe1-85ad-965c4984542e | -7.14464 | -44.06493 | 2026-05-26 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b62743c-0897-3f77-92ea-26c4a42debef | -5.81581 | -43.20517 | 2026-05-26 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e554f75f-a98c-3e54-9533-fb0b27b51ccb | -7.13966 | -44.05961 | 2026-05-26 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9210edea-4a35-386f-aa1a-de61c4ce0c43 | -5.79591 | -45.12688 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c80da3ab-a83b-394b-80e2-9b69d0c45209 | -7.01343 | -45.00547 | 2026-05-26 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0786f74e-fa57-3f06-926c-f7adc70fb849 | -7.13239 | -44.06702 | 2026-05-26 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a66ab3de-b62f-354e-b69f-f28a1378588e | -5.79078 | -45.1345 | 2026-05-26 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6caddb8-9a42-374c-bcf4-9af4ba602275 | -8.33613 | -45.38124 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b748ed75-1ad3-3423-846b-724f0157c758 | -8.55661 | -45.9819 | 2026-05-26 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d6aa4482-0671-39b3-bffb-4e43231e8e16 | -9.36485 | -45.46752 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 39493d11-22d2-34a3-8f51-4744c4e83cf6 | -9.364 | -45.47203 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2e951c4b-2bc0-3f2e-a73a-22632b36fd3d | -10.63837 | -48.33125 | 2026-05-26 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00a739d7-7405-3330-b533-8cf9cd300f8e | -14.16749 | -45.4397 | 2026-05-26 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbb66cf5-4757-3fc4-8e74-0d76821ff697 | -10.63141 | -48.32962 | 2026-05-26 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbdb7e3d-5741-377d-b23f-434fe959e02c | -10.6293 | -48.32939 | 2026-05-26 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27221e13-db2b-3a17-8c2d-ddd3957cd7e0 | -9.30254 | -45.49805 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f7c5eee-7501-37a1-b9e0-a010b8f968f1 | -12.04773 | -45.27562 | 2026-05-26 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02df3996-372d-3fcb-88fc-b91c4700cafe | -10.60302 | -44.32399 | 2026-05-26 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dad15939-6b43-3dbb-8edb-a2c74ae89f26 | -8.61533 | -45.03218 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7eede56d-0a1a-3714-8487-7aec6eb8d005 | -12.04272 | -47.33353 | 2026-05-26 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7249152-ea71-372a-b81c-bd539dc86ddc | -8.61615 | -45.02769 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7dd95fb-13c0-3c61-a7d7-d67a870ed2a6 | -14.24825 | -45.82909 | 2026-05-26 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eeadfc5d-594b-33af-93e4-9c899e73b921 | -9.33805 | -40.21044 | 2026-05-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| dac81a1e-cbf4-3cbe-80b1-70a99e2ffcda | -14.24745 | -45.83308 | 2026-05-26 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8ff5c9f-aa37-3f1d-8e32-833ac80c8197 | -7.59935 | -46.46814 | 2026-05-26 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e474facf-112a-32db-888e-8fa637e3b5c3 | -11.97172 | -46.79269 | 2026-05-26 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1f3b728-f165-385e-a2a3-4c6c3df72e36 | -8.61296 | -45.02745 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d662e79c-133c-308d-9a94-4903898e28db | -9.35796 | -45.47083 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dbd9e2c8-2f93-385d-bbae-bc2f1d5abb89 | -8.55985 | -45.98584 | 2026-05-26 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 288625fc-ddbc-347e-a5d6-a31827084169 | -14.1612 | -45.44229 | 2026-05-26 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02d5bd69-3183-325e-83f1-6ccfb824e803 | -14.16543 | -45.44431 | 2026-05-26 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e43e9a9a-11c5-38f9-82a1-991657ffcd20 | -8.54932 | -45.98569 | 2026-05-26 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6881d542-bd62-3159-8904-fb9caea5a660 | -12.04269 | -47.33497 | 2026-05-26 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c49d7006-de14-3012-8f11-2f6f4e984c4f | -7.5967 | -46.46941 | 2026-05-26 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30e1a3cf-5b66-39e4-8221-f85269950019 | -9.3571 | -45.47538 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3a28698-7e8b-31e1-a070-116eab1ea804 | -8.55566 | -45.98681 | 2026-05-26 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0a6798aa-4552-347a-8f4f-e2fb83275afb | -8.33021 | -45.37857 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92f90620-f24b-3db4-98ff-bb04aec24748 | -8.9721 | -47.98782 | 2026-05-26 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8a33d78-d8cc-308a-ad80-9820b38fccf0 | -8.97688 | -47.98591 | 2026-05-26 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d74cf789-08dc-3fe7-ad06-9c67fb457255 | -8.62292 | -45.0244 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95d05a13-b8e3-3b35-9d74-b20a384f774d | -9.46733 | -46.11441 | 2026-05-26 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08cc6b51-a07d-3280-8af5-bd85e8406b23 | -14.16619 | -45.44056 | 2026-05-26 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cc1677d-5edc-3d0a-985f-6aa15d387be7 | -8.62574 | -45.02517 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1364307a-aa1b-362e-8d4b-41da1c808de1 | -10.62997 | -48.33671 | 2026-05-26 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78c306fc-fcf5-3a3e-9281-bd8675ec6403 | -10.63625 | -48.33099 | 2026-05-26 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56855bbb-5f93-3430-98ea-3b544b5c01ba | -8.32993 | -45.38049 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3eab9a3f-603d-346e-87c9-95fa440fbd94 | -9.35019 | -45.47877 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f6da90f9-2208-33d3-b512-76943aaa1dbd | -12.0416 | -47.33907 | 2026-05-26 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac9f057f-8bb1-3374-85e7-20013d81f66f | -14.03977 | -46.35179 | 2026-05-26 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6710a915-6291-311e-9a86-795ff9714762 | -8.62213 | -45.0287 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40b6f84f-e1f7-3297-9ee3-b8f9fa30b8bc | -7.59781 | -46.46363 | 2026-05-26 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74fa4915-763c-3c3a-a340-f17596705a63 | -14.04064 | -46.34751 | 2026-05-26 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23ea15e6-2cd3-3203-9da7-12943715d464 | -8.62492 | -45.02946 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f040931-39b8-321e-8500-c8f244f79ab8 | -9.46424 | -46.11186 | 2026-05-26 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 401ca12f-ca04-3d49-b5a7-512660b6bffd | -8.61895 | -45.02844 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a31079e-a0ce-39ae-83d6-933052573529 | -8.6121 | -45.03197 | 2026-05-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bf7fa0f-e0aa-3f67-ae59-30e7dd76be63 | -9.29739 | -45.49218 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bc984c5-9f7e-33e9-9308-fb9862a6dfee | -9.35105 | -45.4742 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 87e8c542-71dc-3426-96fe-ca62c8a772d8 | -9.37266 | -45.46674 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9a6fd05e-1dbf-3362-9053-09c591605745 | -10.60373 | -44.32029 | 2026-05-26 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 198d97ec-8667-3fdf-a43d-de2e4c2c57da | -9.37089 | -45.46873 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3b72ab8f-7fd0-365c-9527-12dc7049a2f3 | -8.97919 | -47.98901 | 2026-05-26 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0caef48-2318-32ed-add3-4f4f59759f74 | -10.59751 | -44.32293 | 2026-05-26 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 58399cdc-b49e-37cd-b553-fe49e8569daf | -8.55357 | -45.9844 | 2026-05-26 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 29a198c7-9402-34a1-abe8-c58a886f3462 | -11.61458 | -47.90234 | 2026-05-26 03:38:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09ffa866-33b3-3ef5-81bd-ac5f2f9de787 | -9.33734 | -40.21455 | 2026-05-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ec3a30b3-bc0b-3834-9535-bac08661d63e | -9.37173 | -45.46428 | 2026-05-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a885fcad-0985-3cf8-b92a-be172058df46 | -11.3773 | -52.9496 | 2026-05-26 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 62d58bbb-9230-395c-ae94-7168a9eea8ca | -11.3584 | -52.9514 | 2026-05-26 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 61b3eaa4-94b7-3ba0-818f-88fac8f6bfd7 | -21.32517 | -47.07367 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35834d1b-8214-3d02-b0de-69907da37c58 | -21.26793 | -49.47736 | 2026-05-26 03:40:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 04dc0377-5db4-3de5-844d-0eb7db3d8d2d | -18.08178 | -46.87958 | 2026-05-26 03:40:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d481a78f-243b-3c7d-abb4-6c1f5f7d58b3 | -21.30406 | -48.5882 | 2026-05-26 03:40:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 49072e8d-0726-3f53-a85d-efed6c496a5a | -21.55375 | -47.0526 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be45c792-c5fd-3884-bb50-47b877e647bd | -21.32063 | -47.06866 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fec13cb-cb36-3447-b8c0-5c6a9e338d35 | -21.29966 | -48.58879 | 2026-05-26 03:40:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| de54b3c2-2c84-3b38-9aa1-80614e460b3a | -21.55051 | -47.05558 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 301d07d3-eec9-33a4-aa56-83fbc78fa4b0 | -18.29133 | -40.14423 | 2026-05-26 03:40:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0404fcf6-e16c-3525-9046-12278d069524 | -21.55827 | -47.05757 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da6a2fee-4411-3641-9fdb-e5d19a89f7ea | -21.5566 | -47.05338 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c07d07c9-bddb-31c4-81cd-3409c7b75a90 | -21.5513 | -47.05202 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0982ba5-c010-3cf0-903b-0fa19f1d9a1c | -18.0856 | -46.87724 | 2026-05-26 03:40:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8a31fa3-2202-38e3-82d3-10ae2287bb63 | -21.30553 | -48.59012 | 2026-05-26 03:40:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 11bb946e-1220-3d79-9b8e-ce828b943eec | -21.55581 | -47.05693 | 2026-05-26 03:40:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b857c45-2af9-3965-be49-71ae967ee8e7 | -18.29215 | -40.13956 | 2026-05-26 03:40:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README5.md)
