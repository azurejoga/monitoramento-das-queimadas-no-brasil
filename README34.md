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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cd39729-19a8-3195-ae6a-e56b1b14fd7d | -3.73101 | -52.13478 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d99c3b14-bfb9-305a-8ec3-6c3f22eac663 | -3.71636 | -51.11127 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adcdd950-0edc-328b-ba84-bfe1163292fd | -3.71581 | -51.11476 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7fe7980-f883-34ae-9fc4-6644680f6cb0 | -3.71356 | -51.10726 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19ecc342-918b-3293-854a-65f17d90b1de | -3.71247 | -51.11425 | 2024-10-19 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 243c0753-fc7e-3648-b8b3-ba37569e8b90 | -3.70327 | -51.59991 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06cfb3bc-10c4-3e0a-95b2-1e531942dcb1 | -3.70273 | -51.60337 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54496cb2-bd75-30b2-9985-b45af58a08d1 | -3.6994 | -51.60285 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4ea5249-2feb-3d6a-9be1-54dadbd899f5 | -3.60463 | -52.11855 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95083d9b-9aec-3bbc-8589-e498fc5d59bd | -3.60408 | -52.122 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e29ad6fc-dfab-3b01-ae68-200de6beffb6 | -5.55435 | -51.10193 | 2024-10-19 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4481cf2c-8cc7-300e-8470-e11cad74d810 | -5.65121 | -51.29474 | 2024-10-19 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3afe24cf-3ea9-3a08-b465-56d690e274ab | -5.51737 | -51.1181 | 2024-10-19 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4062beb4-f914-373e-aefc-23530a679582 | -5.514 | -51.11758 | 2024-10-19 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49615650-68a4-3c7a-b36b-ec0752b473b6 | -0.36658 | -51.7114 | 2024-10-19 04:49:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 258c3783-ae1f-314e-ac51-c2c0ce24caa5 | -1.76584 | -52.2358 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 202d1049-cf65-3734-ba18-473ebd7a1c6f | -1.72496 | -52.53858 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3660c93-9b2d-3e4d-bdc2-c87c6fe5c770 | -1.71151 | -52.49311 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05ba285c-c2a4-3f47-9ed3-f60d0f3d725f | -1.71042 | -52.54355 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90235cdf-5079-3947-9bd1-e0fc6e44e7ae | -1.70872 | -52.51074 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a40d8f9f-2b86-301a-92fa-14a8a3e31182 | -1.70817 | -52.53596 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b41e4e0-f94a-37f7-858a-348c63593ab3 | -1.70538 | -52.53191 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67197afc-504a-3b05-a1fa-558f45128c3e | -1.70537 | -52.51022 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96ce7096-975b-3d23-be50-957ef08a9bf4 | -1.70481 | -52.51374 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6088ca1-4741-352d-9a5a-ec3f6260f6cc | -1.70201 | -52.5097 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8680793b-46eb-39b7-8996-b9e668e962ce | -1.50522 | -52.58079 | 2024-10-19 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e000006-d350-3803-b007-8475e18d72fa | -1.4357 | -52.44275 | 2024-10-19 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05262a8b-a573-3806-bfd5-c6c1257db203 | -1.43235 | -52.44223 | 2024-10-19 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| effb406e-c033-3e66-85c6-52ba1b2b2079 | -1.43179 | -52.44576 | 2024-10-19 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ee70bc6-cac1-3398-a028-1bea0f23cb16 | -1.34454 | -52.29188 | 2024-10-19 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fa4d686-0b93-3022-9a1c-938da2dc3169 | -1.27963 | -52.92692 | 2024-10-19 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74a01061-781d-3301-b6ad-706dc8179b21 | -1.27623 | -52.92638 | 2024-10-19 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c079ec0-5bd9-3c97-a2d9-99311b27208d | -1.26422 | -52.91387 | 2024-10-19 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e05a9d9-6687-3e3f-aa5d-c9ab990fa813 | -0.87776 | -52.92884 | 2024-10-19 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1396f7fe-56ac-3c4a-b1dd-53c9729bfaae | -2.20668 | -51.9493 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18f8ba6e-0e5e-3494-889a-4ad76d139b30 | -2.21001 | -51.94982 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4449571-cbc6-31f8-82b3-e8a5e6133072 | -2.0895 | -52.11193 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4591652c-c66f-39de-9327-aa6c3fbffc22 | -2.08895 | -52.1154 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8ea5e0c-dd83-3ee1-9466-e3c2742834cb | -2.087 | -52.25758 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32542824-f5e8-344e-8e3e-63f45d6fe61c | -2.08562 | -52.11488 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20b9c8e1-fedd-3863-b25f-433290c96f3a | -1.98534 | -53.189 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe01e3e9-4f2a-32dd-8d9d-d001954d532a | -1.98499 | -53.19235 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9cacb36a-2ac6-39f5-887f-6fb59e1e71ba | -1.98476 | -53.19264 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 510b4c5b-0f5f-3765-93cf-3596db2be28e | -1.95176 | -52.06215 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 251438ec-62f9-30a5-8a3a-5d4cb34ce6aa | -1.93915 | -52.7283 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62a511ee-d589-3451-b5e1-741fd8ff0fce | -1.89257 | -52.67376 | 2024-10-19 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52b1d359-a4f9-3e88-8183-e17e893e87b8 | -3.54609 | -53.02128 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a98ee41-3759-39fd-99d9-2fd91ae15a9d | -3.54273 | -53.02076 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2eb44994-203d-3c1d-849c-2234fc734efd | -3.54216 | -53.02433 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6e39e2b-5d6c-3832-bdd6-065c867f42ee | -3.4564 | -53.01111 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a24a4d8-6b48-3b72-9e86-03096125873e | -3.45584 | -53.01465 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab33e068-057a-33ed-9222-54f462b66af2 | -3.45304 | -53.01057 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a17fbbef-0c27-30e4-b295-b82c9a02bdba | -3.36418 | -53.21635 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af1e3e2d-86df-33b9-92e9-1840f0927988 | -3.36362 | -53.21991 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7a1d462-4917-3974-a8da-626c9caca003 | -3.36306 | -53.22348 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2b13845-7b22-3c49-9b93-dcf01f8a78ec | -3.35067 | -53.21414 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46fad501-fcbf-3ece-b85c-bc0714613c53 | -3.3501 | -53.21773 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c2fbe9d-1c49-3e95-a3ac-79c655d93034 | -3.31218 | -52.85839 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccc0b623-3d3d-31dd-886c-c9f14801c6c8 | -2.98524 | -52.85069 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| f120b6a6-4f7c-3deb-9a5e-2b7bb83ca398 | -2.98188 | -52.85017 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 5c1a3d68-c8a8-3313-93bd-bf468c8bcc3e | -2.98132 | -52.85371 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 4c13133e-5481-3113-b9d6-b66e4e1487c1 | -2.97853 | -52.84963 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b41f52fd-575c-355b-af17-5781097d6709 | -2.97797 | -52.85318 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9f042be4-12cf-31f7-a053-9905c9a22769 | -2.97517 | -52.8491 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6456d959-0dfc-3554-a03b-70e72b82a8ed | -2.97461 | -52.85264 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2ba5bad8-4c34-3ab5-8011-35c12738ed8f | -2.95893 | -52.90821 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecf0b3bf-fe6a-3cab-ac3e-f9af21410913 | -2.95837 | -52.91175 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3a5b0841-0c0a-37f6-9c5a-2622ee4fcb8c | -2.95556 | -52.90769 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 204e7a84-37a4-38e7-b7b9-3db260920a94 | -2.955 | -52.91122 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 702c03f8-d8c4-3eeb-8a24-a0b681e3643f | -2.95444 | -52.91478 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 6507800f-9fa9-36f9-8374-1212a1a30e0a | -2.9522 | -52.90717 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 7048ef49-efa1-3c3a-adfc-7315bbe99f43 | -2.95164 | -52.91071 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5edf49c9-1c9b-3c89-824f-b2920acc5cca | -2.95108 | -52.91425 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 73750799-0454-30f4-bbf6-e35942ad3b6c | -2.94827 | -52.91019 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78c7f1f9-6ec0-3b13-811c-6a1367a48f60 | -2.94665 | -52.79021 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f1a5c39-ed7a-3a2c-a158-acc5a90d043d | -2.85862 | -53.25597 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e0a99cc-924d-3168-9a01-eea627ced828 | -2.85723 | -53.33016 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28eddc6a-1ff9-3f0d-baa3-a8e8d51e0560 | -2.85665 | -53.33379 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e314f65-9642-34c8-82d4-25a32541e3a6 | -2.85607 | -53.33742 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2fb6292-5248-35ad-ae98-caec443f04ec | -2.85557 | -53.31871 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ef003bf-9619-38a5-b7ec-1faf366ed2bc | -2.85523 | -53.25544 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f84323b6-740a-35ad-9fec-d1c2a65bdac8 | -2.85383 | -53.32962 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4726694b-7ca6-3b64-abf4-ae0b682a7bfa | -2.85325 | -53.33325 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 88c0670c-fcdb-3301-b175-4f547f9ace4f | -2.85267 | -53.33689 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 1694a782-ef3d-324b-96df-8742845d3ccf | -2.85159 | -53.32181 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e47866e2-996c-3141-99ec-d8d033ece001 | -2.79241 | -52.92609 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92f8f31d-7072-3415-b5b1-cd3f15cc7402 | -2.73711 | -52.57337 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1c5b8d85-f904-3a64-b3e3-938a984b651c | -2.73655 | -52.57687 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 17cc8f6d-5706-3164-8010-46b087148b0f | -2.73377 | -52.57285 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ae18941b-d729-3397-977a-4e44f7bd57e7 | -3.30065 | -53.70728 | 2024-10-19 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 56365c63-4793-38bd-a941-46c6f4a60728 | -3.3268 | -52.99475 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32f84c64-f6cb-302c-bad4-49aac42d97fb | -3.31554 | -52.85891 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3aec636-ca74-359c-8d04-8c32eda4960d | -3.30793 | -53.37403 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b2064d8-aca6-39f8-bb3b-1fa60a78c84e | -3.22555 | -52.61407 | 2024-10-19 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c2d632d-2e43-3f49-ae4c-2c7687749168 | -3.21386 | -53.37063 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea2679ad-3d55-351c-9acc-fc8a4ba2c067 | -3.06067 | -53.23895 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fda5b74-4bc3-3909-bd0e-27a67906c7b7 | -3.0601 | -53.24254 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2569defb-8d6b-3dc5-b04c-c82d8c3c8e87 | -3.05982 | -53.23906 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f07d496-2c45-3cc9-ac50-dab2b6dd1219 | -3.05925 | -53.24265 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 663f80f6-57f1-326f-aafb-fb5420c7ecc8 | -3.05643 | -53.23853 | 2024-10-19 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README35.md)
