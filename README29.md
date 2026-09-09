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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8015a52-5f1d-3c0e-a029-8571a778566a | -10.62021 | -67.92933 | 2026-09-09 06:29:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73f82548-2626-3617-a442-568eb5ecf0fb | -10.61902 | -67.92799 | 2026-09-09 06:29:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a81af84-bc9d-3471-9a87-75b1e576d1a6 | -9.32164 | -68.20843 | 2026-09-09 06:29:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb4b7a41-9dca-3f86-8146-91c82ace867e | -8.74867 | -72.76868 | 2026-09-09 06:29:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2cfea4d-9439-341c-941c-5f31ec459694 | -9.14422 | -67.82504 | 2026-09-09 06:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87fb2ef7-a3fc-3753-a19f-473996bb8854 | -9.3264 | -68.20911 | 2026-09-09 06:29:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e73dfac-4e46-3e82-adf2-c16cd89e5864 | -1.03269 | -53.72591 | 2026-09-09 07:35:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 174d0f4c-6783-3b82-a0bb-0f7c300d85d4 | -1.18752 | -55.71243 | 2026-09-09 07:35:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| cc2bb956-e512-3f13-bfe1-01a6dde7b02d | -1.31027 | -54.65182 | 2026-09-09 07:35:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| afed96b5-dbe3-39bd-9d22-929793aa776c | 2.66386 | -60.17659 | 2026-09-09 07:35:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0553a25b-0b3f-3d94-9c63-b7377044076d | -3.7703 | -58.8478 | 2026-09-09 07:37:00 | AQUA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2d5d0096-cb5f-3438-97ac-a892f3a79ac0 | -2.93791 | -50.48218 | 2026-09-09 07:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| d00cc38b-cdda-3d07-a506-92e5855eff0b | -6.55442 | -62.88831 | 2026-09-09 07:37:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 99e94b12-b4d9-36bc-abdf-c5a9268412fe | -3.14543 | -60.65238 | 2026-09-09 07:37:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5233435b-eaa7-3d8b-8bbd-bb441a8f4c1c | -2.94435 | -50.47826 | 2026-09-09 07:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 25dbd344-a739-3807-b96a-a38eed738c5f | -1.66699 | -55.66417 | 2026-09-09 07:37:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ff3fc3de-231b-3977-b998-a9379d17f461 | -7.12312 | -56.50882 | 2026-09-09 07:37:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 60de1a46-6d4d-3a31-9b7a-9e3910b611e3 | -3.15429 | -60.65368 | 2026-09-09 07:37:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 4f16cd23-af57-3ef6-a78d-c1144f7ae303 | -6.55279 | -62.89856 | 2026-09-09 07:37:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a10ea7c8-e017-350a-a44a-ea1ff01e1d25 | -2.9425 | -50.44923 | 2026-09-09 07:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 87837a30-3b27-3f05-bfc2-8afcebfc6dc4 | -9.01309 | -65.41725 | 2026-09-09 07:39:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 65cb8fd5-4c2c-3c4e-8d38-ea3307ebf5c0 | -9.00965 | -65.41087 | 2026-09-09 07:39:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3580caaa-a1cb-359b-814a-b53e029f7410 | -13.2863 | -61.7837 | 2026-09-09 07:39:00 | AQUA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 73245357-cad3-3b85-8342-58bf841d6bdc | -10.7003 | -45.9925 | 2026-09-09 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8df37243-1801-3a4d-ba30-07c9acbfc71a | -10.719 | -46.0128 | 2026-09-09 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e17927aa-692a-3cd9-bb7a-46579f35872e | -2.96607 | -40.02894 | 2026-09-09 11:28:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f0faab5a-9206-3f61-9197-44e40cc78ac5 | -2.97549 | -40.03024 | 2026-09-09 11:28:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 52b202db-8aeb-3f69-8473-cc791dd6ca34 | -3.46332 | -43.53833 | 2026-09-09 11:28:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b4df505a-d32f-3e26-bb7f-5f7363129a86 | -10.61839 | -40.1846 | 2026-09-09 11:30:00 | TERRA_M-M | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| ae04e074-0076-3ff6-b953-8ef180d8f399 | -11.00762 | -45.08146 | 2026-09-09 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 60b36159-da78-3970-839b-68b4cc4f03ad | -6.31672 | -38.97598 | 2026-09-09 11:30:00 | TERRA_M-M | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| d5e035c2-c2b7-37c7-91a5-861fa49d5e08 | -8.09583 | -45.67964 | 2026-09-09 11:30:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 637ea765-6a71-3aeb-aa03-a7eece479143 | -6.16352 | -44.64383 | 2026-09-09 11:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| b6623a8d-3853-324a-867e-44eb45d82908 | -9.69399 | -43.44743 | 2026-09-09 11:30:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 252ea0b7-2e2e-328f-ae86-13307b41b338 | -5.76716 | -45.07597 | 2026-09-09 11:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 88b07316-f430-3c1a-bb59-224bdf859780 | -8.6199 | -47.3602 | 2026-09-09 11:30:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0d64fbfb-b15b-3278-9c4a-dcc3cc5ac933 | -7.49232 | -39.3583 | 2026-09-09 11:30:00 | TERRA_M-M | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ebc77213-a18d-3be3-ba32-accef332096d | -6.16215 | -44.65335 | 2026-09-09 11:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 1a39a5a3-6073-3a13-a3f3-dee069b80572 | -13.179 | -43.56878 | 2026-09-09 11:30:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| b6313e78-8735-338c-b3bd-72e2cab4ef73 | -13.39505 | -43.00434 | 2026-09-09 11:30:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 28.7 |
| a3efa8bb-f7b3-36ca-9103-96e98512d355 | -7.52474 | -45.9306 | 2026-09-09 11:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f09f598c-ac73-3179-a21a-665b1395ab52 | -13.18028 | -43.55958 | 2026-09-09 11:30:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7bc0d450-6d30-323b-ab90-88f3e435441d | -10.17912 | -42.21969 | 2026-09-09 11:30:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 30faf3ce-0e11-3e5f-9522-9bac21578358 | -10.69399 | -46.00858 | 2026-09-09 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 68003a48-2cd1-31dc-870d-c2ba62391406 | -9.77586 | -43.45633 | 2026-09-09 11:30:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7917fba9-6251-3c5b-baa5-f3af7c49de9f | -10.70029 | -46.02995 | 2026-09-09 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 279.2 |
| 1a3bad42-b997-399a-b90d-02aaec96be2c | -9.69649 | -43.49316 | 2026-09-09 11:30:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b48adf9e-7494-341a-be86-4bfcdcf2c661 | -10.7018 | -46.01994 | 2026-09-09 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 286.2 |
| 44d7b31e-a035-3aee-9d29-cd827dd341ad | -5.30504 | -43.05579 | 2026-09-09 11:30:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4a955954-f4ff-36d1-b397-85e55490904d | -9.70915 | -43.40414 | 2026-09-09 11:30:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 20.1 |
| ea03b241-4876-3753-8f45-3d78593657f4 | -13.64802 | -43.63844 | 2026-09-09 11:30:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 034662d2-5be8-393b-9b9a-5b1222e59cea | -7.68651 | -44.31633 | 2026-09-09 11:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f9818d69-67f3-3222-833c-ff31a49fd1a2 | -8.97516 | -44.9726 | 2026-09-09 11:30:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0177d277-8b6a-3f3a-bdf7-865eeeeb57f6 | -9.70029 | -43.46646 | 2026-09-09 11:30:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2a470b54-7721-36ec-a0ee-c4f05d3574db | -9.26079 | -45.65543 | 2026-09-09 11:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d34c3332-c1f0-31e8-a7eb-486477555d25 | -9.31555 | -38.01166 | 2026-09-09 11:30:00 | TERRA_M-M | PARICONHA | ALAGOAS | Brasil | 2706422 | 27 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 5d0a9f93-b263-30eb-a3af-4e6ac3ef6984 | -10.74155 | -45.94472 | 2026-09-09 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 07f84021-d25d-31f4-8e01-7e13c5f2f12e | -8.89773 | -41.21998 | 2026-09-09 11:30:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 93f5fc7b-0722-375c-85aa-9b1192196581 | -5.77801 | -45.06724 | 2026-09-09 11:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 690b8ef9-0fb3-36b2-a13e-147e2a713d4e | -6.33067 | -43.80875 | 2026-09-09 11:30:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d98681ef-2980-3084-9ff8-2470bf7e18b7 | -6.36164 | -43.59431 | 2026-09-09 11:30:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e05e34f4-f870-36d3-9c7c-636f57d0687a | -6.82409 | -43.83689 | 2026-09-09 11:30:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e5f72e06-d5d5-3382-bb07-3532386fd394 | -13.39636 | -42.99482 | 2026-09-09 11:30:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 23f6f7c6-13c2-3e1a-b9dd-78e6f5e50ddc | -8.72763 | -47.89741 | 2026-09-09 11:30:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| bf39a778-7c5b-34e5-9919-eff8a9b00107 | -10.74791 | -45.96576 | 2026-09-09 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 87959f54-4621-3b34-af3d-b1a042182b1e | -5.6081 | -44.83866 | 2026-09-09 11:30:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0650ff62-f109-372e-93d3-ffd92d510ed9 | -12.58626 | -45.4494 | 2026-09-09 11:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9216c2c5-9df8-3c9f-b9ec-abb148383188 | -7.13444 | -42.11762 | 2026-09-09 11:30:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 17b9cf7f-44c4-3575-92a4-374603dd33b7 | -10.7033 | -46.00996 | 2026-09-09 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f9556605-9f3e-35ad-a8e9-ef0e70c30b6f | -13.72154 | -41.5834 | 2026-09-09 11:30:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f2476ab3-252c-3ae7-b406-e4ffb74ef16a | -9.70788 | -43.41304 | 2026-09-09 11:30:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 42.3 |
| 56754fdd-60d3-37e4-9e8e-48a4de7fbcba | -8.61234 | -47.36544 | 2026-09-09 11:30:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 201d4efe-b936-3d8d-a919-5ac4376c01d9 | -10.69249 | -46.01856 | 2026-09-09 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6b1e001a-42ce-382c-9b26-95ed624fc76e | -13.81862 | -42.17274 | 2026-09-09 11:30:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| aa2d6633-28a9-3dc9-802f-fcc49a30e939 | -5.60667 | -44.84841 | 2026-09-09 11:30:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 05942645-813c-3f58-94b2-37d61c2d5f40 | -8.09734 | -45.66951 | 2026-09-09 11:30:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 98dcc79a-43f4-333c-a6f0-37f63d22dfb6 | -10.58625 | -45.74775 | 2026-09-09 11:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3066a0fe-3fd6-31ea-a838-88933fa47ba3 | -4.50004 | -42.54998 | 2026-09-09 11:30:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| fae8dd69-404d-3184-9018-694888a3deeb | -11.21742 | -39.81137 | 2026-09-09 11:30:00 | TERRA_M-M | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 9e8866fe-1a3c-3b6c-b3b8-b5a265886569 | -5.77654 | -45.07724 | 2026-09-09 11:30:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 734f81eb-9bf2-373c-92d7-82725e9ea10f | -8.95221 | -45.69664 | 2026-09-09 11:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b40e7c4d-2493-340c-8a7d-0a146a10595a | -9.69272 | -43.45633 | 2026-09-09 11:30:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 56.3 |
| 97da205f-405e-3c2a-ac6e-d2076bf46193 | -6.32938 | -43.81765 | 2026-09-09 11:30:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| c7c4c1eb-a5ec-39f8-a88d-2941f21fe8c1 | -3.96515 | -43.12719 | 2026-09-09 11:30:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb34ef36-d730-30da-81c4-e158843c46be | -5.19018 | -42.75824 | 2026-09-09 11:30:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0cf0d83e-c40b-3435-b3ff-e86fbe13b8b7 | -6.32257 | -38.97031 | 2026-09-09 11:30:00 | TERRA_M-M | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 2217fa62-6fca-353a-a18b-0984a1ed2f87 | -12.01224 | -42.28042 | 2026-09-09 11:30:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 8deda764-58b8-320e-8446-86fc5747ae6e | -14.00991 | -42.18911 | 2026-09-09 11:30:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 09325768-e5ac-3564-ac1f-50cac7243a72 | -12.01088 | -42.29039 | 2026-09-09 11:30:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 916bdfe0-f5e0-3792-9613-8368f9420d75 | -16.41668 | -43.04578 | 2026-09-09 11:32:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c54aff38-5c82-3676-a188-a8bbc40bfd92 | -14.39738 | -43.54771 | 2026-09-09 11:32:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 54a67df8-2870-309f-8b74-13b92373714a | -14.91233 | -44.66881 | 2026-09-09 11:32:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7fc7e13b-4d7a-3c0d-adb6-f5cc2d4afcaa | -14.39608 | -43.55714 | 2026-09-09 11:32:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 94e5f447-0a74-39aa-a35e-19455a6da1ff | -16.4153 | -43.05609 | 2026-09-09 11:32:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8fca0cdd-bf2f-3e30-8518-232e715ae27d | -9.7141 | -43.3956 | 2026-09-09 11:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 116.5 |
| ff2b7682-62ca-39c2-8cd8-0103fbce6123 | -9.6947 | -43.4217 | 2026-09-09 11:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 91d470c7-db71-3604-945d-dac78b75b8f1 | -9.7138 | -43.4192 | 2026-09-09 11:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 118.2 |
| fa2ff3a2-4ef9-3829-9014-65930a820069 | -9.6951 | -43.3981 | 2026-09-09 11:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 87.2 |
| e93c2cf5-2f51-33ef-b69f-7726fcbb4d16 | -10.7186 | -46.0355 | 2026-09-09 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.3 |
| 56a14000-254a-3d7e-b9b3-61354b457ac3 | -10.719 | -46.0128 | 2026-09-09 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |


[Clique aqui para ver as próximas entradas](README30.md)
