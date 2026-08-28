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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9039aee3-4cf9-3051-970f-e3494b07f6a7 | -6.2596 | -55.39255 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7c0240cc-6b18-3c75-828d-4acee959a96b | -7.57634 | -61.31548 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6f41ad74-60f1-3614-a659-f823e71869e3 | -7.00896 | -59.57544 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f67e445b-6863-3ba9-afae-e19b5ccd6852 | -6.62934 | -53.18206 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c7ceeaa3-ffd7-36e0-b901-1f5bc384c130 | -6.38456 | -65.23592 | 2026-08-28 17:28:00 | NPP-375 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 045853c4-7aa6-30c8-a3da-789262c2c9aa | -10.27145 | -64.50443 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 36799ceb-267b-399c-abfa-d760bec5c717 | -6.62185 | -53.18325 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8dd53a87-a60a-3462-9c2d-82f414c0435d | -7.61843 | -61.35577 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 1bcd7f3b-9536-37f9-8a63-cc43ff3847f0 | -6.59313 | -55.42901 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 34e09782-15c3-3a1e-bae6-10866361eeb8 | -7.34946 | -55.17749 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| deb979d7-469e-37eb-9947-e97bd66e17eb | -6.26189 | -55.40714 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| bc8d8545-55d6-3960-bd46-398c6c30e6a5 | -5.99454 | -57.68348 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3398a61f-3ba6-3919-8b92-d507d1f507e1 | -4.60896 | -54.87001 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3d8e3c69-be7a-36df-8739-562bb730b1ef | -6.77366 | -59.44289 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 116d439b-325d-33c3-9477-dc80ef1b9360 | -3.73959 | -57.23527 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e66b3b6f-11c1-3448-8f6a-4337d6f8ceda | -10.07741 | -68.55382 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 15f001cb-5503-3e69-8607-d294ca2f63e5 | -6.2361 | -53.47961 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c4792704-8421-399c-9a6d-c6ff6d786f2d | -7.66509 | -64.6474 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 06711618-b9f1-3562-bde1-e3fe15cc93f5 | -7.10077 | -55.48121 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 8e032e5c-27b1-3238-a055-7dda499c0f5b | -6.04049 | -58.05441 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73814e50-4939-35e8-a1c4-9c7c4a66736a | -5.89881 | -57.7665 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee56bef7-e6a4-3e26-84f9-0f2c9f599622 | -6.69031 | -56.35388 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| a63025ad-3ac2-3fed-badd-c09b679abba0 | -8.87983 | -66.90605 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 32bf628a-abf6-3beb-b2d8-558984daed7e | -7.49109 | -55.28225 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 20fdfe15-f5d9-3307-923f-bc59ce53b4d8 | -8.77795 | -50.0792 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ff9e9f17-3c39-3fcb-8b0d-3ac009f11618 | -8.94685 | -50.79184 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2ffabf69-7e44-3823-ab2e-b08a22dca19d | -6.00739 | -57.83571 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 77d03a74-9e69-3068-ac99-ad70765dada5 | -7.93157 | -70.66849 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 803a0b01-7c0f-3096-bd2e-22eaae412541 | -6.82338 | -55.60659 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 586cdf7a-4ca4-3083-8bd3-37a18a671f55 | -9.42891 | -51.59277 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c1ce4494-9e6a-3463-a093-a05d24110648 | -9.06502 | -65.40915 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ff67811f-65af-3119-80be-cba401467936 | -8.79609 | -50.49641 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 06f28c87-fb48-3680-a50e-19087f25335f | -8.79488 | -49.99151 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 7269df66-bdbd-3735-8f29-ad05ab6b2785 | -8.87877 | -66.89778 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3a9a1252-b76e-3014-8e33-c3dbf996ed60 | -6.75569 | -58.73427 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 6a18c944-7b36-32c0-a38d-855e815d3d5f | -2.81231 | -43.82578 | 2026-08-28 17:28:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 308d70fe-55a9-3363-b0d4-6e2e2ced5b5e | -9.21173 | -65.79565 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9a42066-6a8c-3709-b846-1df10ed38ea4 | -3.73906 | -57.2318 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0ee5dd27-7191-3473-9277-a7611322b302 | -7.34776 | -55.16659 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bf3d6b32-2303-345a-ba14-5877141f8c5e | -6.5988 | -55.44302 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e216fafe-2522-3740-a639-9e8e487397ee | -8.04522 | -45.86227 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 02a02412-56da-3109-9f02-33716c9b7499 | -5.92163 | -61.39503 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 02b7e05b-fbff-3eb6-86d5-3809a2458d2b | -8.57021 | -54.8163 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 24a9b1d6-b255-3a33-b2ee-02f67a83b286 | -6.77932 | -55.68402 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 69e1769e-250b-3923-aa80-471b4dd3cb47 | -6.86478 | -56.52565 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 091cc8c9-c3e4-3c2d-830f-5b38b6cc659e | -4.10094 | -60.66297 | 2026-08-28 17:28:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 536eb75c-13dc-318e-9ac5-3edd322100f1 | -7.60291 | -61.33215 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8d1e375c-1486-3b2f-8ddd-51817e414716 | -9.4141 | -50.43683 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 337944b3-43a0-3c6d-bb67-a60cc2079f07 | -7.36195 | -55.19059 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 531f86e5-f8f2-3c8d-b451-0659c47d7027 | -7.45352 | -50.9315 | 2026-08-28 17:28:00 | NPP-375 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b860221c-71a3-3327-97cd-f9435ab4d810 | -5.89441 | -57.76001 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 7255ec10-bfda-36e7-9653-6741b5aef114 | -9.9264 | -60.44183 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 84ace2f9-c844-3ddb-a276-931fd5bce0d1 | -6.42073 | -54.77055 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 853def03-7cea-3e37-ab6f-62c64cd40191 | -8.82792 | -49.6034 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e18defd2-1a21-322d-aa83-1cc1818af42e | -8.31863 | -47.6284 | 2026-08-28 17:28:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a867d868-cc22-39f6-a1f0-f6ba3930da73 | -9.22614 | -51.52752 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6180a086-cdd5-351f-bd3d-496832042207 | -8.24825 | -70.09223 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 792f68bf-9857-3662-91b9-4fac3d359f06 | -4.31672 | -59.47408 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cedd8863-59ee-30a6-b047-617831d9e21c | -5.84886 | -57.7526 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a56e6d82-d15f-300d-ad55-34910d881dd4 | -7.47784 | -61.4095 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a5379514-f8e7-37dd-be4a-4e678da22ec8 | -7.51136 | -61.38922 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 13d84ded-f0ad-3eb8-af72-f1b066ba7e8f | -5.58048 | -47.45446 | 2026-08-28 17:28:00 | NPP-375 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f99169a3-cb9d-3dc0-a36d-34f8c54320a6 | -7.49899 | -55.2884 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7c3c97fd-13b3-3699-942e-ec626183a87b | -7.50643 | -55.28685 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 672edd43-8024-363d-8ab0-e61712843037 | -9.69364 | -65.09971 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0eedec14-8112-3629-af86-99b99ca74394 | -5.81516 | -43.79461 | 2026-08-28 17:28:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 61458450-3b1d-3984-bd08-133534b3417d | -6.95836 | -56.52109 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29c26ebf-8262-34ac-b636-487f47b29670 | -6.84019 | -59.9457 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 35d320cd-b166-36e7-b0c8-e7f52a7e2987 | -4.47537 | -55.40369 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 6b22a94a-4ced-35e7-9c48-1e63098ac906 | -9.69322 | -65.09647 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 20bd40fd-d26a-3b6a-b6c4-938d50885779 | -9.87739 | -60.25898 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f6e3d618-0dc5-3e42-8ebf-f0559b2093a2 | -6.86757 | -56.52164 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2027bdcf-c2c8-3989-9313-21411440483c | -8.01749 | -48.01474 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a93372c7-8e30-3567-8512-420f6c7107a6 | -8.43106 | -70.72052 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 884df080-4538-3d8c-af35-4b5c7b2e3409 | -6.16616 | -57.79594 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 107a058c-320b-3980-b22d-5ad33e2c79cb | -6.38373 | -65.23864 | 2026-08-28 17:28:00 | NPP-375 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 662ca02d-9e8b-39d7-ac44-394cf1be2dd8 | -8.93576 | -62.40487 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 24f7ed4d-077d-366d-bc9a-2a04cd7c8054 | -8.0236 | -51.81176 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6ba8f39c-129f-3f7f-a81c-cac8e0dda85d | -6.25413 | -53.36954 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6443bcc1-066d-3b43-9ed7-4018bd369740 | -7.44178 | -65.42382 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| bfff9619-daa5-3df5-832b-07df7471bc7b | -10.08468 | -68.55873 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 86803881-1362-39fc-a89b-6d7a61988271 | -8.00837 | -51.80643 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0faed089-da39-3ac5-b1ea-aa1953059a23 | -6.41038 | -51.69179 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5672ad18-05f1-34ad-a87e-4cfdfb8d1cf6 | -4.90165 | -56.26339 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 77ed2cd2-c704-3229-98f5-24a027b23b83 | -6.43059 | -55.52892 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c8824e7e-8a4a-339a-b0b9-5c94ef5cc0f0 | -8.02098 | -48.01508 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 596e24d2-a8d9-3448-bb55-999ef5ac212b | -8.67104 | -49.53816 | 2026-08-28 17:28:00 | NPP-375 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 566e7183-393d-351f-8112-d29ce3aaa4c7 | -8.95296 | -69.46527 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0c4d6c6f-75da-3efd-ada0-31fe2b655abc | -6.65555 | -56.4165 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05d37de6-c172-3bd3-b667-c3578a267b56 | -8.21721 | -70.50189 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 1d62d846-d776-35da-b94b-c6f194c2f2a6 | -8.60098 | -54.83419 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| f395f5b4-3e04-36b5-9676-b357fd16a99e | -6.6256 | -53.18266 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4c3abc54-dac3-3b45-bbb5-6756b6c53c80 | -8.60486 | -54.79193 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 314bfa89-4a72-3daf-8075-aad1a6366877 | -4.92984 | -55.77037 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bac82ffc-f91d-3995-abea-b0ecce9664e8 | -6.95586 | -59.4852 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| d78522ec-f9c4-31eb-a1a4-6f42fea79d22 | -8.79709 | -50.03655 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7606beec-ff7d-3dcf-8a45-c903b45457d8 | -10.39251 | -61.2395 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4fa2a4e1-2117-34f8-9765-8019c9452fa2 | -8.3368 | -45.73103 | 2026-08-28 17:28:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 967db06b-aefc-3fc5-9fd5-1ae541e73161 | -5.81951 | -52.3181 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 73e16867-5413-3310-9fbe-b6e1abae5f65 | -7.92426 | -70.66912 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 32.9 |


[Clique aqui para ver as próximas entradas](README127.md)
