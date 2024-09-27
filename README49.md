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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14ddfbb1-c835-39c8-bffe-7d7eb831d071 | -11.66118 | -44.52429 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45672fb5-438d-3f87-be5a-316d26961593 | -11.6608 | -44.51182 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39667731-206a-3ce4-81d7-93a6846e8f6b | -11.6584 | -44.52539 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56ef4a17-4d5c-3fef-ae6b-8307d9432d3a | -11.65672 | -44.52347 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5afefa84-2898-317d-93bd-c6c25aac5f19 | -11.65588 | -44.52798 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6903c104-2353-3c2a-9683-5e161665aff3 | -11.65554 | -44.5155 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 421840de-f712-368d-a80b-b83ad69f711e | -11.65474 | -44.52002 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16eca0d1-31d6-35e6-97d3-f3477ddcda4c | -11.65394 | -44.52455 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8b700dc-fd3e-3b7f-be36-18fee19320e3 | -11.65393 | -44.5136 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51a079ff-dfcf-33aa-b09e-6c5a4e8aad29 | -11.65309 | -44.51812 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 465e1ff6-e62a-3fff-8400-1ce584692c89 | -11.65028 | -44.51917 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fd438ab-b29f-3258-b677-a3e615b68245 | -11.64948 | -44.52369 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d8132c8-15cc-3cb6-8051-6c75be301496 | -11.64501 | -44.52285 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bff9eca-2da5-3178-ac78-09badee91926 | -11.63609 | -44.52117 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 66fa0dc9-3383-375b-ba00-c0cf0d56caaf | -13.44314 | -43.77537 | 2024-09-27 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dddb2987-0a98-3318-ad4f-71a64eb7fa89 | -13.44245 | -43.77917 | 2024-09-27 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa0cd5aa-417b-3880-bfee-62ac342f0dae | -13.43705 | -44.02268 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0161044-a577-370a-ba6f-a0c76cdf4d28 | -13.43286 | -44.02192 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 84f59345-d08f-370b-9ca8-b0bd671073ec | -13.43215 | -44.02586 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 799035b1-7aae-35a8-9dbc-fedbe1a050f2 | -13.42867 | -44.02114 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1b8e38f7-7302-399f-9538-263ef173e9d4 | -14.79452 | -44.17193 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0540b941-a262-3c6e-a80d-1070622ce0c6 | -14.79382 | -44.17575 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 344a36c3-207a-347d-9a3c-ef220cedfac6 | -14.79039 | -44.17116 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2394f75-f9f5-343a-ba62-1a9e59d30fd8 | -14.78968 | -44.17502 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d6bc2fc-23b3-3fc2-bbaf-fd59a8faee85 | -14.71939 | -45.50786 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fbbb376-6c52-399e-8344-dda2a3e835d5 | -12.25119 | -45.48982 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d146635-2b37-3846-aefb-d1f560990919 | -12.24944 | -45.49317 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4010a42-49d1-3dc1-8865-bac0366c422d | -12.24648 | -45.48892 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32ee3230-5e94-322e-af11-3d89f84c9c42 | -12.24551 | -45.49403 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5c1ea317-7228-3619-a6d6-7bae4db5656a | -12.24473 | -45.49226 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2de36def-3791-32cc-8650-d9f5f15de405 | -12.2438 | -45.49741 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f9d228ce-1942-3732-87fb-0ff9a9380aae | -12.24079 | -45.49319 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c1e2b44c-3a54-3399-a14c-48110ffd2e8c | -12.24001 | -45.49141 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e40f0d7e-eb01-3257-9700-9b2d2d5599fb | -12.23982 | -45.49831 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 60d9eea7-277b-3a73-bdf8-c6202f2298f2 | -12.23908 | -45.49655 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 22d1ddaf-8a2b-33ca-b9aa-5324456297c0 | -12.23607 | -45.49235 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94d2bc7f-702d-3dec-8434-48a7ad312719 | -12.23529 | -45.49057 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db7f054b-d3c6-334b-ab38-845a258b2277 | -12.23135 | -45.4915 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 280085d9-1a1a-328d-849f-4c9658e1d7f9 | -12.23056 | -45.48972 | 2024-09-27 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cb7bf10-8df1-31e3-a1d1-3a6975fcb10a | -11.27711 | -46.13177 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b1f82766-d769-328e-bc6a-4a00a619fb6c | -11.27324 | -46.12479 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4fe6ce12-34f1-36e6-9987-389cd855ad1e | -11.27262 | -46.12811 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e3be3cbf-5a83-3f9a-b5fd-401cfb4e5dca | -11.27201 | -46.13131 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1f8cd097-c184-328c-a250-5d292b3e85cb | -11.26883 | -46.12075 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7de5a644-8080-3a54-bf37-44d674e1bbee | -11.2682 | -46.12407 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d9e247ea-dac7-307b-a220-00d65dc0b970 | -11.26697 | -46.13057 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9aa93792-e0b3-35e3-ab9f-61881040e92c | -11.26641 | -46.13353 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fd71d331-0e0a-3dea-8f5c-67b2594621e2 | -11.26318 | -46.12326 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 2048e66e-4cfd-334d-8f18-c94fcb0559dd | -11.25319 | -46.12392 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e60379a0-b27a-3346-a220-66f79fc025da | -11.25311 | -46.12169 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffa6f15d-e351-3b89-b013-12085abf7c0c | -11.25254 | -46.1247 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b786d0b-a632-316e-bdd7-cc2c40386d9b | -11.24935 | -46.11662 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 763970aa-7fc4-3aaf-9753-ca41f7bfdef7 | -11.24877 | -46.11981 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f652f20f-c14f-3cb5-9e0a-ca5b07729698 | -11.24821 | -46.12284 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 869a205c-dfa6-354c-acb8-6e2a29f4d369 | -11.24137 | -45.50931 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a285051-3aba-37a9-b922-cb4803bacb95 | -11.19291 | -45.5566 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 85c055b9-992b-34cb-8173-2615c6af8618 | -11.18907 | -45.55037 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c98fc992-3e4d-3ccc-8975-6d944f3bb1a3 | -11.1878 | -46.03078 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c5390832-49bc-3adb-8f2d-13874dc7f01e | -11.18668 | -46.03677 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d4145171-1d02-3374-a938-eb139f5f56b0 | -11.18236 | -46.005 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8122980c-d074-3783-9a84-8a5b3935922e | -11.18121 | -46.01108 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34c87311-108a-3a30-a874-b1d29cd3ec0d | -11.14654 | -45.5377 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6919b4e9-0079-37dd-957c-4cddcb1ad9af | -11.14354 | -45.55368 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b26ee8e-1599-3b9a-a164-9b012c220fea | -11.14273 | -45.53141 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1180a6ef-ac04-380f-be0f-7925442ced64 | -11.14255 | -45.55894 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8b9349e-55e2-36dc-b8ad-bbc3d7c876c3 | -11.14173 | -45.53674 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb447427-4eda-3d4b-8a9f-8ffa09d01b91 | -11.13873 | -45.55268 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 911725b4-ffe9-3131-8ae5-476a51c2f7cf | -13.28795 | -46.31929 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25e427a0-b8bc-3cb5-87cd-c0928e17ab0b | -13.28503 | -46.32303 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 00e12b8a-ac13-3e3d-9644-5e3cbde88f1b | -13.28396 | -46.32883 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d74c76a8-9725-31fe-8be1-997edf36caba | -13.28186 | -46.32457 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b848293b-cd12-3ff8-9fde-6a5ff0e00862 | -13.2746 | -46.30972 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d318ecdc-a1ee-3555-987d-81f21602d208 | -13.27297 | -46.30614 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9554c8a4-e2b2-3e9b-bfde-b9b13701fcfe | -13.27162 | -46.3134 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3e8dcfda-333c-35d1-9b8e-537e2ca23e89 | -13.22776 | -45.6513 | 2024-09-27 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57ab6955-09f2-32f0-96c9-590f3edd9d22 | -13.22404 | -45.64533 | 2024-09-27 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4d74edb-ee74-30e5-b5e6-21e67e1cc1f9 | -13.22309 | -45.65035 | 2024-09-27 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e48a6e34-3f27-3584-876a-a5f891dd72e5 | -12.95541 | -45.39039 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6edc6f9c-db8c-3bd1-b4e4-1859914ba50a | -12.95451 | -45.39525 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b866711d-6999-3828-93c9-5b2528261cf6 | -12.72818 | -45.57449 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6598917b-5f0f-3832-b0a0-aea5d6b3d4e1 | -12.72443 | -45.56846 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 778c1977-c500-3a4c-8369-58e1bfea6c6f | -12.72069 | -45.56243 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0219643b-472d-3351-a2e2-5af444fc65f0 | -12.71974 | -45.56752 | 2024-09-27 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a7ab150-f534-37d6-877f-de83d6d67ff5 | -14.72758 | -45.51416 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84cf4ed8-0768-3df3-a224-3aef2d03d7a4 | -14.72671 | -45.51888 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 888dd1a3-68d7-35ed-8f05-99df38891d30 | -14.72392 | -45.50866 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e567d6e3-ac43-342c-9897-a633bff8d22c | -14.72305 | -45.51337 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b952adc-a5e4-33f9-85f2-b15008fcd286 | -14.71385 | -45.48737 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44aaee6c-56a8-3b72-9293-d116355e3c73 | -14.7121 | -45.49677 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51d32135-caa1-3c84-ba55-afe64bb2326a | -14.70935 | -45.48642 | 2024-09-27 03:47:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39caf8e4-4329-3547-bf4a-a373c9b6374b | -14.16913 | -46.43997 | 2024-09-27 03:47:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ee47875a-bf70-3813-963a-380986dfd9c2 | -12.18747 | -46.75497 | 2024-09-27 03:47:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b206801b-0da1-3d08-9eb3-09453feefb35 | -12.18233 | -46.75398 | 2024-09-27 03:47:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24f527f6-de60-33c1-8fc8-3da92592b761 | -11.33058 | -46.23528 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1400e54-844f-3145-baed-b07a64a29de1 | -11.33003 | -46.23826 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0a51337-ae5a-36f1-ba35-e0510a630c28 | -11.10828 | -46.18154 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e52bd8ef-7101-34db-9a9c-3e47bc4ed284 | -11.10776 | -46.18438 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07d6471e-0723-31df-8811-7d82faadbb54 | -11.10275 | -46.18327 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92123df8-ba24-3c92-8352-2e9eb08d1979 | -11.09152 | -46.15954 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74699a19-4600-3782-957b-d61c2cc51817 | -11.09098 | -46.16247 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README50.md)
