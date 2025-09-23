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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a0e6916-a8b9-3259-a234-902cf51398d1 | -15.5871 | -42.3997 | 2025-09-23 02:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| fe9adcab-51b6-3797-93c5-3789fa202566 | -12.7755 | -57.8799 | 2025-09-23 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 345.1 |
| 194b4a34-0054-3e6f-90f0-3ef977ab1259 | -12.7568 | -57.8616 | 2025-09-23 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 93001aae-a141-3a82-80e5-7daab27831c1 | -6.3412 | -56.2009 | 2025-09-23 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 8ea74a49-aee6-38f7-bc0c-cc0073bab731 | -12.7753 | -57.8999 | 2025-09-23 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 456b4590-bdf6-3cb2-af46-e32ab44911fd | -12.7758 | -57.86 | 2025-09-23 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 219.1 |
| 00e81ed9-5cd8-3de1-a123-1f4f3bfc813f | -12.7563 | -57.9015 | 2025-09-23 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 733b040d-2bd3-3758-8911-0c82b12c0efb | -11.6249 | -52.8416 | 2025-09-23 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 79a416b5-c978-3b53-84c9-5981d293964a | -11.6247 | -52.8624 | 2025-09-23 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 19e1592c-e32b-3236-aad0-d1494c665a12 | -7.8887 | -44.0281 | 2025-09-23 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| fc7b9c75-e5d6-3922-92c2-f4686ee1a078 | -12.7565 | -57.8815 | 2025-09-23 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 282.1 |
| 858a23a7-0240-367c-ac66-acd2b33ccfa7 | -6.3412 | -56.2009 | 2025-09-23 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b686d700-1493-390c-bd89-3f8fe2007f84 | -11.6436 | -52.8605 | 2025-09-23 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5096b427-2a5c-3eb6-90ba-7602c45ee467 | -11.8946 | -41.2612 | 2025-09-23 02:40:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 34c3bb94-d43c-30df-ae4b-17d6c558d4f4 | -8.5179 | -44.9749 | 2025-09-23 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 455d3c66-d0bb-3efc-a9d9-ebae3baafb33 | -15.5871 | -42.3997 | 2025-09-23 02:40:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 88643ed9-e2e3-364d-841e-5a0a975ddb2f | -11.6247 | -52.8624 | 2025-09-23 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c83b59b2-9072-36e9-b81f-7b1ef5d307da | -11.6249 | -52.8416 | 2025-09-23 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| fd7f165d-6065-35c3-932f-29b50e700672 | -11.6247 | -52.8624 | 2025-09-23 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f078d77d-ce85-3c3c-8c12-646ac8b0cc09 | -6.3412 | -56.2009 | 2025-09-23 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| bb165af9-e9af-30e6-9c75-fa886abfbaba | -11.8946 | -41.2612 | 2025-09-23 02:50:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 7ea61053-1e42-3751-bac2-3dc61fb2411f | -12.7568 | -57.8616 | 2025-09-23 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 6346d6fc-3276-33d8-884f-a30eb9a47099 | -12.7755 | -57.8799 | 2025-09-23 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 8c8cf3c0-bf04-325c-b293-11592f38d075 | -12.7758 | -57.86 | 2025-09-23 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| a2a76f1b-f0d0-34d1-a1c8-9ea1c391bcd1 | -12.7565 | -57.8815 | 2025-09-23 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 8d7258c1-3443-392d-97d1-4b75c378708c | -11.6249 | -52.8416 | 2025-09-23 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3c9fcb54-57ea-3ec3-b282-a1569420badc | -15.5871 | -42.3997 | 2025-09-23 03:00:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 78c71d93-6414-3413-94a7-89918c3d16aa | -6.3412 | -56.2009 | 2025-09-23 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 44824570-2105-3316-8022-1a2a35bbb82d | -6.3412 | -56.2009 | 2025-09-23 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ec3c6443-5854-3a81-80a6-3e1d8c377618 | -6.3412 | -56.2009 | 2025-09-23 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| dd5dfde4-4ff0-36a3-911f-8c991b1117ec | -15.5871 | -42.3997 | 2025-09-23 03:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b6a34c64-be39-3840-9d95-b0b91e51e942 | -3.65479 | -40.35057 | 2025-09-23 03:28:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c8d81c9c-b4ff-34d5-990e-1153e3f4b55e | -3.65425 | -40.35372 | 2025-09-23 03:28:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 74cbb436-3fbd-35da-aaf3-3a7dd3d38886 | -4.62081 | -38.69413 | 2025-09-23 03:28:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bce7ab4b-4111-3182-8a03-bb34cc38735e | -3.80956 | -41.56303 | 2025-09-23 03:28:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b7f5b9cf-18b8-3680-a5a6-80f43012dab5 | -3.81021 | -41.5592 | 2025-09-23 03:28:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| cffeaf76-00ee-3de0-adee-93766cdc5978 | -3.65375 | -40.35288 | 2025-09-23 03:28:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d3373d7f-447b-32c5-a9a0-ea221cfae281 | -12.7378 | -57.8632 | 2025-09-23 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 1fce3378-c596-3033-a538-4f1b55390793 | -12.7568 | -57.8616 | 2025-09-23 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| a2a6bba7-d0dc-396b-9d54-b9ac20f83a1d | -12.7565 | -57.8815 | 2025-09-23 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 07ae5264-c2d2-318a-b4ad-008fd69aeb02 | -15.5871 | -42.3997 | 2025-09-23 03:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 08193e2e-f65d-3c95-a25d-fa8b77dc352a | -12.7375 | -57.8831 | 2025-09-23 03:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 302c6317-d329-3d91-bc61-c94f14e5f4bf | -6.3412 | -56.2009 | 2025-09-23 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b0ec905f-78c7-3708-9c53-f8ff7ca1a9c6 | -7.04258 | -41.99588 | 2025-09-23 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74f818c4-5eb7-33d8-8198-6aa2f075e730 | -7.8951 | -44.02301 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9a2a6639-158d-396e-a7fc-35eaaf888a0d | -4.77908 | -42.75893 | 2025-09-23 03:30:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7d38c512-9ce5-3c12-a9b4-98f2ac9a9447 | -5.10499 | -43.16506 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad44576a-fc9b-3f31-86c7-223fed8829c2 | -5.94406 | -45.39521 | 2025-09-23 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1e746ae-2a3a-3e5b-96c6-c3d0bd259c82 | -5.23406 | -43.69353 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37eff7fe-fe9b-3bd6-a355-bfd3d54b06fa | -7.03818 | -34.91501 | 2025-09-23 03:30:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 820f7827-071a-3eaf-8d6a-c80b68da157e | -7.88187 | -44.02546 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| aaf9bec9-8c2b-30bc-af8a-c3158b296ae8 | -4.01314 | -43.26724 | 2025-09-23 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d63004a6-82a9-394c-8779-9386be16367d | -4.39824 | -44.37517 | 2025-09-23 03:30:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ff0337e-8a2f-3aff-9685-6d2cabde7e86 | -8.14039 | -44.46727 | 2025-09-23 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 928b3295-81b5-3d7a-88e3-5efe9297f238 | -6.4111 | -43.77039 | 2025-09-23 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd051dca-5623-348b-8505-9c0924ff7cc6 | -4.77829 | -42.7634 | 2025-09-23 03:30:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 78d458bc-981c-3c84-ac39-36572a038a6f | -7.88277 | -44.02069 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 42271e9d-e43f-3b16-8d3b-575ac1b6976b | -8.52591 | -44.94522 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a2681bd0-21ee-3f0a-8d16-98c9f53096e2 | -8.52587 | -44.94727 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c621533d-cd1a-32e1-a095-7ec1fee3c233 | -8.52484 | -44.95253 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2437758d-2e8a-35dc-a5ce-1c4099c0bf51 | -7.22683 | -45.17632 | 2025-09-23 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01088044-27bf-30b4-adab-da0fbca75f34 | -4.40597 | -44.37029 | 2025-09-23 03:30:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 343ee9fe-7ca7-386d-b81c-d380649d2447 | -6.41338 | -43.76835 | 2025-09-23 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 908b3f33-5e0c-356f-be89-57e098bbdd02 | -4.78349 | -42.76899 | 2025-09-23 03:30:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d016398b-107a-362d-864b-7d35b1d674fd | -4.00825 | -43.27231 | 2025-09-23 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f22fa65f-3344-30ff-9b40-49153066c143 | -10.09003 | -39.55795 | 2025-09-23 03:30:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66419893-6fb6-30d3-9fee-dfa84aa3bd8d | -5.10398 | -43.17168 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9134837-8b8a-3fc7-bbae-531edbde622e | -5.64437 | -42.59706 | 2025-09-23 03:30:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1b5d881f-dbef-3d8c-8143-983ca137b8b9 | -7.88982 | -44.01718 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3fd8e147-a547-3b7d-a437-0bfe033e7110 | -8.52162 | -44.96889 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9292cff5-b9bf-3990-a83a-65ea59450d64 | -4.01538 | -43.26836 | 2025-09-23 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6469c1f-b14e-32e2-9f07-906fafdeb767 | -9.85465 | -37.34502 | 2025-09-23 03:30:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d9bbb288-87d0-39c6-bf32-7315e6c867a8 | -8.13943 | -44.47235 | 2025-09-23 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 689b7433-d5a2-30d0-8bb1-6c03065dc8f4 | -7.23009 | -45.17853 | 2025-09-23 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c15199c3-16c0-3c8d-9a78-c43edf3c907c | -6.59598 | -44.5454 | 2025-09-23 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d48c3216-ceef-35a9-a9fc-ddcb74d9130a | -7.28735 | -44.15432 | 2025-09-23 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 97a115f2-7ce7-38fd-9bb8-a63aee3f62e9 | -5.12095 | -40.74472 | 2025-09-23 03:30:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d62a6aee-380b-3216-9d09-fa7ec649a7f0 | -7.1848 | -39.66675 | 2025-09-23 03:30:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2443ff14-ef2c-309a-9788-21f9a8eee687 | -4.9675 | -43.23034 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 491b3112-4b2b-3ff1-9a33-2e7905ed6f7c | -6.4121 | -43.76495 | 2025-09-23 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09be03e3-3bbe-3273-89ef-8ed5d98c841e | -7.03467 | -34.91444 | 2025-09-23 03:30:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d0f0757f-b080-3390-a843-0c36acf780a3 | -6.26214 | -45.33292 | 2025-09-23 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 406c5104-a902-3de2-ba12-d062f236c9c3 | -5.65103 | -42.59968 | 2025-09-23 03:30:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 939a82ea-8fce-39cb-a037-9cce49400bb5 | -5.68222 | -41.39893 | 2025-09-23 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| accccfc7-d8ff-31ef-978b-6b96d5fd14a6 | -8.5218 | -44.96691 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eb6ac34d-5ba9-3a9f-b137-7bd080052e2b | -7.04272 | -41.99565 | 2025-09-23 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f7c3cc0b-d6b9-3c01-8dc2-7a418a995af7 | -5.65026 | -42.59792 | 2025-09-23 03:30:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 87c2b3aa-1b60-3b65-a2b5-cafd26a04bff | -5.1042 | -43.16964 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f401cd3-d6c5-3752-a52f-849ccdbe585b | -7.03754 | -34.919 | 2025-09-23 03:30:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| badfcbd9-6654-37e5-8b47-79fbfe7d4bbd | -7.49957 | -35.24923 | 2025-09-23 03:30:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4288a540-cdf2-3157-8f50-96f6960d4e78 | -4.78428 | -42.7645 | 2025-09-23 03:30:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bbb49bfa-b99a-3c17-be11-1339862e0a1c | -5.12619 | -40.74554 | 2025-09-23 03:30:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a885168-162e-3591-8eb2-3b7e4af2c784 | -5.64513 | -42.5989 | 2025-09-23 03:30:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5d3bf3f6-28b0-3ae5-b7cf-c215340405ea | -8.51981 | -44.9774 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 668a2e34-5fe3-3847-8c47-087e0847b777 | -8.76533 | -38.97644 | 2025-09-23 03:30:00 | NOAA-21 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52c564c6-6894-3632-afe8-d8df752834d8 | -4.76351 | -43.6347 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 659d406a-f539-3ce0-8fad-450ced26e1be | -9.30337 | -35.69858 | 2025-09-23 03:30:00 | NOAA-21 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 421f59bb-70ab-3573-b218-345881c07fc8 | -7.03882 | -34.91105 | 2025-09-23 03:30:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c3febf77-7527-3061-a3c0-2596f824da31 | -8.52717 | -44.97392 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c9bbb51-bc41-3c81-858a-2d0f465f207d | -7.88803 | -44.02664 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README5.md)
