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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 638f6a21-8891-3f8e-be68-892e09395e26 | -7.07599 | -35.10065 | 2025-09-15 03:28:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| 1a3eb0dd-902b-3f0d-8f90-8acbaa7fbda2 | -5.95707 | -42.79812 | 2025-09-15 03:28:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df96a0d5-370d-36a4-84e9-a855b66149fd | -6.40928 | -42.61787 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6497092a-2dae-3174-8f5d-d619223aeaa2 | -6.40853 | -42.62212 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 245b9f03-4ee8-3290-9b34-a189cf5a31df | -6.18156 | -41.18029 | 2025-09-15 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18fd6046-70ae-346f-9e22-e7e6633d3273 | -5.84466 | -44.1711 | 2025-09-15 03:28:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea78e24e-80eb-384b-924c-e8522a36fa1e | -7.35857 | -44.3036 | 2025-09-15 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97eab83d-0bd6-3197-bb57-6d190b73e739 | -5.96071 | -42.79581 | 2025-09-15 03:28:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1b2498cd-754f-3db0-bf9e-084f69c35158 | -6.41571 | -42.60998 | 2025-09-15 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 70ca3ba5-9436-3f17-95a3-76e97ed18f47 | -14.9411 | -46.5755 | 2025-09-15 03:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 83b37f62-92bd-3677-b98e-3dac229fafce | -14.8028 | -51.6175 | 2025-09-15 03:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 640d32fb-d1fe-3ed4-a2a9-b1d112353c96 | -23.4754 | -47.37 | 2025-09-15 03:30:00 | GOES-19 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.6 |
| 083ed166-f2d6-382f-8eb3-5539d32ab83e | -12.5975 | -45.7251 | 2025-09-15 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 03c21b8a-fe1d-30af-a270-3c50a347e78c | -12.9791 | -47.9713 | 2025-09-15 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 98a316b5-bc12-35e5-8d09-11fcfc60c3b7 | -8.9787 | -45.8118 | 2025-09-15 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 35bd8523-a6d1-3752-8a29-94fc5face0c9 | -12.7879 | -47.9318 | 2025-09-15 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 3746e1cb-3602-3ee6-bf12-7dd061a9c920 | -12.9984 | -47.9685 | 2025-09-15 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 78f00c4c-a2f3-3e78-a972-abbf5416db59 | -12.60329 | -45.72935 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 29e8dae3-2b39-3cf2-b005-2eb04ebfdedd | -8.64458 | -46.36804 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed20f2ad-4dc2-3f03-ad65-390df01c241e | -12.60378 | -45.73355 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 834c209a-fbc7-3703-a10e-cdad9dab7e01 | -10.63877 | -44.21053 | 2025-09-15 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 895a1faa-3474-3597-91bd-2f40e92444fb | -7.86542 | -43.58408 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 1e792b7e-c6e3-31b9-b49b-0813d63afeb2 | -8.9079 | -45.49314 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99785bf7-b7fb-3fdc-b062-65845472539b | -7.88839 | -43.5577 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| cb6cca9b-e642-3a8c-a3a6-268662d56ad5 | -7.89056 | -43.5839 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 243.3 |
| 9d5dbd61-b320-3bad-a27f-0a7150a77a41 | -8.95696 | -45.79571 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95e5b071-dfab-3009-8b90-0a00ec0578cc | -7.49962 | -44.37647 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f19aa34-d94a-3c0d-98f0-63df93d2d6f1 | -11.33278 | -43.51914 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39d1e94f-2615-3864-8fff-8f8d56b51da2 | -8.9177 | -45.49467 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 676e338f-73ef-3a21-89a0-c2a7fafdde2e | -12.5615 | -45.64251 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f69532c0-0dd3-3aec-954c-32438674e666 | -8.80285 | -38.41469 | 2025-09-15 03:30:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ea4ccbb7-8777-3df3-89d4-92d3739fc922 | -7.8672 | -43.57473 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 1ad64d61-2382-362f-9350-6b5c5c046184 | -11.78137 | -46.66641 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af2020d0-4833-33b1-9d51-3cd9b82959ee | -12.80057 | -47.95105 | 2025-09-15 03:30:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 911157d3-02b9-380c-a715-f69795e5ecf4 | -10.93372 | -45.51007 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bfa23f10-0abb-32e7-8aca-afb070a397eb | -7.88099 | -43.6014 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d063baf-8b5d-385c-8a70-f5db1f0323ed | -12.59386 | -45.71051 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67b6f033-49d2-308a-91fa-3fc575633dc2 | -8.95818 | -45.78939 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaf96d4f-9a9c-358b-9932-5df69316c154 | -12.59856 | -45.72678 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5f2ea9b2-b1ea-378b-ad17-bb8388306c6d | -8.91776 | -45.47779 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06dd79bd-156d-3c60-8291-9652d471c71a | -7.86696 | -43.60664 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9f7cd680-ceca-33bc-ad26-ed87198024cc | -12.59803 | -45.72259 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fc1eb396-0185-383c-9302-4b452c3c30e3 | -12.59913 | -45.71722 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b869148-c726-315f-be02-4c1e5e34d16f | -7.87038 | -43.58782 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| aaeec7ce-450f-39fc-8ea7-6dffbe0785f5 | -11.76081 | -46.66278 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85c42ba4-6dc0-33d1-9a69-eeef638c8148 | -7.88252 | -43.59008 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 30cd9371-464f-3fbd-ab68-191dccf05df7 | -11.47428 | -43.598 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6086bc5b-c85a-37e3-8a47-31b9c0c68c49 | -7.99569 | -44.83133 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe52c381-781d-3831-851f-c6432b9fdfcc | -8.97973 | -45.82868 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d59c0b01-4ce3-3a5e-9e0d-e1b32b394531 | -7.86167 | -43.56683 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c625ee16-4f14-36ad-a83c-3474faeacfe5 | -7.69579 | -44.68237 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 704e2312-fbfb-3a58-a18d-45dde5d388e8 | -7.8591 | -43.58088 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2b6a946-9e72-383b-af85-0f55cbef6eff | -10.93641 | -45.49823 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0e9e2f61-746e-3a35-9f7a-19f47d35aae2 | -8.98558 | -45.76335 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7df30388-7a1c-3e00-b982-a4d623064e2a | -10.66704 | -46.24988 | 2025-09-15 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1845e6d5-b686-3ab8-a2f3-2c2d96892ae7 | -12.55518 | -45.6411 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fddcd709-8b25-3ef6-8652-c2a39492bf45 | -12.01076 | -46.66269 | 2025-09-15 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab4d9388-7899-33ea-b5fc-9049100de702 | -11.12802 | -45.31386 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c3a1b26-7b6f-3fab-8339-bc5d1202905c | -12.782 | -47.93297 | 2025-09-15 03:30:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f8bcca14-8b71-33b2-b7d8-58d49596654e | -8.60363 | -46.35308 | 2025-09-15 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9a7a416-a803-3aa0-98f1-b3a382420aab | -7.86808 | -43.57006 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bcf209c0-a334-3921-84cd-1d424ecfe638 | -11.7634 | -46.65021 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c19e5a4-a908-308c-8da4-a77eed877efc | -12.11864 | -44.83114 | 2025-09-15 03:30:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bdea00a-ed05-320c-811d-5075439c5045 | -12.00222 | -46.67448 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9d13e1d-2f45-370e-8faf-f7422b121c0f | -11.46939 | -43.59268 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f2d0bff-107c-3db9-9cd2-34e93f978866 | -8.00428 | -44.8217 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fbb3472-193d-33d0-a88d-7e6a77979c4b | -10.63279 | -44.2092 | 2025-09-15 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e02c118-c20b-3078-b4b8-fdad4e46956d | -9.23062 | -45.67795 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bc81346-7eed-3f14-b483-996a326d25e3 | -10.6379 | -44.2149 | 2025-09-15 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c154b78e-d087-3f1b-87b6-33dced7d3550 | -7.86278 | -43.59799 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 709ec6b9-b4ca-3ab9-ba8b-7da4ed4d7b1e | -7.69791 | -44.67122 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 58537bf3-f277-3f4c-84b3-6777865cecc6 | -7.87303 | -43.60777 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00d6c93e-c301-3e94-8de8-57cc21c15d0b | -10.65953 | -46.24475 | 2025-09-15 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab54ea55-9d3b-3385-9e36-9eba1f3f9905 | -8.12754 | -43.66743 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b114ac7-8389-3772-9ed1-717380adb48c | -11.84255 | -41.75775 | 2025-09-15 03:30:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 37564fc9-95dc-3d00-b0aa-28c81d9a33b8 | -7.88068 | -43.56566 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 017a97a6-6033-3894-a2b5-a2574aa2cd8d | -12.58922 | -45.70811 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0ea35ee6-4e9f-3f79-a494-e41cfdd730e5 | -7.87631 | -43.55527 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1deb0af4-abe8-3651-bf8c-68cc28f5761c | -8.97303 | -45.82681 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd15b911-e60a-37fc-aa04-3af15a15a2fb | -9.23305 | -45.66563 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4affa0c3-ed74-3cde-9ae7-71db751c283b | -8.91117 | -45.51236 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9677d576-4ead-3914-bc24-cda57774b4d3 | -7.67224 | -44.49091 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44186965-56c0-3fd0-9ba0-955409b2f546 | -7.86177 | -43.60067 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec8c9d1e-b868-3e0c-88aa-9fd66af7ea3b | -8.9669 | -46.22218 | 2025-09-15 03:30:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2c06b5bb-b5d4-3d5f-80fa-16e022d34ad6 | -12.16753 | -44.09702 | 2025-09-15 03:30:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e7e128f-dff6-3838-bfe3-eb80bf5e3ae6 | -7.86773 | -43.56798 | 2025-09-15 03:30:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 514.7 |
| c2d20218-11b7-3b5d-8ff3-15f726fbd3e8 | -11.75586 | -46.65544 | 2025-09-15 03:30:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 112580a9-ff54-3575-a17e-4013abd02033 | -7.86454 | -43.58875 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| e5664ab6-c014-371f-a67f-c17f42003803 | -7.89144 | -43.57928 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 243.3 |
| fa298e11-679b-3012-a690-3bb25b605b63 | -7.88235 | -43.5565 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| bf9a07f8-4165-3855-b3d1-830e30e39d44 | -11.33447 | -43.51799 | 2025-09-15 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62d26610-ec8f-3da9-bf0c-1902f1467aab | -12.59746 | -45.73202 | 2025-09-15 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 15218909-3c5e-3ba5-83e3-a76559fa88a8 | -7.88881 | -43.5932 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 85a83fe0-f6ab-3ef7-ad4e-34762443b9dc | -7.67934 | -44.48552 | 2025-09-15 03:30:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f105cba8-1e1e-35cc-bdd4-6469f85cd229 | -7.8802 | -43.57233 | 2025-09-15 03:30:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 478.1 |
| 23941303-270c-3170-85d3-2c815c651588 | -13.21651 | -44.07823 | 2025-09-15 03:30:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 335aad19-9ea6-3768-99ff-20b7b08ef794 | -12.00261 | -46.66794 | 2025-09-15 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70c67a85-c0f9-3280-89b4-abe52fcaaf3a | -8.91453 | -45.49471 | 2025-09-15 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a0be1767-ccb0-3c7b-b7b1-991c29a34511 | -10.68481 | -46.25951 | 2025-09-15 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff279c35-9702-3210-92a7-381e2d6a9914 | -10.93959 | -45.5162 | 2025-09-15 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README11.md)
