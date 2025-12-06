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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a75c7041-556a-31bb-bb27-37d62ae0b62b | -1.52211 | -54.42068 | 2025-12-06 05:22:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99495797-887a-31fe-bc7e-57cb63fc9c06 | -2.11099 | -53.57662 | 2025-12-06 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc5f6377-7717-3be0-99ee-9e0584f63ebe | 2.79354 | -61.10117 | 2025-12-06 05:22:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 831851be-0f79-3e40-a65a-223602f02c8e | 2.79765 | -61.10455 | 2025-12-06 05:22:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 75f6ed8a-9e6f-3526-b26d-4953107a7ba2 | 1.98622 | -55.69345 | 2025-12-06 05:22:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d4e64ae-fd1f-3a08-b836-df0c39e20474 | 2.79705 | -61.10064 | 2025-12-06 05:22:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 023f2c52-3da3-3d36-ab28-8edc3d985c2a | 1.98035 | -55.7026 | 2025-12-06 05:22:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73aba4a6-d306-3313-9463-afee7bdd6c54 | -1.51808 | -54.42003 | 2025-12-06 05:22:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 805fc6aa-222c-37ce-b4a7-d85e89ed898a | 0.7891 | -51.96735 | 2025-12-06 05:22:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cbe3042-7f6c-3a02-a80c-1a2348fc3fa8 | 0.45704 | -60.42932 | 2025-12-06 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d8e01d0-e4a6-3b7c-b17e-6aa78ee8c1ff | -2.1134 | -53.57468 | 2025-12-06 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e04887a4-99b2-3d55-b90e-956920fb27be | 1.98979 | -55.69288 | 2025-12-06 05:22:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 47c31050-a50b-3019-98fc-b3ec6646b684 | -2.10846 | -53.5781 | 2025-12-06 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce7e47d4-981b-3085-8b96-44d5d12915aa | -1.99222 | -52.88947 | 2025-12-06 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2874d8aa-54ab-38ec-bdd3-4cb53068f92b | -1.99071 | -52.88741 | 2025-12-06 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 408e7adc-6638-3ba5-b1e7-3487c3ca4c6f | 2.79414 | -61.10508 | 2025-12-06 05:22:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fc7d528b-b6ec-3d62-b816-aec0121b194f | -1.17553 | -53.89062 | 2025-12-06 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb15b8c5-e2e3-3511-a9e8-2ef188f198be | 0.43547 | -50.92495 | 2025-12-06 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9c6756ea-22cf-34d3-a8ef-df76e1135630 | -7.52281 | -63.26076 | 2025-12-06 05:22:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b5dc993-eec4-319d-80e5-9e051ff6711d | 0.3236 | -50.99673 | 2025-12-06 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95a02c6a-1b1d-3a76-85bc-cadbb80760f7 | 1.22388 | -50.91029 | 2025-12-06 05:22:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67676f2f-d24c-3055-a5df-e02c660eba62 | -1.81164 | -54.6501 | 2025-12-06 05:22:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bd7e82b-4110-331e-b2d8-e03cf618c982 | -1.98771 | -52.88872 | 2025-12-06 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8a906f4-0b23-33d5-afa6-4b55464e1ff7 | 0.3227 | -50.99108 | 2025-12-06 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90c59216-d679-31c9-8738-f2d518c6f0b3 | 2.79003 | -61.1017 | 2025-12-06 05:22:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1b722a89-4676-3437-b3fa-e7a64e68d8cf | 1.99693 | -55.69175 | 2025-12-06 05:22:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2a7e264-eac2-33d8-bed7-c4e4b2deae88 | 1.98098 | -55.70662 | 2025-12-06 05:22:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9505b1a2-5abf-39f1-8cae-2fd4572d7f5f | 0.43503 | -50.92216 | 2025-12-06 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f3a3864-fe55-3d67-b2bb-0fe7b010ac88 | 2.5561 | -60.31083 | 2025-12-06 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e83f6f75-a1e7-3806-9db8-22c78a8e1065 | 0.4305 | -50.92572 | 2025-12-06 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 574bb8a1-3de1-349b-b95c-c9e59a557749 | -1.20938 | -53.7295 | 2025-12-06 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 238962a0-f9f2-3efb-95cd-f2b63ec1e4a3 | 2.56573 | -60.3056 | 2025-12-06 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c57ebaec-fde8-3773-ad83-daa1d8248f94 | 1.98328 | -55.69804 | 2025-12-06 05:22:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae9179ae-e04e-38fe-8df7-58e6380cf446 | 0.32765 | -50.99028 | 2025-12-06 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2da73710-2743-3f25-9978-a6b4e7d3bd04 | -19.64444 | -56.83109 | 2025-12-06 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c7dff25a-447a-36c4-b05c-4755613ad72b | -19.65444 | -56.86066 | 2025-12-06 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 35a5ff48-dae8-372a-9ff8-d66d9031c578 | -19.64999 | -56.86004 | 2025-12-06 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 12b86829-40d4-3b18-8d5c-d856ac2764dc | -19.65357 | -56.85828 | 2025-12-06 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 69474814-f59b-3264-b763-2576ffad65e2 | -19.65304 | -56.86291 | 2025-12-06 05:27:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 60747046-f037-3238-9998-ccded6127031 | -3.5361 | -45.4144 | 2025-12-06 05:50:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 48791ee6-8696-3b65-8fd3-bad3ad244c60 | 3.42747 | -51.25222 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc7d74df-6e79-32eb-a746-d240e434af30 | 3.44848 | -51.24844 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9921ed52-bf70-3ed7-bcf1-7fa466c0c1b1 | 3.42047 | -51.25346 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44741807-6db5-3a22-a59b-f67727b10ebb | 3.49047 | -51.24085 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfbf8566-c5de-3f97-9fef-6fec1c85aad1 | 1.98136 | -55.70338 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef2f661b-b15d-3548-af6d-c99f907181a6 | 3.40764 | -51.26263 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b2ab9dc-7704-3fac-b2d0-7aa5d2c48bb5 | 3.45491 | -51.25483 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| effa1155-47bf-3886-b669-1860bf9fdf9e | 1.99062 | -55.69158 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37e76b4c-399a-37ec-bc93-e681014c5038 | 1.9862 | -55.69477 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e005d57f-acc3-394e-8d29-e02457c99a14 | 1.98083 | -55.70012 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25db33e5-03a3-3afb-8490-1291e42776c2 | 3.44963 | -51.25513 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08a995f5-e172-3da5-87de-3529328aec1d | 2.79214 | -61.09921 | 2025-12-06 05:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8cc64803-e72e-328d-bfa4-4e2ca91edc82 | 2.79661 | -61.10308 | 2025-12-06 05:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9bd55492-8455-3065-a9b5-365563f5a014 | 3.45548 | -51.24718 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63c2c31f-7334-3821-9d2b-67d0e0175eea | 3.46652 | -51.23905 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb97e642-013c-3aa7-a982-a9de53245176 | 1.99604 | -55.69059 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7ada871-b7b1-3be9-836e-abd194b5759a | 3.49861 | -51.24624 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b297579-651c-3f4c-ad65-05624c43c2a4 | 1.9819 | -55.70678 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bea57941-b3ee-35ae-b8ab-b3a830d697aa | 1.9819 | -55.70234 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aec257d7-d3ff-3f81-a2f3-6a0114702a13 | 2.55927 | -60.31076 | 2025-12-06 05:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05d7da08-49c9-30fc-8e51-9000da410eb3 | 3.46132 | -51.23924 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6232e0f5-b72b-3992-8086-6e43191dc864 | 1.98571 | -55.69579 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0381ec70-8653-3a87-be85-1efc90ab63a7 | 3.45371 | -51.24817 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae59fd75-c03b-39d7-8449-c9ce11590063 | 1.99708 | -55.69305 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77fe520c-caeb-310a-9669-7a0bf0a831cf | 2.79589 | -61.09862 | 2025-12-06 05:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 28222917-983d-3df7-ab4a-940badd3bd1c | 1.97646 | -55.70761 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba06ce0c-e795-3ad2-80cd-7bf520bc2f5a | 3.46071 | -51.24694 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96644e1a-fe1a-3652-aa75-fee690118934 | 0.45847 | -60.42895 | 2025-12-06 05:50:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d144e7bb-a798-353f-b770-baeeb2843176 | 1.97702 | -55.70651 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| feb5b312-17ff-3cc0-9019-e4c7da57c7ba | 1.99164 | -55.69387 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cf0719e-3537-375a-97ad-b90d793e0bbb | 3.44791 | -51.25607 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56ac5907-6a17-3c7e-a530-03eeeb5ade4c | 3.46833 | -51.23797 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 365a7cb0-78d7-3151-9738-4f2c14c79e97 | 3.41464 | -51.26138 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f5692da-8f5e-3047-ab01-f2ee61d2538a | 3.42164 | -51.26014 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb4f7724-de8a-3c5b-ba3d-fcad566ea8b5 | 1.98247 | -55.7057 | 2025-12-06 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f53fcc34-7b32-3275-af86-d1d99f9cd7c5 | 3.40881 | -51.26929 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 570f96c8-2aef-3077-bf0c-4f65b274e473 | 3.45952 | -51.24028 | 2025-12-06 05:50:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5e4bafd-6578-394e-9463-495780c35265 | -20.92148 | -56.38159 | 2025-12-06 05:57:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8766574-35f8-3a50-935d-31625b705e64 | -20.91451 | -56.38098 | 2025-12-06 05:57:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1f044e5-6dde-36f4-b0e2-b012a83517b6 | 2.79668 | -61.10366 | 2025-12-06 06:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd484239-6d06-3407-9eca-5d7f1452d467 | 2.79602 | -61.09973 | 2025-12-06 06:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc415c79-bdab-3324-b8d2-bda5a5e4708c | 2.80237 | -61.10269 | 2025-12-06 06:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e8b7793-8a63-3b87-ae0c-23b8da659437 | 3.40847 | -51.26305 | 2025-12-06 06:39:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2fb68cef-2ead-3649-a27d-d29a82510aa4 | 3.50943 | -51.25259 | 2025-12-06 06:39:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ebf2bb00-0439-3352-82c1-bd9a6396c1c7 | -3.7133 | -43.6971 | 2025-12-06 06:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 214.7 |
| a6e5e83d-3fc6-3995-85c4-f5a6df875140 | -3.7319 | -43.7193 | 2025-12-06 06:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f66e0d6b-a382-3574-b290-e1bbdbb8ef32 | -3.7132 | -43.7202 | 2025-12-06 06:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 5fb89dc1-5a66-325c-92c8-808dd360c522 | -3.732 | -43.6961 | 2025-12-06 06:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5baacb3f-b225-3b22-977e-ec01edcdea73 | -20.91736 | -56.37345 | 2025-12-06 06:44:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c619009d-41eb-3fd4-957a-f1cacb646afb | -19.66732 | -56.81839 | 2025-12-06 06:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 809e5c43-272d-37fd-b722-f677ef3f1c1f | -19.65251 | -56.85716 | 2025-12-06 06:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 3fc081c7-4d56-3359-a204-7288b87b80bb | -3.7319 | -43.7193 | 2025-12-06 06:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 2767eb26-751b-3966-baea-4f5224121975 | -3.7132 | -43.7202 | 2025-12-06 06:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e639ce35-4511-38aa-ac51-784cd3322533 | -3.7133 | -43.6971 | 2025-12-06 06:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| cb10f1d0-366e-3412-978a-56fd852b0803 | -3.732 | -43.6961 | 2025-12-06 06:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 79bd70ac-3347-309a-8882-8c5912c4e8ac | 2.91788 | -51.01044 | 2025-12-06 12:33:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a8171649-0a8d-3bd8-a297-5bf6b7814182 | 1.9754 | -55.7077 | 2025-12-06 12:33:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| f1039a02-cea8-370f-a0f9-59d9d8078dd7 | -1.39622 | -52.79618 | 2025-12-06 12:33:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0b7cbb21-0e0d-3ff9-b870-f3e60bc9bf75 | -2.62931 | -43.91586 | 2025-12-06 12:33:00 | TERRA_M-T | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 7f37ec5e-0f02-3993-8603-35ef311ad3e1 | -1.41112 | -51.59648 | 2025-12-06 12:33:00 | TERRA_M-T | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |


[Clique aqui para ver as próximas entradas](README10.md)
