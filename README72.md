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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f504754-2b5e-37a0-92c2-c3bcb30eae36 | -2.3024 | -48.57347 | 2025-10-16 05:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a176f1a1-03a6-33d3-bac4-9478daa345bf | -4.16045 | -46.79594 | 2025-10-16 05:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fa315fa-a88b-34c5-9ec9-e82798206289 | -3.5953 | -48.8811 | 2025-10-16 05:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b25f0563-d5a5-3110-a533-81529cdbc27f | -3.6865 | -47.63323 | 2025-10-16 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bb606343-6925-30c2-9066-b258e46baef9 | -3.66821 | -50.27364 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ce175f5-49a0-3246-bd13-3990ee020959 | -3.13871 | -50.21494 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0f7afb6-2928-3867-89ef-cfe9796854a0 | -3.46678 | -51.12502 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39dfd442-7c0d-37cd-8573-5de984a5bc63 | -3.92494 | -47.69526 | 2025-10-16 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dda30edb-6f98-3383-81a2-01e1a99e76a5 | -3.37273 | -52.80058 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6145bda-cf02-3f11-9c94-97b0979ada23 | -2.26024 | -56.05812 | 2025-10-16 05:06:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbf45794-9d03-3b17-b308-e5abe51dc685 | -4.3901 | -43.39808 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| b5b333f6-8cf9-38cb-92df-d3b2ca7cc47d | -1.48842 | -55.6805 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2392f199-9aea-34fb-8505-5b5a321cdef3 | -3.81963 | -50.93434 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7c0ab4e-4870-3705-afd4-9e276374a065 | 1.75804 | -55.76637 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32f39944-1fc7-3793-b725-eba2711aaa82 | -4.38779 | -43.41417 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddb2ac80-5127-3c08-82f2-6d85fb8f71d1 | 1.81245 | -55.93956 | 2025-10-16 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41a3c2cf-e5a9-3c29-bd6c-2b0e90be54b8 | -2.87541 | -50.73642 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad674809-fef2-39ca-983e-f007c1968208 | -3.29787 | -50.01122 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d3f2fc3-d393-3d64-b34b-6f1afff448dc | -3.17456 | -49.7538 | 2025-10-16 05:06:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3357d36-151d-3833-829c-159cb563e81f | -3.41648 | -51.47507 | 2025-10-16 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 131162d5-411e-36cd-b83a-267acc86a9b5 | -4.38935 | -43.40328 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a8768218-bc23-30f9-ab13-e847a8b82d0c | -4.39656 | -43.39899 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 88fa6088-bf4b-3cf4-9d5f-1b5db18e880f | 1.74502 | -55.79476 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb91c2c4-b148-356c-a88b-c7eeb6795d34 | -3.83827 | -44.54602 | 2025-10-16 05:06:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 729a95e3-2206-3ef3-91eb-0964ca25c517 | -3.47324 | -50.02665 | 2025-10-16 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cd973ef-6f94-3b0b-a11b-69bc77c0c6a2 | -3.65639 | -51.7482 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7fd7dba-c88c-3a9f-a883-f14786889b81 | -1.48809 | -55.44393 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b12f0e80-ea97-3c11-b59a-523c66ed424c | -4.66426 | -44.09363 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4edc94b3-09b3-3018-9d57-6bb8ead929a9 | -4.67116 | -44.08984 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7c57d4e3-36cb-30d6-a5c7-58ae325f8d7b | -3.60099 | -48.99127 | 2025-10-16 05:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1bd95be-fe86-3d2f-a6d0-ba968cf81d5c | -3.27134 | -45.84149 | 2025-10-16 05:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d53002c3-4bc6-380b-a835-9a039cbf47a1 | -4.72897 | -46.15923 | 2025-10-16 05:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54f154d9-d834-3f8a-9d8b-972ab404952a | -4.3844 | -43.39186 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f513a774-32ca-3fca-bfcc-72bda3932200 | -4.56277 | -44.00418 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b6fd3fb-fc0b-32e3-8315-3d70a3167aa7 | -2.70333 | -49.86379 | 2025-10-16 05:06:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b085d7fd-0d82-3203-a6c2-4df60d5a3148 | -4.28995 | -48.58103 | 2025-10-16 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 953cce8a-e091-3db8-9e62-46650bbcf8b1 | -4.86795 | -44.58263 | 2025-10-16 05:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45f79fab-ec7c-3487-a2ac-29379947409e | -4.66214 | -44.10801 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f8e2caf6-216a-3821-b934-9ff69e069276 | -3.68088 | -47.63774 | 2025-10-16 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 090b6f49-73be-31cc-8e3f-95f2443178bd | 1.04354 | -51.04192 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22a548e3-e0bf-3371-8230-06f7c77040d4 | -1.49198 | -55.44096 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 807e4743-09b0-32fe-804d-31a0b81a2a66 | -3.01337 | -45.38797 | 2025-10-16 05:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0e22b9aa-ab0b-3f63-881a-6891cec0da3b | 1.8287 | -55.75159 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8358082e-521a-3b71-a46e-72ca57d9d8fb | -2.70445 | -49.85656 | 2025-10-16 05:06:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e10a0c7e-d5c7-3978-96fd-ab6108ceeaa0 | 1.22442 | -51.03193 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8d630213-2061-37ca-8c19-179525eaea92 | 1.84116 | -55.7196 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd2917b1-5c64-383e-9abb-9ca43c5fe629 | -4.4038 | -43.3945 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9086c63d-28fe-3fbc-83ff-f38b87ae1e08 | 1.06196 | -51.01784 | 2025-10-16 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64f04f8e-a178-39ec-aa52-31a70bb3a987 | -4.11063 | -48.02468 | 2025-10-16 05:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| b8c3ba41-42a5-31e1-8495-5fc06e8a8940 | -3.01502 | -45.3768 | 2025-10-16 05:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d419ee0-bde3-34b7-acf0-ba41a7711b02 | -3.33201 | -53.24686 | 2025-10-16 05:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 736d17e9-6214-3fd5-97df-65e7e70aba8c | -3.66008 | -51.74879 | 2025-10-16 05:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd1389b5-575c-3451-883e-1a1541c31c01 | -1.48919 | -55.43696 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5278dd21-2860-3fea-ade9-e55999422c17 | -3.51672 | -52.494 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69fd2b6a-4b74-3072-b7f0-7671a252f99b | 1.81787 | -55.74953 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bab623de-a608-38c1-8e61-70603ba7fd13 | -3.12721 | -50.20948 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77eb34f1-9750-3348-805d-bca17faf1759 | -3.5106 | -52.49389 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 41e157de-56ee-3c40-98db-23fdb2c1d7f1 | -3.28938 | -50.14817 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5793ddd-d638-32b1-8c6b-65b856ac8380 | 1.74276 | -55.80265 | 2025-10-16 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee0784c7-4460-344e-8878-8ed5a97085d5 | -4.3829 | -43.40231 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2bbf6837-209d-3f13-a9d1-5a7d55cafa03 | -4.87524 | -44.57483 | 2025-10-16 05:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc21bf21-3ee2-32bd-8bdf-2f25058d2067 | -4.66073 | -44.10924 | 2025-10-16 05:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 31a261d7-284c-375f-aace-757f5d4c58c5 | -2.87466 | -50.74123 | 2025-10-16 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6ebb35f-7109-34d7-8b6e-53534a4f4db6 | -3.51478 | -52.49041 | 2025-10-16 05:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e608995-8440-3c74-8f37-fc82c446f2bd | -4.40458 | -43.3891 | 2025-10-16 05:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 32ba4175-65af-39de-81b3-8a204b13129d | -10.65129 | -45.24243 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 738a396d-8e48-3dc8-bebc-16d661f5f782 | -9.687 | -44.504 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36df834e-b208-3ff4-8f50-4ed56b212c04 | -5.87365 | -43.88263 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f36754f-b5fd-3d96-9e6d-42e8f51da573 | -7.0797 | -44.95185 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 213a6e0e-d805-3d5d-b093-c0accb2bba15 | -9.22959 | -48.59839 | 2025-10-16 05:08:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd34facb-fd25-3491-a772-274206a148c7 | -5.65868 | -45.96519 | 2025-10-16 05:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adf9b678-f9a1-3819-b934-669d38b550c8 | -7.41169 | -44.75166 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5d0a7fb-1bf3-3ce5-a9ab-1fce328a86c2 | -7.48117 | -42.75621 | 2025-10-16 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 04cd94a4-5ccc-30c8-bf14-1c11aa93c500 | -8.47016 | -44.18869 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1656d5b6-1aeb-35e5-b58a-d8308ab9aec2 | -5.88009 | -43.8832 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd3cbaaf-62a3-383f-ba30-59e1212756b6 | -8.23472 | -43.32613 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bef26134-039e-38fb-97b8-cce5090ab336 | -10.89335 | -47.92223 | 2025-10-16 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 126bcb7f-a306-37ac-81d3-d559bc766e12 | -7.07368 | -44.95058 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 174425a7-40ac-36b7-9e3a-d80248e9778e | -5.87744 | -43.84958 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbaced9a-d4a6-387a-8db7-f79d6e439b7b | -5.32486 | -43.94209 | 2025-10-16 05:08:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 757ac4ea-6cb9-32d0-bafb-c8bf52a2ffc2 | -8.20091 | -43.31569 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| dbbc642a-d194-3b9a-a419-bbbb1ec91abf | -10.16469 | -47.11261 | 2025-10-16 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 845c87d2-a0c5-3d90-88bd-1f326d7584ab | -8.45494 | -46.17887 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6c793cd-c7d5-35aa-9907-b4edff633ddc | -6.1943 | -52.73621 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f61f332-68e8-3706-b020-4a685da12d13 | -5.4772 | -42.9268 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d618a01b-a21c-356b-a411-f9e469b22d65 | -5.83851 | -42.33878 | 2025-10-16 05:08:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| db24bba4-20cc-3a1e-a903-15ef0377f62e | -8.20016 | -43.32157 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| b699e5b9-072b-3ed1-a256-32850ea86528 | -7.04287 | -42.73721 | 2025-10-16 05:08:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac64b288-a6ad-3daf-84ff-341262c7b3bc | -4.34762 | -50.54296 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98d3f68e-eb60-3d02-8890-8a721da1d522 | -4.97691 | -47.10606 | 2025-10-16 05:08:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 839203f7-07df-3be9-a407-7c6545ef8de3 | -10.6359 | -44.42324 | 2025-10-16 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 937f47d1-720b-31a4-81b8-c3c5053ec525 | -11.00449 | -49.57713 | 2025-10-16 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 546f0339-d328-3266-ae6c-9f7e744fd4c4 | -6.03189 | -44.31929 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcbd7440-3a72-30db-b3a1-ff8b12024c6c | -4.35162 | -50.54354 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cd3479a-2a03-3c4b-89c1-651b4a309f7e | -5.92576 | -44.73068 | 2025-10-16 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fd61589-3aca-386c-a4b6-786328870501 | -7.50905 | -46.64113 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae12effd-5f16-3082-9336-c3fb740992f7 | -7.24125 | -49.51635 | 2025-10-16 05:08:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a342a2b-fec3-3899-b688-cac6eceaa5d7 | -10.12429 | -44.58876 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 263de55c-23ba-34a0-b0eb-2ef30439fefb | -7.94845 | -43.268 | 2025-10-16 05:08:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 32416bfc-d8c0-3a19-a4c0-66a4283cb091 | -10.83026 | -43.95028 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README73.md)
