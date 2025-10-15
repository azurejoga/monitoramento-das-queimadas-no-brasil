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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5211210b-4cfc-3d1d-8dcc-b170258c0b76 | -7.16333 | -42.49932 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 815dd9e0-2ad3-317e-af34-6ab1580f2916 | -8.45831 | -44.19424 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8dac7b28-008c-3906-9fe6-3ba8026c3dd1 | -6.37437 | -41.49757 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6848e3d2-910e-3f3d-91b7-3ab695d0f54c | -4.39602 | -43.61806 | 2025-10-15 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 099afede-2eab-3268-bdc5-d46ef43abdaa | -6.14788 | -41.72767 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 57908c22-0812-3490-9f70-d6898322bfce | -7.0208 | -42.73131 | 2025-10-15 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 75874f4c-ee50-37ab-8b78-5217348ba7d2 | -2.79862 | -48.94107 | 2025-10-15 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1c37896-e506-32e6-8dd4-e23b7423f5d1 | -5.56699 | -41.31996 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b8a7655b-4aa1-376d-bb11-c3495ad508bc | -9.47445 | -46.07192 | 2025-10-15 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddf1b12d-06c7-3d1e-9da1-104c28636543 | -5.73965 | -44.9852 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 65172fe2-224c-3217-a74c-99bc50e11855 | -7.09068 | -41.95248 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5f83264-ca0b-3741-9639-2588de8650ee | -5.40668 | -44.23579 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6381bc1c-178f-3440-ab79-fffcc71582dd | -5.62137 | -42.68661 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fe572826-a487-3bab-a960-517a874bbf3c | -7.18612 | -41.39258 | 2025-10-15 04:06:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f5926dc8-7b54-39c5-b0f1-3f2cb47de7e3 | -7.94612 | -44.14062 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99cba27c-c07a-3a4a-b762-b161a13c1699 | -6.12657 | -44.27367 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f913085-4efa-3aca-8b8e-550395dfc700 | -4.30866 | -44.55403 | 2025-10-15 04:06:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a03e5af2-7d41-3c33-9e3f-9a670eba6961 | -5.87364 | -43.86746 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c11371f8-962e-3763-8315-dd40891c9fd6 | -5.1387 | -45.69483 | 2025-10-15 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab9b0de4-27e3-3d95-b54c-55521331f608 | -4.63948 | -42.81744 | 2025-10-15 04:06:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 797d8611-12c8-3cf8-b706-690b53e902f9 | -4.28814 | -41.73626 | 2025-10-15 04:06:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9cfc4e36-15ae-3c08-9d2e-871e2ad33fcf | -6.4236 | -44.029 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b2a2d0c-121e-366a-a1b4-daadb1b3293e | -4.90864 | -45.62643 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da666a0c-575e-3a77-99df-53ce62c6de93 | -4.12289 | -50.71968 | 2025-10-15 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33b5665c-c078-3793-986d-0dfa634870d4 | -8.20931 | -44.01528 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c81d4eb-b18b-3cfe-b80b-5315e06a55a7 | -5.5929 | -42.84281 | 2025-10-15 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1c956392-a9cb-3a71-baed-f1d686354b5b | -7.49326 | -41.87798 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d526d58-3463-3b98-9211-36c8e84211c8 | -5.9733 | -46.60708 | 2025-10-15 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0e2a026-aa5f-3a88-a826-5ab486788f7d | -4.27728 | -48.58816 | 2025-10-15 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce260114-6a2c-314a-aaa9-718cc27e0bc1 | -6.57683 | -42.96062 | 2025-10-15 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39e81aca-b7c6-3df3-b5c3-c980d380558d | -5.71437 | -44.41534 | 2025-10-15 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 872ab9e2-402b-3cfa-88d1-3b8aa494c0fb | -5.98023 | -42.92231 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4a30f4d8-e0fa-3b87-be56-4c7c17d26a1b | -5.58891 | -42.84594 | 2025-10-15 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 44f0ddcd-ee36-3dac-bac0-94709a459ae6 | -5.9496 | -43.75765 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 129e5d15-8878-309f-9fb5-388db9845865 | -5.19488 | -46.14074 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 328a1c14-efe9-3afb-821d-29dc4b4af271 | -5.27695 | -41.04794 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 873b200e-79f9-38fb-bf96-8b5580c2f16c | -5.97995 | -42.88094 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6ff40f51-0ccf-3300-8f0d-f6f622356540 | -5.26454 | -41.01767 | 2025-10-15 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b5c66afd-9b0c-328c-995b-a3809a40dbec | -7.56828 | -43.83586 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 37310c2b-70db-3f85-82b7-f84c0a8503a1 | -4.66448 | -43.12074 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b691888-1d88-3603-9789-fc3bc29b0c3e | -6.41031 | -45.36395 | 2025-10-15 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6dd4792-bdb1-35e7-88b1-7cf5de639542 | -7.57174 | -43.83637 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac6ccf8c-bd03-3136-bb86-7694d37f9562 | -8.22069 | -43.31969 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 27b741f7-5a08-3d26-8f8c-bf2b5e459dff | -5.98363 | -42.92286 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e352140b-b4d0-334f-914d-b29d4683b212 | -4.66387 | -43.12453 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| c364f1eb-62db-3417-b5e2-3e2f589fd6f4 | -6.17625 | -44.29757 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 900075b5-8e02-30d4-b0ff-de4ea0cbcd70 | -7.29218 | -43.85546 | 2025-10-15 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59c00047-cf9c-3329-8380-e5b7deffd81f | -5.48698 | -45.4104 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca5e9e5b-95b5-37e1-a7f1-528a236da0cd | -4.85418 | -43.20477 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bfded5d-569e-321a-82e9-1ddd72fc1e8f | -5.58136 | -44.74381 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6872046-d7ae-3f88-962c-65ac0f30b854 | -5.11382 | -46.05416 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b87bae79-4569-3486-ac15-f89cebf757fd | -6.42741 | -41.82877 | 2025-10-15 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97615d78-257e-369b-ab82-33f1497b25db | -6.16547 | -44.38511 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0644ed15-6f82-3267-836b-3ead88895f4e | -8.2859 | -43.43859 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3da793ed-6a36-3bb2-8af4-f06bc192a733 | -6.05282 | -41.89749 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 67586324-8432-3707-b671-c644a85a49cb | -5.31705 | -42.92342 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f54c2b9-a5ae-35b0-a6cf-276bb4858446 | -5.24809 | -44.4694 | 2025-10-15 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c633d93-ddb9-3f68-a501-233b410783df | -5.56862 | -41.30963 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2015c583-0ecb-301c-8fd8-639dcb2ddf4f | -6.25867 | -38.16543 | 2025-10-15 04:06:00 | NOAA-20 | MARCELINO VIEIRA | RIO GRANDE DO NORTE | Brasil | 2407302 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d53c3e5-e0dd-3de3-a155-41e0491c93f0 | -7.57093 | -42.69156 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8577fd09-fb99-3e92-86dd-1a4704d23fd8 | -3.42445 | -50.25884 | 2025-10-15 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f960d34-47d7-3117-93a0-f3f4013e832a | -7.48672 | -42.1335 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 64eab4a9-9d9c-3d6e-bc7d-5f934ce24cc7 | -5.48307 | -44.63528 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1fca16b-fb6f-3df7-93db-790a6e3350c1 | -5.85604 | -43.8644 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36f519c7-06bb-31df-bc9e-19a6bce5aae1 | -5.48749 | -43.79079 | 2025-10-15 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d2a4bfc-7324-3648-b44f-dbf82068d466 | -7.25133 | -44.91399 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57ccc532-a25c-3cfa-a8ab-ffd086fac5e7 | -4.78442 | -37.72292 | 2025-10-15 04:06:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f2da352e-a008-3576-a4c8-ddeed6db7e33 | -5.31423 | -42.9192 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6e33f85-d428-395f-a229-24815afb6a6b | -5.06092 | -44.44465 | 2025-10-15 04:06:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0fd125c-d7dc-37a7-8645-2bfb8159858a | -3.67653 | -45.22233 | 2025-10-15 04:06:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b60b72f6-8bcb-3241-9f43-ab20f96098bc | -3.83205 | -44.54733 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cd70eaf2-bebe-301f-a8f7-1bd98bbb1004 | -6.19518 | -43.28623 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db9bab19-3f26-3f87-ab50-7f7577955468 | -5.4059 | -42.65269 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dce9b4f7-fbfa-3e71-8ad9-8b5fd1026585 | -7.49263 | -42.138 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7ccc4e48-2b54-3d14-8588-7b7d81bfa87f | -5.87098 | -42.79582 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| af80ddb7-8014-369d-aeeb-c4ba615ce35f | -5.87139 | -43.85897 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e38451b3-c260-38ed-81e0-bfdd3e39aaea | -2.79522 | -48.94198 | 2025-10-15 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb254774-8bfd-3141-9755-308067be3e11 | -10.33344 | -40.61763 | 2025-10-15 04:06:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9d228a71-ee72-3218-b932-b1dafe652bb4 | -6.54877 | -43.92946 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70318b78-7fe4-3a2c-8da2-8cc927db87e8 | -5.73736 | -41.31503 | 2025-10-15 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7b0eb77-60c8-30fc-92f2-a200aa00b2a8 | -6.42677 | -42.55981 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| bd61ea72-60da-3c28-a8da-bf2dc050986d | -5.86346 | -42.82076 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 99285d6d-6eca-3b0f-af61-9d3688c2b5e6 | -8.17597 | -43.95861 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c41e0125-075d-3acc-b542-c5edfc253dbb | -7.49871 | -42.14255 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ed073977-6f60-38a5-9f49-e01542ec29b5 | -4.6898 | -45.83694 | 2025-10-15 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c54e21ce-833a-3871-9b29-e06b741141de | -5.76676 | -46.00961 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3d88b16-d8d0-37a6-ae36-e739e5186e87 | -5.82581 | -46.53706 | 2025-10-15 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bff63d3f-fff4-3738-aece-4593728f947a | -7.57143 | -42.70988 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b134855f-806b-30b6-bda4-45248abbda5c | -5.86502 | -43.85365 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09e15acd-dbb3-33a8-ac6e-0cc0b3becbd0 | -7.56507 | -43.89883 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86a72f75-ae7f-3c45-8b6e-f9d681ce52b6 | -6.14347 | -41.75539 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a20ab8a5-a9cc-375c-bd90-958185718934 | -6.28026 | -42.97652 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a3f47b5-2b69-3d25-bb93-2e452b4c119c | -7.19657 | -39.35315 | 2025-10-15 04:06:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 61216f8b-fa76-390b-bb5c-1559bfe9b016 | -6.42778 | -44.02563 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae7ba788-8974-3a3f-9019-ac8b6ec9ae4f | -5.86723 | -43.86234 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d453317-416f-3f37-be7d-49869c1985a9 | -7.17389 | -42.19835 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 111e3ed1-a5b0-39dd-9c94-2f45b4e82797 | -8.21659 | -44.07977 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bbcee10-9e68-3ac0-bb65-b3b85f049439 | -7.485 | -42.65567 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6d02fddc-c463-3be2-88e3-43c710ecbce4 | -5.87905 | -42.85333 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 811b00f1-f90b-3804-9662-f9061a245ddb | -4.55068 | -45.40634 | 2025-10-15 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
