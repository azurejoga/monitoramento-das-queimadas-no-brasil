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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4a4f5a8-4bd4-31ae-8031-9d7714b21541 | -8.92669 | -45.46502 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 216e63f0-40e4-3c5c-bf8c-ca3ebe3f4229 | -8.65885 | -46.35064 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39eab8aa-24e3-3f0c-a52d-1acfc955b5b0 | -8.59502 | -46.34388 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40149bf1-5377-3fb0-bd17-d097621be1ec | -7.25759 | -44.59642 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3050c286-e8c4-32fd-8313-c95621f11494 | -7.62889 | -46.54905 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12a4c9f7-f604-306d-9755-ffa129001994 | -5.52786 | -45.32999 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94abb427-51bb-3117-af94-0c814e93ccbe | -9.09636 | -44.84791 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 3c278754-eebc-36b4-88f1-dc3d3ac6672a | -5.76737 | -43.9665 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27c14662-34a0-3bc6-af80-252ce3b80a25 | -12.10251 | -44.82758 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d0fd1f9-0d92-3839-a722-187d48f1b5a7 | -11.35482 | -47.36286 | 2025-09-16 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4f5f89b-170a-31a4-a6e6-5f9a6173015e | -5.90127 | -49.09957 | 2025-09-16 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce995b93-2db8-37ca-8519-1731b88c5d9a | -6.96653 | -44.44516 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b00432ca-3479-35cd-b139-2c9651253bd8 | -10.63046 | -44.2189 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39bdb901-883e-3c5c-8692-bf2dc463a3db | -10.7278 | -44.75368 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 569cc188-4ad6-3dbf-9f1c-ad2e368118e3 | -10.15024 | -46.14445 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75058e9c-6d8c-37db-a1e9-94f404aaf010 | -5.79571 | -45.93368 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1333e9b7-7372-3e23-ae5b-967310b51215 | -8.98633 | -45.75624 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 199f459c-1dc8-3b55-a56c-79cd6a753a30 | -10.79917 | -50.68466 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd0f7419-08a0-399c-a07e-1bb39286d120 | -12.1069 | -44.82377 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 649e4d3c-1d95-3319-8c8d-4658d8fa147a | -6.34437 | -44.76439 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc5dfda0-fd4b-35e5-8a68-c97d7ce20f6e | -11.60221 | -46.96836 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20d6f326-0282-353c-83ec-ac3eff1d3f25 | -5.42115 | -43.19131 | 2025-09-16 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72b153b9-80cf-3b14-bcf7-ef7d35b8cee3 | -7.69227 | -44.66138 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a95d80f-08dd-386e-9ad5-538d6eb15b38 | -6.26229 | -43.46881 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5dc61d08-1571-3d03-ae97-3789153febc6 | -5.80333 | -44.86298 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f76c23f-3591-37b7-b4a4-fc0259ff0918 | -9.09259 | -44.84711 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e01f25d-6b75-307b-9854-00e5d4a27c7c | -11.07767 | -49.75346 | 2025-09-16 04:02:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 920e54fe-982a-353e-b1b5-ec4fc0b156d8 | -8.10093 | -50.15872 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2758872c-8a4a-351c-ad7a-acdb78931e10 | -6.26524 | -43.47364 | 2025-09-16 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19b250d3-fdb0-3991-85ce-ebc708b2ca87 | -11.50389 | -43.70744 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12459fb4-d984-386e-8e32-77c3cb2d56f2 | -7.71074 | -49.55899 | 2025-09-16 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3468281f-78d2-3689-9d98-48e14cb85663 | -10.74479 | -44.76552 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 81112dfa-47a0-3a1e-8b62-64f7b2b82f03 | -7.55721 | -50.45509 | 2025-09-16 04:02:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4eb0069a-155b-32af-a26e-afd90b40d72d | -10.71251 | -44.73944 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed4ca577-70bf-389a-adbf-96b27083fb12 | -7.6885 | -44.50229 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c089e14f-cf3e-3b13-9448-8f34e6fe1b96 | -7.40218 | -49.99841 | 2025-09-16 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9642a56f-a455-343a-9fad-25d8d6a8ca31 | -8.93038 | -45.51573 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22e610f0-09b1-3e37-b377-07207dc42623 | -11.44796 | -43.55758 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cb165ab-8034-3c92-abd6-57f9b4d0a859 | -5.77648 | -43.9348 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb8cc73d-bbac-30f3-819e-1fa462c3cacf | -9.04785 | -44.83678 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 11ef8005-c3d7-3695-b50c-0884c9ce1b99 | -11.71534 | -46.87083 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0daa45dc-ae7b-3d82-9086-321fff3b7bc4 | -5.78107 | -45.88972 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8da2151-0d00-3b7a-ada5-f121fcbd50ee | -7.16487 | -44.35413 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79555939-f83a-3d98-81a5-c6129c266715 | -12.11127 | -44.82001 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3363c22-0c25-3f5a-8a4c-39a2db285413 | -7.98401 | -45.64706 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e12e9d00-022f-34a2-923a-4f0acc13bae2 | -6.62388 | -44.73003 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56840625-a411-3902-9c7a-d97652d08c54 | -5.25301 | -44.14539 | 2025-09-16 04:02:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 36a2be46-9575-3c46-aac3-a56a662cee05 | -11.0771 | -49.75648 | 2025-09-16 04:02:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efd7076f-ef23-321a-a7ac-4e75f006976f | -8.4187 | -45.74786 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5240239e-1ef6-3977-8456-f7c844b0f9db | -9.86352 | -46.45183 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fb8f52a-f6f7-3119-9cf3-ddd23752c728 | -10.6525 | -46.45753 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 466eb92b-5367-3323-85ab-85b0a3dbcae4 | -6.12721 | -42.94441 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a5e9e284-3b8c-3f66-bfa3-093a9793deba | -10.79453 | -45.97779 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e9dae38-b63a-3613-94f3-3efc03b49b3b | -10.64076 | -46.45852 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cc52cce-9cd2-36c1-9599-42f1f8a52b95 | -5.98442 | -45.84273 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49876257-a2d9-3d7f-a526-dd594112c967 | -10.7225 | -44.76237 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c85c74f1-4a24-3832-84e0-845fe7b67d6a | -8.3934 | -47.25868 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2245b1d-7b86-37cd-822e-1f987b49a923 | -10.64683 | -46.2277 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 414fad8c-09cf-3caf-a8ee-9da3a89eab21 | -12.11908 | -44.84242 | 2025-09-16 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd35b733-c809-33f5-b7d3-8086f5c85f15 | -5.81274 | -43.48748 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 516e4064-4e2b-30b0-9d83-41f423696c2e | -11.71041 | -46.8745 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 20fff6da-2a6e-32c5-934a-da6f7a86a228 | -11.45551 | -43.55492 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b14ffa6-07c6-310d-9b83-e175f5ba40e8 | -12.0557 | -46.53471 | 2025-09-16 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a365168-6352-3151-bb5e-f6d1e9bf5f20 | -5.761 | -43.69186 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c99d7369-63f7-3725-acc4-65362567d582 | -6.49876 | -38.87136 | 2025-09-16 04:02:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9579d35c-797b-3b94-8601-348a6827560d | -12.11633 | -44.83465 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7d348c7-a110-3da2-924f-09df2c0bcc9a | -7.13449 | -47.97485 | 2025-09-16 04:02:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94803444-de06-3c8f-8661-a8836a8d00fa | -8.76188 | -48.80506 | 2025-09-16 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a7b26b9-cca3-37b7-a30c-011da35cb814 | -7.90484 | -46.23373 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8aefb756-c96b-3c73-9ed9-750ccfc94654 | -7.89993 | -46.23701 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87e7f168-082a-3736-a51f-f31c4228b781 | -8.98113 | -46.24921 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 41e660c5-222c-3005-97d7-e6d61806ee94 | -12.10616 | -44.82818 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ea62ea1-d3ac-392d-8fbc-cafad0c03141 | -9.05165 | -44.83743 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f91adb4-399e-32d7-9e12-917f53855654 | -11.44114 | -46.94634 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f0d6be65-190d-3dd8-9141-a18b72d2e3c2 | -7.31001 | -43.92377 | 2025-09-16 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c023f47a-5cc8-38f1-8fc3-216d8ad13d31 | -12.11559 | -44.83908 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 040b7d2e-b309-38e4-8d93-431a0c5e7b59 | -8.03487 | -49.83377 | 2025-09-16 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5364a17a-08c8-3ba2-9fff-d27f2ee6d60b | -5.79141 | -45.93305 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f27f9d26-ce35-38cd-b31f-41f590f9a2d7 | -12.00562 | -46.65052 | 2025-09-16 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f44740c1-13a1-3e2f-9b11-86bd3a600555 | -7.22822 | -43.96697 | 2025-09-16 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34785483-a56d-3f1a-ba9c-3e5b426f7939 | -7.43706 | -46.17401 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6df8271d-9c4e-36f3-a330-5720e7b76fca | -6.45227 | -43.31483 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5fb36e8e-7f44-3649-bcb8-1108d4d8dd85 | -8.60508 | -45.73557 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 01d7f695-050b-37b8-8fe1-b7ebfca09086 | -6.17101 | -41.22918 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 43206f14-34a6-34ad-9137-0155f4c8409b | -10.72036 | -44.7527 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f3720886-8715-37f7-a225-5e1b137fa5c8 | -10.71665 | -44.75211 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b1d1f533-8752-3b13-98f7-3c162519c836 | -7.0362 | -44.14589 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9f2bece-9963-365e-a800-66f17214b21a | -8.00182 | -45.66517 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae862b78-8f6a-368b-9a6d-68ee03680fab | -7.19819 | -48.60486 | 2025-09-16 04:02:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbacb73d-45aa-381e-aaf2-51a2a9305ed9 | -10.63696 | -48.74666 | 2025-09-16 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36cfa744-8015-3c5d-9370-4ce0e7e17c37 | -11.43207 | -46.92494 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c0cb0be-907f-36a0-bb52-a2bd22ccc09e | -11.99703 | -46.67583 | 2025-09-16 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95a52ee3-bf64-3d3f-b76f-715af9a9097b | -6.17659 | -41.21548 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3bb061c-1e7e-3818-b1a7-87325820f288 | -5.74259 | -43.92621 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cefcea8d-3db1-3584-8a12-a08478e313f7 | -7.68208 | -44.67491 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d8b9434-2d7e-3ee3-9c71-467ab852a545 | -10.71415 | -46.49184 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4063284a-dc89-3909-be3e-5f7c240bc298 | -7.01569 | -44.89309 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83228838-0a89-3e32-9fe7-e9ce36376b3d | -5.80673 | -44.86715 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b43f1d11-f9a8-33b2-a63e-1fdfacc32319 | -7.41323 | -42.08311 | 2025-09-16 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ceae32e2-8265-3482-82fa-7f56714348c2 | -6.45157 | -43.31913 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README13.md)
