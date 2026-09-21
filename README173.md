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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 258ddd9c-cbfd-3467-b113-8575706050dd | -5.40056 | -45.70253 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a17da11c-4f9d-3eed-a77d-5c9593c6b7f0 | -6.92075 | -42.94234 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 29f1b710-a544-3ec8-8b96-c16100e6cc38 | -6.47125 | -48.43725 | 2026-09-21 16:03:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 17.9 |
| cd0abe94-1ad9-31c6-a95a-6c42e6ee85a6 | -7.86945 | -49.30484 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4e5f389b-f2e8-37b1-b6da-91e413118a51 | -7.75202 | -46.70843 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1907b60-20e7-340b-b2f6-eb4bd4a618c0 | -5.14651 | -38.13392 | 2026-09-21 16:03:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 430fc744-cf9f-3c62-8d58-85ae514dcdf4 | -5.85659 | -49.78459 | 2026-09-21 16:03:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c0ac2432-0bba-30ff-97a4-01ddaf297f22 | -2.47544 | -49.81983 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 793897fe-6801-3211-a30c-f04caf31788a | -2.46808 | -49.81178 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fab6f525-5c80-3b53-b6bd-f72b477cc956 | -7.41929 | -44.79282 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e48e7e32-9caa-391b-b0aa-0e1c5419783f | -6.83264 | -45.5578 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a7323961-f2d4-39c7-af03-45badce12b5d | -6.21053 | -45.35131 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 243bad12-31a3-3fe5-82c5-7aff6443af34 | -7.73435 | -43.89902 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d8551171-4832-358a-a075-a74ce7f93af3 | -6.85289 | -45.52767 | 2026-09-21 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 705cb1ca-d829-3e3a-b48a-ce751f32b272 | -4.84948 | -40.52396 | 2026-09-21 16:03:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 640101e0-e902-304e-8179-663173a52934 | -7.13141 | -42.07309 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9effe51d-a05d-334a-a1ec-0ce9dc991aaf | -7.57693 | -44.71326 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 255e3c13-014b-3727-b41d-1b9b2315a64a | -2.78285 | -51.35607 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 8d57789f-9d54-38f9-8c1b-b38d6b20b656 | -8.49861 | -47.03378 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| cc4e543a-2e64-39cd-9467-b0936c9939b5 | -6.31479 | -47.62141 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cd272990-1c32-3b1d-b8a7-a98a0c0b5c13 | -8.45523 | -48.45228 | 2026-09-21 16:03:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cc18b067-2e59-355f-abd5-82516975078b | -8.43027 | -46.85359 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eabe96ee-5e71-3f4b-8a87-7ea1b63a03e7 | -5.82037 | -47.79211 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| deacd4f0-c369-373c-9471-2b1a20869502 | -7.43936 | -44.76736 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8fb88a0f-91e9-3384-96bc-341478b3411e | -8.26591 | -47.5693 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c58f1ff8-6487-3a3f-8fb6-c2de6d789587 | -5.82362 | -47.77339 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f8a86e9b-618a-35af-bec8-57cff58e0f3c | -3.87875 | -43.60841 | 2026-09-21 16:03:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d68917ce-c9ac-362c-bbb8-efc938bbd70c | -6.9872 | -44.7121 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 7149a558-4e7b-32c5-a979-a01f749164a9 | -7.50864 | -46.22831 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 611af1f3-7b48-30e3-92cd-7d81653756bf | -6.95143 | -44.99934 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2d7c952d-4456-3894-80ab-25e606711c62 | -6.91734 | -38.73704 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fdd84413-4e9b-38c4-9043-e476e6ddbfb5 | -3.8381 | -40.60578 | 2026-09-21 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 974d82e4-d076-31c7-a91c-de56c1818afc | -4.81984 | -43.63609 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c03920cf-7f69-3b73-a1e6-f1bf9b358677 | -4.82256 | -42.9093 | 2026-09-21 16:03:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b5ca4d70-6edf-3ba1-b335-6a0233f63082 | -3.86674 | -38.54654 | 2026-09-21 16:03:00 | NOAA-21 | PACATUBA | CEARÁ | Brasil | 2309706 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f7244e08-df63-36c9-8331-393816af09b7 | -8.4188 | -47.5295 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55bc67ec-e0ff-3292-986a-95ea830695ba | -1.15118 | -46.76507 | 2026-09-21 16:03:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 9086c787-d18a-33ac-be21-89dc975e4411 | -6.38525 | -43.81771 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f3aa84c9-5393-3201-b30d-c0113145f6b7 | -8.63831 | -47.36551 | 2026-09-21 16:03:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8e304102-f74d-3521-9201-5c711ac46b56 | -3.70538 | -38.84956 | 2026-09-21 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 98a2c724-1d54-3349-baea-d7c21e7a0ab4 | -7.51288 | -46.2216 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 688def9a-78a3-36bf-b876-0d768f819bba | -5.74848 | -43.72269 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| d6d00652-e251-3689-9404-aa61f9d1da49 | -6.98155 | -47.46812 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fa55395a-638e-3011-bc3d-2fb339df051d | -7.73584 | -49.39054 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 766ca5cb-84f9-3341-b7af-475f32c4463b | -6.36144 | -43.36095 | 2026-09-21 16:03:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9ad65487-ef67-394a-829a-498211767b60 | -7.15713 | -42.08878 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 23f96b7c-27b9-3adb-863d-087e440e0ff9 | -1.37043 | -49.32758 | 2026-09-21 16:03:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a4d8ad3f-d868-3616-a81c-dbb1fefffd0d | -7.94578 | -44.80511 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 29c28c3d-0902-3b39-9526-6a39bfcb6359 | -3.81735 | -38.46617 | 2026-09-21 16:03:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2cf34ebb-2117-3110-bbca-4dd022e62b60 | -8.80542 | -48.75396 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 1b3fc2f3-20cb-3048-ad75-a341c986ff60 | -7.11681 | -48.43426 | 2026-09-21 16:03:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ba64688-c941-3f3b-9bb4-cec3e3efb2b1 | -3.5838 | -40.31383 | 2026-09-21 16:03:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| bb6d5372-4178-3100-bde9-715148fe2da4 | -3.32889 | -42.55311 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 313aa890-5cda-3821-b4f2-352f24f5954f | -6.56511 | -45.56843 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 29e72546-d4c4-3699-a3c8-dbdc4c8f271a | -7.1687 | -37.7248 | 2026-09-21 16:03:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 010acb63-6908-32fc-96c8-2d12676eb6e4 | -6.29635 | -41.76189 | 2026-09-21 16:03:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| a4d6994f-f20b-31da-8f4f-800c0e48ba54 | -4.11387 | -46.39817 | 2026-09-21 16:03:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 49750f4e-ec8e-3273-803c-bd179c92b8bf | -7.72761 | -43.89543 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7f71f2b4-233b-3b87-a486-4f4c243d459a | -3.44285 | -50.61136 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 341db71e-9f7f-3cc8-b1b9-56175232517f | -6.93777 | -42.91825 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 49c0be3c-2902-3948-b392-ef6fd79609ae | -4.26606 | -41.7461 | 2026-09-21 16:03:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| db903226-3eb9-3136-b345-5d36cf0b7d10 | -8.31318 | -45.98387 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 38fd1921-3677-31fe-a5a3-32c5e0dccc07 | -3.16773 | -42.5847 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a0daacc5-9432-3cc3-a0c3-85ec0d0dcee8 | -3.86891 | -38.40561 | 2026-09-21 16:03:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4d6f1e1b-d31b-31e1-8bb5-3317a70f6120 | -4.20845 | -44.66979 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| acb80ce1-183c-300e-b71d-d49ac219ac35 | -5.74208 | -43.70802 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e6e445d7-a248-300a-b250-d7c9d867b9e4 | -1.73934 | -47.7547 | 2026-09-21 16:03:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 05e2380e-f440-339c-aeda-109f4646ef7f | -6.84085 | -43.76932 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d94f29d7-d6ad-3667-8d23-5fa1aeb306ee | -4.19917 | -44.79102 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a0ac181d-69fb-332d-a75d-22edca8211d0 | -5.65736 | -42.63632 | 2026-09-21 16:03:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 83ef32d1-5412-3be9-a2d0-f24cab2dec7d | -6.86059 | -44.57432 | 2026-09-21 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| af341fb0-f92c-3ae4-ac6d-c12f5195f952 | -6.83595 | -44.07227 | 2026-09-21 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c3245a6e-291b-3d6a-b3d0-409a7a4e6ead | -6.98486 | -44.70591 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| a3fc6d11-aedc-3eb5-8a95-55a27da1f043 | -6.25074 | -41.65588 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 283.3 |
| 71017800-4ebf-3d60-95b9-a5b8374265d1 | -3.60908 | -42.76418 | 2026-09-21 16:03:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| d3d0b8c3-05b9-3c95-a072-30211b3965f9 | -6.5499 | -44.84299 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 26176e1d-1c50-36ad-8da7-7cd4fa5f7d55 | -7.50779 | -46.2222 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 23d3f920-5d0a-3511-99c3-6d1d14a38230 | -7.40826 | -44.81423 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8e1b8e07-3d3b-35b3-91ed-78d92f69066f | -6.49954 | -45.87642 | 2026-09-21 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 71b2d692-502a-353d-96df-7e00915539f2 | -5.20596 | -49.32433 | 2026-09-21 16:03:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f051a849-8341-3baa-a5b5-1a348b017b53 | -5.90142 | -45.29532 | 2026-09-21 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34b431ca-13a3-3427-b7f6-9157a995d8a8 | -5.22442 | -42.7203 | 2026-09-21 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 63467a1b-0a89-3842-bcfe-e9e4d661e109 | -5.48512 | -45.71756 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d7f2c1f-7583-395a-855f-b830ab5b6708 | -7.05915 | -49.90487 | 2026-09-21 16:03:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 49dcd83d-7eea-3a30-bbae-d321a740cfcb | -6.16881 | -47.5027 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 1cc5b2ac-1252-363b-81ff-1702ade88548 | -7.16329 | -37.71148 | 2026-09-21 16:03:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 297349ce-040a-3ee3-8f7e-01d5b903f425 | -6.17856 | -47.61211 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 200f5952-5e52-3dcd-a061-a81504f00dcc | -8.465 | -48.45781 | 2026-09-21 16:03:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 768c97e5-be21-35c0-84cf-b7ae46cb1cc8 | -7.54253 | -45.20908 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c1521d0e-44f2-375d-82c3-54890b83272b | -6.98049 | -39.89006 | 2026-09-21 16:03:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| ef8b834b-a8c6-3809-b517-bdf4444c8aab | -6.73515 | -44.28139 | 2026-09-21 16:03:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 720fc357-3056-3d05-b3f7-1962857970cf | -5.75735 | -47.28953 | 2026-09-21 16:03:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0bc68957-4f07-3c09-bd59-d37867a9731a | -6.23318 | -45.44138 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 36521ec6-df3f-3e93-bfef-071842462769 | -8.72827 | -49.55495 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| c588def1-e04f-34af-91b7-7fb951a83948 | -3.84 | -41.70428 | 2026-09-21 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 9d6485ee-9ca1-3e57-a569-8f1475830fe2 | -4.21279 | -44.66916 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| d834be33-5988-3680-8d34-a52973792839 | -7.51246 | -46.21854 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e2da19be-2a16-3f92-bb52-fcbd525dec3f | -6.56063 | -45.53437 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 09163e10-5620-3ded-b310-676067b342b6 | -6.93973 | -42.90364 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 32f69c42-95e7-3a32-95b5-9d5eb3c860f6 | -5.34854 | -45.96273 | 2026-09-21 16:03:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README174.md)
