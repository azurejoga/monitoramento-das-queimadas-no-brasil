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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c449a74-e0e8-3e25-af97-167b82a76e5e | -11.66111 | -43.65131 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f25a1630-fb0c-37b9-802d-b54dd09bf7a3 | -10.95931 | -45.43926 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e5e8a8dd-cdbb-3638-ad6c-d36b6fb67947 | -11.6417 | -43.63168 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 1b36bce3-ffae-3a4a-b754-9224e5e9fafd | -11.6388 | -43.64007 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9738861a-8028-3e3d-b2cf-6b4f8e5678fe | -9.84333 | -38.92265 | 2026-10-05 15:54:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5a140090-421c-3a5e-ac28-87838805779d | -10.98421 | -39.93998 | 2026-10-05 15:54:00 | NOAA-20 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 42.7 |
| ce9f46c8-c0f1-3c08-9e65-a6590abc39c3 | -11.6379 | -43.63282 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a8093f30-3de8-3dee-89cd-796d759d3cbc | -10.96901 | -45.41426 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4fb4c650-4997-39af-a112-fba407a4f2a0 | -10.95116 | -45.42386 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 00999f0b-26c8-3e1a-aa85-891636a2208c | -9.08994 | -35.74142 | 2026-10-05 15:54:00 | NOAA-20 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 65a7d184-d285-3645-a1fd-533d96185fb3 | -11.56112 | -41.73843 | 2026-10-05 15:54:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 57492880-8afa-3624-98e3-975a99bb7dfd | -11.16123 | -43.49691 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| da60fc0d-0464-3ff3-9b14-9d0fde51c4be | -11.67199 | -43.64684 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e9ed310f-bbf7-3034-acce-440b385b3a6d | -11.6818 | -43.63338 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 22edb204-d6a2-3f7f-8f1c-1a1e02cf6bff | -12.10959 | -43.277 | 2026-10-05 15:54:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 76559828-1f85-30e4-9b43-76ab005c9111 | -11.72714 | -43.50292 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| eaa5abf6-0ffa-3573-88bf-0734df11f733 | -11.74063 | -43.4255 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87e1012d-fc15-3604-b58f-e6949547ad49 | -11.108 | -46.08967 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| b7c80ffc-2dc9-3af6-b4f0-00943e6d0152 | -10.97081 | -45.42942 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4e326579-eb78-3f07-a4fb-8d60fc64626e | -11.11382 | -46.08369 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 47d49788-e039-3f57-9be7-c6b03f4f8ebf | -11.68228 | -43.63739 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 219e076b-1cf6-3537-a246-f18e23e3ed7b | -11.63558 | -43.61407 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 96f0987d-5d6d-3b59-a09e-8c9d8c586695 | -11.45155 | -43.3951 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 84a2b29d-0a72-3d8a-ac20-641e54e112fd | -11.64687 | -43.62722 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f9c8cefa-a7ee-393b-ba0d-5ee972d37718 | -11.64352 | -43.63214 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8b4e7f59-cf69-3d6a-8ca4-7f54fbed1a07 | -11.16078 | -43.49326 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6da3e7b1-3bd3-3f94-a94c-71486a063009 | -11.43987 | -47.6856 | 2026-10-05 15:54:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f4b17a98-f99b-3cdf-be56-550dc3170262 | -10.18064 | -39.59491 | 2026-10-05 15:54:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c6c69598-33e3-3a31-8d49-32b6829c26a8 | -11.71721 | -43.50384 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f94a474a-7bd8-3b7d-a5cf-32792de9f87e | -11.63229 | -43.63353 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| c29c093f-2bbd-3b90-b6e5-c6141ede430b | -11.81669 | -47.36652 | 2026-10-05 15:54:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 0a42ec7f-d883-3cbe-a02f-ef8f98489508 | -11.64642 | -43.62338 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1fec8938-8e04-3711-8166-dbe7f2f71750 | -11.37387 | -42.54986 | 2026-10-05 15:54:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c1a5b1fb-3b25-3255-9f88-22a2deb29c7b | -11.63388 | -43.61352 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 03fb0ed1-8839-39c9-89e6-3c487dd7bb26 | -11.6846 | -43.65682 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| bd0afc94-e284-3d67-a70f-5bb877219dbf | -10.9639 | -45.42453 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4fad942c-2113-3b11-88e1-3316575ed760 | -10.30224 | -40.10948 | 2026-10-05 15:54:00 | NOAA-20 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4a8f7893-4889-32bd-9c33-c6f56905cba3 | -10.96742 | -45.4543 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 77974b42-1b63-307e-a69b-ecec8b12c4a1 | -11.28179 | -44.28913 | 2026-10-05 15:54:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8740460d-e3f4-3b71-92d4-1061a4eba046 | -11.63373 | -43.56358 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 968a5696-d127-3b3d-af82-2c6819bd7fb0 | -11.63835 | -43.63643 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 189e1f77-4da4-3dbf-b755-21c88bf286a1 | -10.74939 | -45.29543 | 2026-10-05 15:54:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 10bfb231-20f9-3e9e-bfab-a460403f7dd5 | -11.64126 | -43.62799 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 77e27626-2c79-3853-8192-65549c252bf9 | -11.64818 | -43.62384 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| dc138e96-e8c7-3514-bda5-a4653a815c62 | -10.74382 | -45.30118 | 2026-10-05 15:54:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f71cfcd1-67f2-3abe-bba8-0e6d93e70bc3 | -11.10739 | -46.08427 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 5c2b21ee-be51-35aa-9661-72e0098a33cc | -11.46257 | -43.39369 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 70839576-5229-3f45-86d0-3959763497a8 | -11.65583 | -43.60657 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fabab01f-aa80-33e1-8128-283c82541d65 | -11.27674 | -45.22488 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| df76a188-a06c-3503-a51f-2702f6bd1879 | -11.20385 | -47.13592 | 2026-10-05 15:54:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 72267406-bccf-38dd-8fa8-3293d47847ff | -10.95174 | -45.42876 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 07dee690-1aca-3917-996a-c2de4ec75e66 | -10.97707 | -45.42878 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 74bb9af2-1fa7-3f9b-999a-e656fa8739ea | -11.74705 | -43.43217 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5261d324-4c3b-3ced-b896-cf18acdc3a87 | -10.96682 | -45.44923 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 48b47012-8638-3e09-82d0-95e34e1cd9e1 | -11.63977 | -43.60204 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a637e334-e68d-388e-b68c-e856c67b3c11 | -11.64024 | -43.6058 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e257b200-93a3-33d4-b667-10dba7f014be | -11.66266 | -43.64839 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 2dbc4dce-2538-3f27-b85d-d2005c5ab729 | -11.63745 | -43.62918 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ad7833e3-c399-349a-a1b6-e23628562538 | -11.68316 | -43.64476 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 877c4774-f81c-31f4-b233-35a2a42e08a6 | -11.45706 | -43.39437 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 08718022-bb1f-3fac-92e0-fdac0b921731 | -10.06294 | -39.61453 | 2026-10-05 15:54:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| cfe450d2-640f-3aee-ba3c-b7440ae63da2 | -10.40047 | -40.50917 | 2026-10-05 15:54:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 92283287-597e-389a-9a96-6f97d9a4d710 | -11.72671 | -43.49917 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 66ea2f22-2e24-3317-8d0d-9250b1d10314 | -11.19893 | -39.31607 | 2026-10-05 15:54:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f9b904f1-9add-328e-9e33-778c62f027ba | -11.77015 | -44.92287 | 2026-10-05 15:54:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 975aacd5-3adf-35de-a2fc-140da9837f79 | -11.82817 | -43.54181 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0804e2ab-ea94-3756-b51d-00dd255ad7f5 | -11.11386 | -46.08315 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 7e628d1c-d5e9-3fad-8ebc-d2e7dd3919a9 | -10.95293 | -45.43887 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9056dbd0-6b58-3ad2-b179-ef5469ac1beb | -11.95987 | -43.29094 | 2026-10-05 15:54:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f93f9675-a41e-37cb-8304-3ac5064ce546 | -11.63565 | -43.62869 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 42384b89-f17e-3b2b-9d97-da4208e94902 | -10.97021 | -45.42437 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 31dfcf0a-38ea-3a45-af27-d6c0dbfbfe3a | -11.6631 | -43.65188 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 637e168f-cfcc-38a6-b92a-7441303b6596 | -11.11447 | -46.08907 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| e5a1b612-acc9-3737-bd63-14ffeba08d01 | -11.6309 | -43.62225 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 81c8e813-ed9c-3259-a7a5-7e27a56e5744 | -10.95233 | -45.43382 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 511aeb61-0b4b-3897-b762-3aa98db74389 | -11.63464 | -43.60649 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5a208886-0d5c-33f6-8159-eb8cb0c1b604 | -9.03664 | -45.16647 | 2026-10-05 15:54:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3744b624-f569-3092-adcf-6f0a52a867c4 | -7.66124 | -44.37391 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 578a3fb7-c3c2-3003-949a-8fea72929fb2 | -7.65059 | -44.3793 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2bc7be11-621d-3553-874e-7b09e03c7bac | -7.50834 | -35.00591 | 2026-10-05 15:54:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 98031a9c-c9b6-33dd-a0f3-358997dfbcb7 | -6.7038 | -45.22198 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2dec349b-c6d8-3a90-b39e-3f9a3fa058b9 | -7.48293 | -42.80163 | 2026-10-05 15:54:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ea11794f-5454-3f2f-a7be-c5be386d8667 | -6.9128 | -43.66537 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 03150c93-6f1d-36e8-b48f-ee2c6d11cdb9 | -9.84477 | -44.78999 | 2026-10-05 15:54:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5f2d7146-5d94-3676-b093-67617fb61bb3 | -8.64733 | -45.83898 | 2026-10-05 15:54:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d96fb54-88ff-39d6-b689-142331e512b2 | -8.00567 | -35.08738 | 2026-10-05 15:54:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 57d4308c-9246-3bd9-a94a-ca67cbbab71c | -9.16242 | -45.12778 | 2026-10-05 15:54:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 260c1a49-34da-3410-965a-4ae04a535690 | -7.83326 | -45.30143 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 39640137-9739-3665-9254-15869efecdee | -7.6501 | -44.37565 | 2026-10-05 15:54:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6d340b32-2a3a-38e0-9799-b0ef30cc365c | -6.33451 | -42.5544 | 2026-10-05 15:54:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ddd3eead-0605-3317-b16b-135220fa9ca7 | -6.60788 | -43.74273 | 2026-10-05 15:54:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 0dd73603-5ce9-3bdf-943f-83e432e3e0ea | -8.78012 | -47.5616 | 2026-10-05 15:54:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 506fa87a-eb8f-3c1d-9f7f-38f81ea4d3b6 | -6.60808 | -37.88754 | 2026-10-05 15:54:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 16d2fa8f-e898-3b4d-9add-1cc6104327b7 | -9.96948 | -45.60023 | 2026-10-05 15:54:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d4eb0f6b-8c92-3f41-94a8-881eacd0ac9b | -6.85136 | -35.01405 | 2026-10-05 15:54:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 85132f69-40ea-3f6c-881d-707a9faa836e | -7.8296 | -45.31913 | 2026-10-05 15:54:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 490731df-3873-3786-9107-8c3b52c64e08 | -6.91411 | -43.67486 | 2026-10-05 15:54:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 02bcaa67-01e8-3cd3-a42b-59acd66fe244 | -6.68738 | -45.23215 | 2026-10-05 15:54:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 27dd7b6d-44ea-37da-8c72-29c675e64be3 | -7.17206 | -42.0075 | 2026-10-05 15:54:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 73acdee7-2f55-3461-8ec8-c75165b523de | -6.59694 | -41.56375 | 2026-10-05 15:54:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |


[Clique aqui para ver as próximas entradas](README73.md)
