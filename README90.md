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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c70c17b-bd5e-3b24-b015-eaec1658a16a | 1.67545 | -55.61335 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5ddcd8a-01c0-3db7-ae15-17685e7fae45 | 1.68136 | -55.60401 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 505a7fad-33f8-391a-996f-0aa4c1f1ce77 | 0.48314 | -50.7894 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0f7d869-5996-3e7d-a4a0-eb12ab4a911c | 3.05072 | -60.54319 | 2026-10-10 05:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f65458e6-1d82-3ce0-8811-e6b3e5949cbe | 2.41176 | -50.96583 | 2026-10-10 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74694233-7a47-3c1e-a884-2754473a0d7c | 2.81324 | -50.95015 | 2026-10-10 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 293e190d-0d7b-32af-ab07-8c41f0f37aab | 4.68705 | -60.59077 | 2026-10-10 05:01:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06b5fa3a-f8e4-3dd7-af90-6877b30d1817 | 0.95787 | -51.30928 | 2026-10-10 05:01:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| feac95e8-8e48-3b90-aacb-44c574320620 | 2.81717 | -50.95318 | 2026-10-10 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fab33ee-41eb-3913-9e51-2d91baabb7e2 | 0.94899 | -55.75587 | 2026-10-10 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c7945c1-3b8d-3de7-96e9-17fe560ba8b5 | 3.72087 | -51.65613 | 2026-10-10 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44002d73-bfc2-355d-931c-2205e69e7531 | 1.73489 | -55.57045 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 743f682b-2034-36ec-8555-4c6d30203709 | 3.04568 | -60.54398 | 2026-10-10 05:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1967164-5e61-3a12-889c-20119c8fdb0f | 0.99835 | -51.09704 | 2026-10-10 05:01:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cceadf3-3d85-3075-a291-aae53d224f94 | 1.98597 | -60.61634 | 2026-10-10 05:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7e23dc96-e5e4-3666-a65f-58f5573952b5 | 1.7326 | -55.5792 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd7351c0-3b5a-3ad7-a229-628e64bb7dd4 | 3.7405 | -51.60669 | 2026-10-10 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bed1b25-7628-3806-a990-f7c86e6e266d | 3.73719 | -51.60721 | 2026-10-10 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2812f64e-9961-30fe-ae8a-d9197736809c | 0.29317 | -51.40505 | 2026-10-10 05:01:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 655b6b3d-0111-335a-bb1b-05f6ac2fc597 | 2.42685 | -51.40533 | 2026-10-10 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10ae936d-5906-3394-8177-81fbe8bfb6e4 | 1.76072 | -55.53377 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1a530ad-20c8-3dff-855c-55e4f846f5bc | 0.36791 | -50.94724 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a726264d-ac03-3782-b9ac-684860601bc5 | 2.81381 | -50.9537 | 2026-10-10 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b464c0a9-b57a-31f1-9a94-87a4eb11fdd0 | 2.01885 | -61.09606 | 2026-10-10 05:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9396b3ac-46d8-3064-a9e8-1bae477c5ea2 | 2.8166 | -50.94962 | 2026-10-10 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3065714-4ad6-3c7b-8a6d-9f86641efe54 | 0.54072 | -50.88673 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1373592-2dc2-3f87-93a2-0139ac40087c | 0.94371 | -50.20266 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d27b1d9e-2c54-3971-a0a5-09669b44633f | 3.72032 | -51.65268 | 2026-10-10 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fd9a3b2-6883-3c97-8eaf-32998531f8c9 | 1.00174 | -51.0965 | 2026-10-10 05:01:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3730ccf-9c01-3d7e-bb33-9e64664f5ed7 | 1.6725 | -55.61805 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdd001d7-ccfd-3f70-b177-a87d913113c7 | 0.9396 | -50.19934 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 177adacc-4a1d-3d83-bd7e-16abd726db18 | 0.36449 | -50.94777 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8662a6e-8fba-3fad-af9a-f2d78ad00770 | 4.27516 | -60.89379 | 2026-10-10 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb11b136-93f4-3aca-8ccd-8849a6f057c5 | 0.5373 | -50.88726 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3d850cf-beb8-3a53-978c-dca3f7bf80b9 | 1.41233 | -50.67784 | 2026-10-10 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a826c70a-bf86-38ea-b9d1-93eb5118056f | 0.99893 | -51.10066 | 2026-10-10 05:01:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0d721af-4894-34d8-93b1-b4ea5a8d2524 | 1.68431 | -55.59937 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd474896-aba8-3287-b9c1-c46273e6d6f0 | 2.72727 | -60.26743 | 2026-10-10 05:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b15d6267-ba68-3832-8374-0d4dea4446ff | 0.48941 | -50.78461 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf9c0957-f180-368f-af32-5fbd60c8ebcb | 0.42186 | -51.7914 | 2026-10-10 05:01:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fcbcd8a-58ba-3cbb-80e1-b65ad50bbc52 | 1.05775 | -50.03354 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8eebb5d-c623-3dec-877f-2c550d2534ec | 0.94248 | -50.19492 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae787388-ea79-3b76-83bd-8729cedb6071 | 1.98595 | -60.61538 | 2026-10-10 05:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c5b90fe6-6963-3124-9ce7-988ad055d2bc | 3.04522 | -60.54104 | 2026-10-10 05:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e900ae4a-a630-390a-93f3-d4c9ae7bc7dd | 0.47971 | -50.78994 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f678cee2-c2c6-36df-8233-6b9bcb4b26e2 | 1.66849 | -55.6397 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84cb48fe-a9fd-3b78-be51-bcca7ce65d74 | 1.7313 | -55.57101 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fbb9cb8c-8ad0-3c0e-afde-7906dca5094a | 3.97909 | -51.6323 | 2026-10-10 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 534c5949-d07c-3bba-bedc-66baf200b821 | 1.6879 | -55.5988 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 769d25a5-8703-3274-91a2-19903640e17d | 0.29036 | -51.40916 | 2026-10-10 05:01:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41d96b30-b78a-393f-bcee-68b2b4c33870 | 1.67377 | -55.62623 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac89f283-eeb3-352a-9645-80084a034939 | 3.74105 | -51.80472 | 2026-10-10 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae23e37a-037f-337b-9452-8407f68abc6e | 0.29654 | -51.40453 | 2026-10-10 05:01:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b011c3d4-9218-3454-900f-d60dbc3e4475 | 1.03765 | -50.02061 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 238e9bff-e36d-389a-bc1a-5486fe5a2e46 | 1.76724 | -55.52857 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08cbbcf3-d5c5-3706-bea3-207ce9bce38d | 2.73219 | -60.26661 | 2026-10-10 05:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 68251af3-d6ad-3665-8713-824a1ec5fad2 | 1.7744 | -55.52745 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 930f2d73-4cbf-33ef-959f-2311c56bf4aa | 0.47628 | -50.79047 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23031aec-d35b-3545-bd87-83b6d1eff99f | 0.70142 | -51.43274 | 2026-10-10 05:01:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc4bf4a5-e6eb-3c60-a6bc-a7e2889e80b9 | 1.00231 | -51.10012 | 2026-10-10 05:01:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f56f6229-b01f-3f6e-8e07-457734efe141 | 0.29991 | -51.40401 | 2026-10-10 05:01:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 10a68a27-fb1f-3741-8efe-d0f9f997a724 | 0.48598 | -50.78514 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ef38a1a1-3174-3b86-9ea3-a61d57b67d0d | 0.46942 | -50.79155 | 2026-10-10 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0543f0ee-1156-3377-897d-99f480cedc5b | 1.68199 | -55.60811 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c8d9b03-b2f7-3333-b731-2cd9476f5f3f | 2.72644 | -60.26188 | 2026-10-10 05:01:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a436cb1b-2754-36bd-b78b-b78c99be6042 | 3.99507 | -51.62625 | 2026-10-10 05:01:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87f138fa-2de5-349b-af07-c8560254c810 | 1.8167 | -55.51661 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b7a4e44-9081-36f5-98ec-10df8e495d5d | 1.7643 | -55.53321 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d1312bb-849e-3939-9864-9c42240082f6 | 2.01369 | -61.09686 | 2026-10-10 05:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 660ac3d4-a013-33ac-a3f3-75c4b740a221 | 1.41158 | -50.67411 | 2026-10-10 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f065182-65b4-3c96-9f42-c48b1d065d5c | 1.75123 | -55.54363 | 2026-10-10 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 274dadcf-42c4-391b-997a-44c3ecbb2949 | -7.23209 | -44.17959 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 709e708f-a740-3e8c-92db-dc6bf3382f57 | -3.48138 | -55.44091 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7af3f211-6661-3719-9be9-65ea412ac1da | -4.8501 | -42.82407 | 2026-10-10 05:04:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 56517b63-c870-3cff-9c38-d77bc6406922 | -2.39753 | -51.30466 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0883a66d-8171-389d-af9f-727529e4bb20 | -1.64135 | -54.40084 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cd2d184e-d009-3610-ad32-2c455567cacc | -6.37411 | -55.172 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b12c632-683f-3b28-811a-39cb4badc4be | -4.59433 | -55.7201 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e60d6740-bc71-37e7-9b6a-bcdd5adba95b | -5.75223 | -45.13632 | 2026-10-10 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a79c4d7a-0d12-3db4-85d6-3a7ec6efc6df | -6.67489 | -55.09863 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aac41dba-58ac-3970-ba15-1192265bee48 | -6.37246 | -55.16098 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3b249b1-c954-30e2-8455-752831a5561d | -2.93755 | -54.04898 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 291e8a61-2a1f-3d88-a66b-cbbfe80069c3 | -5.72545 | -53.49913 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7b9fb92-09e0-3ba4-a826-5db075b5285c | -5.97555 | -55.34983 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83c6b6e1-055f-32bb-a28d-5aaed3a761e9 | -3.58244 | -54.7169 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2cd1e81-c9ae-3333-af1b-14dde49d6bb7 | -6.08199 | -55.69868 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a54cbef-f693-3eed-8676-91552146fa75 | -0.97013 | -52.44093 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43ad117e-c2fa-36a4-90f5-221d7c087e46 | -7.20907 | -44.34282 | 2026-10-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0f6b609-bdbd-3287-ba63-b74bfc8adf5b | -3.73115 | -59.46547 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aaa85dae-51ab-3d62-8c46-994cc0ab9961 | -2.06177 | -61.1386 | 2026-10-10 05:04:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a32fedc-dc30-3570-a3df-ff61d8635f48 | -3.34533 | -50.40771 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fc4a2dd-eb4b-3878-bfa6-728443f4bc54 | -7.26852 | -57.11328 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 544934fd-d9ac-38f6-9dbe-0931046896da | -5.68448 | -53.47831 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4634ddcc-11fe-3310-bda1-c17c2a68783e | -3.26202 | -54.18879 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a203cef4-95c9-3d32-b72b-0b3637567bf9 | -5.96553 | -55.34822 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3d22277-cf33-3616-bccb-f5c14ec26fd0 | -3.94046 | -56.05323 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 955d51a6-bee4-3491-a724-fb24bb1b61d8 | -3.14641 | -53.71847 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd32d97e-d6d0-3761-87ea-f25d14bf5b05 | -4.22497 | -59.54717 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f831a1af-1bec-388f-869d-2bf4f8965003 | -3.15476 | -50.59328 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16e4fd9f-1dc0-31fc-bea2-3531c823c57b | -8.2391 | -46.42843 | 2026-10-10 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README91.md)
