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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 344636a4-0d0e-3148-8717-d3c181cca955 | -3.67415 | -50.22945 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c1ff4a79-fc7c-359a-84eb-719d4f9f5d7c | -4.2811 | -48.64556 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e0c297b-fc6a-3e24-ad7a-4727b761efe7 | -3.71181 | -50.14409 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6652aebd-4c09-3082-9cfd-0f41444eb437 | -3.01186 | -53.23814 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf61b401-942f-3b4a-923a-3f8c8f9843f4 | -2.75465 | -46.81351 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ac6587e-6f54-3bd0-8c09-985b840623bb | -2.23532 | -50.69781 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ec0f197-ae6c-3481-ae4c-85ed8dc22ed0 | -3.05925 | -50.50027 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8fc6efe-947c-3a5e-8bf6-e10b4cf6a779 | -3.05003 | -51.06651 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83b613ad-a515-30cf-b7f9-d3bc7e4027ce | -3.85014 | -47.07191 | 2024-11-06 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ff05c868-ea33-3158-9b3d-ea4559f51ab8 | -3.06029 | -52.50473 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 312fb646-8066-32f0-b4de-f557d6adcbde | -4.7365 | -48.97109 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8715b3f6-2aa9-3a49-a10c-9965a711e1bd | -4.93796 | -43.62738 | 2024-11-06 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d034f72c-6e50-342d-828c-139d03007ea1 | -3.23514 | -53.39697 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7549917b-e203-300d-92e0-f29b55328763 | -3.03608 | -53.26218 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b17959b-a4f9-3095-b433-4fd35bcc7c93 | -2.278 | -49.10994 | 2024-11-06 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4524a994-d8eb-3449-9dda-4019ba2ffde4 | -3.70211 | -51.84463 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb9f7a09-cce9-369d-aae5-a1de95b434f7 | -3.44288 | -51.62685 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0a524ab0-bc8b-30e9-8dd2-c0157126b683 | -4.35967 | -48.64409 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 507f49eb-cdf3-3535-95ed-63cf47696140 | -3.77809 | -51.29573 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d7e5b52-bc0d-3fbc-a76c-82e60b6d8fe4 | -4.36216 | -45.75894 | 2024-11-06 04:36:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2285fa0f-2dd9-3669-9d1d-c4623274c90f | -3.11941 | -51.11252 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de74e498-5070-33cd-8ba6-021ea043d3f5 | -3.23328 | -45.55585 | 2024-11-06 04:36:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31ec2324-9ebc-3b2e-9fe7-607808164c66 | -2.8291 | -52.92573 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab63ea71-e3eb-30fa-8e3f-b85f69d00803 | -2.86051 | -48.45462 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdc8799d-3a68-307c-b2c1-b1c44b8f7c7b | -3.17584 | -50.58253 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c085b259-8f34-305c-8310-d3cb5fe8539c | -4.48509 | -48.49331 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88879264-4752-33a8-947c-c3eb9269c1cd | -2.45363 | -49.0312 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 156558b5-acee-3841-a879-87219840d14b | -2.9738 | -51.43437 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a98f238-0703-3222-aad6-3b47989e9774 | -3.09939 | -50.2499 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a1775d5-6b67-3832-bd33-4097e7717583 | -2.58218 | -46.11837 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 432ba6e0-c12c-3ef6-93b1-b92a9d31d55f | -2.90605 | -48.59531 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f963e0da-41bb-3fc9-a59c-b9db3f3c4df6 | 1.20715 | -50.75947 | 2024-11-06 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ad8f131-6d2f-3cd5-83f0-1ac054a78233 | -2.38764 | -49.77403 | 2024-11-06 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92e99dfa-583a-30ec-875d-7193ae9a3b1b | -2.84728 | -49.44373 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32039435-3f45-3f40-9081-fece785282e7 | -2.82373 | -52.95914 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4fc96d79-5c3b-3def-991e-89fbf19434e0 | -3.17938 | -51.25996 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17512d7d-1473-3f19-951c-06f0a688371e | -3.85369 | -52.14211 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfbce469-91d0-33bd-be57-a319ed96460b | -2.67259 | -48.65397 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 038c4175-701b-3a4b-b9be-8469d9a374a7 | -2.451 | -48.85462 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88d0e928-ab36-3764-b684-f3208dbfe3cb | -3.97195 | -48.16862 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2c6d91ad-4e37-3c2d-b9d0-856f63126f40 | -3.06206 | -50.50448 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83bbfa5e-2b28-341d-8af0-34591d1aaf1b | -3.3351 | -51.14563 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bd0b850-efe6-3489-a1e7-c92a1724a7e0 | 0.187 | -51.0609 | 2024-11-06 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ab4e359-eefa-3f7a-bcc6-11819c3a203a | -3.2299 | -54.86217 | 2024-11-06 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2d4ef38-ce26-318e-85ec-629d97dac6ea | -0.84961 | -52.84155 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5739442-9b23-3934-9825-f1354d35b39a | -3.03098 | -51.20982 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1358d7f1-5ca5-3f95-8386-0302f2604210 | -4.75495 | -45.90763 | 2024-11-06 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f70bbad7-7376-3a53-b7dd-4c791ee2bf53 | -3.12637 | -51.11364 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c5c9cbe-7cce-3df1-b78d-b54ca24d3c23 | -2.91669 | -51.04291 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9cfb6149-e4d0-30f9-a8a2-ab8f695b3743 | -2.82833 | -52.90603 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 52a53863-89cb-3807-90c6-327062cf1e4a | -2.63834 | -51.75089 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af19088d-c33c-318e-a211-774ae5b39202 | -4.75072 | -45.91116 | 2024-11-06 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06c70bf6-39a0-34bd-8a37-c7ffaaa544eb | -1.42478 | -52.18053 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5efcacbc-fc27-358d-9785-447199735358 | -3.83415 | -46.49462 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac6cf6a5-cdd5-3ba0-8f0f-d73b1a16627c | -3.09746 | -45.94451 | 2024-11-06 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fefb293-732a-34ec-8bc6-64b3e866ce8d | -3.48542 | -52.10396 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7a82018e-4c2f-3d98-bb4f-ccae4d407b10 | -4.68936 | -46.39185 | 2024-11-06 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d00b49c0-ba67-3126-831a-94ba8be7e350 | -3.18037 | -49.74258 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f918dc60-f886-3164-a8d4-52b135b3e8f8 | -3.79252 | -51.43656 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b151192e-f66c-309a-9ee4-3a38d78079da | -4.23616 | -48.54324 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 55697534-515c-3464-bd93-01d54e4c8c51 | -3.73025 | -45.92375 | 2024-11-06 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3174b526-5ca1-38bd-b838-bcfa534aab01 | -3.10656 | -50.29166 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f7cd5ca-3ac0-309a-ace5-fc0bf8a84be1 | -2.44701 | -49.03016 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d030662e-b924-3cba-b2ed-e33378bf52c6 | -3.76346 | -52.1708 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd272b6e-8d0e-39ec-b9db-0a4b4686458a | -2.79817 | -51.49015 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e239266-f32b-3bbc-97b4-5ce190e40cfe | -2.48416 | -53.98467 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c77a147-cd47-3190-a20a-a930abb3cc69 | -3.23429 | -53.4021 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 038768c3-5eb4-31e1-a51e-b3ca4a110a5d | -2.84676 | -49.46858 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6214809c-50f4-34ff-98c8-d7bb98389e06 | -2.94207 | -51.06266 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26692675-3b71-3181-86dc-d2be32b56c68 | -2.60479 | -49.19301 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84038bbb-51f0-38f0-8752-96a7ef2c0191 | -2.82067 | -52.95362 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| edd27f83-b43b-3341-b323-4ad6e4f2571f | -3.22881 | -50.38143 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 94275ff3-8139-3abb-b862-606bc33532b7 | 1.35023 | -50.875 | 2024-11-06 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ea6dd670-1a75-337f-b43b-7c143a33f91f | -3.25298 | -50.18589 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6407930f-d9de-3219-b6f9-0f2a59441d2d | -4.60007 | -48.69193 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e426a9cf-b881-30e9-9624-7c41e56288be | -2.76107 | -53.22387 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb168dad-0177-3513-91ad-bec9d4b48b20 | -2.89736 | -48.62912 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f0099c6-579e-32de-b3bc-500ca53f2f35 | -2.7965 | -48.57846 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c503ebff-bbcf-3496-994f-e1220d7b8fba | -2.81683 | -52.95298 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 95d9d0c7-9d07-3e44-99ab-b1496ec7e713 | -2.97158 | -51.02273 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccd7bbb3-fe58-3381-aaf8-a320b4c74814 | -2.90309 | -51.46807 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 504ed422-466b-36af-94cd-1a9152dd5263 | -2.85013 | -51.77157 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 86065982-06f2-3b65-bb14-878e4062695e | -2.82528 | -52.94946 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2d19fae7-ba4e-3517-a80a-085c700578ce | -2.87228 | -49.50109 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edce4924-583c-3059-ab3c-976dc11dc4c0 | -1.15778 | -54.07659 | 2024-11-06 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aaaeb704-0a99-3dd8-8e53-0928eb2226d9 | -3.95312 | -45.76616 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c38627d4-d9af-3d9f-85fb-897f54db7c80 | -2.90968 | -49.4147 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06534b9c-5fe1-36d7-a4c5-6ede1c141c17 | -5.47877 | -44.8618 | 2024-11-06 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d81cc807-2b39-3fc0-93ff-7fecfa121de9 | -2.05708 | -52.66794 | 2024-11-06 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d9ac6fb-075b-3d28-a597-d4ed09278c40 | -3.78078 | -51.32389 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60f476bf-4779-3b95-a1fb-73b4a8382f52 | -4.07896 | -48.30959 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f32f211-edee-3f38-b7e6-042fb258a096 | -3.53903 | -47.37767 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d2937e81-f53f-3b15-a2da-41e1a5aeec35 | -3.52873 | -50.35041 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9ff4c51c-9940-35cb-b6ee-7fef13290036 | -2.83225 | -51.80473 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1f953a04-3062-3fc2-9313-89aae0c5aac9 | -2.87819 | -51.30742 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d00842a-4ebe-39bc-8d7a-c129a152fec4 | -2.9179 | -49.3414 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecd57ae3-77a9-333d-85a9-32b9506a4fd2 | -3.97635 | -48.16219 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88792591-2f67-3e7c-8051-805b5740f414 | -4.56044 | -48.00928 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| eedd004e-7bfa-3f02-89d9-4a5fa3cf9744 | -2.41049 | -48.85173 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51e4f502-fe58-3c57-ba12-76b21a4080d0 | -3.75635 | -48.89451 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README45.md)
