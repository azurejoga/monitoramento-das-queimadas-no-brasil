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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0225577e-56bd-31a3-9152-feb38881b94a | -12.25268 | -50.53749 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 599eccbb-0fd2-37ed-8d2f-86c6ce607c8d | -5.99882 | -57.82965 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61a77bb1-cb37-33f9-b18e-859a82b60330 | -8.24131 | -54.96967 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89e053ec-0f3b-3e4f-a4e1-85608d0bc1b8 | -8.80138 | -50.49269 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4c47f24-f3ba-360b-b40d-49bdabcf85d9 | -10.80694 | -54.0179 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7c4dd90-313f-325c-8d7c-723ae84af7b9 | -9.40054 | -51.63463 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb327e82-7725-3673-9d41-45b0461a277d | -8.95154 | -62.3925 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 063d0f02-4789-3c60-8e55-0aeb2174a793 | -8.16644 | -46.17073 | 2026-08-29 04:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78408353-8a98-346f-92d5-e1b048726d66 | -8.183 | -54.93864 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76400507-c84c-3f8b-9cc8-18888fc7ac11 | -9.20386 | -51.54646 | 2026-08-29 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bdaafa4c-9645-36d9-a1c3-a63da583851a | -6.51212 | -53.59573 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c82af2f-274c-372b-9d50-808c3d25b622 | -7.59032 | -61.34713 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9fd16e44-d5aa-3331-9adf-259351469ad6 | -10.51044 | -59.6306 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25b90ff8-7077-3527-85d8-a180fdf99a09 | -8.98647 | -50.78828 | 2026-08-29 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 746a8449-aea2-3e57-9721-7b168409c794 | -8.66276 | -49.54921 | 2026-08-29 04:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 7fb5faee-7c04-30eb-b448-efa934a19b11 | -10.28366 | -62.81844 | 2026-08-29 04:53:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e73249ad-1725-3984-90a7-0bb1aea452bf | -6.93179 | -58.96069 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5e3a167-0ec0-3005-8c69-77259a92ad39 | -7.36632 | -55.17888 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79e70064-0285-3903-b45a-7020ac4c6af0 | -6.9511 | -59.48565 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 043e2dcf-211b-3df4-9d94-efaf20414cd3 | -11.71724 | -54.53856 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bcb9e2fd-0e4f-36e7-923f-674f3d49da53 | -12.25955 | -50.53856 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b605fa30-d185-3505-a7a5-f54055a81e98 | -6.31886 | -54.74393 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62e26aba-eb56-3445-b277-d81a8333ee9c | -10.75456 | -54.03601 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 832a9270-96b1-3291-8002-e4bd861337ca | -11.49189 | -46.93929 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 040037bd-cabd-3b73-bd1b-690eaa390542 | -8.59152 | -54.80062 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ec7920c-e907-3e4f-9ae9-45e354802399 | -8.53277 | -55.26557 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7af58156-a2ba-3e63-9106-ebd3220566cb | -11.23441 | -53.99688 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b261f3be-e07d-3792-8617-b6a5a9fcbd2f | -6.15882 | -57.7835 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b07ea937-2b3e-3272-9f8e-3c168855a501 | -9.87007 | -60.29952 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c8b58c42-25b1-3f11-a1d4-fa31f662bbdf | -7.57162 | -61.38601 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8a56e2b1-ebf7-3e64-8c1f-d2cc7c6ea44d | -8.79424 | -49.99157 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9005f73-76bb-3680-b70d-3c65409c8446 | -6.82156 | -59.57673 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ae04d04d-f699-39b4-83bd-616e1f1c1411 | -6.11738 | -57.68849 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0557c442-1878-38bc-aaaa-21687340b510 | -11.04177 | -57.21932 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01fd0d8b-fb74-3522-b74f-0ced01ae199f | -11.22205 | -53.9872 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5220868c-1b9e-3a7f-811f-7cc810675801 | -11.04361 | -57.20894 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7dfb4e4b-bb89-3bff-8c7e-39868d492f77 | -13.31279 | -48.20894 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14fc03a1-b8e8-3abe-97cd-4b94b4af7d92 | -11.02323 | -57.23129 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40eb5066-0164-3e4f-a1dc-11dbae420356 | -8.03321 | -51.81854 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9599b265-7986-3d3e-92cc-09c984abbe30 | -11.48776 | -46.93865 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96218c2c-5fab-3d06-b005-17f317a125f7 | -7.28273 | -45.86042 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42c8b762-7e61-31c7-b630-8b85f52063a7 | -11.03292 | -57.2116 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4282ae70-2c7d-324c-8100-9d1b7a45cf1c | -7.5367 | -44.4559 | 2026-08-29 04:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 793ca42d-80ea-3687-9eba-411204684ee0 | -9.38693 | -60.28976 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ff9d59e-b0ae-3ad3-afce-663bdbc860b1 | -10.80648 | -54.01799 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97430ab6-9321-3f2e-bbf7-a919a416ad9d | -11.48202 | -45.06838 | 2026-08-29 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7278893-f9d4-3360-9f5d-f73bb565ac3f | -13.31362 | -48.20235 | 2026-08-29 04:53:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8acc545-79e9-3d9e-b058-6ee11ed798f2 | -8.82415 | -49.63537 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f730802b-c386-3cb1-9683-8898b88bcac8 | -6.4049 | -51.67544 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aec5954c-c3a3-32e9-9e14-218d3a2683b0 | -10.38756 | -61.24291 | 2026-08-29 04:53:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c27cb4d-4ca7-3baa-bf21-2d46d3d43ba7 | -10.76345 | -54.00309 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd049205-272d-3eac-be38-ed64d67b3ed0 | -6.76338 | -55.66962 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81f9c966-4886-37ed-b891-65fb0011c337 | -6.81609 | -59.45973 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a128034-9b48-3672-96f9-27e73fd116e6 | -7.51384 | -55.31267 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| bb547591-c527-35ca-900e-54d6be5e8221 | -5.88301 | -57.76566 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 889b6637-5f35-3bbf-b01c-e7a2be5dbc5d | -9.87397 | -60.30632 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e2d0613-c5aa-3bd6-9edb-101bca924636 | -8.58755 | -54.75758 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 557f1222-3db9-3d7f-9c98-7995750053e3 | -8.94588 | -50.80731 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e2dd75a-c219-3225-a898-f1220443d78b | -5.94098 | -57.7364 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85b35c07-3060-3fc7-82ae-5352383a22f0 | -11.62467 | -54.59027 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c24aaf03-ecea-35cf-a63e-a2a1ed630287 | -6.16623 | -57.79384 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85f780e7-2986-3fd3-ba80-5af8be3f55b6 | -11.03994 | -57.22968 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a8d6d357-3737-32c7-916b-d562918c6f9f | -6.82779 | -59.95407 | 2026-08-29 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59945f60-ed46-306b-8db4-68f162f58ef2 | -9.91682 | -60.43691 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1412de7d-bf8e-3242-9e84-5d23614bacf7 | -6.94832 | -58.94989 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3447b137-beb6-3865-944d-6d9ac8477d86 | -11.23562 | -45.07375 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 403006c3-b3ff-394f-ba2b-c7ed553e9732 | -11.27785 | -54.03451 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4730eb16-6490-3144-9a56-38c64d55fd87 | -9.13277 | -61.01462 | 2026-08-29 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc4149f1-471c-3dcf-b840-6f63a756292d | -7.19903 | -42.7338 | 2026-08-29 04:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f82c638-9c66-33b3-a6f4-fbb934253d16 | -12.43016 | -42.89165 | 2026-08-29 04:53:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f580364d-13f3-3fc0-bfe1-e3fa29c9ca9d | -9.60988 | -55.12714 | 2026-08-29 04:53:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| d7c54db1-7c9a-37ac-a02a-add538fe93a2 | -9.42925 | -51.68925 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a17eee02-a234-3305-ab65-eeb222d074ce | -11.62039 | -46.72589 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94910583-d18c-37ed-8fb8-097211beea32 | -9.42375 | -51.70266 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bd43320-87ee-3069-9ee7-ea06b353698c | -8.81841 | -49.6267 | 2026-08-29 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d0875a4-d07c-3221-bb0c-6315d983140e | -9.39999 | -51.63812 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e01ac49-55b7-327e-8ee8-a4d563ce82b8 | -8.95233 | -62.38833 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d777bc1d-1561-38d4-b7ee-b7ca33310014 | -6.84529 | -59.94458 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 424888ed-a41c-3244-825e-5413f71f649c | -6.27348 | -53.13996 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a8a89a7-39c6-3bc5-8a02-6e16476934e7 | -6.5529 | -47.47078 | 2026-08-29 04:53:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c55f4bbc-0654-3779-a822-299cead9fb25 | -8.53185 | -55.36012 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7ff0c202-e583-33a9-811d-e47fbcf7c7ae | -11.27724 | -54.03823 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baea1bba-144e-3993-b24a-f92a68907c53 | -6.53993 | -55.2435 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56ef74a1-c914-331e-a747-e9cccff4059f | -7.30163 | -49.54311 | 2026-08-29 04:53:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f25f50f4-6b55-31fa-8d73-4681da9ec2a4 | -13.4073 | -51.80167 | 2026-08-29 04:53:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 151d0e20-4eb2-3ff5-a483-b120061c8556 | -7.34048 | -55.16243 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c88968d-d0aa-3112-94e8-ea752a4a3e79 | -6.93214 | -58.95775 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f7a5f5e-2bd6-3cbb-a769-867adcc8faa2 | -8.50495 | -55.32575 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dccf6daf-0aab-3b4d-872b-9290dedfc695 | -9.46293 | -51.58412 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e60422a-ab1c-33a8-8372-240e41cb6c2b | -11.2372 | -54.00117 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6754f5cf-4c1a-3cc7-bab8-6c3df9f327fb | -11.14527 | -50.59725 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02e911e5-6ea0-382d-b71e-7dbc1025783b | -11.48417 | -46.93415 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a1fbe29-9904-3409-8e36-b7ade6a28435 | -11.37194 | -45.14139 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ddecd5fb-ad74-3109-baa0-a3bc2daf8692 | -8.95501 | -62.40601 | 2026-08-29 04:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8198e42-eaae-31e2-8520-af3c58f7ce3c | -11.61145 | -46.72865 | 2026-08-29 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbc5b1ea-f181-37b8-a5e8-725b25295b6c | -8.59219 | -54.79652 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95fae83a-d48c-369f-bfdc-04ae3490865a | -8.53645 | -55.26618 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84065973-758c-3a23-acbf-a03d38a6710a | -6.72469 | -60.01708 | 2026-08-29 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf58d4cb-bec4-3501-b8c0-0b9acbc1fe50 | -10.07457 | -48.69559 | 2026-08-29 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 636db770-357e-318b-ad00-6df69f2979f8 | -5.88223 | -57.77026 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README46.md)
