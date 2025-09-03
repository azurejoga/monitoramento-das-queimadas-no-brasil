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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3357eedd-3ae7-3b97-bfa6-3594f3eb8633 | -10.55093 | -50.42508 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b154bbb1-ac31-3e68-87b2-6d731e201148 | -7.71741 | -48.75033 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba76c880-2988-39d7-87d6-ab370734aba2 | -9.13279 | -49.64708 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bed2cb81-f942-35c3-a99a-be990fb11957 | -7.912 | -46.43499 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2bb4779-e48a-37d7-841f-3f7f3bc2b056 | -11.21665 | -55.06982 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ee8d84b-9019-381f-959e-f0ee8e3dadbc | -8.87574 | -45.83656 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3912e178-e016-3d81-bae2-3c5c3bb29a3b | -11.60999 | -52.12078 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d50d8dd9-4e13-3c8f-8a91-1db74ea866f6 | -8.09565 | -47.58638 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d533f21-70aa-3fba-bcfc-fd0fbc4b54f3 | -11.57761 | -49.90443 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d901fdd-189d-3f6a-aef2-6de495ebc1e3 | -6.10015 | -43.28472 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5d123dec-f405-33e7-a32b-e9f86b6b1e49 | -9.33371 | -55.23049 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad5f5daf-fc3c-3723-a591-60e802dce301 | -6.22787 | -42.42716 | 2025-09-03 04:46:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c3c88a2f-5d24-3466-a07e-5ccae6e2a355 | -7.38041 | -57.14836 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72826cfb-265c-3a78-94d5-2e8fa30d1521 | -10.95788 | -50.76892 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 957d6455-9e7e-351f-8372-8db971acdb63 | -6.34184 | -53.44397 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0846a2b4-2c54-3697-8ec2-8f26818296b7 | -10.14777 | -46.28159 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05757e40-d8cf-30fa-8378-78943e4df638 | -11.6088 | -52.06309 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7651863-86b6-34d7-94c2-4f2dd4f639fc | -11.60556 | -52.1057 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 001005fa-b366-3f16-aed9-88d261448a4d | -10.10347 | -46.25603 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1509b3e1-3f48-31a8-97a4-cc759f7e46de | -6.23439 | -42.42859 | 2025-09-03 04:46:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 88deecd8-28e7-3529-8cbb-5e6fd54c4393 | -6.79108 | -52.81511 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d9ce85d-167c-3c4d-914b-eb6b7fca2b10 | -6.2226 | -41.80202 | 2025-09-03 04:46:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 30d02887-a6d5-343a-9be4-17ea01336b16 | -6.27808 | -43.51062 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19951788-1e98-3c0e-85ee-90f17ec72fbf | -11.26693 | -48.95031 | 2025-09-03 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19f1e46b-0a3d-3ce9-9094-20afd88fb12d | -7.92989 | -46.5492 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fba042ee-8406-3a31-b839-4ba112be0dbf | -10.09381 | -54.76561 | 2025-09-03 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5869b963-5ce2-3057-a97a-671bd5ecbf9a | -7.10882 | -50.77742 | 2025-09-03 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc5b7981-4779-34d4-bdb5-cf8255894205 | -9.60729 | -55.39178 | 2025-09-03 04:46:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d1daebd-68b5-37c9-b993-8be3ec85cd0c | -11.59623 | -52.12217 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 34e56195-b355-31b4-bce5-f85cc5f15eb4 | -6.66764 | -45.92168 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd61605b-2472-3a48-9a1b-d8aef14a7b6c | -5.69271 | -45.39652 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faec7bb4-76ce-3b62-9611-78c5a1a03945 | -9.3982 | -48.04713 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c77dbd4a-4933-3012-9b33-5f809e3cadfa | -7.47974 | -44.84069 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89ae7050-0901-3ca1-bf3e-642fe82968b5 | -6.36968 | -43.01115 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd3d8bb1-7979-3986-93a8-2f8378077965 | -11.80948 | -50.63417 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c87191c4-6236-3bd2-a34e-b4430e961cd6 | -5.91648 | -57.72251 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 85f20226-87ad-387e-8bec-f23f032a913c | -5.81103 | -43.22252 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f444fcc9-8993-385d-921d-1f5efbc63222 | -6.54595 | -42.95966 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0eff585-ef9f-36a6-bf86-29f4b375fee1 | -8.14752 | -54.9306 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c35ff38-95bb-30ec-a928-be218595ad23 | -8.36754 | -52.53373 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22bbd1ec-7529-340c-8a59-7a58f7e63f2e | -7.70056 | -48.74091 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 42445fb4-b124-302c-a844-5556b961ef53 | -5.84666 | -43.013 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ceb22bce-0d58-3268-b3db-01437a241a8d | -6.80853 | -52.81414 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48d27427-cdca-329b-8478-4026bae0f6bf | -10.061 | -48.0919 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb4adac0-26c8-3ca4-9184-d840cde7037a | -6.80133 | -44.6423 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7791eb4a-e0a7-3763-adf6-6ab80d3a5291 | -6.77478 | -52.80882 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9da872d0-83f9-3773-b47f-047d57eab1c1 | -6.24408 | -42.62688 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b5b3d6ce-3fe7-3851-bc92-1b7379dde5b5 | -10.09095 | -54.76098 | 2025-09-03 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| de147ed6-faae-3668-93f2-4b90468408f0 | -11.75118 | -49.92257 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26c0c8b4-f52a-393e-9195-ec6846f28ad5 | -7.11796 | -44.75708 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5fa58ff4-62c8-38df-89e8-5dfd4242d3e2 | -5.92098 | -57.72313 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| e1a8f63e-cec3-35a1-83bc-9f9e833800d2 | -9.75316 | -46.91368 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31892f70-89ee-38bd-95e4-e73ac0008248 | -6.09053 | -43.17701 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6eae52ee-2488-34f8-a60f-e54095ea7f1d | -8.01561 | -50.09993 | 2025-09-03 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a64d099-c277-32eb-b753-8b9f62f76f70 | -11.44413 | -47.30436 | 2025-09-03 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3af1e2d2-cfa8-3b9e-adec-da4800e2a68c | -12.57758 | -44.78475 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 419c0874-73a5-3572-a956-25e9e0424d3a | -6.73361 | -42.26271 | 2025-09-03 04:46:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2b0bfaf7-29d9-3c79-b58f-23b564a56c22 | -7.94039 | -46.53283 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c730fb9-91bb-3270-9989-3625d0ea41cd | -11.68045 | -52.19359 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a622e09-758e-3e2f-998c-83c17b179005 | -11.11694 | -44.64627 | 2025-09-03 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17f67eb6-7614-3e1f-bb02-57bbf380b3a9 | -11.26754 | -48.94603 | 2025-09-03 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f23c3a21-5d32-3580-bfd0-72af2342623c | -9.7704 | -49.39594 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb544599-52a1-3196-afd9-f959bd71f496 | -8.87262 | -45.8279 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8273606-3386-3f77-9467-48028156cdd3 | -6.95883 | -42.96816 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| acb4239c-e5e3-31fc-8628-b7094185a620 | -6.78829 | -52.81091 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c279204-6545-314a-a37a-4dfceeb250ea | -11.9508 | -50.60246 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4ef7423-501b-37a9-b2b9-75cd645d5eea | -6.45287 | -42.39182 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f81025e5-7039-399a-8338-806802f5ba26 | -8.88497 | -45.82737 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3600e140-ae47-346e-93b6-c5dda64969b2 | -9.73427 | -49.00481 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3ccee9e-eeab-3d96-907b-5a0be5ce79cf | -8.86183 | -47.93127 | 2025-09-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29035bed-dac6-3696-91e8-96296ab1298f | -8.89041 | -45.78724 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dfd4942-350b-39d5-a4a6-9ede0f0896e8 | -9.75718 | -46.91428 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29512f5f-e616-3539-8dd4-118a9da886ff | -6.03754 | -46.01702 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 985cc30e-35b8-3151-bcd4-601ba92762ad | -6.44461 | -49.52702 | 2025-09-03 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a280a474-d6af-3e4b-9b17-b2452596955f | -6.27219 | -43.58588 | 2025-09-03 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6215ee36-a6fb-3d22-8471-6a4655a81c7b | -8.15258 | -54.69434 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3344c2a1-f2a0-355e-a515-ad84eb505af9 | -6.82597 | -52.81324 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d25037e6-9e90-37df-b5ab-32479696f411 | -6.7349 | -42.25327 | 2025-09-03 04:46:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4915c5cc-a93a-37e2-9895-f79ab2972d3d | -10.45357 | -53.61713 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ae49fdea-b286-3d80-9df6-9e6f902218c2 | -7.70421 | -50.30964 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 373668b4-8dab-387c-90f0-b9911aeffd89 | -10.50009 | -50.31918 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ba50926-ef68-3545-a896-8dff969fd4de | -10.49387 | -50.33722 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92e96723-b9b7-3d96-bf19-bf64918cc7ed | -6.86029 | -52.81494 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 588575b0-e79b-366d-a01d-9af00934cd5c | -10.53057 | -50.42192 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b42fed5-55e8-3fc6-b828-1cd7c86b50cd | -10.90475 | -45.79446 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 844bda36-e629-37bf-a392-f6913abb1c67 | -5.90394 | -43.3581 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18c46e23-097b-3fb6-9aba-2459684249fa | -10.96826 | -50.91862 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a9fa84b-c711-3f52-acec-a8d295cb50ba | -11.05554 | -45.40582 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b5b1a89-39dc-365b-8856-feefcaa028d7 | -7.0508 | -50.8645 | 2025-09-03 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e582bd66-2f19-30b6-9824-496bc58c1b61 | -8.09433 | -47.59562 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 484c4d9a-1aed-3097-bcc4-2dab08161a85 | -5.54434 | -51.34071 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 273bbcff-17d7-3854-aecd-0788f889fcc4 | -11.12242 | -45.11547 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7d4451ed-98c2-3286-8c05-0faef716a52f | -8.85745 | -47.93516 | 2025-09-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf44bfd2-e382-3145-871c-fb7a40f79e10 | -6.80284 | -52.82811 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d7eea2c-709a-3a6e-8bbd-5840b29b41f8 | -8.37031 | -52.53778 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7ba65651-946b-3e82-8f8b-1c0ba5cda78d | -11.58798 | -52.13163 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9a063073-21a8-3ab1-b8a4-329d28c8cbb2 | -6.54216 | -42.95008 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 873bd389-1153-3773-9e46-b2763723c66f | -10.96718 | -50.92585 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53c0e944-c46e-36c4-922b-80effabc86d2 | -7.01911 | -44.35512 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d3e4929-7774-313b-8c35-9b59b0e7da5a | -8.02135 | -44.08665 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README53.md)
