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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6582db7-72e3-35d4-92ea-7b7d67ab15d1 | -6.62092 | -41.46771 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e735b205-3b3a-3e5d-8c7e-8b349f351b5f | -6.76867 | -41.44616 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 40d538b7-96d0-3691-8020-cb7817ef7378 | -12.84863 | -46.4682 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9139ef80-7acd-3b56-b45d-86b64ed2b4a5 | -6.61494 | -41.4664 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2f6b260e-716c-3fe3-b3db-7ac607fd9eae | -6.39766 | -42.28701 | 2025-11-17 03:27:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| aec72a71-8a34-387d-bf86-ffc92923263d | -10.9669 | -44.53478 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9e8c4e03-c517-3bc6-97ee-5392af2ed36f | -11.96626 | -44.93993 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a781682-983d-39f1-895f-c01cf976a880 | -12.85599 | -46.46921 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25ba6cbb-6f33-37ad-b20a-6d3cd52a09cb | -12.8667 | -46.03235 | 2025-11-17 03:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bffce415-06ba-31ab-89c1-65c6611463c1 | -7.09625 | -42.73346 | 2025-11-17 03:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fcf71d24-05ea-3de3-a013-853cb20b2e5f | -6.68488 | -42.04339 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| 612ccf47-b6a9-3499-aede-8b73ce9d3435 | -11.41065 | -43.32106 | 2025-11-17 03:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab2ca99b-329e-345b-a15a-c63951a1e6ea | -6.77534 | -41.44347 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1bdfbbfa-4c5e-3755-95a0-0036e32215fe | -10.55691 | -44.82331 | 2025-11-17 03:27:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f74a619a-1059-3174-9bec-d629b532ac26 | -11.62025 | -43.90884 | 2025-11-17 03:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f2004b76-fdc2-3250-9d0d-ea8b9cc39a4c | -7.6178 | -42.58172 | 2025-11-17 03:27:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91ac2902-6567-3a4f-9d8c-a71e43cc85ea | -11.67328 | -44.73187 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edbdad9b-4b96-3d19-959a-86845c47e437 | -10.96816 | -44.52875 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ce965523-fafc-3f85-9ac5-edabaab833d2 | -9.74767 | -43.97052 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9cb50b16-e369-395d-aba2-611ff3a0c4f2 | -10.88085 | -44.6376 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d79fa5c-94c4-3176-af78-b13cc9f09d70 | -9.7159 | -43.95692 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e085946e-3277-3f02-bb1a-8f937c024039 | -11.13179 | -44.94112 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e59dc8cd-7d05-3013-8333-93afb237421c | -11.70958 | -44.4545 | 2025-11-17 03:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa1c43a0-6131-3b64-903c-8f50e5079551 | -5.88536 | -43.97593 | 2025-11-17 03:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f9e395f-d385-37b3-8c30-2f743de51df6 | -6.39289 | -42.2881 | 2025-11-17 03:27:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 84eef670-ea28-3672-873a-e571f001397b | -11.71077 | -44.4487 | 2025-11-17 03:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf9c2435-696c-3990-9a2b-914147402cda | -10.95965 | -44.5275 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6b47e42-6ccb-36f7-acf2-be1e430c781c | -12.80066 | -46.44512 | 2025-11-17 03:27:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6fc2e9b7-356c-3f7f-837b-553e133b82a5 | -10.81984 | -44.3117 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62886310-df5e-367a-9111-4b3deee0e5c6 | -6.39924 | -42.28925 | 2025-11-17 03:27:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 19973053-5aaa-3236-b9ab-cf5077fc55cb | -11.68122 | -44.72728 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26ae45fe-7009-3c99-b377-a0027eff2315 | -9.74884 | -43.96471 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c67da6b3-8a4f-35ad-b3be-0722374fb9d5 | -9.72433 | -43.96472 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5926ec9e-ce3f-3d11-93e7-bb5cd59c5161 | -9.71002 | -43.96733 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 99decaed-90f5-3846-b662-c2b95a0ad051 | -6.34879 | -41.75435 | 2025-11-17 03:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 455432a8-eb07-33b3-b935-c5f14d852fd3 | -6.68603 | -42.04955 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 7b7ce77d-b4d1-33af-bd8b-bf658340be58 | -11.66533 | -44.73647 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 580b3c27-645f-3ada-ad6e-f5b347a5b897 | -6.67773 | -42.04723 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| f3617f51-a1b2-3611-8136-314d951e68b8 | -6.68778 | -42.03975 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 2c9cb88f-fb1c-33a2-82d8-69ce959b0f5f | -6.8988 | -38.88139 | 2025-11-17 03:27:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2ab3ab80-72b7-3de1-9d24-93e755a0a48d | -12.43177 | -43.17336 | 2025-11-17 03:27:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6f138eba-9f47-3cba-856e-d592cacf2755 | -8.24725 | -41.42654 | 2025-11-17 03:27:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21607fd6-2e2c-3873-91e5-49fa781c8582 | -7.86547 | -37.56798 | 2025-11-17 03:27:00 | NPP-375D | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ba29b579-476d-3679-b6a4-3ddbe2726bb7 | -9.06271 | -44.79467 | 2025-11-17 03:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ee697422-01ce-31c4-8439-e123c6b06bca | -11.66783 | -44.72432 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54dda328-376d-3753-89ac-b5c413eb3504 | -12.79861 | -46.44931 | 2025-11-17 03:27:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78252bc1-fc2b-32cb-bab6-7c5aaf7a1917 | -12.80146 | -46.43621 | 2025-11-17 03:27:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| edce65e7-e400-3e6e-8cc5-6561bce2f1f0 | -9.06405 | -44.78795 | 2025-11-17 03:27:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6c2d5919-673e-3c5c-8203-0a7bd5db7f6d | -11.13319 | -44.93425 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b80ff37e-e4d3-3f47-9a07-04be9a0a210f | -8.80809 | -40.40759 | 2025-11-17 03:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b023fa78-443f-3bcc-852f-72adc8c5b142 | -12.42575 | -43.17196 | 2025-11-17 03:27:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0ac92598-3d16-3b6e-8a8e-e2cf12916155 | -12.85952 | -46.03135 | 2025-11-17 03:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e65dc9e3-e5c9-3eca-862a-993e4a6f9f31 | -11.78326 | -44.65047 | 2025-11-17 03:27:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abe490e9-6dd2-330d-aa72-2c9d415c36e2 | -6.67239 | -42.04133 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| ac1a3506-e926-3435-ad03-045c46c86ee7 | -11.1329 | -44.93303 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0dd69b60-00a5-3111-a292-fe0954d0f4b9 | -6.71668 | -42.94192 | 2025-11-17 03:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 498e6975-20a5-34e6-a759-eeafb82af1de | -10.78703 | -44.32289 | 2025-11-17 03:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f330630-114f-365e-b66c-1995009bf7c7 | -6.68515 | -42.05449 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| aa96f1dc-3e7c-3690-9423-0412c4d5edae | -11.67203 | -44.73793 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94d446dc-8e0f-332b-8e2d-1264ec28ac2c | -6.71009 | -42.94086 | 2025-11-17 03:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 860af860-cb07-39c3-8ea8-2426508fb7cb | -12.88891 | -46.45736 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be5e0c91-4027-3c54-af1a-dcf16b899d72 | -9.74414 | -43.96924 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 563947a2-16c9-3265-abd5-35b8f45cdb77 | -9.72245 | -43.95868 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a3a8332d-0387-3296-ae4a-0c903621ead0 | -8.3627 | -40.97074 | 2025-11-17 03:27:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 43f511a6-c07e-3023-9db7-d69ab0905c64 | -12.80012 | -46.44239 | 2025-11-17 03:27:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c649ddc6-8072-3394-93b1-fcd0b38a041d | -12.46235 | -39.63761 | 2025-11-17 03:27:00 | NPP-375D | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae8151e4-6f08-3f97-b6b8-685bc35144df | -7.70958 | -42.94836 | 2025-11-17 03:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2a5d08c5-51de-364d-9597-11731983ef44 | -6.67891 | -42.05338 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 0f555ffb-b4a6-3022-a212-4ccfac75ab89 | -7.08904 | -42.73758 | 2025-11-17 03:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6e388a76-4bd5-3352-aeee-5a4a9548eabb | -7.7022 | -42.95195 | 2025-11-17 03:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c2888660-43f6-31cb-a689-57c32ac27228 | -6.68578 | -42.03852 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| fab257ae-4f0d-3ab1-8bf3-e841bf871af4 | -12.32621 | -44.22395 | 2025-11-17 03:27:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de2ea4e7-9f63-39f5-b3fa-032260e570fd | -7.08998 | -42.73242 | 2025-11-17 03:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d0917d93-9887-3063-89e5-92566ccb53b6 | -6.68305 | -42.05323 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 11b87f19-ceb2-373d-8070-546e0de1b10b | -9.71893 | -43.95705 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3f525ab7-62ae-30da-8569-6e3ad7bf9116 | -6.67333 | -42.03631 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 9da3077f-b53e-3b32-8dc2-ce57139321e3 | -7.09647 | -42.73343 | 2025-11-17 03:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 91499ae2-aa70-31a5-a5b9-d00eb4d7fd20 | -12.85559 | -46.46627 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3e2c99b-0871-3f19-9294-e21c090d6b51 | -12.85383 | -46.47448 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 974f55a9-5a9a-3473-ad28-4f65f909e414 | -9.7287 | -43.97772 | 2025-11-17 03:27:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 39d125b8-7b27-3144-ab7e-a02d2a535128 | -6.3558 | -41.75069 | 2025-11-17 03:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7e389f1c-524a-3030-a13f-4a60a04ed0e0 | -13.46468 | -44.037 | 2025-11-17 03:27:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98c33c85-f8c7-3621-9176-45f49073cc2d | -8.11535 | -43.52755 | 2025-11-17 03:27:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66d1fb5a-e856-3fc9-8183-2a211ff4aee8 | -11.40246 | -43.32968 | 2025-11-17 03:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6c790ec-3541-34b8-81da-2208ee9028cc | -11.67637 | -44.72742 | 2025-11-17 03:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 794844fe-e85c-37c0-b194-f1b5f6bbaf9d | -6.67981 | -42.04837 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| c73d3d32-6cd4-3d4a-843d-db09dcb877a6 | -12.84685 | -46.47626 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8b2cd6f-aa44-3fe0-9fa9-91c084703b61 | -7.12636 | -41.66246 | 2025-11-17 03:27:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ca9093b7-ed04-3112-b168-4fa91978468e | -12.87052 | -46.43764 | 2025-11-17 03:27:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f998c1fc-2cd3-33a3-8790-91631b15be28 | -6.67533 | -42.03745 | 2025-11-17 03:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 0cd371b0-39ae-31cf-b20a-320082fe0240 | -6.87387 | -39.84221 | 2025-11-17 03:27:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2a4ff1a7-3ee4-3675-beec-053c7a36e003 | -14.65568 | -46.54351 | 2025-11-17 03:29:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c31d418c-0862-311d-851d-93683fe73345 | -14.65178 | -46.54192 | 2025-11-17 03:29:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ad5051e-b962-3e36-bec7-434c0c1db400 | -14.64806 | -46.54455 | 2025-11-17 03:29:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5603e0df-98cb-3409-9624-a6a935779fda | -14.65001 | -46.54974 | 2025-11-17 03:29:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3510d819-5a5c-3e44-95a7-0db26a74a70e | -2.5238 | -47.8115 | 2025-11-17 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 9dccde68-3d08-3016-8388-fc0cf9534bef | -5.0401 | -43.5973 | 2025-11-17 03:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 56a89093-84f6-324a-8318-530645d71a57 | -6.6873 | -42.0535 | 2025-11-17 03:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 9eedc635-4c61-3937-a9c3-f510760a20b4 | -2.5053 | -47.812 | 2025-11-17 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 80f7badb-a563-3a11-99cd-d4e8afcb9fc5 | -6.6875 | -42.0296 | 2025-11-17 03:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |


[Clique aqui para ver as próximas entradas](README13.md)
