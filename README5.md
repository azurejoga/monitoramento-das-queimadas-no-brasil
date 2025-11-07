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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c35d2fae-424b-3ba4-957b-081c5f650c81 | -9.47277 | -36.02414 | 2025-11-07 03:36:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e87b2639-c43a-38c3-aa9e-847516c6fed2 | -5.77155 | -40.83829 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5aef8e84-4b71-347a-88c8-07553433fe57 | -5.26673 | -47.16792 | 2025-11-07 03:36:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc175dd4-f549-3843-b75f-c49ab3fe4df6 | -5.26402 | -47.16425 | 2025-11-07 03:36:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6d25a57-84ee-36c4-91d7-bcb6b365b7bb | -10.28218 | -36.35482 | 2025-11-07 03:36:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c7614854-e8b6-37ae-9079-d256cf1c61e0 | -5.43633 | -44.6642 | 2025-11-07 03:36:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b5a9929-5e92-3b8e-8472-99d0db0acadd | -5.76795 | -40.80178 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 8ff72a97-f759-37df-b057-069a39fde56f | -6.7007 | -39.97459 | 2025-11-07 03:36:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 571db222-33fb-3f6f-8521-1313ad1a3d8a | -5.76713 | -40.80671 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43eb2fe7-6d2b-30fb-a71c-78cecb997b5c | -10.27815 | -36.358 | 2025-11-07 03:36:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ad19290e-58a5-32d0-a842-623989581749 | -6.63038 | -39.50551 | 2025-11-07 03:36:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 727e3524-eb9f-3645-9061-f3633f3852a1 | -7.14274 | -40.46067 | 2025-11-07 03:36:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 986e0316-8c50-3c05-8d7c-6784a3503183 | -5.36605 | -44.73972 | 2025-11-07 03:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3cec5d7a-9eae-3b99-ba34-3173c7159660 | -6.21867 | -40.69445 | 2025-11-07 03:36:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c7431b9d-f916-3502-8714-ff51994ef30f | -7.43001 | -39.03865 | 2025-11-07 03:36:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 268d94e3-8311-318d-9932-3bdc5264b68e | -6.45906 | -44.45846 | 2025-11-07 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d117634c-5ed8-3691-a6e0-0731cf18a8eb | -5.43716 | -44.65944 | 2025-11-07 03:36:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b40ca36-d4da-3ab4-9cad-7c33481d330d | -7.38496 | -39.63518 | 2025-11-07 03:36:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| c50cda27-6412-30ec-bc8f-a28ff4ed9505 | -5.77226 | -40.84001 | 2025-11-07 03:36:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f3f7cd80-a119-3455-abd8-8f897e620276 | -7.38456 | -39.63456 | 2025-11-07 03:36:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| eb1a99a2-46a7-3cba-adee-438ed76231da | -7.38562 | -39.63121 | 2025-11-07 03:36:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 0fbf4525-bc65-3c76-9ee7-04f4856e94fc | -7.19416 | -39.91479 | 2025-11-07 03:36:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b70c18a2-de82-3b65-a6e2-263c5212c19d | -10.23897 | -39.59419 | 2025-11-07 03:36:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8721a846-9b59-33d6-951f-2c70f3955b56 | -6.89795 | -35.50138 | 2025-11-07 03:36:00 | NOAA-20 | CUITEGI | PARAÍBA | Brasil | 2505204 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f4bf8142-916b-3b93-9077-c89b4c26960f | -6.74026 | -39.65439 | 2025-11-07 03:36:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b35ecb5c-45df-3a6e-9872-03a187b1bb06 | -6.73856 | -39.65332 | 2025-11-07 03:36:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43ffbd86-e577-3693-877b-70a9f0429955 | -8.75073 | -44.23486 | 2025-11-07 03:36:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d90eb960-a4ae-38ee-95cc-934abad37192 | -5.27102 | -47.16616 | 2025-11-07 03:36:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd72449e-3871-3771-8749-0290554fa0f1 | -6.25919 | -43.6845 | 2025-11-07 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7507c639-5839-3071-807d-88dcec3d7958 | -5.2738 | -47.16943 | 2025-11-07 03:36:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5902b530-c014-3196-bc07-5701bfc137a7 | -6.50825 | -38.73584 | 2025-11-07 03:36:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 986ece1e-fa7f-3e99-80d8-bc30986239cd | -5.95072 | -42.17958 | 2025-11-07 03:36:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 09a1cd31-a6ba-3c52-a449-bb5222e4d6d6 | -16.30807 | -45.6171 | 2025-11-07 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30e07541-eeed-3b7a-81b0-9a231b92d6b2 | -16.31416 | -45.61476 | 2025-11-07 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4035cc88-9526-3a79-915d-73e660ff64ad | -13.22286 | -44.56074 | 2025-11-07 03:38:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cd6863c-90dc-3d9b-b44e-7d6853f978bf | -13.22103 | -44.55939 | 2025-11-07 03:38:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9176322d-02f8-3053-bd2f-752051014daf | -16.3054 | -45.09871 | 2025-11-07 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97abd502-63e4-3d5b-9feb-e82287be1923 | -16.29806 | -45.61124 | 2025-11-07 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6feb225-a94f-3765-b451-39af827697fd | -13.54092 | -44.55953 | 2025-11-07 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 9c9454f1-7974-3795-ae6a-b48b72bd7650 | -13.53563 | -44.55848 | 2025-11-07 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 654c5d00-94ad-3857-9979-d08c889c3f51 | -16.33025 | -45.61831 | 2025-11-07 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a79c83a7-d4ef-3541-815c-5dad7d10f194 | -16.3027 | -45.61594 | 2025-11-07 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6fb627a-de75-3616-8e4e-08e353fd1b50 | -16.33562 | -45.61952 | 2025-11-07 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76ffc66a-1ea0-3808-b485-771c9f2d6f02 | -12.81641 | -43.77921 | 2025-11-07 03:38:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 898f4e10-b5ee-3312-a888-19b74e0595c4 | -12.81374 | -43.77961 | 2025-11-07 03:38:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cc143d5-91e1-3fc5-876b-4c6daa47e5db | -13.21756 | -44.55954 | 2025-11-07 03:38:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e65b1e0-c397-3afc-ad07-baaa4a51342b | -13.22033 | -44.56286 | 2025-11-07 03:38:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75290a9b-cebe-3757-90b7-4a870d81ae9d | -16.34097 | -45.62072 | 2025-11-07 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58fded08-216b-3a36-9aa6-e9147c8ba694 | -16.32489 | -45.61712 | 2025-11-07 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 585edc72-ee2e-3635-ba05-2f4b256dcb0a | -16.31952 | -45.61594 | 2025-11-07 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49aba754-0061-3690-8e70-681edd901b8f | -4.746 | -42.9171 | 2025-11-07 03:40:00 | GOES-19 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 00fa9933-4f7c-3459-85dc-da1b2d455751 | -9.4537 | -59.1949 | 2025-11-07 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7974f4ad-ec63-3e82-b574-c651447ec798 | -5.0868 | -44.7887 | 2025-11-07 03:40:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 62f1caa8-9a04-3f5a-aa71-0c48e8fef29e | -9.4535 | -59.2143 | 2025-11-07 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| ed529331-bd1a-35d2-b8c1-c91a37e6f8eb | -19.37473 | -44.80269 | 2025-11-07 03:40:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9d12d5c-b471-338e-896b-59465e6d8403 | -23.60098 | -49.01213 | 2025-11-07 03:40:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfd52776-e719-3aa3-9115-db2670a468c2 | -18.97493 | -50.03571 | 2025-11-07 03:40:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18a96c52-6d3b-3ea7-944e-f02839697822 | -18.97914 | -50.03164 | 2025-11-07 03:40:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0206bf6d-0aa7-3f45-81a9-4d2c8d1a8616 | -23.58464 | -47.03543 | 2025-11-07 03:40:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8604ef6b-dc22-30d1-adc1-31b87b8b3531 | -18.9778 | -50.03743 | 2025-11-07 03:40:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8516a70-8b8c-39f6-adc4-ad804e2b5780 | -19.84141 | -44.89998 | 2025-11-07 03:40:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccaf95e5-6aeb-3591-83ca-06284d43831a | -23.5818 | -47.03691 | 2025-11-07 03:40:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0763c086-7ba5-3d81-bdea-3de7983b41f1 | -22.10364 | -47.12571 | 2025-11-07 03:40:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e489c54b-b2b2-3cbd-a458-d48306af165f | -18.98287 | -50.03176 | 2025-11-07 03:40:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79070685-c6f3-36ed-95bd-c64e59793687 | -22.10288 | -47.12915 | 2025-11-07 03:40:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 416187e5-0ddc-3b4d-a78e-bd2401be5196 | -19.54276 | -44.172 | 2025-11-07 03:40:00 | NOAA-20 | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30019163-290b-3d48-b4ce-5e8d523627bc | -27.44928 | -48.44672 | 2025-11-07 03:42:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6dea1216-2a53-3351-8547-fc8b804eb172 | -27.44847 | -48.45021 | 2025-11-07 03:42:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0255f683-bf67-355f-88bf-306c71eb098a | -27.45275 | -48.45503 | 2025-11-07 03:42:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b8a5bd6-9702-3416-82fc-293782bab059 | -27.44341 | -48.44873 | 2025-11-07 03:42:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ae7b5187-7736-3815-b198-9f55908db06c | -9.4535 | -59.2143 | 2025-11-07 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 9b73b188-fd80-3dbc-993a-b19eadb952d1 | -5.0868 | -44.7887 | 2025-11-07 03:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d0f7ac37-58f4-38d6-bab6-ff8467b68eb7 | -4.2961 | -45.8938 | 2025-11-07 03:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d66b2593-1ba6-33c0-8651-8a5f1fcaaa61 | -6.5631 | -51.1126 | 2025-11-07 03:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a11d4ab2-d8cb-30df-9344-378cce44d792 | -9.435 | -59.1959 | 2025-11-07 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5766d87e-89a8-31a4-8248-73490c57fa5f | -9.4349 | -59.2154 | 2025-11-07 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 5494c717-b044-3249-9793-3107dac6d783 | -9.4349 | -59.2154 | 2025-11-07 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 3d0db039-79bb-3610-9742-270ce2d0711d | -9.4537 | -59.1949 | 2025-11-07 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b37143ca-ca54-36cd-92c5-f619cad4f39e | -9.4535 | -59.2143 | 2025-11-07 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 28556506-412b-3dfe-bbcc-dfaba3df0844 | -9.4537 | -59.1949 | 2025-11-07 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2519c722-338c-3cdc-92f2-bcb6fa44e434 | -9.4349 | -59.2154 | 2025-11-07 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 8a8d0279-1f37-3a33-a699-91ae1531ad77 | -9.4535 | -59.2143 | 2025-11-07 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 1a29b05a-df96-394c-bc49-79c19d25c225 | -5.0868 | -44.7887 | 2025-11-07 04:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 528b7aad-01d6-3860-93e1-2196f565144d | -3.45623 | -48.83442 | 2025-11-07 04:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1fed229-b011-34a9-a5fe-3d8ecc6fa941 | -4.47031 | -43.22697 | 2025-11-07 04:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00f0b865-0e13-3020-a3fd-a7f8b6f2afb9 | -4.73981 | -42.92926 | 2025-11-07 04:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8b49812b-521a-37f1-8fb7-28e52be892e4 | -3.06068 | -49.37472 | 2025-11-07 04:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c0c2d40-7737-3fff-b7c3-3bfb11c4a209 | -3.09254 | -50.32087 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b66c5815-3f36-3294-a5a0-7d6f50615e5a | -4.68919 | -43.40441 | 2025-11-07 04:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4207238-23f0-3352-b5f0-352504e00307 | -2.98257 | -52.82113 | 2025-11-07 04:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9fed990-2c94-3e42-b5b0-c7bc8a06a59b | -3.52871 | -47.54911 | 2025-11-07 04:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d46b03c-d330-30fc-b2d7-b9f30eb60039 | -3.34392 | -52.04903 | 2025-11-07 04:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8332b868-f2e1-3304-82bd-6a42adb3ea6c | -2.28688 | -48.49897 | 2025-11-07 04:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 747dc674-1e2d-343f-b6d3-f5ff8fc1ae8e | -4.74334 | -42.9298 | 2025-11-07 04:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd2b4c51-8e61-3bea-84aa-b8c360323a42 | -2.9817 | -52.82639 | 2025-11-07 04:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a481b68-f61a-3cdb-b3e8-6745dc3e4235 | -3.29041 | -50.03824 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 947ea34e-0692-3bca-a3d6-a98310ea63ed | -3.40554 | -50.27271 | 2025-11-07 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa00c191-8bea-334e-9511-e71f00cb7ccf | -4.29055 | -45.88985 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 600947d2-51ca-3a9f-8f94-774fff7cf010 | -2.78786 | -50.31853 | 2025-11-07 04:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebdf2ff9-ddf7-393a-bc3a-ad691226115c | -4.29439 | -45.88692 | 2025-11-07 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README6.md)
