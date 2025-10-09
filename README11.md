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
| b84ccb9b-c684-3ca8-a280-08ad9fdecfd1 | -7.75652 | -44.02794 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 194d0ed8-4a59-3b27-8efe-e6c2e767a8b2 | -8.5541 | -44.63063 | 2025-10-09 03:30:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56015f42-8eb3-379c-86de-a729fd8560a0 | -8.1985 | -43.35131 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 5e8ea922-04bf-32b1-989e-b5174c08bf96 | -8.49317 | -46.23845 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3a928bab-3c2b-33ab-85cd-3684c69b1e0f | -7.81409 | -44.13322 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad47a366-9088-3337-81a9-1d29b252995a | -9.61785 | -40.33215 | 2025-10-09 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 6ab75921-716d-3001-b7a5-4ce2f1ac3a57 | -5.6474 | -43.61068 | 2025-10-09 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 711f39d8-3f01-3f0c-b9fc-facc408f069c | -7.20337 | -45.48798 | 2025-10-09 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41eb1344-d827-34f4-ab66-e31ff3200ff3 | -6.72379 | -42.86787 | 2025-10-09 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 3055eb55-7611-31a2-be77-a0b08dc2572f | -8.63601 | -45.14596 | 2025-10-09 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6b4adc74-daca-38eb-aab9-a3044e19a25d | -10.1956 | -44.56224 | 2025-10-09 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9690fd1b-9bdf-33b3-a7ab-d38bb7566675 | -8.53757 | -46.22402 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e3d02f2b-36b7-3c3e-8db6-90f30d0f3be2 | -10.86629 | -44.63683 | 2025-10-09 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| da33ab66-d4a4-3be1-9740-8fbc97a6ac16 | -8.53518 | -46.20839 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 1bfae1fd-2092-3a02-a55b-a36c1da049bd | -5.39575 | -40.98589 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 93c50297-d345-3c72-a4f1-0c2aebb80bd8 | -11.05754 | -40.93787 | 2025-10-09 03:30:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea422c3b-22e6-34a8-b250-3e4909259444 | -7.55797 | -35.20427 | 2025-10-09 03:30:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1c0a0c5e-54f7-34db-bcbd-eb152349920e | -8.73671 | -41.66177 | 2025-10-09 03:30:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3ebe5250-81fa-3c5f-9686-ae2c77cfa02f | -10.08888 | -40.77846 | 2025-10-09 03:30:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7c2ee886-7275-35ca-9bca-7192c9524112 | -7.48553 | -43.11558 | 2025-10-09 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b73014ba-6bdd-34da-a830-69a3171394ff | -9.17207 | -40.31048 | 2025-10-09 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| bf58a747-0048-37be-9e2e-4724e8f251c4 | -8.53228 | -46.22347 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 956d93a5-6a69-32a5-a1d8-4e85b33ab61f | -7.80151 | -44.20086 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9ae6da29-8b87-3dcd-b1c3-25a15f790dbd | -5.39984 | -40.99376 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8bed6a90-577e-332a-88c9-5ea645575876 | -7.50754 | -42.73962 | 2025-10-09 03:30:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b71d1d6b-0281-34c7-b414-baa8400628e5 | -7.71578 | -42.38071 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b254d7c-fbf8-38ae-b2e3-30214b11d85b | -8.54788 | -46.21754 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ad9e9376-b7c8-3ce9-b214-8712ec35d3d0 | -5.40228 | -40.98988 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 272b6330-b1b3-3db1-816e-ea6600cc46c1 | -8.53365 | -46.21635 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 17bea2e9-629a-3e60-addb-5116fd8ba01b | -6.74528 | -34.95393 | 2025-10-09 03:30:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 26cb046f-0b97-3ed1-ae4d-4b5bbb356c26 | -8.49447 | -46.23174 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| fdcdcbfa-d53f-385c-8de1-370ff8b66d90 | -5.39636 | -40.98243 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b84026a0-5d0e-376f-ae2e-8cbf13c614d1 | -8.50148 | -46.23296 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 06696ac8-ac2d-321a-9d9d-58c7db742944 | -5.24625 | -42.99247 | 2025-10-09 03:30:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1787ecfa-6900-3f9b-8361-21afee4fefe2 | -5.44503 | -44.82867 | 2025-10-09 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 78f0e89b-c38c-3fa3-b462-59ec129698ba | -7.51657 | -37.66288 | 2025-10-09 03:30:00 | NOAA-21 | ÁGUA BRANCA | PARAÍBA | Brasil | 2500106 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 961c4334-ccbc-3170-bbdc-7f90007214fb | -7.50478 | -42.72221 | 2025-10-09 03:30:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 95411143-6232-3309-a4c0-571b2fc5107b | -7.76802 | -44.03513 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 36919d14-05e6-3e39-b0ec-d6889dcd9b42 | -5.64114 | -43.60955 | 2025-10-09 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 26c68e89-aa9a-389e-a853-2bf3da28f1ff | -8.51115 | -46.22045 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 42434072-2d18-318e-b983-fe5c8243185e | -5.39697 | -40.97897 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a2f5c6c9-4733-3b81-9f2d-e06b12688ac6 | -8.20006 | -43.34276 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 59958eb1-c768-3b7e-abf6-a3057ebcb5ab | -8.50787 | -46.22761 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c04a16ec-6102-3ff8-aa80-98284f9254cf | -8.52655 | -46.21564 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 067aa915-9d15-3c41-8a89-13f0d816dda8 | -5.24542 | -42.99704 | 2025-10-09 03:30:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b00baddc-8940-3314-a2e0-17995ab63fe7 | -7.79555 | -42.40785 | 2025-10-09 03:30:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9642703d-f9d4-317a-885f-5fd6ad312837 | -6.32274 | -37.62313 | 2025-10-09 03:30:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 252af508-cd38-3016-be8e-5fa0f047439c | -5.64204 | -43.60452 | 2025-10-09 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1889db9d-becc-3c6a-b72a-652514276fe7 | -7.51719 | -37.65924 | 2025-10-09 03:30:00 | NOAA-21 | ÁGUA BRANCA | PARAÍBA | Brasil | 2500106 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6065d17b-f22b-3bf2-a95b-7ace6297d641 | -7.75541 | -44.03372 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9dac76f0-dd91-3710-8067-2dbb94ab1aa5 | -7.77571 | -44.03727 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7dad81f7-efd6-3676-924a-80d2052d67f5 | -8.18391 | -43.33081 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| b2d0c9a4-fe92-33ce-8489-86ff488d474c | -7.2828 | -41.9747 | 2025-10-09 03:30:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6bdacfc5-874a-3db3-8a15-5d1154617f8d | -7.32745 | -44.79738 | 2025-10-09 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aea18840-b1bb-3a94-8fcd-42534ee2b28f | -9.61268 | -40.32905 | 2025-10-09 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| df26b078-0181-3efd-958b-fdd1000f8ed4 | -8.19494 | -43.33731 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 2a203f0f-5a23-3049-8e8b-122ef6f51490 | -7.66791 | -42.58139 | 2025-10-09 03:30:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4d428d4e-3800-348a-9e19-da14f9715b48 | -7.77425 | -44.03618 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fec1236a-33bf-336b-bc10-fee41b549c55 | -8.49948 | -46.23328 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| de10a605-32ac-3aae-957c-b2ff5931920f | -7.76222 | -44.04072 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e90a0a69-a28f-3eb3-9825-6af65e4a59b4 | -7.7704 | -44.03115 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 689c458f-b495-38ba-8947-68bf8c67699c | -7.77445 | -42.3964 | 2025-10-09 03:30:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f068c88c-b2a4-3629-86c6-1d2af422606d | -8.19255 | -43.33769 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 35c8e4a6-12fa-311e-9e00-b8e1626f08b0 | -8.54477 | -46.22425 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 6f227f78-1dd0-3c0c-b8c4-d5fd1f7057ad | -7.34375 | -43.87328 | 2025-10-09 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae119f1d-b74f-3d9d-9052-21a4b5c06f35 | -5.44974 | -44.82844 | 2025-10-09 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d1554bc1-d103-306a-aea9-1c90861f10f5 | -10.09047 | -40.77734 | 2025-10-09 03:30:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2ad89504-8d70-3066-9bec-74cdb28bb099 | -6.74462 | -34.95794 | 2025-10-09 03:30:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7fd47632-8409-31f9-b69d-4bc0f7066a17 | -7.50177 | -42.73864 | 2025-10-09 03:30:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a7b11188-abe9-366d-bd38-6844c667a6f9 | -5.03713 | -43.60776 | 2025-10-09 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b944a71f-c53f-38cb-a131-1a60de48af57 | -8.19417 | -43.34157 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| a053f86d-1789-3593-bf23-94db0ec30bd3 | -5.54815 | -41.30384 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 90c6e707-414d-3ed0-9dde-72b710893753 | -5.31361 | -45.38482 | 2025-10-09 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2de7812c-f6ce-3c89-b95a-cdf491931821 | -10.86208 | -44.62577 | 2025-10-09 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 6dec8a2b-45b9-3010-b951-48e14f9d925d | -9.29896 | -40.23345 | 2025-10-09 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01f01585-b48c-3630-812e-def200f8497d | -8.22706 | -44.15569 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 10a07ff2-6723-3e5e-a5c8-a9ce993b3119 | -6.45621 | -44.57947 | 2025-10-09 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c7cd6195-5071-38b9-8772-abf089e45a6b | -8.18982 | -43.33192 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| f78e0829-72bc-3e9b-baec-6ff783dfb413 | -9.61311 | -40.33133 | 2025-10-09 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 84c17c1f-8646-30ea-be4f-63339760135f | -8.22613 | -44.16062 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 289e8b87-8e55-301b-909b-7642751d13b0 | -10.09474 | -40.77384 | 2025-10-09 03:30:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e715f2dc-971b-3396-9524-03625ba5057c | -10.86723 | -44.63198 | 2025-10-09 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 41864c6c-f532-3473-a6bb-262e3864d182 | -5.44618 | -44.82249 | 2025-10-09 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 40258254-028d-3954-8490-607099cfab6b | -8.50982 | -46.22731 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 147f0e72-2727-349e-9bee-cf330a4b8d3f | -11.05854 | -40.93251 | 2025-10-09 03:30:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6b538c5c-b279-3b32-b0e7-d8a2f96d61fd | -5.39105 | -40.9815 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8fa554fa-7047-351c-852a-89c09c2d6690 | -8.52515 | -46.22293 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 0f44f1da-a96c-3804-bc19-43faf515d72f | -7.78037 | -44.24446 | 2025-10-09 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 193953cf-cb71-30bd-a734-57c2248825f0 | -10.92968 | -42.84666 | 2025-10-09 03:30:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d94eb09d-6edf-31f3-9245-279d23495cc5 | -7.7733 | -44.04121 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 35c8f0e1-1837-3ccd-a6f2-529ff1e0e326 | -9.03506 | -40.6432 | 2025-10-09 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c100d924-de23-3bd5-a762-1773a0adb95f | -8.19684 | -43.34728 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| b7049325-e624-347e-97fc-b4673f3450f1 | -7.27664 | -41.97745 | 2025-10-09 03:30:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b6fca415-5008-35c7-af07-016e4f665d0d | -8.50223 | -46.21961 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 2f752e4c-8e28-3e77-bd48-64f6937f24bc | -13.8129 | -45.83183 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4292719-d2a3-30e4-8caf-e7046f13051f | -15.29882 | -46.18638 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad2b5ce7-5107-30ed-80f1-29bf2b2e5259 | -15.78776 | -46.25171 | 2025-10-09 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 489a62b4-d990-3297-ab5e-3f8bcfaca9ab | -12.23207 | -43.78395 | 2025-10-09 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 330049d1-28eb-3582-a6a3-ecfcd3264f3f | -15.46897 | -47.95954 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de3eec82-6d44-3684-be62-7889e83669d3 | -18.29716 | -45.43245 | 2025-10-09 03:32:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
