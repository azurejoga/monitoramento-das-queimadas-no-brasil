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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 203b22be-41c6-319b-9f1c-51284f097961 | -7.79264 | -42.60539 | 2025-10-08 03:47:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e99ac741-9695-391c-bfe3-d90a3b9b0b5f | -7.0021 | -42.88231 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| e4533aac-1af5-3650-acb5-cb1af5146c98 | -7.45072 | -43.12672 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1946a7e8-7104-3678-a94e-783baba7e0f5 | -5.74127 | -44.98176 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d883e56-2101-3b72-9175-2e5e2c070866 | -5.59548 | -44.42895 | 2025-10-08 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 784c67d0-d0d2-3ab2-9e18-50238da212c7 | -5.13103 | -44.96763 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e89f640b-621b-38c1-880f-17dd244c3ed1 | -7.47647 | -43.10572 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b556b1b4-f62b-33b8-95b3-aef8e82321a7 | -4.68608 | -45.8423 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3875c638-1509-39f2-9a28-f881738ac3c3 | -7.09878 | -39.75592 | 2025-10-08 03:47:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d0cc87e-df9b-3063-9927-f39213651f66 | -4.69341 | -45.844 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| acf9482b-1c73-30f7-8d47-8361a761fb8a | -3.78877 | -49.43526 | 2025-10-08 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d77ba207-07fa-362f-ac7b-9296970a5297 | -7.59775 | -37.80558 | 2025-10-08 03:47:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7b44601b-4026-34ac-9962-f83508503ac0 | -7.52953 | -42.72154 | 2025-10-08 03:47:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89d72914-6d50-32c2-9ab8-a9096e95ba51 | -6.98364 | -45.1899 | 2025-10-08 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb988949-2404-3c4e-be0d-3b8309e23370 | -7.78783 | -44.22493 | 2025-10-08 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3c75f3e0-fef2-3c5f-8f8e-d274bc3a9e04 | -7.00568 | -42.88705 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| dc17235a-f982-31ec-aaf2-ceab42df6583 | -5.41029 | -45.29374 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5aafa5f-4a20-3909-b3cf-30ac00596776 | -7.47717 | -43.10166 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f13dd2f2-fd58-37b0-959c-41181e170d1b | -4.50931 | -46.35523 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b7c5c17d-3195-3871-8e3c-49c35dfac52b | -4.69345 | -46.47132 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af19406f-9571-35ce-bfdb-04a3e0b1167f | -5.45293 | -45.87049 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd25fbad-c54a-362e-9c9d-bcd80580aed8 | -6.65547 | -41.98555 | 2025-10-08 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5456aa0e-56ce-338c-8775-2ba721de5327 | -4.50543 | -46.36424 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a6019a40-a701-3712-aad5-5274d913d8b2 | -8.17157 | -34.97927 | 2025-10-08 03:47:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d76b4f87-169b-3fbb-8b8a-af045afa4610 | -5.25493 | -43.15131 | 2025-10-08 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 07dd2eac-c07a-3707-875f-854fabae0f54 | -5.81954 | -46.74347 | 2025-10-08 03:47:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d6d0c49-a51c-3072-aa96-61e6e0b11697 | -5.25769 | -45.27494 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f0e96e2-7ee3-393e-92b2-c385d16f3589 | -7.01356 | -42.89241 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| b9d82066-86f4-3180-be78-8517a2933cf7 | -7.80592 | -44.22662 | 2025-10-08 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8649026-0d88-3607-8a1a-d8a4ba7fcbc6 | -7.01131 | -42.87968 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 23a2ba97-37b3-3742-9350-cf883437218c | -7.00142 | -42.88632 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 59816eec-fecb-3fdc-b4e2-7cfe53de2f90 | -4.49735 | -46.35755 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3c9d3c83-3b85-33af-bdf5-a8c37ad55fb7 | -5.14178 | -44.96577 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 33f63d10-8a58-3007-b985-7fc3e7981b17 | -7.7002 | -42.38634 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab122d29-f1df-339c-b5bb-8f199526745f | -7.23797 | -45.32721 | 2025-10-08 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea9212bd-d5db-3d8b-a28a-eb3d32ab0415 | -4.85463 | -45.76088 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d73b087f-5097-3b78-859d-c82c55c12df4 | -4.85441 | -45.66684 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e7e10d9-ea73-3b83-a033-6dba58aea1ab | -5.40477 | -46.22324 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f81b1c31-66af-32dc-869a-75f85d202b2b | -7.79027 | -44.21058 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9e6fbb49-2a82-3061-8599-aa7b9ab89827 | -7.47795 | -43.12284 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0fc62325-42ea-3d6b-b02a-4a7045ff20a2 | -7.82458 | -44.14783 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c85c4861-9f8c-37aa-adc2-070f46ac15b8 | -5.25824 | -45.27179 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60ff78b3-42d4-37c2-9452-d32a3384f90e | -7.44258 | -43.13493 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 44e8d704-4704-3acc-8a7a-77224ec7a390 | -6.17327 | -44.68375 | 2025-10-08 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 488963aa-8ae7-3522-bd57-468a3af43f5a | -7.78119 | -42.40366 | 2025-10-08 03:47:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 003ef890-228a-3036-a75c-b3fc1908d0e4 | -7.02479 | -42.87769 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 603d44f0-7f8e-3cc6-b760-1a88b27877aa | -5.36524 | -41.0025 | 2025-10-08 03:47:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| fb039980-38e3-3e9a-b4a9-09c36d167b4e | -7.01423 | -42.88838 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 0e23d900-682f-37db-b85f-619cf2611c2e | -4.08826 | -48.04498 | 2025-10-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c509f736-11c7-3f34-9c10-970fbe70db82 | -7.78066 | -42.40445 | 2025-10-08 03:47:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ad351919-4eba-377e-a777-1e0e5ef9fea0 | -7.28329 | -41.97704 | 2025-10-08 03:47:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9871cf01-5d35-33e2-802d-a9cbf2c87748 | -7.47855 | -43.06804 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10dfc98e-6dea-319a-9dac-9ed019559566 | -7.31953 | -39.25423 | 2025-10-08 03:47:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1669be1e-623c-3e75-b606-a3545b65a070 | -7.46916 | -46.84968 | 2025-10-08 03:47:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a167714c-29bf-3199-8bf4-028d327031e1 | -4.69278 | -45.84756 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1a845f83-a5f3-3398-ac03-e1777b3c87cd | -5.71683 | -44.82331 | 2025-10-08 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59a64fbb-a48e-3593-984e-cd930c608f2f | -7.80975 | -44.17825 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d5a859e-1614-3c82-8ada-823ad28bdddc | -8.15118 | -38.62849 | 2025-10-08 03:47:00 | NOAA-21 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e612fc1-08d8-3ce1-b964-b4620c264357 | -7.28728 | -41.97771 | 2025-10-08 03:47:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0eb79d67-b7f8-3483-9928-9e29700cbe47 | -7.79208 | -44.22432 | 2025-10-08 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e69d190-73c3-33e8-a930-96e7dd713d08 | -4.69746 | -45.84092 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c2937514-6026-323d-8862-504020b16b81 | -8.84632 | -36.5682 | 2025-10-08 03:47:00 | NOAA-21 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e403a5f8-05a0-3468-b86d-cb6c28458574 | -7.47652 | -43.13113 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1944730d-8afc-3357-bfa2-0ac21942bdaf | -7.43848 | -43.14606 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ac0081a9-d855-3d70-a71b-38e6d27407ff | -5.99717 | -39.31352 | 2025-10-08 03:47:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c48deb6f-3aaa-308a-925e-bfc73430c64f | -5.90316 | -44.56921 | 2025-10-08 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f72a1811-370c-3c68-b549-c87f7eb6b6e8 | -3.78987 | -49.429 | 2025-10-08 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 96d83f10-cb8b-3c7d-a152-7fb0044e8b4f | -5.70662 | -44.21365 | 2025-10-08 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fc6ff21d-dec2-3c36-8434-2a610347366a | -7.78832 | -44.21878 | 2025-10-08 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2bb556b0-a283-37cf-8f9f-928c945b5146 | -5.50351 | -39.70329 | 2025-10-08 03:47:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 48cfb071-3766-338f-a6a7-1d52397f3d4b | -5.82516 | -46.74459 | 2025-10-08 03:47:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5e479b8-353a-3f70-ae97-7787deec6f4d | -4.69403 | -45.84044 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bc6bea2a-4403-3a1d-9934-920308d34a43 | -7.44397 | -43.12662 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5b16c1bc-c67d-3633-9076-f210a5af32d2 | -4.49602 | -46.36546 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8012e945-d160-34ce-a2d8-f9e96eb850cc | -5.26187 | -45.1898 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6cf2877-ce5a-338d-804b-19cef34e3888 | -7.01851 | -42.88905 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.5 |
| 72d2a6d1-7623-3c3b-bd4a-eaa843883382 | -5.59168 | -45.83839 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75866f1e-21ea-3f60-ac08-d31690f9e6dc | -7.78059 | -42.40731 | 2025-10-08 03:47:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9f294f8b-7d12-3a7d-8a33-ecae84a2a9bc | -5.13157 | -44.96442 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 96d72f9d-99bb-31e1-8c71-c3086c0dc4ae | -5.24001 | -46.5783 | 2025-10-08 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 625f280e-7988-3883-bbe2-c2e7c78a6ef2 | -7.02541 | -42.79578 | 2025-10-08 03:47:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6840c58e-3562-3426-bc3f-88ae916aa026 | -4.68547 | -45.84594 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 525c76b8-9d1f-343c-b470-8958e027f383 | -7.34919 | -43.86809 | 2025-10-08 03:47:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e9ba2eb5-0e58-31c5-8ec3-d093a78c5ed4 | -5.15999 | -46.92564 | 2025-10-08 03:47:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1630fedd-4e3a-32e7-bcdd-1564caeedfe8 | -5.40403 | -46.22737 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37c57df9-992d-37e6-aa32-d0ad0993bdcd | -4.69806 | -45.83734 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b247815e-b224-327a-92cf-caa7f6c8fb37 | -7.52437 | -42.98001 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9dead4bb-82d5-3f0d-ac67-b30f722f11fc | -7.676 | -42.57722 | 2025-10-08 03:47:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b477607a-9cda-3803-a3b3-cb105848ac21 | -7.4576 | -43.04465 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 09d278ab-78ec-3166-889e-907e2f64e1f8 | -7.00277 | -42.8783 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 82fb6ec6-98e1-3b7c-a01b-b5610a867ea7 | -3.21961 | -49.35695 | 2025-10-08 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5b92c39-e7dc-3049-8b27-854638c6b4f6 | -7.792 | -42.60914 | 2025-10-08 03:47:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3c37bbbb-6343-3706-8007-e5e3e1a47501 | -7.44641 | -43.12604 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f5f22c8f-bc35-31cd-a49a-2d7b5355cc77 | -7.44711 | -43.14749 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5dd8a4cf-ead4-30af-a89d-1b5f2c2bfbbb | -6.08921 | -46.23839 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 616c0b84-dabb-3fec-a5e8-696e857ea202 | -7.70899 | -42.38405 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c9e15d4-4924-36be-b8c1-c0b84d5eb56d | -7.67593 | -42.40535 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c9ff60ba-ba10-354a-b897-9f83789d4721 | -5.17404 | -45.13323 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54d51863-2b1d-3efe-8894-7ec89f5a9438 | -5.80569 | -35.53265 | 2025-10-08 03:47:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4990d0d9-3281-3f13-95dd-041880a9f220 | -7.53019 | -42.71771 | 2025-10-08 03:47:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
