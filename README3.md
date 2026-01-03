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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dda87de5-0caa-3f9b-9b2c-3d7842d99c54 | -18.48468 | -39.86085 | 2026-01-03 03:51:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6c8e9870-2643-3797-b4d8-34d3c45897fe | -13.42657 | -43.86183 | 2026-01-03 03:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b975892-0f71-3de2-b8dc-40a9be9cb227 | -15.37158 | -43.60272 | 2026-01-03 03:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3a4b2f4d-d9be-3014-bbee-a6f193c6d210 | -12.95195 | -41.18412 | 2026-01-03 03:51:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3b46f78b-7ba1-31dc-b29a-17a6358b28ab | -16.25256 | -42.22906 | 2026-01-03 03:51:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4ffe2fa8-c7f1-39ee-a4a8-7ea188b4b81b | -17.49749 | -41.59138 | 2026-01-03 03:51:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 90309ba7-10ba-3004-b903-900578f331eb | -7.58125 | -40.10425 | 2026-01-03 04:08:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1adc6512-7461-3d87-8753-b54c9a8e16ae | -4.68397 | -38.16148 | 2026-01-03 04:08:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4f5e438d-e636-3a09-b8af-1b648aff92fd | -4.17403 | -43.63019 | 2026-01-03 04:08:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 790d80f6-5902-368c-a2ea-03db91b68440 | -5.46681 | -39.28277 | 2026-01-03 04:08:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2293c655-eb3c-3a68-a429-2dc6822689cc | -5.95632 | -39.98995 | 2026-01-03 04:08:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 337c7173-65b6-3bce-b57e-f603a4ad9f20 | -0.82971 | -48.7821 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 131d2f80-4d21-3f72-8a80-43ae9d16dbe4 | -2.94455 | -39.92675 | 2026-01-03 04:08:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5930769b-3b51-343e-8a45-bb07d587b7a0 | -0.80579 | -48.7691 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 263dbea7-fbda-30a6-9427-b60992e4415c | -4.87518 | -44.39992 | 2026-01-03 04:08:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aab9b950-4b7a-3628-bfa8-22a0dacafff0 | -5.42468 | -44.86666 | 2026-01-03 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a17431bf-72b2-3fb4-96ef-06f856a18a6a | -2.73313 | -42.73042 | 2026-01-03 04:08:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7527183-36f9-3039-9ad5-854d90ae97f2 | -5.90176 | -43.72103 | 2026-01-03 04:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 16a5d57c-80b9-3c9e-9744-1797a1bda0b2 | -5.70921 | -39.8474 | 2026-01-03 04:08:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 438c7aa8-c130-39b2-a926-43a9774d6d78 | -2.31549 | -44.80097 | 2026-01-03 04:08:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f6ffc114-58e4-3a26-8e27-154c5ba4c5ae | -7.58466 | -40.10477 | 2026-01-03 04:08:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b01899b5-e8c7-3767-9140-d7f86e5898ea | -4.17752 | -43.63074 | 2026-01-03 04:08:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a676a67-6bfb-3259-829b-1cb5b42719ca | -4.44212 | -38.05902 | 2026-01-03 04:08:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 419e5ad2-1468-3d2a-9072-3463f6a7c3c5 | -5.98648 | -43.73846 | 2026-01-03 04:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 658a4f72-e30c-3781-8d59-e5ea7936e848 | -5.4648 | -40.69875 | 2026-01-03 04:08:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f16f3d74-1d64-346c-bf9f-2baafdd83cdb | -4.86723 | -49.17857 | 2026-01-03 04:08:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad54274b-2d56-38f0-b2ca-0acb8ad87a03 | -0.08916 | -51.2833 | 2026-01-03 04:08:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c2d73c0e-3aba-3a92-8de9-6896918f706e | -5.49258 | -40.73882 | 2026-01-03 04:08:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3454ff41-37ec-3901-841e-30b4ca0856bf | -5.27107 | -40.46037 | 2026-01-03 04:08:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9b221ee5-1ef9-36bd-a4ef-54ce4b2b93af | -5.42564 | -36.70455 | 2026-01-03 04:08:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ee27fec2-08ea-35ae-ba06-3b07539da7bf | -4.422 | -43.10999 | 2026-01-03 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22b8f141-c7de-3ebf-a048-b30c02dfc3bc | -2.94789 | -39.92727 | 2026-01-03 04:08:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1678bcc6-ebdb-315f-b27e-3caed5d14de9 | -4.24578 | -46.78757 | 2026-01-03 04:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08a5b804-f74c-3982-bab3-d0358d605b19 | -5.32746 | -43.56147 | 2026-01-03 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5f28287b-cb08-3830-8468-5de1711ec846 | -5.29105 | -44.96909 | 2026-01-03 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3c6901f-95bc-3b49-a9e2-a8f4e1716c4b | -5.42033 | -44.8679 | 2026-01-03 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8188e4ed-0dac-3063-89aa-8cda62e133ab | -5.28886 | -44.96557 | 2026-01-03 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49a8272e-e3b5-302f-8195-8f78492ce944 | -9.48146 | -36.03387 | 2026-01-03 04:08:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1eca8465-2e9e-35e4-b592-8b069d0f5a0e | -0.80627 | -48.76615 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| beab9cc7-ab4f-3b50-9b68-aff92b859ab6 | -6.08336 | -41.81789 | 2026-01-03 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2f819d2f-a94f-3f09-bb25-6f69ce0f9695 | -4.75635 | -46.71079 | 2026-01-03 04:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6612cb6-c887-37c9-987a-68a982bba4d1 | -3.46789 | -40.78591 | 2026-01-03 04:08:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9635f78e-984a-3e0f-a877-c95017cd8bb4 | -3.06466 | -44.96225 | 2026-01-03 04:08:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55f79967-513d-359d-a34f-02522b6c3476 | -5.04291 | -43.61086 | 2026-01-03 04:08:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bb236ff-7975-3881-aa86-300f5ac98b75 | -4.06134 | -43.34547 | 2026-01-03 04:08:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36be296b-95b7-342c-8473-872608b1e5fe | -4.94123 | -39.85323 | 2026-01-03 04:08:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c0c715c7-9639-39b9-a472-de84b841629a | -4.44275 | -38.05486 | 2026-01-03 04:08:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5479a8ff-ab07-360d-abfa-005d17e2ff40 | -3.85359 | -40.7093 | 2026-01-03 04:08:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 141ebb3f-6e97-31bf-ab3b-11ea6760cac1 | -4.68877 | -37.39352 | 2026-01-03 04:08:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| aa2480aa-127b-3b4c-a3dd-3338b3c5e10d | -5.16585 | -39.89445 | 2026-01-03 04:08:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 394d671d-7e2e-35b5-8bf7-0e0fdde32649 | -4.17464 | -43.62633 | 2026-01-03 04:08:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7f7c977-ad2d-3a08-b815-65f5dc8397b9 | -7.08984 | -38.78473 | 2026-01-03 04:08:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ae0da99-94bf-3a17-8166-8e5aff957f92 | -5.32402 | -43.56089 | 2026-01-03 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 36a839fe-b2d4-329a-8ffc-2f6790b3eb4a | -6.26361 | -35.18063 | 2026-01-03 04:08:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| f54014a2-f6a1-33d1-a0af-971250f3b310 | -6.66253 | -38.98106 | 2026-01-03 04:08:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 40af7983-479c-3882-9a87-7561b7f3d7c7 | -0.80216 | -48.75942 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ef56683-94a9-3189-9c3d-caf0d315c73e | -4.73766 | -38.72816 | 2026-01-03 04:08:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dbc18c93-daba-3ce6-98c8-8d2153ebfbe1 | -7.01904 | -39.6837 | 2026-01-03 04:08:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d6a345e4-4db0-3af9-8501-41de3421b2f3 | -5.40487 | -41.91927 | 2026-01-03 04:08:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3258744d-dff1-393d-9fbf-b6b05fa4b84f | -4.68947 | -37.38892 | 2026-01-03 04:08:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 978ddef1-06c2-3dd2-a2c6-56422fb80dff | -4.32156 | -45.05487 | 2026-01-03 04:08:00 | NOAA-20 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5608ca9a-eba4-36ae-8393-a1b3b5d1c7f3 | -9.8564 | -36.17405 | 2026-01-03 04:08:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 127cc48a-6d2b-3533-98b0-1ac7b2a9beb7 | -0.79806 | -48.75267 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3469f0a-138d-3df5-b60a-08845606b447 | -1.68592 | -54.05373 | 2026-01-03 04:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70d45718-3dd3-3f2f-8df3-70ca7e69bc37 | -1.11826 | -47.74509 | 2026-01-03 04:08:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba280d28-a6c1-32fa-b5ce-9860e0048d52 | -1.68705 | -54.04696 | 2026-01-03 04:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d668f84-a1e8-3c89-a878-c50090c6f96d | -5.52602 | -37.78785 | 2026-01-03 04:08:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 309864cc-7a20-398c-8b02-8bf72a21eac1 | -5.90237 | -43.71724 | 2026-01-03 04:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc89674e-2071-397c-b8ac-aad35304d95b | -3.03085 | -39.72023 | 2026-01-03 04:08:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0e09f89b-d969-3bf1-a8cb-0050c704de2a | -5.98587 | -43.74221 | 2026-01-03 04:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c4b708c-988f-3ac2-ae75-0a3d0caf1a8c | -0.83479 | -48.78292 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c120935-b0ea-36bc-b320-c0e7477ef8f0 | -3.0131 | -41.12681 | 2026-01-03 04:08:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c908d04d-e910-3a53-a9fd-43fd533f6b3a | -4.42541 | -43.11054 | 2026-01-03 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47d18a44-07ea-35c2-82f2-5fad1494acfe | -5.02048 | -40.2634 | 2026-01-03 04:08:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ccbced48-33bc-3d5a-85a9-3fb40387ce03 | -5.3234 | -43.56467 | 2026-01-03 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75b65358-7119-3860-9bb7-741697e06387 | -5.32057 | -43.56031 | 2026-01-03 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8a1d8111-5ba5-3dae-9f93-096f95c63570 | -5.42399 | -44.86848 | 2026-01-03 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 497b407c-ca34-326d-ba7e-947c1ea17238 | -4.68758 | -38.16202 | 2026-01-03 04:08:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0da22c1c-89af-3ea7-9b52-f4130406676b | -2.26307 | -46.48314 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b47f797c-b07f-36a8-8697-badc6e1a414b | -1.66428 | -53.92686 | 2026-01-03 04:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 789a64ec-4c1b-3b27-87b9-0f88a9187808 | -2.42571 | -44.04997 | 2026-01-03 04:08:00 | NOAA-20 | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf4daa34-1bb4-3ff5-b435-d2d945a58532 | -5.42102 | -44.86606 | 2026-01-03 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cba11e5-0042-3198-a997-1a5b7b66d4ce | -0.82464 | -48.78126 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ace7d35-7241-3ee3-b5cf-50a5d1a3ff1e | -5.32278 | -43.56847 | 2026-01-03 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7257081b-c4d4-3eba-a15f-b55b25230f86 | -1.67117 | -53.92834 | 2026-01-03 04:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f906af8f-5d7e-3a83-840b-b29d48c13e77 | -0.48414 | -48.50685 | 2026-01-03 04:08:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dad9c16b-ce13-3a9a-9bf5-5f48070f7509 | -1.45469 | -47.01929 | 2026-01-03 04:08:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19e61841-6914-36d5-82b9-852a718f31cf | -5.88853 | -39.66004 | 2026-01-03 04:08:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f52c584-fdf8-3d34-ba0e-53c8eca7498c | -1.41823 | -46.79701 | 2026-01-03 04:08:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b6e73dd-d30d-3ae0-a9ec-2d5fdcc7feb4 | -5.46425 | -40.70225 | 2026-01-03 04:08:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8729bd8c-86fb-38da-950e-de4e026d7aff | -5.46093 | -40.70173 | 2026-01-03 04:08:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f7d963fd-c5fa-307e-ad95-d16911f8363e | -0.80168 | -48.76237 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66b66d1c-f498-308c-9d2d-b4d2ffcff8db | -9.48154 | -36.0318 | 2026-01-03 04:08:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 42f13da1-aac6-3f87-87e6-d61327a01278 | -4.24996 | -46.78831 | 2026-01-03 04:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 725cb120-7a53-3fd1-bc18-fd7ba5c759eb | -2.31929 | -44.80158 | 2026-01-03 04:08:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b7cbc4c1-26b8-3486-8276-ac14909efda5 | -3.30436 | -42.75488 | 2026-01-03 04:08:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fa9a917-1d51-3065-a941-a3bc05b0192e | -4.29959 | -39.0189 | 2026-01-03 04:08:00 | NOAA-20 | MULUNGU | CEARÁ | Brasil | 2309102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 75848edd-7128-302c-9962-cae319bb8de6 | -4.43167 | -43.42271 | 2026-01-03 04:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34601708-6f93-3015-b72b-9b52430c40be | -6.26453 | -35.18265 | 2026-01-03 04:08:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6530fab0-69c2-31ea-aa18-f2eaaa5de48d | -6.73341 | -39.65284 | 2026-01-03 04:08:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README4.md)
