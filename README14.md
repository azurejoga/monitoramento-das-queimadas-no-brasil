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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 570d5954-c929-33a9-96e6-3c9213465af7 | -14.01995 | -55.12412 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6e4f227d-9b62-3afe-83a3-39b36cd9cef2 | -9.87539 | -49.33803 | 2025-06-03 05:12:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5320900e-8cb4-3642-bcde-18ed7c11c209 | -12.48898 | -57.184 | 2025-06-03 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6494e03d-68bf-3fa0-be17-eab5363798d1 | -12.0965 | -54.67111 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49d2d4db-30c8-301c-a88f-253f06541413 | -11.5529 | -56.43295 | 2025-06-03 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 312d8def-7ff9-3afb-ac08-1fc10771fffd | -10.46169 | -47.94063 | 2025-06-03 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23846367-a0fe-3fdd-b4a6-c6ee623008d4 | -14.01618 | -55.12356 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9dfd0126-6d5d-374c-a29f-ca2e923ca40a | -11.55692 | -56.42964 | 2025-06-03 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 622b8d43-707f-3dbe-82fa-7294706c2d72 | -11.40671 | -52.95016 | 2025-06-03 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f365d4a-1f96-3551-a997-1a81333df2f6 | -10.6826 | -57.60162 | 2025-06-03 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b321b31-cd4c-36fb-a366-7ad7482fa2bf | -10.68206 | -57.60514 | 2025-06-03 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54bfd0b7-117c-39c8-8546-bf1cc3fa4c26 | -10.23676 | -52.22116 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d55a128f-4897-3591-b671-49e59801a539 | -10.696 | -57.64708 | 2025-06-03 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdda737d-38d2-307d-aaf1-ade470417393 | -11.44038 | -55.00832 | 2025-06-03 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ec1b995-46cc-3a55-a39c-669b42485700 | -11.90672 | -54.78023 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 562e90e9-7f57-3394-b751-f296f02f52c3 | -11.03508 | -59.17877 | 2025-06-03 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91803446-5dc4-36ee-98ee-31cbdf3bf710 | -9.24 | -63.28572 | 2025-06-03 05:12:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e98efcf-1430-38ce-9c73-049b76d320a9 | -11.90232 | -54.78429 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 05cdb511-398b-3487-aa51-7a9ca32a35b9 | -10.23762 | -52.22783 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac3e1d90-9dd5-32a6-a199-128844df7816 | -13.36617 | -54.26373 | 2025-06-03 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a65af45-fff6-3d6b-940f-f9ddf72813dc | -11.64663 | -55.36996 | 2025-06-03 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69bd7e87-02aa-3b32-9ad5-f905548673f7 | -14.01552 | -55.12831 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03a537d6-db99-3142-bc1c-618f2209b559 | -12.48843 | -57.1877 | 2025-06-03 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 228b52b7-169c-3c34-9258-e369a737eb96 | -11.90606 | -54.78484 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ca38932a-c2c5-355f-8fdc-4b5c11b98032 | -12.45562 | -54.91602 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 578320b9-1360-343a-9936-a686656164ef | -11.2517 | -49.4987 | 2025-06-03 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d94b27c-3eb8-34ca-a6bb-870c1412ae60 | -11.91932 | -54.41768 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01f2f4f5-4a9a-31f3-98b9-c3e789af27ad | -14.02549 | -55.13946 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71b07ea5-c3be-3cbf-baf9-9f2f7072b1f9 | -11.2521 | -49.49541 | 2025-06-03 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ac2143c-13ba-39be-acf8-cf80ede4c264 | -11.41089 | -52.95071 | 2025-06-03 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85ceb837-729e-388f-bf39-b19d37003952 | -11.92016 | -54.81955 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11f9b5bb-a012-30cd-b85c-23b2a613d2f0 | -14.02992 | -55.13531 | 2025-06-03 05:12:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e0a26dd-2e26-343e-aa2c-014bd05c4047 | -13.48541 | -56.55884 | 2025-06-03 05:12:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21335c3c-e847-3d70-a166-561df33a880c | -13.6369 | -52.18346 | 2025-06-03 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90c39159-6fef-3464-aef2-3211f24a6e4d | -10.46223 | -47.94218 | 2025-06-03 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0dee2a34-b4d1-3ffa-ba00-b11b46dfd8b6 | -11.9239 | -54.82011 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bff9f3d-605f-382b-b2ed-e218f73913d7 | -11.92315 | -54.41822 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80d89744-2ba0-3705-b42f-0c66282a5685 | -10.49424 | -53.66159 | 2025-06-03 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18f3a47d-d5f4-3063-87cb-f0e6339ec18c | -7.89242 | -61.47403 | 2025-06-03 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ee4a9bd-9514-358a-86c4-7175b57b3f2a | -11.58038 | -47.44302 | 2025-06-03 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 101dba04-55cc-3277-b560-4325095997f8 | -11.92248 | -54.42305 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44176e09-fa3c-3649-a6aa-4e33530e1cb2 | -10.45541 | -47.94397 | 2025-06-03 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a8bb4eae-7816-31ea-bc4a-d8c0a84b7581 | -11.55634 | -56.43347 | 2025-06-03 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fd02767-cbc4-34a6-ba09-da7db12c9184 | -9.9636 | -64.96597 | 2025-06-03 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20642d41-6450-389d-8029-5379034db5a8 | -10.24107 | -52.22178 | 2025-06-03 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 150a4858-3dfa-3e44-99fb-8c54444dad3d | -13.64143 | -52.18419 | 2025-06-03 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c539a3f-4025-3daa-ab67-98955e75a152 | -11.55749 | -56.42582 | 2025-06-03 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de834639-ee04-3d9e-b170-22751895f083 | -12.16948 | -54.2596 | 2025-06-03 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb0669d2-eac2-3ab1-979c-94e74ad13656 | -11.79397 | -47.38021 | 2025-06-03 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2c3c739-039a-3d81-ae27-63095122dd0c | -18.83997 | -47.67947 | 2025-06-03 05:14:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 885d050c-117a-37fa-aa30-bb882c2151f7 | -17.76195 | -52.43909 | 2025-06-03 05:14:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 195b0614-398f-3048-bbf0-c4b41fca9da9 | -21.24882 | -56.15793 | 2025-06-03 05:14:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 727675e7-5734-3876-bc0c-21d79f2f61ce | -19.06648 | -53.44559 | 2025-06-03 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b272333e-d209-3826-820a-a49b74cc15ee | -20.6912 | -56.67624 | 2025-06-03 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d24c5779-9334-3833-b4d5-2378f452ba82 | -18.87409 | -53.63721 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 42.5 |
| b1629c09-d652-328e-b672-3cc170d3cc40 | -18.34772 | -53.25103 | 2025-06-03 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b76d22c-26c9-312c-8ce4-bfaae34eab78 | -18.87845 | -53.63462 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 448da771-5e80-32fa-8aa0-fde8c1ff1abc | -16.30729 | -54.88301 | 2025-06-03 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d6d9e28-f85f-3420-9fd2-c4689292b0d2 | -20.71633 | -56.63074 | 2025-06-03 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 10fd44c8-3b98-3ea3-ba4b-cdb2c7dbe92a | -20.72074 | -56.62639 | 2025-06-03 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffb36d99-8c25-3dd3-a9da-0928f2981f95 | -18.87741 | -53.64367 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 31359a3f-4dc5-330c-9068-5c54295865a0 | -18.86913 | -53.64107 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 8937e2cd-f729-386b-a1a7-2db075c04deb | -21.24493 | -56.15733 | 2025-06-03 05:14:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7f9814f-d7d0-34dd-8558-770c1f526526 | -18.873 | -53.64613 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a22c8b97-d001-39b3-8b16-647871266d57 | -20.95848 | -56.60766 | 2025-06-03 05:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e6dd456-22aa-3577-95e0-eb2ebba2a817 | -20.72761 | -56.63254 | 2025-06-03 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ba2e89a-e50e-3266-a575-af2bea1b7d99 | -18.86417 | -53.64487 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 928ba026-9502-3c62-ac22-adcfd4b274ba | -21.89585 | -55.96868 | 2025-06-03 05:14:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 301891e4-a199-37f4-8e64-3a3864b5b6fa | -18.40383 | -54.57977 | 2025-06-03 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 939eb5b8-6521-32b6-9290-6b799d6ef77a | -18.83808 | -53.60012 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fe46577-0fee-380c-80d3-e9bc857886d0 | -22.31553 | -53.63237 | 2025-06-03 05:14:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7020bde0-5e58-3938-80d0-756ae5fc9779 | -20.56824 | -55.3863 | 2025-06-03 05:14:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cb6a14c-5418-340c-954c-fca22fb63f3a | -18.87022 | -53.63208 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 74badf4a-d7c1-36c1-bb23-803e12dbe304 | -18.86525 | -53.63597 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 534c02ba-1db2-35fc-857d-fafc64f5b8fa | -21.80272 | -52.76552 | 2025-06-03 05:14:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7751425f-979d-322f-92f5-1a9f4ff44ea7 | -19.70774 | -54.6184 | 2025-06-03 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 024c05c1-f3f5-301c-b828-668c884fdab9 | -20.69184 | -56.67131 | 2025-06-03 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb6f88ab-43ca-3703-8d64-1c5f86c6cabd | -18.87793 | -53.63917 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 253f90ee-3ff7-3d53-92fd-1035c3920261 | -16.39589 | -58.1764 | 2025-06-03 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2aec410a-b5f7-3bc1-ac11-981e676defab | -21.59978 | -57.57841 | 2025-06-03 05:14:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 451f7e8d-f300-3c9a-bf1e-9beca683fe49 | -18.84024 | -47.68405 | 2025-06-03 05:14:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3dc1eaa-1530-3c29-abbd-d08ee9ea13e6 | -16.62855 | -52.13515 | 2025-06-03 05:14:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 851840a9-077c-3d84-8b22-1a149453d45d | -20.9547 | -56.60708 | 2025-06-03 05:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e5351c0-55a8-3ead-943c-4091ac1791b6 | -20.72385 | -56.63196 | 2025-06-03 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80ae9fbf-cc35-31d8-8106-85264fcd29cf | -18.86471 | -53.64043 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e2f526e4-36e0-32b6-80d5-8506bd1d8953 | -18.87852 | -53.63778 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 20.7 |
| bb1ed962-5d43-3c27-8f51-d605ffacc8c6 | -18.34715 | -53.25574 | 2025-06-03 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 228abeb8-d6d7-3602-8018-6355b48c6af2 | -18.87796 | -53.6423 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 08a52ef4-1932-34ab-8e61-be42c11c3de1 | -14.85229 | -56.45914 | 2025-06-03 05:14:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba68bba9-b2a4-3641-beb9-d365dbe46572 | -18.86967 | -53.63662 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 42.5 |
| eb53ee08-f8a6-371a-af82-8c23e55f9100 | -21.80329 | -52.75997 | 2025-06-03 05:14:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b6f2b39-3d29-3d8e-aa40-cbd014dfbe9b | -20.72009 | -56.63137 | 2025-06-03 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3f21be4-00fc-3429-99d3-f5a68feb644a | -19.81196 | -53.83765 | 2025-06-03 05:14:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4406863f-a72a-38ed-8ef7-fedaa2848e78 | -18.87465 | -53.63267 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 96591c15-7775-3ffd-b1cb-82ac0ae8b2da | -18.40845 | -54.57652 | 2025-06-03 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 920314c6-8550-303e-bd7b-7e74de8e4e9e | -18.87354 | -53.64168 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 6ed13bfb-3bdb-3493-ad3f-a854e97b28ee | -20.7245 | -56.62699 | 2025-06-03 05:14:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c9fe8bb-abb6-3b54-adc2-b27358e43bec | -16.70486 | -57.9608 | 2025-06-03 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 345022e8-ffbc-3c76-a34b-c4a40f5b0beb | -18.86858 | -53.6455 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 19.1 |
| dea4f53e-fb3a-3116-b222-087c019af8fe | -18.8658 | -53.63146 | 2025-06-03 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README15.md)
