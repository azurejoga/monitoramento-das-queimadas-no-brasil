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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 038bc37c-f0b5-33d6-a267-39a6a50c39ad | -9.68936 | -44.52939 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 969a9740-5af3-3908-a510-44ae75ebcfc0 | -10.84708 | -47.87255 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3104ab3-26d1-3ba5-aa6e-701e9bf7d993 | -10.65232 | -45.24476 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e58b3cb4-ac91-3961-9d1c-6e2c5e9861ef | -11.37834 | -61.20902 | 2025-10-16 04:40:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddc2d4af-e2fe-3dd1-8b33-bfebeac16537 | -11.21131 | -43.99827 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b60ced0c-6c70-31b2-8592-ae035e3fa73b | -10.12451 | -52.3423 | 2025-10-16 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bd1dab2-944a-3e08-9660-271dbf726ff9 | -13.72249 | -43.99796 | 2025-10-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f7bd02d-f254-3e55-a5d5-6ce5a85b8418 | -9.69681 | -44.50701 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14216c52-a159-302b-a154-83f998298155 | -12.05025 | -47.65775 | 2025-10-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 166295b7-fa8d-33c4-bd3b-c4efc8aa0462 | -8.45143 | -44.18316 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7b1fb1e4-54c9-3620-b1e7-991c4fa2a0ae | -10.15092 | -44.54058 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe1e7b85-1746-3317-8212-bd7d2fdbbd43 | -13.8976 | -42.51273 | 2025-10-16 04:40:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eec4150e-d1c9-309d-a5f3-a55203bd75db | -10.89075 | -47.91582 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36c962c1-76ec-387b-8470-16142aca72b8 | -9.08789 | -47.95107 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c7a9f8c7-fbbc-39b8-8edc-06f7da79861f | -10.61099 | -42.31666 | 2025-10-16 04:40:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9e86c5bd-910c-3e55-9671-94e4c8349b6a | -8.46916 | -46.21637 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fef5ce66-3e8c-3006-804e-a2c738af301d | -9.71933 | -44.50867 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a804fb1-0491-33d9-b325-6cb713bd3c82 | -10.50738 | -43.37838 | 2025-10-16 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d78eebbd-e7af-36ba-ac6f-189912c39fe9 | -9.70375 | -44.48832 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d85af048-cd89-35c8-b349-6f322d109cfc | -11.31671 | -45.25046 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7ef2c8fe-41dd-37bf-821e-242dfe471e9f | -10.81549 | -43.93845 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f2ed07ab-b473-3aa7-8c14-59561990cdef | -8.54633 | -48.26368 | 2025-10-16 04:40:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 260cb47a-d1b3-3d05-a6a4-30a321afd465 | -10.03408 | -43.84054 | 2025-10-16 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e15ddd35-01f3-39f6-b373-9c02359b8bb7 | -11.75942 | -61.07823 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac0c7a9d-a032-3635-ad0d-733c4051db82 | -11.58553 | -44.08908 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6796103b-2c0c-3efb-97e3-da06b4d7dfa8 | -11.57319 | -48.55867 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66700fa1-9ec0-3277-aea4-05e7c09b2bf2 | -9.28816 | -45.36883 | 2025-10-16 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7494baf1-52ef-3844-91de-930308976fb1 | -8.41037 | -46.25684 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b7c5ce1c-77ba-350f-9fcf-d0fbe90f2da0 | -8.47248 | -44.18586 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| bbad8fe6-b1f9-3260-9952-4bb604453124 | -11.0042 | -49.5769 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b35aace0-e349-3d13-8905-1424210c8ec8 | -10.6728 | -45.33204 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4657afa0-bd44-317b-bfb4-244efd9463be | -10.16952 | -47.11498 | 2025-10-16 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f4bbc76-9a6e-38e0-b43d-9d3e0c5a14f1 | -11.70941 | -44.27083 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7826e135-3d9f-3c13-944e-6f9e5a92fb46 | -15.59884 | -42.40073 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af9a0d72-3054-3693-ba63-bbc55494b1d6 | -11.61602 | -48.78831 | 2025-10-16 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7ebac81-4e36-3a9d-b055-c41d0b5de9ad | -9.81421 | -47.63532 | 2025-10-16 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7818f68-375f-378e-8e7c-71321e05b1c9 | -11.67675 | -51.32554 | 2025-10-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 335ad8c9-73d5-3368-b7d4-60394f60144a | -9.34582 | -47.39852 | 2025-10-16 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37a1e48e-ccfe-30fd-b3a7-a8ef3d5871bd | -9.677 | -47.90137 | 2025-10-16 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5012b950-85e2-3de7-b395-43a6972a0201 | -10.87757 | -48.80164 | 2025-10-16 04:40:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ea5feb9-b4ae-3171-a68f-3b299a2bacd5 | -12.7208 | -48.63927 | 2025-10-16 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 97141ffb-b623-3a04-b9cc-d51ca67ba1d1 | -8.56229 | -44.58615 | 2025-10-16 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6d61512-7e0b-3f86-8b41-fbcea2fe5589 | -11.31722 | -45.24683 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d91485f-4db6-3fc8-8a38-2a7fa69554e0 | -13.70544 | -44.57917 | 2025-10-16 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6b58cef-3fee-35d0-8baa-2a058a28a31f | -10.88146 | -47.93036 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f31c4f12-de52-3348-a143-5a87bb2f966c | -15.96068 | -43.01799 | 2025-10-16 04:40:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40fe2293-3928-378b-89cd-885b9b9cf396 | -11.59032 | -44.08274 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92c44221-ce0e-34b3-94fe-512afb6bbf37 | -11.48922 | -44.10234 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d54fae6-d502-370f-ae55-8f9b20cf3ab9 | -10.83642 | -43.95011 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c5a096a-2a4b-3a7f-a472-f5a875ccf091 | -10.17014 | -47.11078 | 2025-10-16 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2c62ad7-d3f2-3f63-aa2f-6e98ac6dc225 | -10.30518 | -43.99067 | 2025-10-16 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ad75ceb-e5b8-33c6-b826-af8e0d725bac | -11.58793 | -44.07144 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2768783e-058a-398d-a56b-f2b74aef65f0 | -11.58673 | -44.08025 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b5b8dcf5-954e-388a-8800-c7ecbd38f8e0 | -9.72246 | -44.51702 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 097ea1fb-3e5d-31a6-8e42-af3371416e7e | -10.88435 | -47.93502 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b445d12-523b-32a9-8177-3e155172ce6f | -9.15851 | -46.87387 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e397ef67-fcb1-3f53-a492-a19acf62b03f | -15.96572 | -43.01879 | 2025-10-16 04:40:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ef615c30-dd05-3469-ba3a-6d7c096d66e6 | -11.96836 | -44.24634 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18ab556d-5b14-3ae7-918c-5ef0608ed7ef | -11.45664 | -47.63434 | 2025-10-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15db11d3-9365-3233-a2a2-397b6e93904a | -11.60802 | -48.5369 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2abbde65-d576-3457-81d4-22531ebcf9f6 | -11.42708 | -44.13096 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acdb32b2-92a0-3717-933b-3861fa291f84 | -12.83945 | -43.81472 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 912f879d-b89f-34f2-9960-f8369eab660a | -11.42702 | -44.0639 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8fac693-b036-3697-8ca4-371a0e65b8a6 | -14.74793 | -42.37572 | 2025-10-16 04:40:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| aba466ec-2fe7-33f8-835b-8141eb90b7b6 | -8.47198 | -46.24813 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2629e446-6671-3e56-9673-0a93a2ecc34d | -10.7251 | -47.59072 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b84be14-462d-320c-8e97-d9fc96209922 | -8.07092 | -46.42842 | 2025-10-16 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21f9f643-28c1-3658-b7b4-f376c4753673 | -10.1318 | -44.57801 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9c587ff7-b4a4-358c-b101-1efcc372031c | -10.12615 | -44.55756 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4690caa6-909a-3671-89a3-37a87c8a3ca4 | -11.4509 | -44.05384 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ea446aa-5d79-32bf-9b91-4fa8b524090a | -10.80999 | -47.96859 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dee6ae2-f505-3b9f-ac44-163defb6760b | -14.64544 | -42.38303 | 2025-10-16 04:40:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3b719c54-8f0a-3895-a0cd-e6de058c5e4a | -10.03963 | -43.83261 | 2025-10-16 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a111a25e-d656-3911-982f-1300c73e585c | -9.08847 | -47.94729 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 073342bc-b77e-391c-b522-dc90cc144f54 | -12.72313 | -48.64734 | 2025-10-16 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 26537df2-772c-3013-8cde-eca62cbf0436 | -10.66175 | -45.29445 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4cbde2c8-27b0-3e34-a7b4-e51210851e6c | -11.73103 | -62.29477 | 2025-10-16 04:40:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e35d7b33-a9d3-3cd3-8d76-414a55a0a293 | -9.36837 | -46.94816 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5af39b0-c9fe-3390-8d99-ddbb732785f6 | -15.80597 | -42.45603 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e7a2f7c-260e-39ed-93ae-e1fea58d5e87 | -11.47695 | -49.81856 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14ae7a3d-6b9a-30e9-aa25-52af8fdccdf9 | -13.65591 | -43.93393 | 2025-10-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2d008cd6-2a4b-3d96-8e4e-46f02424daa9 | -9.82254 | -45.26991 | 2025-10-16 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fcf6fde-5cab-3710-92a6-d314f795c412 | -11.50706 | -44.069 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3caf37f0-d5f6-315c-acb5-1c4a1075457a | -12.60437 | -56.51168 | 2025-10-16 04:40:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1919c376-641e-3831-b8e5-437ced754264 | -11.32843 | -45.25579 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7bc76fa-e0b2-32fb-99b0-17beeddd9c50 | -11.19691 | -46.41726 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 498cd46f-580e-3706-910a-ce3337a9b7f9 | -10.90657 | -47.58651 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d9aa496-4b05-330e-ba1c-91498b4a2570 | -11.47586 | -44.10227 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e18d031-4eb2-3fe8-9fb4-c74d71beeb41 | -10.9763 | -48.75249 | 2025-10-16 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cf9109d-b4ae-3152-9db2-706dcb45b224 | -11.44116 | -44.15956 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f3a61608-cde0-3938-8b27-1fb8080faa41 | -9.22566 | -48.59829 | 2025-10-16 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c7934b85-5d7b-3681-a17c-768d3d5cf24d | -10.62306 | -45.24775 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa103c47-d97c-3f92-964d-04c42b62131e | -10.13257 | -44.58135 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2d21285b-212e-314c-9913-93bcba291998 | -10.51196 | -43.37902 | 2025-10-16 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20427035-7dc4-3f4c-9485-0cb7919a7046 | -12.64296 | -44.30402 | 2025-10-16 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c126bcf-98b5-3955-8f7c-69894c32eec4 | -9.15611 | -46.865 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| db96c252-9e32-3bbb-9afb-a48210dd45fc | -10.86744 | -44.41453 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bbb1373-06af-353a-9ea0-0d5cf7be4c52 | -11.48266 | -44.08345 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7bdfe7c-97b0-3414-bdaa-06ad2fa97b93 | -10.65636 | -45.24532 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80bb0a2e-c8ed-31fe-8752-7fed8fc918f5 | -10.66688 | -45.28729 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README61.md)
