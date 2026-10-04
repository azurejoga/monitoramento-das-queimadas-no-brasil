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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8089ad87-fd18-382a-8ec9-cd6a2f305406 | -3.13711 | -53.73561 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4ab9521-04aa-3627-83e0-a8c4785f1ab5 | -3.43751 | -50.66523 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4f9f87e-0771-3ebe-bfeb-e2b759eae2c0 | -1.87938 | -50.6154 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b9b02da-b6d5-3025-8ad8-afb688fb5815 | -3.18546 | -54.08631 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36b259b3-b649-3ce1-b480-0517aed1d638 | -3.28084 | -53.83186 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86ddf659-e290-3063-b2df-54b0632a1862 | -3.31224 | -49.13427 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 081d45df-cfc5-31cf-b25f-7275943e94db | 1.94424 | -50.91096 | 2026-10-04 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8373c4bc-43ba-3e89-a6ac-e21cf74b3a79 | -3.69852 | -50.66435 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5898fba9-7e54-3c50-a816-11d02bdeded3 | -4.15443 | -47.53665 | 2026-10-04 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc0df4a2-af23-3c4c-84e8-6f44b07a80dd | -4.26456 | -46.36631 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 025aff9e-bba3-384d-a41b-d98749371fe2 | -1.48504 | -49.47599 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 723a5359-902b-351f-a4b8-6f893ab3afaa | -2.90365 | -49.40268 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf79459a-7b91-3743-abda-8615551cd88d | -1.09424 | -54.11357 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 91ea81c2-72f6-30cb-a83a-7ba91f5f6580 | -2.81823 | -54.11494 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 113f566d-06b4-3ae7-8889-89b7ce3a494a | -3.22302 | -54.30925 | 2026-10-04 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db23fba3-fe7c-3c7d-8eaf-7d73d2c56a6f | -3.20749 | -50.75011 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3ec2b80d-d11c-3a49-b45f-2967889f1672 | -3.00572 | -50.46935 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f394a844-0d5b-33b1-83b6-3223e940f266 | -1.2075 | -55.86417 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d4fd7ae4-5d77-3d3c-a0c7-f1662b7ce1f5 | -2.97198 | -54.21091 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88d30fe5-c63b-3561-9350-d750838ce964 | -4.51346 | -45.88718 | 2026-10-04 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67348c9b-2188-3821-930f-96b0accccbf2 | -2.81739 | -54.09595 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0784217-8ad7-37b4-a262-3d72a22f71d1 | -2.96094 | -48.70681 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e3351f3-bdbb-358b-b1ba-2dc5c69648c7 | -2.35216 | -48.86941 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bedae985-e76c-3ce2-a810-f5429a3d911c | -2.65409 | -48.5713 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f69d9a6-5e39-3f97-b470-2903d7b9466d | -2.92978 | -48.74994 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 015f71c2-da06-307c-95c9-aec3c61921f7 | -1.68625 | -48.20355 | 2026-10-04 04:55:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1b25dfd-107b-33a9-bb49-6d7fc5cc22cd | -3.65714 | -55.5016 | 2026-10-04 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09a4037a-e969-3a27-b723-fe5b354534e4 | -3.12255 | -53.75557 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b60403b-3fc5-32dd-96a2-6ee10287d28b | -3.12604 | -53.74626 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72ac1fcb-4062-30c6-a8e6-722d84d73259 | -4.28006 | -50.28077 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| d87f9dab-0777-3671-a7b6-e72faaa773a9 | -2.88846 | -54.13323 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d0af65b-903e-3dbf-b086-9dc25b5cb35d | -3.08118 | -49.541 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 048ea968-da51-3155-9330-0ce2c42e9c8a | -2.79769 | -54.09749 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfc93bd9-86ba-399c-93cd-bf181324219c | -2.25679 | -51.88665 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 920251ad-2780-375c-948f-98594ace4e50 | -4.28339 | -50.2813 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 792fdc82-fa26-39bd-a1c1-d36f1ce2c044 | -3.00282 | -53.87831 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7519f9bb-0756-3aff-bfb4-da5a72111867 | -3.12394 | -53.74686 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acd9b4c9-a977-3c47-b379-af3a2bf7106c | 1.04059 | -50.02169 | 2026-10-04 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f42fb1cb-5582-3237-82c0-c483a2a973fa | -2.80676 | -54.08954 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca6449b8-8cc4-3dc5-8a2c-45f6e5079c63 | -3.1686 | -48.58646 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6085a8f3-9a7d-3674-8d50-9da141fa6a66 | -3.11862 | -53.7326 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 747cc14c-c691-33be-bb83-19075db4e770 | -2.82276 | -54.11097 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fdc24531-e38c-3903-a6b9-5a1ecf28bc8a | -2.84751 | -51.29321 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7fbe69f-3a8d-323a-b30a-710e4351df17 | -4.80504 | -48.22118 | 2026-10-04 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2298f72-d7bb-3c8d-969f-1ba18f009eba | -2.75292 | -51.56021 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a712b61-fc61-3d44-9b90-7d00dae31631 | -3.11723 | -53.74131 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28147fb6-120a-3eb5-bf8e-7c9422339fb6 | -2.69358 | -49.03469 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| e9030642-3c2a-3ec7-ad5f-5f8988944057 | -2.1118 | -48.99889 | 2026-10-04 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 158ebc10-817f-36b5-a56d-1cc56c2377f1 | -3.30887 | -49.13374 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc93479b-a66c-3427-91c6-f5ec3f413d4f | 3.64434 | -60.76017 | 2026-10-04 04:55:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 346ac15d-7d33-3081-82ff-d78dce7c7b24 | -4.26002 | -46.37031 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1a4bad2d-f776-3784-9e6c-3beae880e2e4 | -2.74845 | -51.54478 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82ca4b42-97c7-313c-a536-c09dca76422f | -4.27451 | -50.2728 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a19cba19-c806-32c1-b71c-3c1d971bc0c9 | -2.92701 | -53.94393 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f0c99f4-ccba-3d3d-a73b-85bd1877c694 | -1.41284 | -49.26884 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61aee3d7-481c-3280-b2ec-6d8238fd8101 | 2.09887 | -50.73663 | 2026-10-04 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 643e7ce5-7d93-38c8-9ae5-3c803bae56b9 | -3.1378 | -53.73125 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2825cd35-4739-326b-a9f2-cdcfb4db8f71 | -4.13608 | -51.1861 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9790717b-54f1-37bb-882e-d1256f69a7b0 | -2.81526 | -54.13337 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e23ab738-ec84-359b-83de-b4dd53d0efac | -1.26002 | -54.55796 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 776c919c-4bc7-34ac-9327-532ff67b0348 | -3.29907 | -50.32454 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a884ea01-c54f-3783-b20b-553c2528cf6a | -2.91484 | -54.09052 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56a00d8b-ef2c-3987-ac66-0256c0f5835d | -3.13857 | -53.73935 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 400b7439-524b-397e-9807-8bb3a1416cb4 | -3.70683 | -50.65501 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06711ed8-d9d1-3521-a849-9e2db0378635 | -1.46229 | -49.46889 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc2fc8af-66f0-326b-8cca-9ad96f99bf49 | -3.01504 | -50.47074 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e303610-ab1a-3cdc-89e0-cee508d658a0 | -4.26788 | -49.97701 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5351434-9db3-30f1-bb72-9baf90736ef9 | -1.26233 | -54.55518 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7d5a63c-1be8-314e-9eee-6073a44d7737 | -2.88996 | -54.12403 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c83b4f0-6367-3974-8b2f-c0b592a1c486 | -2.57189 | -49.11027 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4ba1666-4eca-31e9-846f-91dce26141d6 | -1.49942 | -49.44989 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6be4c6f9-fae7-32bd-895d-3b332c08b770 | -3.81955 | -52.0504 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e24ad21e-5f0f-3481-aa8c-50d813c6afc4 | -2.80759 | -54.1085 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3c225cad-13d9-3eb9-a0bb-db8a913e844f | -3.64428 | -55.50321 | 2026-10-04 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3266fc23-7f86-301e-82bd-c0d15f9ba6e3 | -1.90972 | -47.01634 | 2026-10-04 04:55:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a89e098f-db16-30c8-b283-5b96b0cdf106 | -2.90513 | -54.12647 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01440243-6bca-3e7b-b040-12946055837e | -2.78936 | -54.10089 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccdbc393-45dc-37b7-a7ae-10953183777f | -4.27017 | -50.74737 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8824846d-90b3-3357-a16b-1c3e0753ad22 | -3.18693 | -54.07977 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9dae7ca-9fc9-3429-a372-eea54a5b20f0 | -2.12965 | -50.93483 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6df47908-14e7-39bc-a12c-e10ae659f643 | 2.01491 | -61.09184 | 2026-10-04 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecdea330-b5ad-348a-9f14-c3a34c353992 | -3.07839 | -49.53699 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8460684e-e428-3e7f-8b0f-9d59626c8a67 | -2.90423 | -54.08411 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ed8b5fb-7d23-3cef-8921-94809da3d6eb | -2.8235 | -54.10636 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3f56d1c-b9aa-3559-a018-f8c583f69274 | -2.80684 | -54.11309 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0886b249-0885-3891-a721-fe0355f8b819 | -1.21316 | -55.85681 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 691b9267-e3ec-3a70-8c9a-a7a579d4b3b2 | -4.53635 | -50.77858 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70a5a22c-da80-3a4e-9204-8ad3417df540 | -2.82202 | -54.11556 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0ed06299-5083-3eb7-9098-55de858e3f56 | -1.85877 | -47.97295 | 2026-10-04 04:55:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d800ebf8-7fad-3c3f-8c9f-769c8da1ba4f | -3.27528 | -50.02681 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9c6d7f0-7b8d-3c13-bd08-6e7863fc95c9 | -2.82286 | -54.13462 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b8ffa9b3-f06c-3595-b5bc-f5a9d8565740 | -3.19032 | -57.91985 | 2026-10-04 04:55:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d8f7456c-4a1e-3857-9c19-20223701c5fc | -1.62656 | -55.01794 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d85f8e62-0e15-3a37-94dd-a3c9ebc8aa17 | -3.81494 | -50.84252 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b6f1418-d804-3f32-ad90-9feae019f6d0 | -2.89075 | -54.14309 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca342100-93dd-35f6-87d0-693001b0d092 | -3.08228 | -49.53402 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2edfc4b2-0e43-38d6-b371-4e4a74885a4f | -1.12064 | -54.15076 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d57a41e7-3e10-37d4-9845-0f686e50db2f | -3.29653 | -49.12455 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| efceb9e2-498c-30d3-acb5-aeeeda52406d | -3.07318 | -51.27803 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3c5defa-4a26-3dee-8f93-2702f5de569c | -2.88391 | -54.13722 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README41.md)
