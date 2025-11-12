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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2b46df5-3759-3554-aad6-3a83884fb42e | -5.00152 | -46.82384 | 2025-11-12 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c24f898-b696-3109-aeac-0437695d2cd0 | -6.10947 | -41.54116 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 88c49ffa-5852-37f8-98a8-a2b9adae2492 | -8.31489 | -43.63864 | 2025-11-12 04:31:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6103d75e-6dae-3325-8919-bc4390b4dbc3 | -2.57597 | -47.47129 | 2025-11-12 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42599dc0-4c6e-301d-aab4-ab855797fd6a | -6.07878 | -41.55569 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 161cbdbe-b7ea-33d3-be9a-144a12e857c3 | -3.10009 | -49.27243 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 286a82be-28e3-3975-9dec-e57791752c42 | -5.22904 | -49.57806 | 2025-11-12 04:31:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cbf692f-934f-32b3-89d8-4953f13c2d0e | -3.88753 | -47.18131 | 2025-11-12 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85f00483-fdd9-31aa-967b-1583d4f44893 | -4.10594 | -48.02168 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a63742a-a93f-3195-bc52-81e95feeb23e | -3.2592 | -44.66614 | 2025-11-12 04:31:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54adaf6b-3c13-3d5b-a315-edf2a6f2d214 | -2.86793 | -51.48194 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 897b3b79-a927-3e82-b940-7e37fbfc17be | -7.28182 | -41.57723 | 2025-11-12 04:31:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 897957e4-b9c6-3f8b-a033-b59b01e5cf4c | -3.09723 | -49.26809 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b968865-a231-359d-8d34-68811f48b7b0 | -4.10981 | -48.01871 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f61e5ff-43b7-3db4-b434-1de6ed117c61 | -7.49046 | -40.12523 | 2025-11-12 04:31:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad296bfb-d9c2-3e6e-b8a2-eb9fbf59b2f1 | -2.91015 | -51.46826 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8eeeb9c-7ca4-3c34-9e87-7c64a7ea60fc | -5.64885 | -45.98465 | 2025-11-12 04:31:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79b2afaf-0776-3923-81b9-3745b9523db9 | -2.73957 | -47.14405 | 2025-11-12 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 175532a6-3b36-3222-a1ed-bdcfb2df9828 | -7.14185 | -41.26094 | 2025-11-12 04:31:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 00ac8dae-aada-3f82-b559-c43cad7f50d3 | -4.91814 | -49.99768 | 2025-11-12 04:31:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0d07537-1caf-3dcb-ae52-7d8aabd35127 | -6.87887 | -42.84727 | 2025-11-12 04:31:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0f71896-c029-3993-97f7-977b786e9161 | -4.1159 | -48.02325 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28fd2703-737b-366c-8a08-5faaa014c1f9 | -4.9603 | -43.71186 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 161e54cf-db9d-3027-9305-3ab168d2b20e | -4.50617 | -49.66485 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bd6eb2c-922f-36e9-953a-de69f98b2854 | -4.26463 | -44.60309 | 2025-11-12 04:31:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47a8ee3b-a910-3f77-8c36-56ed7281c093 | -10.49958 | -44.94241 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c3b1b25a-2109-34ec-b63d-67a4812763d0 | -3.58504 | -46.46008 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 984a7ea8-e65a-3f05-803f-604d96934f6c | -3.71492 | -45.82437 | 2025-11-12 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b08903b8-3262-31c8-bfc8-580463aabbfe | -11.00444 | -38.3217 | 2025-11-12 04:31:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6b10ede-24c4-3ed3-8b3e-dd25e3340105 | -3.06524 | -51.07822 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 079e9bf7-a4e3-3bb9-ad3c-6650338ee623 | -7.45934 | -44.74009 | 2025-11-12 04:31:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c0991db-eee8-3a41-9d0d-70ae4a6a8332 | -5.00537 | -46.82089 | 2025-11-12 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f884b0a-0cfd-3ec3-939d-b714622c7c05 | -2.83674 | -48.83269 | 2025-11-12 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e6ae0d5-943b-3e8a-8407-ca11b9afd617 | -7.78615 | -43.79668 | 2025-11-12 04:31:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 724c04c6-be45-3189-a76c-f278419d74c7 | -2.39683 | -49.39895 | 2025-11-12 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d58389f7-ce23-318f-b037-e00af88f6e92 | -7.00442 | -42.78585 | 2025-11-12 04:31:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b8ae545-ac09-3031-a256-e97f66475d6d | -3.98487 | -47.29846 | 2025-11-12 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| cd0066ba-c10e-3d27-8f34-f1aa04f38288 | -4.48131 | -44.29946 | 2025-11-12 04:31:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f86ec498-1280-3ad3-a2ea-234e2c1e3902 | -4.82885 | -45.54775 | 2025-11-12 04:31:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbd0ef8f-fca3-332a-b6e2-8d557e0973f8 | -7.50025 | -41.24121 | 2025-11-12 04:31:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4943703d-47a2-373f-a9a4-f1e28d069428 | -7.12685 | -41.86832 | 2025-11-12 04:31:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 23df9463-e464-333b-827d-0c8f352f6cd9 | -3.77053 | -48.92133 | 2025-11-12 04:31:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77591c7e-7375-3901-960e-ea8316d55582 | -5.71718 | -46.50627 | 2025-11-12 04:31:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f2dd97e-60e5-3c98-b303-c6c9f15bf03e | -3.36559 | -49.51006 | 2025-11-12 04:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdb0688f-e606-3379-9102-93e9c06162a7 | -6.78116 | -42.84333 | 2025-11-12 04:31:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ee7ffdfb-094b-31a3-af05-b0ff75e8e12a | -3.2385 | -50.03997 | 2025-11-12 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dad04349-9fe1-320c-84e7-fd84ff31f487 | -4.40948 | -43.12159 | 2025-11-12 04:31:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e71ea952-d046-3399-9d74-897c523b1627 | -2.63926 | -49.19485 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2dd6a45e-3efe-32cf-9a71-bf57c12b8e34 | -8.72873 | -48.52711 | 2025-11-12 04:31:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad243ab7-bdb5-3e67-bc5f-a9cc2b1ae452 | -2.87734 | -51.47327 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 979fe454-2e26-341e-9b96-1d07219aa9ae | -4.77522 | -42.66216 | 2025-11-12 04:31:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6261e813-ca9b-3cb8-95eb-9b118bfe211e | -11.00394 | -38.32575 | 2025-11-12 04:31:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0fb238d9-5a4e-3bd5-a66b-dfb0a231e5b8 | -7.28622 | -41.57787 | 2025-11-12 04:31:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2636a723-1070-3e13-a99c-08303d26287a | -4.72721 | -42.82093 | 2025-11-12 04:31:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71deeafd-fd9a-3531-8c3a-380ca6c6cdcf | -6.90186 | -42.07832 | 2025-11-12 04:31:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 89b9f322-ed78-3284-8019-94a9f3ddbe61 | -6.1011 | -41.56923 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40b210c1-4503-34ae-9d61-956677806f08 | -4.51385 | -45.63131 | 2025-11-12 04:31:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6807feb-95ae-3bc9-b56d-de497bff7777 | -3.84454 | -50.05941 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e1b79718-d943-3202-ac0f-3285ae5cc9c7 | -7.47568 | -42.55593 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9489dada-1397-34e6-ac42-db2b388dc6f9 | -9.66913 | -43.89605 | 2025-11-12 04:31:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 33ef8863-d664-33d4-b4cf-3747a6285a3d | -4.11091 | -48.01175 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d45ee2a-ef95-3718-b62c-97e4bebe9e95 | -2.88125 | -51.47387 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 430a0124-3706-3008-8db9-80f01e59c8f9 | -3.35338 | -42.15979 | 2025-11-12 04:31:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e50b2512-8276-326b-be0a-e96955fe0992 | -2.96217 | -44.59138 | 2025-11-12 04:31:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c2e7f24-ddd4-3c48-9704-46011eec90c6 | -3.63491 | -50.23751 | 2025-11-12 04:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| babf9a79-37a1-3a47-a851-9e91df21af0a | -4.21523 | -45.95246 | 2025-11-12 04:31:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b89bf7e7-e328-3f26-a55d-a96680afe9b5 | -3.86673 | -40.98565 | 2025-11-12 04:31:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4ce2a524-ed10-3e00-9da4-593f7ea19cce | -4.3145 | -43.05714 | 2025-11-12 04:31:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 178b1ab4-27d1-303f-90d7-7058f06cfb4e | -4.58477 | -46.44158 | 2025-11-12 04:31:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 041e7154-77e6-3824-b1ec-4b558c9e1fb3 | -4.86903 | -49.59203 | 2025-11-12 04:31:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7d1ddb6-7fde-3982-b3b0-22426e73e88e | -4.08384 | -50.31341 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c22c5d94-11e1-37b8-afd2-4df39fbc1c2c | -6.54585 | -43.03587 | 2025-11-12 04:31:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f5b5f83-ec4e-3981-9341-5e308dc01ba9 | -4.95461 | -43.72459 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d4c521ee-eb79-3137-9256-aea1e10f5d9d | -10.49524 | -44.94629 | 2025-11-12 04:31:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9cb2a8d8-9448-33de-86f6-34f285b0ee51 | -7.49129 | -40.11938 | 2025-11-12 04:31:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bcdf79bd-8af8-374a-8ad5-a5c11d8be988 | -8.31417 | -43.64368 | 2025-11-12 04:31:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbaef0b1-3e1b-37fc-abcf-27bd74c65cc1 | -3.26151 | -44.67432 | 2025-11-12 04:31:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dde2695b-ced3-3678-bb37-d741aa6fd91b | -2.39744 | -49.39505 | 2025-11-12 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 05cf7156-56c3-3d23-8573-5a91f32edd94 | -4.43193 | -38.95916 | 2025-11-12 04:31:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e787dd9d-9601-3131-8b06-35f723004a8b | -7.28056 | -41.5859 | 2025-11-12 04:31:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 57783009-41e0-31f7-bd24-49a3798b7a1a | -4.54788 | -50.26419 | 2025-11-12 04:31:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbf126fb-738c-3402-8986-48582fc060d1 | -4.96201 | -43.72578 | 2025-11-12 04:31:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e488bffc-44e0-3dd2-be39-96ef196d45f1 | -7.06446 | -41.58652 | 2025-11-12 04:31:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 54f0bffd-230b-3588-81b7-850fcb708de7 | -2.63914 | -49.21832 | 2025-11-12 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb32f1ff-1914-325d-9dd8-2c59ef3e7a0d | -6.89834 | -42.07061 | 2025-11-12 04:31:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1a9a362e-4849-31b3-ab4b-bf560d2fb352 | -7.12746 | -41.86417 | 2025-11-12 04:31:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6c3fd15d-5c2a-376d-ac35-b82d8916b237 | -4.11145 | -48.00827 | 2025-11-12 04:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11ecef1e-df36-3f64-9dfd-ac116d5d244d | -3.35286 | -42.16323 | 2025-11-12 04:31:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2032e389-cfde-3dc8-9f12-3c7f1fb9e968 | -3.49458 | -55.41455 | 2025-11-12 04:31:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b949f0cd-4689-3906-8ed8-d61b7c26b59d | -2.91328 | -51.47377 | 2025-11-12 04:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17af29ac-a150-342d-b5b4-25a6f15b8e8f | -8.0076 | -43.35148 | 2025-11-12 04:31:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dfb62982-3abc-3768-ac90-29bc6a4806ee | -8.72543 | -48.5266 | 2025-11-12 04:31:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| accdc75d-b919-3565-90fb-b4cff5bc134a | -4.28265 | -46.0644 | 2025-11-12 04:31:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed3fbf99-ae8b-3153-bf0c-43c3cf6e2022 | -6.09448 | -41.58501 | 2025-11-12 04:31:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa06fbe0-a034-3a48-bb00-243c0ddcaaaf | -3.35737 | -42.1604 | 2025-11-12 04:31:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2111bc3-0ef6-33e9-9255-79881a40295e | -7.06536 | -41.58427 | 2025-11-12 04:31:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| faea2a83-41a2-3f7b-bd8e-25a7c2e9d5bb | -9.18984 | -41.03193 | 2025-11-12 04:31:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10792e86-fdba-342c-b9d1-bf4303b179be | -3.88423 | -47.1808 | 2025-11-12 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79a914b1-dbe4-3322-aa0f-a3620fc487cd | -5.6055 | -41.07038 | 2025-11-12 04:31:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c0fca9c-01fc-3b4f-a6e4-024a4051f3cd | -6.47708 | -43.53675 | 2025-11-12 04:31:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
