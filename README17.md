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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc39c77d-7734-309f-a25e-88aeba6dc502 | -13.5944 | -46.99357 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87228679-7620-3ce0-914d-06ea999f7d17 | -16.47538 | -45.09515 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53b3f705-6beb-331f-a627-87fdc10e6ae6 | -15.79314 | -48.22583 | 2025-08-19 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6fcb2a13-4e54-362c-9961-9c0f7820c4b5 | -14.86805 | -48.06931 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2b1c8ea-d843-3b10-8d57-c15e1321a46f | -17.41819 | -46.70839 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af654dfb-d3bf-3e82-b296-09ae24e2a166 | -12.50086 | -45.56602 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b2c57b3-0c4d-3af5-8a1f-736aeda5a151 | -18.28312 | -49.61356 | 2025-08-19 03:38:00 | NOAA-20 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 13312607-b049-3843-8a68-a78e6fa7d91a | -14.86284 | -48.06256 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f07a460-ba23-34bc-bca1-f81f2476b165 | -17.8123 | -44.49376 | 2025-08-19 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5ab1a55-263e-32c3-84c4-4d3c78adfcbf | -17.28985 | -44.892 | 2025-08-19 03:38:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4b2b983-fb2e-33db-a1be-1473596abef0 | -12.92578 | -46.10686 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8044e3b1-cd63-3fc8-8b72-f30fed1e85d1 | -17.81367 | -44.48704 | 2025-08-19 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 238ee56a-5b69-34a5-accf-bed5c4258343 | -14.16972 | -45.31913 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91fc9c54-cd8b-39d1-b531-f4c89c6def9c | -16.4792 | -45.10269 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b60bcd0-588f-3840-9412-ed7bf1bc264b | -12.99349 | -45.1865 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01c79bd7-956a-3242-9c02-65f3fb022f91 | -12.99131 | -45.19773 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8086de07-ea23-3229-8d27-b9ab0bdb6893 | -16.4767 | -45.08877 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90f5f4dc-59b7-31de-9088-172b44da38fa | -13.5884 | -46.99004 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9b56912-8771-3fdb-8a18-95c5c9f80791 | -16.47615 | -45.08395 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c938fff-a562-3ee1-81db-e9464602218e | -16.49974 | -45.10728 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89f36aa3-275a-3996-bf6a-cb63406758fb | -15.7981 | -48.23346 | 2025-08-19 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cc1751e-4fdf-331f-8803-04886f4867c0 | -12.43096 | -48.70195 | 2025-08-19 03:38:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1b9e3e9-bca7-381a-a85b-ae02306a043f | -15.75222 | -46.60769 | 2025-08-19 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb6f878c-1394-3d69-bb43-19e680ee5606 | -16.47604 | -45.09196 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41747269-9205-3b61-a35a-4e319da75e89 | -16.19936 | -42.88039 | 2025-08-19 03:38:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aba16776-f3b2-3db8-a205-f8fa1760c97b | -16.40284 | -40.57138 | 2025-08-19 03:38:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b6034e97-e56b-3608-b55b-529f541c4271 | -14.52207 | -42.21063 | 2025-08-19 03:38:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 687bdac9-7aa5-3e06-b007-2b059afaa586 | -12.65586 | -45.81031 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f714641-34dc-3f1b-9015-0797e030e764 | -16.49012 | -45.1018 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 46aec2cd-8845-3f2b-8cc3-39c724e8069f | -17.3894 | -46.70609 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d448e748-0f8a-358e-8747-ff2f1afe252c | -14.17199 | -45.30515 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6657d1ed-478b-3104-8e01-52468a73cd92 | -16.4768 | -45.08075 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3ac6ea8-057d-31bc-9d2d-5b6e63019828 | -14.85848 | -43.88988 | 2025-08-19 03:38:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f64c944c-84e2-3aae-a6ad-b4496fc141c7 | -17.28547 | -44.8879 | 2025-08-19 03:38:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 769c9675-fa41-3b1a-a713-79c49143167a | -13.6219 | -46.89142 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33caeca0-8b21-3d9c-9deb-cd20e095b8e8 | -16.05729 | -44.58238 | 2025-08-19 03:38:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15339012-830a-30e7-8257-5b4010f5a093 | -12.92482 | -46.11153 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3e02cf7-3184-36db-962a-c65be9b816b9 | -13.86262 | -45.54328 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c56fbb9e-b097-34ce-9739-a64bd063cf61 | -19.81414 | -44.32871 | 2025-08-19 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8dd9a36-e5ad-3d3a-92e5-4a06c590a59a | -16.71251 | -47.62957 | 2025-08-19 03:38:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86bd8ebe-71ae-3b04-bbc0-64bb3b7b4492 | -15.75137 | -46.61172 | 2025-08-19 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f6f2bf1-3719-3202-8e76-43395d461b86 | -17.48776 | -45.85528 | 2025-08-19 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fe60b0f-d4df-3406-9d1f-dd894233175b | -16.47736 | -45.08556 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d3a7ef5-c254-33c9-bfc8-89b29acec61c | -16.47874 | -45.09792 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a8bbac3-c835-3c7e-b1ce-8c3d5f19287b | -12.99537 | -45.20641 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f552e3cd-3bba-3d72-8324-9d2061d9bcc0 | -13.61472 | -46.89547 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6dbf9ad0-bf07-3790-acb9-7737702bbb8d | -16.50488 | -45.10841 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fafd612-fe94-3410-9835-d47dde85837a | -13.59552 | -46.98805 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 508f0341-1f8f-3409-86e7-3c41c6f30a96 | -12.63588 | -46.89564 | 2025-08-19 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c55cec43-dc12-3584-b9bd-015f8630f598 | -12.49942 | -45.56613 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55de9ceb-adfb-3b41-8f2a-ec05e5b7cc69 | -15.74971 | -46.61676 | 2025-08-19 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d3572d2-d085-357e-a0c5-f498b344d4c4 | -16.47747 | -45.10431 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 515f7310-ff2f-3bb2-bfa7-142985f64291 | -14.17194 | -45.30818 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6405a78f-4a54-360f-914a-1ec940bdce7b | -13.8068 | -44.19846 | 2025-08-19 03:38:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbae0a33-1eeb-3a75-90e3-dc72b2f6e4fc | -16.78906 | -40.06405 | 2025-08-19 03:38:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 25d18da9-fb08-3d99-ba8f-a61e1d6828fc | -16.48118 | -45.09309 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0355d831-908b-3990-8fee-a9b32e246734 | -12.99637 | -45.19708 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa8ea44b-d759-3d40-84fd-d0c5d63f8218 | -18.95114 | -46.27291 | 2025-08-19 03:38:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66a64c5b-f60d-3af6-9145-6eacab30de80 | -19.81518 | -44.32359 | 2025-08-19 03:38:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20d79c74-3224-3be7-929c-3a0a958c554a | -17.3404 | -47.10332 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9cc75f6-bdbb-3f6a-97f3-fa7dbda32bb4 | -14.84264 | -48.06373 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24c2c420-e803-333e-8c04-cdb1afadde58 | -17.41904 | -46.70434 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3d4fdcf-1516-3381-b11a-f999f5cdf022 | -15.74461 | -46.61245 | 2025-08-19 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0f68710-4d63-31f2-9ffc-0f03926910ee | -14.16984 | -45.31611 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78db033f-62d7-3533-87d9-18b8663b6ed4 | -15.74618 | -46.60793 | 2025-08-19 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c7a84f7-d1dd-3675-8b72-f136d63683ef | -14.1712 | -45.31182 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a198c187-b3a1-33a3-8887-38e765df1bdf | -14.73854 | -46.30019 | 2025-08-19 03:38:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ca90a6b-9217-34e2-9898-2ce4b9a71e5f | -16.48129 | -45.08509 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 825d8a74-6c82-38cd-abcc-408203d1c7e5 | -12.42959 | -48.70838 | 2025-08-19 03:38:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27929e2e-d60c-391e-93d7-6e085e3a26cf | -18.94583 | -46.27186 | 2025-08-19 03:38:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 49c010d0-47fc-3a4c-8fec-4576aca245b7 | -16.4781 | -45.10112 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 422a14d5-80a3-3123-b3fb-27243d9bab34 | -17.33817 | -47.17081 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3344f20-358a-367e-8442-89bfb5b82b63 | -15.39391 | -39.33528 | 2025-08-19 03:38:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b368ce70-bb73-3976-ac3e-4025309e9f34 | -16.47552 | -45.08717 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7080dc3-c89f-3287-b5ad-3db1fdde6f55 | -12.64764 | -45.82116 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c47b90c-5f14-3232-8e8a-a587bd97a93f | -17.93274 | -44.36702 | 2025-08-19 03:38:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15524c80-9e37-3310-8103-10aaeb97ff52 | -15.74546 | -46.60833 | 2025-08-19 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31d34c15-e02e-3176-ae5e-bce32ea6eec7 | -17.28485 | -44.89093 | 2025-08-19 03:38:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f7fa7e0c-48d0-3971-867c-45719026048d | -14.86161 | -48.06831 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 895117a4-6615-3bde-8281-d9791e1b14d6 | -16.48052 | -45.09629 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c024b48-ed43-37db-9c48-2b752d3601cc | -16.00796 | -47.79128 | 2025-08-19 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beeb1c4f-176e-3025-86b9-684151c5678d | -14.85138 | -48.05399 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac3fda00-35e0-39c6-b357-6d2574a03b2e | -18.61296 | -46.68527 | 2025-08-19 03:38:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef5743bc-b36c-30bb-82b0-a8624dec69b9 | -17.41181 | -46.71085 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a65c831-dc88-3029-a1d5-60b7dd0fc601 | -17.28644 | -44.88738 | 2025-08-19 03:38:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0d04e27-6872-3ec1-94ea-2e9c6b66a9f0 | -13.42859 | -45.91105 | 2025-08-19 03:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9f6dd06-ec4d-305f-be26-5782956f43ad | -13.43513 | -45.90823 | 2025-08-19 03:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9422a05f-1ee9-3c02-8140-7e2e67226daf | -17.29084 | -44.8915 | 2025-08-19 03:38:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98e97b9f-0bed-39d2-892f-804f6becda80 | -16.48763 | -45.08782 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3069e5fb-0d98-3f3d-badc-2bdc35b6db70 | -17.5703 | -44.47428 | 2025-08-19 03:38:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d975d35-4947-34b9-a895-5bee5f8fde46 | -16.47473 | -45.09832 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1581a71-f13e-3f05-9bc2-e9b9cc98413f | -14.16576 | -45.31068 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e4b351e-9ec5-30c0-be32-fe03c0716c00 | -17.3442 | -47.17035 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e187200b-3787-3305-9a0a-dfafc76abcca | -12.99011 | -45.19965 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2d669dd-4249-3dea-9ead-59d4ab220395 | -14.17056 | -45.31245 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a9f8e3-87ea-3d52-83fc-539fd83fa636 | -16.47743 | -45.07755 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecf5a418-0e1f-3735-b33a-340c6c7911cf | -17.28523 | -44.89346 | 2025-08-19 03:38:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a44f12bd-ae45-3c1d-a7c8-f5078b5be9f6 | -17.98485 | -46.35593 | 2025-08-19 03:38:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3dd9904-f472-375c-8d1c-14c4912970f4 | -14.86048 | -48.07362 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8335336d-172e-35c0-9b82-da286bed74ea | -16.57068 | -40.66792 | 2025-08-19 03:38:00 | NOAA-20 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
