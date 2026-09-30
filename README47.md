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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62062fc7-6c8e-3a6f-bdf9-49d2c3cd4811 | -10.48993 | -49.27826 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c067f7d-88a0-3012-b997-35e47ed305e6 | -15.6358 | -43.23076 | 2026-09-30 04:53:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a9f15a3d-f925-34f8-af00-7ffbac56f50b | -3.14921 | -54.08374 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6967a8b-5b30-3076-9a4c-990099142133 | -7.80948 | -45.81907 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6b3bee42-d8ec-3457-83a3-1797df7a3c44 | -7.34292 | -55.22701 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9cb6389-060f-3b04-821a-e8a2de2c770f | -7.01353 | -45.30276 | 2026-09-30 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be5f96e1-f6a3-3ae7-9e70-e5efe3beae7b | -3.16561 | -54.0998 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2bd82657-a510-3817-abcf-8195b66f158e | -5.73337 | -45.05434 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 181c8a7b-8f9d-3301-bf69-1b7a502b159a | -5.73859 | -45.16644 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0adbe703-e920-35d8-b75b-ac0e2ee35ff9 | -11.13976 | -50.07977 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6dcc7a7-1bf4-3b1e-af68-48815ace8c51 | -6.92668 | -44.56028 | 2026-09-30 04:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e35ba13e-9783-3675-9b4a-37aa89294ab4 | -7.52723 | -44.54438 | 2026-09-30 04:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cba12209-e40a-3e24-bb9b-c5ab160c16cd | -2.89693 | -54.13675 | 2026-09-30 04:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b4c588d-c41c-3651-9c28-4b57be222825 | -10.08644 | -50.31178 | 2026-09-30 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31e47028-230f-3f1f-9204-49c1f2d33cd4 | -5.98769 | -53.55282 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 625ec3e4-b8a1-3c48-a3df-2437fdf5b1d3 | -7.83053 | -45.82241 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96f36323-9651-364e-9610-032f3b19796a | -17.79322 | -47.17168 | 2026-09-30 04:53:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8d96993-ae60-3ad6-8298-0bc538f1ff7c | -11.37863 | -43.37839 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c232719-8273-3550-a36f-900118b8d4e6 | -6.71081 | -45.62845 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e98507a4-c301-3d12-a0d9-9cc025b2dda1 | -6.28795 | -43.64124 | 2026-09-30 04:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50cb2145-03db-3ac2-961b-920f5c08a4ae | -11.39598 | -47.43484 | 2026-09-30 04:53:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d3e049d-f442-3cea-a532-d76399e5fa66 | -8.98541 | -44.1788 | 2026-09-30 04:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3636880-0136-3c51-85da-e027f2b9b617 | -6.99865 | -43.86273 | 2026-09-30 04:53:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6db6b637-e828-36cf-9050-052a816d0801 | -9.78948 | -44.81776 | 2026-09-30 04:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0125ae27-88df-392e-aafe-8a0bbbad685b | -5.81733 | -46.21409 | 2026-09-30 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59ea9e12-f2b1-3af8-99e5-a7f3233f0f57 | -11.7059 | -43.44906 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ad461ad-1db1-3be9-9d90-336038a15f53 | -4.03117 | -54.20558 | 2026-09-30 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04f7e91e-4197-373c-9281-dac99653dea2 | -10.71953 | -50.49833 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cd31560-6560-3b80-8d16-222da72eb3a0 | -9.1646 | -60.79635 | 2026-09-30 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83668dfd-0a52-3e41-a3ad-2613db255a2b | -7.82689 | -45.81791 | 2026-09-30 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d24f2cb-ca28-3950-af17-18613c13b1e3 | -6.11176 | -55.69595 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46be3603-6e98-399d-a491-27b0093ce1a3 | -15.25441 | -44.82172 | 2026-09-30 04:53:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea90953d-d128-3558-ac8c-d6573e5f30da | -8.93264 | -49.77551 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dc8acb8-51fd-3086-8a2c-5ddcc4da1e08 | -9.22236 | -45.85443 | 2026-09-30 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c77e79e-f46c-3773-b0ae-99a69da4386d | -3.5125 | -50.30995 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3134d810-6458-3a51-9413-c4d5c3be491a | -5.74715 | -45.16759 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc4be3ac-ee38-3dbc-9ea6-a7a1f20eec4c | -8.4841 | -54.91194 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b555d09-5d6b-3748-b958-4c4998b3ed93 | -2.90107 | -54.08758 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 9a7eeae4-a44f-3c3b-9c68-6c41108c30a1 | -10.77879 | -47.72651 | 2026-09-30 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 846a000c-8a27-341c-aac1-deccfa87e33f | -6.37895 | -55.13786 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25a939ac-4f7d-3086-b5df-dbb7d6bc8484 | -8.06022 | -55.34169 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78cc880a-813e-308f-9ccb-3c1df98a9e86 | -3.79122 | -52.39347 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f54b191f-4a9a-3b66-a497-c3d51372067a | -11.38424 | -43.37688 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 567960fa-4b6b-3200-9df6-8e1b4561584b | -11.34964 | -43.35468 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 422a9b59-2e61-33be-8bfb-dd63e12ff9ea | -14.89999 | -51.86533 | 2026-09-30 04:53:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f23e94b0-7b09-3bb9-b2e3-6f6b96e82f02 | -3.95949 | -49.04884 | 2026-09-30 04:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a97736b-a7b0-3bc4-a385-308ddebb4a13 | -5.75572 | -45.16877 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f055f88-4abf-3636-84a9-2537466748ad | -7.72644 | -54.79641 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4d8c461-c617-3690-a451-82cde320a6d3 | -6.72934 | -45.61926 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3b17c23b-992b-389a-b57a-339be242d737 | -17.12788 | -52.12881 | 2026-09-30 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3af4b595-4379-3298-b1ea-e3cf68643281 | -7.49096 | -55.59452 | 2026-09-30 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4a84de4-1a58-315c-8b35-64c0d4c35a96 | -11.13688 | -50.07539 | 2026-09-30 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21c66c91-51d9-34fd-996d-99d5c2b468b0 | -11.18784 | -44.83789 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cec327e5-2498-3aec-8914-b489f95b8dd7 | -9.80531 | -44.83992 | 2026-09-30 04:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 821c7ed8-62c5-33e9-80c7-aec9f58b21a1 | -3.35654 | -50.75748 | 2026-09-30 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52c8fc6f-baf2-33b1-9458-6846a7ac2050 | -10.66042 | -50.74209 | 2026-09-30 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06e7314a-1c64-329d-b226-027f8bc191f2 | -18.10526 | -44.40964 | 2026-09-30 04:53:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 760aa793-7531-326e-b492-72f603410bc7 | -6.39839 | -55.23312 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 227a4d0a-eee6-332e-8f8f-4220ea93ec0f | -10.90178 | -43.85653 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd0079c9-bbbc-30ef-9ee1-104b85875b86 | -6.33408 | -51.15594 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60e0e561-13b3-301e-adbc-78530ca49432 | -3.3762 | -50.84919 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0837731-5853-383d-8422-37244915afcb | -5.09334 | -49.05881 | 2026-09-30 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 007fa208-2b79-3c7d-82d0-40ef25a3c6d7 | -10.82244 | -48.71878 | 2026-09-30 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 248cee38-1a8d-34f6-9b8f-4c2de1cdc22d | -11.21097 | -44.81754 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c80e57a5-09fd-3ebe-885b-b0c840bba8f9 | -6.39858 | -44.83981 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac68d4a5-eb83-384f-9178-7a105f839b43 | -3.15061 | -54.07502 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39b92989-1aef-3b70-bd8e-2f0228f7ffd5 | -11.41082 | -43.42022 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 345ae4af-0a32-3eb9-a818-f7ab2eb12fbe | -11.45818 | -43.46588 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a953f123-cec4-31bb-b249-01ee9fac35de | -5.13028 | -56.02159 | 2026-09-30 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1da53e42-160c-3e91-a43a-3fe7d8b21d5d | -5.97196 | -55.37335 | 2026-09-30 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ede76e8-0ab8-3d59-8991-bb1b183c17e8 | -8.25179 | -45.44057 | 2026-09-30 04:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 134b43d8-1b91-308a-8eef-fc94672afa04 | -2.89665 | -54.09137 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7290c063-f475-396b-9d10-032599d67ca9 | -8.58584 | -50.41466 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 06a6efcf-fa8c-3171-b923-9729afa6d925 | -4.8107 | -46.84812 | 2026-09-30 04:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45c0718f-1269-344f-9cac-f80bfdc24d0d | -2.90706 | -54.0976 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5c8c195-bba6-34ef-9729-71786148e150 | -11.18395 | -44.83966 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0bcf6456-84b3-30ae-bf16-100fdec022ea | -3.37795 | -50.94484 | 2026-09-30 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc8e394c-8dd8-3ea6-8ccb-cce25f0ffd19 | -11.3934 | -43.4739 | 2026-09-30 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b904b395-16dd-31de-b01e-beb71ea1cbde | -9.60534 | -51.58448 | 2026-09-30 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3538518b-12d9-30ef-9014-3c84ebb228cc | -11.16621 | -44.81932 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b31f2052-984d-331e-bc0a-31a96aa71499 | -8.83875 | -49.70373 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f812b7e3-e38a-31db-8aa6-4ebb63051fee | -5.76264 | -45.17311 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35224b3c-3811-36aa-998a-568d827c44d2 | -8.11495 | -54.85145 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf5333c8-a96f-37b3-a414-8c023ae82e36 | -10.71784 | -44.42481 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b46cc1d0-12ec-36dc-afb0-19ff42fd9e71 | -14.53335 | -48.29305 | 2026-09-30 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b70275e5-e201-308c-bf0c-da1ce12005c7 | -10.71209 | -47.83193 | 2026-09-30 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33cdd994-24ed-3c6c-aeba-475a5cf07c14 | -13.55982 | -53.20715 | 2026-09-30 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79b5c4b2-d338-3ad3-8cf7-6a92b8534fa9 | -3.70876 | -54.22984 | 2026-09-30 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7322f48f-3b7d-3a70-83a6-35d53fae6181 | -4.48273 | -43.65471 | 2026-09-30 04:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ea8bcf6-a9ff-37c5-801b-06f8f24daab4 | -5.74287 | -45.16702 | 2026-09-30 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| acba7bd2-34a3-3682-b02d-5e91870838a3 | -7.54757 | -55.04124 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db367d6c-6a2b-3e6a-be2b-638f777cc2e7 | -7.02131 | -44.61898 | 2026-09-30 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b877b3fc-5096-3da2-8597-5042c37e6ae1 | -4.36175 | -47.77479 | 2026-09-30 04:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5d62b3ab-9a09-3379-acec-51739b2dd413 | -8.71857 | -50.07779 | 2026-09-30 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d77c5ac2-5cee-3a95-af6f-d46bfe4737e2 | -10.64692 | -50.71759 | 2026-09-30 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 763aff66-fe2f-393e-a228-c1374527b7c5 | -6.71023 | -45.63247 | 2026-09-30 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 026f2a5a-24bd-379a-8936-2e1d082562ee | -6.37902 | -55.14075 | 2026-09-30 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eef4693d-ceca-398b-abed-aa1527055460 | -11.17922 | -44.83896 | 2026-09-30 04:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f0c9b56d-8112-3205-ba0d-2bbb60c44716 | -5.09277 | -49.06249 | 2026-09-30 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73f5772f-3b9a-32ad-bd31-490046c259d5 | -7.92821 | -47.37688 | 2026-09-30 04:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README48.md)
