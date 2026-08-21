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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b41d46b-dd57-35d8-81ab-83c92e496653 | -18.2134 | -50.7518 | 2026-08-21 00:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 9b364424-f49d-34dd-bdfb-e28ee7ec1efe | -6.6938 | -58.942 | 2026-08-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 9abcea03-6a8e-325f-bb7f-34b37f7d30bf | -11.175 | -54.001 | 2026-08-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| fc8f3638-bb1e-3257-a1d3-991e0a826a13 | -7.36 | -45.8361 | 2026-08-21 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 55dcab7c-681f-337a-aa8a-403ee23d6ddc | -10.7504 | -50.3182 | 2026-08-21 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 55282338-e827-37a2-95a6-10fb36bd36f3 | -15.7156 | -47.781 | 2026-08-21 00:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 9c30d23b-0f99-31e5-8b37-db28efc50fa4 | -6.2155 | -55.6316 | 2026-08-21 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| e7bade95-bdda-313d-a7f3-10c48037bc17 | -18.0285 | -44.6113 | 2026-08-21 00:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 91.7 |
| dd2f84bd-3656-3ead-8758-722d4af44875 | -6.8593 | -59.0318 | 2026-08-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 945f90fc-935d-33a0-81d4-c013d7826950 | -7.3791 | -45.8119 | 2026-08-21 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 304.8 |
| 1219999a-f1a5-3082-8f92-e2bab28ee412 | -7.7703 | -61.1443 | 2026-08-21 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ffa2d8d6-4063-31c3-b32e-78a293e3619f | -10.3162 | -50.278 | 2026-08-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c261771e-c2a0-3b9e-a5ff-99018daf02f4 | -18.1934 | -50.7554 | 2026-08-21 00:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 129.5 |
| bb8a8dde-88d3-33e1-9d77-55ae33570ab3 | -11.1558 | -54.0233 | 2026-08-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 14dac305-54ce-3ede-b395-5b935b230d3e | -8.3903 | -62.6963 | 2026-08-21 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 358aa213-60d7-3938-bc05-3c0dafa6e428 | -3.5407 | -48.1673 | 2026-08-21 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 72182caa-639d-37d2-9904-735cf0a248b9 | -6.8756 | -59.4171 | 2026-08-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 86682dbe-6884-32d4-8f87-83d9b664fd0b | -6.8755 | -59.4364 | 2026-08-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 88f729ad-f09d-346c-ab14-9d562f1241f4 | -14.5855 | -53.0056 | 2026-08-21 00:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 44796d52-5965-32a1-89fb-a3c103ac9339 | -10.3159 | -50.2994 | 2026-08-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 6550e32b-1c0e-33b6-8221-d5161737fdc7 | -6.9516 | -59.028 | 2026-08-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| f247e3b0-f3a5-3551-a9bd-5afea11c95c0 | -6.8939 | -59.4356 | 2026-08-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 650d9dab-a591-3731-8b73-37a4c6ebca52 | -10.2592 | -50.3051 | 2026-08-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 812f23eb-ada5-3e43-9d34-5094dba9abd7 | -11.1747 | -54.0216 | 2026-08-21 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 221.8 |
| 4eaf1ba9-ea18-310b-b512-363774248f49 | -10.7501 | -50.3396 | 2026-08-21 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6fdcf7aa-579e-3114-98b7-dbd4c40c1df0 | -6.9333 | -59.0094 | 2026-08-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 93a702b2-1834-3f72-908c-2b00ae431d8a | -13.3926 | -54.3758 | 2026-08-21 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 44c71848-2894-3ad6-a451-ebdcdc7d659f | -6.2156 | -55.6118 | 2026-08-21 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 3bee0b50-227d-3a6e-9c19-259be76ffd25 | -3.5591 | -48.1882 | 2026-08-21 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 248626a7-d83b-3286-8e3f-56988cd24e96 | -10.3148 | -50.3848 | 2026-08-21 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 553224b1-e91b-3063-9b21-db9fb013b71b | -6.6939 | -58.9226 | 2026-08-21 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 96a35918-ed8c-3060-808f-51f04d18f631 | -6.2341 | -55.6109 | 2026-08-21 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 7392b633-1907-3bad-84b3-e609dd84a8ee | -3.5221 | -48.1896 | 2026-08-21 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a18b6a76-e2d3-328e-bc2f-2b26ad461c33 | -10.7693 | -50.3162 | 2026-08-21 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| dd77df64-30c2-3b0e-b9ae-0a691631fdfa | -7.3791 | -45.8119 | 2026-08-21 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 344.2 |
| 11141fbf-c2ac-34b3-a0d2-c622a2fe1d0e | -15.7156 | -47.781 | 2026-08-21 00:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 45.7 |
| f5a5d22b-b0d1-3088-88c5-3699a36abee8 | -12.5104 | -54.755 | 2026-08-21 00:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5b150b30-3796-3f05-92d5-7988f60644b5 | -11.175 | -54.001 | 2026-08-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| c99c9f4b-b650-3efb-aa86-3bab9075d43b | -3.5406 | -48.1889 | 2026-08-21 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 226.9 |
| cacb082a-6e99-3d23-8330-6030d87f1898 | -13.4117 | -54.3737 | 2026-08-21 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c71338ba-70a0-3575-88a0-2980dbcab679 | -4.0943 | -42.5097 | 2026-08-21 00:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 974e0baa-929d-319c-8641-b6f62730e645 | -6.894 | -59.4164 | 2026-08-21 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 4cb6a4f8-2e25-34aa-9dc5-21c771390b9c | -6.8939 | -59.4356 | 2026-08-21 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 6579a50d-75dc-3584-ba58-3c49fa9cd6e8 | -11.1745 | -54.0421 | 2026-08-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 09c7e357-dc4b-3a36-8737-6ea3a16bb9bb | -18.1934 | -50.7554 | 2026-08-21 00:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 50ad78fe-801d-3b7f-8376-d8b5598984bb | -8.3903 | -62.6963 | 2026-08-21 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 110401e8-d5f8-314e-a96c-1a5792ffe973 | -7.3415 | -45.8152 | 2026-08-21 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d7bd501a-929b-3ee3-87d7-326faa89c5bd | -13.3926 | -54.3758 | 2026-08-21 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| c23c0585-465c-34a5-973f-cdcdeee26b28 | -10.7504 | -50.3182 | 2026-08-21 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 20a3e50f-206f-34be-822c-3853e65a9805 | -6.8593 | -59.0318 | 2026-08-21 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 23a76d27-11e4-3383-a9d9-ecd6562c214c | -18.0285 | -44.6113 | 2026-08-21 00:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 76da2c19-ef1b-35f6-a9da-00eed0182805 | -7.3788 | -45.8344 | 2026-08-21 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 5c4e5c78-e029-3479-a094-53d9c5dc91cd | -6.6939 | -58.9226 | 2026-08-21 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| f48856ef-8098-355f-91fc-ac5a4d110172 | -6.6938 | -58.942 | 2026-08-21 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 06e57c4c-fb63-3cdd-a5d3-f494707926bf | -7.7703 | -61.1443 | 2026-08-21 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 53d1e9b6-3496-3e0e-af23-aeb7fdde36cd | -11.1558 | -54.0233 | 2026-08-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 2f5c80e6-4d02-321b-bf86-95f86ddf9547 | -6.2155 | -55.6316 | 2026-08-21 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| aeeb074c-6755-3145-a2e8-92158565539e | -3.5407 | -48.1673 | 2026-08-21 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| d0c81ea0-fe5b-3284-b8eb-87204a97101d | -7.36 | -45.8361 | 2026-08-21 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 8bc867fb-84c5-3c18-8d9c-8292a2a3b2f6 | -7.3603 | -45.8136 | 2026-08-21 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 438.3 |
| 46ab0dc5-1b91-388e-b0ee-20ff2ffedf7a | -6.2156 | -55.6118 | 2026-08-21 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 1493d04d-0d1b-391a-b067-757e2a7786df | -18.2134 | -50.7518 | 2026-08-21 00:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 178.4 |
| ffb98e28-0ce4-3128-ae46-c7c55e98354e | -6.9517 | -59.0086 | 2026-08-21 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c9e4b4df-3afb-3b9a-8778-d95ed8e2a00a | -6.2341 | -55.6109 | 2026-08-21 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 194.2 |
| 34cbb9fb-2860-34cb-b414-43afc5dc782e | -11.1747 | -54.0216 | 2026-08-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 193.6 |
| 5bee6e88-1b62-3ffb-a51e-4a74f407e9fd | -11.1936 | -54.0199 | 2026-08-21 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 68c22b21-dfbc-3e6a-9775-d296b68034d2 | -10.3151 | -50.3634 | 2026-08-21 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| c71a8726-7023-30eb-aeb3-24657823cf8b | -10.769 | -50.3376 | 2026-08-21 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 39cdecde-877c-3ede-959f-023b1ac4ecc9 | -10.7501 | -50.3396 | 2026-08-21 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| dfde50f0-3ce7-3075-a6d9-734e37cc5804 | -7.7702 | -61.1634 | 2026-08-21 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 31dd53e5-3312-3ca0-b937-0a3f77b09a75 | -10.3148 | -50.3848 | 2026-08-21 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| a46b26cb-d6b3-3526-8423-50f47a13402e | 2.5983 | -60.697 | 2026-08-21 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 618d9ccb-18ac-3921-92f0-a4f953756334 | -9.9954 | -48.5522 | 2026-08-21 00:42:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92b192b8-4243-35a1-b524-f1746a0583d1 | -9.4441 | -51.6273 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 905eb145-45a2-3a3f-9d7c-fd6531e34a1d | -12.2433 | -43.1702 | 2026-08-21 00:42:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8b839317-754a-3c05-bbd7-5af8ad6f74c1 | -3.5444 | -48.171902 | 2026-08-21 00:42:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a68c83-0f1f-3d1c-8b75-0e082a2eee6a | -7.3408 | -55.687901 | 2026-08-21 00:42:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 455dff61-dd0d-39e0-8266-cf921e2eecc2 | -6.4261 | -52.7537 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd5ea54-5826-3d04-8efc-27fde40651c6 | -2.1147 | -47.116001 | 2026-08-21 00:42:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6023b96c-e0c0-3e14-9e8b-b71fa02db1e3 | -14.3271 | -51.906502 | 2026-08-21 00:42:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d9eaf60-a2e2-3e40-937d-a2897a8e97a5 | -14.9023 | -44.807899 | 2026-08-21 00:42:00 | METOP-C | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f1add038-b2c1-3e6c-9302-e88930579e0a | -5.6086 | -43.9991 | 2026-08-21 00:42:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4fc8684a-2fe2-3a6a-a0ac-d46bb942e30e | -6.851 | -59.427101 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b06a1a8b-60e6-3ee0-b011-0975f310f1d2 | -6.3401 | -44.0835 | 2026-08-21 00:42:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cfc56f7-edef-3ff2-a690-bb1ebb2869af | -7.7669 | -61.141701 | 2026-08-21 00:42:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7a23882-fb48-3ab4-984a-149a59125eba | -15.0034 | -52.674 | 2026-08-21 00:42:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a5396892-b733-30cd-a2bf-8c10430223ac | -9.0628 | -50.874001 | 2026-08-21 00:42:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50b06bf4-5acf-39b6-8094-95db84a12766 | -11.1629 | -54.029701 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c22de207-ab7e-3937-9db3-cd765f791676 | -10.7299 | -44.7812 | 2026-08-21 00:42:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3798c232-9134-3191-bad9-1d3aa88c4b93 | -12.2336 | -43.1726 | 2026-08-21 00:42:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| eac8f6f1-24da-3a5d-8ca6-c99becca8965 | -8.4503 | -46.944401 | 2026-08-21 00:42:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f5c2180-7e36-361d-941c-de66fd70bae3 | -11.1727 | -54.027699 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b00cae90-360e-358d-86ea-913a50ad9a84 | -18.977699 | -47.030499 | 2026-08-21 00:42:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 60c50895-5e5d-3402-bf8a-1eabed19a234 | -12.5041 | -47.84 | 2026-08-21 00:42:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc8ca2a8-3726-3076-8a8b-d16a853b5b54 | -8.494 | -54.874001 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c24ae1c4-c470-302a-bcef-1271f1b92809 | -10.53 | -50.8162 | 2026-08-21 00:42:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f68dd991-8c7d-3a0b-89f0-771c2ef93d68 | -6.2276 | -55.402802 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4faad0c9-4317-305f-af4b-b4be27a513ed | -6.8607 | -59.425098 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c36333fd-7958-3939-925b-12113e8bf328 | -20.959999 | -49.1521 | 2026-08-21 00:42:00 | METOP-C | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 94c8623e-6a21-3036-b314-59f15fc0be28 | -15.7179 | -47.7934 | 2026-08-21 00:42:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
