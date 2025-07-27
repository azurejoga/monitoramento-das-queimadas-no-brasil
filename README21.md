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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb56eb0f-fbbd-3e0b-8c16-873287072d99 | -10.28224 | -64.45442 | 2025-07-27 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3602ef83-e35e-36a6-9f43-1ee23dd59f9a | -6.64376 | -58.83128 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38f2e524-4c2b-332d-9225-b3cb826394f6 | -8.96874 | -62.2305 | 2025-07-27 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5831a099-5b36-3adb-99dc-df52aa1c72b7 | -7.60644 | -61.21923 | 2025-07-27 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bef1a815-cf07-3f1c-a1f4-8f96508a80b0 | -11.93609 | -63.84701 | 2025-07-27 05:25:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b71a45c6-11ed-3b48-8821-4bc7d63aa04f | -3.11915 | -48.96405 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cfe44fd0-bf8f-3853-acad-6252ebd89b21 | -7.74783 | -51.1202 | 2025-07-27 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 425fd6a0-2202-3997-85aa-1be58136b3a0 | -6.68298 | -58.82607 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f898cb79-0ae0-3bcc-ab7d-a31b0e9dfd76 | -6.55749 | -56.18316 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29e1e70a-fa97-3da0-b06a-d4fe7ff54a35 | -6.55562 | -56.20033 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a17f3b4-0ee8-3d58-b010-252c9dcdfa15 | -6.66534 | -58.84967 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05e04392-a2c5-34bd-b80f-043e10a45376 | -6.64489 | -58.84652 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8ff585d-29af-329d-bb6d-b03cec113822 | -7.90046 | -63.52775 | 2025-07-27 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 626df45e-24b8-39cf-8ba7-432ce31b87b1 | -6.64546 | -58.84284 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df34abf7-cd06-3364-a4f7-6a48db7ae60e | -9.02956 | -59.76384 | 2025-07-27 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f60de0ae-50bc-3019-9027-37ba59a67336 | -6.5461 | -56.18416 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1941935-eea6-3e5a-8756-6795605f979b | -7.55596 | -61.4083 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a2ffb5e-a36f-326f-831a-095ca2f0464f | -6.63922 | -58.86063 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b78a39d1-621f-3f36-adee-ffc2b979c6e1 | -6.64091 | -58.82707 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ea5e172-cc05-3850-863e-cee051ae37fe | -6.62103 | -58.84285 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eafd3b68-e7ae-3d07-bd19-149c02c7521b | -6.63581 | -58.8601 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e273607-919b-319c-9a78-9abe55742867 | -6.64319 | -58.85749 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| acaef177-aaab-3c90-83e4-6609ac961cf7 | -6.629 | -58.85906 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2976032b-ac7f-3bf6-b0f7-f2f5c1833804 | -6.53664 | -56.19006 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a301b8d-e0af-3008-a06e-73f1ed0408d2 | -7.29187 | -60.1859 | 2025-07-27 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9d4510e-afd0-3d1e-b003-8519fc28af8f | -7.50323 | -63.50691 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bdedf0f-9676-32c4-ba65-b039585b47dd | -6.66592 | -58.82344 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da8f40bb-81f9-3007-86b6-7476281edc0a | -6.55362 | -56.18259 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b9652b3-72e1-3d08-83dd-4af34c00b32e | -2.83009 | -52.35849 | 2025-07-27 05:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e95a47a1-57b1-3cbd-aa0d-33629fcb281e | -3.11979 | -48.95965 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 30614343-80bf-3383-886d-d34596d193ef | -6.64035 | -58.83076 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba02af6c-c895-3bda-b6c9-30550fa182cd | -11.3024 | -55.12509 | 2025-07-27 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35b2fed6-dd6c-339a-b079-8bb0de025dce | -6.66477 | -58.85334 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7be22e00-7fea-3ea3-b649-dd398b15a977 | -6.65625 | -58.84076 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97844890-03d5-3a48-9a49-95bc3e0d019b | -8.7224 | -63.14586 | 2025-07-27 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31ec0d10-bc26-33c7-bcfe-b1ce50af0a5b | -9.43382 | -51.74513 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd56e0ee-59a6-3279-9228-5427c7ca0e74 | -3.39091 | -47.49657 | 2025-07-27 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b17b3ae-0ec4-3a2c-bae6-15f762c2bc77 | -6.67046 | -58.8392 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbb3e0e7-c83e-3695-a9bb-1c1e4caa39e0 | -6.65058 | -58.85489 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 61ba55a0-2f6f-35dd-817a-abc8da7a0606 | -3.3975 | -47.49752 | 2025-07-27 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc122f40-6db7-3efa-b189-727d835c6938 | -7.607 | -61.21575 | 2025-07-27 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 22149242-24e0-3bd8-98d4-bfa3a9a855e3 | -6.49507 | -56.20352 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b5977ce-8aff-3183-96b0-fae2ae804f92 | -6.68353 | -58.84496 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e61645d0-09de-3c8f-8f1b-44fc8ea85e5d | -7.56318 | -61.40586 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa8df221-5e5b-3e00-b0b0-3ac2746778c2 | -2.74085 | -48.68655 | 2025-07-27 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a139809d-0ea7-3005-ab19-e8b631a3a4e6 | -6.65455 | -58.8292 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dc3338d-25c3-35bf-aa0d-bd9bbe0b6b6e | -6.64262 | -58.83865 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 740da98f-e931-3102-b7cb-443e5dfd6d3f | -3.40328 | -47.50397 | 2025-07-27 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57238325-e57a-3f4c-90e3-f2676cf1d329 | -7.74694 | -51.12677 | 2025-07-27 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ddd3b81-af55-36f6-aefd-620bc580e86a | -6.64092 | -58.84966 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7bd276d4-c9a9-31a0-b3e3-4e91d72ce864 | -6.65568 | -58.84443 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b09b48c-3c49-3523-bbe0-0f5dbbd59e23 | -6.62559 | -58.85853 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c41bd5a9-efc1-3c8c-9fe6-712192f2de0d | -7.74738 | -51.12353 | 2025-07-27 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ee4ca23-673b-3c33-936a-c72703aca479 | -7.5704 | -61.40342 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 242dfcbc-c8f1-38e1-ab97-b6facca28965 | -7.7591 | -51.12053 | 2025-07-27 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e698f2d-b595-36a5-81be-077105d733dd | -9.43797 | -51.75601 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5df23e5-03a5-36c1-8c25-1e0d1529c51a | -8.07259 | -63.86155 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4cffbff-4cd4-3118-a1eb-3315c2acf987 | -6.64717 | -58.83181 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65e95edb-dbcb-3854-9769-799673eedebd | -10.297 | -57.05111 | 2025-07-27 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ee9d6d8-5032-302b-9e05-7892d408bba3 | -6.66591 | -58.84601 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eef8e82d-b214-3afa-85bd-4e54b6124889 | -7.49525 | -63.8243 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f068351-b4f5-337b-81a3-c11fa117c60f | -6.66535 | -58.82711 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12e049ee-ccf3-34c2-aa5f-616719f6ab43 | -6.64433 | -58.85018 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b6f1f23-0549-3473-ad82-f542f949a842 | -6.62159 | -58.83919 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 296e69f4-0547-3a15-a8ce-6306b9ba97be | -3.0706 | -49.50184 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2913e909-388d-3b5b-be04-f0b04d1fa75c | -6.65171 | -58.84757 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90dd867a-eec5-3fb9-8352-9a31a0784aab | -6.62331 | -58.8507 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16815f1d-f9ea-3d51-bd5f-dc3e6f2667e8 | -6.65853 | -58.84862 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d687b3d0-65b8-3b6f-9ce9-a7f5f07a96a1 | -7.10337 | -59.76527 | 2025-07-27 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9f3a33b-104b-327b-a2a6-82798982515a | -7.56707 | -61.40289 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6021ba35-ab1e-34f3-8c28-a34dbe5bc6c9 | -6.63636 | -58.83392 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d3ecdbf-966d-3935-a953-7583389ca160 | -6.66705 | -58.83867 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2058ec9e-9dd1-3669-9048-17706cac8306 | -8.07328 | -63.85744 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90ca3eb9-065e-35fb-857b-3dc07d482715 | -6.67216 | -58.85073 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c67fb116-5fd0-3fbc-8434-1b515f6ded28 | -6.65114 | -58.82866 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 008e5da2-44fe-3ec4-a56a-8732405da1d8 | -5.91744 | -61.30252 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72f730bd-51b1-34ff-af83-dcc3e094b91c | -6.67557 | -58.85125 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a922ca2-cc4d-359a-8fbc-a7bde5328d72 | -6.64319 | -58.83496 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16d10c34-e8b5-39af-a4eb-5377647a2cd0 | -7.29296 | -60.17892 | 2025-07-27 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 247dea02-2918-3413-83b1-b839cea300dd | -6.67898 | -58.85176 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28ea8a71-9d5b-332a-80d5-99800bd3b15d | -9.46384 | -57.85081 | 2025-07-27 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47b999b6-c655-3d73-8feb-2af204ea3091 | -6.55214 | -56.19229 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14b9e335-83a5-3167-a337-e9c38e4b437e | -6.66307 | -58.84181 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c511f58-6ceb-3c3d-bd36-34236b67200d | -6.53592 | -56.19488 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99b31564-fb21-3323-b6c0-645bd441795f | -8.60696 | -64.03775 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ce2cee5-004d-3a73-a13f-452de041ffc1 | -6.55915 | -56.19822 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee7f7504-a968-3308-8423-662d2348ebd7 | -13.09804 | -52.1372 | 2025-07-27 05:25:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76df6f66-9e28-32e6-b5d7-f3a47d981524 | -6.62387 | -58.84705 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5dd76fd-256b-339c-a47e-3649402a9916 | -7.60312 | -61.2187 | 2025-07-27 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b203d01a-d535-350b-820f-be4fe6ce1111 | -9.91802 | -48.90044 | 2025-07-27 05:25:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4590ecea-936d-368a-9f8e-98a6b5a0ce24 | -9.43296 | -51.75186 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd2eccfc-c1f4-3eef-a145-6676c9fd1f2a | -3.06425 | -49.50489 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1046ecf1-996d-341a-b8f9-453717333e18 | -6.66137 | -58.85281 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ecd6efa7-0f37-3f00-b90c-91bd7ae19ffe | -6.63979 | -58.85697 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a7b5a467-22ca-3e6f-a9e3-5ade5e664e15 | -6.65512 | -58.82552 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ace85a14-0a0d-34ba-abad-b315b6a2d0ad | -6.63238 | -58.8371 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea8b87eb-0338-3ed6-8827-fe6838c3c491 | -6.67899 | -58.82924 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae0dd63d-0f8c-327b-8096-672852e97cbd | -6.67614 | -58.84757 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d9b6f7c-b7c6-32a6-9fa0-515ed68b0da0 | -6.63807 | -58.8455 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04670ba0-64c6-318a-b858-c7c1dfe215b8 | -6.65853 | -58.82605 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README22.md)
