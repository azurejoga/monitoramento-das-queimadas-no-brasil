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

## Dados Diários - Página 379

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f555ca7-95d0-3156-95a9-83324907f17c | -2.93016 | -58.37582 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e727ec07-3bd4-392b-a16d-b20fafcdc9c1 | -2.75266 | -54.0382 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ce842a87-27d9-3fac-84e6-82d37d65e213 | -3.3085 | -54.02592 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 95201fa2-21b0-3c8c-b724-dbfa5fd0e208 | -1.11687 | -52.25993 | 2026-10-08 16:39:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0b4cb7f3-d463-3b3a-81d0-c35a6117e5aa | -3.00076 | -54.05467 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2b4efb0c-c38a-38a9-b040-765d89f0a7d5 | -3.45175 | -59.54991 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| aacc3fed-eb1c-3744-b03b-626a69287bbf | -3.92853 | -54.57657 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c28367ad-eef2-3029-aea3-d582598fbde5 | -5.3478 | -45.71796 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 4e4ae6ad-35d8-3434-9006-9aa4d8f0fd8a | -6.19611 | -52.8681 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| de96768b-2041-39f6-bc8c-ba908c1b2dea | -2.75047 | -56.60794 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6df0ffd4-b40f-351f-9a08-068df6aa52b5 | -1.33229 | -52.4431 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3b540130-fa50-379e-aa2d-3d6f32def0e5 | -3.00371 | -54.08254 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| c45e62f3-3e93-3881-8d29-19855b19e99d | -5.88831 | -45.96845 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4106952a-cf9e-31fa-b7e0-fce6d66fbe85 | -5.35102 | -45.96189 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 21509fb1-33f7-3e26-8c62-2e64ec784c2c | -5.51367 | -42.83048 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 76dd69f3-b266-385d-94c1-c01241b039cf | -6.1242 | -51.94775 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0569cfa4-07f3-3759-a1e9-64a1ae6e709e | -4.39208 | -56.04559 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3d5c718a-3940-3fab-8b11-6302b147ada8 | -3.51057 | -43.83426 | 2026-10-08 16:39:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 24df0c3e-115b-3f6a-a715-aca7669dfbcf | -5.61872 | -43.04173 | 2026-10-08 16:39:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| adcd71bb-42f9-3199-9981-ec50482bd2f0 | -2.46597 | -56.08332 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| aef6006a-0bbb-387b-a2c7-5fc3a5203065 | -3.80021 | -41.64529 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 3b91ccef-9b2f-3360-91b6-3da6dbaffc56 | -1.549 | -52.75666 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 900ff4b7-c394-3d13-9a35-14556a671af7 | -2.70895 | -56.54684 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61dc3a33-6791-33c8-8f8f-762f7629af13 | -3.04857 | -59.36128 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6e7b66b0-cd32-3055-a44d-ff05ae2e5b22 | -5.88883 | -45.9719 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d15967d9-cfc8-387b-bea6-b839310388cf | -2.96713 | -57.77056 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 912e7392-0c0f-3672-afc7-c16ce72d326e | -1.28413 | -55.41511 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 21a0133e-d5b7-3973-949a-5b6b4bb9cd0c | -3.9469 | -55.84372 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1226cd7c-bd2a-326e-8406-92a7ce4cc7be | -6.22409 | -53.27785 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad6ad580-6b7a-3b72-b62b-163ed1f8c737 | -3.01711 | -51.02003 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3f7687f5-e465-3995-a09b-b42baa3b44a7 | -6.04183 | -53.48632 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| fc674a91-1384-35c1-ba4f-0a3b357dea7b | -4.18676 | -44.45084 | 2026-10-08 16:39:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 832d1739-06fa-3c18-9565-e415d7758267 | -3.10215 | -53.95822 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| e479af6e-a3d2-38c9-aa5c-098ac012cbe7 | 0.52822 | -50.77204 | 2026-10-08 16:39:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0b0bc558-ae50-34f1-a740-f9c6062e2472 | -3.95009 | -56.02336 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 10f775ac-71ed-32c7-9519-ee8f3d87ffee | -4.08771 | -44.10297 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 8dcd597e-a991-3767-80bf-fe197b8ddc85 | -1.3264 | -56.4176 | 2026-10-08 16:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 45f7a8cb-c991-3194-8ec3-926872a3ce38 | -0.34 | -52.0359 | 2026-10-08 16:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 821eb1d4-a386-34bf-a542-11aa4ef93930 | -1.856 | -57.057 | 2026-10-08 16:40:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| bd90778d-1bd4-32cf-8208-32365944853c | -1.4118 | -48.9318 | 2026-10-08 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 3d803f1d-8f61-3162-8902-d7bbb375e049 | -12.1549 | -44.7314 | 2026-10-08 16:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 7c7836f6-12c1-38c1-9ea6-b048e769e0ee | -6.6899 | -45.3746 | 2026-10-08 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 51a9f98d-f467-32df-84a5-21391573b32f | -9.6758 | -65.0214 | 2026-10-08 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 29d64123-0306-3208-aa10-e703bab32a27 | -8.9501 | -45.1334 | 2026-10-08 16:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 205.1 |
| 0c9aae89-5e5c-3b1a-b2d9-fe903dea5839 | -12.1922 | -44.7953 | 2026-10-08 16:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 88b58da0-59ad-3a61-b7dc-a81f914187f1 | -10.9953 | -45.4068 | 2026-10-08 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| dc0a8ab4-28c6-38d1-a211-f78b9e24ec37 | -2.572 | -56.1646 | 2026-10-08 16:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 314.9 |
| ca13a483-067b-3071-a809-c9302075db66 | -11.2295 | -46.2403 | 2026-10-08 16:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| a74235d2-6073-3516-bcda-d745614705b0 | -3.0447 | -57.4851 | 2026-10-08 16:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 9741bcf0-8ed9-3305-adbf-bbda5c043b04 | -0.3952 | -52.0152 | 2026-10-08 16:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 4d749971-2c62-376e-be3d-c71f3a067f1d | -12.232 | -44.7194 | 2026-10-08 16:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 47085f3c-e871-3b66-b185-e55c7a8f0423 | -12.1545 | -44.7547 | 2026-10-08 16:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 209.5 |
| 67467384-fb4c-3c54-9580-6328bc0963c6 | -9.6572 | -65.022 | 2026-10-08 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 0c1747a1-9b93-30cb-8e54-219991ff8460 | -3.3912 | -58.0017 | 2026-10-08 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ea967736-e313-3345-9b78-9c3428eb770f | -9.6757 | -65.0401 | 2026-10-08 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 3db8e64d-5590-301c-b0ec-9ee95f755430 | 4.44584 | -60.94896 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e6904aa6-9974-38c9-a55d-7325d17ab1cc | 1.66765 | -55.8092 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| eab2ffc5-c3f0-3a2e-8826-3678f77dc17a | 4.44336 | -60.92503 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 291d3ba1-a437-3850-85a0-48b261b5bba7 | 3.14608 | -51.50368 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3084cd62-178d-3143-a3c3-12036d0df823 | 4.44526 | -60.92598 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5fbd464f-4c3e-30bf-b9b0-9acba0cfc88d | 1.71012 | -55.60089 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d5d6256b-1e5c-35c6-a95e-4b3ff8d73c05 | 3.73757 | -51.6214 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2a41e413-2ded-3647-b017-21a0f4371be8 | 3.74253 | -51.61345 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9d79e240-3577-3c24-9100-1fa1e2414455 | 0.30509 | -60.43831 | 2026-10-08 16:41:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d71557d0-4d5f-37df-846b-c4a5c33c1441 | 1.66028 | -55.79838 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5405ed23-c890-396c-839a-8997f6b3e1d1 | 3.51533 | -51.2504 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc74d669-4fd5-3ad1-b2b0-57b1f67f04a5 | 3.52186 | -51.25563 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e7ada277-da16-33bd-b75f-6e253b3ab656 | 2.76063 | -60.00762 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 18.9 |
| d003b799-41a5-371d-91f2-fb119a2d8fd3 | 1.76177 | -55.54464 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dfc5c376-ae50-36e8-ab3a-bf0b730d6cc9 | 3.55097 | -51.28123 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 1b832c8f-e239-312c-bdc0-3c8cd21db4aa | 3.7983 | -60.42284 | 2026-10-08 16:41:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3327e402-b450-3160-a715-a168432cb3eb | 2.58116 | -60.12235 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a9c684e1-9138-3250-840a-4c2627e385fb | 2.32417 | -50.81551 | 2026-10-08 16:41:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5e0fb6d0-2167-3cdb-938a-619a03144ec1 | 1.98184 | -55.90491 | 2026-10-08 16:41:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 88b385ba-b91d-30e9-a19f-f9b147a1f47a | 2.11283 | -50.82605 | 2026-10-08 16:41:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| da986308-4202-3bb3-8617-8f1c07bc9d41 | 1.69417 | -55.62277 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| ca129bf3-8c9d-3574-935b-4756d0febb4f | 1.7044 | -55.6055 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 85e6b618-f28a-35e1-b8fe-837528c6e090 | 1.31258 | -50.87631 | 2026-10-08 16:41:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bc6657b7-6e6d-31ab-8403-e8acc4248bc1 | 0.09809 | -60.63224 | 2026-10-08 16:41:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 317fec33-98cb-38f9-a6b7-c846fcd70d72 | 3.4892 | -51.46352 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ad36e915-cbb4-3d56-8e66-08c999ceb616 | 2.74986 | -60.03252 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 764c2864-ee0e-3e60-9ca7-3877d79e9c6d | 3.31346 | -60.06308 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 9fdba59f-8382-34f6-8914-6d88bb7286a0 | 1.31322 | -50.87215 | 2026-10-08 16:41:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 225a5bc7-6eda-3b57-ab1c-f94833a0e27d | 3.79791 | -60.42171 | 2026-10-08 16:41:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 57952caf-b3c4-3d9c-8ef6-7156d0b7de8a | 2.09666 | -50.83604 | 2026-10-08 16:41:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 02a17fcc-0a0d-3e5a-972f-50f58d390256 | 1.66832 | -55.81128 | 2026-10-08 16:41:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ca37deb7-2aed-3023-9776-d12f75c34f79 | 3.74187 | -51.61771 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4e0616c5-880a-32aa-b13d-181872f646ef | 4.27186 | -60.10895 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ae94ca52-b9db-3c6d-97c9-b37e2692634b | 3.51109 | -51.25396 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8b15c263-efa8-3697-b115-818fae733043 | 4.27834 | -60.3512 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0251e5e3-25e8-3ab8-8119-4642058f5e4d | 4.68588 | -60.57909 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 07cbf84a-5c88-3c71-ab82-ffdb4a7eb77c | 2.74897 | -60.03784 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 84192df0-ae44-3f1a-93a7-606c2188f5f0 | 3.74237 | -51.61644 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e471942d-fab8-326c-8140-90551b198a23 | 3.52121 | -51.25974 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9f12cb5c-d02a-34a9-86d9-f0b97828550a | 3.61156 | -61.07077 | 2026-10-08 16:41:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2f6bfcc2-730a-35cf-99f7-c47e93687153 | 2.52689 | -50.8377 | 2026-10-08 16:41:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 335e99c2-07e7-3479-9b38-6678b56ee989 | 1.66924 | -55.80564 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 82a36fc1-e64b-371f-a8b7-6f37461fb9dc | 1.70524 | -55.60014 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 04db8609-8cc1-3449-b498-f536780b1b1f | 2.0022 | -55.87362 | 2026-10-08 16:41:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0fd07f49-e8ef-3d98-8bd1-d83f80f8746e | 3.54083 | -51.27543 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |


[Clique aqui para ver as próximas entradas](README380.md)
