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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b85bc26b-d71f-3244-bae0-b76fcf93910d | -8.67936 | -54.65147 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f688736e-20a6-3d41-b713-54730fb3e51c | -7.55366 | -55.56384 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e9f2b96-f9e4-3769-b70b-5cb6009425c2 | -8.54607 | -54.72125 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f64e827-114d-3468-bbad-98c21d4a6a56 | -6.76244 | -59.46723 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7911b636-c629-3f6f-aa55-ef43c0c1ed1e | -11.18355 | -54.02775 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b6e90f54-f2ba-3e25-a0f4-78c368240d61 | -13.61055 | -51.79769 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a1f212d-5a0d-3b47-ac43-84f0cea889f6 | -8.6754 | -54.65463 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7bf933f-6816-3310-a298-1d1c74668791 | -11.8334 | -58.83671 | 2026-08-20 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8afd1c98-8130-366e-9983-04ef8816d259 | -13.40816 | -54.3748 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 899cf070-6d82-3ae1-9a12-8fafdd3535b7 | -8.56982 | -54.72489 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec28b47d-ddd2-3141-aa8e-dfed024fbb85 | -11.21488 | -54.00559 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9d444f7-c014-3239-abcb-a6e441700359 | -8.49967 | -54.86711 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b63fa67-66e1-3949-a0d1-8f32b284a7ca | -7.54379 | -55.58372 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75e1b61d-af77-34d3-9154-1665788b781f | -8.56918 | -54.66079 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48942661-6257-3bff-b4d0-f86376addb31 | -9.21383 | -59.78463 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12552b4b-4c68-343f-8c94-8b0b88eaedbc | -9.39355 | -60.56334 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 591a5f5e-2951-3d85-94e2-aaeb7fecaf61 | -10.52174 | -50.78883 | 2026-08-20 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cdbacfa-af2c-3a0c-9fc4-fe577fd898cc | -11.20416 | -54.00397 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9793c765-e7cf-313d-a072-ec97065421b9 | -8.6714 | -54.63512 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f3697c3c-1391-3a1a-87c3-a2229f9f2ce3 | -8.53962 | -54.87703 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d6f00f4-3b77-39f0-b3b6-31b3bc6332a2 | -8.04714 | -54.03258 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebba612e-e124-3ba1-8a4d-a5ff0a7e1bbf | -8.10124 | -51.66258 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9e41b20-4eea-3074-812f-20e9b1f55fa4 | -7.37707 | -59.95267 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 847de370-4b55-3c2c-b664-6d1e827993c2 | -9.20659 | -59.78344 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ed25c55-4bac-3b91-a46d-9040ddaec93e | -11.81082 | -44.81185 | 2026-08-20 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c929529a-6f32-3bd9-8f30-4b767778c825 | -8.49857 | -54.87433 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d433057a-8f41-3def-897c-f04b5a42af06 | -7.56523 | -55.55492 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7afb308-ae4a-341c-9bdc-9af33d174cf6 | -7.05678 | -59.84558 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 818b96d7-80c0-3ef0-9ddf-970c25bc8cbf | -11.21445 | -55.06036 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63aea095-3bc8-30c6-9999-701e619485b4 | -10.33454 | -57.56881 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f290adf-db6f-34b9-8863-49c0980006df | -8.56805 | -54.66817 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| febf01cb-1df9-3cb0-a873-c679a1645688 | -6.86327 | -59.03396 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46682e7f-5856-3c35-9307-73571785938f | -8.53773 | -54.77608 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 162605e5-5662-33bb-85ff-4154e0266128 | -10.32789 | -57.56774 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 367758b3-9c40-3a82-bfd5-73b79c4d28be | -9.39425 | -60.56203 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96aa64b0-db14-35c2-b7ac-f6c089214d12 | -8.10516 | -51.66312 | 2026-08-20 05:06:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 200cbd9c-2411-34ea-80aa-70888e89bbfa | -8.55311 | -55.31984 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0692aaa5-febe-3647-92c1-3c9cf381815d | -13.41295 | -54.36689 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a352c25-4bb0-3940-a57f-64eadfe86705 | -10.39635 | -61.20727 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ee4a7db-8b41-3d13-a0c6-42548af27e15 | -11.22641 | -55.05061 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21318c79-5ff8-3e60-b5fb-c99ec2f9969e | -10.93397 | -57.11152 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 149c5aa1-847d-32bf-ae99-a363a335cd45 | -7.76889 | -61.14085 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e31df8a5-fd4f-3b26-a682-f8e53b268f73 | -13.44832 | -51.7892 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f38bfea9-b7fb-37a7-aec2-8fa885a9d47a | -8.67084 | -54.63881 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 17f66416-3678-3ac4-9613-cbb871095f2c | -11.19167 | -54.01477 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83f20703-e6f7-3358-85d6-fde6f4e2cd30 | -12.84885 | -48.42429 | 2026-08-20 05:06:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2359612-0db7-3994-9545-7ccac0a45217 | -8.4952 | -54.87381 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b49893c-b801-3d4b-9485-ae01769ceed8 | -11.82941 | -58.83985 | 2026-08-20 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35a2289a-e4f7-3e34-aaf2-b4ce6dc62ba0 | -14.73472 | -47.1524 | 2026-08-20 05:06:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6eb6b04-11e4-3852-98de-969b4a869171 | -9.14013 | -60.61578 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 193e0ceb-fa68-3670-b4ca-dafbbfd44143 | -6.86393 | -59.02986 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcbf04ed-ceae-368a-bd10-cf037e7415ea | -9.39583 | -60.55281 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92c3b6ed-911d-3a3d-a66c-bfb8f4090d81 | -10.74651 | -50.35658 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e8608a5-9543-3ec6-b65f-31cd74eab6dc | -11.21159 | -55.05608 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 496e7d43-fbed-3f10-be4e-d88eb80cf979 | -6.81109 | -59.00154 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c668464a-db9f-3433-93da-e73d438fa43e | -13.41235 | -54.37114 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e54cba7f-28bb-324f-b248-db55a339aabc | -7.53546 | -55.57171 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c8e87a7-f311-37c0-91ea-f83c0b8bd4bf | -11.69304 | -62.75316 | 2026-08-20 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a6f24cb-9020-31ed-bb63-555335c68da1 | -8.52668 | -54.87124 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 382cd085-f0d7-3667-8107-7ed52fa1b512 | -7.60891 | -60.95861 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbaf5515-79bd-381f-b33e-5ef73d9585d7 | -7.86715 | -63.76714 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38d42bbd-d575-36b9-bf3c-5e0240a0abe2 | -9.12921 | -51.15535 | 2026-08-20 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86a5b1c7-ae7d-3e1a-b185-bb357e75871f | -10.48239 | -50.3214 | 2026-08-20 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d91297bb-a769-3bf1-b5a5-c37498267cde | -11.42551 | -54.32243 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b41f4510-6d10-32a6-9ee4-34e7eae6a1c6 | -13.43961 | -43.84159 | 2026-08-20 05:06:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c902df6e-5ba4-3924-a9f5-ed9e59d69e32 | -9.47421 | -51.63443 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65e77e87-4a19-38d2-a4a1-218cc637b103 | -8.57736 | -54.77481 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19fa0e6d-53d5-3130-935b-0e845f4b3824 | -9.39723 | -60.56728 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72be6cc8-ff37-34f5-a766-5174b1dce7e7 | -12.00215 | -53.44106 | 2026-08-20 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7e1b240-fb7b-3353-bf7a-99f10fc2a196 | -10.38311 | -61.215 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8576c219-a41f-318c-80eb-8cba278c23d7 | -9.38874 | -60.59432 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f2baf69-cf02-34e3-9c60-d704fb41fe09 | -8.67596 | -54.65094 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbf2e5ec-3e11-30b4-829c-fa9bcc6f439a | -10.39718 | -61.20242 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 259decc5-d68a-31ca-bf3d-edce6300735b | -7.5377 | -55.5792 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 927b725e-cf1d-33e1-93c7-e9a7b6958352 | -7.83189 | -61.61442 | 2026-08-20 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4601a05-f9ad-387f-9a63-f59316acd8ca | -9.74604 | -59.31335 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 428d3863-7278-3e77-8567-eec60875e2ea | -8.0477 | -54.02878 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c2cc8b8e-37e2-3849-84de-2c63e0aba6c2 | -13.40588 | -57.04143 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 654d4eb0-b228-3f75-9752-6302f005385d | -6.87536 | -59.02745 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5420c2f3-a7f5-3db4-9576-1c7535fa8fd7 | -9.05607 | -57.07078 | 2026-08-20 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e93b7233-aa06-31ec-8420-af39395a9bed | -12.37924 | -46.45422 | 2026-08-20 05:06:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 158647ea-88bf-30b4-8e52-9bef93771af6 | -9.50284 | -51.66331 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10720cbf-32bc-3073-8175-c9c4a1c90fb9 | -11.21615 | -55.04905 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b36a2738-3b0a-338c-aa62-687dedb3639d | -7.48274 | -55.31957 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f373befc-49eb-3b94-b53d-21a00c0e54db | -7.71236 | -56.72663 | 2026-08-20 05:06:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3157f357-622c-3216-9fda-664a83c74922 | -11.20298 | -54.01223 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d68b0b00-5d60-3606-b751-b1b469e00bf7 | -7.43451 | -59.78811 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54522bcb-f5e8-31a4-b29e-a472eeeb7d11 | -13.44678 | -51.80109 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d3d067f-3e34-3a7d-8223-8b0ac7c43f42 | -8.57939 | -54.68498 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48488f92-d959-3899-90a6-591edd7cf253 | -8.5592 | -54.79429 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e9b540a-6650-31e1-8912-013ade9abcfd | -8.72023 | -49.6208 | 2026-08-20 05:06:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 38cc65df-6efc-3278-8a56-b35e8e1ac395 | -6.77264 | -59.45106 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 506ba252-44d0-32e5-ab10-60355f70e30d | -7.09971 | -59.77017 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b2fb314-3af1-39db-a21a-04abe558eafc | -6.85744 | -59.02456 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d69ee63e-5313-3c55-a33c-0be1245baf07 | -11.18452 | -54.01369 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 811a6dc4-792d-3bba-a004-975df79cfb19 | -13.40774 | -54.38943 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 36d97236-e73e-37d8-9ae2-543010490875 | -7.53877 | -55.57223 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0ef36c6-fea6-31d8-a6e7-3a163884bc4b | -7.42213 | -60.00639 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9dac2c6-fbae-3f8e-8206-aa3baf3fb900 | -8.49912 | -54.87072 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d82afc0-c9c5-30c4-96dd-49ac735688f7 | -9.11841 | -61.60211 | 2026-08-20 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README54.md)
