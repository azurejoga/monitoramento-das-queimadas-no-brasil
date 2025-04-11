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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e05a15b-1657-3dea-a07c-37abc9a50aeb | -10.26054 | -39.57561 | 2025-04-11 03:49:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6b59312d-7c5c-336d-b543-1dcd88901403 | -11.91597 | -38.13256 | 2025-04-11 03:49:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b7f4ebf7-469d-3029-acce-4e2a44079d1f | -9.63 | -36.81527 | 2025-04-11 03:49:00 | NPP-375D | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9d131296-e319-38f7-929d-1e6b422390ca | -11.90227 | -37.64225 | 2025-04-11 03:49:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c23b77c5-2fcb-38d4-895c-cbf5a722dac6 | -15.80786 | -43.57236 | 2025-04-11 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 48dd943f-77aa-3c53-bfcc-4d9ef263e756 | -20.19195 | -51.15649 | 2025-04-11 03:51:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2dcf740f-f4f6-3ecd-8211-b5fe7a539680 | -21.07709 | -48.6707 | 2025-04-11 03:51:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| ea03a2f2-f61a-3dc5-8265-47555144a6ab | -20.191 | -51.16074 | 2025-04-11 03:51:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 888be91d-afd6-3326-ab4a-9dd07a06247c | -17.78115 | -42.80804 | 2025-04-11 03:51:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b20e7d6-3518-3e3f-90f8-1ec21aa13209 | -21.08134 | -48.67116 | 2025-04-11 03:51:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| e7dd9041-90e5-37d6-af63-c0271930e3a1 | -20.18519 | -51.15946 | 2025-04-11 03:51:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bf6a13b4-fa2b-3340-89f3-539c497e5d4d | -17.75072 | -42.89477 | 2025-04-11 03:51:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3719773f-1063-39e9-8b32-be71dc38f4b9 | -20.18431 | -51.15818 | 2025-04-11 03:51:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7a4192f-ebd4-3fb4-9266-2774d57bbcd4 | -20.76272 | -46.76996 | 2025-04-11 03:51:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 48e7e2f9-dfc4-3cce-a16d-c952f243bc2f | -21.17835 | -43.98145 | 2025-04-11 03:51:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c0d4279a-8c4b-34e0-bb92-f2995d7ebe40 | -15.80395 | -43.57161 | 2025-04-11 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 33ef1d5d-0a52-30ec-8bc1-c56ec0455970 | -20.18332 | -51.16249 | 2025-04-11 03:51:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f0ea3f3-e72f-335f-961a-af48d362e4f6 | -20.18614 | -51.15517 | 2025-04-11 03:51:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 074989f9-9986-36b7-9314-9589931c8302 | -21.91269 | -42.26142 | 2025-04-11 03:51:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1c8bbfbb-0727-3032-9f56-0e8f4e3b6918 | -15.80878 | -43.56725 | 2025-04-11 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c401d59c-dffa-3235-8787-e97ff85b1535 | -20.1911 | -51.15518 | 2025-04-11 03:51:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| badc4b75-7a82-3fb4-b2bb-bdc7c7fc82fd | -21.07829 | -48.66504 | 2025-04-11 03:51:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 2111def6-0693-3baf-9e8a-4f9e9bebd5a5 | -20.19013 | -51.15941 | 2025-04-11 03:51:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6b04881c-7de5-3cef-9081-a494451a0cef | -21.07646 | -48.66998 | 2025-04-11 03:51:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 05b53941-d85c-392b-9a5a-1158d3d038b5 | -15.80487 | -43.56651 | 2025-04-11 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 074a07df-2ad0-3916-af08-053bbbc52a74 | -19.764 | -48.93388 | 2025-04-11 03:51:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe959423-5fc1-3911-bcc5-3b572214ed46 | -19.76912 | -48.93499 | 2025-04-11 03:51:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 38477b88-63aa-3262-8cf3-8ffbcf83b126 | -23.40661 | -46.55698 | 2025-04-11 03:53:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ee573359-e0ea-3c44-baf8-84c675430250 | -22.85722 | -42.98015 | 2025-04-11 03:53:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0274c980-20ef-3534-a5b3-670317398d8e | -22.9019 | -43.75208 | 2025-04-11 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b66b121b-a847-38ca-b3b8-4fab7ab11214 | -22.7851 | -43.75715 | 2025-04-11 03:53:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c2722f7c-dcad-39a8-91c4-2ac0c9210649 | -23.33794 | -46.77407 | 2025-04-11 03:53:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a7a3ec7f-87f2-3f4e-b5d7-ab30d9a1e8a7 | -22.69568 | -43.43142 | 2025-04-11 03:53:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 52eafa68-6689-3d0a-970b-7a3bc3c39e83 | -22.47851 | -48.36383 | 2025-04-11 03:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 342920c0-e3cb-3215-a4df-f794d01f22cc | -22.90686 | -49.6913 | 2025-04-11 03:53:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 90c9e406-841a-3b81-ba61-1f1bb14f9048 | -23.98673 | -48.9171 | 2025-04-11 03:53:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82311e76-f62c-33d3-864e-7ea55f9df65b | -6.43701 | -41.23402 | 2025-04-11 04:10:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 55026eb4-3f97-3a33-9fac-377f10c0354b | -5.26839 | -44.7515 | 2025-04-11 04:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef50722e-c2e0-3adf-ac8b-09d007436a88 | -4.87286 | -47.40939 | 2025-04-11 04:10:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bedcec43-a3e6-3bdb-93c4-759b34fea22e | -5.26613 | -44.74789 | 2025-04-11 04:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2482d490-61db-3792-9fa7-fe4c13ea8f25 | -5.93499 | -44.35861 | 2025-04-11 04:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ec3d7c3-6850-3811-8002-6e47865bca1e | -5.269 | -44.74776 | 2025-04-11 04:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8238ffa5-dd90-355e-8da9-16df3c5a4a21 | -5.47009 | -44.69936 | 2025-04-11 04:10:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b5068970-6ebf-34cf-8ecd-af5644b39cc5 | -6.8405 | -42.78383 | 2025-04-11 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 59effaf1-4fd9-349d-95fd-9f1bf4bb5818 | -6.59064 | -44.77613 | 2025-04-11 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c96a4c1-3b49-3ec1-a38f-c4f814a653fe | -10.98481 | -44.43908 | 2025-04-11 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87ed2871-0707-3dcc-a426-e100466817ae | -6.66024 | -47.59179 | 2025-04-11 04:12:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 302b1e84-6b73-3b3e-81be-e70bfc0f668c | -11.56817 | -47.62236 | 2025-04-11 04:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 415ed430-130b-3631-8a93-743d87fc259c | -8.1123 | -43.11978 | 2025-04-11 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 130222b9-e74b-3be1-ace7-a4a8c3851891 | -6.37185 | -43.68535 | 2025-04-11 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a873acd5-2221-341c-8165-55f9b6f59c34 | -7.06319 | -44.38294 | 2025-04-11 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 637e6386-02a6-3e08-b894-54592ac590b7 | -7.32549 | -43.13354 | 2025-04-11 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6e881f9e-e7dd-3be7-94dc-0b1be6bc9aa5 | -11.57475 | -47.62798 | 2025-04-11 04:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a873d5df-d8ac-38f1-8f78-9033cdb6e95a | -11.57109 | -47.62733 | 2025-04-11 04:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe843ec1-52c2-37b2-a045-664f3f549f21 | -7.24969 | -44.77889 | 2025-04-11 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13178544-97f8-3b05-9897-c8ad201438b4 | -10.98262 | -44.43152 | 2025-04-11 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f911dae-d3f3-331c-9373-25d67bbf5740 | -6.83719 | -42.78331 | 2025-04-11 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a0b7599a-e8c4-30df-9cb6-ff2b24f90c73 | -11.57401 | -47.63234 | 2025-04-11 04:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 286c9f9c-1139-3d11-8a60-abefd1cb5d0d | -6.37517 | -43.68588 | 2025-04-11 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8ace690-4875-3f0b-b23b-4f4e62d89369 | -10.9815 | -44.43854 | 2025-04-11 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55c060a0-9db1-3635-8714-eab7a2ae1ed5 | -11.90183 | -37.64073 | 2025-04-11 04:12:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e7b0fa51-a819-3c29-b359-eeafdaff99b3 | -6.6633 | -47.59747 | 2025-04-11 04:12:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ccb1db6-5e34-34b1-8549-dfe5c2845661 | -11.74786 | -41.13826 | 2025-04-11 04:12:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6c6d24ed-aed7-3461-bd03-82de1bcdcca4 | -6.65939 | -47.5968 | 2025-04-11 04:12:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d02ff16e-a3e2-36e3-a28b-08286e06cdab | -10.98105 | -38.2728 | 2025-04-11 04:12:00 | NOAA-20 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a301b914-17fd-3f2c-841c-a4c0d42b3786 | -10.98318 | -44.42801 | 2025-04-11 04:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1290be0-f689-395a-8ad7-f630fe10247c | -6.59404 | -44.77671 | 2025-04-11 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d3b8f9c-6e41-33cd-a3df-4a2fdc7f8e80 | -11.57326 | -47.63672 | 2025-04-11 04:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f45a4c18-eeef-3e54-9f10-7867c6f7e738 | -11.75082 | -41.14299 | 2025-04-11 04:12:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 368ef941-abe8-3396-a225-48ebcdab59f3 | -11.75439 | -41.14357 | 2025-04-11 04:12:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4f3709c-e964-3bfe-a918-0d4e5c950fef | -11.755 | -41.13943 | 2025-04-11 04:12:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07c1c13c-91b8-3560-b1a1-b09af7f9fcbd | -6.66245 | -47.6025 | 2025-04-11 04:12:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d35cda6-6313-3b5d-9e32-10c33c233744 | -6.3713 | -43.68884 | 2025-04-11 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96d9e985-3aa5-3ebd-9ab5-0b71773b4414 | -6.96633 | -42.80365 | 2025-04-11 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c74a2e7b-e4f7-3f7e-a45a-ee41db842192 | -7.24571 | -44.78199 | 2025-04-11 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81115785-fec0-3389-8533-8ae8e7c0c101 | -15.07872 | -48.9454 | 2025-04-11 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d21537b1-f3fa-3860-870c-6568ce0ad96e | -15.24958 | -47.45768 | 2025-04-11 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49dc2465-e0c0-3b11-992d-481628f1c8a2 | -15.2461 | -47.45706 | 2025-04-11 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b993318-065d-356a-980d-acf4e8686327 | -13.04592 | -53.71277 | 2025-04-11 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 658f42b5-1a9b-3315-a476-d4e6af6c11d0 | -19.41944 | -48.99446 | 2025-04-11 04:14:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15a1f085-0d18-316b-baca-1ae68cdb5b09 | -14.47705 | -50.28521 | 2025-04-11 04:14:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 251528d6-2755-315b-88fe-376ebdade47f | -13.04428 | -53.71593 | 2025-04-11 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 658d004e-2a79-3d03-b2fa-67275934ee98 | -15.80676 | -43.56674 | 2025-04-11 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d344b15f-e929-3f36-b337-80a5800e6b9a | -16.88321 | -43.91951 | 2025-04-11 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75339f41-4afe-3dd1-b214-8327d1b3a5b3 | -13.04557 | -53.70941 | 2025-04-11 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa289472-8a36-338c-a624-e295c4a95f1b | -17.31216 | -44.92761 | 2025-04-11 04:14:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2eed9595-6805-3438-a9bc-8c4e5fb44de6 | -13.17673 | -54.11253 | 2025-04-11 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfbd28da-a13d-3cb2-b0cc-3bbcb2c4a0dc | -13.04654 | -53.70952 | 2025-04-11 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29c24ed2-d726-30bf-9491-5ec58dbb41e9 | -15.80337 | -43.56619 | 2025-04-11 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbdc7de3-012c-340b-b4d5-88c3353bdc3f | -13.04951 | -53.71712 | 2025-04-11 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8718f17d-6f4a-345e-a300-e30cb2621067 | -13.04493 | -53.71265 | 2025-04-11 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 837a5990-9548-3ae0-9a46-f8365eca2489 | -15.83825 | -49.66977 | 2025-04-11 04:14:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 774600f1-38c7-3dca-b5aa-65617c389ef4 | -13.0453 | -53.71606 | 2025-04-11 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35e712d0-f102-399e-b075-eac47d486754 | -17.09304 | -43.80527 | 2025-04-11 04:14:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15208939-f58e-3e9b-89d0-a6850fd0899c | -18.68848 | -48.51826 | 2025-04-11 04:14:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8758032a-5fe6-37bd-b137-3622f3976f23 | -17.75962 | -56.30901 | 2025-04-11 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7a0f9431-9c19-34e0-9403-ee781712d367 | -17.75397 | -56.30766 | 2025-04-11 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bf395413-2a10-365e-9ad6-8b7054ef1f46 | -13.48354 | -43.70253 | 2025-04-11 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 532ba010-556c-3330-bcff-7c6818a4919a | -19.49744 | -44.80628 | 2025-04-11 04:14:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b47fc88-12a3-301a-8609-f503c65f5589 | -15.24892 | -47.46165 | 2025-04-11 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README3.md)
