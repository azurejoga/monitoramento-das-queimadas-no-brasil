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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42bffc3f-0cff-32ea-9102-dc0e045d02b3 | -3.05653 | -39.92951 | 2026-08-01 04:19:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8b0c7c7c-fce3-346b-8cfe-147be52ccad1 | -7.50797 | -45.84057 | 2026-08-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a3bd7259-118e-35be-859b-6cc8a7d10f52 | -7.0127 | -45.85141 | 2026-08-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40139454-4005-308e-b3b1-2c8f64ecac73 | -6.01036 | -47.40499 | 2026-08-01 04:19:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5dee9669-f981-3e6b-a6c0-6ab9a2c9b514 | -6.56291 | -55.15836 | 2026-08-01 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 58ba89c9-2b0b-3982-bb06-74070498f892 | -4.27233 | -48.19189 | 2026-08-01 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56565c38-c7be-35e3-9ae3-d6517b753837 | -7.23087 | -43.42219 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c067f6a3-5b9c-305e-bef6-68b8218a5b34 | -4.26582 | -38.03304 | 2026-08-01 04:19:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d42a89df-f42e-3f9a-83c7-447632e12074 | -6.54274 | -41.86842 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0c5b9b4f-9bc9-3c17-b04e-5cdc808ca425 | -7.11238 | -43.66439 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8763331-a3da-33b4-88da-eed8709e647a | -3.66072 | -48.96239 | 2026-08-01 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e35f8a85-72a6-3022-b5e1-234a0d838415 | -6.18768 | -40.87852 | 2026-08-01 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d9606b6-71c1-3de3-aabb-7d7bc2b9cd84 | -4.26083 | -38.03657 | 2026-08-01 04:19:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 55.2 |
| d1d7fe92-8a20-3b19-99be-df5b8a509069 | -3.05274 | -39.92895 | 2026-08-01 04:19:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2739ac53-c53e-3aaa-b2a4-376fa999a871 | -7.4945 | -46.12085 | 2026-08-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb2ee7c5-4451-3c42-88fe-f8e57f0f94a8 | -3.84991 | -44.09069 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ffefedb-3061-3a97-995e-b2a84d3d608e | -6.27037 | -41.8757 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 50e386cc-3e6e-3e19-8c34-ddd6a3532f34 | -6.42776 | -42.82595 | 2026-08-01 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa537462-03f3-34b2-ac75-5b96a0f057e5 | -6.15334 | -47.24017 | 2026-08-01 04:19:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dde3c603-63e7-38fc-b89f-19823accae43 | -6.1027 | -55.80885 | 2026-08-01 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e351dc2a-059d-35dc-81b0-a649e412f279 | -7.19507 | -42.9896 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3538cf75-c7b4-32df-8804-a71c0cec5fe6 | -6.19194 | -46.69749 | 2026-08-01 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43ca043b-dd51-3139-afa6-f52208775d95 | -7.19617 | -42.95942 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc043da7-2a27-3f23-bae8-9d9b51218a26 | -7.64624 | -45.04608 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28ee719d-e4f4-3fa3-8308-e61f56ebc270 | -5.81692 | -44.75974 | 2026-08-01 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b322718c-dbf9-358f-92ce-2eaa4c4a84f6 | -6.27331 | -41.88026 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 20de8e4c-9687-39a5-9ab5-61a2e8629fbb | -14.0925 | -46.2637 | 2026-08-01 04:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 9f45e7b0-b54a-3b13-99d4-4d7d571240ce | -11.2402 | -54.8534 | 2026-08-01 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| ff2d6ea6-f9b0-3f09-9253-daaaacff238e | -11.2591 | -54.8517 | 2026-08-01 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| debc8e72-ba7e-3f7d-b49e-861572ba25cd | -4.2578 | -38.0284 | 2026-08-01 04:20:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 52843a88-5389-39e2-82aa-e403bac9dcb2 | -11.2399 | -54.8737 | 2026-08-01 04:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a64a3403-cf43-3b1a-903c-bd1408a2bdc9 | -14.073 | -46.2669 | 2026-08-01 04:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 112.2 |
| df5f45c1-824d-32fe-9b44-3965a654ce0d | -14.092 | -46.2866 | 2026-08-01 04:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 55e6833a-2073-32f3-951d-d2c73d9be708 | -14.0725 | -46.2899 | 2026-08-01 04:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 9e4eda75-ae42-3c70-b535-7332835ce13b | -14.07077 | -46.28232 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 691e0c10-39e5-3db7-b593-13073d27afc1 | -11.24085 | -54.8518 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 85b3b954-53ae-36f8-b5c7-9109f4ca3c3a | -14.06911 | -46.27115 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 158d3877-e6a5-3d1e-b68d-ad6f02dd0e8f | -14.34997 | -48.03993 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b4364b8-2cc2-3bc9-b90e-5b3542562248 | -12.62539 | -44.62811 | 2026-08-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7741241c-cd23-3fbf-91cc-689f14fc71f5 | -14.07462 | -46.27932 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70cee8f7-8bb4-345c-9f3a-4f26b8ff4319 | -12.06988 | -45.81356 | 2026-08-01 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b3e0042-b679-3d0a-9467-f6d6ccf17724 | -14.07351 | -46.26461 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d3ce490f-9978-3a5a-a596-b3f634a6472c | -8.58178 | -45.06646 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b2abcf3-9e01-30f6-b740-4eaf985c7262 | -14.0895 | -46.29263 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 455e1d68-450e-3f06-8e68-98a8c6cb6c8b | -12.18409 | -45.04861 | 2026-08-01 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5970c8a6-f573-37a3-9ce3-a7e385916bb1 | -15.02934 | -39.41633 | 2026-08-01 04:21:00 | NOAA-21 | JUSSARI | BAHIA | Brasil | 2918555 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8e92b312-ccea-3d57-9107-4ab91af81dff | -13.25893 | -54.36671 | 2026-08-01 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86567a9a-cb76-313e-86b7-9cf0eab34812 | -15.03398 | -39.41695 | 2026-08-01 04:21:00 | NOAA-21 | JUSSARI | BAHIA | Brasil | 2918555 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c636fb21-375b-3ee8-a13f-56a99d618048 | -15.62771 | -47.83833 | 2026-08-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 838d22d0-b902-361c-a437-a01970ab977e | -11.2313 | -54.87349 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 16d33c96-dfb8-3dc5-ba59-0bf785d81a59 | -8.19551 | -55.44082 | 2026-08-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| def8750b-6978-3af3-8baa-076452e21e1d | -11.24234 | -54.87228 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cb575ded-70d0-3178-8033-ba320c97a294 | -11.24939 | -54.86361 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ac551132-e35b-39e0-933c-6312f2dfe56d | -14.77156 | -48.29816 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c516f007-aee6-3eeb-9fa6-c811b6695ffe | -14.41666 | -48.04397 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4219d2c-dce5-31bb-852e-99175f9bde30 | -9.26746 | -50.69333 | 2026-08-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e630f242-4c9f-35a3-a14e-42ccdba9ed7a | -14.08287 | -46.24799 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c369778a-a68c-35b5-8ed1-02bb0139f6ef | -9.10759 | -49.64431 | 2026-08-01 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dd1190d-ebdb-3770-96b4-faa8a7d2c099 | -13.85717 | -41.3393 | 2026-08-01 04:21:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9a4530e0-c2e5-33d2-aaa1-267edfadafb3 | -10.95319 | -50.3009 | 2026-08-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25cc6a54-948a-3af7-a893-d6ce01f784a7 | -15.60883 | -41.3957 | 2026-08-01 04:21:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2f57f2b6-22ed-3e7e-80bc-08f72c862cb6 | -13.95562 | -47.82701 | 2026-08-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0cc2963-f2c4-36ad-b876-52295958c5b9 | -14.07022 | -46.28586 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 57cd9abe-345f-3634-a62a-88f55525bf02 | -12.60178 | -44.62439 | 2026-08-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54184801-9ff6-33da-914b-e1789903cc14 | -12.339 | -48.21923 | 2026-08-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b97cbfa3-986b-3381-83b8-93b2687d5a61 | -12.69531 | -44.74788 | 2026-08-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba726efa-1caa-38de-addd-6f80c987f56f | -14.41053 | -48.03911 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02267c51-bbd3-3a0a-917e-c19f27472f34 | -14.07628 | -46.29048 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 33d19551-c66d-3f3e-ad51-c64224e6dcbf | -11.54985 | -46.91137 | 2026-08-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1fcf348-1ba8-3517-8250-0dba5ca166ba | -14.08397 | -46.24092 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e00bcf2c-e8df-3a56-bd4d-d4b3615ab10c | -14.08068 | -46.26215 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 548b0ead-0c61-3341-a380-2cfa21a9aa69 | -12.19739 | -45.27367 | 2026-08-01 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c075dd0a-3325-34bc-97e6-76bba5d4253f | -14.08895 | -46.29617 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 58d4d50a-760d-3cba-b6aa-8b566ab45f1c | -14.33643 | -48.03796 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0da0cc1a-3747-3109-9e8b-f6b809196f02 | -11.22651 | -54.84216 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de1cf038-49d3-3108-80f3-60a20919ead9 | -12.33963 | -48.2154 | 2026-08-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79fd87f9-2cb6-31ee-b951-3e008bbfafec | -14.3466 | -48.03936 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9710493b-670c-3915-9c4f-036bd1c207eb | -14.08507 | -46.23386 | 2026-08-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dc3ed15-3a31-3172-a62c-cfde02ac08d6 | -14.81895 | -48.50443 | 2026-08-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cce5b71f-d5e7-391b-ad9a-89441152dfd1 | -11.25458 | -54.86471 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d586a0c4-4362-33dd-9039-8b825cea5e61 | -9.8254 | -45.33562 | 2026-08-01 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36be9dd8-0a00-3e14-83a0-374d4313e771 | -11.31727 | -54.47769 | 2026-08-01 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f858c9b4-e09c-31a6-aaff-acd0dd03c63e | -9.59465 | -48.54935 | 2026-08-01 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c12aafdd-6d81-3e68-8274-bc59dc2de68b | -12.61356 | -44.61496 | 2026-08-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dda36c6-b1b8-34e2-8399-c3d67dd64575 | -9.71121 | -47.3333 | 2026-08-01 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cdae215e-d8c1-3598-a4d3-a71bdaee46fc | -12.61916 | -44.60078 | 2026-08-01 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27786d2f-67a1-392a-88ea-e15b42c712f3 | -14.87681 | -52.76391 | 2026-08-01 04:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3e939e0-8a3d-3721-a314-42801931033b | -15.81907 | -48.17152 | 2026-08-01 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e0dd0a36-4fd1-3a88-85b3-c40068c27fb5 | -15.64063 | -46.43996 | 2026-08-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3d0031d-c85c-36fd-8389-184611db00dc | -14.08837 | -46.23439 | 2026-08-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 959b03dd-97a1-3048-98e3-1e8e5b80e1e0 | -11.23294 | -54.83675 | 2026-08-01 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf3017ae-0c1a-30b9-a41e-bb7615efa479 | -13.06234 | -52.72649 | 2026-08-01 04:21:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4db25116-8887-37d2-bf06-0e5f4710266b | -14.07185 | -46.25345 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a393404-aa97-3be1-a13b-674590d3e9c1 | -14.07241 | -46.27169 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 31bf8159-d8a6-3146-b844-ed7f84bc416f | -9.0033 | -45.17655 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a773ab6-81fe-352c-bb93-6131fbe1c91d | -8.97741 | -45.16891 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2316dc29-a60d-3888-be16-5698b6d4fb9b | -9.88335 | -48.7356 | 2026-08-01 04:21:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 245cfc30-d113-3fcd-930c-58747fdfd884 | -9.00661 | -45.17706 | 2026-08-01 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0198d82-565f-3424-be9a-91d157788fe8 | -14.07681 | -46.24338 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0771796-7b98-3c8f-b102-7fd634e8b7c8 | -14.08343 | -46.26623 | 2026-08-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |


[Clique aqui para ver as próximas entradas](README12.md)
