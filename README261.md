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

## Dados Diários - Página 261

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a49becc7-b471-3298-904a-39b3100ec527 | -14.59468 | -41.34539 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f2a97844-bdc8-38ba-8a86-2a9dc915e754 | -15.69519 | -40.72881 | 2026-10-09 15:58:00 | NPP-375 | MATA VERDE | MINAS GERAIS | Brasil | 3140555 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 32d0002e-ef86-3893-9036-25deac8c8a18 | -14.06408 | -43.83743 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 2889b63f-acdd-3d73-846c-6b4a21ddde16 | -17.50953 | -43.67422 | 2026-10-09 15:58:00 | NPP-375 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1d470253-ef2e-3db1-b6a1-648dcf6c8ac8 | -11.83219 | -43.59004 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| b66fe044-d162-388a-adba-9b4827d038b4 | -15.00596 | -40.47347 | 2026-10-09 15:58:00 | NPP-375 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 58161bbf-b12d-34e0-9967-854c097e355a | -15.37668 | -41.89909 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| 0f5e83c7-ba30-3f5e-be4a-c3858174e42e | -12.00288 | -43.45087 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d7fd5bb7-1643-3bf6-a986-7011d14ca892 | -16.5008 | -41.20361 | 2026-10-09 15:58:00 | NPP-375 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d333802b-c301-38f9-bada-fa53fd3b5ec6 | -15.38946 | -41.91528 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| a6368064-32e7-344f-8965-40fb1417ef07 | -11.6324 | -42.76132 | 2026-10-09 15:58:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 770282b4-eade-31c5-826d-8a3c2ab1c0c4 | -15.79088 | -43.38205 | 2026-10-09 15:58:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d34bf0c-d5ab-3314-a4c4-21d19a1d3637 | -15.92059 | -38.96543 | 2026-10-09 15:58:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9022e065-6355-3e74-8f93-db6d7d93cac1 | -12.20193 | -44.7393 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 4a4748d7-4e9d-3721-a304-ed4e2849b8e4 | -11.59263 | -43.70021 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 31dce66d-eead-3c92-a6c3-8827063e184d | -15.01337 | -46.25979 | 2026-10-09 15:58:00 | NPP-375 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d0b2e202-5408-32b1-b573-a4397f8ae71d | -12.33783 | -47.09684 | 2026-10-09 15:58:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1c7f336e-f406-3870-a5f2-66445df9f0e8 | -16.99547 | -45.46918 | 2026-10-09 15:58:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 56fa7d1f-9720-3efb-9ab8-bf8f79505630 | -15.11676 | -43.63447 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 720aeec4-7f8f-345c-b696-4fc37624a5c2 | -11.87035 | -43.56809 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d7f28425-526c-34a5-b93d-3b651506bdba | -16.07536 | -45.97425 | 2026-10-09 15:58:00 | NPP-375 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8723ab69-86d0-3399-9d7a-9b362b81163e | -12.82775 | -44.62922 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 600f3ef1-25e1-37dd-9462-b0993d026354 | -11.99893 | -43.45585 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 205b8d66-955a-3bb2-a071-e5e14eb2d53c | -16.83275 | -41.03846 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 4dabd557-5e23-3075-8e91-042b3b57af63 | -11.83314 | -43.59805 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a8a718ea-160c-31dd-b33b-bd5a16ec8272 | -14.92971 | -41.79465 | 2026-10-09 15:58:00 | NPP-375 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 367aa71e-8e46-3dca-acbd-455ae680d5b6 | -11.98778 | -43.46939 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ba7d1e20-6426-3cca-b95a-7d2b8a821326 | -12.23865 | -44.73036 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 932a11a2-4c0d-3fc6-9a8c-d2330a9936db | -15.17219 | -43.80944 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4b9d032d-1313-344c-af4e-fa9f11b251dd | -17.5157 | -43.67338 | 2026-10-09 15:58:00 | NPP-375 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 64358f3f-fb14-327b-8b5b-b78f9e1867fd | -14.0633 | -44.79729 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d2360380-e0f2-3655-96a5-c346f3df7ea5 | -15.54084 | -41.01612 | 2026-10-09 15:58:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 32d608e3-601c-3830-bf63-5eac59e1ced0 | -14.89919 | -46.16668 | 2026-10-09 15:58:00 | NPP-375 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fb5ca24a-4758-3ec2-863e-0ea815cdc473 | -13.2452 | -39.76347 | 2026-10-09 15:58:00 | NPP-375 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 60d9d24a-9d83-3e1b-92f9-01c511d8fe08 | -11.99025 | -43.48098 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f4103f73-8c19-3ed4-b9c9-d62af8f80a5e | -15.37871 | -41.91685 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 272.3 |
| 3d604379-6c00-3bb7-b05b-7d2bafe91ca3 | -16.30047 | -41.20855 | 2026-10-09 15:58:00 | NPP-375 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 935674e9-e715-32fc-8b8d-fa626fac3c71 | -12.18512 | -44.64785 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9b1b0c57-7b90-3d05-a539-ffb56527a62c | -11.98394 | -43.48538 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bc453f0b-72b3-3545-8b33-68d5ea59a423 | -12.2158 | -43.94868 | 2026-10-09 15:58:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 7e5da4dc-3344-3342-bf84-e5fe32f0f228 | -12.81263 | -42.34716 | 2026-10-09 15:58:00 | NPP-375 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b39426f9-bf01-3413-9f22-9aea9023ea50 | -11.31272 | -44.82823 | 2026-10-09 15:58:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 173ed9d7-36ff-3878-b269-66ecb795ef1e | -14.82792 | -42.3174 | 2026-10-09 15:58:00 | NPP-375 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 429f7cd8-8d27-3203-832e-e63615468885 | -14.44161 | -40.79068 | 2026-10-09 15:58:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 7783a98c-91f4-3660-b659-2a4b8c62167e | -12.16031 | -44.74269 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 57d73ea9-2562-385c-99d4-528934e56444 | -15.576 | -44.52851 | 2026-10-09 15:58:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9d5bb94b-f07f-3304-9ade-36b5ee17bd99 | -15.3933 | -41.90121 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.4 |
| cccc84e0-3fdf-3b0a-91f3-0dbef429d89a | -15.7829 | -44.68958 | 2026-10-09 15:58:00 | NPP-375 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8a7d1ed3-13a7-39eb-a2ea-a40dd5012d28 | -11.20756 | -40.56411 | 2026-10-09 15:58:00 | NPP-375 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 401d30a8-4d42-351c-b7e8-6d0643997d43 | -13.49565 | -40.7264 | 2026-10-09 15:58:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b91bea26-f448-34dc-9bdf-81b20e7c8592 | -18.31857 | -42.37785 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.9 |
| 4f4f9b58-2896-3edb-9ebc-ddd1752044f3 | -13.47371 | -42.47942 | 2026-10-09 15:58:00 | NPP-375 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 94d28027-231e-37e4-92fe-6361999cea64 | -18.37599 | -42.369 | 2026-10-09 15:58:00 | NPP-375 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 355654f2-9af0-3a19-a9b4-744ae75bf82b | -11.57594 | -43.65966 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 412b70ea-dffb-33a5-af76-523ee2d2f1f7 | -15.9106 | -38.95767 | 2026-10-09 15:58:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 210a1974-ac6f-317c-b2df-8a39b2bb0c2a | -12.21917 | -44.62178 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8aeb07b7-ee16-391a-8657-a7de2e913ecc | -11.99555 | -43.47659 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e2400ce1-32ce-3cb7-8f0d-31c47da63968 | -11.73363 | -43.50203 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d4a2bd81-d51a-3bb4-b445-5e8ff7482f77 | -15.84843 | -42.02607 | 2026-10-09 15:58:00 | NPP-375 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.4 |
| cbffa680-1695-3aaf-af59-2c156d8c1ca8 | -15.85367 | -42.02624 | 2026-10-09 15:58:00 | NPP-375 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 6fde881a-116f-3344-8fda-4055bd1c052b | -12.00412 | -43.45068 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 595f816a-4131-3956-8b93-efe3fcc68e46 | -11.78738 | -45.59108 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6301f140-9244-3d98-bec0-0b888a39bbd3 | -14.72947 | -40.78749 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4024ee01-bd7a-31e6-9085-9761d1bf0b69 | -11.98269 | -43.46563 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| a8e14bf4-1b44-304a-ad1c-d93bb3c97da7 | -15.38667 | -41.89105 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| cb9b05e8-2c59-30b2-9366-73323474d0b7 | -11.61665 | -43.60622 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f414917b-3cc7-38a5-a974-922f96c5b225 | -12.65778 | -43.21541 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 84449487-4753-3016-8c10-874b818cae93 | -12.05813 | -43.41827 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 205c2184-3f36-339e-b283-9a5659501e7d | -12.12851 | -43.31108 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 71f0a9a8-654d-3bb9-bf35-c2abac81d805 | -11.96672 | -43.48686 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 13c63105-3356-377e-943e-2aead7defc7a | -14.58227 | -41.20058 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 3de4aeec-a6da-3f3c-bb17-d7d067ac77af | -17.10277 | -41.57259 | 2026-10-09 15:58:00 | NPP-375 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.0 |
| f02b5e6d-a170-3866-8bbe-f66baf3edde3 | -18.31779 | -42.36982 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| 80d53770-7b4b-3649-b9b6-68f8270092f7 | -16.07474 | -45.96754 | 2026-10-09 15:58:00 | NPP-375 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 025369fc-0b54-3a45-9c81-0d4af7663b3e | -16.71271 | -41.88327 | 2026-10-09 15:58:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 8f8aff62-1168-3be5-8bd2-e68557f0de9a | -17.51003 | -43.67912 | 2026-10-09 15:58:00 | NPP-375 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5353f5ba-0a2f-30dc-a6d4-81ffd4ae2d5d | -11.88663 | -47.39412 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2ff20065-4f21-30a3-997f-01ad0a708251 | -11.47109 | -43.39412 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| c6015bb5-9d8e-3d50-ab92-317ff19891f2 | -11.88383 | -47.38779 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 70fec812-8165-337c-a727-b0c8caabf8d5 | -15.37583 | -41.89172 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| cb52790b-ae20-3870-a196-bbfa34a74e77 | -11.59886 | -43.70322 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| ec7e5e35-6751-352b-a364-6dd016e207c7 | -16.96867 | -41.1621 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 28f1297e-9964-3cad-9fd4-ede62970a6aa | -13.40606 | -43.48159 | 2026-10-09 15:58:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 82c5308b-bef8-3975-8502-2090b4cee2b9 | -11.59598 | -43.63309 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 46524150-58a9-3025-9e02-9ff58b5f9b81 | -11.31404 | -44.82671 | 2026-10-09 15:58:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 054dfc36-a05e-3497-8cae-e7e11c06927f | -12.20929 | -44.74854 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 9d5cc4de-4a01-3899-b294-500fcf8bcb36 | -11.48339 | -39.07247 | 2026-10-09 15:58:00 | NPP-375 | BARROCAS | BAHIA | Brasil | 2903276 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0caa6168-93db-3f92-ac27-eb91a7d539e1 | -14.05476 | -44.79122 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d4bd91c3-4331-3f61-b8e2-f536d012f2e8 | -17.95013 | -44.35101 | 2026-10-09 15:58:00 | NPP-375 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4b3c94b3-4d18-3f05-92eb-571e27971766 | -11.98043 | -43.45672 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 85f9258e-3e3d-359b-8353-c8f20242c3bb | -15.2579 | -42.38346 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| c2ad3d71-1083-3f84-95fc-99abfb5e3492 | -13.97133 | -43.93494 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 60ec5214-4605-359c-a5d4-e111e3afc0f0 | -12.28547 | -38.74942 | 2026-10-09 15:58:00 | NPP-375 | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 23bd0c1e-50ab-36ea-9a3e-957b2a17b25f | -13.28419 | -46.97167 | 2026-10-09 15:58:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c0f481df-9436-32f7-9b11-34215a2fb43b | -15.69556 | -42.36364 | 2026-10-09 15:58:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 420000a4-1bd2-3032-9b03-4e2dbbaa6985 | -13.08419 | -46.80497 | 2026-10-09 15:58:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 8437fecc-0f6f-37eb-941b-f79e873098ff | -17.16555 | -46.12866 | 2026-10-09 15:58:00 | NPP-375 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 619c136c-8641-3ca4-8611-ff5bc6223b21 | -12.25282 | -44.75549 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7c6d852b-02dc-341b-abf6-bd96cb36b8f8 | -11.97905 | -43.49287 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 06a7ec29-e14a-35bb-ac93-311acb97793f | -12.05289 | -43.42278 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |


[Clique aqui para ver as próximas entradas](README262.md)
