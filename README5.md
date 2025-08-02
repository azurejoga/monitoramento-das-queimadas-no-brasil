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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f3b7e5e-0f25-324a-a9bb-e275ad099bfa | -11.7733 | -45.02011 | 2025-08-02 03:32:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee28f6cf-b87e-3ed0-94f9-fc8c94fc37c6 | -7.24073 | -43.39001 | 2025-08-02 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69d80e0f-9ebe-31ab-bbc9-d309a211ff96 | -8.03468 | -43.11761 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 126cb9a9-cb7a-36fc-b48a-c569ec10c23d | -10.04411 | -44.71747 | 2025-08-02 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1b965fd2-59d6-32fa-b97a-481250250886 | -7.87988 | -45.54187 | 2025-08-02 03:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4124cc27-6493-3bc8-86d0-34f61d96deef | -5.57212 | -43.60644 | 2025-08-02 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 90bc3fb8-76e5-3ff6-a2ca-305a736352b4 | -10.64431 | -45.2389 | 2025-08-02 03:32:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0abff95-4f57-3aaf-9f21-20729e4dd934 | -6.76643 | -36.98861 | 2025-08-02 03:32:00 | NPP-375D | VÁRZEA | PARAÍBA | Brasil | 2517100 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 96981fdf-d690-3e12-b00e-72c4811677ba | -10.4632 | -46.95185 | 2025-08-02 03:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcf9bb48-4655-3e4b-9475-45139e769b0b | -10.63785 | -45.23768 | 2025-08-02 03:32:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e8bbd3d-2ea9-3d7c-a874-8b2075e79631 | -8.04222 | -43.11007 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| bdf8a468-78f7-3e1b-8fe3-f5e7528b580f | -10.63891 | -45.23236 | 2025-08-02 03:32:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96dcf816-add0-3f81-80d7-c24c8fb724df | -9.05315 | -45.06869 | 2025-08-02 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f08ef05-8d63-3d51-9562-67a6d05e84ce | -9.19799 | -45.29451 | 2025-08-02 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8744f11f-3c6f-30dc-97f9-c1fd2a802358 | -8.04893 | -43.10689 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 5f4778ad-efa1-3b3c-8b32-035e36b9997e | -6.79198 | -42.98608 | 2025-08-02 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| aff3d294-341a-3a60-91ef-01f3141f78bd | -7.27125 | -43.39561 | 2025-08-02 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 61bd16b9-b290-3fd1-b981-06b511741fb8 | -6.52072 | -42.81462 | 2025-08-02 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1ac7d27c-14ff-3fdd-9c69-9acd49df98d9 | -6.6937 | -43.07715 | 2025-08-02 03:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f5dc9cc-4a60-390e-ba6b-6c6d812ac45f | -10.03938 | -44.71736 | 2025-08-02 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c07d05da-4f60-3fcf-99bd-9c5737f51ac2 | -9.38826 | -45.50196 | 2025-08-02 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d8de1b66-f64c-3707-ad32-753cc5e3cc23 | -5.57079 | -43.60566 | 2025-08-02 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5530b84c-551c-3ef4-a6c0-743435998d1a | -8.03307 | -43.12626 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 767c3e33-8257-3ce1-9bc8-acbefd279b9b | -8.03388 | -43.12194 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 99e56c94-a707-3b22-853a-1ba430e41986 | -8.6679 | -36.23116 | 2025-08-02 03:32:00 | NPP-375D | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8fac9ea0-0ba1-3d1a-be5d-a8ea5d51138e | -10.5828 | -45.27744 | 2025-08-02 03:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc284303-c574-31f7-b7c6-97239ac34cf3 | -5.48243 | -42.16143 | 2025-08-02 03:32:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3cb7b7b1-0ec6-3a58-9360-d748c1255dbd | -7.88105 | -45.53566 | 2025-08-02 03:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd5d3562-e371-3f91-9462-30dc27828721 | -8.03226 | -43.13058 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 172d82dd-b6f4-35eb-8a88-a8ab632778dd | -10.58478 | -45.27221 | 2025-08-02 03:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 009349f0-2a5d-3e74-9d51-6a61572031e0 | -6.78601 | -42.98488 | 2025-08-02 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 302749a4-58ce-3edc-b182-e66498190d85 | -10.03309 | -44.716 | 2025-08-02 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dd91277a-de68-36b4-82be-4bfff4974aa3 | -6.69973 | -43.07832 | 2025-08-02 03:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e626a423-1a87-3e24-8ecb-65ae0de4d5e2 | -5.57305 | -43.60134 | 2025-08-02 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 74317dca-4898-3328-a028-87e3a1feaf1e | -8.02226 | -43.15123 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 1dcaa626-787b-378c-a6e1-62a67a4daa75 | -10.64538 | -45.23352 | 2025-08-02 03:32:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 687ead31-d255-33ab-a336-3369e2f14807 | -10.04038 | -44.71239 | 2025-08-02 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6e8f3f95-364e-3828-9b30-bc7969bcb825 | -6.70089 | -43.07542 | 2025-08-02 03:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2675b28-51c7-3d12-8777-c26333e8afd1 | -9.06182 | -45.05918 | 2025-08-02 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35adc3c7-171d-3083-9a77-0ff512e036a0 | -10.02524 | -44.71334 | 2025-08-02 03:32:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cddd8a2c-f49b-3956-a553-336ac84cf826 | -9.19453 | -45.29735 | 2025-08-02 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dc7e3950-a86b-3a6e-bc13-830dabfe3d1e | -9.06843 | -45.06013 | 2025-08-02 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8374949c-dd75-3ccb-847c-2abc860b0abd | -8.02471 | -43.13814 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 38c77bc5-ebe9-3311-98a3-3862717bb8b1 | -8.05564 | -43.1037 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 04f10f58-0f9e-374e-8b14-0512c923ee7a | -8.02552 | -43.13382 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| beb68915-910e-39c1-98d7-d1af094d877f | -8.02983 | -43.14361 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| b92313e0-b30a-3306-9358-af167de8fa04 | -8.03145 | -43.13491 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f1e56dd2-a7ab-3618-8aad-4d82b97e2d14 | -11.78067 | -45.01574 | 2025-08-02 03:32:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5348f959-4cb4-3ea8-b55f-130b0cc19ca0 | -5.57168 | -43.60057 | 2025-08-02 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2fff81ef-083b-3243-97e4-ffbfdc1e24a3 | -5.56487 | -43.61021 | 2025-08-02 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8966fe59-8a65-3d2b-ab44-c580bc18db93 | -8.0239 | -43.14249 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 2e447179-42a6-33c5-a7ad-e4dc0705750f | -5.56988 | -43.61085 | 2025-08-02 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 279cbedb-198e-3c07-8560-7b3588a6cdcd | -4.77491 | -45.33968 | 2025-08-02 03:32:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db2be2e8-ccc2-31ef-9d62-dd11fe0f5a3a | -10.58388 | -45.27215 | 2025-08-02 03:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9905866d-bde3-3400-bf90-7df327f1e03d | -6.88538 | -40.88081 | 2025-08-02 03:32:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4aac42fa-611a-359e-99ac-6fa2853d76d7 | -8.02714 | -43.12516 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 0cbbd00f-aeca-3608-952c-96058947e8c6 | -9.18793 | -45.29593 | 2025-08-02 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b2b5ff9e-40fa-3437-8cd1-a4b7c1cc13c2 | -6.36418 | -36.90613 | 2025-08-02 03:32:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1be95df2-fe08-3dbf-9107-fa03b21f998f | -9.19037 | -45.29838 | 2025-08-02 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fd68f1dd-214e-39d6-83f7-f7697b115535 | -8.03064 | -43.13926 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 26d84b2b-c26f-3d5d-8258-5b07a6ffd771 | -10.59333 | -45.26289 | 2025-08-02 03:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9376de8b-1a16-389d-bae0-237c97d12d98 | -9.04755 | -45.06259 | 2025-08-02 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c813db1c-a46c-3262-b352-b7882750ddce | -5.56582 | -43.60502 | 2025-08-02 03:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 20f95c17-80c6-3914-b3f6-ccf21afc60ad | -7.87395 | -45.53542 | 2025-08-02 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c42799f-cabe-3b02-8a38-bebf5cc8e1ee | -5.64852 | -42.5966 | 2025-08-02 03:32:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9059b2b1-551e-37fc-8566-9b4c66ee3231 | -7.87299 | -45.54068 | 2025-08-02 03:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 680e3773-e35a-3c0c-8460-90b8665878b5 | -9.39488 | -45.50359 | 2025-08-02 03:32:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bf0b9805-28b4-30f2-b80c-b48647867542 | -6.88338 | -38.9846 | 2025-08-02 03:32:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6dcdffde-cf91-377f-a4fd-9921fd9938c1 | -6.52747 | -42.81124 | 2025-08-02 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9f4d7be4-540d-3989-a4af-3c6c5a311522 | -6.69456 | -43.07236 | 2025-08-02 03:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a88d9914-8e6a-330c-9456-ba3347ecdded | -9.19564 | -45.29174 | 2025-08-02 03:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 37835c22-b5cb-3f50-b7c2-71a7f7e46905 | -10.58375 | -45.27745 | 2025-08-02 03:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71afbf22-5edc-3d9f-ba02-b61f13af2e43 | -6.52587 | -42.82023 | 2025-08-02 03:32:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a6e51112-d11b-3140-b9ae-cffa83346938 | -6.70056 | -43.07368 | 2025-08-02 03:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20720bf6-094e-3fb5-bf6c-b9c1223804b2 | -8.02795 | -43.12085 | 2025-08-02 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| cb3dfb95-78f6-3c13-b982-91ad286cbabb | -7.87417 | -45.53444 | 2025-08-02 03:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61b66de3-0e01-319b-ae9f-20636bd736de | -12.65521 | -44.49628 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e976c6e1-5cc3-3725-a93a-a5f1320fe01a | -12.66073 | -44.53924 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21a0e2f7-fe3e-3ded-b0f0-34e716a28e8b | -12.66887 | -44.48991 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 18e9d78e-4e92-30f7-a7c9-f00d3e5befd9 | -18.53021 | -49.49744 | 2025-08-02 03:34:00 | NPP-375D | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 08a20ad5-711e-397c-8725-702b4b42ba8e | -12.67358 | -44.53718 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f77bb70-ad8e-30b1-a214-ce041752642e | -18.21208 | -44.70908 | 2025-08-02 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0f2947c-32a9-3db7-96f4-2af6aa58dbb8 | -12.67895 | -44.50154 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a51e975-e1f6-36d0-949a-9541e2f67ed7 | -18.77211 | -40.91352 | 2025-08-02 03:34:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 30a84deb-3479-3144-9a7c-9cd0c3dc10d5 | -12.0319 | -44.01955 | 2025-08-02 03:34:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62d48b1d-117e-3e12-b6ce-0ed450e4459c | -12.6709 | -44.48979 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9e4e600b-9092-3e88-b35c-7bec064a59d0 | -12.44673 | -47.05198 | 2025-08-02 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0ed6789-0dcd-3144-8b81-0cabb5de71cc | -12.67498 | -44.50009 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8bd7bc05-c13e-3d40-92e0-7db9d6b69fd5 | -12.65252 | -44.50975 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 62cb4af2-f66b-3968-9593-11cb32709b52 | -16.69159 | -41.01399 | 2025-08-02 03:34:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d3f24c57-6294-3b28-9f03-e89b576c28c5 | -12.65486 | -44.52921 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d15b50f-a69a-372e-a583-6b8394b63912 | -12.67132 | -44.51795 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7060aa54-41e1-3fc4-b614-d00fe7bee998 | -18.24261 | -45.17187 | 2025-08-02 03:34:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9dfd01f0-4143-3e82-940e-dd9de297e331 | -12.65936 | -44.50657 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f549c6c9-8531-3b05-9e35-2f5dbd7b1a9f | -12.67302 | -44.50024 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8897ca03-29ba-34cb-80a0-46048edb3a12 | -12.67955 | -44.53842 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be995d9e-d26f-364d-80f5-e8580835a1c4 | -12.66629 | -44.5122 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 40a322b8-ae7c-391d-b7cb-1ffc062f31d5 | -18.23911 | -45.17419 | 2025-08-02 03:34:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbe47b6a-823e-3682-bebc-a3d6619d369e | -12.65626 | -44.50064 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9a2d2ab8-98a1-37a9-9795-2a5c887ca60f | -12.53432 | -44.72327 | 2025-08-02 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README6.md)
