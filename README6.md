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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bca3c40d-9362-3a72-9ca9-0acfb3fb1c0a | -8.74602 | -49.74677 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c96af4ce-a797-343c-925f-ac7342aef21a | -8.75437 | -49.75253 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8d4659f2-c428-3d3d-a70b-b043a2a86a13 | -10.71745 | -49.62365 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42886a9e-cc9f-3aff-8bbb-c46184c077e5 | -7.20999 | -43.11715 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 0c656d6d-6998-3eed-bb2e-23d35dbb79af | -14.04739 | -55.13816 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9a622b45-fc3e-3b4c-b005-f48f5c8e0e5e | -18.84361 | -53.61929 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 03d97f6d-88c4-3749-b98f-37a210f84734 | -18.84178 | -53.62789 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90929209-6cb0-3915-aef6-8ebcd7f2fd2a | -20.06874 | -45.29525 | 2025-05-27 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21377a30-836f-3baf-bede-3f1776b62608 | -18.84742 | -53.62915 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cde62491-d46a-3bff-bed3-a42d5d5dca9d | -18.85583 | -53.61737 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 2cbb38a9-1b74-38d3-97f2-8fb0f9729273 | -15.88824 | -43.4561 | 2025-05-27 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 82765d68-838f-3999-ab63-d60f1a5f339a | -18.85613 | -53.62777 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dcc27cce-b5fb-3e73-bf22-bccf5d454866 | -18.84487 | -53.62519 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 13f45dc0-9fc2-3134-8724-fb40eac9e552 | -18.85111 | -53.61185 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1cc1f3a8-e31b-31c0-b871-c09255b028b3 | -18.83544 | -53.61433 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d1bb431-9e54-31ae-b141-8a430c5a8951 | -18.83503 | -53.60422 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82c41db3-52a2-37fc-bbb2-9608815154b6 | -18.84247 | -53.59703 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f2475e0-373d-342f-ab04-49f1b0b59c26 | -14.14896 | -45.48123 | 2025-05-27 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78421a6c-23b9-3b8c-b82e-1e20b8167310 | -14.65599 | -45.08881 | 2025-05-27 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db54d9b4-a16d-37eb-a325-ac6205b8b6e3 | -18.83703 | -53.62242 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32704ecc-a509-3113-b075-66ed986e1a9f | -18.85338 | -53.61342 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a8b41f05-401d-33cd-877a-65edbfa061a8 | -20.06532 | -45.29465 | 2025-05-27 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f5d9da9-cd4d-3acc-b193-0b29ec51d532 | -17.78271 | -42.80825 | 2025-05-27 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2799e404-f24f-3eb3-8fc1-c4687beb7c0f | -15.89158 | -43.45667 | 2025-05-27 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8beb3a2b-3d22-3402-8634-ce95964b717b | -17.61112 | -42.55733 | 2025-05-27 04:04:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc5b7cb1-e732-3c03-9095-4a5cb51c47c0 | -14.14682 | -45.47161 | 2025-05-27 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 416c8019-c91a-371b-a402-b9424242872c | -14.02062 | -55.13183 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08ef6b9e-c03a-35a7-9529-cfe128ec77c5 | -18.84389 | -53.60289 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dea5d71a-f182-3e6f-b733-4749937726ec | -15.4247 | -39.47805 | 2025-05-27 04:04:00 | NOAA-21 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0915b420-b2f3-3106-a616-7c0e991841e9 | -14.14528 | -45.48057 | 2025-05-27 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 396c57d6-6dad-3a4e-bccb-b5b2d2513d12 | -18.84582 | -53.62088 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 27.6 |
| e732783d-c50f-3c22-bac6-09885b2f4d78 | -14.59502 | -48.35878 | 2025-05-27 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72425c6e-0d92-3a39-9d5d-6b1f9a96a8ea | -17.83913 | -50.81095 | 2025-05-27 04:04:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c857d20-39cc-3e11-80ed-3af7135aa73f | -14.62388 | -47.94606 | 2025-05-27 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff8528dc-332b-3865-b93e-448da0ca46c6 | -15.52746 | -42.65015 | 2025-05-27 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a055b55a-4bc1-33c3-869b-69c2b2e94a86 | -14.62829 | -47.94236 | 2025-05-27 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 535baf88-9a7f-3aa1-948a-f98f98e59f95 | -18.84811 | -53.59825 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 269756aa-d561-3b9d-8c44-41d66286693f | -14.14237 | -45.47542 | 2025-05-27 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13ac89b3-870f-3ef9-a9d6-4e6c42dbe088 | -15.25042 | -47.46708 | 2025-05-27 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c467bf6-20d3-39c5-9b47-a3fdd68c4979 | -18.84556 | -53.63783 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faf67754-8730-30e3-9f47-9f07bf25d5d4 | -14.1505 | -45.47226 | 2025-05-27 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 120f78e9-fbff-37fd-9f82-f49a06d0999b | -18.84085 | -53.63222 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb62c2b3-b2ca-340e-ab5e-0edaac5c7468 | -17.53333 | -52.12468 | 2025-05-27 04:04:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62108974-2398-319e-b04c-49539042bd55 | -14.69423 | -48.11125 | 2025-05-27 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57b650aa-ff1c-35c5-8ea7-f3f5643e8eac | -18.83977 | -53.60965 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 57fcb326-b282-364d-9c62-5a6abb881501 | -14.66317 | -45.09008 | 2025-05-27 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b085e97b-b111-3af0-8ca7-8f50dfe09301 | -18.84067 | -53.60544 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2565e528-4af6-37d7-b722-6e4fceae514d | -14.02605 | -55.13925 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a501cae-8b47-3958-b874-aae252edbe8b | -18.84834 | -53.62482 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0dc25af6-9ba8-341b-b419-c68d52f87674 | -18.85807 | -53.61899 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 2a2179f3-6b83-36df-8512-ea75f25a2b68 | -18.8505 | -53.62648 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 424a1414-0a5b-3c07-87e0-e3dabac06910 | -18.83886 | -53.61388 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 227f5732-8419-3de9-a59a-fcdad5275fca | -14.03277 | -55.14075 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2846fd2-e1c3-349a-b89e-2e23b4d1d4f1 | -18.83795 | -53.61816 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 21.7 |
| cb89a6e2-71cd-39b6-9895-b60f8831c460 | -18.83413 | -53.60843 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a4f5e8c-4605-397d-999a-2d78ad7c2a35 | -18.84863 | -53.60816 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ee3864a5-3db1-3aa6-95e1-6f87cd1f8954 | -14.03538 | -55.12863 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b731b7f-1f19-36ae-92e1-6cc27681b8aa | -18.85676 | -53.61303 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 41d7d0ac-f910-313d-9ebe-8ecdf31b7298 | -14.018 | -55.14396 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6834bb2c-da44-3812-8fd2-81b616e3da98 | -12.65424 | -52.44 | 2025-05-27 04:04:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c9f722b-13da-3981-8344-e0d90920064c | -18.83825 | -53.60166 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7bbd9468-8423-3616-9228-4034cabf5409 | -14.01931 | -55.13788 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d397ab29-ef06-38a7-b87f-350105478536 | -18.85524 | -53.605 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b81004c0-5ad3-3aa3-a213-3909fc84e624 | -18.84296 | -53.60708 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6460bea1-0af5-3a36-a3a0-673f8ad5fe2a | -17.53479 | -52.11748 | 2025-05-27 04:04:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4375ca98-7516-3bfc-ab9f-b8a082ce9b67 | -15.2545 | -47.46781 | 2025-05-27 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69ca9a84-f404-3cc9-b8b0-d47e8fcab10b | -14.62889 | -47.94261 | 2025-05-27 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e4108f1-f45b-3c91-93f1-daa6f8b7c65b | -18.85765 | -53.60882 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b78197c6-88e3-3780-991e-819829669d8d | -15.88489 | -43.45552 | 2025-05-27 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cf4c199e-30ba-3ec5-80e8-e5e85d466fb4 | -14.66389 | -45.08585 | 2025-05-27 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cd9ddf7-3037-39fb-a92a-409cbbfaae5d | -18.84649 | -53.6335 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40502269-5085-3eda-b2f2-17c160019452 | -12.11556 | -54.66401 | 2025-05-27 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f16adba-eecd-397a-9f6e-783b89f96c44 | -18.84157 | -53.60123 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9347e1a2-6851-3dff-ae43-32dd49e70abb | -12.64562 | -54.07948 | 2025-05-27 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a99a98ad-d385-3843-835f-be0ac804630b | -18.85242 | -53.61776 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e83eac3a-9a1e-34e8-9ce4-e2ea31335a69 | -18.85019 | -53.61616 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 232cc006-54a1-33a6-a063-d081a62b7384 | -18.83919 | -53.59744 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b84c6884-b4db-3408-b120-22078162ecb3 | -15.52802 | -42.64659 | 2025-05-27 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fde7f92c-0b0f-386a-932d-bcc87dddab24 | -14.83937 | -40.9063 | 2025-05-27 04:04:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 26203485-4e76-3eda-8f56-568e0d2a6c5c | -18.85304 | -53.6305 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 392f6b4f-15d1-397f-96ab-b997f94ad77f | -14.14605 | -45.47609 | 2025-05-27 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98daaf59-1d34-3480-97bc-6af2e4e213e2 | -18.85902 | -53.61466 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 60c29fdc-9673-3534-bcc4-0a18efc1167a | -14.04283 | -55.13805 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d8d27ad0-fc94-3075-b7e0-bec7bcd57de6 | -18.84927 | -53.62047 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 62ddffec-6f4c-3f46-afb5-c0873bdd009f | -18.84722 | -53.60244 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec68135a-f55b-34b3-813c-973efc2bd8f4 | -12.12105 | -54.67165 | 2025-05-27 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4501b71a-8735-3e65-ba6f-b7cf10b6c0c0 | -12.65595 | -52.43144 | 2025-05-27 04:04:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f14155c6-6428-33d3-b524-5af7373f07da | -18.84956 | -53.60397 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dc89cb1-d0da-3677-bad8-4d067c3cf8ea | -18.84481 | -53.59871 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ee55718-9913-31df-a0a2-9bdc2be95ec2 | -15.8019 | -43.57065 | 2025-05-27 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9ced7f76-27e6-39e1-819e-1a9b928f4d9f | -18.85396 | -53.62617 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 53eafa2e-ad09-38d4-9b8d-8604873f7109 | -14.04204 | -55.13034 | 2025-05-27 04:04:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d900ff7d-2b36-3696-90a5-95a3156b508e | -15.88369 | -43.46288 | 2025-05-27 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 39f4a80f-8862-3329-8bf1-dcde9e6ec29f | -18.85854 | -53.60467 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ee3f12f-28fe-36bc-bad2-c6756a5a9466 | -18.83612 | -53.62671 | 2025-05-27 04:04:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e450267-0561-3efb-94af-c1fbdc0c271b | -17.91803 | -45.53585 | 2025-05-27 04:04:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 328a0563-aa58-3837-bcb7-fa7a9cf17917 | -19.45447 | -45.30785 | 2025-05-27 04:04:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d51c6d92-9d14-311e-a5b6-6e6f9999dfa8 | -13.69649 | -45.24591 | 2025-05-27 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2900b288-42ba-3239-a75c-a16afe900b0e | -13.37927 | -48.72963 | 2025-05-27 04:04:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b91db16-7e5a-3ba9-8d6d-b260ccdd30fe | -17.53407 | -52.12103 | 2025-05-27 04:04:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README7.md)
