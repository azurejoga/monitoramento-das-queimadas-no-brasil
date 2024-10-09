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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27bdc9a6-5866-3df2-9b9e-24bd1139ef66 | -7.35396 | -47.11103 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cdb505d-a977-32e3-8876-02099b5fdf1f | -7.35352 | -47.11429 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3cd9c59-2730-3d21-9c2e-58e14ef03adc | -7.34871 | -47.11038 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 568eb69d-2a5c-3230-adaf-7b0e37ddeadd | -7.04494 | -48.06182 | 2024-10-09 05:01:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e931e78d-b35c-3105-aa83-690d16bafdb0 | -7.0079 | -47.37071 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3324113a-0b07-3a64-be1c-8bca75239767 | -7.00749 | -47.37368 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 293f8679-02ca-3aaf-9ff8-caa785a2e27d | -6.96546 | -47.39269 | 2024-10-09 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d99a8b68-d3b1-344e-9c88-c7dd267e497b | -6.94105 | -48.17622 | 2024-10-09 05:01:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59999be9-aed3-3d08-aec0-dee9e3e8621e | -6.66853 | -47.10642 | 2024-10-09 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 262dbcb0-ef45-32aa-bda5-2b1bf0702143 | -6.66809 | -47.10955 | 2024-10-09 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07a14548-804d-3ac8-807e-f2f6ccd5d486 | -6.66293 | -47.10868 | 2024-10-09 05:01:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8887fd2-888b-3264-bac5-9976bf1adcff | -6.61931 | -47.08052 | 2024-10-09 05:01:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acc096c2-69f1-31be-bf9a-5367bb332b7a | -6.61888 | -47.08364 | 2024-10-09 05:01:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa50c3f7-6b1d-3ad5-b1b5-4f9e8e2e5215 | -9.20911 | -47.95589 | 2024-10-09 05:01:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab9b2d47-c7b9-3991-b6b3-550a8b5c9725 | -9.20871 | -47.95885 | 2024-10-09 05:01:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43beff32-43a5-3079-9897-40602a4333cf | -1.84794 | -47.85216 | 2024-10-09 05:01:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2d25884-18da-3756-82e7-769dcfd55678 | -1.84338 | -47.85146 | 2024-10-09 05:01:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 177bf627-017a-3ede-8ae3-615fbd4e7594 | -3.46169 | -47.66086 | 2024-10-09 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae1b0d42-4c90-3609-8f63-1801ec432e93 | -3.11686 | -48.6356 | 2024-10-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f750774-ac5b-3782-9f2a-5ccd98afb894 | -3.11245 | -48.63493 | 2024-10-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe627dcd-fde0-39d3-a78a-fc656a051369 | -2.9427 | -48.74556 | 2024-10-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b239b2f-1070-31ca-b44e-6dd0b6195608 | -2.79014 | -48.56417 | 2024-10-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f57fd588-04d9-3a4c-b2a1-4cacfe1dbdfd | -2.78947 | -48.56852 | 2024-10-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08c01d66-5cf9-33fb-a43f-c9a18a1822de | -2.78881 | -48.57286 | 2024-10-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28c94628-ca30-34fb-9677-f55e8a556dd9 | -2.78658 | -48.09838 | 2024-10-09 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a675b40-3750-3dda-8ce2-47cd8cf2c16c | -2.76455 | -48.64349 | 2024-10-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb08a916-1c86-3d0c-ae1f-7ffb6f481ffb | -2.7237 | -48.73643 | 2024-10-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecee4472-a8a9-3c11-8b72-83dfe0be057f | -2.71934 | -48.73577 | 2024-10-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8daf6f7e-5007-3038-907b-12557433114d | -2.71498 | -48.73513 | 2024-10-09 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f80da41-45f0-3b79-8304-73f0d59863b3 | -2.53801 | -47.62466 | 2024-10-09 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6cd593b-f813-3c2a-944a-953ba8ba11ca | -2.53537 | -47.62666 | 2024-10-09 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 728906d3-2202-3696-b5ba-eb8439e48819 | -2.4831 | -48.05284 | 2024-10-09 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c528b2a2-bae2-341d-bf00-1e1fcefbf92a | -2.47383 | -48.05918 | 2024-10-09 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df7d02f0-84c4-3fa5-8d65-60bc4f7d4413 | -2.47327 | -48.05614 | 2024-10-09 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ea6cffa-3f31-3f7c-8f3a-af011b6ea3e5 | -2.47315 | -48.06374 | 2024-10-09 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bbb9974-2d07-3199-8690-6d17ced78c55 | -2.47256 | -48.06072 | 2024-10-09 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9006ce8e-7cc0-3a66-87e4-6e753791b70c | -2.47185 | -48.06525 | 2024-10-09 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 832c386c-f3f9-3b83-9a89-98981753cbfe | -2.20443 | -48.15872 | 2024-10-09 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8af8233a-9d2d-3476-8ff1-b3f08c11ae01 | -2.18357 | -48.8256 | 2024-10-09 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd78a743-813f-36c2-94fd-a34c4e2e4732 | -4.49407 | -48.11995 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c1c58277-b7d6-3a85-9b67-39d114189170 | -4.4894 | -48.11925 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5448b98a-730e-3657-868c-319c41b3632c | -4.45972 | -47.96266 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf44669a-8779-3cd5-a312-849ccd9f411b | -4.38213 | -48.71259 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3adc6313-89d9-33c9-8817-323ec76651ac | -4.37892 | -48.7034 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 11b6d65e-5de5-3e28-b76a-6056764666f1 | -4.37829 | -48.70766 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c0fd4ccd-a167-3e9b-8d72-7897f3293c0d | -4.37766 | -48.7119 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f9826bd2-0ac4-3058-adf9-852d43fefda7 | -4.28563 | -48.63568 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a909b79d-0188-3735-be80-64b8ce15eabc | -4.28497 | -48.64011 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88df4b04-24b5-3422-8338-91190ebf2c64 | -4.28246 | -48.62609 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5efd59f7-ecaa-3465-860e-5b076afdabc0 | -4.27865 | -48.62081 | 2024-10-09 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e8f6e29-2076-3acd-a8bc-0fe99fa447af | -4.20385 | -48.1433 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83f4b3d9-4f99-31df-927d-5def49a5aa84 | -4.09905 | -48.25174 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09121fdf-7ba8-3732-a991-d260a4d9a8ea | -4.09835 | -48.25648 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a72af3c0-d69a-391e-b043-6ba56692bec3 | -4.09767 | -48.26113 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8f92f5cc-525a-3b43-bc70-57f4b74bf5e5 | -4.09698 | -48.26583 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ceb6e68e-5f92-3b6a-96a8-c8a29c2c933d | -4.09628 | -48.27053 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8924982b-a43f-3c8c-90f3-ff4de1bfb5b6 | -4.09446 | -48.25099 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70a0bc1a-dc4a-375b-a29e-9b3423730c10 | -4.09375 | -48.25583 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3608079-0edf-3196-8629-66309df4419d | -4.09306 | -48.26051 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0e6e7fd-ce23-39d5-8fc2-f66c27082fd6 | -4.08573 | -48.2785 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 883cb978-1ba5-3594-8928-9ff23217f7ac | -3.94083 | -47.96066 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07f0fdf6-77ec-30f9-a64c-a68d35d4a28c | -3.94009 | -47.96565 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77455da0-0c02-3350-8d63-297f0ec8122d | -3.93541 | -47.96494 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a5e467d-3408-3744-b6af-6bca715e07be | -3.9114 | -48.34707 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f70f1ba-e864-3b21-b0af-55d9ca8027da | -3.91071 | -48.35163 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc1159a3-e44b-30ee-8f71-36330b89b38b | -3.90751 | -48.34195 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 494cb5ef-1961-3cf2-a364-6a0bc6f33c74 | -3.90682 | -48.34655 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd0fb1d7-5929-3b31-91ea-cca7dfd92c71 | -3.90614 | -48.35106 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39f945cf-94c7-3f1a-ada5-a7b5725519df | -3.90295 | -48.3413 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f233757c-e893-3206-9483-00f0c3297b57 | -3.8977 | -48.34525 | 2024-10-09 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 610ea658-fd16-37c4-9ff0-2e5afb6ff812 | -5.85349 | -48.16168 | 2024-10-09 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 440ff228-b18c-3f8e-adda-6db2cd7c5f42 | -5.84874 | -48.16092 | 2024-10-09 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ea70aa5-d47a-30b5-af84-c1046b0c6bee | -5.72618 | -48.9777 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 672cf729-fcd0-3322-8373-0647823b6327 | -5.7217 | -48.97701 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 368a4988-8afb-39a5-b860-d71259148a45 | -5.51319 | -48.96021 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6646c633-4680-3eb9-bc1b-d64e2251d759 | -5.43314 | -48.32317 | 2024-10-09 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15f17df3-2aeb-3b74-b265-e03f295f7458 | -5.43243 | -48.328 | 2024-10-09 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f612efa6-1de5-3e12-9e4c-ab23a93d8565 | -5.74927 | -49.25239 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b00c3655-88ae-35a7-a0a0-6625706ea107 | -5.74906 | -49.25353 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1098e43d-a6cf-354c-a410-adeaf8f7bbab | -5.74778 | -49.26208 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4df7e5b8-71bc-34ff-83f8-4278270195a8 | -5.71007 | -49.27399 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d6f7b18-feb8-32b7-a901-45e42973a289 | -5.70944 | -49.27827 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f58b367e-f7dd-3648-8dac-0301e557ac79 | -5.7088 | -49.28259 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3df84e35-d0c9-368f-9042-1ff0cc50b09e | -5.70687 | -49.32602 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 510c81f2-7ed4-3b6a-930c-2de83d9cc85f | -5.67369 | -49.27738 | 2024-10-09 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de38ed71-d0d6-3923-a255-9c1946943437 | -7.43858 | -49.68526 | 2024-10-09 05:01:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33ea1a57-35de-36bc-a260-0e2883944734 | -7.12036 | -49.86612 | 2024-10-09 05:01:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b70fcb6-b7d1-33b3-8b2a-6a995d738333 | -7.11607 | -49.86536 | 2024-10-09 05:01:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cd51cb0-3469-3979-aea6-535cf2caf3bc | -7.11177 | -49.86468 | 2024-10-09 05:01:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 35484337-f1cb-3325-93d3-e005cf0b6e7c | -7.01517 | -48.54649 | 2024-10-09 05:01:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 61b78195-c2f0-3fe7-aa4d-20bb1764a4d7 | -8.7484 | -49.78484 | 2024-10-09 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62f373f6-7207-350e-8bc7-a866d416a5a6 | -8.52536 | -50.02803 | 2024-10-09 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0caf021b-da0b-351c-bc79-3fa1687760d9 | -8.52102 | -50.02734 | 2024-10-09 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ef0e212-8ef0-330f-8f94-6e4a8f6e3a5a | -8.37702 | -49.62208 | 2024-10-09 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d237d61-1c16-3e74-8bb3-0b25a026f066 | -8.33953 | -49.66187 | 2024-10-09 05:01:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6ee2587-2e7c-3e55-a19d-8d4590705f09 | -8.30112 | -49.23577 | 2024-10-09 05:01:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18c8db2d-69df-3542-93a4-ae6099c847b8 | -8.07399 | -49.66479 | 2024-10-09 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d8e243c-674e-3ff6-888c-174df1396da1 | -8.07338 | -49.66922 | 2024-10-09 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ed975f2-7a20-3625-a2b2-94415744ea4c | -8.06954 | -49.66424 | 2024-10-09 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 545538bf-b6b7-3dea-806f-68cd8adbcbb3 | -8.06894 | -49.66861 | 2024-10-09 05:01:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README162.md)
