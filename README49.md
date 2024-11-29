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
| 7c94a5a2-779e-3ec5-9694-b8de206cf9c0 | -1.23896 | -51.6093 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd02090-6dd5-3b25-97ec-6ab05533c3d9 | -1.08599 | -53.63878 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ca4090e9-2092-38ca-ad4a-dd1b686ade94 | -3.01505 | -47.80099 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04dd7ba5-7b43-3b49-b898-ef295b7377be | -3.26144 | -54.10711 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b525186c-eacf-34c0-a089-cb47e42a9557 | -1.45608 | -51.4998 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a36502c5-84d8-397c-a17d-686e5098971b | -1.89094 | -54.54029 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c631ed74-7fae-356c-9a69-a2c1c328b5b0 | -3.14736 | -53.24759 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb186c47-c42c-3eaf-83bb-b3fb14f531bc | 1.205 | -55.97973 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88875485-e487-3c27-9490-e14a4caee98f | 0.87548 | -50.80837 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c5fc350-ef4a-344a-8a7a-6e94219bbe1c | -2.31777 | -51.95824 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faa962ba-a045-33ba-8273-bfe8d72f175c | -3.7293 | -49.87173 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9815ceca-fcba-33ed-93c0-6c2b60005613 | -3.56013 | -51.03424 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc6e304b-bf37-3c37-a2b5-ec54eb1545fd | -3.31056 | -50.02779 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eeb1d72e-81a7-3fe6-a9ed-f18d2d4f57d8 | -3.08045 | -54.5684 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ef576bf-6b65-390e-8fed-76bd138ced94 | -1.66263 | -52.51633 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55bdba2d-d015-3b16-89b9-9876efda9ee4 | -3.1217 | -53.10569 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe9e9c95-a4bd-3581-a5fd-a2694256dcb3 | -3.37633 | -50.11896 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87416465-0310-33e5-b9fc-da7a9efa1600 | -3.66424 | -54.29388 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec4301df-78ee-360b-ac8c-85d4fc284442 | -1.206 | -53.6791 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3240a46-4ad0-3da8-b277-1bc9ca1517a0 | -2.58753 | -53.98021 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe22235d-1b68-3b32-b331-f4c24fa2ef5d | -3.04845 | -48.49294 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 259d39e3-4271-3a41-8acf-1e6a17e41cbc | -2.82845 | -54.11343 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d49f1735-2888-3267-952f-78b2db20425f | -2.98576 | -53.27905 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1a926db3-fef7-3792-8d80-7583e7f29b34 | -2.3476 | -53.92477 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86586c09-4f8f-35f6-8e16-5852cda13798 | -4.51591 | -48.06436 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a60a130-a2db-3aa1-811c-d78eba24c94f | -3.22697 | -54.17587 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 84fc46a9-48d8-3ae3-8bde-2d2af023272a | -1.19511 | -53.87851 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ca766dfc-4747-3fec-a873-739d8240ba31 | -3.63012 | -51.43226 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3421810b-12d7-360b-975a-a4e07bbfc2e7 | -1.08105 | -53.38856 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0617a427-0e3e-348a-a4e1-61656c8c99d4 | -3.26312 | -54.11797 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 149a49b0-503d-3c1a-8113-d6fa24e4ec34 | -4.28288 | -55.74261 | 2024-11-29 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a1d2813-a2c7-356b-8b6b-802314a09684 | -4.17079 | -48.61615 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fd15db5-2971-3cc3-8d94-84e4f4447cfd | -1.27455 | -51.62592 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f69c255-b72d-3dab-a6cd-93457ff9c99a | -1.37988 | -55.04724 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e15e8b5-bd67-3dbf-aef0-887126bad925 | -2.16226 | -52.7366 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e69ba48b-c1dd-37a1-82af-c8ad8a501d9f | -3.28833 | -53.67493 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb7b3114-63cb-39ce-9664-0d5c771c8c96 | -2.64267 | -47.12741 | 2024-11-29 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db0babaa-4164-3483-b8f3-e2c289efc4d0 | -1.16486 | -53.57013 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c5a879bb-1cf8-3064-a8bc-b1a5d15d06b9 | -3.9657 | -48.06919 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2584c141-831b-3b4b-a095-fe1000fca6dd | -1.14718 | -53.68344 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3763cc7-fb80-3b49-8a6a-ac4ae7113473 | -5.72386 | -43.84134 | 2024-11-29 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3e39602-cc4f-3f1d-a269-b21ddbf91df8 | -2.91524 | -53.90842 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd4427ec-d68c-3e4d-914c-4ad7287792e7 | -1.58568 | -53.83728 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a8647e56-7dda-37e0-86a4-0d1f5ca21aa3 | -3.03459 | -48.50188 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| afe87b61-f941-3879-bbe0-5e8d608f7325 | -1.09512 | -53.21174 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0004de9-7ec0-326f-b0e0-7e48bc6b8c7f | -2.95865 | -53.89048 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51fed07e-54bf-326c-8fa9-4613881661d8 | -1.99341 | -54.90175 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d047a74a-2ad6-35c0-8766-3946f3660259 | -3.34561 | -53.30698 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25cfb1a6-31b3-393f-9f35-a022c817db97 | -2.88291 | -53.30905 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4a20a62-5ea4-38d6-b16f-76321acf8a80 | -3.10049 | -54.02922 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbaa546c-72c5-38a0-bb7c-6c6f3376a038 | -1.30489 | -51.73006 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8325d884-f3fd-3514-816b-fae2d440ddda | -2.73587 | -54.03133 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7e7ab26-03e4-3c09-82b6-e6964092796a | -1.69953 | -52.21354 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfb6c70b-ea10-3b0a-bcdc-881278ef4294 | -1.3038 | -55.74094 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9a387724-b86a-3236-abe0-99cd2f098dc7 | -2.8962 | -53.96527 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eca03a7-6631-3e8c-97be-b2fbe88cf2aa | -1.68373 | -52.53384 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a51db9ff-a12a-3315-8f80-4d63d85a5e88 | -3.57907 | -52.06385 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ed2a9e6-6d8b-3cf9-86e1-9bc4292ba2cb | -4.47816 | -48.11265 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c43ee9fd-90c2-35e1-bd16-17b34c1af56d | -1.66147 | -52.50188 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 775800dd-fbd8-3003-85f5-0808c6e2608f | -2.59334 | -54.07288 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a47bba24-1a66-3b27-9cc8-2c3fd6b9a020 | -2.65259 | -51.77066 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8334a2f6-4586-3702-bcaa-9b7603d025d6 | -2.17377 | -53.27494 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14a6b4fe-dff0-3121-8d66-6e63c405736f | -3.3876 | -50.1104 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9feb43b6-ed97-32c3-b086-6ea39da6abfb | -2.29231 | -50.58682 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 434a409f-8d2a-36c1-aa25-3690ea139ceb | -3.18989 | -54.32582 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 537efaf0-34c5-3921-a40e-dc0f87f9a55d | -1.67816 | -52.52586 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ae90c2b-5a49-32f2-ab5b-e13b5c95a6e0 | -1.63622 | -52.26871 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4fa7da35-a6a6-321a-9da5-a80d69b1b550 | -1.50996 | -52.55701 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 87c1a1b4-2d9e-32c3-ad10-f72a4918bf85 | -3.24533 | -53.64351 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97048bcc-66f3-3b82-a753-8d55e37f25d3 | -1.42702 | -53.3936 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba986f19-f334-3bb1-a868-50a96deed85d | -3.10577 | -53.81831 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc85cddf-c940-3608-a8ca-4bc2518ff362 | -2.86274 | -54.00233 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58fb0283-914e-37ad-9f2c-c235854f5e7b | -5.03699 | -44.17522 | 2024-11-29 04:57:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb6ae86d-aff8-38cb-bda8-82bac03279a2 | -2.56154 | -54.31937 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ef94fe9-b663-3008-8b3c-d992766a8271 | -1.31785 | -51.73574 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e7ccdf5f-e138-3c5d-a72b-d8722c6bd8a0 | -2.8046 | -54.07092 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c59e43c-64fe-346c-b7e5-6ec5f9e898bd | -1.56359 | -52.01154 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13ea6b9a-8bba-3fea-9c07-698fec69c9f5 | -2.81682 | -53.94952 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec32098a-bff2-35b4-b86c-a3d5cef06c93 | -3.08815 | -54.12956 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d5456bf-b865-3d0d-95a9-bff6d2ed0fab | -1.71268 | -52.63138 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1479f23e-f47f-3ac6-a7ef-6b5f40f20895 | -1.99109 | -53.28889 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77bfef7f-a050-3bef-94f7-8130cc1515cf | -2.96196 | -53.89099 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b8cb54b7-ad4a-3f7f-8527-533f6a042b92 | -2.69771 | -51.36539 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df29a106-5eb9-3cfc-abce-a00e67c43a6f | -3.67358 | -54.45111 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89ac8cac-cfe3-32a6-bfc2-13aea183f48a | -3.52812 | -51.24712 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ba5f5d3-4656-3f9a-b748-4e79282aa792 | -3.02907 | -54.04931 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2735df57-b92a-3402-bf41-cf354a8123ae | -3.91821 | -53.67166 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 632fd668-2f84-3433-883c-55e8cfb5f7b4 | -4.18202 | -48.62544 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b9e4691-ac9e-3cfc-a2f2-23f1b0720fe6 | -4.2678 | -54.71885 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d774d2c-9d8d-32c0-81da-921d89e1daef | 0.10329 | -49.84441 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ae9e910-c81d-35b9-825b-212308689fdc | -3.77971 | -46.69408 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e389ed3-a3da-3312-838f-34282d19659f | -1.62244 | -47.50571 | 2024-11-29 04:57:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4eba1ec-0df8-38ab-a158-b1fe8d1b7179 | -1.10202 | -53.40582 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b494fa96-19b2-339d-b802-9a3ad3d7b0dc | -0.95737 | -51.65528 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 17b80105-d575-33b6-94a9-f68029d7e8eb | -3.68753 | -50.2312 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db47d2b5-87cf-32c4-b621-5cb4f915ddb8 | -1.14919 | -51.68774 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b3e21bb-f082-3b5a-818e-61ae48f6c288 | -3.26859 | -53.8231 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23a44a89-c05e-304d-b7f8-de8f23de0210 | -4.02173 | -46.99859 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b3ade37-281d-3bd3-ac84-364fe358ddaf | -2.54585 | -53.98421 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96eb838f-04ea-300b-878e-8a9d5f2299c5 | -2.40663 | -53.85302 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README50.md)
