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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 640ef488-af0b-3335-b735-afb5d70735f2 | -11.48315 | -49.74984 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 54cddaa2-4ea8-3233-8b84-ed1abaa611ca | -10.80671 | -48.72906 | 2026-09-28 17:09:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0fd4d3d4-a539-3027-bc8e-f8ba03913bf8 | -11.10733 | -51.17553 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 60fb1fe8-7777-316d-b504-0a482e9d1a55 | -8.51019 | -46.89428 | 2026-09-28 17:09:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bbbc08ad-a861-34c6-ad4e-b30954781325 | -8.92006 | -66.86999 | 2026-09-28 17:09:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a18834e0-2ccf-383e-bec1-05a18f247047 | -9.76683 | -44.84172 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d3e2b056-a9be-3356-886c-2d5a1c4b0bf4 | -8.00812 | -43.73756 | 2026-09-28 17:09:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 708fd6f8-d0c5-31cc-b25c-ea56e3b6b428 | -9.50678 | -46.35455 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4fd8312d-5ded-3d13-92bf-ccf33db58cf6 | -11.57567 | -47.39343 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 693c43b8-d5af-30ea-bfc1-ca365f8cb644 | -7.27771 | -55.57224 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 96255f5f-f7c0-3a8d-938f-4655ebc921ac | -10.86451 | -53.95386 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2bb216b6-a6cd-3f92-bdfa-8f325ffe9781 | -10.69093 | -60.72246 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db8645b4-caa4-36a6-8bca-db81a037f7ca | -8.26686 | -54.74813 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| bfd54a0e-184e-3804-b886-cb4c4d6ae312 | -10.2683 | -44.63404 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 312f880c-7b10-377a-bfd5-f08f65d74102 | -8.23927 | -54.6563 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7e80bb40-a287-3935-9fbc-59c7eaf6a110 | -10.92126 | -50.6678 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0c6ecbf4-ec72-3a01-9891-c735abdd8f44 | -10.96362 | -50.66982 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a83e77b8-3818-3f6c-811d-f19e11d8c3ec | -9.36001 | -46.82277 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 00a85a67-106f-3fcd-92e9-06a95121a301 | -11.57936 | -45.4635 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 8d3878fe-5f34-3c4f-85fc-eb6ec7e070cd | -10.68382 | -44.45318 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c54c730e-8b34-3c23-a2cb-a60158652eb7 | -10.28629 | -49.96408 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 016bca47-f872-3b12-a1cb-e26e0f54bb44 | -11.75602 | -50.76292 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| f35b9377-1f09-31e1-99d0-f594839043f8 | -10.75477 | -61.49324 | 2026-09-28 17:09:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 23358a0a-5663-3cfa-8538-fab21783c886 | -6.14241 | -53.12609 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 405a5ea8-1df5-32ea-a35d-4fa6dab7b8d6 | -7.68364 | -44.88043 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5c8841f1-33bf-3b9b-9368-33ee664916b2 | -7.01058 | -45.30579 | 2026-09-28 17:09:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 970369e9-587d-38a7-9ee1-f248e67637d9 | -7.05834 | -42.88115 | 2026-09-28 17:09:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| b1236935-5996-3110-a105-ac7594cce6aa | -11.3434 | -54.03763 | 2026-09-28 17:09:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a25d7d19-5ded-32f5-83a0-753b4a7bce16 | -12.06138 | -48.53433 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 2da65c90-28bc-3132-a726-803b2ef27f00 | -10.22195 | -50.0143 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| db09d788-a33f-3e36-a9b6-c273aa9f8ccd | -4.25814 | -46.89201 | 2026-09-28 17:09:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ba906fa0-d711-3f47-9e2d-239898f85212 | -8.2704 | -54.7049 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 3e9fc952-2964-35a1-8426-9f0c08bca4e3 | -11.38818 | -45.39906 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7f89d084-a3b6-3bf0-92df-8a3d1f40d266 | -12.1356 | -57.24349 | 2026-09-28 17:09:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0f56f91e-ec34-389b-b0b6-6546a0b96a54 | -10.94899 | -43.89732 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.6 |
| bc286687-9262-304f-90c5-089dbfbc3e44 | -7.67379 | -44.8912 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 454f5fd7-5f06-33dd-8055-611ed47d6344 | -9.17235 | -60.78041 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9e652536-2c63-39ba-9d16-593d44091973 | -6.94961 | -41.61999 | 2026-09-28 17:09:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 54.6 |
| c8d4fa1f-b080-3739-9915-e2dbae34dd37 | -7.26984 | -45.3337 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fd88555a-c436-3a42-bcb5-3876d807a2fc | -6.67686 | -46.11757 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 28f76640-2343-3337-9f5f-efc9f88e85d5 | -11.45898 | -49.74895 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| c3215e9d-3c5d-358e-af41-30186cac57eb | -10.29529 | -48.16743 | 2026-09-28 17:09:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80ce3e86-db8d-385f-a72a-57b1495979e7 | -9.12809 | -46.45714 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85a84d43-539b-3297-8971-9f426b79a292 | -6.80655 | -44.63319 | 2026-09-28 17:09:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bac7b242-0283-326a-9ceb-a3f64f6c495c | -7.68519 | -44.88905 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| ce3d3533-9609-3a9c-ac80-7983fa64f09e | -11.23022 | -61.16528 | 2026-09-28 17:09:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f6adeaf3-5430-398c-8ae7-cadc056c68dc | -10.95316 | -43.88789 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 913a0d66-c208-354d-95c0-7bf59e2ea710 | -10.72633 | -50.48079 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 425d0ab6-dfbc-34ab-9ec3-f314da42cd39 | -9.82046 | -44.94522 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 86b28620-01b2-3649-ad2b-70e71123f7f2 | -9.77652 | -44.86275 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79bf8222-fe0c-3a53-a2c4-4732948fd159 | -9.69629 | -58.12141 | 2026-09-28 17:09:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a205b6e0-7e72-321d-9317-a999240d647d | -11.07318 | -48.8864 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a40b8d1e-dfcc-3575-bd24-c2f8126140a4 | -12.75906 | -52.81675 | 2026-09-28 17:09:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e81c6c01-94f1-3756-b349-13b0ce0bdd7b | -7.26493 | -45.3384 | 2026-09-28 17:09:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 696314f2-61d7-3fb3-81e5-a043499bc880 | -8.18676 | -54.79963 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 66930e70-def5-3e5c-bd15-b3c0ae92e47c | -11.46676 | -49.74759 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| aca9e31a-8b6d-3d9d-8945-fd38939cec0d | -8.73081 | -44.89831 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1a5ed826-e308-34ea-911a-2429864e9e38 | -9.25307 | -63.41036 | 2026-09-28 17:09:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0c3ac840-193b-3b16-bb2a-6d1f2eca92f7 | -11.1781 | -50.62723 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e5625ed6-80c9-34d3-bfa8-6699807a1017 | -11.98841 | -57.60885 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7ecab70d-25aa-334c-89af-7bb55ddbfd14 | -9.30201 | -46.4492 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e0e83c3-23df-33cc-90e9-cfca2192b810 | -6.14116 | -52.74788 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 535e9738-f899-3ef6-8c85-db85c17be8d9 | -7.36465 | -60.58166 | 2026-09-28 17:09:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 702f7941-f4fe-3ff3-b697-2215f52e37a2 | -11.08304 | -46.07736 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e0dac7f6-bd6d-35ed-9180-1142a6383782 | -11.07515 | -48.89777 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 21921e2a-3d21-35f4-98b3-c6329acff4fa | -10.8286 | -57.22105 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e67f2ea5-4c25-338d-bdf3-41dea4e94562 | -8.73314 | -44.91094 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e57e9583-e8ad-3dcf-a26c-c26fb0205b89 | -8.62316 | -46.98898 | 2026-09-28 17:09:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| c5e7a0b1-60b0-3980-9832-47b4ea2ed294 | -8.85901 | -46.59635 | 2026-09-28 17:09:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5322f077-16f6-3232-8ad4-71f49367ec89 | -4.85901 | -45.27687 | 2026-09-28 17:09:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6bf9aa4a-f47b-3d16-a56a-af9397da2f62 | -11.15531 | -48.32851 | 2026-09-28 17:09:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 86a7fff3-76e9-3c20-a76c-d85a2848b426 | -8.60027 | -54.65871 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0b7fe353-b41d-3380-a853-866cdb014201 | -6.04692 | -45.16802 | 2026-09-28 17:09:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4621cdd4-eed3-3876-abf9-33010dd3057e | -6.05255 | -53.60632 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0227baa9-e98b-3fef-af50-c6340fb464f6 | -7.69386 | -54.75761 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 83d69ea0-1f02-3fef-8fa2-dc2bd6925821 | -5.25289 | -44.93723 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b9d7f68e-1014-3c8b-9b6f-ec4d3d3c1c2b | -9.84197 | -45.21053 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e59d4540-91b4-33d5-9be7-02f26ce77db0 | -9.14693 | -49.9646 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 76f373c2-8553-3c04-9c77-d7be658e14dd | -7.52714 | -45.08036 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2fa6fe2d-f6b5-3909-816e-a5298f93d94a | -10.10801 | -43.95466 | 2026-09-28 17:09:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a8b7a64d-d59e-3c35-b50c-1e59d0a16067 | -12.06691 | -48.54131 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| a132b3f0-533d-3c9f-93be-23440f60d462 | -11.08249 | -46.07642 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47f9d171-aa24-37af-aba6-7f2ba85e4f44 | -8.6883 | -50.60696 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f9c20b90-fc2a-3c95-b0b1-06ae9029e9ae | -9.13502 | -67.93417 | 2026-09-28 17:09:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d9c4df3e-828d-39ac-9d64-f0ce8f29ae66 | -6.8393 | -52.44225 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2c4782e0-c159-30d5-af6f-1a595fd73868 | -8.11209 | -43.99964 | 2026-09-28 17:09:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 000cf202-38ca-3618-835b-e45832a40dd6 | -11.52785 | -47.39469 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 11b37794-9565-3dff-869f-8f825fd8c27e | -5.80309 | -46.09161 | 2026-09-28 17:09:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e535847d-18a6-3a23-b138-3eb2ea97aa6f | -11.38876 | -45.40224 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 411815b5-af8f-3f70-b487-b9578becda9b | -8.92905 | -45.04955 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 97142d9f-edef-34b1-af55-1baf899cbdbe | -9.65165 | -45.55074 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 11348534-f122-31d4-b8dc-370b2617b6dd | -5.88882 | -49.98347 | 2026-09-28 17:09:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 95e2038f-9374-3f9b-8b30-febcdb105603 | -9.35929 | -46.53766 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| c0fcb5c9-72d3-3d49-becf-1ebcfdab6cf3 | -8.30396 | -45.42515 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7de13cb0-53a5-3e74-9cbe-1137c28c77c2 | -7.66507 | -45.47622 | 2026-09-28 17:09:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2c7d15c9-29d2-3e06-8638-f83ac3edf19e | -10.61522 | -53.99033 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 30e2488d-8442-383e-a6d5-8ece7ab1d83e | -6.73434 | -52.32898 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fd69acd8-7e5f-308f-9a4f-9376595764b5 | -10.90982 | -44.65286 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 42f6e703-7b2e-31a1-bb83-62a9e666095d | -10.30319 | -48.16085 | 2026-09-28 17:09:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 78579a3d-052c-3e9f-aed0-03085f893375 | -9.92804 | -60.72237 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |


[Clique aqui para ver as próximas entradas](README150.md)
