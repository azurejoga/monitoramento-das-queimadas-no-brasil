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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89cfbd2d-a63f-3796-ade1-c3bae1c2370c | -11.5054 | -43.5426 | 2025-09-29 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 0ce47055-ce01-382b-acf3-c7cfa7c0475e | -9.7674 | -46.1971 | 2025-09-29 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 0b811696-6520-3c76-8cb5-4c2e43486458 | -11.383 | -45.0543 | 2025-09-29 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1b4fa0de-3e53-3ce6-9c0b-0824356e552d | -7.8375 | -46.7766 | 2025-09-29 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3c279013-122c-3baf-a986-47433f5a1f32 | -7.8378 | -46.7544 | 2025-09-29 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| bd26db07-8240-304a-afe9-aa975723bac4 | -14.8889 | -47.1999 | 2025-09-29 13:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 135.5 |
| c63cc967-b650-37a2-bac2-eb4f6108f43d | -7.2216 | -44.7601 | 2025-09-29 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| dbb03ba9-7c57-3f9e-9dbe-85d7c1c46b7d | -6.4319 | -43.0707 | 2025-09-29 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 3caec9bd-96c8-3fff-a9a3-399724670cbe | -9.3708 | -47.556 | 2025-09-29 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 52fb4b42-0356-35e9-b670-32350a58490f | -9.7643 | -47.7786 | 2025-09-29 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| cd72ce91-e5fa-36a3-8d9b-ee7d9a6f2e1e | -6.9692 | -43.7927 | 2025-09-29 13:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 7f66d7e6-cdb9-3536-b476-af59a5d71405 | -9.2821 | -45.733 | 2025-09-29 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| f2c7cdcb-ee6a-3bde-9096-96740a834aca | -6.5232 | -45.1843 | 2025-09-29 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| f59945e9-9acd-354a-84e4-507449399695 | -13.3989 | -48.1549 | 2025-09-29 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| dc4cfae4-f944-364e-b2ae-f75b782d7fd9 | -9.7454 | -47.7806 | 2025-09-29 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 0aa5c677-8ce3-372d-bfcc-36c563ecb405 | -14.7176 | -45.2057 | 2025-09-29 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| a1950e7e-55d8-3908-b782-83e995db4fe0 | -11.4409 | -45.0229 | 2025-09-29 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| f935d813-1fe6-377a-8e6e-bc26a264252b | -8.1614 | -46.3899 | 2025-09-29 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 000753f4-02e1-3cf9-b078-21471c9ae204 | -6.0811 | -42.4644 | 2025-09-29 13:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| f27fda94-813e-3485-b5e5-8768c93606e4 | -14.5331 | -48.4491 | 2025-09-29 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.8 |
| f3113a51-ad54-35fc-9ff9-c4f7a86a1538 | -6.0797 | -42.6064 | 2025-09-29 13:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 7b1d8254-a9bc-367f-8f3e-e26261f14011 | -6.6192 | -44.9493 | 2025-09-29 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 178d6197-935a-3a08-b943-996f5a876d7e | -8.5413 | -44.6284 | 2025-09-29 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| d7c4d7d1-b433-34e4-8a50-dfbb132e7a42 | -7.3001 | -42.825 | 2025-09-29 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 219be1ce-11c1-3d0a-a9ce-58c9faf815fb | -7.2214 | -44.783 | 2025-09-29 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 6c02143d-b902-38ac-a898-365f71ec7857 | -6.0623 | -42.466 | 2025-09-29 13:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 0cdfbd13-9c21-3e9f-b48b-e62bf4dd49c3 | -11.3443 | -45.0828 | 2025-09-29 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 807f060e-4701-3349-b956-ed8861d8c21b | -8.9456 | -51.6712 | 2025-09-29 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 2b3e0d1a-2faa-3dfe-bf44-db6ddda3f6fe | -11.8482 | -51.7916 | 2025-09-29 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| f9401ca9-e93b-3dfe-963e-6df620a76d11 | -8.5221 | -44.6535 | 2025-09-29 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4889f808-0dd2-3fe5-a934-0d88255de6a6 | -9.4007 | -54.6984 | 2025-09-29 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 1b7838c7-92f7-3e81-9795-a6657d7b70c0 | -11.46 | -45.0202 | 2025-09-29 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| ed381d26-92f9-317d-8fc8-5301c60999ae | -11.4421 | -44.9535 | 2025-09-29 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e9d83165-6b3c-3157-a976-d67e32486fb6 | -8.88 | -47.6282 | 2025-09-29 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 930d3b7a-680b-3926-926b-26ef24d609d6 | -7.8165 | -46.9781 | 2025-09-29 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| d5154c4d-3b09-33ca-ac49-6632e1b9e55d | -7.2999 | -42.8486 | 2025-09-29 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| e637fade-060f-3987-8c5c-d596b55159a6 | -15.6127 | -46.2465 | 2025-09-29 13:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 0d9ada36-faba-3515-b68a-2a216010d1d0 | -11.3642 | -45.0339 | 2025-09-29 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| e1e88a26-7bc5-3a26-afde-5bf96549b53d | -12.863 | -46.9582 | 2025-09-29 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 7e6e22d6-f653-3510-8e7c-7886cbffdb43 | -11.3447 | -45.0597 | 2025-09-29 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| a7fec97c-2953-3237-b47e-60f3e18475d0 | -9.7451 | -47.8027 | 2025-09-29 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9467dfeb-f0a4-3ef7-b1d3-21d8dfe08c65 | -13.011 | -49.4423 | 2025-09-29 13:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 7ebbe5a7-fc6f-3fad-9a5e-b2604c4d96d2 | -6.4317 | -43.0942 | 2025-09-29 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| fa2cdf99-b564-3f12-b374-d62d45467a5e | -7.4488 | -46.299 | 2025-09-29 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4c6c75ac-0634-3377-aeed-7fe284351408 | -11.3826 | -45.0774 | 2025-09-29 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 66b219c1-7b6d-36f7-adf8-20e23f416450 | -11.4405 | -45.0461 | 2025-09-29 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 03fdb5f7-65e6-3247-90d0-a04ce0907208 | -9.9959 | -43.6172 | 2025-09-29 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ff7b3d43-b78d-372b-ab4e-875b0c1de70e | -8.874 | -46.6092 | 2025-09-29 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 25ee7bc7-3431-39c6-b363-9be8b902b755 | -7.8566 | -46.7527 | 2025-09-29 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 439d96e3-a0f5-3ad6-bd9b-d187079cb2d4 | -9.7677 | -46.1745 | 2025-09-29 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| b6449b46-5658-3ce7-82e1-166a0a980dea | -9.7399 | -45.4755 | 2025-09-29 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5a6d0cec-0a5e-33fe-bdef-b534c8d0b23e | -9.4455 | -47.6144 | 2025-09-29 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 63ab27d0-3192-3d64-87c1-5e89cfa5d858 | -9.4194 | -54.697 | 2025-09-29 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 47b84f7f-75d4-319d-9d12-acd3f032f769 | -12.9547 | -45.1618 | 2025-09-29 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 231.5 |
| de93d205-cd6e-3511-a546-10251839ff91 | -5.4742 | -41.0767 | 2025-09-29 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 654fb5eb-16d7-34c1-8c6b-20645d66b1c0 | -7.5089 | -44.297 | 2025-09-29 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 46750287-3806-3280-b90f-901a59b87268 | -7.2813 | -42.8269 | 2025-09-29 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 225285ba-c680-30b1-a19f-32a5c68d61cb | -10.6883 | -46.7604 | 2025-09-29 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b2c7f5b4-adcb-39a4-a500-ca40bcc83c5f | -7.281 | -42.8505 | 2025-09-29 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 64497ec7-1889-32ce-b169-1c929d558581 | -6.748 | -43.3938 | 2025-09-29 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 3048deb4-1ee9-315c-8a8d-ee4d4f804985 | -11.3447 | -45.0597 | 2025-09-29 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| a90bec67-eede-3b28-ac01-48dab595ce7f | -8.2662 | -45.5018 | 2025-09-29 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 1ba4528e-b7a3-3961-abd2-4b4dfdb32a7d | -7.9008 | -44.5805 | 2025-09-29 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 83d7e4bd-7141-3693-8f3d-5b7b99881dca | -13.011 | -49.4423 | 2025-09-29 13:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 50eded85-9fcd-3b2c-a5b2-bfa6be5aaddb | -9.7451 | -47.8027 | 2025-09-29 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| ec28a056-8b40-34fe-b958-c21e7c78f997 | -15.6324 | -46.2429 | 2025-09-29 13:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9bc0c596-14d9-3aca-b46b-309a1bfdd7be | -6.5232 | -45.1843 | 2025-09-29 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 134993c4-b90f-3294-8d19-f32dab9f721b | -5.4258 | -42.2797 | 2025-09-29 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 88d9f2e8-c5c9-390c-873c-3bd1b0e33974 | -10.3257 | -48.2001 | 2025-09-29 13:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e8462bce-be16-3a6c-ad4b-5cc1c0480011 | -7.9006 | -44.6035 | 2025-09-29 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 576979ea-a185-3317-979b-506cb962d78e | -13.1816 | -50.6969 | 2025-09-29 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 16fa6dde-2dd8-36cc-b5ab-d233882cd3c2 | -9.1105 | -45.8426 | 2025-09-29 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| a4fa46b4-f918-38aa-bd88-5a21da476014 | -9.7674 | -46.1971 | 2025-09-29 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 1db9230d-4ac1-347c-b11a-7e0ffcdd0219 | -5.9185 | -45.839 | 2025-09-29 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b5461f6a-b8ad-3dc2-adfb-a5376b719316 | -15.219 | -50.1071 | 2025-09-29 13:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 8263718e-d41e-34eb-a521-23e6a792df2d | -7.2405 | -44.7584 | 2025-09-29 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 3f540779-968b-3083-9e66-933c1d9a37ea | -9.7264 | -47.7827 | 2025-09-29 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 109d36f8-bb9f-3c45-8872-38284d58c4a1 | -11.4409 | -45.0229 | 2025-09-29 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 2ff8e1fd-17aa-360b-ade2-75485c4b9c10 | -12.9435 | -46.7655 | 2025-09-29 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 7f6e8c55-1adf-31ec-8c89-0cd88e69c88f | -6.0797 | -42.6064 | 2025-09-29 13:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| d6fd1bf4-265d-39f8-885c-87cd1cba30f5 | -6.0609 | -42.608 | 2025-09-29 13:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| f318b541-248f-3a28-8d37-a2b3036db0fe | -7.9049 | -49.1945 | 2025-09-29 13:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ab68deb1-2ce6-3fcf-9dd1-d2c46e9ddf97 | -7.8019 | -48.3173 | 2025-09-29 13:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1c7f0bae-2e0a-3148-9b9a-41aa6a0b61be | -9.939 | -55.1632 | 2025-09-29 13:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 20e76132-2515-3682-9fc8-c36a94982e30 | -8.9456 | -51.6712 | 2025-09-29 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 42053be9-5233-3470-9293-e6edb2248e94 | -12.8634 | -46.9356 | 2025-09-29 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 20e66e20-c439-31d0-9230-6e4355076700 | -10.0065 | -45.3976 | 2025-09-29 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 8408d9ea-8ef8-3164-a662-21f84d61e2a0 | -7.3653 | -42.1058 | 2025-09-29 13:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 195.1 |
| b2213ed4-2b05-320c-9cad-a05053a6cb21 | -8.1614 | -46.3899 | 2025-09-29 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d08e2d16-c0a4-369f-93c2-aa2c4e9965dc | -12.863 | -46.9582 | 2025-09-29 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 4b016b04-688c-3d0c-a37f-624e4bc6fbd9 | -7.365 | -42.1298 | 2025-09-29 13:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| f48388cd-ccd6-34b8-b89b-144e3d0255ca | -6.4131 | -43.0724 | 2025-09-29 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4b66b1d9-be06-3500-a24a-fe2115f68a06 | -7.8163 | -47.0003 | 2025-09-29 13:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| bd44b1b3-9377-3eb8-abb2-17e7004344ff | -9.9872 | -45.4228 | 2025-09-29 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 5cef6992-9b66-3f3d-b7e7-b09f1abff808 | -7.3001 | -42.825 | 2025-09-29 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| 14198887-2b6f-3480-9623-1a3720141052 | -9.3708 | -47.556 | 2025-09-29 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 4cb23ad7-3c67-3d2a-961a-ef10a9f0bcbc | -14.5336 | -48.4268 | 2025-09-29 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f3fd7c24-ae2d-3b00-a951-2a2ea73b3fcc | -8.2474 | -45.5037 | 2025-09-29 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a11cba41-34dc-35a3-8e41-63e1f0443d75 | -9.9875 | -45.3999 | 2025-09-29 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 33f050a4-727d-3efe-a1a3-17cd34f806ae | -13.3989 | -48.1549 | 2025-09-29 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 120.1 |


[Clique aqui para ver as próximas entradas](README93.md)
