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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cdac332-100b-3285-8fd3-97453379354d | -11.79087 | -43.5597 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8807d2ca-e7eb-3bd7-8f12-6b4d90c7c52e | -11.7267 | -43.44033 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3977d882-2164-3b3d-bc42-631140298233 | -17.44441 | -41.91931 | 2026-10-02 03:19:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3988378d-5500-32ee-ba90-491638a0bf64 | -11.41676 | -43.51715 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dbd56ff7-5151-3800-b70f-24c06999c827 | -11.73464 | -43.43562 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea27f6da-b3d2-3843-bafc-4f51b80927aa | -11.2634 | -43.57043 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af3d551f-35fe-345d-bb54-f0746e64fecb | -12.52142 | -43.1043 | 2026-10-02 03:19:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2484fc22-adfa-3045-aac3-61bcd9eb2370 | -12.85706 | -43.81113 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 20603f05-96ca-3fa7-a70e-3ff5902c1aa1 | -11.74916 | -43.44589 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0481d56-c9bb-37ca-bf65-ddabacf62916 | -11.68733 | -43.59889 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6a36f0d-a4bf-3d65-9795-d9935c1c0010 | -11.72488 | -43.42835 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 198c02ae-e3c4-3e55-b354-01470a795ec6 | -11.46696 | -43.41905 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7c08e68f-2d0b-3662-91b7-b17fe4af9621 | -11.74244 | -43.44459 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce7a0597-0325-3a87-83f4-cf71b4ee8ba3 | -11.43465 | -43.40586 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e0138852-5563-3c26-b4f6-882e675ed13e | -11.74011 | -43.44311 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1504272-39e5-386f-bab3-94dc6a144da4 | -13.54435 | -40.07671 | 2026-10-02 03:19:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8c0354d7-da26-3621-b57e-71c82493ec44 | -11.42119 | -43.40317 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41a02056-e717-3447-9ce9-9f6052f08d5f | -12.52916 | -43.09954 | 2026-10-02 03:19:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d4a39482-bc9d-318a-8563-73a132ec6938 | -11.71967 | -43.5093 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1afa3461-eb6d-3f56-9df7-46c8f017c986 | -12.53693 | -43.09377 | 2026-10-02 03:19:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 53677b12-fd17-33aa-b1e0-76ac573818f2 | -11.7585 | -43.56948 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 22d87b4d-7618-3324-8558-7ce5b3f636ae | -11.6633 | -43.61277 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 169348b7-954e-3301-a38a-24ffbeb6ced8 | -11.74682 | -43.44444 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 952416ce-5ace-3366-8367-3e22039e8460 | -14.04311 | -43.84676 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7e1185a-fbe1-3aa0-adf6-7014831178d5 | -11.79416 | -43.56712 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3f726896-60fe-3993-b6dd-43d35f59b7db | -17.43885 | -41.91822 | 2026-10-02 03:19:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e980dae6-382a-3c62-ac22-4aded217feab | -11.68187 | -43.59876 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 98599099-cd40-3ce4-9fb9-fcbe07a9ffad | -16.86064 | -40.57663 | 2026-10-02 03:19:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 92996bbc-308e-3449-b387-465d4db8ac88 | -11.41552 | -43.52335 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 443506b0-bccc-3fb3-9775-868b34e836dc | -11.73216 | -43.44785 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3587f199-3e34-3e86-9727-45cb037f311a | -11.64631 | -43.55841 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 98acdc02-3f53-3bf9-869f-0a5a146b34c3 | -11.68063 | -43.60461 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9842a012-1e54-3aca-bf63-b9df1c6f5e19 | -12.52926 | -43.09804 | 2026-10-02 03:19:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bdeb2c9e-8a9c-3828-b958-88d6dad61416 | -11.66456 | -43.61376 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 4753e9e5-eec5-3f37-97a0-8076920760d6 | -11.79158 | -43.57967 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5e1cac2f-9e6a-3cf0-b879-b6be8e7c5dde | -11.71454 | -43.43145 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95c09769-bf31-37e6-a1ba-05b8d4631672 | -17.30595 | -42.32466 | 2026-10-02 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| af6cd78b-422b-3d25-a78d-2792ecf27ddc | -11.7236 | -43.43443 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df50d55c-19a2-3328-b255-062c0d7c3983 | -13.14071 | -40.8756 | 2026-10-02 03:19:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d5381aa2-4edf-3824-94bb-aafc8bad5fed | -11.66696 | -43.59498 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| a62f4b87-a8c1-326f-89f0-fb8d82457af7 | -11.74372 | -43.57286 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 9aa4c68b-78a5-3c88-b250-84a5595f7e53 | -11.75734 | -43.57511 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 341172e2-0fb5-3b8f-aa8c-7b7210c8f179 | -11.46317 | -43.43747 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d472fec3-98f9-3d1a-839a-6cb64bef7df9 | -11.67954 | -43.60978 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0e881d99-a7a2-32f5-bd67-5d673aacb201 | -11.77455 | -43.55993 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d551bf5-875e-3b7b-a904-27c5576921c6 | -16.85935 | -40.57499 | 2026-10-02 03:19:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fea9086e-eb61-30d4-a59b-2d68a340856e | -11.70137 | -43.50657 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab638905-17b1-3dde-b080-84ac0db754ab | -13.34214 | -43.85318 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9848e8c9-081c-3956-b08a-a76fca2abf10 | -11.70353 | -43.59646 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5919e8a5-8dce-376f-bf6b-3b5d8d10f283 | -11.47116 | -43.43272 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4b7ce6ed-8aa5-387e-8044-4ed18e46f995 | -11.77683 | -43.58296 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 1c590af5-8478-317e-9fbd-1161194d514a | -11.70214 | -43.59543 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5692a904-ba56-3d69-84ac-b45353fb5cd6 | -13.86659 | -43.63905 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6b63d3f5-dd18-3aac-b318-9cfcaea6436e | -11.42792 | -43.40453 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9d360fc8-bbfe-3f03-80cd-e30729e6c2d9 | -11.70479 | -43.59048 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e600bb1a-afb0-30a2-8a00-ef47e3fc0ae4 | -15.39734 | -43.00297 | 2026-10-02 03:19:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cc7305a6-b549-3773-8a7f-b9ad5e4a31c4 | -11.67931 | -43.60357 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8b54a73-48cd-35eb-936e-eda055e48a21 | -11.70008 | -43.51269 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a97886b4-55c1-3729-930e-3bcb70a7fd4e | -15.49917 | -41.55465 | 2026-10-02 03:19:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 86d1f8ec-8918-3083-8e68-9dc18be7aea1 | -16.85868 | -40.57836 | 2026-10-02 03:19:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 409d83f8-c43f-3a43-ba17-9468f453b513 | -11.66451 | -43.60693 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 342.6 |
| 1bbbb47e-35bc-3f72-bfd4-a25646ea52ac | -11.75587 | -43.44723 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53921aba-f720-36de-8266-1e251f15130d | -16.99659 | -41.1827 | 2026-10-02 03:19:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4aaf3f57-0d5a-39d4-941d-360982e19bec | -13.33733 | -43.85699 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 164faa6f-6113-392a-85f6-832b83db8601 | -16.11889 | -42.22549 | 2026-10-02 03:19:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e75ba98c-b4a3-380b-bdc3-c2f25d059117 | -11.69822 | -43.51126 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8c308964-9874-368d-bc66-2b3f4a45154f | -11.26677 | -43.519 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81f4983c-f4b4-3176-8019-0a5f669240ff | -11.77007 | -43.5816 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 70f69aab-5c94-3269-adad-3cbda5dcea1a | -13.48927 | -42.50466 | 2026-10-02 03:19:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fc4f9713-f200-35ce-a353-b19e71130c92 | -13.33594 | -43.86336 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 324dce09-3498-3cc2-a7c0-db5f3d5b3b39 | -11.72124 | -43.43283 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 86ac4888-5372-334f-8f4d-b4fa5bacdc61 | -11.6658 | -43.6079 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 9e681557-7852-37e4-b382-1e3c74db689e | -16.99587 | -41.1862 | 2026-10-02 03:19:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d852caaa-affb-3943-90fb-e8d6889d86b1 | -15.61335 | -42.3963 | 2026-10-02 03:19:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f411f6cb-e555-3f3c-a927-f3129423d24e | -11.68869 | -43.59988 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b60b6af4-d903-3257-9223-3e6c503f12bd | -11.7505 | -43.57414 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 26d78b37-ad12-3da5-aa37-4efd46d0b078 | -11.4699 | -43.43885 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f2133eb0-0f3c-3b3e-8f28-333d0b9aa1ce | -11.27147 | -43.56558 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 014cf588-63ca-3fc4-b916-5c5d54cc90a0 | -11.68053 | -43.59765 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 45bed05a-5597-3a3f-a9a2-d25b65fa9706 | -17.22116 | -41.20391 | 2026-10-02 03:19:00 | NOAA-21 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6f17206e-9077-373c-8eca-8aecc4a265a6 | -11.72903 | -43.44186 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9280e056-37c0-37bf-bd59-11c215a24ff2 | -11.46443 | -43.43135 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 45cd3eb3-1abf-3b8d-93f1-186d7642d106 | -11.79303 | -43.57259 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bd1cb4f1-751b-3a66-ad66-6ac47f6db86d | -11.7169 | -43.43306 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b5a6cf5-f9c2-3efe-b707-38e060ba4ca8 | -11.68636 | -43.61093 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 89cc3c25-aadf-37b8-a6f2-3625f4e59096 | -11.46026 | -43.41758 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2389280b-7644-3d32-9464-4aef73cac73c | -11.69674 | -43.59521 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67c9fbb4-f50c-3f58-a4c2-cc74ded5d721 | -11.78819 | -43.56195 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f2149062-268e-3c13-b6ba-47b9e7263a78 | -11.41709 | -43.52414 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6578b0d2-c028-3124-b6a3-4e0249bf1e64 | -13.86006 | -43.63757 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b9741483-0ec0-3bc5-9aa0-5d94e5630f12 | -11.74116 | -43.45072 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a73d80d-7597-3719-847e-586850d3d086 | -13.85832 | -43.63858 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 97bb31f5-3f64-3f87-bc40-dc34d0e82c1c | -11.80221 | -43.57261 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 143ac7ac-82f2-350c-9421-0ce91f0de0d6 | -11.73158 | -43.42974 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 98d9b14a-0990-3685-8218-34ce047dc542 | -11.47243 | -43.42657 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b51e5612-1c81-3a0e-be27-b682c116f0eb | -11.77333 | -43.56581 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a5009927-8a34-37e9-b1a9-112486e9a7b2 | -11.65213 | -43.59847 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1571caa5-119e-30c0-8ef9-af6fc78a6311 | -11.65471 | -43.58599 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ebb932b-113b-323b-a748-b53594dfb57c | -11.78134 | -43.5611 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5a6c9ad-a973-3746-98d1-ecae57ddb6ea | -14.04183 | -43.85264 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README24.md)
