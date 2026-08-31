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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8d0c560-c349-34cf-9979-7f61df471dda | -17.86255 | -50.50729 | 2026-08-31 16:28:00 | NPP-375 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 283.8 |
| 32153fe5-1789-3b2b-bd31-39f289ebd33b | -20.13578 | -46.0271 | 2026-08-31 16:28:00 | NPP-375 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7380813-11e9-3a7b-aee8-98cb24bf97a5 | -19.83006 | -47.94629 | 2026-08-31 16:28:00 | NPP-375 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa1e2e9c-5573-3d54-9ba1-9b154752ec44 | -18.51484 | -48.3419 | 2026-08-31 16:28:00 | NPP-375 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d64f1547-28ed-3892-b27e-08dbe04c8333 | -15.08635 | -48.02667 | 2026-08-31 16:28:00 | NPP-375 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1d444516-037c-3521-bf11-333c42944b15 | -3.1267 | -61.1811 | 2026-08-31 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4cb0a4cc-df17-3079-bee6-7691e99b5d36 | -10.107 | -68.4008 | 2026-08-31 16:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 5a9338d4-ead3-3392-bff9-2f1aa0ce37a9 | -11.3427 | -45.1751 | 2026-08-31 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 58f98cfe-dac7-3a83-adc5-904d445b97cb | -12.3618 | -50.5417 | 2026-08-31 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 63935b7e-db30-3dd0-b214-0be3217e4242 | -10.8463 | -50.2224 | 2026-08-31 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 168c4bce-59f7-3c8b-a278-64cbfd3fbfc1 | -6.8387 | -59.4186 | 2026-08-31 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 3ea00475-e137-35c5-8398-ad7dda57a37d | -10.5607 | -50.3595 | 2026-08-31 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a60425b1-8c79-31e4-8107-5cb7b864e50c | -9.4156 | -45.6499 | 2026-08-31 16:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| b6bcdb50-46a6-33b7-ad69-32564f62c4d7 | -9.4342 | -45.6704 | 2026-08-31 16:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 52371a45-7d4f-3ce0-8019-ba3481a7ec0f | -3.7898 | -59.3415 | 2026-08-31 16:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ce6d6e10-3a28-3a1e-b7f4-be2d377b3670 | -7.9172 | -61.329 | 2026-08-31 16:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 6ef8325b-2a66-3fc7-9f3b-8a2832cae2cc | -6.8386 | -59.4379 | 2026-08-31 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b470e14a-4668-3c4e-8def-960dbc29f9c5 | -8.2229 | -54.9412 | 2026-08-31 16:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 134e032e-8986-3dba-a246-b8af6add7c13 | -5.9636 | -57.6704 | 2026-08-31 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 91b5b39b-754c-3c9a-84b3-f5a53d414d62 | -6.0923 | -57.7238 | 2026-08-31 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ca666727-870c-385e-8b5a-49feadb1f1af | -11.1824 | -50.5706 | 2026-08-31 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 9443a301-cb5c-3383-9713-810f40bed2e3 | -12.1711 | -50.5432 | 2026-08-31 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| aa4a39d1-cba0-333b-bc6d-a8513d5d621b | -10.8215 | -50.6519 | 2026-08-31 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 67a5673c-ad44-34fc-9c52-dabcc5e8573f | -10.7833 | -50.6772 | 2026-08-31 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 73e91301-42fd-384a-a56e-1c67346519d8 | -6.7833 | -59.4208 | 2026-08-31 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ae1f44c2-efaf-378f-90de-e54137c87c64 | -9.5964 | -47.6204 | 2026-08-31 16:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 37236721-f77f-34db-bc9a-219842752dd1 | -9.4339 | -45.6931 | 2026-08-31 16:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| c6357f7c-f2f3-3575-b51f-afa3ff9098fa | -8.9596 | -60.5934 | 2026-08-31 16:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| c0324ffd-1401-3ea3-92a5-7ec902f367cb | -11.1939 | -53.9993 | 2026-08-31 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 08794731-7804-3fba-8de7-797c9e544166 | -10.7428 | -50.8727 | 2026-08-31 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 39c4743b-7aa9-3a8e-890c-856d8f998db9 | -10.802 | -50.6965 | 2026-08-31 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 41817660-8a9a-3219-ade4-4beb7cd4be4b | -11.0563 | -51.4751 | 2026-08-31 16:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 3c4a9566-4ba5-3456-9736-7b65037f0a47 | -8.5555 | -66.9574 | 2026-08-31 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 8ff90874-c127-314b-8955-94f95e8f238f | -3.4185 | -61.3461 | 2026-08-31 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6818bca9-aa4a-3deb-b1e6-4efa306027e0 | -3.6216 | -60.547 | 2026-08-31 16:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| d62b2bc8-5763-3c95-88e2-f6cf8e20da24 | -10.8235 | -50.5026 | 2026-08-31 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ee7e28e1-1974-3e49-b36a-491ce039be10 | -9.1711 | -49.9835 | 2026-08-31 16:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9b6e43a0-b0c0-3c13-9c6c-b5f35b66cec5 | -6.1295 | -57.6637 | 2026-08-31 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 5a79311b-cec4-3b01-b360-d7705660a9e2 | -10.3013 | -49.9801 | 2026-08-31 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| dd22567b-c5a2-31ee-a2a2-7e0ba01ff813 | -3.9707 | -60.0258 | 2026-08-31 16:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| ba6a2b1b-65d3-352b-9a0e-e6820d94223c | -7.529 | -61.3635 | 2026-08-31 16:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 1531e6ef-79d3-315a-951c-e692be245f65 | -12.1899 | -50.5623 | 2026-08-31 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c4d3c7e3-4fa5-34cf-a9b7-16f8f39bad09 | -11.0566 | -51.4539 | 2026-08-31 16:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 88ac1f47-17c9-30c5-a7fd-4c7f0e6791f0 | -13.4519 | -57.039 | 2026-08-31 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| b4cf1a1a-a1c3-3691-81f2-2ad4c6884fee | -3.7566 | -65.1309 | 2026-08-31 16:30:00 | GOES-19 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| be70d8c2-29e0-3c51-a54c-bd29b774cefc | -10.844 | -45.3356 | 2026-08-31 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 31c12dc0-8716-3fb7-a9e7-07b8467b8580 | -11.175 | -54.001 | 2026-08-31 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9917de80-c12e-3249-8876-eb64498d1970 | -9.7873 | -59.4479 | 2026-08-31 16:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2dddf3dc-f6ee-38e0-a32c-198761860821 | -10.5601 | -50.4022 | 2026-08-31 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 83b09786-c11a-3286-a9e4-f045ca70f00d | -10.1538 | -45.6982 | 2026-08-31 16:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| e331813f-3341-3f85-aee1-b663d2622558 | -10.7268 | -50.6618 | 2026-08-31 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a0aef1b2-2354-3f95-8448-b6cfd037d083 | -6.8756 | -59.4171 | 2026-08-31 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| a1323512-d5a7-3be3-a703-2cf91a1f3d14 | -10.8043 | -50.5259 | 2026-08-31 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 9d39bc7f-ede0-35aa-ad31-250a77bd6370 | -7.3119 | -60.5706 | 2026-08-31 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 816ce39e-9834-3439-974d-338194b54aa3 | -10.8025 | -50.6539 | 2026-08-31 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| baa989fd-67f8-3eba-832b-64c2d2e131ce | -7.0057 | -59.2575 | 2026-08-31 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 9c7c6dc8-7c7e-355b-86fc-dbd04d0b6f2d | -10.7618 | -50.8707 | 2026-08-31 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| df344d4d-7420-3bed-bd1a-a810b82e306c | -8.87 | -66.8935 | 2026-08-31 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| f45bd68a-3892-3a6f-8f0a-2a34c87b15d1 | -8.9253 | -66.9477 | 2026-08-31 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 7c2f4c51-3bcc-38d0-8e32-cbf36490b0f5 | -3.1998 | -61.161 | 2026-08-31 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7df179c8-1d5f-3fed-b2e3-2687e0e0d7b5 | -6.9872 | -59.2582 | 2026-08-31 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5b0c78c7-1f77-3983-a965-a1b009c0c63b | -9.6676 | -47.9429 | 2026-08-31 16:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 5fda1bbd-bb9e-3a6a-815e-025631426a26 | -10.1084 | -50.299 | 2026-08-31 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| fd21318c-dbd4-37df-9c65-1432f749b11f | -13.4707 | -57.0574 | 2026-08-31 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 830266b2-5df4-3a1d-8d59-f2d4e302a1f7 | -10.5598 | -50.4236 | 2026-08-31 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 60005819-326c-34e2-8a61-56b77349edfe | -8.1345 | -45.4923 | 2026-08-31 16:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 1c536f6c-819d-3f7c-a69c-4ab3935104eb | -10.8212 | -50.6732 | 2026-08-31 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 087d8748-aff0-33d9-9354-0473366b9a10 | -7.9425 | -44.2538 | 2026-08-31 16:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| a6e615d3-dd3a-3cef-af43-e0927f6c1d52 | -12.09147 | -47.18138 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2d637a90-5ef8-313a-a835-4bc261701906 | -9.41527 | -45.64886 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ef2d1971-44d7-31df-878a-54054052f061 | -9.41712 | -45.66199 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7d4cab62-13c7-3639-a3af-acb86014c9dc | -9.68176 | -47.93917 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| be31a0b6-d534-3082-8bd7-4ea275cc4fd5 | -9.96379 | -46.78339 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 44186e70-8cbd-3289-8f4c-62836f7d7409 | -11.23541 | -45.14593 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| bf978ccf-d6b0-3176-a089-204a5d6f8ace | -11.68494 | -47.60096 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d413c71f-0bf5-37f2-906a-ac527748480b | -8.76619 | -45.38927 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a2203776-7d4e-37e0-81db-7e50a485aca2 | -8.86461 | -47.07642 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e4e3c373-d04b-3584-a936-4840dee23908 | -11.32347 | -45.19788 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2314fba4-c3a6-3ca6-8b09-3420694a1ca5 | -12.10346 | -41.53361 | 2026-08-31 16:30:00 | NPP-375 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e98adf99-37a8-3096-8b04-e070d3300ef1 | -15.40521 | -52.70642 | 2026-08-31 16:30:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 46eaa6dd-970b-396d-9543-a994888c9d03 | -11.69922 | -47.60839 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d0878123-1ee6-3c27-96d7-96e54b204c80 | -11.21428 | -46.10396 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7573c132-9abb-325f-ae8f-34e1e3ff9b39 | -12.89979 | -45.83672 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| eef6094d-09d5-3a44-87f4-6a40f9d37ab2 | -9.18975 | -51.55062 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| abf86cc1-9b2a-35db-81db-b33bfd72d265 | -12.10038 | -47.27859 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0acdbd33-b8b1-3c54-90cd-acd1180dbbd7 | -8.49392 | -45.53449 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d326ebc-d9cf-3b43-819b-37ca66c115bd | -14.57154 | -53.5925 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| fa4471fe-92e6-31c7-9962-48932d9302e1 | -15.40523 | -52.71538 | 2026-08-31 16:30:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f4d8782b-426d-3936-b295-8d0c28945537 | -11.24888 | -45.10786 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 28af44b9-d816-3630-ae80-ab15e7c91b9b | -11.20496 | -46.1186 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| b8286592-33af-3ccd-b7ec-d201da7eb2a4 | -10.9591 | -48.40483 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| da85574b-be68-3006-8867-aed8bada731d | -15.2507 | -52.73899 | 2026-08-31 16:30:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 03992913-2574-3af3-b33a-624423996159 | -11.91068 | -44.83793 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 59f17530-82ec-375e-a117-becfcf628d6e | -11.21804 | -45.10323 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 070348d5-c581-3424-9837-3aa191483a22 | -9.66463 | -50.85737 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 4a8e639e-39c7-3b2b-9b09-2cd047443759 | -9.21047 | -51.58126 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| c430117a-c98a-31f8-9afc-9f13078b8a96 | -15.28248 | -53.89001 | 2026-08-31 16:30:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 87d4a232-8a02-39b7-9d28-5f61d0cca4df | -9.42275 | -45.67507 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c4a5f24a-f8bd-3ba2-96d7-29e2ce3faff3 | -9.5934 | -47.60871 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b18d2486-3554-34b2-88f0-32df2325fed4 | -11.24943 | -51.26647 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |


[Clique aqui para ver as próximas entradas](README114.md)
