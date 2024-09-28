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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b8da182-9fa6-31c5-a067-46e94390d780 | -18.59643 | -43.41278 | 2024-09-28 03:32:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 804c2aa2-1111-3131-9f57-f754ee1f9ae0 | -19.83091 | -44.44205 | 2024-09-28 03:32:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c60b2d8-9cfe-3f96-a687-f2659c684778 | -19.74722 | -43.96686 | 2024-09-28 03:32:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 39832129-fb41-317e-8d09-f9d61472c42e | -19.74716 | -44.29658 | 2024-09-28 03:32:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e52ac5e-306b-3cff-b6d2-b23ae016d83f | -19.74657 | -43.96989 | 2024-09-28 03:32:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e76e56b-7239-3669-bbbb-ee7e8ae67c85 | -19.74645 | -44.29997 | 2024-09-28 03:32:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32e87698-01b0-34fc-956c-f3f5f6a5519a | -19.73649 | -44.01741 | 2024-09-28 03:32:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 018e8051-feff-35c1-9064-b2de1e9026dc | -19.73585 | -44.02043 | 2024-09-28 03:32:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02b3df9f-af7c-3b6c-aa65-5f17d7a468e3 | -19.73314 | -44.01864 | 2024-09-28 03:32:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53117dd8-fd74-34d2-89f8-a9f3c5c70626 | -19.68972 | -43.8968 | 2024-09-28 03:32:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83c855a4-e59b-3740-b184-4e6714fc3911 | -19.6891 | -43.89976 | 2024-09-28 03:32:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 311e2b36-266a-3972-b678-450710c7895e | -19.68848 | -43.90271 | 2024-09-28 03:32:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75fec67a-3521-3f3b-b773-0bca3032eba0 | -19.68783 | -43.90582 | 2024-09-28 03:32:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daf0e465-a72b-3d80-b6c1-bf329df02f3d | -19.51724 | -44.09795 | 2024-09-28 03:32:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 153ff97a-eca2-358e-9e4e-884c9af5fe78 | -19.51657 | -44.10111 | 2024-09-28 03:32:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 10352786-e27d-3903-ac4c-861ba753cb9e | -19.51589 | -44.10431 | 2024-09-28 03:32:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3c24ca31-95dd-3770-9be3-df701403fc7e | -20.82259 | -44.80303 | 2024-09-28 03:32:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cb494240-f1db-361e-ba76-70ab37c1f94c | -20.82188 | -44.80635 | 2024-09-28 03:32:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 82cbebfa-be42-3b97-935d-c6da748bae7e | -20.49965 | -43.62585 | 2024-09-28 03:32:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d8af7492-6a17-3ee9-a476-2831aae9f955 | -20.49848 | -43.63146 | 2024-09-28 03:32:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b9c9a433-3dc9-379f-99d1-6c254bef89f5 | -20.18324 | -43.52362 | 2024-09-28 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8a7c11cd-c211-3942-b485-72b68b4efe4a | -20.1823 | -43.52809 | 2024-09-28 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 37686fd6-8999-343f-b9e1-4e8c76d16231 | -20.17845 | -43.52218 | 2024-09-28 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 76696933-24ea-35cf-a189-f4bf3752d3c9 | -20.17496 | -43.53884 | 2024-09-28 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2567b46c-f356-33af-8814-a632ccf9846f | -20.17012 | -43.53761 | 2024-09-28 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e36f896e-b692-3924-922d-bf0dd65a34f8 | -21.83669 | -44.80468 | 2024-09-28 03:32:00 | NOAA-20 | CRUZÍLIA | MINAS GERAIS | Brasil | 3120805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e30907f9-6298-3e53-a1e6-765697a683a6 | -21.83598 | -44.80802 | 2024-09-28 03:32:00 | NOAA-20 | CRUZÍLIA | MINAS GERAIS | Brasil | 3120805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c97f32da-5c36-3191-aae6-e35f2c055f5a | -21.10693 | -44.27044 | 2024-09-28 03:32:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 40ab3274-3e10-3583-a54e-f7def8aef047 | -21.10187 | -44.26953 | 2024-09-28 03:32:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b184669f-6bba-357c-bac1-aff8faa70f7d | -21.1012 | -44.27266 | 2024-09-28 03:32:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e957e7cb-676e-3ad8-bbd9-c12385444783 | -17.84061 | -45.89605 | 2024-09-28 03:32:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 59b4a131-5743-3c06-a25e-99ea784dbfba | -17.83956 | -45.90083 | 2024-09-28 03:32:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 397d6d3d-417b-3510-a093-5057ac1dfde3 | -20.55875 | -46.25896 | 2024-09-28 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 516b78b6-cb81-3011-8cd3-5702ac48d988 | -20.51929 | -45.88472 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e7447a2f-29aa-34a8-9dae-160386323282 | -20.51861 | -45.88779 | 2024-09-28 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 78d1cd79-25f3-3e90-b421-536710fe8b93 | -20.51682 | -45.88322 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 599e0a5e-c5ae-3dd3-97e9-5b31d2ffd476 | -20.51619 | -45.886 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 06bd1575-6e42-370c-8088-a8b48f67e254 | -20.51365 | -45.88363 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 099b420b-e57b-346f-86b2-932ac0c65ea4 | -20.51305 | -45.88632 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b02ac3d-94ae-3f4b-a75c-c1296aaa5469 | -20.51233 | -45.9031 | 2024-09-28 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5caee4a8-a81e-3b7c-b50a-3548db50796c | -20.51124 | -45.90791 | 2024-09-28 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99c8d29d-3253-3626-9b26-4e91b7dcbeb5 | -20.51116 | -45.88222 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d480402a-a20a-372b-8487-ec8175a4b3e1 | -20.51057 | -45.88483 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dcc844d8-2a60-35bd-9730-921bdad20221 | -20.50919 | -45.90401 | 2024-09-28 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| aa1c6e9d-22ff-3c4d-9028-2c80c6347f40 | -20.50813 | -45.90886 | 2024-09-28 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e898d3cd-1ca5-3495-ab7d-65039befa537 | -20.508 | -45.88262 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc78206f-0f57-3641-9c82-b68782502f4f | -20.50741 | -45.88529 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b91833b-97d6-3dd7-84a7-d269e2d97272 | -20.50574 | -45.90619 | 2024-09-28 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71df9a2c-29b7-3fa0-a37a-64e2ef054293 | -20.50365 | -45.90245 | 2024-09-28 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6344e904-9915-3032-ba6d-c9b5957f7422 | -20.50258 | -45.90736 | 2024-09-28 03:32:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6334466e-7985-32e3-8b0d-b4b4c19e6306 | -20.50234 | -45.88164 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3aa82f4e-3ba0-3123-83f4-57908dad5418 | -20.49605 | -45.88351 | 2024-09-28 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ebb69971-ce73-35d0-9040-ea15f5363701 | -20.44606 | -45.4821 | 2024-09-28 03:32:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33c1d545-71d0-3345-9ba8-0569e425589b | -20.44516 | -45.48623 | 2024-09-28 03:32:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e6c4904-454f-3530-9c84-426c7f323c08 | -20.1505 | -46.57078 | 2024-09-28 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 913c1827-c212-3615-9b3e-f94648fceb6d | -20.14931 | -46.56568 | 2024-09-28 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d00de033-70b1-3120-bffd-0882c30dfeab | -20.14835 | -46.56986 | 2024-09-28 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e14756b0-9303-3496-8fb9-0b88d1a9feab | -20.14655 | -46.56081 | 2024-09-28 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d207ad3d-e09a-3983-9edd-ac7443f928d3 | -20.14565 | -46.56485 | 2024-09-28 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84dc80fc-024c-393a-a25a-f5ac3ab36b8b | -20.14446 | -46.55989 | 2024-09-28 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bf1b498b-d38c-3aa6-b70d-0a6982384e32 | -19.80333 | -45.72758 | 2024-09-28 03:32:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9b9eb6e4-cff3-3299-b95c-7a8b1dadc9cf | -19.79942 | -45.71842 | 2024-09-28 03:32:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20b45bf7-a001-3749-9823-f052608fa6f8 | -19.79856 | -45.7224 | 2024-09-28 03:32:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75347958-871c-39cd-919c-ec87d69747e1 | -19.7961 | -45.71954 | 2024-09-28 03:32:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0a719191-bd17-3a1a-a06d-daea7e1db72e | -19.57844 | -46.12371 | 2024-09-28 03:32:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d953d987-f607-3457-b1cb-c072384737a4 | -19.57264 | -46.12249 | 2024-09-28 03:32:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 145bd221-ea18-3c2b-8efe-2b3ae4908abf | -22.16329 | -45.82368 | 2024-09-28 03:32:00 | NOAA-20 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3596ca45-7181-3b9f-9b8f-c924775b8f53 | -22.16193 | -45.82306 | 2024-09-28 03:32:00 | NOAA-20 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f73a734b-ef70-3cf9-8e36-00d681e6ee9e | -21.95768 | -45.81618 | 2024-09-28 03:32:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| fe2e7be2-0321-36cd-9931-6e8e7519c02c | -21.95686 | -45.81979 | 2024-09-28 03:32:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| b701c4a9-94c6-368e-b92d-bfdd9bef479f | -21.9563 | -45.8175 | 2024-09-28 03:32:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f6924b54-838b-3776-ae47-efd1429a3c04 | -21.95551 | -45.82116 | 2024-09-28 03:32:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5862b7db-c4bb-3f59-80bb-6e3a17e46dc3 | -21.83507 | -46.13074 | 2024-09-28 03:32:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2d81218d-4bfe-38a8-988b-7c166d2fdea4 | -21.83422 | -46.13454 | 2024-09-28 03:32:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 207e8d7f-3ba7-38a8-adbc-b77f30a0e492 | -23.57022 | -47.35283 | 2024-09-28 03:32:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 834491e3-6ac6-3383-8def-ab4bdf5937cf | -23.56968 | -47.35361 | 2024-09-28 03:32:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 91ef2839-11ba-3e67-bc26-5047ae75c221 | -23.56912 | -47.35743 | 2024-09-28 03:32:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ccc34266-7eab-3b34-a81e-29ca6736d623 | -23.56861 | -47.35826 | 2024-09-28 03:32:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5b3591e6-08a7-3cff-b443-ab51afce2263 | -23.14488 | -47.17012 | 2024-09-28 03:32:00 | NOAA-20 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f04fad69-abd5-38f1-85bc-366644a56a26 | -23.13919 | -47.16859 | 2024-09-28 03:32:00 | NOAA-20 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7648af18-91e8-3e1a-8eb0-a3fa207e2f15 | -22.44901 | -46.89898 | 2024-09-28 03:32:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea9d2f40-f406-31aa-af39-1a329ad6d1e9 | -18.83356 | -46.68792 | 2024-09-28 03:32:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57c652dd-e795-3186-96ba-5cae3833404e | -18.8325 | -46.69276 | 2024-09-28 03:32:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26ffc872-7965-3e2a-9049-934837abfc28 | -22.19181 | -48.6119 | 2024-09-28 03:32:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b6111063-5a01-395a-b98c-a9e8708d419f | -22.1906 | -48.60892 | 2024-09-28 03:32:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 5102e77a-29e3-335c-b486-fc6ef5202641 | -22.18925 | -48.61455 | 2024-09-28 03:32:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 2cfcf173-0fbe-38e2-b2ea-265f48031f99 | -22.18789 | -48.62027 | 2024-09-28 03:32:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5594bf9c-26ef-3818-a746-293f6d56a989 | -22.18543 | -48.61057 | 2024-09-28 03:32:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| ba8f7ca5-cccb-3c3f-90d2-c9ed542c4a2c | -22.18407 | -48.6161 | 2024-09-28 03:32:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 96b2c336-ec8b-3388-8d04-5722b894bb3b | -22.18291 | -48.61307 | 2024-09-28 03:32:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 82e85d72-7937-3fa3-b980-38aef715603a | -22.18161 | -48.61849 | 2024-09-28 03:32:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| fe8a6a65-3402-3a6f-b134-a7411e8f6024 | -22.04852 | -47.24421 | 2024-09-28 03:32:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 33b400db-5146-3298-8011-f59eb6ebc475 | -22.04744 | -47.24888 | 2024-09-28 03:32:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 756cd178-ebc6-329b-bb6d-223237178f8b | -21.92172 | -48.4866 | 2024-09-28 03:32:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cec69db6-0281-3ac5-aa89-e45f20db82af | -21.88906 | -48.50391 | 2024-09-28 03:32:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1ac94ea-e19f-343c-9881-01fed234d334 | -21.88768 | -48.50972 | 2024-09-28 03:32:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82ff0a72-dbf4-3651-ac76-3d5b9b042896 | -21.88484 | -48.50062 | 2024-09-28 03:32:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91effa01-aa5e-3ac9-8b73-2adeaebdc45e | -21.88414 | -48.49642 | 2024-09-28 03:32:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21f12e62-2fa1-3cda-ad53-762a0c97d929 | -21.88344 | -48.50634 | 2024-09-28 03:32:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b95a97f5-3e9f-3e86-b684-b49a490dccec | -21.88281 | -48.50203 | 2024-09-28 03:32:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
