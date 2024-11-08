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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bcf4542-90d7-3ab8-a9de-7b8dc2d7ffcd | -2.17805 | -47.56281 | 2024-11-08 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58850716-033c-38c7-83de-74688cef4695 | -4.88479 | -45.42795 | 2024-11-08 03:57:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2baafc70-5f34-3ed3-8b99-3822ab5a8d3d | -4.68003 | -46.41091 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 37e2cd62-3b96-3a06-8c27-8ec4b028ba80 | -3.65912 | -42.26281 | 2024-11-08 03:57:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e1dac022-8cb1-3f54-9d86-089786598ae0 | 2.52648 | -50.94226 | 2024-11-08 03:57:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27488855-667e-353f-b9a5-d2eea922c25d | -4.61376 | -45.71496 | 2024-11-08 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5de375ff-c62e-3c06-b927-e9f4452f6784 | -4.50802 | -45.67972 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 0d786360-5e1e-38da-a1ff-4b47589e3f31 | -4.91438 | -44.04949 | 2024-11-08 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc957953-1aae-3488-80a0-8b14a3220547 | -4.60954 | -49.58342 | 2024-11-08 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 30444b5f-54d7-30e1-907d-4fcc3ea556de | -4.30737 | -45.69012 | 2024-11-08 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9403a6ac-c935-3713-8d28-a88e15c96d81 | -5.17426 | -44.22815 | 2024-11-08 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80636494-e72d-305c-9e60-845227e7f231 | -3.2617 | -46.31541 | 2024-11-08 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6e69cc8-7a14-33e7-8e05-a5dd3c8accf8 | 1.66657 | -51.00055 | 2024-11-08 03:57:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81a69162-8284-36e0-a20f-d80ca30cedc0 | -3.95228 | -48.16628 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d654db51-befb-3b46-9a7d-9891d9bc87cf | -4.68536 | -46.40701 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6dec96a-5b17-3e1f-8b3a-b9d1d6d6f008 | -2.87741 | -46.7714 | 2024-11-08 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2700a68-109f-3a46-ac4e-957dfda8ae54 | -6.26174 | -39.37133 | 2024-11-08 03:57:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 15d0dc15-bca0-3f47-8556-113e4b51dbfa | -3.26251 | -46.31053 | 2024-11-08 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42e5d415-0f28-357f-bd8c-c8b944545f1d | -2.44256 | -46.315 | 2024-11-08 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc4aca6e-8b9d-3fb1-bb92-100f9bb0b666 | -4.39413 | -49.4147 | 2024-11-08 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d8a0a9a-fdfe-3cac-aa65-4fd1ecff1fd7 | -3.97226 | -48.18031 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f2c04af1-b33c-32db-9d23-a906c5c7e87c | -4.40821 | -46.14741 | 2024-11-08 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6343e9f6-d472-3812-b192-50b99306c418 | -4.70562 | -43.79188 | 2024-11-08 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9fa630d-2a3a-35c9-839b-2f14c8b6ab9b | -3.54246 | -47.38549 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 88c48617-91cd-3616-a947-d6b427dab2db | -3.95388 | -48.15665 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cebed576-3296-3032-9018-712d56466de7 | -4.61197 | -40.56976 | 2024-11-08 03:57:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 33e819e3-7b2f-3fee-875c-da224a123d4f | -5.39241 | -42.661 | 2024-11-08 03:57:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a884cbaf-2e05-33de-bd1f-79911978af18 | -4.28416 | -45.69493 | 2024-11-08 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 474fddd9-12d9-319b-ba9f-99c0cf8590ac | -3.43721 | -42.20613 | 2024-11-08 03:57:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d6840f94-955a-331d-b143-c369e5fd1f30 | -3.9726 | -48.17258 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 404d1c99-ab44-3ee0-a9fa-2fa51786215a | -1.15109 | -52.01045 | 2024-11-08 03:57:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d6c4a84c-fbfc-3a5d-ad4b-6e59ff2267c1 | -4.24373 | -48.54324 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0176d37c-4045-3317-ac6e-f333a751137f | -1.5014 | -52.16437 | 2024-11-08 03:57:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4253c78f-cba6-3c60-afe1-5fe3c6089a28 | -5.32668 | -44.23157 | 2024-11-08 03:57:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de6524e0-5955-31b2-ba54-9e5b1811ee49 | -5.7399 | -42.00661 | 2024-11-08 03:57:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 67ee241e-6cd3-3c2e-b4f0-4746f9961acb | -3.68779 | -39.43026 | 2024-11-08 03:57:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c2dec544-abfc-3425-b962-ed1361d17d9f | -3.20707 | -44.1195 | 2024-11-08 03:57:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b9cbf75-9479-3638-892c-d0a85e7b6654 | -0.92623 | -47.12963 | 2024-11-08 03:57:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0938b304-c8d0-30ff-b44e-0cbb0a513af4 | -4.51167 | -45.68449 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fc8a47c-0fac-3ada-a00c-f7f37cbff6cc | -4.78756 | -45.41253 | 2024-11-08 03:57:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d2bee97-128f-35d4-80b3-65894f46b66d | -3.60028 | -42.85495 | 2024-11-08 03:57:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 788166f6-6b15-33b9-b61c-de7597cdf701 | -0.95734 | -47.88865 | 2024-11-08 03:57:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba0a7c29-d361-333f-8003-243aebaca873 | -3.7426 | -52.10609 | 2024-11-08 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4506de0-42d4-388b-9952-cc98f3065ceb | -4.51822 | -45.69863 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 31f93191-4813-37a4-987a-aa9e4af7d017 | -3.24462 | -46.47784 | 2024-11-08 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ed70313-2b1d-39c6-af0b-7ee29f7a4116 | -5.54299 | -41.67969 | 2024-11-08 03:57:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d210ccef-39bd-3ef8-be2c-ff5d5bff2b36 | -2.18139 | -46.4642 | 2024-11-08 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f01bff92-2062-3b5f-8f6c-ee9f023507b7 | -3.53624 | -47.36139 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 323f37d9-bd74-371f-a3bd-031fc91256f8 | -4.27981 | -45.69411 | 2024-11-08 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae69203f-5bc3-35fb-b7bf-235f4186f3ba | -3.54835 | -47.38062 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| b2c8964e-7f79-3205-bf4c-8f4809d98b63 | -4.46781 | -48.11669 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4c43267-4aaa-3c03-879e-73346056172e | -4.39476 | -49.41097 | 2024-11-08 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ac15505-87b7-36bd-b903-dd146dba114e | -5.18051 | -46.18752 | 2024-11-08 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd84cdde-691c-3bb8-ad95-62b6322e9a61 | -4.23048 | -46.90472 | 2024-11-08 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 392a3f09-9b3d-3d03-85a6-c2a6a559691c | -5.17104 | -44.22452 | 2024-11-08 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5093399-69f3-398e-9ebe-687c1d772f90 | -5.74111 | -41.99898 | 2024-11-08 03:57:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7bc40111-0f88-33bf-aa42-3e9df61d3c13 | -3.97334 | -48.17409 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4da141ec-d780-3189-8a8f-21da8850c773 | -3.24544 | -46.47285 | 2024-11-08 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0132fe3a-80b9-312f-9764-949b3766a400 | 2.51964 | -50.94328 | 2024-11-08 03:57:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63806cdb-17a6-3a03-9f7d-6045c2d17199 | -1.47386 | -47.22401 | 2024-11-08 03:57:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c940bd93-43d8-33e9-b4a9-4facc14829c8 | -4.783 | -45.65071 | 2024-11-08 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cece62be-3491-3e00-a79a-e743bdf40f5e | -3.80047 | -44.02438 | 2024-11-08 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b464df7-f5d3-3beb-b71d-861173dac36e | -4.69072 | -46.37439 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c15d32f-afae-33b0-ac20-72acf08a46c2 | -0.92328 | -47.13684 | 2024-11-08 03:57:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8195e4ec-4352-38d2-8a7c-6ac10c4c31de | -4.31056 | -42.49397 | 2024-11-08 03:57:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e0adc64-b2b8-331f-b1f1-6b70b5995222 | -3.72154 | -40.69816 | 2024-11-08 03:57:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 681b2b2a-1afd-3e96-9969-9fb78fbb0e74 | -3.91317 | -38.36039 | 2024-11-08 03:57:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0a16ba67-1aa2-31df-b06e-49e4101b3361 | -2.18057 | -46.46933 | 2024-11-08 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4741d21e-8448-3bf6-98de-028e4636e3e0 | -3.58681 | -43.03284 | 2024-11-08 03:57:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be42e824-98a8-3ac7-83b1-af105a57b2fb | -3.80815 | -47.79884 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd385703-0f4c-33e0-b069-76d34cc8b97c | -3.06732 | -45.74467 | 2024-11-08 03:57:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6141c5a-7072-3c21-b2a6-1c282fbc78b6 | -3.58616 | -50.27914 | 2024-11-08 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04bfdf3f-f374-3ebd-b539-43d305bb87bb | -2.57245 | -44.35638 | 2024-11-08 03:57:00 | NOAA-20 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c4712af-637a-324c-828b-8e84f509931f | -3.66594 | -50.25948 | 2024-11-08 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30bc4d65-2590-3b86-b345-190aa7b21b39 | -4.37678 | -48.58751 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e41d7a7-10d7-3006-a685-8bdf725025f4 | -4.61021 | -49.57944 | 2024-11-08 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a391b153-7606-38d9-aa54-53775eae6f26 | -4.23756 | -47.87278 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ad52d3a-4a50-3024-9a2c-37649f323626 | -4.67841 | -46.44916 | 2024-11-08 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f536d86a-7b1d-371a-ac90-dc25d97fcd64 | -3.5589 | -47.38337 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b6cb3ba2-f7a8-38eb-ae4f-89f5e1f7481f | -4.40558 | -45.645 | 2024-11-08 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c5183e9-b224-3a26-97ee-dfb047f80c3b | -5.17035 | -44.22753 | 2024-11-08 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f10e359b-e55e-340a-ad2a-b88972febbf4 | -4.22575 | -46.90379 | 2024-11-08 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d96a2e2-1154-3d8f-be6a-5c5b3a8e39f1 | -3.54247 | -44.96991 | 2024-11-08 03:57:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d875d244-84d3-3b97-b5ce-823cf5cdadd9 | -3.71845 | -41.68728 | 2024-11-08 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0b79a599-6158-3048-b329-68aeda1f68e5 | 0.03291 | -49.43433 | 2024-11-08 03:57:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17c98351-83ce-37ca-a902-99a6db15517f | -4.50957 | -45.69695 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5808f183-d25a-352d-90bb-6f2f8dbdca33 | -3.94866 | -48.15592 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27735bdc-0730-35b3-8468-d31beb98fa7c | -5.74456 | -41.99957 | 2024-11-08 03:57:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b6866018-4b2d-38c1-9fc8-c99ccba500b6 | -3.95282 | -48.16301 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e28bc32b-39b7-3c24-b56f-d15e2d6bf91b | -1.64491 | -47.82736 | 2024-11-08 03:57:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 771d4d81-6629-35db-b50a-1ebf00cdfcb2 | -4.51219 | -45.6743 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 900c7f5a-5759-323c-ac8d-d1f0c458b484 | -3.96323 | -48.13249 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7071ee8b-5d73-32aa-8189-356508116fab | -4.51741 | -45.67694 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| e1905cd1-daae-3c75-a1a3-91ec43e54930 | -4.77227 | -45.74234 | 2024-11-08 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58f72b86-8376-3d39-b03f-d9b762d24582 | -1.38421 | -47.50578 | 2024-11-08 03:57:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 411fa5dc-f3e7-3a18-a304-43d70e1923c0 | -3.54924 | -47.37519 | 2024-11-08 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82a77ff5-0879-3a72-954a-b7d7af406fc1 | -5.85589 | -41.50182 | 2024-11-08 03:57:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f8e7a78d-c33a-33a4-8de2-79bc150f3f46 | -4.14343 | -44.41586 | 2024-11-08 03:57:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5288b184-4059-39b0-9ec9-2cfee77ff187 | -4.99216 | -46.82034 | 2024-11-08 03:57:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c6e2f97-95b7-33b7-96d7-a7a55aa2a30c | -5.05043 | -41.95068 | 2024-11-08 03:57:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README17.md)
