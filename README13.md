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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| faa4b94f-e056-3571-b680-75b9087bf139 | -9.01441 | -40.99883 | 2026-08-28 03:30:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8881e213-997e-3965-9617-d862b493efc8 | -11.0095 | -45.07553 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a61b1e36-13e2-3b15-99f0-1a9b2a86f4ad | -11.40188 | -45.14667 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e0baeb4-cd67-3917-8300-34dbb29ef3b3 | -12.23226 | -41.89905 | 2026-08-28 03:30:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 95ccfec9-d23c-35c0-9c87-3dfa00aae1db | -11.01688 | -45.0711 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 77734f1a-89b2-3eaa-968c-0adb6f023c6a | -6.89992 | -43.64763 | 2026-08-28 03:30:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 870c8423-6ca7-31de-8b3e-f384653dc029 | -7.2019 | -42.74223 | 2026-08-28 03:30:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e930b98f-c6e0-39f9-8950-980d4c946412 | -9.01474 | -40.99963 | 2026-08-28 03:30:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 5046f658-58b5-3b74-a0a4-d9cab7b4f542 | -11.49444 | -45.1146 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b5c4d63-cab8-302e-a043-4a49650130e4 | -11.48754 | -45.11381 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe2a3cad-8193-3960-9f64-d3eee253e5d7 | -11.48855 | -45.07498 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9725e3b-878e-31b5-bc07-f731113ec2f1 | -11.57315 | -45.52453 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9fc17109-8a48-3418-bbcd-e76009089ce5 | -11.56224 | -45.50789 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| fed7e8ef-4c84-3c6c-8db8-fd9a2170a005 | -10.52924 | -43.98696 | 2026-08-28 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9b156d6-8f59-35e8-bc9d-32f61a644011 | -11.56888 | -45.55124 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 30bc048b-c2a7-3aaa-a762-eb18f39cf5a2 | -11.57851 | -45.53954 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8467cc7a-18c2-3ab6-b1de-1e3239a0777a | -8.70355 | -44.25656 | 2026-08-28 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a73b7a8f-0372-307e-aa33-b2786a6512bd | -11.01626 | -45.0772 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87620338-b1e8-3beb-8a0f-9ad164c3e023 | -11.40327 | -45.13991 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 86922979-ad6d-34d2-b4c3-c207ca2f12dd | -11.56901 | -45.50999 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 65608838-7486-3f09-b37b-7a75a66d86e5 | -11.48975 | -45.06921 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34128da2-2740-39f1-aeb5-7d54a1e171e2 | -11.40419 | -45.14015 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fab13c8-458c-31b7-b247-8586639b88df | -8.28756 | -39.97305 | 2026-08-28 03:30:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 41472c05-2523-39ea-bf23-5091df88e552 | -9.00924 | -40.99853 | 2026-08-28 03:30:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3298a6e7-b142-3c85-849c-260776313d4d | -11.37326 | -45.14801 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cdf44c9d-e134-3fd4-b598-04eb4c8f2fb0 | -11.57293 | -45.53157 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 163a1e2d-82f6-3313-a831-a523ab647df7 | -11.569 | -45.54408 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8ef96d84-21f5-3c27-b7cd-0481b3d9c39f | -7.19996 | -42.74062 | 2026-08-28 03:30:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0dfa6612-eb93-370d-8137-06df1204a46e | -11.57731 | -45.53898 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| b1758658-b188-3438-8e8f-16163550d751 | -7.07115 | -43.61508 | 2026-08-28 03:30:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2db4f50d-7a8c-34ee-b233-fff0543d77f7 | -11.57715 | -45.54617 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fb459f8-90ae-3b44-8448-8ec73eaa475d | -6.89662 | -43.64308 | 2026-08-28 03:30:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18a4ffc7-b6bb-398d-aa0c-ca0361c7cf86 | -6.90221 | -43.6502 | 2026-08-28 03:30:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcca7140-1c4a-3648-b21a-ba4cd7d10700 | -11.57005 | -45.51049 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8a2a5ecd-aaf7-3e48-9cb2-ef18cfeecd29 | -7.44188 | -41.49126 | 2026-08-28 03:30:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c516dfac-fd98-30fd-b2ef-9d71c9486827 | -11.01751 | -45.07121 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8dc37887-4d96-3311-b941-ef51a5c26383 | -11.57869 | -45.53246 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| ebbadb6d-58f8-3adf-a8c4-ca45fa2b4aa3 | -11.57024 | -45.54466 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1f5bb8f8-70ac-389f-b3ff-d34f734a3e93 | -9.00891 | -40.99775 | 2026-08-28 03:30:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0f23a624-0f6e-33e2-801e-ba659d14c8c7 | -11.56456 | -45.5021 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7efcdc3f-03d8-3f4f-bcd7-73522ae4a0c4 | -11.56471 | -45.5364 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| e94bbb54-a69e-30aa-bcdf-0994cdaf069a | -9.0154 | -40.99598 | 2026-08-28 03:30:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 2cdceb57-4fd4-3c10-b029-a5f3a09a4443 | -11.57451 | -45.51809 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 1b3afd41-d0cf-3df8-9b3b-337c952930d8 | -11.00891 | -45.07539 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8ba9047-7a08-3538-8ea1-d16815b2a545 | -11.57176 | -45.53106 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c9bbba36-55ce-311c-9b3c-26222f94b6d8 | -10.53034 | -43.98146 | 2026-08-28 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61ed29df-9a84-3426-9a9a-603ba317bed9 | -9.00991 | -40.99489 | 2026-08-28 03:30:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 69a55b1c-c4a9-3f23-8890-4f3484b8ee63 | -11.5649 | -45.49541 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5d6fff8a-504d-3014-8226-ecf14ab2132a | -11.48622 | -45.12022 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc3fb882-8ffd-3a3b-bca2-64ec71e8c0dd | -9.0151 | -40.99519 | 2026-08-28 03:30:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ac82a539-bb20-38d8-bfa2-0e816ffeea18 | -11.57591 | -45.54559 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ece33579-9a1f-3a98-8a07-6156e35f9fdc | -7.19561 | -42.74086 | 2026-08-28 03:30:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ebd093f7-8280-35bf-8f96-ec523fc6084d | -11.56876 | -45.51676 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 87325b4d-4f13-3bbc-b622-40c1bb83ce20 | -10.09967 | -40.918 | 2026-08-28 03:30:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c20f0602-2f25-3446-96c7-7755bec02193 | -11.56761 | -45.55064 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9dbc603e-445c-377e-b2fb-fcc45113d65b | -11.39741 | -45.13868 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6cf0ab6c-b9d7-3603-867c-b9f09261f3af | -11.56327 | -45.50836 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c8e32042-a9c6-3445-b71d-2b1937e66099 | -11.39649 | -45.13843 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eaf1d8d-a363-3c36-8822-e3a979732cf0 | -11.56193 | -45.51484 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a2785b9a-35c4-31e1-92e1-d34cffeb3fe5 | -11.01567 | -45.0771 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 43c33d30-cb81-3500-8df4-1eab36400f22 | -11.48732 | -45.08089 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a8e4702-01b9-3c55-b298-65c05a801621 | -11.57159 | -45.5381 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 496f8ea5-192a-3a20-96bf-41f8f92b1432 | -11.56631 | -45.52273 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 244ede6f-a6da-3e4e-ad8e-1af973135034 | -11.56359 | -45.50155 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 598069de-daa3-3b54-8725-1c4ba3c32bd9 | -11.57038 | -45.53756 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 4a860ee5-a6c9-30ad-9b81-bb9326693240 | -10.0975 | -40.91785 | 2026-08-28 03:30:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5deef3d8-5a60-34f0-924b-db8e426707be | -9.0096 | -40.99412 | 2026-08-28 03:30:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fda1aa4b-88cd-393f-a820-2e9c8b6d65a5 | -7.01616 | -42.11664 | 2026-08-28 03:30:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2d477de3-9fd3-32d8-86d9-068e4c7c1f95 | -11.56769 | -45.51624 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 0f808f34-7e8b-3253-8d36-77677574da75 | -11.56606 | -45.52984 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a85436a3-7f51-31fe-8caa-df550c7110f8 | -8.64126 | -38.1506 | 2026-08-28 03:30:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2b90fff1-f32b-37ee-8387-306ad998c862 | -11.56741 | -45.52327 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 29747af8-fddb-354e-a13a-21d0b2526137 | -11.01076 | -45.06956 | 2026-08-28 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5adbad09-3a00-324e-bcdb-edb773771ca8 | -11.56491 | -45.52929 | 2026-08-28 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c1d3a70b-5d03-3908-9c66-a9c4f9d2defc | -15.37709 | -39.48308 | 2026-08-28 03:32:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 23859e0e-5e6d-325b-aa88-4748e6f98437 | -12.50294 | -43.8105 | 2026-08-28 03:32:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 51c58ffb-84a2-3e22-ae8c-dfb9f6117f80 | -14.90922 | -43.4127 | 2026-08-28 03:32:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 030cf50a-759c-3b32-9543-3828c745b780 | -12.77625 | -46.44847 | 2026-08-28 03:32:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef2f94b5-7b88-3d1b-aabd-9c83fc3a4007 | -12.42624 | -43.41066 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7df7a2ab-cc44-35c5-8603-77341b76e3f6 | -15.52701 | -41.93247 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 20fcbe89-ef28-3cbb-bb0d-c8d180b0b41b | -14.07594 | -44.0648 | 2026-08-28 03:32:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25d9e215-9017-383c-a28d-5d7b9e11d1ba | -13.5951 | -45.78414 | 2026-08-28 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c921c6d4-0693-3216-aab0-dd37e20a2761 | -12.7668 | -44.27111 | 2026-08-28 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e70b5213-269e-3ebb-b719-45a17c799ece | -15.5218 | -41.93139 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43cda588-fff5-3f8a-a65d-082a3d68fcd1 | -13.60871 | -45.78686 | 2026-08-28 03:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aae662d9-d72d-35c7-b753-39845d2cef89 | -12.42571 | -43.40852 | 2026-08-28 03:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| cb7e57d8-1832-3068-9971-4d96fa49d729 | -12.76497 | -44.26757 | 2026-08-28 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3322bf52-57ae-3dbe-a818-57a25ada2f44 | -15.58062 | -41.77692 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fb2b331c-6d2d-3a00-896c-728c06909c45 | -12.7576 | -44.27139 | 2026-08-28 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 990e23e2-4203-3dca-93ee-1e55bb096859 | -12.7639 | -44.2728 | 2026-08-28 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6e2b5d3-f2c2-308d-b8d2-520efeda404a | -17.53624 | -42.47451 | 2026-08-28 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| baa1cd11-fc4a-3b38-aa1c-8a2c109e2970 | -12.78091 | -46.44818 | 2026-08-28 03:32:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 128999dd-3584-3317-8766-62eb642b66b6 | -12.75868 | -44.26616 | 2026-08-28 03:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f79bd041-3773-3897-9cdc-e6fc4a0fec11 | -14.1156 | -44.39075 | 2026-08-28 03:32:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88d15a81-928c-3ce3-9e3c-8cb0b93dec0f | -12.78329 | -46.45043 | 2026-08-28 03:32:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 905b4487-e48e-39ea-aadb-677ced18be39 | -14.90839 | -43.4164 | 2026-08-28 03:32:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0baa913d-02b0-37ab-a830-9c65fc5597af | -15.52834 | -41.92573 | 2026-08-28 03:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| a7ba0299-433d-3459-b0f8-bac6aa8c9d3a | -17.78989 | -39.70728 | 2026-08-28 03:32:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0f43c6b1-f03d-32da-918b-6314f20e06a6 | -15.14288 | -43.79593 | 2026-08-28 03:32:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 682eefac-f09f-37ec-99b5-af160c11debe | -12.50912 | -43.81179 | 2026-08-28 03:32:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README14.md)
